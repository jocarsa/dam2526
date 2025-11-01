

### 🧩 **Ejercicio final de unidad: Mini-motor de juego 2D**

**Objetivo:**
Diseñar un pequeño motor 2D en JavaScript que integre las funcionalidades aprendidas a lo largo de la unidad, combinando animación, control de objetos, detección de colisiones y estructura modular del juego.

---

### **Descripción del proyecto**

Crea un juego sencillo en el que un personaje se mueve dentro de un escenario, recoge objetos y evita obstáculos.
El programa debe estar organizado como si fuera un **mini motor de juego**, con clases y funciones reutilizables.

---

### **Requisitos mínimos**

#### 1️⃣ Estructura base

* Crea un archivo `index.html` con un `<canvas>` de 800×600 píxeles.
* Usa un archivo `motor.js` donde definas las clases principales.
* Utiliza imágenes para el fondo y los sprites.

#### 2️⃣ Clases principales

Implementa, al menos, las siguientes clases:

```javascript
class Motor {
  constructor(canvasId) { ... }      // Configura contexto, bucle y actualización
  iniciar() { ... }                 // Inicia el bucle principal
}

class Escenario {
  constructor(mapa) { ... }          // Carga el mapa (array bidimensional)
  dibujar(contexto) { ... }
}

class Entidad {
  constructor(x, y, sprite) { ... }  // Posición y aspecto gráfico
  dibujar(contexto) { ... }
  mover(dx, dy) { ... }
}

class Jugador extends Entidad {
  actualizar(teclas) { ... }         // Movimiento según teclas pulsadas
}
```

#### 3️⃣ Funcionalidades

* Movimiento del jugador con **W, A, S, D**.
* Colisiones con muros.
* Detección y recogida de objetos.
* Contador de puntos en pantalla.
* Bucle principal con `requestAnimationFrame()`.

#### 4️⃣ Extensiones opcionales

* Añadir enemigos con movimiento automático.
* Añadir partículas al recoger un objeto.
* Cambiar de nivel al alcanzar cierta puntuación.
* Mostrar pantalla de inicio y fin.

---

### **Entrega**

📂 Estructura sugerida:

```
/101-EjercicioFinal
├── index.html
├── motor.js
├── fondo.png
├── sprites.png
└── README.md
```

En el `README.md` explica brevemente:

* Qué partes del código representan los componentes del motor.
* Cómo ejecutar el juego.
* Qué mejoras opcionales implementaste.

---

### **Criterios de evaluación**

* Uso correcto del lienzo y contexto de dibujo.
* Implementación modular (clases o funciones bien separadas).
* Detección de colisiones funcional.
* Fluidez en la animación (bucle de renderizado).
* Creatividad en gráficos y mecánica.



