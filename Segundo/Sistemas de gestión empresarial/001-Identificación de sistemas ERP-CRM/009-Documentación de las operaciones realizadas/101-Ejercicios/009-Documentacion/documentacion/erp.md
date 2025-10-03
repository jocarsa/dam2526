📁..
   ├─ 📁anterior
   │  ├─ 📁cabecera
   │  │  ├─ 📄comportamiento.js
   │  │  ├─ 📄estilo.css
   │  │  └─ 📄index.php
   │  ├─ 📁comun
   │  │  ├─ 📄estilo.css
   │  │  ├─ 📄Ubuntu-B.ttf
   │  │  └─ 📄Ubuntu-R.ttf
   │  ├─ 📁crm
   │  │  ├─ 📄comportamiento.js
   │  │  ├─ 📄estilo.css
   │  │  └─ 📄index.php
   │  ├─ 📁escritorio
   │  │  ├─ 📄comportamiento.js
   │  │  ├─ 📄estilo.css
   │  │  └─ 📄index.html
   │  ├─ 📁iniciarsesion
   │  │  ├─ 📄comportamiento.js
   │  │  ├─ 📄estilo.css
   │  │  └─ 📄index.html
   │  ├─ 📁listadodemodulos
   │  │  ├─ 📄comportamiento.js
   │  │  ├─ 📄estilo.css
   │  │  └─ 📄index.php
   │  ├─ 📁plantillas
   │  │  ├─ 📁calendario
   │  │  ├─ 📁fichas
   │  │  ├─ 📁formulario
   │  │  ├─ 📁grafica
   │  │  ├─ 📁kanban
   │  │  │  ├─ 📄comportamiento.js
   │  │  │  ├─ 📄estilo.css
   │  │  │  ├─ 📄index.php
   │  │  │  └─ 📄kanban.json
   │  │  └─ 📁lista
   │  └─ 📄index.php
   ├─ 📁basededatos
   │  └─ 📄instalacion.sql
   ├─ 📁documentacion
   │  ├─ 📁__pycache__
   │  │  ├─ 📄arbol.cpython-312.pyc
   │  │  └─ 📄cabeceras.cpython-312.pyc
   │  ├─ 📄arbol.py
   │  ├─ 📄cabeceras.py
   │  ├─ 📄documentacion.py
   │  └─ 📄erp.md
   ├─ 📁instalador
   │  └─ 📄index.php
   └─ 📁posterior
      ├─ 📁data
      │  └─ 📄kanban.sqlite
      ├─ 📄config.php
      ├─ 📄data_1757686436.json
      ├─ 📄iniciarsesion.php
      ├─ 📄kanban.php
      ├─ 📄listadodemodulos.php
      └─ 📄savekanban.php# 📁 ..
## 📁 anterior

- 📄 [index.php](anterior/index.php)

    ```php
    <?php
  session_start();
  if(!isset($_SESSION['usuario'])){
    header("Location: iniciarsesion/index.html");
    exit;
  }
?>
<!doctype html>
<html lang="es">
  <head>
    <title>ERP Jose Vicente</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="comun/estilo.css">
  </head>
  <body>
    <?php include "cabecera/index.php" ?>
    <?php /*include "listadodemodulos/index.php"*/ ?>
    <?php include "plantillas/kanban/index.php" ?>
  </body>
</html>

    ```
### 📁 cabecera

- 📄 [comportamiento.js](anterior/cabecera/comportamiento.js)

    ```javascript
    
    ```
- 📄 [estilo.css](anterior/cabecera/estilo.css)

    ```css
    #superior{
  background:var(--solido-fondo);
  padding:20px;
  color:var(--solido-frente);
  font-weight:bold;
  display:flex;
  justify-content: space-between;
}
#inferior{
  background:white;
  padding:20px;
  color:black;
  font-weight:bold;
  display:flex;
  justify-content: space-between;
  border-bottom:1px solid var(--solido-fondo);
}
#inferior nav{
  display:flex;
}

    ```
- 📄 [index.php](anterior/cabecera/index.php)

    ```php
    <!-- Módulo cabecera -->

<style>
  <?php include "estilo.css";?>
</style>

<div>
  <header id="superior">
    <nav>
       ☰ Aplicaciones Aplicaciones
    </nav>
    <nav>
      💬 ⏰ JOCARSA A
    </nav>
  </header>
  <header id="inferior">
    <nav>
      Aplicaciones
    </nav>
    <nav>
      <input type="search">
    </nav>
    <nav>
      <div>X de Y</div>
      <div id="paginacion">
      ⏪⏩
      </div>
      <div id="vista">
        🪟​🪟​
      </div>
    </nav>
   </div>
</div>

<script>
  <?php include "comportamiento.js";?>
</script>

<!-- Módulo cabecera -->

    ```
### 📁 comun

- 📄 [estilo.css](anterior/comun/estilo.css)

    ```css
    :root{
  --solido-fondo: steelblue;
  --solido-frente: white;
  --color-primario: steelblue;
  /* Lighter tints */
  --steelblue-100: #f0f6fa;
  --steelblue-200: #d1e3ef;
  --steelblue-300: #a3c7df;
  --steelblue-400: #75abcf;
  /* Darker shades */
  --steelblue-600: #3e74a0;
  --steelblue-700: #355f83;
  --steelblue-800: #2b4a66;
  --steelblue-900: #203549;
}
*{
  padding:0px;
  margin:0px;
}
@font-face {
  font-family: 'Ubuntu';
  src: url('Ubuntu-R.ttf');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'Ubuntu';
  src: url('Ubuntu-B.ttf');
  font-weight: 700;
  font-style: normal;
}

body, html {
  height: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
  font-family: 'Ubuntu', sans-serif;
  background:rgb(240,240,240);
}
button{
  border:0px;
  padding:10px 20px;
  border-radius:5px;
  background:var(--solido-fondo);
  color:var(--solido-frente);
  margin:5px 0px;
}

    ```
- 📄 [Ubuntu-B.ttf](anterior/comun/Ubuntu-B.ttf)

    ```
    [Contenido omitido: archivo mayor de 262144 bytes]
    ```
- 📄 [Ubuntu-R.ttf](anterior/comun/Ubuntu-R.ttf)

    ```
    [Contenido omitido: archivo mayor de 262144 bytes]
    ```
### 📁 crm

- 📄 [comportamiento.js](anterior/crm/comportamiento.js)

    ```javascript
    
    ```
- 📄 [estilo.css](anterior/crm/estilo.css)

    ```css
    
    ```
- 📄 [index.php](anterior/crm/index.php)

    ```php
    <!-- Módulo kanban -->

<style>
  <?php include "estilo.css";?>
</style>

<div id="listadodemodulos">
  <nav>
    <ul>
     
      
     
    </ul>
  </nav>
  <section>
    
   
    
  </section>
</div>

<script>
  <?php include "comportamiento.js";?>
</script>

<!-- Módulo listado de modulo -->

    ```
### 📁 escritorio

- 📄 [comportamiento.js](anterior/escritorio/comportamiento.js)

    ```javascript
    
    ```
- 📄 [estilo.css](anterior/escritorio/estilo.css)

    ```css
    
    ```
- 📄 [index.html](anterior/escritorio/index.html)

    ```html
    <!doctype html>
<html>
  <head>
    <title>
      Iniciar sesión
    </title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="../comun/estilo.css">
    <link rel="stylesheet" href="estilo.css">
  </head>
  <body>
    <main>
      Escritorio
    </main>
    <script src="comportamiento.js"></script>
  </body>
</html>

    ```
### 📁 iniciarsesion

- 📄 [comportamiento.js](anterior/iniciarsesion/comportamiento.js)

    ```javascript
    document.querySelector("button").onclick = function(){
  let usuario = document.querySelector("#usuario").value
  let contrasena = document.querySelector("#contrasena").value

  let objeto = {
    "usuario":usuario,
    "contrasena":contrasena
  }
  fetch("../../posterior/iniciarsesion.php", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(objeto)
    })
    .then(res => res.json())
    .then(result => {
        if (result.success) {
            window.location = "../"
        } else {
            document.querySelector("#estado").textContent = "Error de inicio de sesión";
        }
    })
    .catch(error => {
        console.error(error);
    });
}

    ```
- 📄 [estilo.css](anterior/iniciarsesion/estilo.css)

    ```css
    body{
  background:var(--steelblue-300);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
main{
  width:200px;
  height:200px;
  background:white;
  padding:20px;
  margin:20px;
  margin:auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align:center;
}
main *{
  margin-top:10px;
  width:100%;
  box-sizing:border-box;
  padding:5px;
  border:none;
  border-bottom:1px solid grey;
}
#estado{
  color:red;
}

    ```
- 📄 [index.html](anterior/iniciarsesion/index.html)

    ```html
    <!doctype html>
<html>
  <head>
    <title>
      Iniciar sesión
    </title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="../comun/estilo.css">
    <link rel="stylesheet" href="estilo.css">
  </head>
  <body>
    <main>
      <h1>CRM</h1>
      <input type="text" id="usuario">
      <input type="password" id="contrasena">
      <button>
        Iniciar sesión
      </button>
      <div id="estado"></div>
    </main>
    <script src="comportamiento.js"></script>
  </body>
</html>

    ```
### 📁 listadodemodulos

- 📄 [comportamiento.js](anterior/listadodemodulos/comportamiento.js)

    ```javascript
      // APLICACIONES ////////////////////////////////////////////////////////////////
  fetch("../posterior/listadodemodulos.php?ruta=aplicaciones")
  .then(function(respuesta){
    return respuesta.json();
  })
  .then(function(datos){
    let contenedor = document.querySelector("section")
    datos.forEach(function(aplicacion){
      let articulo = `
           <article>
              <div class="logo">`+aplicacion.icono+`​</div>
              <div class="texto">
                <h3>`+aplicacion.nombre+`​</h3>
                <p>`+aplicacion.descripcion+`​</p>
                <button>Instalar</button>
              </div>
            </article>
        `;
        contenedor.innerHTML += articulo;
    })
  })
  
  // CATEGORIAS ////////////////////////////////////////////////////////////////
  fetch("../posterior/listadodemodulos.php?ruta=categorias")
  .then(function(respuesta){
    return respuesta.json();
  })
  .then(function(datos){
    let contenedor = document.querySelector("ul")
    datos.forEach(function(aplicacion){
      let lista = `
           <li>`+aplicacion.nombre+`</li>
        `;
        contenedor.innerHTML += lista;
    })
  })

    ```
- 📄 [estilo.css](anterior/listadodemodulos/estilo.css)

    ```css
    #listadodemodulos{
  display:flex;
}
#listadodemodulos nav{
  flex:1;
  padding:20px;
  overflow-y:scroll;
}
#listadodemodulos nav ul{
  list-style-type:none;
  padding-left:30px;
}
#listadodemodulos nav ul li{
  padding:10px;
}
#listadodemodulos section{
  flex:4; 
  display: grid;
  grid-template-columns: auto auto auto;
  gap:10px;
}
#listadodemodulos section article{
  background:white;
  min-width:300px;
  width:90%;
  height:100px;
  display: flex;
	flex-direction: row;
	flex-wrap: nowrap;
	justify-content: space-between;
	align-items: center;
	align-content: stretch;
	padding:10px;
	margin:10px;
	border:1px solid var(--solido-fondo);
}
#listadodemodulos section article .logo{
  font-size:40px;
  flex:1;
}
#listadodemodulos section article .texto{

  flex:4;
}


    ```
- 📄 [index.php](anterior/listadodemodulos/index.php)

    ```php
    <!-- Módulo listado de modulos -->

<style>
  <?php include "estilo.css";?>
</style>

<div id="listadodemodulos">
  <nav>
    <ul>
     
      
     
    </ul>
  </nav>
  <section>
    
   
    
  </section>
</div>

<script>
  <?php include "comportamiento.js";?>
</script>

<!-- Módulo listado de modulo -->

    ```
### 📁 plantillas
#### 📁 calendario
#### 📁 fichas
#### 📁 formulario
#### 📁 grafica
#### 📁 kanban

