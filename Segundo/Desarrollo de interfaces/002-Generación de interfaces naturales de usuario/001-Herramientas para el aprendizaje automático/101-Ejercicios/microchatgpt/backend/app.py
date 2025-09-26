#!/usr/bin/env python3
# app.py — Minimal Flask backend that proxies chat to Ollama

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

app = Flask(__name__, static_folder=None)
CORS(app)  # Allow local dev from any origin; tighten in production


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    Expects JSON:
    {
      "model": "llama3.1:8b-instruct-q4_0",
      "message": "your prompt",
      "history": [ {"role":"user","content":"..."}, {"role":"assistant","content":"..."} ]
    }
    Returns:
    { "reply": "assistant text", "raw": <ollama raw response> }
    """
    data = request.get_json(force=True) or {}
    model = data.get("model") or "llama3.1:8b-instruct-q4_0"
    message = (data.get("message") or "").strip()
    history = data.get("history") or []

    if not message:
        return jsonify({"error": "message is required"}), 400

    # Build messages array for Ollama chat endpoint
    messages = list(history) + [{"role": "user", "content": message}]

    try:
        r = requests.post(
            f"{OLLAMA_HOST}/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": False,   # keep it simple; you can add streaming later
            },
            timeout=600,
        )
        r.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": f"Ollama request failed: {e}"}), 502

    payload = r.json()
    # Typical shape: { "model": "...", "created_at": "...", "message": {"role":"assistant","content":"..."} }
    reply = (payload.get("message") or {}).get("content", "")

    return jsonify({"reply": reply, "raw": payload})


@app.route("/api/models", methods=["GET"])
def list_models():
    """Return installed models from Ollama (`ollama list`)"""
    try:
        r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=10)
        r.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": f"Ollama request failed: {e}"}), 502
    return jsonify(r.json())


# ---- Optional: serve frontend for convenience (dev use) ----
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    root = os.path.join(os.path.dirname(__file__), "..", "frontend")
    if path == "" or path == "/":
        return send_from_directory(root, "index.html")
    return send_from_directory(root, path)


if __name__ == "__main__":
    # Run: python3 app.py
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)

