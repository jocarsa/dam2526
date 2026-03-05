#!/usr/bin/env python3
import os
import glob
import torch

from datetime import datetime
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
)

from peft import LoraConfig, get_peft_model


# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------
DATA_FOLDER = "entrenamiento"

PRIMARY_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"

OUTPUT_DIR = "./lora-gpu"

MAX_LENGTH = 256
NUM_EPOCHS = 15
LR = 2e-4
BATCH_SIZE = 2
GRAD_ACCUM = 4


def main():
    start_dt = datetime.now()

    print("🚀 Starting GPU training with LoRA")
    print(f"📁 Dataset folder: {DATA_FOLDER}")
    print(f"🧠 Model: {PRIMARY_MODEL}")
    print("-" * 60)

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA GPU not detected.")

    print("✅ CUDA available")
    print("GPU:", torch.cuda.get_device_name(0))

    # ------------------------------------------------------------
    # Load all JSONL files
    # ------------------------------------------------------------
    jsonl_files = sorted(glob.glob(os.path.join(DATA_FOLDER, "*.jsonl")))

    if not jsonl_files:
        raise FileNotFoundError(f"No JSONL files found in {DATA_FOLDER}")

    print("📄 Files found:")
    for f in jsonl_files:
        print("   ", f)

    raw_dataset = load_dataset("json", data_files=jsonl_files, split="train")
    print(f"✅ Loaded {len(raw_dataset)} examples")

    # ------------------------------------------------------------
    # Tokenizer
    # ------------------------------------------------------------
    tokenizer = AutoTokenizer.from_pretrained(PRIMARY_MODEL, use_fast=True)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # ------------------------------------------------------------
    # Model GPU
    # ------------------------------------------------------------
    model = AutoModelForCausalLM.from_pretrained(
        PRIMARY_MODEL,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    try:
        model.enable_input_require_grads()
    except Exception:
        pass

    # ------------------------------------------------------------
    # LoRA
    # ------------------------------------------------------------
    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # ------------------------------------------------------------
    # Dataset formatting
    # ------------------------------------------------------------
    SYSTEM_PROMPT = (
        "Eres un asistente educativo en español que responde de forma clara, precisa y concisa."
    )

    def qa_to_text(example):
        q = str(example.get("question", ""))
        a = str(example.get("answer", ""))

        conv = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": q},
            {"role": "assistant", "content": a},
        ]

        try:
            text = tokenizer.apply_chat_template(
                conv,
                tokenize=False,
                add_generation_prompt=False
            )
        except Exception:
            text = f"SYSTEM: {SYSTEM_PROMPT}\nUSER: {q}\nASSISTANT: {a}\n"

        return {"text": text}

    text_dataset = raw_dataset.map(qa_to_text)

    def tokenize_fn(batch):
        return tokenizer(
            batch["text"],
            truncation=True,
            max_length=MAX_LENGTH,
            padding=False,
        )

    tokenized_dataset = text_dataset.map(
        tokenize_fn,
        batched=True,
        remove_columns=text_dataset.column_names,
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    # ------------------------------------------------------------
    # TrainingArguments GPU
    # ------------------------------------------------------------
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        weight_decay=0.01,
        warmup_steps=25,
        logging_steps=5,
        save_steps=200,
        save_total_limit=1,
        report_to="none",
        fp16=True,
        gradient_checkpointing=True,
        optim="adamw_torch",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
    )

    # ------------------------------------------------------------
    # Train
    # ------------------------------------------------------------
    print("🚂 Training on GPU...")
    train_output = trainer.train()

    print("🏁 Finished")

    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    end_dt = datetime.now()

    print("⏱️ Duration:", end_dt - start_dt)

    metrics = getattr(train_output, "metrics", None)
    if metrics:
        print("📊 Metrics:", metrics)


if __name__ == "__main__":
    main()