- 📄 [comportamiento.js](anterior/plantillas/kanban/comportamiento.js)

    ```javascript
    /*
  Kanban ampliado + edición inline + modal
  (c) 2025 Jose Vicente Carratala
*/

let estado = null;
let dragged = null;
const CONT = document.querySelector("#kanban");

// ==== Carga inicial ====
(function init() {
  const cache = localStorage.getItem("kanbanJSON");
  if (cache) {
    try { estado = JSON.parse(cache); renderKanban(estado); return; }
    catch(e){ console.warn("LocalStorage inválido, cargo kanban.json"); }
  }
  fetch("kanban.json")
    .then(r => r.json())
    .then(data => { estado = data; renderKanban(estado); })
    .catch(err => console.error("No pude cargar kanban.json:", err));
})();

// ==== Render ====
function renderKanban(datos) {
  CONT.innerHTML = "";
  (datos.columnas || []).forEach((col, idx) => {
    CONT.appendChild(creaColumna(col.nombre, col.tarjetas || [], idx));
  });
  CONT.appendChild(creaTileAddColumna());
}

// Columna
function creaColumna(nombre, tarjetas, colIndex) {
  const col = document.createElement("div");
  col.className = "columna";
  col.dataset.title = nombre;

  const head = document.createElement("div");
  head.className = "col-head";

  const title = document.createElement("div");
  title.className = "col-title";
  title.contentEditable = "true";
  title.textContent = nombre;
  title.spellcheck = false;
  title.addEventListener("keydown", (e) => {
    if (e.key === "Enter") { e.preventDefault(); title.blur(); }
  });
  title.addEventListener("blur", () => {
    const nuevo = title.textContent.trim() || "Sin nombre";
    col.dataset.title = nuevo;
    guardar();
  });

  const actions = document.createElement("div");
  actions.className = "col-actions";

  const btnAddCard = document.createElement("button");
  btnAddCard.className = "icon-btn";
  btnAddCard.title = "Añadir tarjeta";
  btnAddCard.textContent = "＋";
  btnAddCard.onclick = (e)=>{ e.stopPropagation(); promptNuevaTarjeta(col); };

  const btnDelCol = document.createElement("button");
  btnDelCol.className = "icon-btn";
  btnDelCol.title = "Borrar columna";
  btnDelCol.textContent = "🗑";
  btnDelCol.onclick = (e)=>{ e.stopPropagation(); borrarColumna(col); };

  actions.append(btnAddCard, btnDelCol);
  head.append(title, actions);
  col.appendChild(head);

  // DnD columna
  col.addEventListener("dragover", e => e.preventDefault());
  col.addEventListener("dragenter", () => col.classList.add("over"));
  col.addEventListener("dragleave", () => col.classList.remove("over"));
  col.addEventListener("drop", (e) => {
    e.preventDefault();
    col.classList.remove("over");
    if (dragged) { col.appendChild(dragged); guardar(); }
  });

  // Tarjetas
  tarjetas.forEach(t => col.appendChild(creaTarjeta(t.texto, t.color)));

  return col;
}

// Tarjeta
function creaTarjeta(texto, color = "#FFF59D") {
  const card = document.createElement("div");
  card.className = "tarjeta";
  card.draggable = true;

  // Botón borrar
  const del = document.createElement("button");
  del.className = "del";
  del.title = "Borrar tarjeta";
  del.textContent = "✖";
  del.onclick = (e)=>{ e.stopPropagation(); card.remove(); guardar(); };

  // Texto editable
  const p = document.createElement("p");
  p.className = "txt";
  p.textContent = texto || "Nueva tarjeta";
  p.setAttribute("contenteditable","false");
  p.spellcheck = false;

  // Doble clic: activar edición inline
  card.addEventListener("dblclick", () => {
    enableInlineEdit(p);
  });

  // Botón ver (modal)
  const view = document.createElement("button");
  view.className = "view";
  view.title = "Ver/editar en modal";
  view.textContent = "👁️";
  view.onclick = (e)=>{ e.stopPropagation(); openModalFromCard(card); };

  // Color picker
  const picker = document.createElement("input");
  picker.type = "color";
  picker.value = normalizaColor(color);
  picker.onchange = () => { card.style.background = picker.value; guardar(); };

  card.style.background = picker.value;

  // DnD tarjeta
  card.addEventListener("dragstart", e => { dragged = card; e.dataTransfer.effectAllowed = "move"; });
  card.addEventListener("dragend",   () => { dragged = null; });

  // Evita que botones/inputs inicien drag
  [del, view, picker, p].forEach(el=>{
    el.addEventListener("mousedown", e=> e.stopPropagation());
  });

  card.append(del, view, p, picker);
  return card;
}

// Inline edit helpers
function enableInlineEdit(el){
  if (el.getAttribute("contenteditable")==="true") return;
  el.setAttribute("contenteditable","true");
  el.focus();
  // Coloca cursor al final
  document.execCommand && document.execCommand("selectAll", false, null);
  window.getSelection().collapseToEnd();
  const finish = ()=>{
    el.setAttribute("contenteditable","false");
    el.textContent = el.textContent.trim();
    guardar();
  };
  el.addEventListener("blur", finish, { once:true });
  el.addEventListener("keydown", (e)=>{
    if(e.key==="Enter"){ e.preventDefault(); el.blur(); }
    if((e.metaKey||e.ctrlKey) && e.key.toLowerCase()==="s"){ e.preventDefault(); el.blur(); }
  });
}

// Tile “Añadir columna”
function creaTileAddColumna() {
  const wrap = document.createElement("div");
  wrap.className = "add-col-tile";
  const btn = document.createElement("button");
  btn.textContent = "＋ Añadir columna";
  btn.onclick = () => {
    const nombre = (prompt("Nombre de la nueva columna:", "Nueva columna") || "Nueva columna").trim();
    const nueva = creaColumna(nombre, [], (estado?.columnas?.length || 0));
    CONT.insertBefore(nueva, wrap);
    guardar();
  };
  wrap.appendChild(btn);
  return wrap;
}

// Acciones
function promptNuevaTarjeta(columnaEl) {
  const t = prompt("Texto de la tarjeta:", "Nueva tarea");
  if (t === null) return;
  const card = creaTarjeta(t.trim() || "Nueva tarea");
  columnaEl.appendChild(card);
  guardar();
}

function borrarColumna(columnaEl) {
  const nombre = columnaEl.dataset.title || "esta columna";
  if (!confirm(`¿Borrar "${nombre}" y todas sus tarjetas?`)) return;
  columnaEl.remove();
  guardar();
}

// ==== Persistencia ====
function guardar() {
  const nuevo = reconstruyeDesdeDOM(CONT);
  estado = nuevo;
  localStorage.setItem("kanbanJSON", JSON.stringify(nuevo));
  fetch("../../../posterior/savekanban.php", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ source: "kanban-ui", timestamp: Date.now(), data: nuevo })
  })
  .then(r => r.json())
  .then(res => console.log("Guardado:", res))
  .catch(err => console.error("Error guardando:", err));
}

function reconstruyeDesdeDOM(contenedor) {
  const resultado = { columnas: [] };
  const cols = [...contenedor.querySelectorAll(".columna")];
  cols.forEach(col => {
    const nombre = (col.dataset.title || "").trim() || "Sin nombre";
    const tarjetas = [...col.querySelectorAll(".tarjeta")].map(card => {
      const texto = (card.querySelector(".txt")?.textContent || "").trim();
      const inputColor = card.querySelector('input[type="color"]');
      let color = getComputedStyle(card).backgroundColor;
      if (inputColor) color = inputColor.value || color;
      return { texto, color: rgbToHex(color) };
    });
    resultado.columnas.push({ nombre, tarjetas });
  });
  return resultado;
}

// ==== Modal con animación desde la tarjeta ====
function openModalFromCard(card){
  // Colores y estilo desde la tarjeta
  const cardBg = getComputedStyle(card).backgroundColor;
  const cardBorder = getComputedStyle(card).borderColor || "transparent";

  // Crear overlay + shell
  const overlay = document.createElement("div");
  overlay.className = "erp-modal-overlay";
  const shell = document.createElement("div");
  shell.className = "erp-modal-shell";

  // Estilo inicial: clon de la tarjeta
  const rect = card.getBoundingClientRect();
  shell.style.top    = rect.top + "px";
  shell.style.left   = rect.left + "px";
  shell.style.width  = rect.width + "px";
  shell.style.height = rect.height + "px";

  // Inyecta modal con fondo de la tarjeta
  shell.innerHTML = `
    <div class="erp-modal" style="--modal-bg:${cardBg}; --modal-border:${cardBorder};">
      <header>
        <h3>Tarjeta</h3>
        <button class="close" title="Cerrar">✖</button>
      </header>
      <section>
        <textarea class="editor" rows="8">${(card.querySelector(".txt")?.textContent || "").trim()}</textarea>
      </section>
      <footer>
        <button class="primary save">💾 Guardar</button>
        <button class="muted cancel">Cancelar</button>
      </footer>
    </div>
  `;

  overlay.appendChild(shell);
  document.body.appendChild(overlay);

  // Animación: crecer al centro (80% de pantalla)
  requestAnimationFrame(()=>{ shell.classList.add("grow"); });

  // Cerrar con animación inversa hasta la tarjeta
  const close = ()=> {
    shell.classList.remove("grow");              // vuelve a su rect original
    shell.addEventListener("transitionend", ()=> overlay.remove(), { once:true });
  };

  // Acciones
  shell.querySelector(".close").onclick = close;
  shell.querySelector(".cancel").onclick = close;

  shell.querySelector(".save").onclick = ()=>{
    const text = shell.querySelector(".editor").value.trim();
    const p = card.querySelector(".txt");
    p.textContent = text || "Nueva tarjeta";
    guardar();
    close();
  };

  // Teclado
  overlay.addEventListener("keydown", (e)=>{
    if(e.key==="Escape"){ e.preventDefault(); close(); }
    if((e.metaKey||e.ctrlKey) && e.key.toLowerCase()==="s"){ e.preventDefault(); shell.querySelector(".save").click(); }
  });

  shell.querySelector(".editor").focus();
}


// ==== Utils ====
function rgbToHex(rgb) {
  if (typeof rgb !== "string") return rgb;
  const m = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/i);
  if (!m) return rgb;
  const toHex = n => Number(n).toString(16).padStart(2, "0");
  return `#${toHex(m[1])}${toHex(m[2])}${toHex(m[3])}`;
}
function normalizaColor(c) {
  if (!c) return "#FFA500";
  if (c.startsWith("#")) return c;
  const tmp = document.createElement("div");
  tmp.style.color = c;
  document.body.appendChild(tmp);
  const rgb = getComputedStyle(tmp).color;
  document.body.removeChild(tmp);
  return rgbToHex(rgb);
}


    ```
- 📄 [estilo.css](anterior/plantillas/kanban/estilo.css)

    ```css
    /* ==========================================================================
   ERP · Design System (namespaced)
   Usa: <body data-namespace="erp"> … </body>
   ========================================================================== */

/* 1) Reset sutil + tipografía */
[data-namespace="erp"] *, 
[data-namespace="erp"] *::before, 
[data-namespace="erp"] *::after { box-sizing: border-box; }
[data-namespace="erp"] html, 
[data-namespace="erp"] body { height: 100%; }
[data-namespace="erp"] body {
  margin: 0;
  font-family: 'Ubuntu', ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: var(--erp-bg);
  color: var(--erp-fg);
  overflow: hidden; /* app layout */
}

/* 2) Paleta, elevación y motion — namespaced tokens */
[data-namespace="erp"] {
  /* Base */
  --erp-brand: #4682b4;          /* steelblue */
  --erp-brand-600: #3e74a0;
  --erp-brand-700: #355f83;
  --erp-brand-800: #2b4a66;

  --erp-bg: #f3f5f9;
  --erp-bg-2: #ffffff;
  --erp-fg: #1f2937;
  --erp-muted: #6b7280;
  --erp-border: #d6dde8;

  /* Estados */
  --erp-ok: #10b981;
  --erp-warn: #f59e0b;
  --erp-info: #3b82f6;
  --erp-danger: #ef4444;

  /* Sombras y radios */
  --erp-radius: 14px;
  --erp-shadow-1: 0 6px 18px rgba(0,0,0,.08);
  --erp-shadow-2: 0 10px 30px rgba(0,0,0,.12);

  /* Header sólido (compat con tu CSS) */
  --solido-fondo: var(--erp-brand);
  --solido-frente: #ffffff;

  /* Accesibilidad motion */
  --erp-ease: cubic-bezier(.2,.7,.2,1);
  --erp-speed: .18s;
}

/* 2.1) Dark mode (opcional) usando data-theme o preferencia del SO */
@media (prefers-color-scheme: dark) {
  [data-namespace="erp"]:not([data-theme="light"]) {
    --erp-bg: #0f172a;
    --erp-bg-2: #0b1324;
    --erp-fg: #e5e7eb;
    --erp-muted: #94a3b8;
    --erp-border: #243145;
    --solido-fondo: #1e3a8a;
    --solido-frente: #e5e7eb;
    --erp-shadow-1: 0 6px 18px rgba(0,0,0,.45);
    --erp-shadow-2: 0 10px 30px rgba(0,0,0,.6);
  }
}
[data-namespace="erp"][data-theme="light"] { /* fuerza claro */ }
[data-namespace="erp"][data-theme="dark"] {
  --erp-bg: #0f172a;
  --erp-bg-2: #0b1324;
  --erp-fg: #e5e7eb;
  --erp-muted: #94a3b8;
  --erp-border: #243145;
  --solido-fondo: #1e3a8a;
  --solido-frente: #e5e7eb;
}

/* 3) Elementos comunes */
[data-namespace="erp"] a { color: var(--erp-brand); text-decoration: none; }
[data-namespace="erp"] a:hover { text-decoration: underline; }
[data-namespace="erp"] button, 
[data-namespace="erp"] input, 
[data-namespace="erp"] select {
  font: inherit;
}

/* Botones */
[data-namespace="erp"] button {
  border: 0; 
  padding: .7rem 1rem;
  border-radius: 10px;
  background: linear-gradient(135deg, var(--erp-brand), var(--erp-brand-700));
  color: #fff;
  box-shadow: var(--erp-shadow-1);
  cursor: pointer;
  transition: transform var(--erp-speed) var(--erp-ease), box-shadow var(--erp-speed) var(--erp-ease), filter var(--erp-speed);
}
[data-namespace="erp"] button:hover { transform: translateY(-1px); box-shadow: var(--erp-shadow-2); }
[data-namespace="erp"] button:active { transform: translateY(0); filter: saturate(.95); }

/* Inputs */
[data-namespace="erp"] input[type="text"],
[data-namespace="erp"] input[type="password"],
[data-namespace="erp"] input[type="search"],
[data-namespace="erp"] select {
  width: 100%;
  border: 1px solid var(--erp-border);
  background: var(--erp-bg-2);
  color: var(--erp-fg);
  padding: .65rem .8rem;
  border-radius: 10px;
  outline: none;
  transition: box-shadow var(--erp-speed), border-color var(--erp-speed);
}
[data-namespace="erp"] input:focus,
[data-namespace="erp"] select:focus {
  border-color: color-mix(in srgb, var(--erp-brand) 50%, transparent);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--erp-brand) 20%, transparent);
}

/* 4) Cabecera (compat con #superior y #inferior) */
[data-namespace="erp"] #superior {
  background: linear-gradient(135deg, var(--solido-fondo), color-mix(in srgb, var(--solido-fondo) 75%, #0000));
  color: var(--solido-frente);
  padding: 16px 22px;
  display: flex; justify-content: space-between; align-items: center;
  font-weight: 700;
  letter-spacing: .2px;
  box-shadow: var(--erp-shadow-1);
}
[data-namespace="erp"] #superior nav { display: flex; gap: 14px; align-items: center; }

[data-namespace="erp"] #inferior {
  background: var(--erp-bg-2);
  color: var(--erp-fg);
  padding: 12px 18px;
  display: flex; justify-content: space-between; align-items: center;
  border-bottom: 1px solid var(--erp-border);
  position: sticky; top: 0; z-index: 8;
}
[data-namespace="erp"] #inferior nav { display: flex; gap: 14px; align-items: center; }
[data-namespace="erp"] #inferior input[type="search"] {
  min-width: 260px;
  background: color-mix(in srgb, var(--erp-bg-2) 85%, #ffffff 15%);
}

/* Paginación y vista */
[data-namespace="erp"] #paginacion { display:flex; gap:.5rem; align-items:center; font-weight:600; }
[data-namespace="erp"] #vista { display:flex; gap:.35rem; font-size:1.1rem; }

/* 5) Listado de módulos (compat con #listadodemodulos) */
[data-namespace="erp"] #listadodemodulos {
  display: grid; grid-template-columns: 280px 1fr;
  gap: 18px; height: calc(100vh - 120px); /* vista app */
  padding: 18px; 
}
@media (max-width: 900px) {
  [data-namespace="erp"] #listadodemodulos { grid-template-columns: 1fr; height: auto; overflow: visible; }
}

[data-namespace="erp"] #listadodemodulos nav {
  padding: 18px;
  background: var(--erp-bg-2);
  border: 1px solid var(--erp-border);
  border-radius: var(--erp-radius);
  overflow: auto;
  box-shadow: var(--erp-shadow-1);
}
[data-namespace="erp"] #listadodemodulos nav ul { list-style: none; padding-left: 0; margin: 0; }
[data-namespace="erp"] #listadodemodulos nav ul li {
  padding: .6rem .75rem;
  border-radius: 8px;
  cursor: pointer;
  color: var(--erp-fg);
  transition: background var(--erp-speed), transform var(--erp-speed);
}
[data-namespace="erp"] #listadodemodulos nav ul li:hover {
  background: color-mix(in srgb, var(--erp-brand) 10%, var(--erp-bg));
  transform: translateX(2px);
}

[data-namespace="erp"] #listadodemodulos section {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 14px;
  overflow: auto;
  padding-right: 4px;
}
[data-namespace="erp"] #listadodemodulos section article {
  background: var(--erp-bg-2);
  border: 1px solid var(--erp-border);
  border-radius: var(--erp-radius);
  box-shadow: var(--erp-shadow-1);
  display: grid;
  grid-template-columns: 64px 1fr;
  align-items: center;
  min-height: 110px;
  padding: 12px 14px;
  transition: transform var(--erp-speed) var(--erp-ease), box-shadow var(--erp-speed);
}
[data-namespace="erp"] #listadodemodulos section article:hover {
  transform: translateY(-2px);
  box-shadow: var(--erp-shadow-2);
}
[data-namespace="erp"] #listadodemodulos section article .logo {
  font-size: 40px; display: grid; place-items: center;
  width: 56px; height: 56px; border-radius: 14px;
  background: color-mix(in srgb, var(--erp-brand) 12%, var(--erp-bg));
  border: 1px solid color-mix(in srgb, var(--erp-brand) 25%, var(--erp-border));
}
[data-namespace="erp"] #listadodemodulos section article .texto h3 {
  margin: 0 0 .25rem; font-size: 1.05rem;
}
[data-namespace="erp"] #listadodemodulos section article .texto p {
  margin: 0 0 .6rem; color: var(--erp-muted); line-height: 1.35;
}

/* 6) Kanban (compat con #kanban) */
[data-namespace="erp"] #kanban {
  width: 100%; height: calc(100vh - 120px);
  display: flex;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px; padding: 18px;
  overflow: auto;
}
@media (max-width: 1200px) {
  [data-namespace="erp"] #kanban { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 700px) {
  [data-namespace="erp"] #kanban { grid-template-columns: 1fr; }
}

[data-namespace="erp"] #kanban .columna {
  background: var(--erp-bg-2);
  border: 1px solid var(--erp-border);
  border-radius: var(--erp-radius);
  padding: 12px;
  flex:1;
  box-shadow: var(--erp-shadow-1);
  display: flex; flex-direction: column; gap: 10px;
  min-height: 240px;
  transition: border-color var(--erp-speed), box-shadow var(--erp-speed), transform var(--erp-speed);
  position: relative;
}
[data-namespace="erp"] #kanban .columna::before {
  content: attr(data-title);
  position: sticky; top: 0; left: 0; right: 0;
  display: block;
  padding: 6px 8px 10px;
  font-weight: 700; color: var(--erp-muted); text-transform: uppercase; letter-spacing: .4px;
  background: linear-gradient(0deg, transparent 0%, color-mix(in srgb, var(--erp-bg-2) 70%, transparent) 100%);
  backdrop-filter: blur(2px);
  z-index: 2;
}
[data-namespace="erp"] #kanban .columna.over {
  border-color: color-mix(in srgb, var(--erp-brand) 50%, var(--erp-border));
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--erp-brand) 20%, transparent), var(--erp-shadow-1);
  transform: translateY(-2px);
}

[data-namespace="erp"] #kanban .tarjeta {
  background: var(--erp-bg-2);
  border: 1px solid var(--erp-border);
  border-radius: 12px;
  padding: 12px 12px 28px;
  min-height: 90px;
  box-shadow: var(--erp-shadow-1);
  position: relative;
  transition: transform var(--erp-speed), box-shadow var(--erp-speed), border-color var(--erp-speed);
  line-height: 1.35;
  color: var(--erp-fg);
}
[data-namespace="erp"] #kanban .tarjeta:hover {
  transform: translateY(-2px);
  box-shadow: var(--erp-shadow-2);
}
[data-namespace="erp"] #kanban .tarjeta:active { transform: translateY(0); }
[data-namespace="erp"] #kanban .tarjeta input[type="color"]{
  appearance: none;
  border: 1px solid var(--erp-border);
  outline: none;
  width: 18px; height: 18px;
  border-radius: 6px;
  position: absolute; top: 10px; right: 10px;
  background: transparent; padding: 0;
  cursor: pointer;
}

/* 7) Login card (compat con /iniciarsesion) */
[data-namespace="erp"] body.login {
  display: grid; place-items: center;
  background:
    radial-gradient(1200px 600px at 10% -10%, color-mix(in srgb, var(--erp-brand) 15%, transparent), transparent 60%),
    radial-gradient(1000px 500px at 120% 10%, color-mix(in srgb, var(--erp-info) 15%, transparent), transparent 60%),
    var(--erp-bg);
}
[data-namespace="erp"] body.login main {
  width: min(95vw, 360px);
  background: var(--erp-bg-2);
  padding: 22px;
  border-radius: var(--erp-radius);
  box-shadow: var(--erp-shadow-2);
  border: 1px solid var(--erp-border);
  display: grid; gap: 12px; text-align: center;
}
[data-namespace="erp"] body.login h1 { margin: 0; }
[data-namespace="erp"] #estado { color: var(--erp-danger); min-height: 1.2em; }

/* 8) Utilidades */
[data-namespace="erp"] .card {
  background: var(--erp-bg-2);
  border: 1px solid var(--erp-border);
  border-radius: var(--erp-radius);
  box-shadow: var(--erp-shadow-1);
  padding: 14px;
}
[data-namespace="erp"] .muted { color: var(--erp-muted); }
[data-namespace="erp"] .row { display: flex; gap: 10px; align-items: center; }
[data-namespace="erp"] .spacer { flex: 1; }

/* 9) Scrollbar bonita (WebKit y compatibles) */
[data-namespace="erp"] * {
  scrollbar-width: thin;
  scrollbar-color: color-mix(in srgb, var(--erp-brand) 35%, var(--erp-border)) transparent;
}
[data-namespace="erp"] *::-webkit-scrollbar { height: 10px; width: 10px; }
[data-namespace="erp"] *::-webkit-scrollbar-thumb {
  background: color-mix(in srgb, var(--erp-brand) 35%, var(--erp-border));
  border-radius: 10px;
  border: 2px solid transparent;
  background-clip: padding-box;
}
[data-namespace="erp"] *::-webkit-scrollbar-track { background: transparent; }

/* 10) Micro-animaciones de entrada */
@keyframes erp-fade-up {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
[data-namespace="erp"] #listadodemodulos section article,
[data-namespace="erp"] #kanban .tarjeta,
[data-namespace="erp"] #listadodemodulos nav {
  animation: erp-fade-up .28s var(--erp-ease) both;
}
/* === Kanban: cabecera de columna con acciones === */
[data-namespace="erp"] #kanban .col-head {
  display: flex; align-items: center; justify-content: space-between;
  gap: 8px; padding: 4px 2px 8px; position: sticky; top: 0; z-index: 3;
  background: linear-gradient(0deg, transparent 0%, color-mix(in srgb, var(--erp-bg-2) 70%, transparent) 100%);
}
[data-namespace="erp"] #kanban .col-title {
  font-weight: 700; text-transform: uppercase; letter-spacing: .4px;
  outline: none; border-radius: 6px; padding: 2px 6px;
}
[data-namespace="erp"] #kanban .col-actions { display: flex; gap: 6px; }
[data-namespace="erp"] #kanban .icon-btn {
  border: 1px solid var(--erp-border);
  
  border-radius: 8px; padding: 6px 8px; cursor: pointer;
  box-shadow: var(--erp-shadow-1);
  transition: transform var(--erp-speed), box-shadow var(--erp-speed);
}
[data-namespace="erp"] #kanban .icon-btn:hover { transform: translateY(-1px); box-shadow: var(--erp-shadow-2); }

/* === Tarjeta: botón borrar === */
[data-namespace="erp"] #kanban .tarjeta .del {
  position: absolute; top: 10px; left: 10px;
  border: 1px solid var(--erp-border); 
  border-radius: 8px; padding: 4px 6px; cursor: pointer;
}
[data-namespace="erp"] #kanban .tarjeta .txt {
  margin: 0; padding-right: 46px; /* deja hueco al color-picker */
  white-space: pre-wrap;
}

/* === Tile para añadir columna (extremo derecho) === */
[data-namespace="erp"] #kanban .add-col-tile {
  background: var(--erp-bg-2); border: 1px dashed color-mix(in srgb, var(--erp-brand) 40%, var(--erp-border));
  border-radius: var(--erp-radius); display: flex; place-items: center; min-height: 240px;
  box-shadow: var(--erp-shadow-1);
}
[data-namespace="erp"] #kanban .add-col-tile button {
  background: linear-gradient(135deg, var(--erp-brand), var(--erp-brand-700));
  color: #fff; border: 0; border-radius: 12px; padding: .8rem 1rem; cursor: pointer;
  box-shadow: var(--erp-shadow-1);
}
/* (Se mantiene todo tu CSS existente) */

/* === Botones extra en tarjeta === */
[data-namespace="erp"] #kanban .tarjeta .view {
  position: absolute; top: 10px; left: 42px;
  border: 1px solid var(--erp-border);
  border-radius: 8px; padding: 4px 6px; cursor: pointer;
  background: var(--erp-bg-2);
  box-shadow: var(--erp-shadow-1);
}

/* === Texto editable (inline) === */
[data-namespace="erp"] #kanban .tarjeta .txt[contenteditable="true"] {
  outline: 2px solid color-mix(in srgb, var(--erp-brand) 35%, transparent);
  border-radius: 8px;
  padding: 6px;
  background: color-mix(in srgb, var(--erp-brand) 8%, var(--erp-bg-2));
}

/* === Modal overlay + shell animado === */
[data-namespace="erp"] .erp-modal-overlay {
  position: fixed; inset: 0;
  background: color-mix(in srgb, #000 40%, transparent);
  display: grid; place-items: center;
  z-index: 9999;
}

[data-namespace="erp"] .erp-modal-shell {
  position: fixed;
  border-radius: 14px;
  overflow: hidden;
  transition: all .28s var(--erp-ease), transform .28s var(--erp-ease);
  box-shadow: var(--erp-shadow-2);
}

[data-namespace="erp"] .erp-modal-shell.grow {
  /* Estado destino (centrado) */
  top: 50vh; left: 50vw;
  width: min(780px, 92vw);
  height: min(70vh, 92vh);
  transform: translate(-50%,-50%);
}

[data-namespace="erp"] .erp-modal {
  width: 100%; height: 100%;
  display: grid; grid-template-rows: auto 1fr auto;
  background: var(--erp-bg-2);
  border: 1px solid var(--erp-border);
}

[data-namespace="erp"] .erp-modal header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 14px; border-bottom: 1px solid var(--erp-border);
  background: linear-gradient(135deg, var(--erp-brand), var(--erp-brand-700));
  color: #fff;
}
[data-namespace="erp"] .erp-modal header .close {
  border: 1px solid #ffffff55; color: #fff; background: transparent;
  border-radius: 10px; padding: 4px 8px; cursor: pointer;
}

[data-namespace="erp"] .erp-modal section {
  padding: 12px;
}
[data-namespace="erp"] .erp-modal .editor {
  width: 100%; height: 100%;
  resize: none;
  border: 1px solid var(--erp-border);
  border-radius: 12px; padding: 10px;
  background: var(--erp-bg);
  color: var(--erp-fg);
  outline: none;
}
[data-namespace="erp"] .erp-modal .editor:focus {
  border-color: color-mix(in srgb, var(--erp-brand) 50%, transparent);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--erp-brand) 18%, transparent);
}

[data-namespace="erp"] .erp-modal footer {
  display: flex; gap: 10px; justify-content: flex-end;
  padding: 10px 12px; border-top: 1px solid var(--erp-border);
}

[data-namespace="erp"] .erp-modal footer .primary {
  background: linear-gradient(135deg, var(--erp-brand), var(--erp-brand-700));
  color: #fff; border: 0; border-radius: 10px; padding: .6rem .9rem; cursor: pointer;
}
[data-namespace="erp"] .erp-modal footer .muted {
  background: var(--erp-bg-2); color: var(--erp-fg);
  border: 1px solid var(--erp-border); border-radius: 10px; padding: .6rem .9rem; cursor: pointer;
}
/* Overlay opaco de fondo, pero modal no es transparente */
[data-namespace="erp"] .erp-modal-overlay {
  position: fixed; inset: 0;
  background: color-mix(in srgb, #000 45%, transparent); /* oscurece el fondo */
  display: grid; place-items: center;
  z-index: 9999;
}

/* Shell animado */
[data-namespace="erp"] .erp-modal-shell {
  position: fixed;
  border-radius: 14px;
  overflow: hidden;
  transition: top .28s var(--erp-ease), left .28s var(--erp-ease),
              width .28s var(--erp-ease), height .28s var(--erp-ease),
              transform .28s var(--erp-ease), box-shadow .28s var(--erp-ease);
  box-shadow: var(--erp-shadow-2);
}

/* Estado destino: 80% pantalla, centrado */
[data-namespace="erp"] .erp-modal-shell.grow {
  top: 50vh; left: 50vw;
  width: 80vw; height: 80vh;
  transform: translate(-50%, -50%);
}

/* El modal usa los colores de la tarjeta */
[data-namespace="erp"] .erp-modal {
  width: 100%; height: 100%;
  display: grid; grid-template-rows: auto 1fr auto;
  background: var(--modal-bg, var(--erp-bg-2));          /* color de la tarjeta */
  border: 1px solid var(--modal-border, var(--erp-border));
}

/* Header con ligera superposición para contraste */
[data-namespace="erp"] .erp-modal header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 14px; border-bottom: 1px solid var(--erp-border);
  background: color-mix(in srgb, var(--modal-bg, #fff) 75%, #000 25%);
  color: #fff;
}
[data-namespace="erp"] .erp-modal header .close {
  border: 1px solid #ffffff55; color: #fff; background: transparent;
  border-radius: 10px; padding: 4px 8px; cursor: pointer;
}

/* Cuerpo y editor mantienen legibilidad sobre el color de tarjeta */
[data-namespace="erp"] .erp-modal section { padding: 12px; }
[data-namespace="erp"] .erp-modal .editor {
  width: 100%; height: 100%;
  resize: none;
  border: 1px solid var(--erp-border);
  border-radius: 12px; padding: 10px;
  background: color-mix(in srgb, var(--modal-bg, #fff) 80%, #fff 20%);
  color: var(--erp-fg);
  outline: none;
}

/* Footer */
[data-namespace="erp"] .erp-modal footer {
  display: flex; gap: 10px; justify-content: flex-end;
  padding: 10px 12px; border-top: 1px solid var(--erp-border);
  background: color-mix(in srgb, var(--modal-bg, #fff) 85%, #000 15%);
}
[data-namespace="erp"] .erp-modal footer .primary {
  background: linear-gradient(135deg, var(--erp-brand), var(--erp-brand-700));
  color: #fff; border: 0; border-radius: 10px; padding: .6rem .9rem; cursor: pointer;
}
[data-namespace="erp"] .erp-modal footer .muted {
  background: var(--erp-bg-2); color: var(--erp-fg);
  border: 1px solid var(--erp-border); border-radius: 10px; padding: .6rem .9rem; cursor: pointer;
}


    ```
- 📄 [index.php](anterior/plantillas/kanban/index.php)

    ```php
    <!doctype html>
<html>
  <head>
  </head>
  <body data-namespace="erp">
    <style>
      <?php include "estilo.css"; ?>
    </style>
    <div class="plantilla" id="kanban"></div>
    <script>
      <?php include "comportamiento.js"; ?>
    </script>
  </body>
</html>


    ```
- 📄 [kanban.json](anterior/plantillas/kanban/kanban.json)

    ```json
    {
  "columnas": [
    {
      "nombre": "Por hacer",
      "tarjetas": [
        { "texto": "Escribir la propuesta del proyecto", "color": "lightblue" },
        { "texto": "Recopilar requisitos", "color": "orange" }
      ]
    },
    {
      "nombre": "En progreso",
      "tarjetas": [
        { "texto": "Desarrollar la función de inicio de sesión", "color": "yellow" },
        { "texto": "Crear el esquema de la base de datos", "color": "lightgreen" }
      ]
    },
    {
      "nombre": "En revisión",
      "tarjetas": [
        { "texto": "Revisar el código del API", "color": "pink" }
      ]
    },
    {
      "nombre": "Hecho",
      "tarjetas": [
        { "texto": "Configurar el repositorio del proyecto", "color": "gray" },
        { "texto": "Reunión inicial del proyecto", "color": "green" }
      ]
    }
  ]
}


    ```
#### 📁 lista
## 📁 basededatos

- 📄 [instalacion.sql](basededatos/instalacion.sql)

    ```sql
    CREATE TABLE `erp`.`usuarios` (`Identificador` INT NOT NULL AUTO_INCREMENT , `usuario` VARCHAR(50) NOT NULL , `contrasena` VARCHAR(50) NOT NULL , `nombrecompleto` VARCHAR(200) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

INSERT INTO `usuarios` (`Identificador`, `usuario`, `contrasena`, `nombrecompleto`) VALUES (NULL, 'jocarsa', 'jocarsa', 'Jose Vicente Carratalá');

    ```
## 📁 documentacion

- 📄 [arbol.py](documentacion/arbol.py)

    ```python
    import os
from typing import Iterable, Optional, List

def list_entries(path: str, show_hidden: bool = False) -> Iterable[os.DirEntry]:
    with os.scandir(path) as it:
        entries = [e for e in it if show_hidden or not e.name.startswith(".")]
    # Directories first, then files; case-insensitive
    entries.sort(key=lambda e: (e.is_file(), e.name.casefold()))
    return entries

def draw_tree(
    path: str,
    prefix: str = "",
    show_hidden: bool = False,
    max_depth: Optional[int] = None,
    _is_last: bool = True,
    _is_root: bool = True,
) -> List[str]:
    """
    Returns a list of strings that represent the tree of `path`.
    """
    lines = []

    name = os.path.basename(os.path.normpath(path)) or path
    elbow = "└─" if _is_last else "├─"
    icon = "📁"

    # Root line (no elbow for the very first line)
    if _is_root:
        lines.append(f"{icon}{name}")
    else:
        lines.append(f"{prefix}{elbow} {icon}{name}")

    # Stop if depth limit reached
    if max_depth is not None and max_depth <= 0:
        return lines

    child_prefix = prefix + ("   " if _is_last else "│  ")

    try:
        entries = list_entries(path, show_hidden=show_hidden)
    except PermissionError:
        lines.append(f"{child_prefix}└─ ⛔ (permiso denegado)")
        return lines
    except FileNotFoundError:
        lines.append(f"{child_prefix}└─ ⚠️  (no encontrado)")
        return lines

    dirs = [e for e in entries if e.is_dir(follow_symlinks=False)]
    files = [e for e in entries if e.is_file(follow_symlinks=False)]
    others = [e for e in entries if not e.is_dir(follow_symlinks=False) and not e.is_file(follow_symlinks=False)]

    # Recurse directories
    for i, d in enumerate(dirs):
        last = (i == len(dirs) - 1) and not files and not others
        lines.extend(
            draw_tree(
                d.path,
                prefix=child_prefix,
                show_hidden=show_hidden,
                max_depth=None if max_depth is None else max_depth - 1,
                _is_last=last,
                _is_root=False,
            )
        )

    # Print files and others
    all_leaves = files + others
    for i, f in enumerate(all_leaves):
        last = (i == len(all_leaves) - 1)
        leaf_elbow = "└─" if last else "├─"
        icon = "📄" if f.is_file(follow_symlinks=False) else "🔗"
        lines.append(f"{child_prefix}{leaf_elbow} {icon}{f.name}")

    return lines





    ```
- 📄 [cabeceras.py](documentacion/cabeceras.py)

    ~~~python
    import os
from typing import Iterable, Optional, List, Set, Dict

# --- reuse your listing helper ---
def list_entries(path: str, show_hidden: bool = False) -> Iterable[os.DirEntry]:
    with os.scandir(path) as it:
        entries = [e for e in it if show_hidden or not e.name.startswith(".")]
    # Directories first, then files; case-insensitive
    entries.sort(key=lambda e: (e.is_file(), e.name.casefold()))
    return entries

def _md_escape(text: str) -> str:
    """Minimal Markdown escape for headings/links."""
    for ch in ["[", "]", "(", ")", "#", "*", "_", "`"]:
        text = text.replace(ch, f"\\{ch}")
    return text

def _rel_link(from_dir: str, target_path: str) -> str:
    try:
        return os.path.relpath(target_path, start=from_dir)
    except ValueError:
        return os.path.basename(target_path)

def _infer_lang_from_ext(ext: str, mapping: Optional[Dict[str, str]] = None) -> str:
    default_map = {
        "py": "python","js": "javascript","ts": "typescript","tsx": "tsx","jsx": "jsx",
        "json": "json","yml": "yaml","yaml": "yaml","md": "markdown","html": "html","htm":"html",
        "css":"css","php":"php","sql":"sql","sh":"bash","bash":"bash","ini":"","cfg":"","txt":"",
        "xml":"xml","csv":"","toml":"toml","rs":"rust","go":"go","java":"java","kt":"kotlin",
        "c":"c","h":"c","cpp":"cpp","hpp":"cpp","cs":"csharp","rb":"ruby","lua":"lua",
        "r":"r","pl":"perl","swift":"swift","makefile":"make","dockerfile":"dockerfile","env":""
    }
    mp = {**default_map, **(mapping or {})}
    return mp.get(ext.lower(), "")

def _read_text_file_safely(path: str, max_bytes: Optional[int] = 262_144) -> str:
    """
    Read file safely with size cap and robust decoding.
    Try utf-8, utf-8-sig, cp1252, latin-1.
    """
    try:
        if max_bytes is not None and os.path.getsize(path) > max_bytes:
            return f"[Contenido omitido: archivo mayor de {max_bytes} bytes]"
        with open(path, "rb") as fh:
            data = fh.read(None if max_bytes is None else max_bytes)
        for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
            try:
                return data.decode(enc)
            except UnicodeDecodeError:
                continue
        # last resort with replacement
        return data.decode("utf-8", errors="replace")
    except Exception as e:
        return f"[No se pudo leer el archivo: {e}]"

def _fenced_block(content: str, lang: str = "") -> List[str]:
    """Return a Markdown fenced code block; switch to tildes if content has backticks."""
    if "```" in content:
        start = f"~~~{lang}" if lang else "~~~"
        end = "~~~"
        return [start, content, end]
    else:
        start = f"```{lang}" if lang else "```"
        end = "```"
        return [start, content, end]

def draw_markdown(
    path: str,
    show_hidden: bool = False,
    max_depth: Optional[int] = None,
    base_level: int = 1,
    files_as_headings: bool = False,
    link_files: bool = True,
    allowed_extensions: Optional[Set[str]] = None,   # e.g. {"py","js","md"}
    max_file_bytes: Optional[int] = 262_144,         # None = sin límite
    lang_override: Optional[Dict[str, str]] = None,  # ext->lang
    use_emojis: bool = True,                         # Desactívalo si tu visor no es UTF-8
    _current_depth: int = 0,
    _root_dir: Optional[str] = None,
) -> List[str]:
    """
    Markdown directory index with optional inline file contents (code fences).
    """
    lines: List[str] = []
    if _root_dir is None:
        _root_dir = os.path.abspath(path)

    if allowed_extensions is not None:
        allowed_extensions = {ext.lower().lstrip(".") for ext in allowed_extensions}

    # Heading
    level = min(max(1, base_level + _current_depth), 6)
    name = os.path.basename(os.path.normpath(path)) or path
    folder_icon = "📁 " if use_emojis else ""
    lines.append(f'{"#" * level} {folder_icon}{_md_escape(name)}')

    # Depth stop
    if max_depth is not None and _current_depth >= max_depth:
        return lines

    # List entries
    try:
        entries = list_entries(path, show_hidden=show_hidden)
    except PermissionError:
        lines.append("> ⛔ Permiso denegado")
        return lines
    except FileNotFoundError:
        lines.append("> ⚠️  Carpeta no encontrada")
        return lines

    dirs = [e for e in entries if e.is_dir(follow_symlinks=False)]
    files = [e for e in entries if e.is_file(follow_symlinks=False)]
    others = [e for e in entries if not e.is_dir(follow_symlinks=False) and not e.is_file(follow_symlinks=False)]

    file_icon = "📄 " if use_emojis else ""
    link_icon = "🔗 " if use_emojis else ""

    # Files
    if files_as_headings:
        for f in files:
            file_level = min(level + 1, 6)
            display_text = f"{file_icon}{_md_escape(f.name)}"
            rel = _rel_link(_root_dir, f.path) if link_files else None
            display = f"[{display_text}]({_md_escape(rel)})" if rel else display_text
            lines.append(f'{"#" * file_level} {display}')
            ext = os.path.splitext(f.name)[1].lstrip(".").lower()
            if (allowed_extensions is None) or (ext in allowed_extensions):
                lang = _infer_lang_from_ext(ext, lang_override)
                content = _read_text_file_safely(f.path, max_file_bytes)
                lines.extend(_fenced_block(content, lang))
    else:
        if files or others:
            lines.append("")  # blank line before the list
        for f in files:
            title = _md_escape(f.name)
            rel = _rel_link(_root_dir, f.path) if link_files else None
            label = f"[{title}]({_md_escape(rel)})" if rel else title
            lines.append(f"- {file_icon}{label}")
            ext = os.path.splitext(f.name)[1].lstrip(".").lower()
            if (allowed_extensions is None) or (ext in allowed_extensions):
                lang = _infer_lang_from_ext(ext, lang_override)
                content = _read_text_file_safely(f.path, max_file_bytes)
                fenced = _fenced_block(content, lang)
                # Ensure proper nesting: blank line + 4 spaces indentation
                lines.append("")
                lines.extend(["    " + ln if ln else "    " for ln in fenced])

        for o in others:
            lines.append(f"- {link_icon}{_md_escape(o.name)}")

    # Recurse
    for d in dirs:
        lines.extend(
            draw_markdown(
                d.path,
                show_hidden=show_hidden,
                max_depth=max_depth,
                base_level=base_level,
                files_as_headings=files_as_headings,
                link_files=link_files,
                allowed_extensions=allowed_extensions,
                max_file_bytes=max_file_bytes,
                lang_override=lang_override,
                use_emojis=use_emojis,
                _current_depth=_current_depth + 1,
                _root_dir=_root_dir,
            )
        )
    return lines

if __name__ == "__main__":
    root = "."
    md_lines = draw_markdown(
        root,
        show_hidden=False,
        max_depth=None,
        base_level=1,
        files_as_headings=False,
        link_files=True,
        allowed_extensions={"js","py","md","html","css"},  # extensiones permitidas
        max_file_bytes=200_000,
        lang_override=None,
        use_emojis=True,  # pon False si ves mojibake en títulos/listas
    )
    print("\n".join(md_lines))


    ~~~
- 📄 [documentacion.py](documentacion/documentacion.py)

    ```python
    from arbol import draw_tree
from cabeceras import draw_markdown

ruta = "../"


with open("erp.md", "w", encoding="utf-8") as f:
  tree_lines = draw_tree(ruta, show_hidden=False, max_depth=None)
  f.write("\n".join(tree_lines))

  md_lines = draw_markdown(
        ruta,
        show_hidden=False,
        max_depth=None,                  # e.g. 2 to limit depth
        base_level=1,                    # root as H1
        files_as_headings=False,         # True: files as headings; False: bullet list
        link_files=True,
    )
    
  f.write("\n".join(md_lines))

    ```
- 📄 [erp.md](documentacion/erp.md)

    ```markdown
    
    ```
### 📁 \_\_pycache\_\_

- 📄 [arbol.cpython-312.pyc](documentacion/\_\_pycache\_\_/arbol.cpython-312.pyc)

    ```
    Ë
    _Ößh´	  ã                   ó    d dl Z d dlmZmZmZ ddededee j                     fdZ	 	 	 	 	 ddedededee	   d	ed
edee   fdZ
y)é    N)ÚIterableÚOptionalÚListÚpathÚshow_hiddenÚreturnc                 óä    t        j                  | «      5 }|D cg c]"  }|s|j                  j                  d«      r!|$ }}d d d «       j	                  d ¬«       |S c c}w # 1 sw Y   #xY w)Nú.c                 óV    | j                  «       | j                  j                  «       fS )N)Úis_fileÚnameÚcasefold)Úes    õÏ   /var/www/html/dam2526/Segundo/Sistemas de gestiÃ³n empresarial/001-IdentificaciÃ³n de sistemas ERP-CRM/009-DocumentaciÃ³n de las operaciones realizadas/101-Ejercicios/009-Documentacion/documentacion/arbol.pyú<lambda>zlist_entries.<locals>.<lambda>   s     §	¡	£¨Q¯V©V¯_©_Ó->Ð? ó    )Úkey)ÚosÚscandirr   Ú
startswithÚsort)r   r   Úitr   Úentriess        r   Úlist_entriesr      sk    Ü	DÓ	ð ORØ ÖN¡K°q·v±v×7HÑ7HÈÕ7M1ÐNÐN÷Oð LLÑ?LÔ@ØNùò O÷Oð Oús!   A&"A!¾A!ÁA&Á!A&Á&A/ÚprefixÚ	max_depthÚ_is_lastÚ_is_rootc                 óh   g }t         j                  j                  t         j                  j                  | «      «      xs | }|rdnd}d}	|r|j	                  |	 | «       n|j	                  | | d|	 | «       ||dk  r|S ||rdndz   }
	 t        | |¬	«      }|D cg c]  }|j                  d¬«      s| }}|D cg c]  }|j                  d¬«      s| }}|D cg c]*  }|j                  d¬«      r|j                  d¬«      r)|, }}t        |«      D ]Q  \  }}|t        |«      dz
  k(  xr | xr | }|j                  t        |j                  |
||dn|dz
  |d¬«      «       S ||z   }t        |«      D ]V  \  }}|t        |«      dz
  k(  }|rdnd}|j                  d¬«      rdnd}	|j	                  |
 | d|	 |j                   «       X |S # t        $ r |j	                  |
 d
«       |cY S t        $ r |j	                  |
 d«       |cY S w xY wc c}w c c}w c c}w )zF
    Returns a list of strings that represent the tree of `path`.
    u   ââu   ââu   ðú Nr   z   u   â  )r   u   ââ â (permiso denegado)u   ââ â ï¸  (no encontrado)F)Úfollow_symlinksé   )r   r   r   r   r   u   ðu   ð)r   r   ÚbasenameÚnormpathÚappendr   ÚPermissionErrorÚFileNotFoundErrorÚis_dirr   Ú	enumerateÚlenÚextendÚ	draw_treer   )r   r   r   r   r   r   Úlinesr   ÚelbowÚiconÚchild_prefixr   r   ÚdirsÚfilesÚothersÚiÚdÚlastÚ
all_leavesÚfÚ
leaf_elbows                         r   r,   r,      sa   ð Eä77×ÑBGG×,Ñ,¨TÓ2Ó3Ò;°tDÙ H hEØDñ ØvdV_Õ%àx w a¨ v¨d¨VÐ4Ô5ð Ð ¨a¢Øà¡hU°GÑ<LðÜt°Ô=ð ÖB! !§(¡(¸5 (Õ"AAÐBDÐBØÖD1 1§9¡9¸U 9Õ#CQÐDEÐDØ ÖqA¨¯©À¨Õ(GÐPQ×PYÑPYÐjoÐPYÕPpaÐqFÐqô $ò 
1ØSY ]Ñ"Ò@¨E¨	Ò@¸&°jØÜØØ#Ø'Ø"+Ð"3$¸ÀQ¹ØØôõ		
ð
ð JÜ*Ó%ò C1ØS_ qÑ(Ñ(Ù!%X¨8
Ø°5Ô9v¸vØ~ j \°°4°&¸¿¹¸ÐAÕBð	Cð LøôC ò Ø~Ð%BÐCÔDØÜò Ø~Ð%CÐDÔEØðüò CùÚDùÚqsB   ÂG  Â!H%Â9H%ÃH*ÃH*Ã%H/Ã=H/ÄH/Ç H"ÈH"È!H")F)Ú FNTT)r   Útypingr   r   r   ÚstrÚboolÚDirEntryr   Úintr,   © r   r   ú<module>rA      s   ðÛ 	ß +Ñ +ñsð ¨ð ¸(À2Ç;Á;Ñ:Oó ð ØØ#ØØñ@Ø
ð@àð@ð ð@ð }ð	@ð
 ð@ð ð@ð 
#Yô@r   
    ```
- 📄 [cabeceras.cpython-312.pyc](documentacion/\_\_pycache\_\_/cabeceras.cpython-312.pyc)

    ~~~
    Ë
    ÄÞßh-  ã                   óÈ   d dl Z d dlmZmZmZmZmZ d(dededee j                     fdZ
dedefd	Zd
ededefdZd)dedeeeef      defdZd*dedee   defdZd+dededee   fdZ	 	 	 	 	 	 	 	 	 	 	 d,dededee   dedededeee      dee   deeeef      deded ee   dee   fd!Zed"k(  r.d#Z eedddddh d$£d%dd¬&«
      Z ed'j-                  e«      «       yy)-é    N)ÚIterableÚOptionalÚListÚSetÚDictFÚpathÚshow_hiddenÚreturnc                 óä    t        j                  | «      5 }|D cg c]"  }|s|j                  j                  d«      r!|$ }}d d d «       j	                  d ¬«       |S c c}w # 1 sw Y   #xY w)Nú.c                 óV    | j                  «       | j                  j                  «       fS ©N)Úis_fileÚnameÚcasefold)Úes    õÓ   /var/www/html/dam2526/Segundo/Sistemas de gestiÃ³n empresarial/001-IdentificaciÃ³n de sistemas ERP-CRM/009-DocumentaciÃ³n de las operaciones realizadas/101-Ejercicios/009-Documentacion/documentacion/cabeceras.pyú<lambda>zlist_entries.<locals>.<lambda>	   s     §	¡	£¨Q¯V©V¯_©_Ó->Ð? ó    )Úkey)ÚosÚscandirr   Ú
startswithÚsort)r   r	   Úitr   Úentriess        r   Úlist_entriesr      sk    Ü	DÓ	ð ORØ ÖN¡K°q·v±v×7HÑ7HÈÕ7M1ÐNÐN÷Oð LLÑ?LÔ@ØNùò O÷Oð Oús!   A&"A!¾A!ÁA&Á!A&Á&A/Útextc                 ó>    dD ]  }| j                  |d| «      }  | S )z+Minimal Markdown escape for headings/links.)ú[ú]ú(ú)ú#Ú*Ú_ú`ú\)Úreplace)r   Úchs     r   Ú
_md_escaper+      s,    à6ò +Ø||B " R D 	Ó*ð+àKr   Úfrom_dirÚtarget_pathc                 ó¢    	 t         j                  j                  || ¬«      S # t        $ r" t         j                  j	                  |«      cY S w xY w)N)Ústart)r   r   ÚrelpathÚ
ValueErrorÚbasename)r,   r-   s     r   Ú	_rel_linkr3      sB    ð-Üww{°(Ó;Ð;øÜò -Üww×Ñ Ó,Ò,ð-ús    # £(AÁAÚextÚmappingc                 ó:   i ddddddddddd	d	d
dddddddddddddddddddddi ddddddddddddddddd d!d"d"d#d"d$d$d%d$d&d'd(d)d*d*d+d+¥d,d-d.d/dd0¥}i |¥|xs i ¥}|j                  | j                  «       d«      S )1NÚpyÚpythonÚjsÚ
javascriptÚtsÚ
typescriptÚtsxÚjsxÚjsonÚymlÚyamlÚmdÚmarkdownÚhtmlÚhtmÚcssÚphpÚsqlÚshÚbashÚiniÚ ÚcfgÚtxtÚxmlÚcsvÚtomlÚrsÚrustÚgoÚjavaÚktÚkotlinÚcÚhÚcppÚhppÚcsÚcsharpÚrbÚrubyÚluaÚrÚperlÚswiftÚmakeÚ
dockerfile)Úplrc   Úmakefilere   Úenv)ÚgetÚlower)r4   r5   Údefault_mapÚmps       r   Ú_infer_lang_from_extrm      sÝ   ðØhðØ\ðØ*.°ðØ=BÀEðØJOÐQVðàðàfðà%+¨Vðà48¸*ðàEKÈVðàTYÐZ`ðð 	eðð %ðð !& eðð -1°ðð 9?¸vðð GLÈBñð PUÐUWðð Y^Ð^`ðð 	eð	ð "ð	ð $ Fð	ð ,0°ð	ð 8<¸Dð	ð BHÈð	ð PTÐT\ð	ð
 	Cðð
 Cðð
 eðð
 %*¨%ðð
 15°Xðð
 ?CÀ6ðð
 KPÐPUðð 	Cñð  G°vÈ<Ð^`òKð 
,KÐ	+GM rÐ	+BØ66#))+rÓ"Ð"r   Ú	max_bytesc                 ót   	 |(t         j                  j                  | «      |kD  rd| dS t        | d«      5 }|j	                  |dn|«      }ddd«       dD ]  }	 j                  |«      c S  j                  dd¬«      S # 1 sw Y   6xY w# t        $ r Y Bw xY w# t        $ r}d	| d
cY d}~S d}~ww xY w)zh
    Read file safely with size cap and robust decoding.
    Try utf-8, utf-8-sig, cp1252, latin-1.
    Nz%[Contenido omitido: archivo mayor de z bytes]r^   )úutf-8z	utf-8-sigÚcp1252zlatin-1rp   r)   )Úerrorsz[No se pudo leer el archivo: r!   )r   r   ÚgetsizeÚopenÚreadÚdecodeÚUnicodeDecodeErrorÚ	Exception)r   rn   ÚfhÚdataÚencr   s         r   Ú_read_text_file_safelyr|   $   sÕ    ð
4ØÐ ¤R§W¡W§_¡_°TÓ%:¸YÒ%FØ:¸9¸+ÀWÐMÐMÜ$Óð 	E Ø77 9Ð#44¸)ÓDD÷	Eà>ò 	CðØ{{ 3Ó'Ò'ð	ð {{7¨9{Ó5Ð5÷	Eð 	Eûô
 &ò Ùðûô ò 4Ø.¨q¨c°Ð3Õ3ûð4úsc   )B ¬B ¸BÁB ÁBÁ,B Á/B ÂBÂB Â	BÂB ÂBÂB Â	B7Â'B2Â,B7Â2B7ÚcontentÚlangc                 óJ    d| v r|rd| nd}d}|| |gS |rd| nd}d}|| |gS )zOReturn a Markdown fenced code block; switch to tildes if content has backticks.z```z~~~© )r}   r~   r/   Úends       r   Ú_fenced_blockr   8   sL    àÑÙ $#dV¨%ØØw Ð$Ð$á $#dV¨%ØØw Ð$Ð$r   é   TÚ	max_depthÚ
base_levelÚfiles_as_headingsÚ
link_filesÚallowed_extensionsÚmax_file_bytesÚlang_overrideÚ
use_emojisÚ_current_depthÚ	_root_dirc                 óÞ   g }|t         j                  j                  | «      }|,|D ch c]!  }|j                  «       j	                  d«      # }}t        t        d||
z   «      d«      }t         j                  j                  t         j                  j                  | «      «      xs | }|	rdnd}|j                  d|z   d| t        |«       «       ||
|k\  r|S 	 t        | |¬	«      }|D cg c]  }|j                  d¬«      s| }}|D cg c]  }|j                  d¬«      s| }}|D cg c]*  }|j                  d¬«      r|j                  d¬«      r)|, }}|	rdnd}|	rdnd}|r	|D ]  }t        |dz   d«      }| t        |j                   «       }|rt#        ||j                  «      nd}|rd| dt        |«       dn|}|j                  d|z   d| «       t         j                  j%                  |j                   «      d   j	                  d«      j                  «       }|||v sÅt'        ||«      }t)        |j                  |«      }|j+                  t-        ||«      «        n^|s|r|j                  d«       |D ]  }t        |j                   «      }|rt#        ||j                  «      nd}|rd| dt        |«       dn|} |j                  d| |  «       t         j                  j%                  |j                   «      d   j	                  d«      j                  «       }|||v s¯t'        ||«      }t)        |j                  |«      }t-        ||«      }!|j                  d«       |j+                  |!D "cg c]  }"|"rd|"z   nd c}"«        |D ]+  }#|j                  d| t        |#j                   «       «       - |D ]5  }$|j+                  t/        |$j                  |||||||||	|
dz   |¬«      «       7 |S c c}w # t        $ r |j                  d
«       |cY S t        $ r |j                  d«       |cY S w xY wc c}w c c}w c c}w c c}"w )zT
    Markdown directory index with optional inline file contents (code fences).
    Nr   r   é   u   ð rL   r$   ú )r	   u   > â Permiso denegadou   > â ï¸  Carpeta no encontradaF)Úfollow_symlinksu   ð u   ð r    z](r#   z- z    )r	   r   r   r   r   r   r   r   r   r   r   )r   r   Úabspathrj   ÚlstripÚminÚmaxr2   ÚnormpathÚappendr+   r   ÚPermissionErrorÚFileNotFoundErrorÚis_dirr   r   r3   Úsplitextrm   r|   Úextendr   Údraw_markdown)%r   r	   r   r   r   r   r   r   r   r   r   r   Úlinesr4   Úlevelr   Úfolder_iconr   r   ÚdirsÚfilesÚothersÚ	file_iconÚ	link_iconÚfÚ
file_levelÚdisplay_textÚrelÚdisplayr~   r}   ÚtitleÚlabelÚfencedÚlnÚoÚds%                                        r   r   r   C   sO   ð" EØÐÜGGOO DÓ)	àÐ%ØASÖT¸#ciik×0Ñ0°Õ5ÐTÐÐTô Az NÑ2Ó3°QÓ7EÜ77×ÑBGG×,Ñ,¨TÓ2Ó3Ò;°tDÙ''¨RKØ	LLC%K=  + ¬z¸$Ó/?Ð.@ÐAÔBð Ð °9Ò!<ØðÜt°Ô=ð ÖB! !§(¡(¸5 (Õ"AAÐBDÐBØÖD1 1§9¡9¸U 9Õ#CQÐDEÐDØ ÖqA¨¯©À¨Õ(GÐPQ×PYÑPYÐjoÐPYÕPpaÐqFÐqá%¨2IÙ%¨2Iò Øó 
	;AÜU QY¨Ó*JØ'[¬°A·F±FÓ);Ð(<Ð=LÙ2<)I q§v¡vÔ.À$CÙ@C, r¬*°S«/Ð):¸!Ñ<ÈGØLLC *Ñ,Ð-¨Q¨w¨iÐ8Ô9Ü''×"Ñ" 1§6¡6Ó*¨1Ñ-×4Ñ4°SÓ9×?Ñ?ÓACØ"Ð*°Ð7IÒ0IÜ+¨C°Ó?Ü0°·±¸ÓHØ]¨7°DÓ9Ö:ò
	;ñ FØLLÔØó 	OAÜqvvÓ&EÙ2<)I q§v¡vÔ.À$CÙ7:awb¤¨C£Ð 1°Ñ3ÀEØLL2i[¨¨Ð0Ô1Ü''×"Ñ" 1§6¡6Ó*¨1Ñ-×4Ñ4°SÓ9×?Ñ?ÓACØ"Ð*°Ð7IÒ0IÜ+¨C°Ó?Ü0°·±¸ÓHÜ& w°Ó5àRÔ ØÀfÖMÀ©Rf rk°VÑ;ÒMÖNð	Oð ò 	?AØLL2i[¬°A·F±FÓ);Ð(<Ð=Õ>ð	?ð ò 
ØÜØØ'Ø#Ø%Ø"3Ø%Ø#5Ø-Ø+Ø%Ø-°Ñ1Ø#ôõ	
ð
ð" Lùòa Uøô ò ØÐ-Ô.ØÜò ØÐ6Ô7Øðüò CùÚDùÚqùòB NsM   ª&PÃP Ã0QÄQÄQ Ä*Q Ä4Q%ÅQ%ÅQ%ÎQ*
ÐQÐ:QÑQÚ__main__r   >   r9   rB   r7   rF   rD   i@ )	r	   r   r   r   r   r   r   r   r   ú
)Fr   )é   )rL   )FNr   FTNr³   NTr   N)r   Útypingr   r   r   r   r   ÚstrÚboolÚDirEntryr   r+   r3   rm   Úintr|   r   r   Ú__name__ÚrootÚmd_linesÚprintÚjoinr   r   r   ú<module>r¾      sì  ðÛ 	ß 6Õ 6ñsð ¨ð ¸(À2Ç;Á;Ñ:Oó ðSð Só ð-ð -¨#ð -°#ó -ñ
#cð 
#¨H°T¸#¸s¸(±^Ñ,Dð 
#ÐPSó 
#ñ4 ð 4°¸#±ð 4ÈSó 4ñ(	%3ð 	% cð 	%°4¸±9ó 	%ð Ø#ØØ#ØØ-1Ø$+Ø.2ØØØ#ñfØ
ðfàðfð }ðfð ð	fð
 ðfð ðfð !  S¡Ñ*ðfð SMðfð D  c NÑ+ðfð ðfð ðfð }ðfð 
#YófðP zÒØDÙØØØØØØÚ8ØØØôHñ 
$))HÓ
Õð r   
    ~~~
## 📁 instalador

- 📄 [index.php](instalador/index.php)

    ```php
    <?php
/*  -----------------------------------------------------------
    Instalador MySQL (archivo único) - Español
    - Pide host, puerto, base de datos, usuario y contraseña.
    - Verifica conexión y acceso a la BD (ya debe existir).
    - Importa el SQL desde ../basededatos/instalacion.sql
    - Manejo básico de DELIMITER para dumps con procedimientos.
    -----------------------------------------------------------  */

declare(strict_types=1);
ini_set('display_errors', '1');
error_reporting(E_ALL);
@set_time_limit(0);
@ini_set('memory_limit', '1024M');

function e(string $s): string { return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }

function bytes_human(int $bytes): string {
    $u = ['B','KB','MB','GB','TB'];
    $i = 0;
    while ($bytes >= 1024 && $i < count($u)-1) { $bytes /= 1024; $i++; }
    return number_format($bytes, ($i ? 2 : 0), ',', '.') . ' ' . $u[$i];
}

function normalize_sql(string $sql): string {
    // Manejo ligero de DELIMITER (propio del cliente MySQL)
    $lines = preg_split("/(\r\n|\r|\n)/", $sql);
    $out = [];
    foreach ($lines as $line) {
        if (preg_match('/^\s*DELIMITER\s+(.+)\s*$/i', $line)) {
            // Omitimos la línea DELIMITER pero luego convertimos // y $$ al final de línea por ;
            continue;
        }
        $out[] = $line;
    }
    $sql2 = implode("\n", $out);

    foreach (['//', '$$'] as $d) {
        $sql2 = preg_replace('/\s*'.preg_quote($d,'/').'\s*(\r?\n)/', ";\n", $sql2);
        $sql2 = preg_replace('/'.preg_quote($d,'/').'\s*$/', ';', $sql2);
    }
    return $sql2;
}

function import_sql(mysqli $db, string $sql): array {
    $errores = [];
    $ok = 0;

    if (!$db->multi_query($sql)) {
        $errores[] = "Fallo al ejecutar multi_query: " . $db->error;
        return [$ok, $errores];
    }

    do {
        if ($result = $db->store_result()) { $result->free(); }
        $ok++;
        if (!$db->more_results()) { break; }
        if (!$db->next_result()) {
            $errores[] = $db->error ?: 'Error MySQL desconocido';
            break;
        }
    } while (true);

    return [$ok, $errores];
}

$RUTA_SQL_RELATIVA = '../basededatos/instalacion.sql';
$RUTA_SQL = realpath($RUTA_SQL_RELATIVA);
$existeSQL = ($RUTA_SQL !== false && is_file($RUTA_SQL) && is_readable($RUTA_SQL));
$tamanoSQL = $existeSQL ? filesize($RUTA_SQL) : 0;

$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
$isPost = ($method === 'POST');
?>
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Instalador · MySQL</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
    :root { color-scheme: light dark; }
    * { box-sizing: border-box; }
    body {
        margin: 0; padding: 0;
        font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji";
        background:
            radial-gradient(1200px 600px at 10% -10%, #7aa7ff22, transparent 60%),
            radial-gradient(1000px 500px at 120% 10%, #00c2ff22, transparent 60%),
            linear-gradient(180deg, #f7f7fb, #eef1f7);
        min-height: 100vh;
        color: #1e1f22;
    }
    .wrap {
        max-width: 880px; margin: 4rem auto; padding: 0 1rem;
    }
    .card {
        background: rgba(255,255,255,.8);
        backdrop-filter: blur(6px);
        border: 1px solid rgba(0,0,0,.08);
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,.08);
        overflow: hidden;
    }
    .header {
        padding: 1.25rem 1.5rem;
        background: linear-gradient(135deg, #0d6efd, #5b9dff);
        color: #fff;
    }
    .header h1 { margin: 0; font-size: 1.4rem; letter-spacing: .3px; }
    .content { padding: 1.5rem; }
    .desc { color: #444; margin: .25rem 0 1rem; }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
    label { font-weight: 600; font-size: .95rem; display: block; margin-bottom: .35rem; color: #2b2d31; }
    input[type=text], input[type=password] {
        width: 100%; padding: .75rem .9rem; border-radius: 12px;
        border: 1px solid #cfd6e4; outline: none; background: #fff;
        transition: box-shadow .2s, border-color .2s, transform .05s;
    }
    input:focus { border-color: #6aa7ff; box-shadow: 0 0 0 4px #6aa7ff33; }
    .btn {
        display: inline-flex; align-items: center; gap: .5rem;
        margin-top: 1rem; padding: .85rem 1.1rem; border: 0; border-radius: 12px;
        background: linear-gradient(135deg,#0d6efd,#3a86ff); color: #fff; font-weight: 700;
        cursor: pointer; box-shadow: 0 6px 16px rgba(13,110,253,.35);
        transition: transform .05s ease-in-out, box-shadow .2s;
    }
    .btn:hover { box-shadow: 0 10px 24px rgba(13,110,253,.45); }
    .btn:active { transform: translateY(1px); }
    .muted { color: #5b5e66; }
    .badge {
        display: inline-block; padding: .25rem .6rem; border-radius: 999px;
        font-size: .8rem; background: #eef4ff; color: #0d6efd; border: 1px solid #d8e6ff;
    }
    .sql-info { margin: .5rem 0 1rem; font-size: .95rem; }
    .log {
        margin-top: 1rem; padding: 1rem; border-radius: 12px;
        background: #0b12201a; border: 1px solid #cfd6e4; white-space: pre-wrap;
    }
    .ok { color: #1e7e34; font-weight: 700; }
    .err { color: #b22222; font-weight: 700; }
    .note { font-size: .9rem; color: #3c3f44; }
    .footer { padding: 1rem 1.5rem; border-top: 1px solid rgba(0,0,0,.06); background: #fafbfe; color: #555; font-size: .92rem; }
    .steps { display: flex; gap: .5rem; flex-wrap: wrap; margin-bottom: .75rem; }
    .step { padding: .35rem .6rem; border-radius: 8px; background: #f1f5ff; color: #21427a; border: 1px solid #d9e5ff; font-size: .85rem; }
    @media (max-width: 640px){ .grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>
<div class="wrap">
  <div class="card">
    <div class="header">
      <h1>Instalador de Base de Datos</h1>
    </div>
    <div class="content">
      <p class="desc">Este asistente importará el archivo SQL de instalación en una base de datos MySQL existente usando un usuario con permisos suficientes.</p>

      <div class="steps">
        <span class="step">1) Introduce credenciales</span>
        <span class="step">2) Verificación de conexión</span>
        <span class="step">3) Importación del esquema/datos</span>
        <span class="step">4) Resultado</span>
      </div>

      <div class="sql-info">
        <strong>Archivo SQL:</strong>
        <span class="badge"><?= $existeSQL ? 'Encontrado' : 'No encontrado' ?></span><br>
        Ruta: <code><?= e($RUTA_SQL_RELATIVA) ?></code>
        <?php if ($existeSQL): ?>
            <span class="muted"> · Tamaño: <?= e(bytes_human($tamanoSQL)) ?></span>
        <?php endif; ?>
      </div>

      <?php if (!$isPost): ?>
        <form method="post" autocomplete="off">
          <div class="grid">
            <div>
              <label for="host">Host MySQL</label>
              <input id="host" name="host" type="text" value="localhost" required>
            </div>
            <div>
              <label for="port">Puerto (opcional)</label>
              <input id="port" name="port" type="text" inputmode="numeric" pattern="\d*" placeholder="3306">
            </div>
          </div>

          <div class="grid" style="margin-top:.5rem">
            <div>
              <label for="dbname">Nombre de la base de datos</label>
              <input id="dbname" name="dbname" type="text" required>
            </div>
            <div>
              <label for="user">Usuario</label>
              <input id="user" name="user" type="text" required>
            </div>
          </div>

          <div style="margin-top:.5rem">
            <label for="pass">Contraseña</label>
            <input id="pass" name="pass" type="password" required>
          </div>

          <p class="note">La base de datos y el usuario deben existir previamente, y el usuario debe tener permisos para crear tablas, índices y, si procede, triggers/procedimientos.</p>

          <button class="btn" type="submit" <?php if (!$existeSQL) echo 'disabled'; ?>>
            <span>🚀 Ejecutar instalación</span>
          </button>
          <?php if (!$existeSQL): ?>
            <p class="err" style="margin-top:.5rem;">No se puede continuar: el archivo SQL no está disponible o no es legible.</p>
          <?php endif; ?>
        </form>
      <?php else: ?>
        <div class="log">
<?php
    // --- Procesar POST ---
    $host   = trim($_POST['host'] ?? 'localhost');
    $port   = trim($_POST['port'] ?? '');
    $dbname = trim($_POST['dbname'] ?? '');
    $user   = trim($_POST['user'] ?? '');
    $pass   = $_POST['pass'] ?? '';

    $errores = [];
    if ($host === '')   $errores[] = "El host es obligatorio.";
    if ($dbname === '') $errores[] = "El nombre de la base de datos es obligatorio.";
    if ($user === '')   $errores[] = "El usuario es obligatorio.";
    if (!$existeSQL)    $errores[] = "No se encuentra el archivo SQL en '". $RUTA_SQL_RELATIVA ."'.";

    if ($errores) {
        foreach ($errores as $err) {
            echo "• <span class=\"err\">$err</span>\n";
        }
        echo "</div>\n<p><a href=\"".e($_SERVER['PHP_SELF'])."\">Volver</a></p>";
    } else {
        $sqlRaw = @file_get_contents($RUTA_SQL);
        if ($sqlRaw === false || $sqlRaw === '') {
            echo "• <span class=\"err\">No se pudo leer el archivo SQL o está vacío.</span>\n";
            echo "</div>\n<p><a href=\"".e($_SERVER['PHP_SELF'])."\">Volver</a></p>";
        } else {
            echo "• Conectando a MySQL…\n";
            $portNum = ($port !== '' && ctype_digit($port)) ? (int)$port : (int)(ini_get("mysqli.default_port") ?: 3306);
            mysqli_report(MYSQLI_REPORT_OFF);
            $mysqli = @new mysqli($host, $user, $pass, '', $portNum);

            if ($mysqli->connect_errno) {
                echo "• <span class=\"err\">Conexión fallida:</span> ".e($mysqli->connect_error)."\n";
                echo "</div>\n<p><a href=\"".e($_SERVER['PHP_SELF'])."\">Volver</a></p>";
            } else {
                echo "• <span class=\"ok\">Conectado</span> a ".e($host).":".e((string)$portNum)."\n";
                if (!$mysqli->select_db($dbname)) {
                    echo "• <span class=\"err\">No se puede acceder a la base de datos \"".e($dbname)."\":</span> ".e($mysqli->error)."\n";
                    echo "</div>\n<p><a href=\"".e($_SERVER['PHP_SELF'])."\">Volver</a></p>";
                    $mysqli->close();
                } else {
                    echo "• Base de datos seleccionada: <strong>".e($dbname)."</strong>\n";
                    $mysqli->set_charset('utf8mb4');

                    echo "• Leyendo y normalizando SQL (".e(bytes_human(strlen($sqlRaw))).")…\n";
                    $sql = normalize_sql($sqlRaw);

                    if (stripos($sql, 'CREATE DATABASE') !== false || stripos($sql, 'USE ') !== false) {
                        echo "• Nota: el dump contiene <code>CREATE DATABASE</code>/<code>USE</code> y se ejecutarán tal cual.\n";
                    }

                    echo "• Importando… esto puede tardar en archivos grandes.\n";
                    [$okCount, $errImport] = import_sql($mysqli, $sql);

                    if ($errImport) {
                        echo "• <span class=\"err\">Se detectaron errores durante la importación:</span>\n";
                        foreach ($errImport as $i => $er) {
                            echo "   - (#".($i+1).") ".e($er)."\n";
                        }
                    } else {
                        echo "• <span class=\"ok\">Importación completada sin errores reportados.</span>\n";
                    }

                    echo "• Sentencias procesadas (aprox.): ".e((string)$okCount)."\n";
                    $mysqli->close();
                    echo "• <span class=\"ok\">Finalizado.</span>\n";
                    echo "</div>\n<p><strong>Instalación completada.</strong></p>";
                }
            }
        }
    }
?>
      <?php endif; ?>
    </div>
    <div class="footer">
      Consejo: elimina o renombra <code>instalador.php</code> cuando termines para evitar ejecuciones accidentales.
    </div>
  </div>
</div>
</body>
</html>


    ```
## 📁 posterior

- 📄 [config.php](posterior/config.php)

    ```php
    <?php
$host = "localhost";
$dbname = "erp";
$username = "erp";
$password = "erp";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("DB connection failed: " . $e->getMessage());
}


    ```
- 📄 [data\_1757686436.json](posterior/data\_1757686436.json)

    ```json
    {
    "usuario": "jocarsa",
    "contrasena": "jocarsa"
}
    ```
- 📄 [iniciarsesion.php](posterior/iniciarsesion.php)

    ```php
    <?php
  session_start();
// Load DB config
require "config.php";

// Get JSON input
$json = file_get_contents("php://input");
$data = json_decode($json, true);

if (!$data || !isset($data["usuario"]) || !isset($data["contrasena"])) {
    http_response_code(400);
    echo json_encode(["success" => false, "message" => "Invalid input"]);
    exit;
}

$usuario = $data["usuario"];
$contrasena = $data["contrasena"];

// Prepare query
$stmt = $pdo->prepare("SELECT * FROM usuarios WHERE usuario = :usuario AND contrasena = :contrasena");
$stmt->execute([
    ":usuario" => $usuario,
    ":contrasena" => $contrasena
]);

$user = $stmt->fetch(PDO::FETCH_ASSOC);

// Return true/false
if ($user) {
  $_SESSION['usuario'] = $user["nombrecompleto"];
    echo json_encode(["success" => true, "nombrecompleto" => $user["nombrecompleto"]]);
} else {
    echo json_encode(["success" => false]);
}


    ```
- 📄 [kanban.php](posterior/kanban.php)

    ```php
    <?php
/**
 * JsonSqliteBridge (PHP)
 * ----------------------
 * Convierte JSON <-> SQLite de forma recursiva.
 *
 * Reglas base:
 *  - Cada CLAVE del objeto raíz del JSON es una TABLA TOP-LEVEL.
 *  - Las subestructuras (dict/list) se materializan como tablas hijas con FK al padre.
 *  - Las listas de escalares se almacenan como (parent_id, idx, valor).
 *
 * Diferencias/ajustes para SQLite:
 *  - Tipos: bool -> INTEGER, int -> INTEGER, float -> REAL, resto -> TEXT.
 *  - 'Identificador' INTEGER PRIMARY KEY AUTOINCREMENT.
 *  - PRAGMA foreign_keys=ON.
 *  - 'loadFromArray' crea SIEMPRE una BD nueva (borra archivo si existe).
 */

// --- Clase auxiliar de definición de tabla (fuera de JsonSqliteBridge) ---
class TableDef {
    public string $name;
    public ?string $parent;   // nombre tabla padre o null
    public ?string $relname;  // campo en el padre que relaciona con esta tabla
    public string  $kind;     // 'dict' | 'list_scalar'
    public array   $columns = [];  // dict: col => tipo SQL
    public array   $children = []; // nombres de tablas hijas

    public function __construct(string $name, ?string $parent, ?string $relname, string $kind) {
        $this->name   = $name;
        $this->parent = $parent;
        $this->relname= $relname;
        $this->kind   = $kind;
    }
}

class JsonSqliteBridge
{
    // Estado de inferencia (para 'write')
    private array $tables = [];      // name -> TableDef
    private array $edges  = [];      // [ [parent, child], ... ]

    // ============ Helpers de nombre / tipos ============
    private static function ident(string $name): string {
        $name = trim(mb_strtolower($name));
        $name = preg_replace('/[^a-z0-9_]+/u', '_', $name);
        $name = preg_replace('/_+/', '_', $name);
        $name = trim($name, '_');
        if ($name === '') $name = 'col';
        if (preg_match('/^\d/', $name)) $name = 'n_' . $name;
        if (in_array($name, ['index','key','primary','value','table'])) $name = '_' . $name;
        return $name;
    }

    private static function joinPath(string ...$parts): string {
        $clean = array_filter(array_map([self::class, 'ident'], $parts), fn($p) => $p !== '');
        return self::ident(implode('_', $clean));
    }

    private static function sqlScalarType(mixed $v): string {
        if (is_bool($v))  return 'INTEGER';
        if (is_int($v))   return 'INTEGER';
        if (is_float($v)) return 'REAL';
        return 'TEXT';
    }

    private static function mergeType(string $a, string $b): string {
        if ($a === $b) return $a;
        $pair = [$a => true, $b => true];
        if (isset($pair['TEXT'])) return 'TEXT';
        if (isset($pair['INTEGER']) && isset($pair['REAL'])) return 'REAL';
        return 'TEXT';
    }

    // ============ Modelo de tabla ============
    private function ensureTable(string $name, ?string $parent = null, ?string $relname = null, string $kind='dict'): object {
        $tname = self::ident($name);
        if (!isset($this->tables[$tname])) {
            $this->tables[$tname] = new TableDef($tname, $parent, $relname, $kind);
        } else {
            if ($this->tables[$tname]->kind === 'list_scalar' && $kind === 'dict') {
                $this->tables[$tname]->kind = 'dict';
            }
        }
        if ($parent) {
            $p = self::ident($parent);
            $this->edges[] = [$p, $tname];
            if (!in_array($tname, $this->tables[$p]->children, true)) {
                $this->tables[$p]->children[] = $tname;
            }
        }
        return $this->tables[$tname];
    }

    // ============ Inferencia recursiva ============
    private function inferValue(string $pathTable, mixed $value, ?string $parentTable, ?string $relname): void {
        if (is_array($value) && self::isAssoc($value)) {
            // dict
            $t = $this->ensureTable($pathTable, $parentTable, $relname, 'dict');
            foreach ($value as $k => $v) {
                if (is_array($v) && (self::isAssoc($v) || count($v) > 0)) {
                    // dict o list
                    $this->inferValue(self::joinPath($pathTable, (string)$k), $v, $t->name, (string)$k);
                } else {
                    $col = self::ident((string)$k);
                    $tt = self::sqlScalarType($v);
                    $t->columns[$col] = isset($t->columns[$col]) ? self::mergeType($t->columns[$col], $tt) : $tt;
                }
            }
        } elseif (is_array($value)) {
            // list
            $elemKind = 'scalar';
            foreach ($value as $el) { $elemKind = (is_array($el) && self::isAssoc($el)) ? 'dict' : 'scalar'; break; }
            if ($elemKind === 'dict') {
                $t = $this->ensureTable($pathTable, $parentTable, $relname, 'dict');
                foreach ($value as $el) {
                    if (!is_array($el) || !self::isAssoc($el)) continue;
                    foreach ($el as $k => $v) {
                        if (is_array($v) && (self::isAssoc($v) || count($v) > 0)) {
                            $this->inferValue(self::joinPath($pathTable, (string)$k), $v, $t->name, (string)$k);
                        } else {
                            $col = self::ident((string)$k);
                            $tt = self::sqlScalarType($v);
                            $t->columns[$col] = isset($t->columns[$col]) ? self::mergeType($t->columns[$col], $tt) : $tt;
                        }
                    }
                }
            } else {
                $this->ensureTable($pathTable, $parentTable, $relname, 'list_scalar');
            }
        } else {
            // escalar en raíz => tabla con una columna 'valor'
            if ($parentTable === null) {
                $t = $this->ensureTable($pathTable, null, $relname, 'dict');
                $t->columns['valor'] = isset($t->columns['valor'])
                    ? self::mergeType($t->columns['valor'], self::sqlScalarType($value))
                    : self::sqlScalarType($value);
            }
        }
    }

    // ============ Topología ============
    private function topoTables(): array {
        $indeg = [];
        $graph = [];
        foreach ($this->edges as [$p, $c]) {
            $graph[$p] ??= [];
            $graph[$p][] = $c;
            $indeg[$c] = ($indeg[$c] ?? 0) + 1;
            $indeg[$p] = $indeg[$p] ?? 0;
        }
        foreach ($this->tables as $tname => $_) {
            $indeg[$tname] = $indeg[$tname] ?? 0;
        }
        $q = [];
        foreach ($indeg as $t => $d) if ($d === 0) $q[] = $t;
        $out = []; $seen = [];
        while ($q) {
            $u = array_shift($q);
            if (isset($seen[$u])) continue;
            $seen[$u] = true;
            $out[] = $u;
            foreach ($graph[$u] ?? [] as $v) {
                $indeg[$v]--;
                if ($indeg[$v] === 0) $q[] = $v;
            }
        }
        foreach ($this->tables as $t => $_) if (!isset($seen[$t])) $out[] = $t;
        return $out;
    }

    // ============ SQLite ============
    private static function newPdo(string $dbPath): PDO {
        $dsn = "sqlite:" . $dbPath;
        $pdo = new PDO($dsn);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->exec("PRAGMA foreign_keys = ON;");
        $pdo->exec("PRAGMA journal_mode = WAL;");
        $pdo->exec("PRAGMA synchronous = NORMAL;");
        return $pdo;
    }

    private static function resetDatabaseFile(string $dbPath): void {
        if (file_exists($dbPath)) {
            @unlink($dbPath);
        }
        // SQLite crea el archivo al abrir la conexión
    }

    // ============ DDL ============
    private function createAll(PDO $pdo): void {
        $order = $this->topoTables();

        // Eliminamos si existiera (por robustez en reintentos)
        foreach (array_reverse($order) as $t) {
            $pdo->exec("DROP TABLE IF EXISTS \"$t\";");
        }

        foreach ($order as $tname) {
            $t = $this->tables[$tname];

            $cols = ['"Identificador" INTEGER PRIMARY KEY AUTOINCREMENT'];
            if ($t->parent) {
                $cols[] = "\"{$t->parent}_id\" INTEGER NOT NULL";
            }
            if ($t->kind === 'dict') {
                foreach ($t->columns as $c => $typ) {
                    $cols[] = "\"".self::ident($c)."\" $typ";
                }
            } else {
                // list_scalar
                $cols[] = '"idx" INTEGER NOT NULL';
                $cols[] = '"valor" TEXT';
            }

            $fk = '';
            if ($t->parent) {
                $fk = " ,FOREIGN KEY (\"{$t->parent}_id\") REFERENCES \"{$t->parent}\"(\"Identificador\") ON DELETE CASCADE ON UPDATE CASCADE";
            }

            $ddl = "CREATE TABLE \"$tname\" ( ".implode(", ", $cols)." $fk );";
            $pdo->exec($ddl);

            // Índice para FK (recomendable)
            if ($t->parent) {
                $pdo->exec("CREATE INDEX IF NOT EXISTS \"idx_{$tname}_{$t->parent}_id\" ON \"$tname\" (\"{$t->parent}_id\");");
            }
        }
    }

    // ============ INSERT ============
    private function insertListScalar(PDO $pdo, TableDef $tdef, mixed $value, ?int $parentId): void {
        if (!is_array($value) || self::isAssoc($value)) $value = [$value];
        $sql = "INSERT INTO \"{$tdef->name}\" (\"{$tdef->parent}_id\",\"idx\",\"valor\") VALUES (?,?,?)";
        $stmt = $pdo->prepare($sql);
        $i = 0;
        foreach ($value as $el) {
            if (is_array($el)) {
                $val = json_encode($el, JSON_UNESCAPED_UNICODE);
            } else {
                $val = $el;
            }
            $stmt->execute([$parentId, $i, $val]);
            $i++;
        }
    }

    private function insertDictRow(PDO $pdo, TableDef $tdef, array $data, ?int $parentId): int {
        $cols = [];
        $vals = [];
        $place = [];

        foreach (array_keys($tdef->columns) as $c) {
            $cols[] = "\"".self::ident($c)."\"";
            $v = $data[$c] ?? null;
            if (is_array($v)) $v = null; // las estructuras anidadas van a tablas hijas
            $vals[] = $v;
            $place[] = '?';
        }
        if ($tdef->parent) {
            array_unshift($cols, "\"{$tdef->parent}_id\"");
            array_unshift($vals, $parentId);
            array_unshift($place, '?');
        }

        if (count($cols) > 0) {
            $sql = "INSERT INTO \"{$tdef->name}\" (".implode(",", $cols).") VALUES (".implode(",", $place).")";
            $stmt = $pdo->prepare($sql);
            $stmt->execute($vals);
        } else {
            // tabla sin columnas (salvo Identificador y posible FK)
            if ($tdef->parent) {
                $sql = "INSERT INTO \"{$tdef->name}\" (\"{$tdef->parent}_id\") VALUES (?)";
                $stmt = $pdo->prepare($sql);
                $stmt->execute([$parentId]);
            } else {
                $pdo->exec("INSERT INTO \"{$tdef->name}\" DEFAULT VALUES;");
            }
        }

        $newId = (int)$pdo->lastInsertId();

        // hijos
        foreach ($data as $k => $v) {
            if (!is_array($v) || (!self::isAssoc($v) && count($v) === 0)) {
                continue;
            }
            $childName = self::joinPath($tdef->name, (string)$k);
            $child = $this->tables[$childName] ?? null;
            if ($child === null) {
                if (self::isAssoc($v)) {
                    $child = $this->ensureTable($childName, $tdef->name, (string)$k, 'dict');
                    $this->insertDictRow($pdo, $child, [], $newId);
                }
                continue;
            }
            if ($child->kind === 'dict') {
                if (self::isAssoc($v)) {
                    $this->insertDictRow($pdo, $child, $v, $newId);
                } else {
                    foreach ($v as $el) {
                        if (is_array($el) && self::isAssoc($el)) {
                            $this->insertDictRow($pdo, $child, $el, $newId);
                        }
                    }
                }
            } else {
                $this->insertListScalar($pdo, $child, $v, $newId);
            }
        }
        return $newId;
    }

    // ============ API WRITE ============
    public function loadFromJsonFile(string $jsonPath, string $dbPath): bool {
        $root = json_decode(file_get_contents($jsonPath), true);
        if (!is_array($root) || !self::isAssoc($root)) {
            throw new InvalidArgumentException("El JSON raíz debe ser un objeto: cada clave es una tabla padre top-level.");
        }
        return $this->loadFromArray($root, $dbPath);
    }

    public function loadFromArray(array $root, string $dbPath): bool {
        if (!self::isAssoc($root)) {
            throw new InvalidArgumentException("El JSON raíz debe ser un objeto.");
        }

        // Inferencia
        $this->tables = [];
        $this->edges  = [];
        foreach ($root as $topKey => $topVal) {
            $topTable = self::ident((string)$topKey);
            if (is_array($topVal) && !self::isAssoc($topVal)) {
                foreach ($topVal as $el) {
                    $this->inferValue($topTable, $el, null, null);
                }
            } else {
                $this->inferValue($topTable, $topVal, null, null);
            }
        }

        // Nueva BD
        self::resetDatabaseFile($dbPath);
        $pdo = self::newPdo($dbPath);

        // Crear esquema
        $this->createAll($pdo);

        // Insertar datos
        $pdo->beginTransaction();
        try {
            foreach ($root as $topKey => $topVal) {
                /** @var TableDef $topTable */
                $topTable = $this->tables[self::ident((string)$topKey)];
                if (is_array($topVal) && !self::isAssoc($topVal)) {
                    foreach ($topVal as $el) {
                        $row = (is_array($el) && self::isAssoc($el)) ? $el : ['valor' => $el];
                        $this->insertDictRow($pdo, $topTable, $row, null);
                    }
                } elseif (is_array($topVal) && self::isAssoc($topVal)) {
                    $this->insertDictRow($pdo, $topTable, $topVal, null);
                } else {
                    $this->insertDictRow($pdo, $topTable, ['valor' => $topVal], null);
                }
            }
            $pdo->commit();
        } catch (Throwable $e) {
            $pdo->rollBack();
            throw $e;
        }

        return true;
    }

    // ============ API READ ============
    public function dumpToArray(string $dbPath): array {
        if (!file_exists($dbPath)) {
            throw new RuntimeException("No existe la base de datos: $dbPath");
        }
        $pdo = self::newPdo($dbPath);

        // Tablas
        $tables = [];
        $res = $pdo->query("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;");
        while ($row = $res->fetch(PDO::FETCH_ASSOC)) $tables[] = $row['name'];
        if (!$tables) throw new RuntimeException("No hay tablas en la base de datos.");

        // Columnas
        $tableColumns = [];
        foreach ($tables as $t) {
            $tableColumns[$t] = [];
            $stmt = $pdo->query("PRAGMA table_info(\"$t\");");
            while ($r = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $tableColumns[$t][] = $r['name'];
            }
        }

        // FKs
        $parentOf = [];
        $fkColOfChild = [];
        $childrenOf = [];
        foreach ($tables as $t) {
            $childrenOf[$t] = $childrenOf[$t] ?? [];
        }
        foreach ($tables as $t) {
            $fk = $pdo->query("PRAGMA foreign_key_list(\"$t\");");
            while ($r = $fk->fetch(PDO::FETCH_ASSOC)) {
                $parent   = $r['table'];
                $childCol = $r['from'];   // p.ej. parent_id
                $parentOf[$t] = $parent;
                $fkColOfChild[$t] = $childCol;
                $childrenOf[$parent][] = $t;
            }
        }

        $rootTables = array_values(array_filter($tables, fn($t) => !isset($parentOf[$t])));

        // Todas las filas
        $allRows = [];
        foreach ($tables as $t) {
            $stmt = $pdo->query("SELECT * FROM \"$t\"");
            $allRows[$t] = $stmt->fetchAll(PDO::FETCH_ASSOC);
        }

        // Index por (child, parent_id)
        $childRowsByParent = [];
        foreach ($parentOf as $child => $parent) {
            $fk = $fkColOfChild[$child] ?? null;
            if (!$fk) continue;
            foreach ($allRows[$child] as $row) {
                $pid = $row[$fk] ?? null;
                if ($pid === null) continue;
                $key = $child."|".$pid;
                $childRowsByParent[$key] ??= [];
                $childRowsByParent[$key][] = $row;
            }
        }

        $buildNode = function(string $table, array $row) use (&$buildNode, $tableColumns, $fkColOfChild, $childrenOf, $childRowsByParent): array {
            $cols = $tableColumns[$table];
            $fkCol = $fkColOfChild[$table] ?? null;

            // columnas escalares (sin Identificador, idx, valor, ni FK)
            $scalarCols = [];
            foreach ($cols as $c) {
                if ($c === 'Identificador' || $c === 'idx' || $c === 'valor') continue;
                if ($fkCol !== null && $c === $fkCol) continue;
                $scalarCols[] = $c;
            }

            $node = [];
            foreach ($scalarCols as $c) {
                $node[$c] = $row[$c] ?? null;
            }

            foreach ($childrenOf[$table] ?? [] as $child) {
                $relField = self::childFieldName($table, $child);
                $childCols = array_flip($tableColumns[$child]);
                $key = $child."|".$row['Identificador'];
                $rowsChild = $childRowsByParent[$key] ?? [];
                if (!$rowsChild) continue;

                if (isset($childCols['idx']) && isset($childCols['valor'])) {
                    // list_scalar
                    usort($rowsChild, fn($a,$b) => ($a['idx'] ?? 0) <=> ($b['idx'] ?? 0));
                    $seq = [];
                    foreach ($rowsChild as $rc) $seq[] = $rc['valor'];
                    $node[$relField] = $seq;
                } else {
                    if (count($rowsChild) === 1) {
                        $node[$relField] = $buildNode($child, $rowsChild[0]);
                    } else {
                        $tmp = [];
                        foreach ($rowsChild as $rc) $tmp[] = $buildNode($child, $rc);
                        $node[$relField] = $tmp;
                    }
                }
            }
            return $node;
        };

        $result = [];
        foreach ($rootTables as $rt) {
            $rows = $allRows[$rt];
            usort($rows, fn($a,$b) => ((int)$a['Identificador']) <=> ((int)$b['Identificador']));
            $arr = [];
            foreach ($rows as $r) $arr[] = $buildNode($rt, $r);
            $result[$rt] = $arr;
        }

        return $result;
    }

    public function dumpToJsonFile(string $dbPath, string $outputPath): array {
        $arr = $this->dumpToArray($dbPath);
        file_put_contents($outputPath, json_encode($arr, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
        return $arr;
    }

    // ============ utils ============
    private static function isAssoc(array $a): bool {
        if ($a === []) return false; // tratamos [] como lista vacía
        return array_keys($a) !== range(0, count($a)-1);
    }

    private static function childFieldName(string $parent, string $child): string {
        $prefix = $parent . "_";
        if (function_exists('str_starts_with')) {
            if (str_starts_with($child, $prefix)) {
                return substr($child, strlen($prefix));
            }
        } else {
            if (substr($child, 0, strlen($prefix)) === $prefix) {
                return substr($child, strlen($prefix));
            }
        }
        return $child;
    }
}


    ```
- 📄 [listadodemodulos.php](posterior/listadodemodulos.php)

    ```php
    <?php
header('Content-Type: application/json');

if (isset($_GET['ruta']) && $_GET['ruta'] == "categorias") {
    require "config.php";

    // Prepare and execute query
    $stmt = $pdo->prepare("SELECT * FROM categorias_aplicaciones");
    $stmt->execute();

    // Fetch all results as associative array
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Return as JSON
    echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
}

if (isset($_GET['ruta']) && $_GET['ruta'] == "aplicaciones") {
    require "config.php";

    // Prepare and execute query
    $stmt = $pdo->prepare("SELECT * FROM aplicaciones");
    $stmt->execute();

    // Fetch all results as associative array
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Return as JSON
    echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
}
?>


    ```
- 📄 [savekanban.php](posterior/savekanban.php)

    ```php
    <?php
// save_kanban.php
header('Content-Type: application/json; charset=utf-8');

try {
  // 1) Leer body
  $raw = file_get_contents('php://input');
  if ($raw === false) throw new RuntimeException("No se pudo leer el body.");
  $payload = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);

  if (!isset($payload['data']) || !is_array($payload['data'])) {
    throw new InvalidArgumentException("Falta 'data' o no es un objeto/array JSON.");
  }

  // 2) Cargar la clase (ajusta la ruta si procede)
  require_once __DIR__ . '/kanban.php';

  // 3) Instanciar bridge y guardar a SQLite
  $bridge = new JsonSqliteBridge();

  // Ruta de la BD. Si quieres “histórico por fecha”, cámbialo por un nombre con timestamp.
  $dbDir = __DIR__ . '/data';
  if (!is_dir($dbDir)) { mkdir($dbDir, 0775, true); }

  // Opción A: sobreescribir siempre el mismo archivo
  $dbPath = $dbDir . '/kanban.sqlite';

  // Opción B (histórico): descomenta
  // $dbPath = $dbDir . '/kanban_' . date('Ymd_His') . '.sqlite';

  // El método crea SIEMPRE una BD nueva (borra si existe)
  $bridge->loadFromArray($payload['data'], $dbPath);

  // 4) (Opcional) Devolver el JSON reconstruido para verificar round-trip
  $roundtrip = $bridge->dumpToArray($dbPath);

  echo json_encode([
    'ok' => true,
    'message' => 'Kanban guardado en SQLite correctamente.',
    'db' => basename($dbPath),
    'tables' => array_keys($roundtrip),
  ], JSON_UNESCAPED_UNICODE);

} catch (Throwable $e) {
  http_response_code(400);
  echo json_encode([
    'ok' => false,
    'error' => $e->getMessage(),
    'trace' => (ini_get('display_errors') ? $e->getTraceAsString() : null)
  ], JSON_UNESCAPED_UNICODE);
}


    ```
### 📁 data

- 📄 [kanban.sqlite](posterior/data/kanban.sqlite)

    ```
    SQLite format 3   @                                                                     .v   l 2l                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        O/;indexidx_columnas_tarjetas_columnas_idcolumnas_tarjetasCREATE INDEX "idx_columnas_tarjetas_columnas_id" ON "columnas_tarjetas" ("columnas_id")*//tablecolumnas_tarjetascolumnas_tarjetasCREATE TABLE "columnas_tarjetas" ( "Identificador" INTEGER PRIMARY KEY AUTOINCREMENT, "columnas_id" INTEGER NOT NULL, "texto" TEXT, "color" TEXT  ,FOREIGN KEY ("columnas_id") REFERENCES "columnas"("Identificador") ON DELETE CASCADE ON UPDATE CASCADE )P++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)zGtablecolumnascolumnasCREATE TABLE "columnas" ( "Identificador" INTEGER PRIMARY KEY AUTOINCREMENT, "nombre" TEXT  )   ¼ òßÊ¼                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Hechodfsa -En revisiÃ³nsafd )En progresosfd Por hacerÝ Ï Ïé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   columnas           /columnas_tarjetas   á Ð§lIá                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             3 YConfigurar el repositorio del proyecto#8080801 UCrear el esquema de la base de datos#90ee90! 5Recopilar requisitos#ffa5009 eDesarrollar la funciÃ³n de inicio de sesiÃ³n#ffff00' ARevisar el cÃ³digo del API#ffc0cb. 	QEscribir la propuesta del proyecto#add8e6
   Þ üöðêäÞ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          		
    ```