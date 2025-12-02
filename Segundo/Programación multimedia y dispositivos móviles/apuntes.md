# Programación multimedia y dispositivos móviles

**Author:** Jose Vicente Carratala Sanchis

## Table of contents

- [Análisis de motores de juegos](#analisis-de-motores-de-juegos)
  - [Animación 2D y 3D](#animacion-2d-y-3d)
  - [Arquitectura del juego. Componentes](#arquitectura-del-juego-componentes)
  - [Motores de juegos Tipos y utilización](#motores-de-juegos-tipos-y-utilizacion)
  - [Áreas de especialización, librerías utilizadas y lenguajes de programación](#areas-de-especializacion-librerias-utilizadas-y-lenguajes-de-programacion)
  - [Componentes de un motor de juegos](#componentes-de-un-motor-de-juegos)
  - [Librerías que proporcionan las funciones básicas de un Motor 2D3D](#librerias-que-proporcionan-las-funciones-basicas-de-un-motor-2d3d)
  - [Estudio de juegos existentes](#estudio-de-juegos-existentes)
  - [Aplicación de modificaciones sobre juegos existentes](#aplicacion-de-modificaciones-sobre-juegos-existentes)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad)
  - [Examen final](#examen-final)
- [Desarrollo de juegos 2D y 3D](#desarrollo-de-juegos-2d-y-3d)
  - [Técnicas de programación 2D3D](#tecnicas-de-programacion-2d3d)
  - [Fases de desarrollo](#fases-de-desarrollo)
  - [Componentes de los objetos](#componentes-de-los-objetos)
  - [Fuentes de audio. Propiedades](#fuentes-de-audio-propiedades)
  - [Cámaras e iluminación](#camaras-e-iluminacion)
  - [Creación de escenas.](#creacion-de-escenas)
  - [Análisis de ejecución](#analisis-de-ejecucion)
- [Utilización de librerías multimedia integradas](#utilizacion-de-librerias-multimedia-integradas)
  - [Conceptos sobre aplicaciones multimedia](#conceptos-sobre-aplicaciones-multimedia)
  - [Arquitectura del API utilizado](#arquitectura-del-api-utilizado)
  - [Fuentes de datos multimedia. Clases](#fuentes-de-datos-multimedia-clases)
  - [Procesamiento de objetos multimedia](#procesamiento-de-objetos-multimedia)
  - [Reproducción de objetos multimedia](#reproduccion-de-objetos-multimedia)
  - [Animación de objetos](#animacion-de-objetos)
- [Análisis de tecnologías para aplicaciones en dispositivos móviles](#analisis-de-tecnologias-para-aplicaciones-en-dispositivos-moviles)
  - [Dispositivos móviles](#dispositivos-moviles)
  - [Hardware para dispositivos móviles](#hardware-para-dispositivos-moviles)
  - [Tecnologías de desarrollo](#tecnologias-de-desarrollo)
  - [Emuladores. Configuraciones](#emuladores-configuraciones)
  - [Aplicaciones móviles](#aplicaciones-moviles)
  - [Modelo de estados de una aplicación móvil activo, pausa y destruido](#modelo-de-estados-de-una-aplicacion-movil-activo-pausa-y-destruido)
  - [Ciclo de vida de una aplicación](#ciclo-de-vida-de-una-aplicacion)
  - [Modificación de aplicaciones existentes](#modificacion-de-aplicaciones-existentes)
  - [Utilización del entorno de ejecución del administrador de aplicaciones](#utilizacion-del-entorno-de-ejecucion-del-administrador-de-aplicaciones)
- [Desarrollo de aplicaciones para dispositivos móviles](#desarrollo-de-aplicaciones-para-dispositivos-moviles)
  - [Herramientas. Flujo de trabajo](#herramientas-flujo-de-trabajo)
  - [Componentes de una aplicación. Recursos](#componentes-de-una-aplicacion-recursos)
  - [Interfaces de usuario. Clases asociadas](#interfaces-de-usuario-clases-asociadas)
  - [Contexto gráfico. Imágenes](#contexto-grafico-imagenes)
  - [Métodos de entrada. Eventos](#metodos-de-entrada-eventos)
  - [Gestión de las preferencias de la aplicación](#gestion-de-las-preferencias-de-la-aplicacion)
  - [Bases de datos y almacenamiento](#bases-de-datos-y-almacenamiento)
  - [Persistencia](#persistencia)
  - [Tareas en segundo plano. Servicios](#tareas-en-segundo-plano-servicios)
  - [Seguridad y permisos](#seguridad-y-permisos)
  - [Conectividad. Tipos.](#conectividad-tipos)
  - [Manejo de conexiones HTTP y HTTPS](#manejo-de-conexiones-http-y-https)
  - [Sensores](#sensores)
  - [Posicionamiento. Localización. Mapas](#posicionamiento-localizacion-mapas)
- [Actividad libre de final de evaluación - La milla extra](#actividad-libre-de-final-de-evaluacion-la-milla-extra)
  - [La Milla Extra - Primera evaluación](#la-milla-extra-primera-evaluacion)

---

<a id="analisis-de-motores-de-juegos"></a>
# Análisis de motores de juegos

<a id="animacion-2d-y-3d"></a>
## Animación 2D y 3D

En el mundo digital actual, los motores de juegos desempeñan un papel crucial, ofreciendo una experiencia interactiva y visualmente atractiva para los jugadores. La animación 2D y 3D es una técnica fundamental en la creación de contenido visual dentro de estos motores, permitiendo desarrollar escenas dinámicas e impactantes que capturan la atención del usuario.

La animación 2D se caracteriza por su simplicidad y eficiencia computacional. Utiliza gráficos bidimensionales para crear personajes, objetos y ambientes, lo que permite un rápido procesamiento de los datos visuales. Este tipo de animación es ideal para juegos que requieren una alta velocidad de actualización, como los juegos de acción o los juegos de estrategia en tiempo real.

Por otro lado, la animación 3D ofrece una experiencia visual más realista y detallada. Utiliza gráficos tridimensionales para crear objetos y personajes con profundidad, lo que permite un movimiento más natural y fluido. La animación 3D es especialmente popular en juegos de acción, simulaciones y juegos de rol, donde la interacción del jugador con el entorno es crucial.

Los motores de juegos modernos incorporan técnicas avanzadas para optimizar la animación 2D y 3D. Por ejemplo, los motores utilizan algoritmos eficientes para calcular el movimiento de los objetos en tiempo real, minimizando el uso de recursos del sistema. Además, se implementan técnicas como la culling (eliminación oculta) para evitar el procesamiento de objetos que no están visibles en la pantalla, lo que mejora significativamente el rendimiento.

La creación de animaciones 2D y 3D requiere un conocimiento profundo de los motores de juegos. Los desarrolladores deben entender cómo funcionan las capas gráficas, los sistemas de física y las herramientas de programación específicas del motor. Además, es importante tener en cuenta la optimización de la animación para garantizar una experiencia fluida y sin retrasos.

En el caso de la animación 2D, los desarrolladores pueden utilizar herramientas gráficas como Adobe Animate o Unity para crear personajes y escenas. Estas herramientas ofrecen una interfaz intuitiva para diseñar gráficos bidimensionales y animaciones sencillas. Para proyectos más complejos, se utilizan motores de juegos específicamente diseñados para la creación de contenido 2D, como Godot o Construct.

La animación 3D es un desafío mayor debido a su naturaleza tridimensional. Los desarrolladores deben tener conocimientos avanzados en gráficos tridimensionales y física computacional. Herramientas como Blender son populares para la creación de modelos 3D, mientras que motores de juegos como Unreal Engine o Unity ofrecen herramientas integradas para crear animaciones 3D.

En conclusión, la animación 2D y 3D es una técnica fundamental en el desarrollo de motores de juegos. Ofrece a los desarrolladores la capacidad de crear experiencias visuales impactantes y detalladas que capturan la atención del jugador. Con un conocimiento profundo de los motores de juegos y las herramientas gráficas adecuadas, los desarrolladores pueden crear contenido visual impresionante que mejore significativamente la experiencia del usuario en los juegos.

<a id="arquitectura-del-juego-componentes"></a>
## Arquitectura del juego. Componentes

En el análisis del desarrollo de juegos, la arquitectura del juego desempeña un papel crucial, proporcionando una estructura sólida sobre la cual se construyen las funcionalidades y mecanismos del juego. Esta arquitectura es fundamental para garantizar que los componentes intercambien información eficientemente y que el juego sea escalable y fácil de mantener.

El componente principal de cualquier motor de juegos es el **motor gráfico**, encargado de renderizar la escena en pantalla, gestionar las texturas, modelos 3D y animaciones. Este componente interactúa con los componentes de entrada para capturar interacciones del usuario, como clics o movimientos del joystick.

Además del motor gráfico, el **motor de física** es otro elemento esencial, encargado de simular la interacción entre objetos en el juego, como colisiones y movimiento. Este componente permite que los jugadores experimenten un mundo realista dentro del juego, añadiendo una capa adicional de immersion.

El **motor de audio** también es crucial, proporcionando sonidos ambientales, efectos de sonido y música para enriquecer la experiencia del jugador. Este componente se comunica con el motor gráfico para sincronizar los eventos visuales con los sonidos correspondientes.

Otro componente importante es el **motor de IA**, que controla el comportamiento de los personajes no jugadores (PNJ) y otros elementos inteligentes en el juego. Esta funcionalidad puede variar desde la simulación del pensamiento humano hasta la creación de algoritmos simples para la navegación y la interacción.

El **motor de recursos** se encarga de cargar, almacenar y gestionar los archivos multimedia utilizados por el juego, como imágenes, modelos 3D y sonidos. Este componente es vital para mantener un buen rendimiento del juego, ya que una gestión eficiente de los recursos puede evitar la sobrecarga de memoria.

Además, el **motor de controlador** se encarga de gestionar las entradas del usuario, como teclado, joystick o gestos táctiles. Este componente es fundamental para permitir interacciones fluidas y precisas con el juego.

El **motor de estado del juego** mantiene un seguimiento del progreso del jugador a lo largo del tiempo, almacenando información sobre los niveles completados, las monedas recogidas y otros datos relevantes. Este componente es esencial para la persistencia del progreso entre sesiones de juego.

Por último, el **motor de red** se encarga de manejar las comunicaciones en juegos multijugador, permitiendo que varios jugadores interactúen simultáneamente en una misma sesión. Este componente es crucial para crear experiencias sociales y competitivas dentro del juego.

En resumen, la arquitectura del juego está compuesta por diversos componentes interconectados, cada uno desempeñando un papel específico pero todos trabajando juntos para crear una experiencia de juego fluida, interactiva y envolvente. Cada componente debe ser diseñado con cuidado para garantizar que el juego sea eficiente, escalable y fácil de mantener a lo largo del tiempo.

### empezamos

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizable (objetos del juego)
    
      // Condiciones de inicio
      
      // Entramos en el bucle
      
      
    </script>
  </body>
</html>
```

### entramos en el bucle

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizable (objetos del juego)
    
      // Condiciones de inicio
      
      // Entramos en el bucle
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        console.log("Estoy en el bucle")
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",1000)
      }
    </script>
  </body>
</html>
```

### condiciones de inicio

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizable (objetos del juego)
    
      // Condiciones de inicio
      const lienzo = query.Selector("canvas");
      const contexto = lienzo.getContext("2d");
      
      // Entramos en el bucle
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        console.log("Estoy en el bucle")
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",1000)
      }
    </script>
  </body>
</html>
```

### clases

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizable (objetos del juego)
      
      class Jugador{
         constructor(){
            this.posx = 256;
            this.posy = 256;
            this.angulo = 0
         }
         dibuja(){
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      
      class Roca{
      
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio
      const lienzo = document.querySelector("canvas");
      const contexto = lienzo.getContext("2d");
      // Instancio las clases necesarias
      var jugador = new Jugador()
      
      // Entramos en el bucle
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        contexto.clearRect(0,0,512,512)
        jugador.dibuja()
        console.log("Estoy en el bucle")
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",1000)
      }
    </script>
  </body>
</html>
```

### vamos con las rocas

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizable (objetos del juego)
      
      class Jugador{
         constructor(){
            this.posx = 256;
            this.posy = 256;
            this.angulo = 0
         }
         dibuja(){
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      
      class Roca{
        constructor(){
            this.posx = Math.random()*512;
            this.posy = Math.random()*512;
            this.angulo = 0
            this.lados = Math.round(Math.random()*10+3)
            this.radio = Math.random()*20+10
         }
         dibuja(){
            contexto.beginPath()
            contexto.moveTo(this.posx+this.radio,this.posy)
            for(let i = 0;i<this.lados;i++){
              contexto.lineTo(
                this.posx + Math.cos((i/this.lados)*Math.PI*2)*this.radio,
                this.posy + Math.sin((i/this.lados)*Math.PI*2)*this.radio
              )
            }
            contexto.closePath()
            contexto.stroke()
         }
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio
      const lienzo = document.querySelector("canvas");
      const contexto = lienzo.getContext("2d");
      // Instancio las clases necesarias
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Entramos en el bucle
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        contexto.clearRect(0,0,512,512)
        jugador.dibuja()
        console.log("Estoy en el bucle")
        rocas.forEach(function(roca){
          roca.dibuja()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",1000)
      }
    </script>
  </body>
</html>
```

### aleatoriedad rocas

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizable (objetos del juego)
      
      class Jugador{
         constructor(){
            this.posx = 256;
            this.posy = 256;
            this.angulo = 0
         }
         dibuja(){
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      
      class Roca{
        constructor(){
            this.posx = Math.random()*512;
            this.posy = Math.random()*512;
            this.angulo = 0
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio
      const lienzo = document.querySelector("canvas");
      const contexto = lienzo.getContext("2d");
      // Instancio las clases necesarias
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Entramos en el bucle
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        contexto.clearRect(0,0,512,512)
        jugador.dibuja()
        console.log("Estoy en el bucle")
        rocas.forEach(function(roca){
          roca.dibuja()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",1000)
      }
    </script>
  </body>
</html>
```

### las rocas se mueven

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizable (objetos del juego)
      
      class Jugador{
         constructor(){
            this.posx = 256;
            this.posy = 256;
            this.angulo = 0
         }
         dibuja(){
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      
      class Roca{
        constructor(){
            this.posx = Math.random()*512;
            this.posy = Math.random()*512;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio
      const lienzo = document.querySelector("canvas");
      const contexto = lienzo.getContext("2d");
      // Instancio las clases necesarias
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Entramos en el bucle
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        contexto.clearRect(0,0,512,512)
        jugador.dibuja()
        console.log("Estoy en el bucle")
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### comentarios

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = 256;
            this.posy = 256;
            this.angulo = 0
         }
         dibuja(){
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*512;
            this.posy = Math.random()*512;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,512,512)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### pantalla completa

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### personaje dibujo y se mueve

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            contexto.beginPath()
            contexto.moveTo(
              this.posx-Math.cos(this.angulo+Math.PI/4)*20,
              this.posy-Math.sin(this.angulo+Math.PI/4)*20  
            )
            contexto.lineTo(
              this.posx+Math.cos(this.angulo+Math.PI/4)*20,
              this.posy-Math.sin(this.angulo+Math.PI/4)*20  
            )
            contexto.lineTo(
              this.posx,
              this.posy+Math.sin(this.angulo)*15 
            )
            contexto.closePath()
            contexto.stroke()
         }
      }
      
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### controles de teclado

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
        switch(e.key){
          case "w":
            
            break;
          case "s":
            y += 10;
            direccion = 2
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
        }
        pinta();
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### ahora me desplazo

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
      class Bala{
        
      }
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
        switch(e.key){
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
        }
        pinta();
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### balas como objetos

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(){
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
        switch(e.key){
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
        }
        pinta();
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### espaciadora crea balas

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
      console.log(e)
        switch(e.key){
        
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### tengo que tambien dibujar las balas

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
      console.log(e)
        switch(e.key){
        
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### les digo a las balas que se mueven

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
      console.log(e)
        switch(e.key){
        
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### mas velocidad para las balas

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
      console.log(e)
        switch(e.key){
        
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### detectamos colision de la bala con la roca

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
      console.log(e)
        switch(e.key){
        
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        balas.forEach(function(bala){
          rocas.forEach(function(roca){
            let midistancia = distancia(bala.posx, bala.posy, roca.posx, roca.posy)
            
            
            if(midistancia < roca.radio){
              console.log("colision")
            }
          })
        })
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### ahora borramos la roca

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
      console.log(e)
        switch(e.key){
        
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        for(let i = rocas.length - 1; i >= 0; i--){
          let roca = rocas[i];
          balas.forEach(function(bala){
            let midistancia = distancia(bala.posx, bala.posy, roca.posx, roca.posy);
            if(midistancia < roca.radio){
              rocas.splice(i,1); // quito la roca del array
            }
          });
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### la bala tambien se rompe con la roca

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
      console.log(e)
        switch(e.key){
        
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        for(let i = rocas.length - 1; i >= 0; i--){
          let roca = rocas[i];
          for(let j = balas.length - 1; j >= 0; j--){
            let bala = balas[j]
            let midistancia = distancia(bala.posx, bala.posy, roca.posx, roca.posy);
            if(midistancia < roca.radio){
              rocas.splice(i,1); // quito la roca del array
              balas.splice(j,1)
            }
          }
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### balas se eliminan al salir de la pantalla

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
      console.log(e)
        switch(e.key){
        
          case "w":
            jugador.posx += Math.cos(jugador.angulo)
            jugador.posy += Math.sin(jugador.angulo)
            break;
          case "s":
            jugador.posx -= Math.cos(jugador.angulo)
            jugador.posy -= Math.sin(jugador.angulo)
            break;
          case "a":
            jugador.angulo -= 0.1
            break;
          case "d":
            jugador.angulo += 0.1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        for(let i = rocas.length - 1; i >= 0; i--){
          let roca = rocas[i];
          for(let j = balas.length - 1; j >= 0; j--){
            let bala = balas[j]
            let midistancia = distancia(bala.posx, bala.posy, roca.posx, roca.posy);
            if(midistancia < roca.radio){
              rocas.splice(i,1); // quito la roca del array
              balas.splice(j,1)
            }
          }
        }
        for(let j = balas.length - 1; j >= 0; j--){
          if(balas[j].posx < 0 || balas[j].posx > anchura || balas[j].posy < 0 || balas[j].posy > altura){
            balas.splice(j,1)
          }
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### mejoramos controles de teclado

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
         mueve(){
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      var giro = 0
      var mueve = 0
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
        switch(e.key){
        
          case "w":
            mueve = 1
            break;
          case "s":
            
            break;
          case "a":
            giro = -1
            break;
          case "d":
            giro = 1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      document.querySelector("body").onkeyup = function(e){
        switch(e.key){
          case "w":
            mueve = 0
            break;
          case "a":
            giro = 0
            break;
          case "d":
            giro = 0
            break;
          
        }
        
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // Controlamos el giro
        jugador.angulo += giro/10
        if(mueve == 1){
          jugador.mueve()
        }
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        for(let i = rocas.length - 1; i >= 0; i--){
          let roca = rocas[i];
          for(let j = balas.length - 1; j >= 0; j--){
            let bala = balas[j]
            let midistancia = distancia(bala.posx, bala.posy, roca.posx, roca.posy);
            if(midistancia < roca.radio){
              rocas.splice(i,1); // quito la roca del array
              balas.splice(j,1)
            }
          }
        }
        for(let j = balas.length - 1; j >= 0; j--){
          if(balas[j].posx < 0 || balas[j].posx > anchura || balas[j].posy < 0 || balas[j].posy > altura){
            balas.splice(j,1)
          }
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### simulamos la inercia

```html
<!doctype html>
<html>
  <head>
    <style></style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
            // Geometría del triángulo (nariz + 2 vértices traseros)
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.stroke();
         }
         mueve(){
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.stroke();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      var giro = 0
      var mueve = 0
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
        switch(e.key){
        
          case "w":
            mueve = 1
            break;
          case "s":
            
            break;
          case "a":
            giro = -1
            break;
          case "d":
            giro = 1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      document.querySelector("body").onkeyup = function(e){
        switch(e.key){
          case "w":
            mueve = 0
            break;
          case "a":
            giro = 0
            break;
          case "d":
            giro = 0
            break;
          
        }
        
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // Controlamos el giro
        jugador.angulo += giro/10
        if(mueve == 1){
          jugador.mueve()
        }
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.clearRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        for(let i = rocas.length - 1; i >= 0; i--){
          let roca = rocas[i];
          for(let j = balas.length - 1; j >= 0; j--){
            let bala = balas[j]
            let midistancia = distancia(bala.posx, bala.posy, roca.posx, roca.posy);
            if(midistancia < roca.radio){
              rocas.splice(i,1); // quito la roca del array
              balas.splice(j,1)
            }
          }
        }
        for(let j = balas.length - 1; j >= 0; j--){
          if(balas[j].posx < 0 || balas[j].posx > anchura || balas[j].posy < 0 || balas[j].posy > altura){
            balas.splice(j,1)
          }
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### mejores gráficos

```html
<!doctype html>
<html>
  <head>
    <style>body,html{padding:0px;margin:0px;overflow:hidden;}</style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            
            // Geometría del triángulo (nariz + 2 vértices traseros)
            contexto.fillStyle = "white"
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.fill();
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
          contexto.fillStyle = "grey"
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.fill();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      var giro = 0
      var mueve = 0
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
        switch(e.key){
        
          case "w":
            mueve = 1
            break;
          case "s":
            
            break;
          case "a":
            giro = -1
            break;
          case "d":
            giro = 1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      document.querySelector("body").onkeyup = function(e){
        switch(e.key){
          case "w":
            mueve = 0
            break;
          case "a":
            giro = 0
            break;
          case "d":
            giro = 0
            break;
          
        }
        
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // Controlamos el giro
        jugador.angulo += giro/10
        if(mueve == 1){
          jugador.mueve()
        }
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.fillStyle = "black"
        contexto.fillRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        for(let i = rocas.length - 1; i >= 0; i--){
          let roca = rocas[i];
          for(let j = balas.length - 1; j >= 0; j--){
            let bala = balas[j]
            let midistancia = distancia(bala.posx, bala.posy, roca.posx, roca.posy);
            if(midistancia < roca.radio){
              rocas.splice(i,1); // quito la roca del array
              balas.splice(j,1)
            }
          }
        }
        for(let j = balas.length - 1; j >= 0; j--){
          if(balas[j].posx < 0 || balas[j].posx > anchura || balas[j].posy < 0 || balas[j].posy > altura){
            balas.splice(j,1)
          }
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### dibujamos estrellas

```html
<!doctype html>
<html>
  <head>
    <style>body,html{padding:0px;margin:0px;overflow:hidden;}</style>
  </head>
  <body>
    <canvas width=512 height=512></canvas>
    <script>
      // Declarar las clases reutilizables (objetos del juego) ///////////////////////////////////////////////
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0
         }
         dibuja(){
            
            // Geometría del triángulo (nariz + 2 vértices traseros)
            contexto.fillStyle = "white"
            const noseLen = 22;     // largo hacia la “nariz”
            const baseLen = 14;     // radio de los vértices traseros
            const spread  = Math.PI * 0.75; // 135° de apertura respecto a la nariz

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            // Dibujo del triángulo
            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.fill();
            // Dibujo el circulo central
            contexto.fillStyle = "red"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial
            this.velocidad = 5;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "blue"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,5,0,Math.PI*2)
            contexto.fill()
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad
          this.posy += Math.sin(this.angulo)*this.velocidad
         }
      }
      class Estrella{
        constructor(){
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
         }
         dibuja(){
            // Dibujo el circulo central
            contexto.fillStyle = "white"
            contexto.beginPath()
            contexto.arc(this.posx,this.posy,1,0,Math.PI*2)
            contexto.fill()
         }
         
      }
      class Roca{
        // Clase roca que crea rocas en la pantalla las cuales tenemos que destruir
        constructor(){
            // El constructor define siempre las condiciones de inicio de la clase
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2
            this.lados = Math.round(Math.random()*20+5)
            this.radio = Math.random()*20+10
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

         }
         // Ahora creamos tantos métodos como sea necesario para definir el comportamiento de la clase
         dibuja(){
          contexto.fillStyle = "grey"
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.fill();
           }
         mueve(){
          this.angulo += (Math.random()-0.5)*0.1
          this.posx += Math.cos(this.angulo)
          this.posy += Math.sin(this.angulo)
         }
      }
      
     
    
      // Condiciones de inicio ///////////////////////////////////////////////////////////////////
      // Variables globales a todo el programa
      
      const anchura = window.innerWidth
      const altura = window.innerHeight
      var giro = 0
      var mueve = 0
      
      // Primero seleccionarmos el lienzo donde vamos a pintar
      
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura
      lienzo.height = altura
      const contexto = lienzo.getContext("2d");
      
      // Instancio las clases necesarias 
      
      var jugador = new Jugador()
      var rocas = []
      var numerorocas = 10;
      for(let i = 0;i<numerorocas;i++){
        rocas.push(new Roca())
      }
      var balas = []
      var estrellas = []
      var numeroestrellas = 100
      for(let i = 0;i<numeroestrellas;i++){
        estrellas.push(new Estrella())
      }
      
      // Controles de teclado
      
      document.querySelector("body").onkeydown = function(e){
        switch(e.key){
        
          case "w":
            mueve = 1
            break;
          case "s":
            
            break;
          case "a":
            giro = -1
            break;
          case "d":
            giro = 1
            break;
          
        }
        switch(e.code){
          case "Space":
            balas.push(new Bala(jugador.posx,jugador.posy,jugador.angulo))
            break;
        }
      }
      document.querySelector("body").onkeyup = function(e){
        switch(e.key){
          case "w":
            mueve = 0
            break;
          case "a":
            giro = 0
            break;
          case "d":
            giro = 0
            break;
          
        }
        
      }
      
      // Entramos en el bucle ///////////////////////////////////////////////////////////////////////
      
      // Definimos un temporizador
      
      var temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        // Controlamos el giro
        jugador.angulo += giro/10
        if(mueve == 1){
          jugador.mueve()
        }
        // De una forma u otra, borro la pantalla para dibujar el siguiente fotograma
        contexto.fillStyle = "black"
        contexto.fillRect(0,0,anchura,altura)
        // Generalmente, primero llamo al jugador (suele haber 1)
        jugador.dibuja()
        // Dibujo estrellas
        estrellas.forEach(function(estrella){
          estrella.dibuja()
        })
        // Y a continuación llamo a NPC, props, lo que sea
        rocas.forEach(function(roca){
          roca.dibuja()
          roca.mueve()
        })
        balas.forEach(function(bala){
          bala.dibuja()
          bala.mueve()
        })
        for(let i = rocas.length - 1; i >= 0; i--){
          let roca = rocas[i];
          for(let j = balas.length - 1; j >= 0; j--){
            let bala = balas[j]
            let midistancia = distancia(bala.posx, bala.posy, roca.posx, roca.posy);
            if(midistancia < roca.radio){
              rocas.splice(i,1); // quito la roca del array
              balas.splice(j,1)
            }
          }
        }
        for(let j = balas.length - 1; j >= 0; j--){
          if(balas[j].posx < 0 || balas[j].posx > anchura || balas[j].posy < 0 || balas[j].posy > altura){
            balas.splice(j,1)
          }
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
    </script>
  </body>
</html>
```

### inercia

```html
<!doctype html>
<html>
  <head>
    <style>body,html{padding:0;margin:0;overflow:hidden;background:#000}</style>
  </head>
  <body>
    <canvas width="512" height="512"></canvas>
    <script>
      // ================= Utilidades =================
      function distancia(x1, y1, x2, y2) {
        let dx = x2 - x1;
        let dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      // ================= Clases =================
      class Jugador{
         constructor(){
            this.posx = anchura/2;
            this.posy = altura/2;
            this.angulo = 0;

            // Física con inercia
            this.velx = 0;
            this.vely = 0;
            this.aceleracion = 0.18;   // empuje por frame cuando hay thrust
            this.rozamiento = 0.995;   // amortiguación (1 = sin rozamiento)
            this.velMax = 8;           // límite de velocidad
         }
         dibuja(){
            // Triángulo orientado
            contexto.fillStyle = "white";
            const noseLen = 22;
            const baseLen = 14;
            const spread  = Math.PI * 0.75;

            const noseX  = this.posx + Math.cos(this.angulo) * noseLen;
            const noseY  = this.posy + Math.sin(this.angulo) * noseLen;

            const leftX  = this.posx + Math.cos(this.angulo + spread) * baseLen;
            const leftY  = this.posy + Math.sin(this.angulo + spread) * baseLen;

            const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
            const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

            contexto.beginPath();
            contexto.moveTo(noseX, noseY);
            contexto.lineTo(leftX, leftY);
            contexto.lineTo(rightX, rightY);
            contexto.closePath();
            contexto.lineWidth = 2;
            contexto.strokeStyle = "#000";
            contexto.fill();

            // Punto rojo central
            contexto.fillStyle = "red";
            contexto.beginPath();
            contexto.arc(this.posx, this.posy, 5, 0, Math.PI*2);
            contexto.fill();
         }
         aplicaThrust(activado){
           if(!activado) return;
           // Empuje en la dirección del ángulo
           this.velx += Math.cos(this.angulo) * this.aceleracion;
           this.vely += Math.sin(this.angulo) * this.aceleracion;

           // Cap de velocidad
           const v = Math.hypot(this.velx, this.vely);
           if (v > this.velMax){
             const f = this.velMax / v;
             this.velx *= f;
             this.vely *= f;
           }
         }
         mueve(){
           // Aplicar rozamiento
           this.velx *= this.rozamiento;
           this.vely *= this.rozamiento;

           // Integrar posición
           this.posx += this.velx;
           this.posy += this.vely;

           // Screen wrap
           if (this.posx < 0) this.posx += anchura;
           if (this.posx > anchura) this.posx -= anchura;
           if (this.posy < 0) this.posy += altura;
           if (this.posy > altura) this.posy -= altura;
         }
      }

      class Bala{
        constructor(xinicial,yinicial,anguloinicial){
            this.posx = xinicial;
            this.posy = yinicial;
            this.angulo = anguloinicial;
            this.velocidad = 12;
         }
         dibuja(){
            contexto.fillStyle = "dodgerblue";
            contexto.beginPath();
            contexto.arc(this.posx,this.posy,3,0,Math.PI*2);
            contexto.fill();
         }
         mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad;
          this.posy += Math.sin(this.angulo)*this.velocidad;
         }
      }

      class Estrella{
        constructor(){
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
         }
         dibuja(){
            contexto.fillStyle = "white";
            contexto.beginPath();
            contexto.arc(this.posx,this.posy,1,0,Math.PI*2);
            contexto.fill();
         }
      }

      class Roca{
        constructor(){
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            this.angulo = Math.random()*Math.PI*2;
            this.lados = Math.round(Math.random()*20+5);
            this.radio = Math.random()*20+10;
            const rugosidad = 0.4;
            this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);

            // ligera velocidad para que naveguen
            const v = Math.random()*1.2+0.3;
            this.vx = Math.cos(this.angulo)*v;
            this.vy = Math.sin(this.angulo)*v;
         }
         dibuja(){
            contexto.fillStyle = "grey";
            contexto.beginPath();
            for(let i = 0; i < this.lados; i++){
              const ang = (i/this.lados)*Math.PI*2 + this.angulo;
              const r   = this.radio * this.puntas[i];
              const x   = this.posx + Math.cos(ang)*r;
              const y   = this.posy + Math.sin(ang)*r;
              if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
            }
            contexto.closePath();
            contexto.strokeStyle = "#333";
            contexto.fill();
         }
         mueve(){
          // ligera rotación y movimiento
          this.angulo += (Math.random()-0.5)*0.04;
          this.posx += this.vx;
          this.posy += this.vy;

          // Screen wrap para rocas
          if (this.posx < -this.radio) this.posx = anchura + this.radio;
          if (this.posx > anchura + this.radio) this.posx = -this.radio;
          if (this.posy < -this.radio) this.posy = altura + this.radio;
          if (this.posy > altura + this.radio) this.posy = -this.radio;
         }
      }

      // ================= Inicio =================
      const anchura = window.innerWidth;
      const altura  = window.innerHeight;

      let giro = 0;        // -1 izquierda, 1 derecha
      let thrust = false;  // empuje activo (W)

      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura;
      lienzo.height = altura;
      const contexto = lienzo.getContext("2d");

      const jugador = new Jugador();

      let rocas = [];
      const numerorocas = 10;
      for(let i = 0; i < numerorocas; i++) rocas.push(new Roca());

      let balas = [];

      let estrellas = [];
      const numeroestrellas = 100;
      for(let i = 0; i < numeroestrellas; i++) estrellas.push(new Estrella());

      // ================= Controles =================
      document.body.onkeydown = function(e){
        switch(e.key){
          case "w": thrust = true; break;
          case "a": giro = -1; break;
          case "d": giro = 1; break;
        }
        if (e.code === "Space"){
          balas.push(new Bala(jugador.posx, jugador.posy, jugador.angulo));
        }
      };
      document.body.onkeyup = function(e){
        switch(e.key){
          case "w": thrust = false; break;
          case "a": if (giro === -1) giro = 0; break;
          case "d": if (giro === 1)  giro = 0; break;
        }
      };

      // ================= Bucle =================
      let temporizador = null;

      function bucle(){
        // Input -> rotación y thrust
        jugador.angulo += giro * 0.08; // suavizo un poco el giro
        jugador.aplicaThrust(thrust);

        // Fondo
        contexto.fillStyle = "black";
        contexto.fillRect(0,0,anchura,altura);

        // Estrellas
        estrellas.forEach(e => e.dibuja());

        // Entidades
        rocas.forEach(r => { r.dibuja(); r.mueve(); });
        balas.forEach(b => { b.dibuja(); b.mueve(); });

        // Jugador al final para que quede por encima
        jugador.mueve();
        jugador.dibuja();

        // Colisiones bala-roca
        for(let i = rocas.length - 1; i >= 0; i--){
          let roca = rocas[i];
          for(let j = balas.length - 1; j >= 0; j--){
            let bala = balas[j];
            if (distancia(bala.posx, bala.posy, roca.posx, roca.posy) < roca.radio){
              rocas.splice(i,1);
              balas.splice(j,1);
              break; // roca destruida, pasar a la siguiente roca
            }
          }
        }

        // Borrar balas fuera de pantalla
        for(let j = balas.length - 1; j >= 0; j--){
          if(balas[j].posx < 0 || balas[j].posx > anchura || balas[j].posy < 0 || balas[j].posy > altura){
            balas.splice(j,1);
          }
        }

        // Repetir
        temporizador = setTimeout(bucle, 16); // ~60 FPS
      }

      // Lanzar juego
      temporizador = setTimeout(bucle, 16);
    </script>
  </body>
</html>
```

### niveles

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Asteroids-lite</title>
    <style>
      html,body{margin:0;padding:0;overflow:hidden;background:#000}
      canvas{display:block}
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
      // ========== Utilidades ==========
      function distancia(x1, y1, x2, y2) {
        const dx = x2 - x1, dy = y2 - y1;
        return Math.hypot(dx, dy);
      }
      function rand(min, max){ return Math.random()*(max-min)+min }

      // ========== Clases ==========
      class Jugador{
        constructor(){
          this.posx = anchura/2;
          this.posy = altura/2;
          this.angulo = 0;
          this.velx = 0;
          this.vely = 0;
          this.aceleracion = 0.18;
          this.rozamiento = 0.995;
          this.velMax = 8;
        }
        dibuja(){
          // Triángulo
          const noseLen = 22, baseLen = 14, spread = Math.PI*0.75;
          const noseX = this.posx + Math.cos(this.angulo)*noseLen;
          const noseY = this.posy + Math.sin(this.angulo)*noseLen;
          const leftX = this.posx + Math.cos(this.angulo + spread)*baseLen;
          const leftY = this.posy + Math.sin(this.angulo + spread)*baseLen;
          const rightX= this.posx + Math.cos(this.angulo - spread)*baseLen;
          const rightY= this.posy + Math.sin(this.angulo - spread)*baseLen;

          contexto.fillStyle = "white";
          contexto.beginPath();
          contexto.moveTo(noseX,noseY);
          contexto.lineTo(leftX,leftY);
          contexto.lineTo(rightX,rightY);
          contexto.closePath();
          contexto.fill();

          // Punto rojo
          contexto.fillStyle = "red";
          contexto.beginPath();
          contexto.arc(this.posx,this.posy,5,0,Math.PI*2);
          contexto.fill();
        }
        aplicaThrust(on){
          if(!on) return;
          this.velx += Math.cos(this.angulo)*this.aceleracion;
          this.vely += Math.sin(this.angulo)*this.aceleracion;
          const v = Math.hypot(this.velx, this.vely);
          if(v > this.velMax){
            const f = this.velMax / v;
            this.velx *= f; this.vely *= f;
          }
        }
        mueve(){
          this.velx *= this.rozamiento;
          this.vely *= this.rozamiento;
          this.posx += this.velx;
          this.posy += this.vely;

          // Mantenemos wrap para el jugador
          if (this.posx < 0) this.posx += anchura;
          if (this.posx > anchura) this.posx -= anchura;
          if (this.posy < 0) this.posy += altura;
          if (this.posy > altura) this.posy -= altura;
        }
      }

      class Bala{
        constructor(x,y,a){
          this.posx = x; this.posy = y; this.angulo = a;
          this.velocidad = 12;
        }
        dibuja(){
          contexto.fillStyle = "dodgerblue";
          contexto.beginPath();
          contexto.arc(this.posx,this.posy,3,0,Math.PI*2);
          contexto.fill();
        }
        mueve(){
          this.posx += Math.cos(this.angulo)*this.velocidad;
          this.posy += Math.sin(this.angulo)*this.velocidad;
        }
      }

      class Estrella{
        constructor(){
          this.posx = Math.random()*anchura;
          this.posy = Math.random()*altura;
        }
        dibuja(){
          contexto.fillStyle = "white";
          contexto.beginPath();
          contexto.arc(this.posx,this.posy,1,0,Math.PI*2);
          contexto.fill();
        }
      }

      class Roca{
        constructor(){
          this.radio = Math.random()*20+10;
          // Evitar spawnear demasiado cerca del jugador
          let ok = false;
          while(!ok){
            this.posx = Math.random()*anchura;
            this.posy = Math.random()*altura;
            ok = distancia(this.posx,this.posy,jugador?.posx||anchura/2,jugador?.posy||altura/2) > 80;
          }
          this.angulo = Math.random()*Math.PI*2;
          this.lados = Math.round(Math.random()*20+5);
          const rugosidad = 0.4;
          this.puntas = Array.from({length:this.lados}, () => 1 + (Math.random()*2 - 1) * rugosidad);
          // Velocidad inicial
          const v = Math.random()*1.6+0.4;
          const dir = Math.random()*Math.PI*2;
          this.vx = Math.cos(dir)*v;
          this.vy = Math.sin(dir)*v;
          this.rot = (Math.random()-0.5)*0.04;
        }
        dibuja(){
          contexto.fillStyle = "grey";
          contexto.beginPath();
          for(let i=0;i<this.lados;i++){
            const ang = (i/this.lados)*Math.PI*2 + this.angulo;
            const r = this.radio * this.puntas[i];
            const x = this.posx + Math.cos(ang)*r;
            const y = this.posy + Math.sin(ang)*r;
            if(i===0) contexto.moveTo(x,y); else contexto.lineTo(x,y);
          }
          contexto.closePath();
          contexto.strokeStyle = "#333";
          contexto.fill();
        }
        mueve(){
          this.angulo += this.rot;
          this.posx += this.vx;
          this.posy += this.vy;

          // Ricochet en bordes (considerando el radio)
          if (this.posx - this.radio < 0){
            this.posx = this.radio;
            this.vx = -this.vx;
          } else if (this.posx + this.radio > anchura){
            this.posx = anchura - this.radio;
            this.vx = -this.vx;
          }
          if (this.posy - this.radio < 0){
            this.posy = this.radio;
            this.vy = -this.vy;
          } else if (this.posy + this.radio > altura){
            this.posy = altura - this.radio;
            this.vy = -this.vy;
          }
        }
      }

      // ========== Setup ==========
      const anchura = window.innerWidth;
      const altura  = window.innerHeight;
      const lienzo = document.querySelector("canvas");
      lienzo.width = anchura; lienzo.height = altura;
      const contexto = lienzo.getContext("2d");

      const jugador = new Jugador();

      let estrellas = Array.from({length:100}, ()=>new Estrella());
      let balas = [];

      // Niveles
      let level = 1;
      let rocksPerLevel = 10; // base
      let rocas = [];
      let levelMessageTimer = 0; // frames restantes para mostrar “LEVEL N”

      function spawnRocas(n){
        for(let i=0;i<n;i++) rocas.push(new Roca());
      }
      function startLevel(){
        rocas.length = 0;
        spawnRocas(rocksPerLevel);
        levelMessageTimer = 120; // ~2s a 60fps
      }
      startLevel();

      // ========== Controles ==========
      let giro = 0;       // -1 izq, 1 der
      let thrust = false; // W

      document.body.onkeydown = (e)=>{
        switch(e.key){
          case "a": giro = -1; break;
          case "d": giro = 1;  break;
          case "w": thrust = true; break;
        }
        if(e.code === "Space"){
          balas.push(new Bala(jugador.posx, jugador.posy, jugador.angulo));
        }
      };
      document.body.onkeyup = (e)=>{
        switch(e.key){
          case "a": if(giro === -1) giro = 0; break;
          case "d": if(giro === 1)  giro = 0; break;
          case "w": thrust = false; break;
        }
      };

      // ========== Bucle ==========
      let temporizador = null;
      function drawLevelText(){
        if(levelMessageTimer <= 0) return;
        contexto.save();
        contexto.font = "bold 48px sans-serif";
        contexto.textAlign = "center";
        contexto.textBaseline = "middle";
        contexto.fillStyle = "white";
        contexto.strokeStyle = "rgba(0,0,0,0.6)";
        contexto.lineWidth = 6;
        const msg = `LEVEL ${level}`;
        contexto.strokeText(msg, anchura/2, altura*0.2);
        contexto.fillText(msg, anchura/2, altura*0.2);
        contexto.restore();
        levelMessageTimer--;
      }

      function bucle(){
        // Input
        jugador.angulo += giro * 0.08;
        jugador.aplicaThrust(thrust);

        // Fondo
        contexto.fillStyle = "black";
        contexto.fillRect(0,0,anchura,altura);

        // Estrellas
        estrellas.forEach(e=>e.dibuja());

        // Entidades
        rocas.forEach(r=>{ r.dibuja(); r.mueve(); });
        balas.forEach(b=>{ b.dibuja(); b.mueve(); });

        // Jugador
        jugador.mueve();
        jugador.dibuja();

        // Colisiones bala-roca
        for(let i=rocas.length-1;i>=0;i--){
          const roca = rocas[i];
          for(let j=balas.length-1;j>=0;j--){
            const bala = balas[j];
            if(distancia(bala.posx,bala.posy,roca.posx,roca.posy) < roca.radio){
              rocas.splice(i,1);
              balas.splice(j,1);
              break;
            }
          }
        }

        // Borrar balas fuera
        for(let j=balas.length-1;j>=0;j--){
          if(balas[j].posx<0 || balas[j].posx>anchura || balas[j].posy<0 || balas[j].posy>altura){
            balas.splice(j,1);
          }
        }

        // ¿Nivel completado?
        if(rocas.length === 0){
          level++;
          rocksPerLevel *= 2; // duplicar
          startLevel();
        }

        // HUD nivel (esquina)
        contexto.fillStyle = "white";
        contexto.font = "16px monospace";
        contexto.fillText(`Level: ${level}`, 12, 22);

        // Cartel de inicio de nivel
        drawLevelText();

        temporizador = setTimeout(bucle, 16); // ~60fps
      }
      temporizador = setTimeout(bucle, 16);
    </script>
  </body>
</html>
```

<a id="motores-de-juegos-tipos-y-utilizacion"></a>
## Motores de juegos Tipos y utilización

En el mundo digital actual, los motores de juegos desempeñan un papel crucial en la creación de experiencias interactivas y envolventes. Estos motores son herramientas sofisticadas que permiten a los desarrolladores crear mundos virtuales detallados, personajes animados y gráficos impresionantes. Los motores de juegos pueden ser clasificados en dos categorías principales: motores 2D y motores 3D.

Los motores 2D son ideales para juegos que se centran en la acción y el movimiento, como plataformeros o juegos de disparos. Estos motores ofrecen una eficiencia en términos de rendimiento debido a su simplicidad, lo que los hace perfectos para dispositivos móviles con recursos limitados. Además, permiten un control preciso sobre la animación y el movimiento de personajes, facilitando la creación de gráficos fluidos y detallados.

Por otro lado, los motores 3D son esenciales para juegos que requieren una experiencia más inmersiva y realista. Estos motores pueden manejar modelos tridimensionales complejos, iluminación sofisticada y física avanzada, lo que resulta en escenas y personajes de alta calidad. Los motores 3D son especialmente populares para juegos de acción, simulaciones y juegos de estrategia.

La elección del motor depende del tipo de juego que se quiera crear y las plataformas objetivo. Por ejemplo, si el objetivo es desarrollar un juego para dispositivos móviles, un motor 2D puede ser suficiente debido a su eficiencia en términos de rendimiento. Sin embargo, si se desea una experiencia más inmersiva, como en los juegos de acción y simulaciones, un motor 3D será necesario.

Además de la elección del motor, es importante considerar las librerías y herramientas que ofrecen. Cada motor tiene su propio conjunto de funciones y clases que facilitan el desarrollo de juegos. Por ejemplo, Unity ofrece una amplia gama de funcionalidades para la creación de gráficos 3D, mientras que Godot proporciona un enfoque más ligero pero igualmente potente.

El análisis de motores de juegos no se limita a su elección y configuración inicial. Es crucial también entender cómo funcionan internamente. Los motores de juegos están compuestos por varios componentes, como el motor gráfico, el motor física, el motor de audio y el motor de entrada. Cada uno de estos componentes trabaja en conjunto para crear una experiencia fluida y realista.

El motor gráfico es responsable del renderizado de los gráficos 2D o 3D en la pantalla. Utiliza técnicas avanzadas como la culling (descarte) para optimizar el rendimiento, permitiendo que solo los objetos visibles sean procesados. El motor físico simula las leyes de la física en el juego, lo que resulta en gráficos y comportamientos más realistas.

El motor de audio es otro componente crucial, responsable de la reproducción de música y efectos sonoros. Ofrece una amplia gama de opciones para controlar la calidad del sonido, la posición de los efectos y la sincronización con las acciones del juego.

Finalmente, el motor de entrada maneja todas las interacciones del usuario, como el movimiento del personaje, la selección de opciones y la realización de acciones. Ofrece una interfaz fácil de usar para asociar eventos de entrada con funciones específicas en el código.

En conclusión, los motores de juegos son herramientas poderosas que permiten a los desarrolladores crear experiencias interactivas y envolventes. Al elegir el motor adecuado y entender cómo funciona internamente, se puede crear un juego de alta calidad y experiencia para los jugadores.

<a id="areas-de-especializacion-librerias-utilizadas-y-lenguajes-de-programacion"></a>
## Áreas de especialización, librerías utilizadas y lenguajes de programación

En el campo de los motores de juegos, la diversidad es una característica distintiva que refleja las necesidades y preferencias de diferentes desarrolladores y plataformas. Algunas áreas de especialización dentro del desarrollo de motores de juegos incluyen la optimización para dispositivos móviles, donde el rendimiento limitado de los teléfonos móviles implica una gestión eficiente de recursos. Otro área crucial es la creación de contenido interactivo y visualmente atractivo, lo que requiere habilidades en gráficos 2D y 3D.

Las librerías utilizadas en el desarrollo de motores de juegos son fundamentales para abstraer las complejidades técnicas subyacentes. Por ejemplo, Unity es una popular plataforma que ofrece una amplia gama de herramientas y componentes predefinidos, facilitando la creación de juegos 2D y 3D. En contraparte, Unreal Engine se destaca por su potencia en gráficos avanzados y física realista, aunque requiere un mayor conocimiento técnico.

Los lenguajes de programación desempeñan un papel crucial en el desarrollo de motores de juegos, ya que determinan la eficiencia y la flexibilidad del código. C# es uno de los lenguajes más utilizados debido a su facilidad de aprendizaje y su integración con Unity. Por otro lado, C++ ofrece mayor control sobre los recursos del sistema, lo que es beneficioso para motores de juegos que requieren altos niveles de rendimiento.

Además de las librerías y lenguajes, el análisis de motores de juegos también implica la consideración de la arquitectura del juego. La elección de una arquitectura adecuada puede mejorar significativamente la escalabilidad y mantenibilidad del código. Por ejemplo, un enfoque basado en componentes permite una mayor modularidad y reutilización de código.

La optimización para dispositivos móviles es otro aspecto crucial en el desarrollo de motores de juegos. Esto implica no solo mejorar el rendimiento general del juego, sino también considerar factores como la carga de recursos, la gestión de memoria y la eficiencia energética. Herramientas específicas como Unity Profiler pueden ser útiles para identificar y resolver problemas de rendimiento.

En conclusión, el análisis de motores de juegos es una disciplina multifacética que abarca desde las áreas de especialización hasta las herramientas y tecnologías utilizadas. Cada aspecto contribuye a la creación de experiencias de juego innovadoras y satisfactorias para los jugadores en diferentes plataformas.

### trucazo js

```html
<!doctype html>
<html>
  <body>
    <div id="contenedor">
    </div>
    <script>
      const $ = s => document.querySelector(s);
      
      $("#contenedor").textContent = "Hola"
    </script>
  </body>
</html>
```

### aframe

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-box position="-1 0.5 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
      <a-sphere position="0 1.25 -5" radius="1.25" color="#EF2D5E"></a-sphere>
      <a-cylinder position="1 0.75 -3" radius="0.5" height="1.5" color="#FFC65D"></a-cylinder>
      <a-plane position="0 0 -4" rotation="-90 0 0" width="4" height="4" color="#7BC8A4"></a-plane>
      <a-sky color="#ECECEC"></a-sky>
    </a-scene>
  </body>
</html>
```

### poco a poco

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere position="0 1.25 -5" radius="1" color="#ffff00"></a-sphere>
    </a-scene>
  </body>
</html>
```

### ahora añado una caja

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere position="0 1.25 -5" radius="1" color="#ffff00"></a-sphere>
      <a-box position="-1 1.25 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
    </a-scene>
  </body>
</html>
```

### ahora creo un plano para un suelo

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere position="0 1.25 -5" radius="1" color="#ffff00"></a-sphere>
      <a-box position="-1 1.25 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
      <a-plane position="0 0 -4" rotation="-90 0 0" width="8" height="8" color="#7BC8A4"></a-plane>
    </a-scene>
  </body>
</html>
```

### cargo un glb o gltf

```html
<html>
  <head>
    <meta charset="utf-8">
    <title>Cargar modelo GLB en A-Frame</title>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <!-- Carga de recursos -->
      <a-assets>
        <!-- Sustituye el src con la ruta o URL de tu archivo .glb -->
        <a-asset-item id="modelo" src="suzanne.glb"></a-asset-item>
      </a-assets>

      <!-- Carga del modelo GLB -->
      <a-entity 
        gltf-model="#modelo"
        position="0 1 -2"
        scale="1 1 1"
        rotation="0 180 0">
      </a-entity>

      
    </a-scene>
  </body>
</html>
```

### controles de orbita

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>A-Frame Orbit Controls — Box</title>
    <script src="https://aframe.io/releases/1.6.0/aframe.min.js"></script>
    <!-- Orbit Controls component (wraps THREE.OrbitControls) -->
    <script src="https://unpkg.com/aframe-orbit-controls@1.3.2/dist/aframe-orbit-controls.min.js"></script>
    <style>body{margin:0;overflow:hidden}</style>
  </head>
  <body>
    <a-scene background="color: #ECECEC">
      <!-- target object at (0,1,0) -->
      <a-box position="0 1 0" rotation="0 45 0" color="#4CC3D9" shadow></a-box>

      <!-- some lighting -->
      <a-entity light="type: ambient; intensity: 0.4"></a-entity>
      <a-entity light="type: directional; intensity: 0.9" position="2 4 3"></a-entity>

      <!-- camera with ORBIT CONTROLS (mouse/touch) -->
      <a-entity
        id="cam"
        camera
        position="0 1 5"
        look-controls="enabled: false"          <!-- avoid conflict -->
        wasd-controls-enabled="false"
        orbit-controls="
          target: 0 1 0;                        /* look-at point */
          enableDamping: true;
          dampingFactor: 0.12;
          rotateSpeed: 0.35;
          zoomSpeed: 0.9;
          panSpeed: 0.6;
          minDistance: 1;
          maxDistance: 20;
          minPolarAngle: 0.01;                  /* avoid flipping over the top */
          maxPolarAngle: 1.54;                  /* ~88 degrees */
        "
      ></a-entity>
    </a-scene>
  </body>
</html>
```

### wasd

```html
<html>
  <head>
    <meta charset="utf-8">
    <title>Cargar modelo GLB en A-Frame</title>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <!-- Carga de recursos -->
      <a-assets>
        <!-- Sustituye el src con la ruta o URL de tu archivo .glb -->
        <a-asset-item id="modelo" src="mapa.glb"></a-asset-item>
      </a-assets>

      <!-- Carga del modelo GLB -->
      <a-entity 
        gltf-model="#modelo"
        position="0 1 -2"
        scale="1 1 1"
        rotation="0 180 0">
      </a-entity>

      
    </a-scene>
  </body>
</html>
```

### hablemos de luces

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere position="0 1.25 -5" radius="1" color="#ffff00"></a-sphere>
    </a-scene>
  </body>
</html>
```

### apago la luz

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere position="0 1.25 -5" radius="1" color="#ffff00"></a-sphere>
      <a-sky color="#000000"></a-sky>
    </a-scene>
  </body>
</html>
```

### ahora quito toda luz

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere position="0 1.25 -5" radius="1" color="#ffff00"></a-sphere>
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0"></a-entity>
    </a-scene>
  </body>
</html>
```

### la luz ambiental es un relleno

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere position="0 1.25 -5" radius="1" color="#ffff00"></a-sphere>
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.5"></a-entity>
    </a-scene>
  </body>
</html>
```

### tenemos luces direccionales

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere position="0 1.25 -5" radius="1" color="#ffff00"></a-sphere>
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.5"></a-entity>
      <a-entity light="type: directional; intensity: 0.9" position="2 4 -3"></a-entity>
    </a-scene>
  </body>
</html>
```

### materiales

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere 
        position="0 1.25 -5" 
        radius="1" 
        color="#ffff00"
        material="color: #ff0000; specular: #ffffff; shininess: 50"
        ></a-sphere>
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.5"></a-entity>
      <a-entity light="type: directional; intensity: 0.9" position="2 4 -3"></a-entity>
    </a-scene>
  </body>
</html>
```

### especularidad

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere 
        position="0 1.25 -5" 
        radius="1" 
        color="#ffff00"
        material="color: #ff0000; specular: #00ff00; shininess: 50"
        ></a-sphere>
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.5"></a-entity>
      <a-entity light="type: directional; intensity: 0.9" position="2 4 -3"></a-entity>
    </a-scene>
  </body>
</html>
```

### brillo

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere 
        position="0 1.25 -5" 
        radius="1" 
        color="#ffff00"
        material="color: #ff0000; metalness: 0.2; roughness: 1"
      ></a-sphere>

      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.5"></a-entity>
      <a-entity light="type: directional; intensity: 0.9" position="2 4 -3"></a-entity>
    </a-scene>
  </body>
</html>
```

### texturas

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-sphere 
        position="0 1.25 -5" 
        radius="1" 
        color="#ffff00"
        material="color: #ff0000; metalness: 0.2; roughness: 1"
      ></a-sphere>

      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.5"></a-entity>
      <a-entity light="type: directional; intensity: 0.9" position="2 4 -3"></a-entity>
    </a-scene>
  </body>
</html>
```

### textura tierra

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <!-- Textura de la Tierra -->
      <a-assets>
        <img id="texturatierra" src="nasatierra.jpg">
      </a-assets>

      <a-sphere 
        position="0 1.25 -5" 
        radius="3" 
        material="src: #texturatierra; metalness: 0.2; roughness: 0.5"
      ></a-sphere>

      <!-- Cielo y luces -->
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.0"></a-entity>
      <a-entity light="type: directional; intensity: 10" position="2 4 0"></a-entity>
    </a-scene>
  </body>
</html>
```

### textura rugosidad

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <!-- Texturas -->
      <a-assets>
        <img id="texturatierra" src="nasatierra.jpg">
        <img id="rugosidadtierra" src="rugosidad.jpg">
      </a-assets>

      <!-- Esfera de la Tierra -->
      <a-sphere 
        position="0 1.25 -5" 
        radius="3" 
        material="src: #texturatierra; metalness: 0.2; roughness: 0.5; roughnessMap: #rugosidadtierra"
      ></a-sphere>

      <!-- Cielo y luces -->
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.2"></a-entity>
      <a-entity light="type: directional; intensity: 2" position="2 4 0"></a-entity>
    </a-scene>
  </body>
</html>
```

### esfera de nubes

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <!-- Texturas -->
      <a-assets>
        <img id="texturatierra" src="nasatierra.jpg">
        <img id="rugosidadtierra" src="rugosidad.jpg">
      </a-assets>

      <!-- Esfera de la Tierra -->
      <a-sphere 
        position="0 1.25 -5" 
        radius="3" 
        material="src: #texturatierra; metalness: 0.2; roughness: 0.5; roughnessMap: #rugosidadtierra"
      ></a-sphere>
      
      <a-sphere 
        position="0 1.25 -5" 
        radius="3.2" 
        
      ></a-sphere>

      <!-- Cielo y luces -->
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.2"></a-entity>
      <a-entity light="type: directional; intensity: 2" position="2 4 0"></a-entity>
    </a-scene>
  </body>
</html>
```

### transparencia

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <!-- Textures -->
      <a-assets>
        <img id="texturatierra" src="nasatierra.jpg">
        <img id="rugosidadtierra" src="rugosidad.jpg">
        <img id="nubes" src="nasanubes.png">
      </a-assets>

      <!-- Inner Earth sphere -->
      <a-sphere 
        position="0 1.25 -5" 
        radius="3" 
        material="src: #texturatierra; metalness: 0.2; roughness: 0.5; roughnessMap: #rugosidadtierra"
      ></a-sphere>

      <!-- Outer cloud layer -->
      <a-sphere 
        position="0 1.25 -5" 
        radius="3.05"
        segments-width="64"
        segments-height="64"
        material="src: #nubes; alphaMap: #nubes; transparent: true; side: double; metalness: 0; roughness: 1"
      ></a-sphere>

      <!-- Sky and lighting -->
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.2"></a-entity>
      <a-entity light="type: directional; intensity: 2" position="2 4 0"></a-entity>
    </a-scene>
  </body>
</html>
```

### animacion tierra

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <!-- Texturas -->
      <a-assets>
        <img id="texturatierra" src="nasatierra.jpg">
        <img id="rugosidadtierra" src="rugosidad.jpg">
        <img id="nubes" src="nasanubes.png">
      </a-assets>

      <!-- Esfera interna (Tierra) -->
      <a-sphere 
        position="0 1.25 -5" 
        radius="3" 
        material="src: #texturatierra; metalness: 0.01; roughness: 0.8; roughnessMap: #rugosidadtierra"
        animation="property: rotation; to: 0 360 0; loop: true; dur: 30000; easing: linear"
      ></a-sphere>

      <!-- Capa externa (nubes) -->
      <a-sphere 
        position="0 1.25 -5" 
        radius="3.05"
        segments-width="64"
        segments-height="64"
        material="src: #nubes; alphaMap: #nubes; transparent: true; side: double; metalness: 0; roughness: 1"
        animation="property: rotation; to: 0 360 0; loop: true; dur: 60000; easing: linear"
      ></a-sphere>

      <!-- Cielo y luces -->
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.2"></a-entity>
      <a-entity light="type: directional; intensity: 20" position="2 4 0"></a-entity>
    </a-scene>
  </body>
</html>
```

### jerarquia

```html
<html>
  <head>
    <script src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <!-- Texturas -->
      <a-assets>
        <img id="texturatierra" src="nasatierra.jpg">
        <img id="rugosidadtierra" src="rugosidad.jpg">
        <img id="nubes" src="nasanubes.png">
      </a-assets>

      <!-- EMPTY (contenedor que rota) -->
      <a-entity
        id="earthGroup"
        position="0 1.25 -5"
        animation="property: rotation; to: 0 360 0; loop: true; dur: 130000; easing: linear"
      >

        <!-- Esfera interna (Tierra) -->
        <a-sphere 
          radius="3" 
          material="src: #texturatierra; metalness: 0.01; roughness: 0.8; roughnessMap: #rugosidadtierra"
        ></a-sphere>

        <!-- Capa externa (nubes) -->
        <a-sphere 
          radius="3.05"
          segments-width="64"
          segments-height="64"
          material="src: #nubes; alphaMap: #nubes; transparent: true; side: double; metalness: 0; roughness: 1"
          
        ></a-sphere>

      </a-entity>

      <!-- Cielo y luces -->
      <a-sky color="#000000"></a-sky>
      <a-entity light="type: ambient; intensity: 0.2"></a-entity>
      <a-entity light="type: directional; intensity: 20" position="2 4 0"></a-entity>
    </a-scene>
  </body>
</html>
```

### postproceso

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>A-Frame Earth with Bloom</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- A-Frame + Post-Processing component (CDN build from project) -->
    <!-- Uses a build of A-Frame compatible with the component -->
    <script src="https://cdn.jsdelivr.net/gh/akbartus/A-Frame-Component-Postprocessing/dist/aframe.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/akbartus/A-Frame-Component-Postprocessing/dist/post-processing.min.js"></script>

    <style>
      html, body { margin: 0; height: 100%; background: #000; }
    </style>
  </head>
  <body>
    <!-- Enable post-processing with Bloom and tune parameters -->
    <a-scene
      post-processing="effect: bloom; bloomParams: threshold: 0.18, strength: 0.35, radius: 0.55, exposure: 1.0"
      renderer="colorManagement: true; physicallyCorrectLights: true;"
    >
      <!-- Textures -->
      <a-assets>
        <!-- Replace with your own asset paths if needed -->
        <img id="texturatierra" src="nasatierra.jpg" crossorigin="anonymous">
        <img id="rugosidadtierra" src="rugosidad.jpg" crossorigin="anonymous">
        <img id="nubes" src="nasanubes.png" crossorigin="anonymous">
      </a-assets>

      <!-- Rotating group -->
      <a-entity
        id="earthGroup"
        position="0 1.25 -5"
        animation="property: rotation; to: 0 360 0; loop: true; dur: 130000; easing: linear"
      >
        <!-- Earth -->
        <a-sphere
          radius="3"
          material="src: #texturatierra; metalness: 0.01; roughness: 0.8; roughnessMap: #rugosidadtierra"
        ></a-sphere>

        <!-- Clouds (slightly emissive to trigger bloom nicely) -->
        <a-sphere
          radius="3.05"
          segments-width="64"
          segments-height="64"
          material="
            src: #nubes;
            alphaMap: #nubes;
            transparent: true;
            side: double;
            metalness: 0;
            roughness: 1;
            emissive: #ffffff;
            emissiveIntensity: 0.25;
            emissiveMap: #nubes;
          "
        ></a-sphere>
      </a-entity>

      <!-- Sky and lights -->
      <a-sky color="#000000"></a-sky>

      <!-- Softer ambient so emissive stands out -->
      <a-entity light="type: ambient; intensity: 0.15"></a-entity>

      <!-- Directional “sun” light (keep it reasonable so bloom isn’t blown out) -->
      <a-entity light="type: directional; intensity: 2.5; color: #ffffff" position="2 4 0"></a-entity>

      <!-- Camera -->
      <a-entity position="0 1.6 0">
        <a-camera></a-camera>
      </a-entity>
    </a-scene>
  </body>
</html>
```

<a id="componentes-de-un-motor-de-juegos"></a>
## Componentes de un motor de juegos

En el análisis de motores de juegos, los componentes desempeñan un papel crucial en su funcionamiento y eficiencia. Estos componentes son la base sobre la cual se construyen las funcionalidades y características que hacen a un juego interactivo y envolvente para los jugadores. Los principales componentes incluyen el motor gráfico, el sistema de física, el control de entrada, la gestión del audio y la inteligencia artificial.

El motor gráfico es uno de los componentes fundamentales de cualquier motor de juegos. Se encarga de renderizar los elementos visuales en pantalla, desde personajes hasta escenas complejas. Este componente utiliza técnicas avanzadas como la programación de sombras, el mapeo de texturas y la optimización de la memoria gráfica para mantener un rendimiento óptimo.

El sistema de física es otro componente crucial que simula los efectos del mundo real dentro del juego. Desde la gravedad hasta las colisiones entre objetos, este sistema permite una interacción más natural y realista con el entorno virtual. La precisión y eficiencia en este aspecto son esenciales para mantener un juego fluido y dinámico.

El control de entrada es otro componente fundamental que maneja la interacción del jugador con el juego. Este componente puede incluir el procesamiento de teclas, el uso de controles de joystick o incluso el reconocimiento de gestos en dispositivos móviles. La capacidad de adaptarse a diferentes tipos de entrada y proporcionar una experiencia fluida es un aspecto clave para la satisfacción del jugador.

El gestión del audio es otro componente importante que contribuye significativamente al ambiente del juego. Desde los efectos sonoros hasta la música ambiental, el control adecuado del audio puede mejorar la inmersión del jugador y añadir una nueva dimensión a la experiencia de juego.

La inteligencia artificial (IA) es un componente emergente en motores de juegos que permite crear personajes y entornos más dinámicos y autónomos. Desde los enemigos que se mueven según patrones preestablecidos hasta los NPCs que interactúan con el jugador, la IA puede añadir una nueva dimensión a las experiencias de juego.

Además de estos componentes principales, existen otros elementos menos visibles pero igualmente importantes. Por ejemplo, el componente de gestión del tiempo controla los eventos y acciones dentro del juego en función del tiempo real, mientras que el componente de gestión de recursos se encarga de la carga y liberación eficiente de los archivos necesarios para mantener un rendimiento óptimo.

La integración de estos componentes requiere una comprensión profunda de la programación y las matemáticas aplicadas. Cada componente debe ser diseñado y optimizado cuidadosamente para garantizar que funcione en conjunto sin interferencias ni pérdidas de rendimiento.

En conclusión, los componentes de un motor de juegos son el esqueleto sobre el cual se construyen las experiencias interactivas y envolventes. Cada uno desempeña un papel crucial en la creación de un juego que sea atractivo, jugable y memorable para los jugadores. A través del análisis y optimización de estos componentes, los desarrolladores pueden crear motores de juegos más avanzados y eficientes, permitiendo una mayor creatividad y diversidad en las experiencias de juego disponibles.

### grid de elementos

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Portfolio Grid 1920×1080</title>
<style>
  :root{
    --bg: #0b0f14;
    --card: #0f1720;
    --ink: #e6eef9;
    --muted: #a9b6c7;
    --ring: #4da3ff;
    --gap: 24px;
    --pad: 32px;
    --radius: 18px;
  }

  /* Fill the screen, prevent scroll */
  html, body { height: 100%; }
  body{
    margin:0;
    background: radial-gradient(1200px 1200px at 80% -20%, #15314d 0%, #0b0f14 60%) fixed;
    color: var(--ink);
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    overflow: hidden; /* keep everything on-screen */
  }

  .wrap{
    box-sizing: border-box;
    height: 100vh; /* lock to viewport height */
    padding: var(--pad);
    display: grid;
    grid-template-rows: auto 1fr;
    gap: var(--gap);
  }

  header{
    display: flex;
    align-items: baseline;
    justify-content: space-between;
  }
  h1{
    margin:0;
    font-weight: 700;
    letter-spacing: 0.2px;
    font-size: clamp(18px, 2.2vw, 32px);
  }
  .subtitle{
    color: var(--muted);
    font-size: clamp(12px, 1.2vw, 16px);
  }

  /* 4×3 grid – fills the remaining space exactly */
  .grid{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 1fr);
    gap: var(--gap);
    height: 100%;
    width: 100%;
  }

  /* Cards */
  .card{
    position: relative;
    border-radius: var(--radius);
    overflow: hidden;
    background: var(--card);
    box-shadow:
      0 1px 0 rgba(255,255,255,0.05) inset,
      0 10px 30px rgba(0,0,0,0.35);
    isolation: isolate;
    transform: translateZ(0); /* new stacking context for crisp transforms */
    will-change: transform, box-shadow;
    transition: transform .25s ease, box-shadow .25s ease;
  }
  .card:hover{
    transform: scale(1.02);
    box-shadow:
      0 1px 0 rgba(255,255,255,0.06) inset,
      0 18px 48px rgba(0,0,0,0.45);
  }

  /* Placeholder media */
  .thumb{
    position:absolute; inset:0;
    background:
      linear-gradient(to bottom right, rgba(255,255,255,0.06), rgba(255,255,255,0.0)),
      repeating-linear-gradient(135deg, rgba(255,255,255,0.06) 0 2px, transparent 2px 6px),
      radial-gradient(120% 120% at 0% 0%, #204a72 0%, #132336 45%, #0f1720 80%);
    /* Optional: image slot
       background: url("your-image.jpg") center/cover no-repeat; */
    filter: saturate(1.1);
  }

  /* Gradient veil for legible captions */
  .veil{
    position:absolute; inset:0;
    background: linear-gradient(to top, rgba(0,0,0,.55) 0 35%, rgba(0,0,0,0) 60%);
    pointer-events: none;
  }

  /* Caption bar */
  .meta{
    position:absolute; left:16px; right:16px; bottom:14px;
    display:flex; align-items:center; justify-content:space-between;
    gap: 12px;
  }
  .title{
    font-weight: 650;
    font-size: clamp(12px, 1.1vw, 18px);
    text-shadow: 0 1px 2px rgba(0,0,0,.6);
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .tag{
    font-size: clamp(10px, .9vw, 13px);
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(77,163,255,.14);
    color: #cfe5ff;
    border: 1px solid rgba(77,163,255,.25);
    backdrop-filter: blur(4px);
  }

  /* Focus style for accessibility */
  .card:focus-visible{
    outline: 3px solid var(--ring);
    outline-offset: 3px;
  }

  /* Small screens: keep all items visible without scrolling by shrinking gaps/padding */
  @media (max-aspect-ratio: 16/10), (max-width: 1200px){
    :root{ --gap: 16px; --pad: 16px; }
    .title{ font-size: clamp(12px, 2.2vw, 16px); }
    .tag{ font-size: clamp(10px, 1.8vw, 12px); }
  }
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>My Portfolio</h1>
      <div class="subtitle">12 projects — fits on screen (1920×1080)</div>
    </header>

    <section class="grid" aria-label="Portfolio items">
      <!-- 12 cards (4×3). Replace placeholder backgrounds with images if you like -->
      <!-- Card 1 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Landing Page Redesign</div>
          <div class="tag">Web</div>
        </div>
      </article>

      <!-- Card 2 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">E-commerce UI Kit</div>
          <div class="tag">UI</div>
        </div>
      </article>

      <!-- Card 3 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Motion Graphics Reel</div>
          <div class="tag">Motion</div>
        </div>
      </article>

      <!-- Card 4 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Brand System “Aurora”</div>
          <div class="tag">Branding</div>
        </div>
      </article>

      <!-- Card 5 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Mobile App Dashboard</div>
          <div class="tag">App</div>
        </div>
      </article>

      <!-- Card 6 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">3D Product Shots</div>
          <div class="tag">3D</div>
        </div>
      </article>

      <!-- Card 7 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Data Viz Suite</div>
          <div class="tag">Analytics</div>
        </div>
      </article>

      <!-- Card 8 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Illustration Pack</div>
          <div class="tag">Art</div>
        </div>
      </article>

      <!-- Card 9 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Marketing Microsite</div>
          <div class="tag">Web</div>
        </div>
      </article>

      <!-- Card 10 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Icon Set “Orbit”</div>
          <div class="tag">Icons</div>
        </div>
      </article>

      <!-- Card 11 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Corporate Templates</div>
          <div class="tag">Docs</div>
        </div>
      </article>

      <!-- Card 12 -->
      <article class="card" tabindex="0">
        <div class="thumb"></div>
        <div class="veil"></div>
        <div class="meta">
          <div class="title">Photography Series</div>
          <div class="tag">Photo</div>
        </div>
      </article>
    </section>
  </div>
</body>
</html>
```

### camara con perspectiva

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Portfolio Grid • CSS3D Side-Bottom Camera</title>
<style>
  :root{
    --bg: #0b0f14;
    --card: #0f1720;
    --ink: #e6eef9;
    --muted: #a9b6c7;
    --ring: #4da3ff;
    --gap: 24px;
    --pad: 32px;
    --radius: 18px;
    --perspective: 1400px; /* camera distance */
  }

  html, body { height: 100%; }
  body{
    margin:0;
    color:var(--ink);
    overflow:hidden; /* keep everything on screen */
    background: radial-gradient(1200px 1200px at 80% -20%, #15314d 0%, #0b0f14 60%) fixed;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, "Noto Sans";
  }

  /* 3D scene: establishes perspective from a low, left-side vantage */
  .scene{
    height: 100vh;
    padding: var(--pad);
    box-sizing: border-box;
    perspective: var(--perspective);
    perspective-origin: 0% 100%; /* bottom-left => side-bottom camera */
    display: grid;
    grid-template-rows: auto 1fr;
    gap: var(--gap);
  }

  header{
    display:flex;align-items:baseline;justify-content:space-between;
    transform-style: preserve-3d;
  }
  h1{ margin:0; font-weight:700; letter-spacing:.2px; font-size: clamp(18px, 2.2vw, 32px);}
  .subtitle{ color:var(--muted); font-size: clamp(12px, 1.2vw, 16px); }

  /* Stage is the plane we tilt in 3D */
  .stage{
    position: relative;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    /* Low-angle, from bottom-left looking to top-right */
    transform:
      translateZ(0)
      rotateX(18deg)   /* tip away from camera (looking up) */
      rotateY(-22deg)  /* camera from the left side */
      scale(.92);      /* keep within viewport after tilt */
    transform-origin: 0% 100%;
    will-change: transform;
  }

  /* Optional floor shadow for depth cue */
  .floor-shadow{
    position:absolute; inset:-6% -10% -25% -10%;
    background:
      radial-gradient(120% 35% at 15% 100%,
        rgba(0,0,0,.45) 0%,
        rgba(0,0,0,.25) 35%,
        rgba(0,0,0,0) 70%);
    transform: translateZ(-200px) rotateX(90deg);
    pointer-events:none;
  }

  /* Grid sits on the stage */
  .grid{
    position:relative;
    width:100%; height:100%;
    display:grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 1fr);
    gap: var(--gap);
    transform-style: preserve-3d;
  }

  /* Cards (with their own 3D) */
  .card{
    position:relative;
    border-radius: var(--radius);
    overflow:hidden;
    background: var(--card);
    box-shadow:
      0 1px 0 rgba(255,255,255,0.05) inset,
      0 10px 30px rgba(0,0,0,0.35);
    transform-style: preserve-3d;
    transition: transform .25s ease, box-shadow .25s ease, filter .25s ease;
    will-change: transform, box-shadow, filter;
  }

  .thumb{
    position:absolute; inset:0;
    background:
      linear-gradient(to bottom right, rgba(255,255,255,0.06), rgba(255,255,255,0.0)),
      repeating-linear-gradient(135deg, rgba(255,255,255,0.06) 0 2px, transparent 2px 6px),
      radial-gradient(120% 120% at 0% 0%, #204a72 0%, #132336 45%, #0f1720 80%);
    transform: translateZ(1px); /* lift slightly above the card plane */
  }

  .veil{
    position:absolute; inset:0;
    background: linear-gradient(to top, rgba(0,0,0,.55) 0 35%, rgba(0,0,0,0) 60%);
    transform: translateZ(2px);
    pointer-events:none;
  }

  .meta{
    position:absolute; left:16px; right:16px; bottom:14px;
    display:flex; align-items:center; justify-content:space-between; gap:12px;
    transform: translateZ(8px); /* bring text closer to camera */
  }
  .title{
    font-weight:650; font-size: clamp(12px, 1.1vw, 18px);
    text-shadow: 0 1px 2px rgba(0,0,0,.6);
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .tag{
    font-size: clamp(10px, .9vw, 13px);
    padding: 6px 10px; border-radius: 999px;
    background: rgba(77,163,255,.14); color: #cfe5ff;
    border: 1px solid rgba(77,163,255,.25);
    backdrop-filter: blur(4px);
  }

  /* 3D hover: cards lift toward the camera and subtly counter-tilt */
  .card:hover{
    transform:
      translateZ(40px)
      rotateX(-2.5deg)
      rotateY(2.5deg);
    box-shadow:
      0 1px 0 rgba(255,255,255,0.06) inset,
      0 22px 60px rgba(0,0,0,0.5);
    filter: saturate(1.08);
  }

  /* Focus ring still works in 3D */
  .card:focus-visible{
    outline: 3px solid var(--ring);
    outline-offset: 3px;
  }

  /* Keep it tight on smaller screens/aspect ratios */
  @media (max-aspect-ratio: 16/10), (max-width: 1200px){
    :root{ --gap:16px; --pad:16px; --perspective: 1100px; }
    .stage{ transform:
      translateZ(0) rotateX(16deg) rotateY(-20deg) scale(.92); }
  }
</style>
</head>
<body>
  <div class="scene">
    <header>
      <h1>My Portfolio — CSS3D</h1>
      <div class="subtitle">Low side-bottom perspective (4×3, all on screen)</div>
    </header>

    <!-- 3D stage (tilted plane) -->
    <div class="stage" aria-hidden="false">
      <div class="floor-shadow"></div>

      <!-- Grid on the tilted stage -->
      <section class="grid" aria-label="Portfolio items">
        <!-- 12 cards -->
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Landing Page Redesign</div><div class="tag">Web</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">E-commerce UI Kit</div><div class="tag">UI</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Motion Graphics Reel</div><div class="tag">Motion</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Brand System “Aurora”</div><div class="tag">Branding</div></div>
        </article>

        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Mobile App Dashboard</div><div class="tag">App</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">3D Product Shots</div><div class="tag">3D</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Data Viz Suite</div><div class="tag">Analytics</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Illustration Pack</div><div class="tag">Art</div></div>
        </article>

        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Marketing Microsite</div><div class="tag">Web</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Icon Set “Orbit”</div><div class="tag">Icons</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Corporate Templates</div><div class="tag">Docs</div></div>
        </article>
        <article class="card" tabindex="0">
          <div class="thumb"></div><div class="veil"></div>
          <div class="meta"><div class="title">Photography Series</div><div class="tag">Photo</div></div>
        </article>
      </section>
    </div>
  </div>
</body>
</html>
```

### css y javascript

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Portfolio Grid • CSS3D Parallax + Hover Depth</title>
<style>
  :root{
    --bg: #0b0f14;
    --card: #0f1720;
    --ink: #e6eef9;
    --muted: #a9b6c7;
    --ring: #4da3ff;
    --gap: 24px;
    --pad: 32px;
    --radius: 18px;
    --perspective: 1400px;
    --rx: 0deg; /* stage rotations controlled by JS */
    --ry: 0deg;
    --stageScale: .96; /* slight zoom-out to keep inside viewport when rotated */
  }

  html, body { height: 100%; }
  body{
    margin:0; color:var(--ink); overflow:hidden;
    background: radial-gradient(1200px 1200px at 80% -20%, #15314d 0%, #0b0f14 60%) fixed;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, "Noto Sans";
  }

  /* Scene = camera holder */
  .scene{
    height: 100vh; padding: var(--pad); box-sizing: border-box;
    perspective: var(--perspective);
    perspective-origin: 50% 75%; /* slightly below center feels “low camera” */
    display: grid; grid-template-rows: auto 1fr; gap: var(--gap);
  }

  header{ display:flex; align-items:baseline; justify-content:space-between; }
  h1{ margin:0; font-weight:700; letter-spacing:.2px; font-size: clamp(18px, 2.2vw, 32px); }
  .subtitle{ color:var(--muted); font-size: clamp(12px, 1.2vw, 16px); }

  /* Stage rotates in real 3D based on CSS vars (--rx, --ry) */
  .stage{
    position: relative; width:100%; height:100%;
    transform-style: preserve-3d;
    transform:
      translateZ(0)
      rotateX(var(--rx))
      rotateY(var(--ry))
      scale(var(--stageScale));
    transform-origin: 50% 80%;
    will-change: transform;
  }

  .floor-shadow{
    position:absolute; inset:-6% -10% -25% -10%;
    background:
      radial-gradient(120% 35% at 50% 100%,
        rgba(0,0,0,.45) 0%,
        rgba(0,0,0,.25) 35%,
        rgba(0,0,0,0) 70%);
    transform: translateZ(-220px) rotateX(90deg);
    pointer-events:none;
  }

  .grid{
    position:relative; width:100%; height:100%;
    display:grid; gap: var(--gap);
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 1fr);
    transform-style: preserve-3d;
  }

  .card{
    position:relative; border-radius: var(--radius); overflow:hidden;
    background: var(--card);
    box-shadow:
      0 1px 0 rgba(255,255,255,0.05) inset,
      0 10px 30px rgba(0,0,0,0.35);
    transform-style: preserve-3d;
    transition:
      transform .25s ease,
      box-shadow .25s ease,
      filter .25s ease;
    will-change: transform, box-shadow, filter;
    /* Each card gets a dynamic Z from JS via the --dz custom property */
    --dz: 0px;
    transform: translateZ(var(--dz));
  }

  .card:hover{
    transform:
      translateZ(calc(var(--dz) + 70px))
      rotateX(-2deg)
      rotateY(2deg);
    box-shadow:
      0 1px 0 rgba(255,255,255,0.06) inset,
      0 22px 60px rgba(0,0,0,0.5);
    filter: saturate(1.08);
  }

  .thumb{
    position:absolute; inset:0;
    background:
      linear-gradient(to bottom right, rgba(255,255,255,0.06), rgba(255,255,255,0.0)),
      repeating-linear-gradient(135deg, rgba(255,255,255,0.06) 0 2px, transparent 2px 6px),
      radial-gradient(120% 120% at 0% 0%, #204a72 0%, #132336 45%, #0f1720 80%);
    transform: translateZ(1px);
  }

  .veil{
    position:absolute; inset:0;
    background: linear-gradient(to top, rgba(0,0,0,.55) 0 35%, rgba(0,0,0,0) 60%);
    transform: translateZ(2px);
    pointer-events:none;
  }

  .meta{
    position:absolute; left:16px; right:16px; bottom:14px;
    display:flex; align-items:center; justify-content:space-between; gap:12px;
    transform: translateZ(8px);
  }
  .title{
    font-weight:650; font-size: clamp(12px, 1.1vw, 18px);
    text-shadow: 0 1px 2px rgba(0,0,0,.6);
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .tag{
    font-size: clamp(10px, .9vw, 13px);
    padding: 6px 10px; border-radius: 999px;
    background: rgba(77,163,255,.14); color: #cfe5ff;
    border: 1px solid rgba(77,163,255,.25);
    backdrop-filter: blur(4px);
  }

  .card:focus-visible{ outline: 3px solid var(--ring); outline-offset: 3px; }

  @media (max-aspect-ratio: 16/10), (max-width: 1200px){
    :root{ --gap: 16px; --pad: 16px; --perspective: 1100px; }
  }
</style>
</head>
<body>
  <div class="scene" id="scene">
    <header>
      <h1>CSS3D Parallax Portfolio</h1>
      <div class="subtitle">Move mouse for camera parallax • Hover a card to pop</div>
    </header>

    <div class="stage" id="stage">
      <div class="floor-shadow"></div>
      <section class="grid" id="grid" aria-label="Portfolio items">
        <!-- 12 cards -->
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Landing Page Redesign</div><div class="tag">Web</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">E-commerce UI Kit</div><div class="tag">UI</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Motion Graphics Reel</div><div class="tag">Motion</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Brand System “Aurora”</div><div class="tag">Branding</div></div></article>

        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Mobile App Dashboard</div><div class="tag">App</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">3D Product Shots</div><div class="tag">3D</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Data Viz Suite</div><div class="tag">Analytics</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Illustration Pack</div><div class="tag">Art</div></div></article>

        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Marketing Microsite</div><div class="tag">Web</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Icon Set “Orbit”</div><div class="tag">Icons</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Corporate Templates</div><div class="tag">Docs</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Photography Series</div><div class="tag">Photo</div></div></article>
      </section>
    </div>
  </div>

<script>
(() => {
  const scene = document.getElementById('scene');
  const stage = document.getElementById('stage');
  const cards = Array.from(document.querySelectorAll('.card'));

  // Config
  const maxRotateX = 10;  // degrees (up/down)
  const maxRotateY = 14;  // degrees (left/right)
  const maxCardDepth = 30; // px extra Z per card based on pointer proximity
  const ease = 0.12;      // easing for camera

  let targetRX = 0, targetRY = 0; // desired rotation in degrees
  let curRX = 0, curRY = 0;

  // Cache card centers for depth parallax
  const cardRects = () => cards.map(el => {
    const r = el.getBoundingClientRect();
    return { el, cx: r.left + r.width/2, cy: r.top + r.height/2, w: r.width, h: r.height };
  });
  let cached = cardRects();

  // Recompute on resize
  window.addEventListener('resize', () => { cached = cardRects(); });

  // Mouse/Touch mapping to normalized -1..1 coords (center = 0,0)
  const getNorm = (clientX, clientY) => {
    const r = scene.getBoundingClientRect();
    const x = (clientX - (r.left + r.width/2)) / (r.width/2);
    const y = (clientY - (r.top + r.height/2)) / (r.height/2);
    return { nx: Math.max(-1, Math.min(1, x)), ny: Math.max(-1, Math.min(1, y)) };
  };

  // Update targets on pointer move
  const onPointerMove = (e) => {
    const pt = e.touches ? e.touches[0] : e;
    const { nx, ny } = getNorm(pt.clientX, pt.clientY);
    // center (0,0) => straight-on (0deg, 0deg)
    targetRY = -nx * maxRotateY; // move mouse right => rotateY negative to face right side
    targetRX =  ny * maxRotateX; // move mouse down  => rotateX positive (tilt down)
    applyCardDepth(pt.clientX, pt.clientY);
  };

  // Depth parallax per card: closer to pointer => slightly forward
  function applyCardDepth(x, y){
    cached.forEach(({ el, cx, cy, w, h }) => {
      // distance normalized: 0 at center of card, ~1 at ~card-diagonal
      const dx = (x - cx) / (w * 0.5);
      const dy = (y - cy) / (h * 0.5);
      const d = Math.sqrt(dx*dx + dy*dy);
      // Invert and clamp: 1 near center, 0 far
      const influence = Math.max(0, 1 - d);
      const z = influence * maxCardDepth;
      el.style.setProperty('--dz', `${z.toFixed(1)}px`);
    });
  }

  // Reset depth when pointer leaves the window
  const resetDepth = () => {
    targetRX = 0; targetRY = 0;
    cards.forEach(el => el.style.setProperty('--dz', `0px`));
  };

  window.addEventListener('pointermove', onPointerMove, { passive: true });
  window.addEventListener('touchmove', onPointerMove, { passive: true });
  window.addEventListener('pointerleave', resetDepth);
  window.addEventListener('blur', resetDepth);

  // rAF loop to ease camera toward target
  function tick(){
    curRX += (targetRX - curRX) * ease;
    curRY += (targetRY - curRY) * ease;
    stage.style.setProperty('--rx', `${curRX.toFixed(3)}deg`);
    stage.style.setProperty('--ry', `${curRY.toFixed(3)}deg`);
    requestAnimationFrame(tick);
  }
  tick();

  // Optional: keyboard focus depth bump, for accessibility
  cards.forEach(card => {
    card.addEventListener('focus', () => card.style.setProperty('--dz', `40px`));
    card.addEventListener('blur',  () => card.style.setProperty('--dz', `0px`));
  });
})();
</script>
</body>
</html>
```

### capas de profundidad

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>CSS3D Portfolio • Parallax + Layered Depth</title>
<style>
  :root{
    --bg: #0b0f14;
    --card: #0f1720;
    --ink: #e6eef9;
    --muted: #a9b6c7;
    --ring: #4da3ff;
    --gap: 24px;
    --pad: 32px;
    --radius: 18px;
    --perspective: 1400px;

    /* Camera rotations (set by JS) */
    --rx: 0deg;
    --ry: 0deg;

    /* Mouse normalized position (set by JS, -1..1) */
    --mx: 0;
    --my: 0;

    /* Slight zoom-out to keep everything inside viewport while rotating */
    --stageScale: .96;
  }

  html, body { height: 100%; }
  body{
    margin:0; color:var(--ink); overflow:hidden;
    background:
      radial-gradient(1200px 1200px at 80% -20%, #15314d 0%, #0b0f14 60%) fixed;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, "Noto Sans";
  }

  /* Scene gives us perspective (camera) */
  .scene{
    height: 100vh; padding: var(--pad); box-sizing: border-box;
    perspective: var(--perspective);
    perspective-origin: 50% 75%;
    display: grid; grid-template-rows: auto 1fr; gap: var(--gap);
  }

  header{ display:flex; align-items:baseline; justify-content:space-between; }
  h1{ margin:0; font-weight:700; letter-spacing:.2px; font-size: clamp(18px, 2.2vw, 32px); }
  .subtitle{ color:var(--muted); font-size: clamp(12px, 1.2vw, 16px); }

  /* Stage holds everything that rotates in 3D */
  .stage{
    position: relative; width:100%; height:100%;
    transform-style: preserve-3d;
    transform:
      translateZ(0)
      rotateX(var(--rx))
      rotateY(var(--ry))
      scale(var(--stageScale));
    transform-origin: 50% 80%;
    will-change: transform;
  }

  /* BACKGROUND DEPTH LAYERS (SVG masks punch real transparent holes) */
  .depth-layer{
    position:absolute; inset:0;
    transform-style: preserve-3d;
    pointer-events:none;
    will-change: transform;
    /* Each layer uses its own --z, --px, --py (set inline) */
    transform:
      translate3d(
        calc(var(--mx) * var(--px)),
        calc(var(--my) * var(--py)),
        var(--z)
      )
      rotateX(0deg) rotateY(0deg) scale(3,3);
  }

  /* A soft floor shadow to sell depth */
  .floor-shadow{
    position:absolute; inset:-6% -10% -25% -10%;
    background:
      radial-gradient(120% 35% at 50% 100%,
        rgba(0,0,0,.42) 0%,
        rgba(0,0,0,.24) 35%,
        rgba(0,0,0,0) 70%);
    transform: translateZ(-220px) rotateX(90deg);
    pointer-events:none;
  }

  /* GRID */
  .grid{
    position:relative; width:100%; height:100%;
    display:grid; gap: var(--gap);
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 1fr);
    transform-style: preserve-3d;
  }

  /* CARDS */
  .card{
    position:relative; border-radius: var(--radius); overflow:hidden;
    background: var(--card);
    box-shadow:
      0 1px 0 rgba(255,255,255,0.05) inset,
      0 10px 30px rgba(0,0,0,0.35);
    transform-style: preserve-3d;
    transition:
      transform .25s ease,
      box-shadow .25s ease,
      filter .25s ease;
    will-change: transform, box-shadow, filter;
    --dz: 0px;               /* depth from pointer proximity (JS) */
    transform: translateZ(var(--dz));
  }
  .card:hover{
    transform:
      translateZ(calc(var(--dz) + 70px))
      rotateX(-2deg)
      rotateY(2deg);
    box-shadow:
      0 1px 0 rgba(255,255,255,0.06) inset,
      0 22px 60px rgba(0,0,0,0.5);
    filter: saturate(1.08);
  }

  .thumb{
    position:absolute; inset:0;
    background:
      linear-gradient(to bottom right, rgba(255,255,255,0.06), rgba(255,255,255,0.0)),
      repeating-linear-gradient(135deg, rgba(255,255,255,0.06) 0 2px, transparent 2px 6px),
      radial-gradient(120% 120% at 0% 0%, #204a72 0%, #132336 45%, #0f1720 80%);
    transform: translateZ(1px);
  }
  .veil{
    position:absolute; inset:0;
    background: linear-gradient(to top, rgba(0,0,0,.55) 0 35%, rgba(0,0,0,0) 60%);
    transform: translateZ(2px);
    pointer-events:none;
  }
  .meta{
    position:absolute; left:16px; right:16px; bottom:14px;
    display:flex; align-items:center; justify-content:space-between; gap:12px;
    transform: translateZ(8px);
  }
  .title{
    font-weight:650; font-size: clamp(12px, 1.1vw, 18px);
    text-shadow: 0 1px 2px rgba(0,0,0,.6);
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .tag{
    font-size: clamp(10px, .9vw, 13px);
    padding: 6px 10px; border-radius: 999px;
    background: rgba(77,163,255,.14); color: #cfe5ff;
    border: 1px solid rgba(77,163,255,.25);
    backdrop-filter: blur(4px);
  }
  .card:focus-visible{ outline: 3px solid var(--ring); outline-offset: 3px; }

  @media (max-aspect-ratio: 16/10), (max-width: 1200px){
    :root{ --gap:16px; --pad:16px; --perspective: 1100px; }
  }
</style>
</head>
<body>
  <div class="scene" id="scene">
    <header>
      <h1>CSS3D Parallax Portfolio</h1>
      <div class="subtitle">Move mouse: camera parallax • Hover: 3D pop • Layered depth background</div>
    </header>

    <div class="stage" id="stage">
      <!-- Depth layers (SVG masks create transparent “holes”) -->
      <!-- FAR layer -->
      <svg class="depth-layer" style="--z:-220px; --px:16px; --py:22px" viewBox="0 0 1920 1080" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <mask id="mask-far">
            <rect x="0" y="0" width="1920" height="1080" fill="white"/>
            <!-- holes (black = transparent in mask) -->
            <circle cx="200" cy="180" r="80" fill="black"/>
            <circle cx="520" cy="260" r="55" fill="black"/>
            <circle cx="860" cy="160" r="70" fill="black"/>
            <circle cx="1280" cy="230" r="85" fill="black"/>
            <circle cx="1650" cy="160" r="65" fill="black"/>
            <circle cx="320" cy="520" r="95" fill="black"/>
            <circle cx="720" cy="620" r="60" fill="black"/>
            <circle cx="1120" cy="560" r="75" fill="black"/>
            <circle cx="1520" cy="580" r="90" fill="black"/>
            <circle cx="420" cy="900" r="80" fill="black"/>
            <circle cx="980" cy="880" r="65" fill="black"/>
            <circle cx="1500" cy="880" r="78" fill="black"/>
          </mask>
        </defs>
        <rect x="0" y="0" width="1920" height="1080"
              fill="rgba(77,163,255,0.10)" mask="url(#mask-far)"/>
      </svg>

      <!-- MID layer -->
      <svg class="depth-layer" style="--z:-180px; --px:28px; --py:36px" viewBox="0 0 1920 1080" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <mask id="mask-mid">
            <rect x="0" y="0" width="1920" height="1080" fill="white"/>
            <circle cx="160" cy="140" r="70" fill="black"/>
            <circle cx="460" cy="200" r="42" fill="black"/>
            <circle cx="780" cy="140" r="58" fill="black"/>
            <circle cx="1180" cy="210" r="72" fill="black"/>
            <circle cx="1700" cy="180" r="52" fill="black"/>
            <circle cx="260" cy="500" r="75" fill="black"/>
            <circle cx="640" cy="640" r="48" fill="black"/>
            <circle cx="1010" cy="560" r="62" fill="black"/>
            <circle cx="1400" cy="620" r="78" fill="black"/>
            <circle cx="360" cy="900" r="72" fill="black"/>
            <circle cx="920" cy="900" r="54" fill="black"/>
            <circle cx="1440" cy="880" r="66" fill="black"/>
          </mask>
        </defs>
        <rect x="0" y="0" width="1920" height="1080"
              fill="rgba(77,163,255,0.14)" mask="url(#mask-mid)"/>
      </svg>

      <!-- NEAR layer -->
      <svg class="depth-layer" style="--z:-40px; --px:44px; --py:54px" viewBox="0 0 1920 1080" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <mask id="mask-near">
            <rect x="0" y="0" width="1920" height="1080" fill="white"/>
            <circle cx="120" cy="120" r="56" fill="black"/>
            <circle cx="420" cy="220" r="36" fill="black"/>
            <circle cx="740" cy="160" r="52" fill="black"/>
            <circle cx="1140" cy="240" r="58" fill="black"/>
            <circle cx="1740" cy="220" r="44" fill="black"/>
            <circle cx="220" cy="520" r="62" fill="black"/>
            <circle cx="600" cy="660" r="40" fill="black"/>
            <circle cx="980" cy="600" r="54" fill="black"/>
            <circle cx="1340" cy="660" r="62" fill="black"/>
            <circle cx="320" cy="920" r="60" fill="black"/>
            <circle cx="880" cy="920" r="46" fill="black"/>
            <circle cx="1380" cy="900" r="56" fill="black"/>
          </mask>
        </defs>
        <rect x="0" y="0" width="1920" height="1080"
              fill="rgba(77,163,255,0.18)" mask="url(#mask-near)"/>
      </svg>

      <div class="floor-shadow"></div>

      <!-- GRID (front content) -->
      <section class="grid" id="grid" aria-label="Portfolio items">
        <!-- 12 cards -->
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Landing Page Redesign</div><div class="tag">Web</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">E-commerce UI Kit</div><div class="tag">UI</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Motion Graphics Reel</div><div class="tag">Motion</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Brand System “Aurora”</div><div class="tag">Branding</div></div></article>

        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Mobile App Dashboard</div><div class="tag">App</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">3D Product Shots</div><div class="tag">3D</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Data Viz Suite</div><div class="tag">Analytics</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Illustration Pack</div><div class="tag">Art</div></div></article>

        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Marketing Microsite</div><div class="tag">Web</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Icon Set “Orbit”</div><div class="tag">Icons</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Corporate Templates</div><div class="tag">Docs</div></div></article>
        <article class="card" tabindex="0"><div class="thumb"></div><div class="veil"></div><div class="meta"><div class="title">Photography Series</div><div class="tag">Photo</div></div></article>
      </section>
    </div>
  </div>

<script>
(() => {
  const scene = document.getElementById('scene');
  const stage = document.getElementById('stage');
  const cards = Array.from(document.querySelectorAll('.card'));

  // Camera config
  const maxRotateX = 10;   // deg up/down
  const maxRotateY = 14;   // deg left/right
  const ease = 0.12;       // camera easing
  const maxCardDepth = 30; // px forward based on pointer proximity

  let targetRX = 0, targetRY = 0;
  let curRX = 0, curRY = 0;

  // Cache card rects
  const measure = () => cards.map(el => {
    const r = el.getBoundingClientRect();
    return { el, cx: r.left + r.width/2, cy: r.top + r.height/2, w: r.width, h: r.height };
  });
  let cached = measure();
  window.addEventListener('resize', () => { cached = measure(); });

  // Normalize pointer to [-1,1]
  const norm = (x, y) => {
    const r = scene.getBoundingClientRect();
    return {
      nx: Math.max(-1, Math.min(1, (x - (r.left + r.width/2)) / (r.width/2))),
      ny: Math.max(-1, Math.min(1, (y - (r.top + r.height/2)) / (r.height/2)))
    };
  };

  function onMove(e){
    const p = e.touches ? e.touches[0] : e;
    const { nx, ny } = norm(p.clientX, p.clientY);

    // Update CSS vars for parallax layers
    stage.style.setProperty('--mx', nx.toFixed(4));
    stage.style.setProperty('--my', ny.toFixed(4));

    // Camera target rotations (center => 0/0)
    targetRY = -nx * maxRotateY;
    targetRX =  ny * maxRotateX;

    // Depth per card relative to pointer proximity
    cached.forEach(({ el, cx, cy, w, h }) => {
      const dx = (p.clientX - cx) / (w * 0.5);
      const dy = (p.clientY - cy) / (h * 0.5);
      const d = Math.hypot(dx, dy);
      const influence = Math.max(0, 1 - d);  // 1 at center of card
      el.style.setProperty('--dz', `${(influence * maxCardDepth).toFixed(1)}px`);
    });
  }

  function reset(){
    targetRX = 0; targetRY = 0;
    stage.style.setProperty('--mx', '0');
    stage.style.setProperty('--my', '0');
    cards.forEach(el => el.style.setProperty('--dz', `0px`));
  }

  window.addEventListener('pointermove', onMove, { passive:true });
  window.addEventListener('touchmove', onMove, { passive:true });
  window.addEventListener('pointerleave', reset);
  window.addEventListener('blur', reset);

  // RAF camera easing
  (function tick(){
    curRX += (targetRX - curRX) * ease;
    curRY += (targetRY - curRY) * ease;
    stage.style.setProperty('--rx', `${curRX.toFixed(3)}deg`);
    stage.style.setProperty('--ry', `${curRY.toFixed(3)}deg`);
    requestAnimationFrame(tick);
  })();

  // Accessibility: focus bump
  cards.forEach(c => {
    c.addEventListener('focus', () => c.style.setProperty('--dz', `40px`));
    c.addEventListener('blur',  () => c.style.setProperty('--dz', `0px`));
  });
})();
</script>
</body>
</html>
```

<a id="librerias-que-proporcionan-las-funciones-basicas-de-un-motor-2d3d"></a>
## Librerías que proporcionan las funciones básicas de un Motor 2D3D

En la exploración del desarrollo de juegos 2D y 3D, una herramienta fundamental es el uso de librerías que proporcionan las funciones básicas de un motor de juegos. Estas librerías son como los bloques con los que se construyen los fundamentos de cualquier juego digital. Una de las principales ventajas de utilizar estas librerías es que abstraen muchos detalles complejos del hardware y el software, permitiendo a los desarrolladores centrarse en la creación de contenido y la implementación de funcionalidades específicas.

Una de las librerías más populares para el desarrollo de juegos 2D y 3D es Unity. Unity es una plataforma versátil que ofrece un conjunto completo de herramientas para crear experiencias interactivas, desde simples aplicaciones hasta juegos de alta complejidad. La biblioteca principal de Unity se llama UnityEngine, y proporciona acceso a una amplia gama de funcionalidades, incluyendo gestión de recursos gráficos, física, audio, entrada del usuario y más.

Otra librería importante es Unreal Engine, conocida por su potencia en el desarrollo de juegos 3D. Aunque ofrece un nivel de control mucho mayor que Unity, también proporciona una serie de herramientas y clases predefinidas para facilitar la creación de contenido visualmente impresionante. Unreal Engine utiliza su propio lenguaje de scripting, C++, pero también permite el uso de Blueprints, un sistema visual que es especialmente útil para principiantes.

Además de Unity y Unreal Engine, existen otras librerías populares como Godot, que ofrece una alternativa gratuita y de código abierto para la creación de juegos 2D y 3D. Godot utiliza su propio lenguaje de scripting GDScript, pero también admite C++. Uno de los aspectos destacados de Godot es su enfoque en el desarrollo rápido y la simplicidad, lo que lo hace una excelente opción para proyectos de prueba o prototipado.

Cada una de estas librerías tiene sus propias ventajas y desventajas, y la elección depende del proyecto específico, las habilidades del equipo y los recursos disponibles. Unity es generalmente preferida por su facilidad de uso y su gran comunidad de desarrolladores, mientras que Unreal Engine ofrece más control y potencia para proyectos más avanzados.

Además de estas librerías principales, existen muchas otras herramientas y bibliotecas adicionales que pueden ser útiles en el desarrollo de juegos. Por ejemplo, las bibliotecas de gráficos como OpenGL o DirectX proporcionan acceso directo a los motores gráficos del hardware, lo que ofrece un mayor control pero también requiere una comprensión más profunda de la programación gráfica.

La utilización de librerías para el desarrollo de juegos no solo facilita el proceso de creación, sino que también permite a los desarrolladores aprovechar las mejores prácticas y técnicas en el campo. Algunas de estas bibliotecas incluyen herramientas para la gestión de recursos gráficos, físicas, audio y entrada del usuario, lo que significa que los desarrolladores pueden centrarse en crear contenido visualmente impresionante y experiencias interactivas sin preocuparse por los detalles técnicos.

En resumen, las librerías que proporcionan las funciones básicas de un motor de juegos son herramientas esenciales para el desarrollo de juegos 2D y 3D. Cada una de estas librerías ofrece diferentes ventajas y desventajas, y la elección depende del proyecto específico, las habilidades del equipo y los recursos disponibles. Al utilizar una librería adecuada, los desarrolladores pueden crear experiencias interactivas impresionantes sin preocuparse por los detalles técnicos, lo que les permite centrarse en la creación de contenido visualmente atractivo y funcionalidades específicas.

<a id="estudio-de-juegos-existentes"></a>
## Estudio de juegos existentes

En este capítulo, nos sumergimos en la exploración de los motores de juegos existentes para entender cómo funcionan y qué características ofrecen a los desarrolladores. Comenzamos por analizar las técnicas de programación 2D y 3D que son fundamentales para crear contenido visualmente atractivo y dinámico.

A medida que avanzamos, nos familiarizamos con la arquitectura del juego, comprendiendo cómo se organizan los componentes como el motor gráfico, el sistema de física y las herramientas de audio. Este conocimiento es esencial para desarrollar juegos eficientes y fluidos.

Continuando nuestro estudio, examinamos los motores de juegos disponibles en el mercado, identificando sus tipos y aplicaciones específicas. Cada uno tiene sus fortalezas y debilidades, lo que permite a los desarrolladores elegir la herramienta más adecuada para su proyecto.

Además, dedicamos tiempo a analizar las librerías utilizadas en motores de juegos, comprendiendo cómo estas facilitan el desarrollo de funcionalidades complejas sin necesidad de reinventar la rueda. Estudiamos cómo interactúan estos componentes y cómo pueden ser personalizados para adaptarse a las necesidades específicas del proyecto.

A lo largo del capítulo, realizamos un análisis detallado de juegos existentes, examinando sus mecánicas, gráficos y sonido. Este estudio no solo nos proporciona una visión práctica de los desafíos que enfrentan los desarrolladores en el mundo real, sino que también nos ayuda a identificar oportunidades para mejorar nuestros propios proyectos.

Finalmente, reflexionamos sobre las áreas de especialización dentro del desarrollo de juegos y las librerías utilizadas por cada uno. Esto nos permite comprender cómo la elección del motor puede influir en el estilo y el rendimiento final del juego, así como cómo los desarrolladores pueden aprovechar las funcionalidades específicas de cada herramienta para crear experiencias únicas.

A lo largo de este estudio, hemos recorrido un camino desde la teoría hasta la práctica, pasando por una comprensión profunda de los motores de juegos existentes y su impacto en el desarrollo de software. Este conocimiento es fundamental para cualquier desarrollador que aspire a crear contenido visualmente impresionante y funcionalmente sólido.

### Introduccion

```markdown
Dispositivo:
Juegos de ordenador (teclado)
Juegos de ordenador (raton teclado)
Juegos de consola
Juegos de móvil

Juegos:
Pantalla
VR
AR

Proyección:
2d / 3d / 2.5d

Desde el punto de vista de la vista:
Vistas: plataforma frontal / cenital (visto desde arriba)

Desde el punto de vista de la juabilidad
RPG
MOBA
Plataformas
Shooters / FPS / TPS - shoot'em'up
Battle Royale
Atrapa la bandera
Tower defense
Arcade
Estrategia
Sandbox (mundo abierto)
Constructivos
Didácticos
Serious Games -> Gamificación aplicada a cualquier otra área

Condiciones comunes
Condicion de inicio - cómo arranca el juego
Condición de éxito - cómo se gana (progresa) este juego
Condición de fracaso (muerte) - condición en la que pierdes el juego y vuelves a empezar

Gestión de la frustración:
Un juego demasiado fácil hace que el usuario pierda interés (no plantea reto)
Un juego demasiado difícil hace que el usuario se frustre y abandone

Factor social versus factor individual

El resto de aplicaciones que desarrollamos, "las desarrollamos para adultos"
```

### rejilla

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      
      // Ahora dibujo una rejilla
      
      for(let x = 0;x<1024;x+=20){
        // Horizontales
        contexto.beginPath()
        contexto.moveTo(0,x)
        contexto.lineTo(1024,x)
        contexto.stroke()
        // Verticales
        contexto.beginPath()
        contexto.moveTo(x,0)
        contexto.lineTo(x,1024)
        contexto.stroke()
      }
    </script>
  </body>
</html>
```

### isometrico

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      
      // Parámetros isométricos reales
      var angulo = 30 * Math.PI / 180
      var cos = Math.cos(angulo)
      var sin = Math.sin(angulo)
      var paso = 20

      // Limpio fondo
      contexto.fillStyle = "#fff"
      contexto.fillRect(0,0,1024,1024)
      contexto.strokeStyle = "#000"

      // Dibujo rejilla isométrica REAL
      for(let u=-30;u<60;u++){
        contexto.beginPath()
        var x1 = 512 + (u * paso * cos)
        var y1 = 512 + (u * paso * sin)
        var x2 = 512 + ((u - 60) * paso * cos)
        var y2 = 512 + ((u + 60) * paso * sin)
        contexto.moveTo(x1, y1)
        contexto.lineTo(x2, y2)
        contexto.stroke()
      }
      for(let v=-30;v<60;v++){
        contexto.beginPath()
        var x1 = 512 + (v * paso * -cos)
        var y1 = 512 + (v * paso * sin)
        var x2 = 512 + ((v + 60) * paso * -cos)
        var y2 = 512 + ((v - 60) * paso * sin)
        contexto.moveTo(x1, y1)
        contexto.lineTo(x2, y2)
        contexto.stroke()
      }
    </script>
  </body>
</html>
```

### isometrico trucado

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      
      // Ahora dibujo una rejilla isométrica "fake" (2:1, alineada con el suelo)
      
      var paso = 20

      // Función de proyección isométrica simple (2:1)
      function iso(i, j){
        return {
          x: 512 + (i - j) * paso,
          y: 512 + (i + j) * (paso / 2)
        }
      }

      // Limpio fondo
      contexto.fillStyle = "#fff"
      contexto.fillRect(0,0,1024,1024)
      contexto.strokeStyle = "#000"

      // Líneas paralelas al eje U (j variable, i constante)
      for (let i = -60; i <= 60; i++) {
        const a = iso(i, -60);
        const b = iso(i,  60);
        contexto.beginPath();
        contexto.moveTo(a.x, a.y);
        contexto.lineTo(b.x, b.y);
        contexto.stroke();
      }

      // Líneas paralelas al eje V (i variable, j constante)
      for (let j = -60; j <= 60; j++) {
        const a = iso(-60, j);
        const b = iso( 60, j);
        contexto.beginPath();
        contexto.moveTo(a.x, a.y);
        contexto.lineTo(b.x, b.y);
        contexto.stroke();
      }

      // Centro
      contexto.beginPath()
      contexto.arc(512,512,5,0,Math.PI*2)
      contexto.fillStyle = "red"
      contexto.fill()
      
      console.log(iso(100,100))
    </script>
  </body>
</html>
```

### personaje

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      
      class Personaje{
        constructor(){
          this.x = 10;
          this.y = 10;
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.beginPath()
          contexto.arc(puntoiso.x,puntoiso.y,5,0,Math.PI*2)
          contexto.fillStyle = "red"
          contexto.fill()
        }
      }
    
    
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      var Personaje1 = new Personaje();
      
      // Ahora dibujo una rejilla isométrica "fake" (2:1, alineada con el suelo)
      
      var paso = 20

      // Función de proyección isométrica simple (2:1)
      function iso(i, j){
        return {
          x: 512 + (i - j) * paso,
          y: 512 + (i + j) * (paso / 2)
        }
      }

      // Limpio fondo
      contexto.fillStyle = "#fff"
      contexto.fillRect(0,0,1024,1024)
      contexto.strokeStyle = "#000"

      // Líneas paralelas al eje U (j variable, i constante)
      for (let i = -60; i <= 60; i++) {
        const a = iso(i, -60);
        const b = iso(i,  60);
        contexto.beginPath();
        contexto.moveTo(a.x, a.y);
        contexto.lineTo(b.x, b.y);
        contexto.stroke();
      }

      // Líneas paralelas al eje V (i variable, j constante)
      for (let j = -60; j <= 60; j++) {
        const a = iso(-60, j);
        const b = iso( 60, j);
        contexto.beginPath();
        contexto.moveTo(a.x, a.y);
        contexto.lineTo(b.x, b.y);
        contexto.stroke();
      }

      console.log(iso(10,10))
      
      Personaje1.dibuja()
      
    </script>
  </body>
</html>
```

### capturo y encierro

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      
      class Personaje{
        constructor(){
          this.x = 10;
          this.y = 10;
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.beginPath()
          contexto.arc(puntoiso.x,puntoiso.y,5,0,Math.PI*2)
          contexto.fillStyle = "red"
          contexto.fill()
        }
      }
    
    
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      var Personaje1 = new Personaje();
      
      // Ahora dibujo una rejilla isométrica "fake" (2:1, alineada con el suelo)
      
      var paso = 20

      // Función de proyección isométrica simple (2:1)
      function iso(i, j){
        return {
          x: 512 + (i - j) * paso,
          y: 512 + (i + j) * (paso / 2)
        }
      }
      function dibujoRejilla(){
        // Limpio fondo
        contexto.fillStyle = "#fff"
        contexto.fillRect(0,0,1024,1024)
        contexto.strokeStyle = "#000"

        // Líneas paralelas al eje U (j variable, i constante)
        for (let i = -60; i <= 60; i++) {
          const a = iso(i, -60);
          const b = iso(i,  60);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }

        // Líneas paralelas al eje V (i variable, j constante)
        for (let j = -60; j <= 60; j++) {
          const a = iso(-60, j);
          const b = iso( 60, j);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }
      }

      document.onkeydown = function(event){
        switch(event.key){
          case "w":
            Personaje1.x--
            break;
          case "s":
            Personaje1.x++
            break;
          case "a":
            Personaje1.y++
            break;
          case "d":
            Personaje1.y--
            break;
        }
        dibujoRejilla()
        Personaje1.dibuja()
      }
      
      
      
    </script>
  </body>
</html>
```

### cargo spritesheet

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      
      class Personaje{
        constructor(){
          this.x = 10;
          this.y = 10;
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.drawImage(sprite,puntoiso.x,puntoiso.y) 
        }
      }
    
    
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      var Personaje1 = new Personaje();
      var sprite = new Image()
      sprite.src = "spritesheet.png"
      
      // Ahora dibujo una rejilla isométrica "fake" (2:1, alineada con el suelo)
      
      var paso = 20

      // Función de proyección isométrica simple (2:1)
      function iso(i, j){
        return {
          x: 512 + (i - j) * paso,
          y: 512 + (i + j) * (paso / 2)
        }
      }
      function dibujoRejilla(){
        // Limpio fondo
        contexto.fillStyle = "#fff"
        contexto.fillRect(0,0,1024,1024)
        contexto.strokeStyle = "#000"

        // Líneas paralelas al eje U (j variable, i constante)
        for (let i = -60; i <= 60; i++) {
          const a = iso(i, -60);
          const b = iso(i,  60);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }

        // Líneas paralelas al eje V (i variable, j constante)
        for (let j = -60; j <= 60; j++) {
          const a = iso(-60, j);
          const b = iso( 60, j);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }
      }

      document.onkeydown = function(event){
        switch(event.key){
          case "w":
            Personaje1.x--
            break;
          case "s":
            Personaje1.x++
            break;
          case "a":
            Personaje1.y++
            break;
          case "d":
            Personaje1.y--
            break;
        }
        dibujoRejilla()
        Personaje1.dibuja()
      }
      
      
      
    </script>
  </body>
</html>
```

### uso cropping

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      
      class Personaje{
        constructor(){
          this.x = 10;
          this.y = 10;
          this.d = 0;
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.drawImage(sprite, this.d*64, 0, 64, 77, puntoiso.x,puntoiso.y, 64, 77) 
        }
      }
    
    
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      var Personaje1 = new Personaje();
      var sprite = new Image()
      sprite.src = "spritesheet.png"
      
      // Ahora dibujo una rejilla isométrica "fake" (2:1, alineada con el suelo)
      
      var paso = 20

      // Función de proyección isométrica simple (2:1)
      function iso(i, j){
        return {
          x: 512 + (i - j) * paso,
          y: 512 + (i + j) * (paso / 2)
        }
      }
      function dibujoRejilla(){
        // Limpio fondo
        contexto.fillStyle = "#fff"
        contexto.fillRect(0,0,1024,1024)
        contexto.strokeStyle = "#000"

        // Líneas paralelas al eje U (j variable, i constante)
        for (let i = -60; i <= 60; i++) {
          const a = iso(i, -60);
          const b = iso(i,  60);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }

        // Líneas paralelas al eje V (i variable, j constante)
        for (let j = -60; j <= 60; j++) {
          const a = iso(-60, j);
          const b = iso( 60, j);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }
      }

      document.onkeydown = function(event){
        switch(event.key){
          case "w":
            Personaje1.d = 3
            Personaje1.x--
            break;
          case "s":
            Personaje1.d = 1 // correcto
            Personaje1.x++
            break;
          case "a":
            Personaje1.d = 0
            Personaje1.y++
            break;
          case "d":
            Personaje1.d = 2
            Personaje1.y--
            break;
        }
        dibujoRejilla()
        Personaje1.dibuja()
      }
      
      
      
    </script>
  </body>
</html>
```

### uso de un bucle

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      
      class Personaje{
        constructor(){
          this.x = 10;
          this.y = 10;
          this.d = 0;
          this.andando = false;
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.drawImage(sprite, this.d*64, 0, 64, 77, puntoiso.x,puntoiso.y, 64, 77) 
        }
      }
    
    
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      var Personaje1 = new Personaje();
      var sprite = new Image()
      sprite.src = "spritesheet.png"
      
      // Ahora dibujo una rejilla isométrica "fake" (2:1, alineada con el suelo)
      
      var paso = 20

      // Función de proyección isométrica simple (2:1)
      function iso(i, j){
        return {
          x: 512 + (i - j) * paso,
          y: 512 + (i + j) * (paso / 2)
        }
      }
      function dibujoRejilla(){
        // Limpio fondo
        contexto.fillStyle = "#fff"
        contexto.fillRect(0,0,1024,1024)
        contexto.strokeStyle = "#000"

        // Líneas paralelas al eje U (j variable, i constante)
        for (let i = -60; i <= 60; i++) {
          const a = iso(i, -60);
          const b = iso(i,  60);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }

        // Líneas paralelas al eje V (i variable, j constante)
        for (let j = -60; j <= 60; j++) {
          const a = iso(-60, j);
          const b = iso( 60, j);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }
      }

      document.onkeydown = function(event){
        switch(event.key){
          case "w":
                          Personaje1.d = 3
            Personaje1.andando = true;
            break;
          case "s":
                        Personaje1.d = 1 // correcto  
            Personaje1.andando = true;
            break;
          case "a":
                        Personaje1.d = 0
            Personaje1.andando = true;
            break;
          case "d":
                        Personaje1.d = 2
            Personaje1.andando = true;
            break;
        }
        }
        document.onkeyup = function(event){
        switch(event.key){
          case "w":
            Personaje1.andando = false;
            break;
          case "s":
            Personaje1.andando = false;
            break;
          case "a":
            Personaje1.andando = false;
            break;
          case "d":
            Personaje1.andando = false;
            break;
        }
        
      
      }
      
      let temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        if(Personaje1.andando == true){
        switch(Personaje1.d){
            case 3:
              Personaje1.x--
              break;
            case 1:
              Personaje1.x++
              break;
            case 0:
              Personaje1.y++
              break;
            case 2:
              Personaje1.y--
              break;
          }
        }
        dibujoRejilla()
        Personaje1.dibuja()
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",66)
      }
      
      
    </script>
  </body>
</html>
```

### recogibles

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      class Recogible{
        constructor(){
          this.x = Math.round(Math.random()*1000);
          this.y = Math.round(Math.random()*1000);
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.beginPath();
          contexto.fillStyle = "green"
          contexto.arc(this.x,this.y,8,0,Math.PI*2)
          contexto.fill()
        }
      }
      class Personaje{
        constructor(){
          this.x = 10;
          this.y = 10;
          this.d = 0;
          this.andando = false;
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.drawImage(sprite, this.d*64, 0, 64, 77, puntoiso.x,puntoiso.y, 64, 77) 
        }
      }
    
    
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      var Personaje1 = new Personaje();
      var sprite = new Image()
      sprite.src = "spritesheet.png"
      var recogibles = []
      var numerorecogibles = 50;
      for(let i = 0;i<numerorecogibles;i++){
        recogibles.push(new Recogible())
      }
      
      // Ahora dibujo una rejilla isométrica "fake" (2:1, alineada con el suelo)
      
      var paso = 20

      // Función de proyección isométrica simple (2:1)
      function iso(i, j){
        return {
          x: 512 + (i - j) * paso,
          y: 512 + (i + j) * (paso / 2)
        }
      }
      function dibujoRejilla(){
        // Limpio fondo
        contexto.fillStyle = "#fff"
        contexto.fillRect(0,0,1024,1024)
        contexto.strokeStyle = "#000"

        // Líneas paralelas al eje U (j variable, i constante)
        for (let i = -60; i <= 60; i++) {
          const a = iso(i, -60);
          const b = iso(i,  60);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }

        // Líneas paralelas al eje V (i variable, j constante)
        for (let j = -60; j <= 60; j++) {
          const a = iso(-60, j);
          const b = iso( 60, j);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }
      }

      document.onkeydown = function(event){
        switch(event.key){
          case "w":
                          Personaje1.d = 3
            Personaje1.andando = true;
            break;
          case "s":
                        Personaje1.d = 1 // correcto  
            Personaje1.andando = true;
            break;
          case "a":
                        Personaje1.d = 0
            Personaje1.andando = true;
            break;
          case "d":
                        Personaje1.d = 2
            Personaje1.andando = true;
            break;
        }
        }
        document.onkeyup = function(event){
        switch(event.key){
          case "w":
            Personaje1.andando = false;
            break;
          case "s":
            Personaje1.andando = false;
            break;
          case "a":
            Personaje1.andando = false;
            break;
          case "d":
            Personaje1.andando = false;
            break;
        }
        
      
      }
      
      let temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        if(Personaje1.andando == true){
        switch(Personaje1.d){
            case 3:
              Personaje1.x--
              break;
            case 1:
              Personaje1.x++
              break;
            case 0:
              Personaje1.y++
              break;
            case 2:
              Personaje1.y--
              break;
          }
        }
        dibujoRejilla()
        for(let i = 0;i<numerorecogibles;i++){
          recogibles[i].dibuja()
        }
        Personaje1.dibuja()
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",66)
      }
      
      
    </script>
  </body>
</html>
```

### recoger

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas id="lienzo"></canvas>
    <script>
      class Recogible{
        constructor(){
          this.x = Math.round((Math.random()*120) - 60); // [-60, 60]
          this.y = Math.round((Math.random()*120) - 60); // [-60, 60]
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.beginPath();
          contexto.fillStyle = "green"
          contexto.arc(puntoiso.x,puntoiso.y,8,0,Math.PI*2)
          contexto.fill()
        }
      }
      class Personaje{
        constructor(){
          this.x = 10;
          this.y = 10;
          this.d = 0;
          this.andando = false;
        }
        dibuja(){
          let puntoiso = iso(this.x,this.y)
          contexto.drawImage(sprite, this.d*64, 0, 64, 77, puntoiso.x,puntoiso.y, 64, 77) 
        }
      }
      function distancia(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }
    
      var lienzo = document.querySelector("#lienzo")
      var contexto = lienzo.getContext("2d")
      lienzo.width = 1024
      lienzo.height = 1024
      var Personaje1 = new Personaje();
      var sprite = new Image()
      sprite.src = "spritesheet.png"
      var recogibles = []
      var numerorecogibles = 50;
      for(let i = 0;i<numerorecogibles;i++){
        recogibles.push(new Recogible())
      }
      
      // Ahora dibujo una rejilla isométrica "fake" (2:1, alineada con el suelo)
      
      var paso = 20

      // Función de proyección isométrica simple (2:1)
      function iso(i, j){
        return {
          x: 512 + (i - j) * paso,
          y: 512 + (i + j) * (paso / 2)
        }
      }
      function dibujoRejilla(){
        // Limpio fondo
        contexto.fillStyle = "#fff"
        contexto.fillRect(0,0,1024,1024)
        contexto.strokeStyle = "#000"

        // Líneas paralelas al eje U (j variable, i constante)
        for (let i = -60; i <= 60; i++) {
          const a = iso(i, -60);
          const b = iso(i,  60);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }

        // Líneas paralelas al eje V (i variable, j constante)
        for (let j = -60; j <= 60; j++) {
          const a = iso(-60, j);
          const b = iso( 60, j);
          contexto.beginPath();
          contexto.moveTo(a.x, a.y);
          contexto.lineTo(b.x, b.y);
          contexto.stroke();
        }
      }

      document.onkeydown = function(event){
        switch(event.key){
          case "w":
                          Personaje1.d = 3
            Personaje1.andando = true;
            break;
          case "s":
                        Personaje1.d = 1 // correcto  
            Personaje1.andando = true;
            break;
          case "a":
                        Personaje1.d = 0
            Personaje1.andando = true;
            break;
          case "d":
                        Personaje1.d = 2
            Personaje1.andando = true;
            break;
        }
        }
        document.onkeyup = function(event){
        switch(event.key){
          case "w":
            Personaje1.andando = false;
            break;
          case "s":
            Personaje1.andando = false;
            break;
          case "a":
            Personaje1.andando = false;
            break;
          case "d":
            Personaje1.andando = false;
            break;
        }
        
      
      }
      
      let temporizador = setTimeout("bucle()",1000)
      
      function bucle(){
        if(Personaje1.andando == true){
        switch(Personaje1.d){
            case 3:
              Personaje1.x--
              break;
            case 1:
              Personaje1.x++
              break;
            case 0:
              Personaje1.y++
              break;
            case 2:
              Personaje1.y--
              break;
          }
        }
        dibujoRejilla()
        for(let i = 0;i<recogibles.length;i++){
          recogibles[i].dibuja()
          if(distancia(Personaje1.x,Personaje1.y,recogibles[i].x,recogibles[i].y) < 5){
            console.log("ok")
            recogibles.splice(i,1)
          }
        }
        Personaje1.dibuja()
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",66)
      }
      
      
    </script>
  </body>
</html>
```

<a id="aplicacion-de-modificaciones-sobre-juegos-existentes"></a>
## Aplicación de modificaciones sobre juegos existentes

Continuando con nuestra exploración del mundo de los motores de juegos, nos encontramos en una sección dedicada a la aplicación de modificaciones sobre juegos existentes. Esta es una práctica común entre los jugadores que desean personalizar su experiencia o mejorar el rendimiento de sus juegos favoritos.

La primera modificación que podemos considerar es la creación de mods para cambiar aspectos visuales del juego, como la apariencia de personajes, escenarios o objetos. Estos cambios pueden ser tan simples como reemplazar texturas o tan complejos como añadir nuevas características a los personajes. Para realizar estas modificaciones, los jugadores generalmente utilizan herramientas específicas para editar archivos binarios del juego, lo que requiere un conocimiento básico de la estructura interna de los juegos.

Otra forma común de modificar juegos es mediante el uso de mods que añaden contenido adicional. Estos pueden ser nuevos niveles, personajes o habilidades especiales que no están disponibles en la versión original del juego. La creación y distribución de estos mods ha convertido en una comunidad activa dentro de la industria del gaming, donde los jugadores comparten sus trabajos con otros para ampliar su experiencia.

Además de las modificaciones visuales y de contenido, también es posible modificar el comportamiento interno del juego. Esto puede implicar cambiar la dificultad, añadir nuevas mecánicas o incluso alterar la historia del juego. La modificación interna requiere un conocimiento más profundo de los lenguajes de programación utilizados en el desarrollo del juego y a menudo implica trabajar con archivos de código fuente.

La aplicación de modificaciones sobre juegos existentes no solo es una forma divertida de personalizar la experiencia del jugador, sino que también puede ser una herramienta valiosa para aprender sobre los sistemas detrás de los juegos. Al examinar y modificar el código o los archivos binarios de un juego, los jugadores pueden adquirir conocimientos prácticos sobre programación, diseño de interfaces y gestión de bases de datos.

Es importante tener en cuenta que la modificación de juegos puede ser legalmente complicada dependiendo del país y las leyes locales. En muchos lugares, el uso no autorizado de mods puede estar prohibido, especialmente si se utiliza para fines comerciales o si infringe derechos de autor. Por lo tanto, es crucial investigar los términos de servicio del juego y la legislación local antes de comenzar cualquier modificación.

En conclusión, la aplicación de modificaciones sobre juegos existentes es una práctica fascinante que combina creatividad, habilidad técnica y conocimiento de programación. Aunque puede ser un proceso desafiante, ofrece a los jugadores la oportunidad de experimentar con nuevos aspectos del juego o incluso mejorar su rendimiento. Sin embargo, como cualquier actividad que implique el uso de software, es importante estar consciente de las implicaciones legales y éticas para evitar problemas en el futuro.

### threejs basico

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Three.js Minimal Example</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Scene
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x3498db); // Blue background

        // Camera
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 5;

        // Renderer
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Box geometry
        const geometry = new THREE.BoxGeometry(1, 1, 1);
        const material = new THREE.MeshPhongMaterial({ color: 0x00ff00 });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // Light
        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(1, 1, 1);
        scene.add(light);

        // Ambient light (optional, for softer lighting)
        const ambientLight = new THREE.AmbientLight(0x404040);
        scene.add(ambientLight);

        // Animation loop
        function animate() {
            requestAnimationFrame(animate);
            
            // Rotate the cube
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            
            renderer.render(scene, camera);
        }

        // Handle window resize
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        // Start animation
        animate();
    </script>
</body>
</html>
```

### suelo y movimiento

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Minecraft Clone</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>
    <script>
        // Block class
        class Block {
            constructor(x, y, z, type = 'grass') {
                this.x = x;
                this.y = y;
                this.z = z;
                this.type = type;
                this.mesh = null;
                
                this.createMesh();
            }
            
            createMesh() {
                const geometry = new THREE.BoxGeometry(1, 1, 1);
                
                // Different colors for different block types
                const colors = {
                    'grass': 0x4CAF50,
                    'dirt': 0x795548,
                    'stone': 0x9E9E9E
                };
                
                const material = new THREE.MeshPhongMaterial({ 
                    color: colors[this.type] || 0x4CAF50 
                });
                
                this.mesh = new THREE.Mesh(geometry, material);
                this.mesh.position.set(this.x, this.y, this.z);
            }
            
            addToScene(scene) {
                if (this.mesh) {
                    scene.add(this.mesh);
                }
            }
            
            removeFromScene(scene) {
                if (this.mesh) {
                    scene.remove(this.mesh);
                }
            }
        }

        // Game class
        class MinecraftGame {
            constructor() {
                this.scene = new THREE.Scene();
                this.scene.background = new THREE.Color(0x87CEEB); // Sky blue
                
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.camera.position.set(0, 10, 0);
                
                this.renderer = new THREE.WebGLRenderer({ antialias: true });
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                document.body.appendChild(this.renderer.domElement);
                
                this.controls = null;
                this.blocks = [];
                this.moveState = { forward: false, backward: false, left: false, right: false };
                this.velocity = new THREE.Vector3();
                this.direction = new THREE.Vector3();
                
                this.setupLights();
                this.createFloor();
                this.setupControls();
                this.setupEventListeners();
                
                this.animate();
            }
            
            setupLights() {
                // Ambient light
                const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
                this.scene.add(ambientLight);
                
                // Directional light (sun)
                const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
                directionalLight.position.set(50, 50, 50);
                directionalLight.castShadow = true;
                this.scene.add(directionalLight);
            }
            
            createFloor() {
                const gridSize = 10;
                
                for (let x = -gridSize/2; x < gridSize/2; x++) {
                    for (let z = -gridSize/2; z < gridSize/2; z++) {
                        // Create different block types in a pattern
                        let type = 'grass';
                        if (Math.random() > 0.8) type = 'dirt';
                        if (Math.random() > 0.95) type = 'stone';
                        
                        const block = new Block(x, -0.5, z, type);
                        block.addToScene(this.scene);
                        this.blocks.push(block);
                    }
                }
                
                console.log(`Created ${this.blocks.length} blocks`);
            }
            
            setupControls() {
                // Pointer lock controls for FPS movement
                this.controls = new THREE.PointerLockControls(this.camera, document.body);
                
                // Instructions
                const instructions = document.createElement('div');
                instructions.style.cssText = `
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-family: Arial;
                `;
                instructions.innerHTML = `
                    <h2>Minecraft Clone</h2>
                    <p>Click to play</p>
                    <p>WASD: Move | Mouse: Look around</p>
                    <p>Space: Jump | Shift: Move faster</p>
                `;
                document.body.appendChild(instructions);
                
                // Click to start
                const startGame = () => {
                    this.controls.lock();
                    instructions.style.display = 'none';
                };
                
                document.body.addEventListener('click', startGame);
                
                this.controls.addEventListener('lock', () => {
                    instructions.style.display = 'none';
                });
                
                this.controls.addEventListener('unlock', () => {
                    instructions.style.display = 'block';
                });
            }
            
            setupEventListeners() {
                // Keyboard controls
                document.addEventListener('keydown', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = true;
                            break;
                        case 'KeyS':
                            this.moveState.backward = true;
                            break;
                        case 'KeyA':
                            this.moveState.left = true;
                            break;
                        case 'KeyD':
                            this.moveState.right = true;
                            break;
                    }
                });
                
                document.addEventListener('keyup', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = false;
                            break;
                        case 'KeyS':
                            this.moveState.backward = false;
                            break;
                        case 'KeyA':
                            this.moveState.left = false;
                            break;
                        case 'KeyD':
                            this.moveState.right = false;
                            break;
                    }
                });
                
                // Window resize
                window.addEventListener('resize', () => {
                    this.camera.aspect = window.innerWidth / window.innerHeight;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                });
            }
            
            updateMovement(delta) {
                if (!this.controls.isLocked) return;
                
                const speed = 10.0;
                this.velocity.x = 0;
                this.velocity.z = 0;
                
                if (this.moveState.forward) this.velocity.z -= speed * delta;
                if (this.moveState.backward) this.velocity.z += speed * delta;
                if (this.moveState.left) this.velocity.x -= speed * delta;
                if (this.moveState.right) this.velocity.x += speed * delta;
                
                // Apply movement relative to camera direction
                this.controls.moveRight(this.velocity.x);
                this.controls.moveForward(this.velocity.z);
                
                // Simple gravity and ground collision
                if (this.camera.position.y > 1) {
                    this.camera.position.y -= 9.8 * delta; // gravity
                } else {
                    this.camera.position.y = 1; // ground level
                }
            }
            
            animate() {
                requestAnimationFrame(() => this.animate());
                
                const delta = 0.016; // approx 60fps
                
                if (this.controls.isLocked) {
                    this.updateMovement(delta);
                }
                
                this.renderer.render(this.scene, this.camera);
            }
        }

        // Start the game
        new MinecraftGame();
    </script>
</body>
</html>
```

### gravedad

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Minecraft Clone</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>
    <script>
        // Block class
        class Block {
            constructor(x, y, z, type = 'grass') {
                this.x = x;
                this.y = y;
                this.z = z;
                this.type = type;
                this.mesh = null;
                
                this.createMesh();
            }
            
            createMesh() {
                const geometry = new THREE.BoxGeometry(1, 1, 1);
                
                const colors = {
                    'grass': 0x4CAF50,
                    'dirt': 0x795548,
                    'stone': 0x9E9E9E
                };
                
                const material = new THREE.MeshPhongMaterial({ 
                    color: colors[this.type] || 0x4CAF50 
                });
                
                this.mesh = new THREE.Mesh(geometry, material);
                this.mesh.position.set(this.x, this.y, this.z);
            }
            
            addToScene(scene) {
                if (this.mesh) {
                    scene.add(this.mesh);
                }
            }
            
            removeFromScene(scene) {
                if (this.mesh) {
                    scene.remove(this.mesh);
                }
            }
            
            getBoundingBox() {
                return new THREE.Box3().setFromObject(this.mesh);
            }
        }

        // Game class
        class MinecraftGame {
            constructor() {
                this.scene = new THREE.Scene();
                this.scene.background = new THREE.Color(0x87CEEB);
                
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.camera.position.set(0, 2, 5);
                
                this.renderer = new THREE.WebGLRenderer({ antialias: true });
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                document.body.appendChild(this.renderer.domElement);
                
                this.controls = null;
                this.blocks = [];
                this.moveState = { forward: false, backward: false, left: false, right: false, jump: false };
                this.velocity = new THREE.Vector3();
                this.direction = new THREE.Vector3();
                
                // Physics properties
                this.onGround = false;
                this.gravity = -20;
                this.jumpForce = 8;
                this.playerHeight = 1.8;
                this.playerRadius = 0.3;
                
                this.setupLights();
                this.createFloor();
                this.setupControls();
                this.setupEventListeners();
                
                this.clock = new THREE.Clock();
                this.animate();
            }
            
            setupLights() {
                const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
                this.scene.add(ambientLight);
                
                const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
                directionalLight.position.set(50, 50, 50);
                this.scene.add(directionalLight);
            }
            
            createFloor() {
                const gridSize = 10;
                
                for (let x = -gridSize/2; x < gridSize/2; x++) {
                    for (let z = -gridSize/2; z < gridSize/2; z++) {
                        let type = 'grass';
                        if (Math.random() > 0.8) type = 'dirt';
                        if (Math.random() > 0.95) type = 'stone';
                        
                        const block = new Block(x, -0.5, z, type);
                        block.addToScene(this.scene);
                        this.blocks.push(block);
                    }
                }
                
                // Add some raised blocks for collision testing
                for (let i = 0; i < 5; i++) {
                    const x = Math.floor(Math.random() * 8 - 4);
                    const z = Math.floor(Math.random() * 8 - 4);
                    const block = new Block(x, 0.5, z, 'stone');
                    block.addToScene(this.scene);
                    this.blocks.push(block);
                }
            }
            
            setupControls() {
                this.controls = new THREE.PointerLockControls(this.camera, document.body);
                
                const instructions = document.createElement('div');
                instructions.style.cssText = `
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-family: Arial;
                `;
                instructions.innerHTML = `
                    <h2>Minecraft Clone</h2>
                    <p>Click to play</p>
                    <p>WASD: Move | Mouse: Look around</p>
                    <p>Space: Jump</p>
                `;
                document.body.appendChild(instructions);
                
                const startGame = () => {
                    this.controls.lock();
                    instructions.style.display = 'none';
                };
                
                document.body.addEventListener('click', startGame);
                
                this.controls.addEventListener('lock', () => {
                    instructions.style.display = 'none';
                });
                
                this.controls.addEventListener('unlock', () => {
                    instructions.style.display = 'block';
                });
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = true;
                            break;
                        case 'KeyS':
                            this.moveState.backward = true;
                            break;
                        case 'KeyA':
                            this.moveState.left = true;
                            break;
                        case 'KeyD':
                            this.moveState.right = true;
                            break;
                        case 'Space':
                            if (this.onGround) {
                                this.moveState.jump = true;
                            }
                            event.preventDefault();
                            break;
                    }
                });
                
                document.addEventListener('keyup', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = false;
                            break;
                        case 'KeyS':
                            this.moveState.backward = false;
                            break;
                        case 'KeyA':
                            this.moveState.left = false;
                            break;
                        case 'KeyD':
                            this.moveState.right = false;
                            break;
                        case 'Space':
                            this.moveState.jump = false;
                            break;
                    }
                });
                
                window.addEventListener('resize', () => {
                    this.camera.aspect = window.innerWidth / window.innerHeight;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                });
            }
            
            checkCollision(newPosition) {
                const playerBox = new THREE.Box3(
                    new THREE.Vector3(
                        newPosition.x - this.playerRadius,
                        newPosition.y - this.playerHeight,
                        newPosition.z - this.playerRadius
                    ),
                    new THREE.Vector3(
                        newPosition.x + this.playerRadius,
                        newPosition.y,
                        newPosition.z + this.playerRadius
                    )
                );
                
                for (const block of this.blocks) {
                    const blockBox = block.getBoundingBox();
                    if (playerBox.intersectsBox(blockBox)) {
                        return true;
                    }
                }
                return false;
            }
            
            updateMovement(delta) {
                if (!this.controls.isLocked) return;
                
                const speed = 5.0;
                this.velocity.x = 0;
                this.velocity.z = 0;
                
                // Fixed movement directions
                if (this.moveState.forward) this.velocity.z = -speed * delta;
                if (this.moveState.backward) this.velocity.z = speed * delta;
                if (this.moveState.left) this.velocity.x = -speed * delta;
                if (this.moveState.right) this.velocity.x = speed * delta;
                
                // Apply movement relative to camera direction
                this.velocity.applyEuler(new THREE.Euler(0, this.camera.rotation.y, 0));
                
                // Store current position for collision checking
                const oldPosition = this.camera.position.clone();
                
                // Apply horizontal movement with collision detection
                const newHorizontalPos = oldPosition.clone().add(this.velocity);
                if (!this.checkCollision(newHorizontalPos)) {
                    this.camera.position.x = newHorizontalPos.x;
                    this.camera.position.z = newHorizontalPos.z;
                }
                
                // Apply vertical movement (gravity and jumping)
                if (this.moveState.jump && this.onGround) {
                    this.velocity.y = this.jumpForce;
                    this.onGround = false;
                    this.moveState.jump = false;
                }
                
                this.velocity.y += this.gravity * delta;
                
                const newVerticalPos = this.camera.position.clone();
                newVerticalPos.y += this.velocity.y * delta;
                
                // Check if we're on the ground plane or outside bounds
                const gridSize = 10;
                const isOutsideGrid = Math.abs(this.camera.position.x) > gridSize/2 || 
                                    Math.abs(this.camera.position.z) > gridSize/2;
                
                if (isOutsideGrid) {
                    // Allow falling off edges
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                    }
                    this.onGround = false;
                } else {
                    // Normal collision detection
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                        this.onGround = false;
                    } else {
                        // We hit something vertically
                        if (this.velocity.y < 0) {
                            // Hit the ground
                            this.onGround = true;
                            this.velocity.y = 0;
                        } else {
                            // Hit ceiling
                            this.velocity.y = 0;
                        }
                    }
                }
                
                // Reset if player falls too far
                if (this.camera.position.y < -10) {
                    this.camera.position.set(0, 5, 0);
                    this.velocity.set(0, 0, 0);
                }
            }
            
            animate() {
                requestAnimationFrame(() => this.animate());
                
                const delta = Math.min(this.clock.getDelta(), 0.1); // Cap delta for stability
                
                if (this.controls.isLocked) {
                    this.updateMovement(delta);
                }
                
                this.renderer.render(this.scene, this.camera);
            }
        }

        // Start the game
        new MinecraftGame();
    </script>
</body>
</html>
```

### raycast

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Minecraft Clone</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
        #crosshair {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }
        #crosshair::before, #crosshair::after {
            content: '';
            position: absolute;
            background: white;
        }
        #crosshair::before {
            width: 2px;
            height: 20px;
            left: 50%;
            transform: translateX(-50%);
        }
        #crosshair::after {
            width: 20px;
            height: 2px;
            top: 50%;
            transform: translateY(-50%);
        }
    </style>
</head>
<body>
    <div id="crosshair"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>
    <script>
        // Block class
        class Block {
            constructor(x, y, z, type = 'grass') {
                this.x = x;
                this.y = y;
                this.z = z;
                this.type = type;
                this.mesh = null;
                
                this.createMesh();
            }
            
            createMesh() {
                const geometry = new THREE.BoxGeometry(1, 1, 1);
                
                const colors = {
                    'grass': 0x4CAF50,
                    'dirt': 0x795548,
                    'stone': 0x9E9E9E
                };
                
                const material = new THREE.MeshPhongMaterial({ 
                    color: colors[this.type] || 0x4CAF50 
                });
                
                this.mesh = new THREE.Mesh(geometry, material);
                this.mesh.position.set(this.x, this.y, this.z);
                
                // Enable shadows
                this.mesh.castShadow = true;
                this.mesh.receiveShadow = true;
            }
            
            addToScene(scene) {
                if (this.mesh) {
                    scene.add(this.mesh);
                }
            }
            
            removeFromScene(scene) {
                if (this.mesh) {
                    scene.remove(this.mesh);
                }
            }
            
            getBoundingBox() {
                return new THREE.Box3().setFromObject(this.mesh);
            }
        }

        // Game class
        class MinecraftGame {
            constructor() {
                this.scene = new THREE.Scene();
                this.scene.background = new THREE.Color(0x87CEEB);
                
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.camera.position.set(0, 2, 5);
                
                this.renderer = new THREE.WebGLRenderer({ antialias: true });
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                this.renderer.shadowMap.enabled = true;
                this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
                document.body.appendChild(this.renderer.domElement);
                
                this.controls = null;
                this.blocks = [];
                this.moveState = { forward: false, backward: false, left: false, right: false, jump: false };
                this.velocity = new THREE.Vector3();
                this.direction = new THREE.Vector3();
                
                // Physics properties
                this.onGround = false;
                this.gravity = -20;
                this.jumpForce = 8;
                this.playerHeight = 1.8;
                this.playerRadius = 0.3;
                
                // Raycasting
                this.raycaster = new THREE.Raycaster();
                this.raycaster.far = 10;
                
                this.setupLights();
                this.createFloor();
                this.setupControls();
                this.setupEventListeners();
                
                this.clock = new THREE.Clock();
                this.animate();
            }
            
            setupLights() {
                const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
                this.scene.add(ambientLight);
                
                const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
                directionalLight.position.set(50, 50, 50);
                directionalLight.castShadow = true;
                
                // Shadow properties
                directionalLight.shadow.mapSize.width = 2048;
                directionalLight.shadow.mapSize.height = 2048;
                directionalLight.shadow.camera.near = 0.5;
                directionalLight.shadow.camera.far = 500;
                directionalLight.shadow.camera.left = -50;
                directionalLight.shadow.camera.right = 50;
                directionalLight.shadow.camera.top = 50;
                directionalLight.shadow.camera.bottom = -50;
                
                this.scene.add(directionalLight);
            }
            
            createFloor() {
                const gridSize = 10;
                
                for (let x = -gridSize/2; x < gridSize/2; x++) {
                    for (let z = -gridSize/2; z < gridSize/2; z++) {
                        let type = 'grass';
                        if (Math.random() > 0.8) type = 'dirt';
                        if (Math.random() > 0.95) type = 'stone';
                        
                        const block = new Block(x, -0.5, z, type);
                        block.addToScene(this.scene);
                        this.blocks.push(block);
                    }
                }
                
                // Add some raised blocks for collision testing
                for (let i = 0; i < 5; i++) {
                    const x = Math.floor(Math.random() * 8 - 4);
                    const z = Math.floor(Math.random() * 8 - 4);
                    const block = new Block(x, 0.5, z, 'stone');
                    block.addToScene(this.scene);
                    this.blocks.push(block);
                }
            }
            
            setupControls() {
                this.controls = new THREE.PointerLockControls(this.camera, document.body);
                
                const instructions = document.createElement('div');
                instructions.style.cssText = `
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-family: Arial;
                `;
                instructions.innerHTML = `
                    <h2>Minecraft Clone</h2>
                    <p>Click to play</p>
                    <p>WASD: Move | Mouse: Look around</p>
                    <p>Space: Jump | Left Click: Remove Block</p>
                `;
                document.body.appendChild(instructions);
                
                const startGame = () => {
                    this.controls.lock();
                    instructions.style.display = 'none';
                };
                
                document.body.addEventListener('click', startGame);
                
                this.controls.addEventListener('lock', () => {
                    instructions.style.display = 'none';
                });
                
                this.controls.addEventListener('unlock', () => {
                    instructions.style.display = 'block';
                });
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = true;
                            break;
                        case 'KeyS':
                            this.moveState.backward = true;
                            break;
                        case 'KeyA':
                            this.moveState.left = true;
                            break;
                        case 'KeyD':
                            this.moveState.right = true;
                            break;
                        case 'Space':
                            if (this.onGround) {
                                this.moveState.jump = true;
                            }
                            event.preventDefault();
                            break;
                    }
                });
                
                document.addEventListener('keyup', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = false;
                            break;
                        case 'KeyS':
                            this.moveState.backward = false;
                            break;
                        case 'KeyA':
                            this.moveState.left = false;
                            break;
                        case 'KeyD':
                            this.moveState.right = false;
                            break;
                        case 'Space':
                            this.moveState.jump = false;
                            break;
                    }
                });

                // Mouse click to remove blocks
                document.addEventListener('mousedown', (event) => {
                    if (event.button === 0 && this.controls.isLocked) { // Left click
                        this.removeBlockAtPointer();
                    }
                });
                
                window.addEventListener('resize', () => {
                    this.camera.aspect = window.innerWidth / window.innerHeight;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                });
            }

            removeBlockAtPointer() {
                // Set raycaster from camera center
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                
                // Get all block meshes
                const blockMeshes = this.blocks.map(block => block.mesh);
                
                // Find intersections
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const blockMesh = intersection.object;
                    
                    // Find the block object
                    const blockIndex = this.blocks.findIndex(block => block.mesh === blockMesh);
                    if (blockIndex !== -1) {
                        const block = this.blocks[blockIndex];
                        
                        // Remove from scene and array
                        block.removeFromScene(this.scene);
                        this.blocks.splice(blockIndex, 1);
                        
                        console.log('Block removed!');
                    }
                }
            }
            
            checkCollision(newPosition) {
                const playerBox = new THREE.Box3(
                    new THREE.Vector3(
                        newPosition.x - this.playerRadius,
                        newPosition.y - this.playerHeight,
                        newPosition.z - this.playerRadius
                    ),
                    new THREE.Vector3(
                        newPosition.x + this.playerRadius,
                        newPosition.y,
                        newPosition.z + this.playerRadius
                    )
                );
                
                for (const block of this.blocks) {
                    const blockBox = block.getBoundingBox();
                    if (playerBox.intersectsBox(blockBox)) {
                        return true;
                    }
                }
                return false;
            }
            
            updateMovement(delta) {
                if (!this.controls.isLocked) return;
                
                const speed = 5.0;
                
                // Get camera direction vectors
                const cameraDirection = new THREE.Vector3();
                this.camera.getWorldDirection(cameraDirection);
                cameraDirection.y = 0;
                cameraDirection.normalize();
                
                // Get right vector
                const cameraRight = new THREE.Vector3();
                cameraRight.crossVectors(this.camera.up, cameraDirection).normalize();
                
                // Reset velocity
                this.velocity.x = 0;
                this.velocity.z = 0;
                
                // Apply movement based on camera orientation
                if (this.moveState.forward) {
                    this.velocity.add(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.backward) {
                    this.velocity.sub(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.left) {
                    this.velocity.add(cameraRight.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.right) {
                    this.velocity.sub(cameraRight.clone().multiplyScalar(speed * delta));
                }
                
                // Store current position for collision checking
                const oldPosition = this.camera.position.clone();
                
                // Apply horizontal movement with collision detection
                const newHorizontalPos = oldPosition.clone().add(this.velocity);
                if (!this.checkCollision(newHorizontalPos)) {
                    this.camera.position.x = newHorizontalPos.x;
                    this.camera.position.z = newHorizontalPos.z;
                }
                
                // Apply vertical movement (gravity and jumping)
                if (this.moveState.jump && this.onGround) {
                    this.velocity.y = this.jumpForce;
                    this.onGround = false;
                    this.moveState.jump = false;
                }
                
                this.velocity.y += this.gravity * delta;
                
                const newVerticalPos = this.camera.position.clone();
                newVerticalPos.y += this.velocity.y * delta;
                
                // Check if we're on the ground plane or outside bounds
                const gridSize = 10;
                const isOutsideGrid = Math.abs(this.camera.position.x) > gridSize/2 || 
                                    Math.abs(this.camera.position.z) > gridSize/2;
                
                if (isOutsideGrid) {
                    // Allow falling off edges
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                    }
                    this.onGround = false;
                } else {
                    // Normal collision detection
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                        this.onGround = false;
                    } else {
                        // We hit something vertically
                        if (this.velocity.y < 0) {
                            // Hit the ground
                            this.onGround = true;
                            this.velocity.y = 0;
                        } else {
                            // Hit ceiling
                            this.velocity.y = 0;
                        }
                    }
                }
                
                // Reset if player falls too far
                if (this.camera.position.y < -10) {
                    this.camera.position.set(0, 5, 0);
                    this.velocity.set(0, 0, 0);
                }
            }
            
            animate() {
                requestAnimationFrame(() => this.animate());
                
                const delta = Math.min(this.clock.getDelta(), 0.1);
                
                if (this.controls.isLocked) {
                    this.updateMovement(delta);
                }
                
                this.renderer.render(this.scene, this.camera);
            }
        }

        // Start the game
        new MinecraftGame();
    </script>
</body>
</html>
```

### crear y eliminar

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Minecraft Clone</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
        #crosshair {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }
        #crosshair::before, #crosshair::after {
            content: '';
            position: absolute;
            background: white;
        }
        #crosshair::before {
            width: 2px;
            height: 20px;
            left: 50%;
            transform: translateX(-50%);
        }
        #crosshair::after {
            width: 20px;
            height: 2px;
            top: 50%;
            transform: translateY(-50%);
        }
    </style>
</head>
<body>
    <div id="crosshair"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>
    <script>
        // Block class
        class Block {
            constructor(x, y, z, type = 'grass') {
                this.x = x;
                this.y = y;
                this.z = z;
                this.type = type;
                this.mesh = null;
                
                this.createMesh();
            }
            
            createMesh() {
                const geometry = new THREE.BoxGeometry(1, 1, 1);
                
                const colors = {
                    'grass': 0x4CAF50,
                    'dirt': 0x795548,
                    'stone': 0x9E9E9E
                };
                
                const material = new THREE.MeshPhongMaterial({ 
                    color: colors[this.type] || 0x4CAF50 
                });
                
                this.mesh = new THREE.Mesh(geometry, material);
                this.mesh.position.set(this.x, this.y, this.z);
                
                // Enable shadows
                this.mesh.castShadow = true;
                this.mesh.receiveShadow = true;
            }
            
            addToScene(scene) {
                if (this.mesh) {
                    scene.add(this.mesh);
                }
            }
            
            removeFromScene(scene) {
                if (this.mesh) {
                    scene.remove(this.mesh);
                }
            }
            
            getBoundingBox() {
                return new THREE.Box3().setFromObject(this.mesh);
            }
        }

        // Game class
        class MinecraftGame {
            constructor() {
                this.scene = new THREE.Scene();
                this.scene.background = new THREE.Color(0x87CEEB);
                
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.camera.position.set(0, 2, 5);
                
                this.renderer = new THREE.WebGLRenderer({ antialias: true });
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                this.renderer.shadowMap.enabled = true;
                this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
                document.body.appendChild(this.renderer.domElement);
                
                this.controls = null;
                this.blocks = [];
                this.moveState = { forward: false, backward: false, left: false, right: false, jump: false };
                this.velocity = new THREE.Vector3();
                this.direction = new THREE.Vector3();
                
                // Physics properties
                this.onGround = false;
                this.gravity = -20;
                this.jumpForce = 8;
                this.playerHeight = 1.8;
                this.playerRadius = 0.3;
                
                // Raycasting
                this.raycaster = new THREE.Raycaster();
                this.raycaster.far = 10;
                
                this.setupLights();
                this.createFloor();
                this.setupControls();
                this.setupEventListeners();
                
                this.clock = new THREE.Clock();
                this.animate();
            }
            
            setupLights() {
                const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
                this.scene.add(ambientLight);
                
                const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
                directionalLight.position.set(50, 50, 50);
                directionalLight.castShadow = true;
                
                // Shadow properties
                directionalLight.shadow.mapSize.width = 2048;
                directionalLight.shadow.mapSize.height = 2048;
                directionalLight.shadow.camera.near = 0.5;
                directionalLight.shadow.camera.far = 500;
                directionalLight.shadow.camera.left = -50;
                directionalLight.shadow.camera.right = 50;
                directionalLight.shadow.camera.top = 50;
                directionalLight.shadow.camera.bottom = -50;
                
                this.scene.add(directionalLight);
            }
            
            createFloor() {
                const gridSize = 10;
                
                for (let x = -gridSize/2; x < gridSize/2; x++) {
                    for (let z = -gridSize/2; z < gridSize/2; z++) {
                        let type = 'grass';
                        if (Math.random() > 0.8) type = 'dirt';
                        if (Math.random() > 0.95) type = 'stone';
                        
                        const block = new Block(x, -0.5, z, type);
                        block.addToScene(this.scene);
                        this.blocks.push(block);
                    }
                }
                
                // Add some raised blocks for collision testing
                for (let i = 0; i < 5; i++) {
                    const x = Math.floor(Math.random() * 8 - 4);
                    const z = Math.floor(Math.random() * 8 - 4);
                    const block = new Block(x, 0.5, z, 'stone');
                    block.addToScene(this.scene);
                    this.blocks.push(block);
                }
            }
            
            setupControls() {
                this.controls = new THREE.PointerLockControls(this.camera, document.body);
                
                const instructions = document.createElement('div');
                instructions.style.cssText = `
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-family: Arial;
                `;
                instructions.innerHTML = `
                    <h2>Minecraft Clone</h2>
                    <p>Click to play</p>
                    <p>WASD: Move | Mouse: Look around</p>
                    <p>Space: Jump | Left Click: Remove Block | Right Click: Place Block</p>
                `;
                document.body.appendChild(instructions);
                
                const startGame = () => {
                    this.controls.lock();
                    instructions.style.display = 'none';
                };
                
                document.body.addEventListener('click', startGame);
                
                this.controls.addEventListener('lock', () => {
                    instructions.style.display = 'none';
                });
                
                this.controls.addEventListener('unlock', () => {
                    instructions.style.display = 'block';
                });
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = true;
                            break;
                        case 'KeyS':
                            this.moveState.backward = true;
                            break;
                        case 'KeyA':
                            this.moveState.left = true;
                            break;
                        case 'KeyD':
                            this.moveState.right = true;
                            break;
                        case 'Space':
                            if (this.onGround) {
                                this.moveState.jump = true;
                            }
                            event.preventDefault();
                            break;
                    }
                });
                
                document.addEventListener('keyup', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = false;
                            break;
                        case 'KeyS':
                            this.moveState.backward = false;
                            break;
                        case 'KeyA':
                            this.moveState.left = false;
                            break;
                        case 'KeyD':
                            this.moveState.right = false;
                            break;
                        case 'Space':
                            this.moveState.jump = false;
                            break;
                    }
                });

                // Mouse click events
                document.addEventListener('mousedown', (event) => {
                    if (!this.controls.isLocked) return;
                    
                    if (event.button === 0) { // Left click
                        this.removeBlockAtPointer();
                    } else if (event.button === 2) { // Right click
                        this.placeBlockAtPointer();
                        event.preventDefault(); // Prevent context menu
                    }
                });

                // Prevent context menu on right click
                document.addEventListener('contextmenu', (event) => {
                    event.preventDefault();
                });
                
                window.addEventListener('resize', () => {
                    this.camera.aspect = window.innerWidth / window.innerHeight;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                });
            }

            removeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const blockMesh = intersection.object;
                    
                    const blockIndex = this.blocks.findIndex(block => block.mesh === blockMesh);
                    if (blockIndex !== -1) {
                        const block = this.blocks[blockIndex];
                        block.removeFromScene(this.scene);
                        this.blocks.splice(blockIndex, 1);
                        console.log('Block removed!');
                    }
                }
            }

            placeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const face = intersection.face;
                    const blockMesh = intersection.object;
                    
                    // Get the normal of the face that was hit
                    const normal = intersection.face.normal.clone();
                    normal.transformDirection(blockMesh.matrixWorld);
                    
                    // Find the block that was hit
                    const hitBlock = this.blocks.find(block => block.mesh === blockMesh);
                    if (!hitBlock) return;
                    
                    // Calculate position for new block (adjacent to the hit face)
                    const newPosition = new THREE.Vector3(
                        hitBlock.x + Math.round(normal.x),
                        hitBlock.y + Math.round(normal.y),
                        hitBlock.z + Math.round(normal.z)
                    );
                    
                    // Check if position is already occupied
                    const positionOccupied = this.blocks.some(block => 
                        block.x === newPosition.x && 
                        block.y === newPosition.y && 
                        block.z === newPosition.z
                    );
                    
                    // Check if position is too close to player (prevent blocking yourself)
                    const playerPosition = this.camera.position.clone();
                    const distanceToPlayer = newPosition.distanceTo(playerPosition);
                    
                    if (!positionOccupied && distanceToPlayer > 1.5) {
                        // Random block type
                        const blockTypes = ['grass', 'dirt', 'stone'];
                        const randomType = blockTypes[Math.floor(Math.random() * blockTypes.length)];
                        
                        // Create new block
                        const newBlock = new Block(newPosition.x, newPosition.y, newPosition.z, randomType);
                        newBlock.addToScene(this.scene);
                        this.blocks.push(newBlock);
                        
                        console.log(`Block placed at (${newPosition.x}, ${newPosition.y}, ${newPosition.z})`);
                    }
                }
            }
            
            checkCollision(newPosition) {
                const playerBox = new THREE.Box3(
                    new THREE.Vector3(
                        newPosition.x - this.playerRadius,
                        newPosition.y - this.playerHeight,
                        newPosition.z - this.playerRadius
                    ),
                    new THREE.Vector3(
                        newPosition.x + this.playerRadius,
                        newPosition.y,
                        newPosition.z + this.playerRadius
                    )
                );
                
                for (const block of this.blocks) {
                    const blockBox = block.getBoundingBox();
                    if (playerBox.intersectsBox(blockBox)) {
                        return true;
                    }
                }
                return false;
            }
            
            updateMovement(delta) {
                if (!this.controls.isLocked) return;
                
                const speed = 5.0;
                
                // Get camera direction vectors
                const cameraDirection = new THREE.Vector3();
                this.camera.getWorldDirection(cameraDirection);
                cameraDirection.y = 0;
                cameraDirection.normalize();
                
                // Get right vector
                const cameraRight = new THREE.Vector3();
                cameraRight.crossVectors(this.camera.up, cameraDirection).normalize();
                
                // Reset velocity
                this.velocity.x = 0;
                this.velocity.z = 0;
                
                // Apply movement based on camera orientation
                if (this.moveState.forward) {
                    this.velocity.add(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.backward) {
                    this.velocity.sub(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.left) {
                    this.velocity.add(cameraRight.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.right) {
                    this.velocity.sub(cameraRight.clone().multiplyScalar(speed * delta));
                }
                
                // Store current position for collision checking
                const oldPosition = this.camera.position.clone();
                
                // Apply horizontal movement with collision detection
                const newHorizontalPos = oldPosition.clone().add(this.velocity);
                if (!this.checkCollision(newHorizontalPos)) {
                    this.camera.position.x = newHorizontalPos.x;
                    this.camera.position.z = newHorizontalPos.z;
                }
                
                // Apply vertical movement (gravity and jumping)
                if (this.moveState.jump && this.onGround) {
                    this.velocity.y = this.jumpForce;
                    this.onGround = false;
                    this.moveState.jump = false;
                }
                
                this.velocity.y += this.gravity * delta;
                
                const newVerticalPos = this.camera.position.clone();
                newVerticalPos.y += this.velocity.y * delta;
                
                // Check if we're on the ground plane or outside bounds
                const gridSize = 10;
                const isOutsideGrid = Math.abs(this.camera.position.x) > gridSize/2 || 
                                    Math.abs(this.camera.position.z) > gridSize/2;
                
                if (isOutsideGrid) {
                    // Allow falling off edges
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                    }
                    this.onGround = false;
                } else {
                    // Normal collision detection
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                        this.onGround = false;
                    } else {
                        // We hit something vertically
                        if (this.velocity.y < 0) {
                            // Hit the ground
                            this.onGround = true;
                            this.velocity.y = 0;
                        } else {
                            // Hit ceiling
                            this.velocity.y = 0;
                        }
                    }
                }
                
                // Reset if player falls too far
                if (this.camera.position.y < -10) {
                    this.camera.position.set(0, 5, 0);
                    this.velocity.set(0, 0, 0);
                }
            }
            
            animate() {
                requestAnimationFrame(() => this.animate());
                
                const delta = Math.min(this.clock.getDelta(), 0.1);
                
                if (this.controls.isLocked) {
                    this.updateMovement(delta);
                }
                
                this.renderer.render(this.scene, this.camera);
            }
        }

        // Start the game
        new MinecraftGame();
    </script>
</body>
</html>
```

### mejoras

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Minecraft Clone</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial; }
        canvas { display: block; }
        #crosshair {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }
        #crosshair::before, #crosshair::after {
            content: '';
            position: absolute;
            background: white;
        }
        #crosshair::before {
            width: 2px;
            height: 20px;
            left: 50%;
            transform: translateX(-50%);
        }
        #crosshair::after {
            width: 20px;
            height: 2px;
            top: 50%;
            transform: translateY(-50%);
        }
        #ui {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 10px;
            border-radius: 5px;
            pointer-events: none;
        }
        #block-selector {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.7);
            padding: 10px;
            border-radius: 5px;
            display: flex;
            gap: 10px;
        }
        .block-option {
            width: 40px;
            height: 40px;
            border: 2px solid transparent;
            border-radius: 3px;
            cursor: pointer;
            pointer-events: auto;
        }
        .block-option.selected {
            border-color: white;
        }
        #reset-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(255,0,0,0.7);
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            pointer-events: auto;
        }
        #reset-btn:hover {
            background: rgba(255,0,0,0.9);
        }
    </style>
</head>
<body>
    <div id="crosshair"></div>
    <div id="ui">
        <div>WASD: Move | Mouse: Look</div>
        <div>Space: Jump | LClick: Remove | RClick: Place</div>
        <div>1,2,3: Select Block Type</div>
    </div>
    <div id="block-selector">
        <div class="block-option selected" data-type="grass" style="background: #4CAF50;"></div>
        <div class="block-option" data-type="dirt" style="background: #795548;"></div>
        <div class="block-option" data-type="stone" style="background: #9E9E9E;"></div>
    </div>
    <button id="reset-btn">Reset World</button>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>
    <script>
        // Block class
        class Block {
            constructor(x, y, z, type = 'grass') {
                this.x = x;
                this.y = y;
                this.z = z;
                this.type = type;
                this.mesh = null;
                
                this.createMesh();
            }
            
            createMesh() {
                const geometry = new THREE.BoxGeometry(1, 1, 1);
                
                const colors = {
                    'grass': 0x4CAF50,
                    'dirt': 0x795548,
                    'stone': 0x9E9E9E
                };

                // Create canvas for texture
                const canvas = document.createElement('canvas');
                canvas.width = 64;
                canvas.height = 64;
                const context = canvas.getContext('2d');

                // Base color
                const color = colors[this.type] || 0x4CAF50;
                const r = (color >> 16) & 255;
                const g = (color >> 8) & 255;
                const b = color & 255;

                // Fill with base color
                context.fillStyle = `rgb(${r}, ${g}, ${b})`;
                context.fillRect(0, 0, 64, 64);

                // Add texture pattern (simulated noise/pattern)
                context.globalAlpha = 0.3;
                for (let i = 0; i < 200; i++) {
                    const x = Math.random() * 64;
                    const y = Math.random() * 64;
                    const size = Math.random() * 3 + 1;
                    const brightness = Math.random() * 50 - 25;
                    
                    context.fillStyle = `rgb(${Math.max(0, Math.min(255, r + brightness))}, 
                                            ${Math.max(0, Math.min(255, g + brightness))}, 
                                            ${Math.max(0, Math.min(255, b + brightness))})`;
                    context.fillRect(x, y, size, size);
                }

                // Create texture from canvas
                const texture = new THREE.CanvasTexture(canvas);
                texture.wrapS = THREE.RepeatWrapping;
                texture.wrapT = THREE.RepeatWrapping;
                texture.repeat.set(1, 1);

                const material = new THREE.MeshPhongMaterial({ 
                    map: texture,
                    color: new THREE.Color(color)
                });
                
                this.mesh = new THREE.Mesh(geometry, material);
                this.mesh.position.set(this.x, this.y, this.z);
                
                // Enable shadows
                this.mesh.castShadow = true;
                this.mesh.receiveShadow = true;
            }
            
            addToScene(scene) {
                if (this.mesh) {
                    scene.add(this.mesh);
                }
            }
            
            removeFromScene(scene) {
                if (this.mesh) {
                    scene.remove(this.mesh);
                }
            }
            
            getBoundingBox() {
                return new THREE.Box3().setFromObject(this.mesh);
            }

            serialize() {
                return {
                    x: this.x,
                    y: this.y,
                    z: this.z,
                    type: this.type
                };
            }
        }

        // Game class
        class MinecraftGame {
            constructor() {
                this.scene = new THREE.Scene();
                this.scene.background = new THREE.Color(0x87CEEB);
                
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.camera.position.set(0, 2, 5);
                
                this.renderer = new THREE.WebGLRenderer({ antialias: true });
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                this.renderer.shadowMap.enabled = true;
                this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
                document.body.appendChild(this.renderer.domElement);
                
                this.controls = null;
                this.blocks = [];
                this.moveState = { forward: false, backward: false, left: false, right: false, jump: false };
                this.velocity = new THREE.Vector3();
                
                // Block selection
                this.selectedBlockType = 'grass';
                
                // Physics properties
                this.onGround = false;
                this.gravity = -20;
                this.jumpForce = 8;
                this.playerHeight = 1.8;
                this.playerRadius = 0.3;
                
                // Raycasting
                this.raycaster = new THREE.Raycaster();
                this.raycaster.far = 10;
                
                this.setupLights();
                this.setupControls();
                this.setupEventListeners();
                this.setupUI();
                
                // Load saved world or create default
                this.loadWorld();
                
                this.clock = new THREE.Clock();
                this.animate();
            }
            
            setupLights() {
                const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
                this.scene.add(ambientLight);
                
                const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
                directionalLight.position.set(50, 50, 50);
                directionalLight.castShadow = true;
                
                // Shadow properties
                directionalLight.shadow.mapSize.width = 2048;
                directionalLight.shadow.mapSize.height = 2048;
                directionalLight.shadow.camera.near = 0.5;
                directionalLight.shadow.camera.far = 500;
                directionalLight.shadow.camera.left = -50;
                directionalLight.shadow.camera.right = 50;
                directionalLight.shadow.camera.top = 50;
                directionalLight.shadow.camera.bottom = -50;
                
                this.scene.add(directionalLight);
            }
            
            createDefaultWorld() {
                // Clear existing blocks
                this.blocks.forEach(block => block.removeFromScene(this.scene));
                this.blocks = [];
                
                const gridSize = 10;
                
                // Create floor
                for (let x = -gridSize/2; x < gridSize/2; x++) {
                    for (let z = -gridSize/2; z < gridSize/2; z++) {
                        let type = 'grass';
                        if (Math.random() > 0.8) type = 'dirt';
                        if (Math.random() > 0.95) type = 'stone';
                        
                        const block = new Block(x, -0.5, z, type);
                        block.addToScene(this.scene);
                        this.blocks.push(block);
                    }
                }
                
                // Add some raised blocks
                for (let i = 0; i < 5; i++) {
                    const x = Math.floor(Math.random() * 8 - 4);
                    const z = Math.floor(Math.random() * 8 - 4);
                    const block = new Block(x, 0.5, z, 'stone');
                    block.addToScene(this.scene);
                    this.blocks.push(block);
                }
                
                this.saveWorld();
            }
            
            setupControls() {
                this.controls = new THREE.PointerLockControls(this.camera, document.body);
                
                const instructions = document.createElement('div');
                instructions.style.cssText = `
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-family: Arial;
                `;
                instructions.innerHTML = `
                    <h2>Minecraft Clone</h2>
                    <p>Click to play</p>
                    <p>WASD: Move | Mouse: Look around</p>
                    <p>Space: Jump | Left Click: Remove | Right Click: Place</p>
                    <p>1,2,3: Select Block Type | World auto-saves</p>
                `;
                document.body.appendChild(instructions);
                
                const startGame = () => {
                    this.controls.lock();
                    instructions.style.display = 'none';
                };
                
                document.body.addEventListener('click', startGame);
                
                this.controls.addEventListener('lock', () => {
                    instructions.style.display = 'none';
                });
                
                this.controls.addEventListener('unlock', () => {
                    instructions.style.display = 'block';
                });
            }
            
            setupUI() {
                // Block selector
                const blockOptions = document.querySelectorAll('.block-option');
                blockOptions.forEach(option => {
                    option.addEventListener('click', () => {
                        blockOptions.forEach(opt => opt.classList.remove('selected'));
                        option.classList.add('selected');
                        this.selectedBlockType = option.dataset.type;
                    });
                });

                // Reset button
                document.getElementById('reset-btn').addEventListener('click', () => {
                    if (confirm('Are you sure you want to reset the world?')) {
                        this.createDefaultWorld();
                    }
                });
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = true;
                            break;
                        case 'KeyS':
                            this.moveState.backward = true;
                            break;
                        case 'KeyA':
                            this.moveState.left = true;
                            break;
                        case 'KeyD':
                            this.moveState.right = true;
                            break;
                        case 'Space':
                            if (this.onGround) {
                                this.moveState.jump = true;
                            }
                            event.preventDefault();
                            break;
                        case 'Digit1':
                            this.selectBlockType('grass');
                            break;
                        case 'Digit2':
                            this.selectBlockType('dirt');
                            break;
                        case 'Digit3':
                            this.selectBlockType('stone');
                            break;
                    }
                });
                
                document.addEventListener('keyup', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = false;
                            break;
                        case 'KeyS':
                            this.moveState.backward = false;
                            break;
                        case 'KeyA':
                            this.moveState.left = false;
                            break;
                        case 'KeyD':
                            this.moveState.right = false;
                            break;
                        case 'Space':
                            this.moveState.jump = false;
                            break;
                    }
                });

                // Mouse click events
                document.addEventListener('mousedown', (event) => {
                    if (!this.controls.isLocked) return;
                    
                    if (event.button === 0) { // Left click
                        this.removeBlockAtPointer();
                    } else if (event.button === 2) { // Right click
                        this.placeBlockAtPointer();
                        event.preventDefault();
                    }
                });

                document.addEventListener('contextmenu', (event) => {
                    event.preventDefault();
                });
                
                window.addEventListener('resize', () => {
                    this.camera.aspect = window.innerWidth / window.innerHeight;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                });

                // Auto-save when leaving page
                window.addEventListener('beforeunload', () => {
                    this.saveWorld();
                });
            }

            selectBlockType(type) {
                this.selectedBlockType = type;
                const blockOptions = document.querySelectorAll('.block-option');
                blockOptions.forEach(option => {
                    option.classList.toggle('selected', option.dataset.type === type);
                });
            }

            saveWorld() {
                const worldData = {
                    blocks: this.blocks.map(block => block.serialize()),
                    playerPosition: {
                        x: this.camera.position.x,
                        y: this.camera.position.y,
                        z: this.camera.position.z
                    }
                };
                localStorage.setItem('minecraftWorld', JSON.stringify(worldData));
                console.log('World saved!');
            }

            loadWorld() {
                const saved = localStorage.getItem('minecraftWorld');
                if (saved) {
                    try {
                        const worldData = JSON.parse(saved);
                        
                        // Clear existing blocks
                        this.blocks.forEach(block => block.removeFromScene(this.scene));
                        this.blocks = [];
                        
                        // Load blocks
                        worldData.blocks.forEach(blockData => {
                            const block = new Block(blockData.x, blockData.y, blockData.z, blockData.type);
                            block.addToScene(this.scene);
                            this.blocks.push(block);
                        });
                        
                        // Load player position
                        if (worldData.playerPosition) {
                            this.camera.position.set(
                                worldData.playerPosition.x,
                                worldData.playerPosition.y,
                                worldData.playerPosition.z
                            );
                        }
                        
                        console.log('World loaded!');
                    } catch (e) {
                        console.error('Error loading world:', e);
                        this.createDefaultWorld();
                    }
                } else {
                    this.createDefaultWorld();
                }
            }

            removeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const blockMesh = intersection.object;
                    
                    const blockIndex = this.blocks.findIndex(block => block.mesh === blockMesh);
                    if (blockIndex !== -1) {
                        const block = this.blocks[blockIndex];
                        block.removeFromScene(this.scene);
                        this.blocks.splice(blockIndex, 1);
                        this.saveWorld();
                        console.log('Block removed!');
                    }
                }
            }

            placeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const face = intersection.face;
                    const blockMesh = intersection.object;
                    
                    const normal = intersection.face.normal.clone();
                    normal.transformDirection(blockMesh.matrixWorld);
                    
                    const hitBlock = this.blocks.find(block => block.mesh === blockMesh);
                    if (!hitBlock) return;
                    
                    const newPosition = new THREE.Vector3(
                        hitBlock.x + Math.round(normal.x),
                        hitBlock.y + Math.round(normal.y),
                        hitBlock.z + Math.round(normal.z)
                    );
                    
                    const positionOccupied = this.blocks.some(block => 
                        block.x === newPosition.x && 
                        block.y === newPosition.y && 
                        block.z === newPosition.z
                    );
                    
                    const playerPosition = this.camera.position.clone();
                    const distanceToPlayer = newPosition.distanceTo(playerPosition);
                    
                    if (!positionOccupied && distanceToPlayer > 1.5) {
                        const newBlock = new Block(newPosition.x, newPosition.y, newPosition.z, this.selectedBlockType);
                        newBlock.addToScene(this.scene);
                        this.blocks.push(newBlock);
                        this.saveWorld();
                        console.log(`Block placed at (${newPosition.x}, ${newPosition.y}, ${newPosition.z})`);
                    }
                }
            }
            
            checkCollision(newPosition) {
                const playerBox = new THREE.Box3(
                    new THREE.Vector3(
                        newPosition.x - this.playerRadius,
                        newPosition.y - this.playerHeight,
                        newPosition.z - this.playerRadius
                    ),
                    new THREE.Vector3(
                        newPosition.x + this.playerRadius,
                        newPosition.y,
                        newPosition.z + this.playerRadius
                    )
                );
                
                for (const block of this.blocks) {
                    const blockBox = block.getBoundingBox();
                    if (playerBox.intersectsBox(blockBox)) {
                        return true;
                    }
                }
                return false;
            }
            
            updateMovement(delta) {
                if (!this.controls.isLocked) return;
                
                const speed = 5.0;
                
                const cameraDirection = new THREE.Vector3();
                this.camera.getWorldDirection(cameraDirection);
                cameraDirection.y = 0;
                cameraDirection.normalize();
                
                const cameraRight = new THREE.Vector3();
                cameraRight.crossVectors(this.camera.up, cameraDirection).normalize();
                
                this.velocity.x = 0;
                this.velocity.z = 0;
                
                if (this.moveState.forward) {
                    this.velocity.add(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.backward) {
                    this.velocity.sub(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.left) {
                    this.velocity.add(cameraRight.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.right) {
                    this.velocity.sub(cameraRight.clone().multiplyScalar(speed * delta));
                }
                
                const oldPosition = this.camera.position.clone();
                const newHorizontalPos = oldPosition.clone().add(this.velocity);
                if (!this.checkCollision(newHorizontalPos)) {
                    this.camera.position.x = newHorizontalPos.x;
                    this.camera.position.z = newHorizontalPos.z;
                }
                
                if (this.moveState.jump && this.onGround) {
                    this.velocity.y = this.jumpForce;
                    this.onGround = false;
                    this.moveState.jump = false;
                }
                
                this.velocity.y += this.gravity * delta;
                
                const newVerticalPos = this.camera.position.clone();
                newVerticalPos.y += this.velocity.y * delta;
                
                const gridSize = 10;
                const isOutsideGrid = Math.abs(this.camera.position.x) > gridSize/2 || 
                                    Math.abs(this.camera.position.z) > gridSize/2;
                
                if (isOutsideGrid) {
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                    }
                    this.onGround = false;
                } else {
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                        this.onGround = false;
                    } else {
                        if (this.velocity.y < 0) {
                            this.onGround = true;
                            this.velocity.y = 0;
                        } else {
                            this.velocity.y = 0;
                        }
                    }
                }
                
                if (this.camera.position.y < -10) {
                    this.camera.position.set(0, 5, 0);
                    this.velocity.set(0, 0, 0);
                }

                // Auto-save every 10 seconds
                if (Math.floor(this.clock.getElapsedTime()) % 10 === 0) {
                    this.saveWorld();
                }
            }
            
            animate() {
                requestAnimationFrame(() => this.animate());
                
                const delta = Math.min(this.clock.getDelta(), 0.1);
                
                if (this.controls.isLocked) {
                    this.updateMovement(delta);
                }
                
                this.renderer.render(this.scene, this.camera);
            }
        }

        // Start the game
        new MinecraftGame();
    </script>
</body>
</html>
```

### no antialias

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Minecraft Clone</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial; }
        canvas { display: block; }
        #crosshair {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }
        #crosshair::before, #crosshair::after {
            content: '';
            position: absolute;
            background: white;
        }
        #crosshair::before {
            width: 2px;
            height: 20px;
            left: 50%;
            transform: translateX(-50%);
        }
        #crosshair::after {
            width: 20px;
            height: 2px;
            top: 50%;
            transform: translateY(-50%);
        }
        #ui {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 10px;
            border-radius: 5px;
            pointer-events: none;
        }
        #block-selector {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.7);
            padding: 10px;
            border-radius: 5px;
            display: flex;
            gap: 10px;
        }
        .block-option {
            width: 40px;
            height: 40px;
            border: 2px solid transparent;
            border-radius: 3px;
            cursor: pointer;
            pointer-events: auto;
        }
        .block-option.selected {
            border-color: white;
        }
        #reset-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(255,0,0,0.7);
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            pointer-events: auto;
        }
        #reset-btn:hover {
            background: rgba(255,0,0,0.9);
        }
    </style>
</head>
<body>
    <div id="crosshair"></div>
    <div id="ui">
        <div>WASD: Move | Mouse: Look</div>
        <div>Space: Jump | LClick: Remove | RClick: Place</div>
        <div>1,2,3: Select Block Type</div>
    </div>
    <div id="block-selector">
        <div class="block-option selected" data-type="grass" style="background: #4CAF50;"></div>
        <div class="block-option" data-type="dirt" style="background: #795548;"></div>
        <div class="block-option" data-type="stone" style="background: #9E9E9E;"></div>
    </div>
    <button id="reset-btn">Reset World</button>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>
    <script>
        // Block class
        class Block {
            constructor(x, y, z, type = 'grass') {
                this.x = x;
                this.y = y;
                this.z = z;
                this.type = type;
                this.mesh = null;
                
                this.createMesh();
            }
            
            createMesh() {
                const geometry = new THREE.BoxGeometry(1, 1, 1);
                
                const colors = {
                    'grass': 0x4CAF50,
                    'dirt': 0x795548,
                    'stone': 0x9E9E9E
                };

                // Create canvas for texture
                const canvas = document.createElement('canvas');
                canvas.width = 64;
                canvas.height = 64;
                const context = canvas.getContext('2d');

                // Base color
                const color = colors[this.type] || 0x4CAF50;
                const r = (color >> 16) & 255;
                const g = (color >> 8) & 255;
                const b = color & 255;

                // Fill with base color
                context.fillStyle = `rgb(${r}, ${g}, ${b})`;
                context.fillRect(0, 0, 64, 64);

                // Add texture pattern (simulated noise/pattern)
                context.globalAlpha = 0.3;
                for (let i = 0; i < 200; i++) {
                    const x = Math.random() * 64;
                    const y = Math.random() * 64;
                    const size = Math.random() * 3 + 1;
                    const brightness = Math.random() * 50 - 25;
                    
                    context.fillStyle = `rgb(${Math.max(0, Math.min(255, r + brightness))}, 
                                            ${Math.max(0, Math.min(255, g + brightness))}, 
                                            ${Math.max(0, Math.min(255, b + brightness))})`;
                    context.fillRect(x, y, size, size);
                }

                // Create texture from canvas
                const texture = new THREE.CanvasTexture(canvas);
                texture.wrapS = THREE.RepeatWrapping;
                texture.wrapT = THREE.RepeatWrapping;
                texture.repeat.set(1, 1);
                
                texture.magFilter = THREE.NearestFilter;
                texture.minFilter = THREE.NearestFilter;
                texture.generateMipmaps = false;

                const material = new THREE.MeshPhongMaterial({ 
                    map: texture,
                    color: new THREE.Color(color)
                });
                
                this.mesh = new THREE.Mesh(geometry, material);
                this.mesh.position.set(this.x, this.y, this.z);
                
                // Enable shadows
                this.mesh.castShadow = true;
                this.mesh.receiveShadow = true;
            }
            
            addToScene(scene) {
                if (this.mesh) {
                    scene.add(this.mesh);
                }
            }
            
            removeFromScene(scene) {
                if (this.mesh) {
                    scene.remove(this.mesh);
                }
            }
            
            getBoundingBox() {
                return new THREE.Box3().setFromObject(this.mesh);
            }

            serialize() {
                return {
                    x: this.x,
                    y: this.y,
                    z: this.z,
                    type: this.type
                };
            }
        }

        // Game class
        class MinecraftGame {
            constructor() {
                this.scene = new THREE.Scene();
                this.scene.background = new THREE.Color(0x87CEEB);
                
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.camera.position.set(0, 2, 5);
                
                this.renderer = new THREE.WebGLRenderer({ antialias: true });
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                this.renderer.shadowMap.enabled = true;
                this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
                document.body.appendChild(this.renderer.domElement);
                
                this.controls = null;
                this.blocks = [];
                this.moveState = { forward: false, backward: false, left: false, right: false, jump: false };
                this.velocity = new THREE.Vector3();
                
                // Block selection
                this.selectedBlockType = 'grass';
                
                // Physics properties
                this.onGround = false;
                this.gravity = -20;
                this.jumpForce = 8;
                this.playerHeight = 1.8;
                this.playerRadius = 0.3;
                
                // Raycasting
                this.raycaster = new THREE.Raycaster();
                this.raycaster.far = 10;
                
                this.setupLights();
                this.setupControls();
                this.setupEventListeners();
                this.setupUI();
                
                // Load saved world or create default
                this.loadWorld();
                
                this.clock = new THREE.Clock();
                this.animate();
            }
            
            setupLights() {
                const ambientLight = new THREE.AmbientLight(0x404040, 2);
                this.scene.add(ambientLight);
                
                const directionalLight = new THREE.DirectionalLight(0xffffff, 2);
                directionalLight.position.set(50, 50, 50);
                directionalLight.castShadow = true;
                
                // Shadow properties
                directionalLight.shadow.mapSize.width = 2048;
                directionalLight.shadow.mapSize.height = 2048;
                directionalLight.shadow.camera.near = 0.5;
                directionalLight.shadow.camera.far = 500;
                directionalLight.shadow.camera.left = -50;
                directionalLight.shadow.camera.right = 50;
                directionalLight.shadow.camera.top = 50;
                directionalLight.shadow.camera.bottom = -50;
                
                this.scene.add(directionalLight);
            }
            
            createDefaultWorld() {
                // Clear existing blocks
                this.blocks.forEach(block => block.removeFromScene(this.scene));
                this.blocks = [];
                
                const gridSize = 10;
                
                // Create floor
                for (let x = -gridSize/2; x < gridSize/2; x++) {
                    for (let z = -gridSize/2; z < gridSize/2; z++) {
                        let type = 'grass';
                        if (Math.random() > 0.8) type = 'dirt';
                        if (Math.random() > 0.95) type = 'stone';
                        
                        const block = new Block(x, -0.5, z, type);
                        block.addToScene(this.scene);
                        this.blocks.push(block);
                    }
                }
                
                // Add some raised blocks
                for (let i = 0; i < 5; i++) {
                    const x = Math.floor(Math.random() * 8 - 4);
                    const z = Math.floor(Math.random() * 8 - 4);
                    const block = new Block(x, 0.5, z, 'stone');
                    block.addToScene(this.scene);
                    this.blocks.push(block);
                }
                
                this.saveWorld();
            }
            
            setupControls() {
                this.controls = new THREE.PointerLockControls(this.camera, document.body);
                
                const instructions = document.createElement('div');
                instructions.style.cssText = `
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-family: Arial;
                `;
                instructions.innerHTML = `
                    <h2>Minecraft Clone</h2>
                    <p>Click to play</p>
                    <p>WASD: Move | Mouse: Look around</p>
                    <p>Space: Jump | Left Click: Remove | Right Click: Place</p>
                    <p>1,2,3: Select Block Type | World auto-saves</p>
                `;
                document.body.appendChild(instructions);
                
                const startGame = () => {
                    this.controls.lock();
                    instructions.style.display = 'none';
                };
                
                document.body.addEventListener('click', startGame);
                
                this.controls.addEventListener('lock', () => {
                    instructions.style.display = 'none';
                });
                
                this.controls.addEventListener('unlock', () => {
                    instructions.style.display = 'block';
                });
            }
            
            setupUI() {
                // Block selector
                const blockOptions = document.querySelectorAll('.block-option');
                blockOptions.forEach(option => {
                    option.addEventListener('click', () => {
                        blockOptions.forEach(opt => opt.classList.remove('selected'));
                        option.classList.add('selected');
                        this.selectedBlockType = option.dataset.type;
                    });
                });

                // Reset button
                document.getElementById('reset-btn').addEventListener('click', () => {
                    if (confirm('Are you sure you want to reset the world?')) {
                        this.createDefaultWorld();
                    }
                });
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = true;
                            break;
                        case 'KeyS':
                            this.moveState.backward = true;
                            break;
                        case 'KeyA':
                            this.moveState.left = true;
                            break;
                        case 'KeyD':
                            this.moveState.right = true;
                            break;
                        case 'Space':
                            if (this.onGround) {
                                this.moveState.jump = true;
                            }
                            event.preventDefault();
                            break;
                        case 'Digit1':
                            this.selectBlockType('grass');
                            break;
                        case 'Digit2':
                            this.selectBlockType('dirt');
                            break;
                        case 'Digit3':
                            this.selectBlockType('stone');
                            break;
                    }
                });
                
                document.addEventListener('keyup', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = false;
                            break;
                        case 'KeyS':
                            this.moveState.backward = false;
                            break;
                        case 'KeyA':
                            this.moveState.left = false;
                            break;
                        case 'KeyD':
                            this.moveState.right = false;
                            break;
                        case 'Space':
                            this.moveState.jump = false;
                            break;
                    }
                });

                // Mouse click events
                document.addEventListener('mousedown', (event) => {
                    if (!this.controls.isLocked) return;
                    
                    if (event.button === 0) { // Left click
                        this.removeBlockAtPointer();
                    } else if (event.button === 2) { // Right click
                        this.placeBlockAtPointer();
                        event.preventDefault();
                    }
                });

                document.addEventListener('contextmenu', (event) => {
                    event.preventDefault();
                });
                
                window.addEventListener('resize', () => {
                    this.camera.aspect = window.innerWidth / window.innerHeight;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                });

                // Auto-save when leaving page
                window.addEventListener('beforeunload', () => {
                    this.saveWorld();
                });
            }

            selectBlockType(type) {
                this.selectedBlockType = type;
                const blockOptions = document.querySelectorAll('.block-option');
                blockOptions.forEach(option => {
                    option.classList.toggle('selected', option.dataset.type === type);
                });
            }

            saveWorld() {
                const worldData = {
                    blocks: this.blocks.map(block => block.serialize()),
                    playerPosition: {
                        x: this.camera.position.x,
                        y: this.camera.position.y,
                        z: this.camera.position.z
                    }
                };
                localStorage.setItem('minecraftWorld', JSON.stringify(worldData));
                console.log('World saved!');
            }

            loadWorld() {
                const saved = localStorage.getItem('minecraftWorld');
                if (saved) {
                    try {
                        const worldData = JSON.parse(saved);
                        
                        // Clear existing blocks
                        this.blocks.forEach(block => block.removeFromScene(this.scene));
                        this.blocks = [];
                        
                        // Load blocks
                        worldData.blocks.forEach(blockData => {
                            const block = new Block(blockData.x, blockData.y, blockData.z, blockData.type);
                            block.addToScene(this.scene);
                            this.blocks.push(block);
                        });
                        
                        // Load player position
                        if (worldData.playerPosition) {
                            this.camera.position.set(
                                worldData.playerPosition.x,
                                worldData.playerPosition.y,
                                worldData.playerPosition.z
                            );
                        }
                        
                        console.log('World loaded!');
                    } catch (e) {
                        console.error('Error loading world:', e);
                        this.createDefaultWorld();
                    }
                } else {
                    this.createDefaultWorld();
                }
            }

            removeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const blockMesh = intersection.object;
                    
                    const blockIndex = this.blocks.findIndex(block => block.mesh === blockMesh);
                    if (blockIndex !== -1) {
                        const block = this.blocks[blockIndex];
                        block.removeFromScene(this.scene);
                        this.blocks.splice(blockIndex, 1);
                        this.saveWorld();
                        console.log('Block removed!');
                    }
                }
            }

            placeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const face = intersection.face;
                    const blockMesh = intersection.object;
                    
                    const normal = intersection.face.normal.clone();
                    normal.transformDirection(blockMesh.matrixWorld);
                    
                    const hitBlock = this.blocks.find(block => block.mesh === blockMesh);
                    if (!hitBlock) return;
                    
                    const newPosition = new THREE.Vector3(
                        hitBlock.x + Math.round(normal.x),
                        hitBlock.y + Math.round(normal.y),
                        hitBlock.z + Math.round(normal.z)
                    );
                    
                    const positionOccupied = this.blocks.some(block => 
                        block.x === newPosition.x && 
                        block.y === newPosition.y && 
                        block.z === newPosition.z
                    );
                    
                    const playerPosition = this.camera.position.clone();
                    const distanceToPlayer = newPosition.distanceTo(playerPosition);
                    
                    if (!positionOccupied && distanceToPlayer > 1.5) {
                        const newBlock = new Block(newPosition.x, newPosition.y, newPosition.z, this.selectedBlockType);
                        newBlock.addToScene(this.scene);
                        this.blocks.push(newBlock);
                        this.saveWorld();
                        console.log(`Block placed at (${newPosition.x}, ${newPosition.y}, ${newPosition.z})`);
                    }
                }
            }
            
            checkCollision(newPosition) {
                const playerBox = new THREE.Box3(
                    new THREE.Vector3(
                        newPosition.x - this.playerRadius,
                        newPosition.y - this.playerHeight,
                        newPosition.z - this.playerRadius
                    ),
                    new THREE.Vector3(
                        newPosition.x + this.playerRadius,
                        newPosition.y,
                        newPosition.z + this.playerRadius
                    )
                );
                
                for (const block of this.blocks) {
                    const blockBox = block.getBoundingBox();
                    if (playerBox.intersectsBox(blockBox)) {
                        return true;
                    }
                }
                return false;
            }
            
            updateMovement(delta) {
                if (!this.controls.isLocked) return;
                
                const speed = 5.0;
                
                const cameraDirection = new THREE.Vector3();
                this.camera.getWorldDirection(cameraDirection);
                cameraDirection.y = 0;
                cameraDirection.normalize();
                
                const cameraRight = new THREE.Vector3();
                cameraRight.crossVectors(this.camera.up, cameraDirection).normalize();
                
                this.velocity.x = 0;
                this.velocity.z = 0;
                
                if (this.moveState.forward) {
                    this.velocity.add(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.backward) {
                    this.velocity.sub(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.left) {
                    this.velocity.add(cameraRight.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.right) {
                    this.velocity.sub(cameraRight.clone().multiplyScalar(speed * delta));
                }
                
                const oldPosition = this.camera.position.clone();
                const newHorizontalPos = oldPosition.clone().add(this.velocity);
                if (!this.checkCollision(newHorizontalPos)) {
                    this.camera.position.x = newHorizontalPos.x;
                    this.camera.position.z = newHorizontalPos.z;
                }
                
                if (this.moveState.jump && this.onGround) {
                    this.velocity.y = this.jumpForce;
                    this.onGround = false;
                    this.moveState.jump = false;
                }
                
                this.velocity.y += this.gravity * delta;
                
                const newVerticalPos = this.camera.position.clone();
                newVerticalPos.y += this.velocity.y * delta;
                
                const gridSize = 10;
                const isOutsideGrid = Math.abs(this.camera.position.x) > gridSize/2 || 
                                    Math.abs(this.camera.position.z) > gridSize/2;
                
                if (isOutsideGrid) {
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                    }
                    this.onGround = false;
                } else {
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                        this.onGround = false;
                    } else {
                        if (this.velocity.y < 0) {
                            this.onGround = true;
                            this.velocity.y = 0;
                        } else {
                            this.velocity.y = 0;
                        }
                    }
                }
                
                if (this.camera.position.y < -10) {
                    this.camera.position.set(0, 5, 0);
                    this.velocity.set(0, 0, 0);
                }

                // Auto-save every 10 seconds
                if (Math.floor(this.clock.getElapsedTime()) % 10 === 0) {
                    this.saveWorld();
                }
            }
            
            animate() {
                requestAnimationFrame(() => this.animate());
                
                const delta = Math.min(this.clock.getDelta(), 0.1);
                
                if (this.controls.isLocked) {
                    this.updateMovement(delta);
                }
                
                this.renderer.render(this.scene, this.camera);
            }
        }

        // Start the game
        new MinecraftGame();
    </script>
</body>
</html>
```

### ssao

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Minecraft Clone</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial; }
        canvas { display: block; }
        #crosshair {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }
        #crosshair::before, #crosshair::after {
            content: '';
            position: absolute;
            background: white;
        }
        #crosshair::before {
            width: 2px;
            height: 20px;
            left: 50%;
            transform: translateX(-50%);
        }
        #crosshair::after {
            width: 20px;
            height: 2px;
            top: 50%;
            transform: translateY(-50%);
        }
        #ui {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 10px;
            border-radius: 5px;
            pointer-events: none;
        }
        #block-selector {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.7);
            padding: 10px;
            border-radius: 5px;
            display: flex;
            gap: 10px;
        }
        .block-option {
            width: 40px;
            height: 40px;
            border: 2px solid transparent;
            border-radius: 3px;
            cursor: pointer;
            pointer-events: auto;
        }
        .block-option.selected {
            border-color: white;
        }
        #reset-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(255,0,0,0.7);
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            pointer-events: auto;
        }
        #reset-btn:hover {
            background: rgba(255,0,0,0.9);
        }
    </style>
</head>
<body>
    <div id="crosshair"></div>
    <div id="ui">
        <div>WASD: Move | Mouse: Look</div>
        <div>Space: Jump | LClick: Remove | RClick: Place</div>
        <div>1,2,3: Select Block Type | World auto-saves</div>
    </div>
    <div id="block-selector">
        <div class="block-option selected" data-type="grass" style="background: #4CAF50;"></div>
        <div class="block-option" data-type="dirt" style="background: #795548;"></div>
        <div class="block-option" data-type="stone" style="background: #9E9E9E;"></div>
    </div>
    <button id="reset-btn">Reset World</button>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>
    
    <!-- Postprocessing Dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/SSAOShader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/SAOShader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/SSAOPass.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/math/SimplexNoise.js"></script>

    <script>
        // Block class
        class Block {
            constructor(x, y, z, type = 'grass') {
                this.x = x;
                this.y = y;
                this.z = z;
                this.type = type;
                this.mesh = null;
                
                this.createMesh();
            }
            
            createMesh() {
                const geometry = new THREE.BoxGeometry(1, 1, 1);
                
                const colors = {
                    'grass': 0x4CAF50,
                    'dirt': 0x795548,
                    'stone': 0x9E9E9E
                };

                // Create canvas for texture
                const canvas = document.createElement('canvas');
                canvas.width = 64;
                canvas.height = 64;
                const context = canvas.getContext('2d');

                // Base color
                const color = colors[this.type] || 0x4CAF50;
                const r = (color >> 16) & 255;
                const g = (color >> 8) & 255;
                const b = color & 255;

                // Fill with base color
                context.fillStyle = `rgb(${r}, ${g}, ${b})`;
                context.fillRect(0, 0, 64, 64);

                // Add texture pattern (simulated noise/pattern)
                context.globalAlpha = 0.3;
                for (let i = 0; i < 200; i++) {
                    const x = Math.random() * 64;
                    const y = Math.random() * 64;
                    const size = Math.random() * 3 + 1;
                    const brightness = Math.random() * 50 - 25;
                    
                    context.fillStyle = `rgb(${Math.max(0, Math.min(255, r + brightness))}, 
                                            ${Math.max(0, Math.min(255, g + brightness))}, 
                                            ${Math.max(0, Math.min(255, b + brightness))})`;
                    context.fillRect(x, y, size, size);
                }

                // Create texture from canvas
                const texture = new THREE.CanvasTexture(canvas);
                texture.wrapS = THREE.RepeatWrapping;
                texture.wrapT = THREE.RepeatWrapping;
                texture.repeat.set(1, 1);
                
                texture.magFilter = THREE.NearestFilter;
                texture.minFilter = THREE.NearestFilter;
                texture.generateMipmaps = false;

                const material = new THREE.MeshPhongMaterial({ 
                    map: texture,
                    color: new THREE.Color(color)
                });
                
                this.mesh = new THREE.Mesh(geometry, material);
                this.mesh.position.set(this.x, this.y, this.z);
                
                // Enable shadows
                this.mesh.castShadow = true;
                this.mesh.receiveShadow = true;
            }
            
            addToScene(scene) {
                if (this.mesh) {
                    scene.add(this.mesh);
                }
            }
            
            removeFromScene(scene) {
                if (this.mesh) {
                    scene.remove(this.mesh);
                }
            }
            
            getBoundingBox() {
                return new THREE.Box3().setFromObject(this.mesh);
            }

            serialize() {
                return {
                    x: this.x,
                    y: this.y,
                    z: this.z,
                    type: this.type
                };
            }
        }

        // Game class
        class MinecraftGame {
            constructor() {
                this.scene = new THREE.Scene();
                this.scene.background = new THREE.Color(0x87CEEB);
                
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.camera.position.set(0, 2, 5);
                
                this.renderer = new THREE.WebGLRenderer({ antialias: true });
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                this.renderer.shadowMap.enabled = true;
                this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
                document.body.appendChild(this.renderer.domElement);
                
                // Postprocessing setup
                this.setupPostProcessing();
                
                this.controls = null;
                this.blocks = [];
                this.moveState = { forward: false, backward: false, left: false, right: false, jump: false };
                this.velocity = new THREE.Vector3();
                
                // Block selection
                this.selectedBlockType = 'grass';
                
                // Physics properties
                this.onGround = false;
                this.gravity = -20;
                this.jumpForce = 8;
                this.playerHeight = 1.8;
                this.playerRadius = 0.3;
                
                // Raycasting
                this.raycaster = new THREE.Raycaster();
                this.raycaster.far = 10;
                
                this.setupLights();
                this.setupControls();
                this.setupEventListeners();
                this.setupUI();
                
                // Load saved world or create default
                this.loadWorld();
                
                this.clock = new THREE.Clock();
                this.animate();
            }
            
            setupPostProcessing() {
                // Create effect composer
                this.composer = new THREE.EffectComposer(this.renderer);
                
                // Add render pass
                const renderPass = new THREE.RenderPass(this.scene, this.camera);
                this.composer.addPass(renderPass);
                
                // Add SSAO pass
                this.ssaoPass = new THREE.SSAOPass(this.scene, this.camera, window.innerWidth, window.innerHeight);
                this.ssaoPass.kernelRadius = 16;
                this.ssaoPass.minDistance = 0.005;
                this.ssaoPass.maxDistance = 0.1;
                this.ssaoPass.output = THREE.SSAOPass.OUTPUT.Default;
                
                // Adjust SSAO intensity for better visibility
                this.ssaoPass.kernelSize = 32;
                this.ssaoPass.kernelRadius = 32;
                
                this.composer.addPass(this.ssaoPass);
            }
            
            setupLights() {
                const ambientLight = new THREE.AmbientLight(0x404040, 2);
                this.scene.add(ambientLight);
                
                const directionalLight = new THREE.DirectionalLight(0xffffff, 2);
                directionalLight.position.set(50, 50, 50);
                directionalLight.castShadow = true;
                
                // Shadow properties
                directionalLight.shadow.mapSize.width = 2048;
                directionalLight.shadow.mapSize.height = 2048;
                directionalLight.shadow.camera.near = 0.5;
                directionalLight.shadow.camera.far = 500;
                directionalLight.shadow.camera.left = -50;
                directionalLight.shadow.camera.right = 50;
                directionalLight.shadow.camera.top = 50;
                directionalLight.shadow.camera.bottom = -50;
                
                this.scene.add(directionalLight);
            }
            
            createDefaultWorld() {
                // Clear existing blocks
                this.blocks.forEach(block => block.removeFromScene(this.scene));
                this.blocks = [];
                
                const gridSize = 10;
                
                // Create floor
                for (let x = -gridSize/2; x < gridSize/2; x++) {
                    for (let z = -gridSize/2; z < gridSize/2; z++) {
                        let type = 'grass';
                        if (Math.random() > 0.8) type = 'dirt';
                        if (Math.random() > 0.95) type = 'stone';
                        
                        const block = new Block(x, -0.5, z, type);
                        block.addToScene(this.scene);
                        this.blocks.push(block);
                    }
                }
                
                // Add some raised blocks
                for (let i = 0; i < 5; i++) {
                    const x = Math.floor(Math.random() * 8 - 4);
                    const z = Math.floor(Math.random() * 8 - 4);
                    const block = new Block(x, 0.5, z, 'stone');
                    block.addToScene(this.scene);
                    this.blocks.push(block);
                }
                
                this.saveWorld();
            }
            
            setupControls() {
                this.controls = new THREE.PointerLockControls(this.camera, document.body);
                
                const instructions = document.createElement('div');
                instructions.style.cssText = `
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-family: Arial;
                `;
                instructions.innerHTML = `
                    <h2>Minecraft Clone</h2>
                    <p>Click to play</p>
                    <p>WASD: Move | Mouse: Look around</p>
                    <p>Space: Jump | Left Click: Remove | Right Click: Place</p>
                    <p>1,2,3: Select Block Type | World auto-saves</p>
                `;
                document.body.appendChild(instructions);
                
                const startGame = () => {
                    this.controls.lock();
                    instructions.style.display = 'none';
                };
                
                document.body.addEventListener('click', startGame);
                
                this.controls.addEventListener('lock', () => {
                    instructions.style.display = 'none';
                });
                
                this.controls.addEventListener('unlock', () => {
                    instructions.style.display = 'block';
                });
            }
            
            setupUI() {
                // Block selector
                const blockOptions = document.querySelectorAll('.block-option');
                blockOptions.forEach(option => {
                    option.addEventListener('click', () => {
                        blockOptions.forEach(opt => opt.classList.remove('selected'));
                        option.classList.add('selected');
                        this.selectedBlockType = option.dataset.type;
                    });
                });

                // Reset button
                document.getElementById('reset-btn').addEventListener('click', () => {
                    if (confirm('Are you sure you want to reset the world?')) {
                        this.createDefaultWorld();
                    }
                });
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = true;
                            break;
                        case 'KeyS':
                            this.moveState.backward = true;
                            break;
                        case 'KeyA':
                            this.moveState.left = true;
                            break;
                        case 'KeyD':
                            this.moveState.right = true;
                            break;
                        case 'Space':
                            if (this.onGround) {
                                this.moveState.jump = true;
                            }
                            event.preventDefault();
                            break;
                        case 'Digit1':
                            this.selectBlockType('grass');
                            break;
                        case 'Digit2':
                            this.selectBlockType('dirt');
                            break;
                        case 'Digit3':
                            this.selectBlockType('stone');
                            break;
                    }
                });
                
                document.addEventListener('keyup', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = false;
                            break;
                        case 'KeyS':
                            this.moveState.backward = false;
                            break;
                        case 'KeyA':
                            this.moveState.left = false;
                            break;
                        case 'KeyD':
                            this.moveState.right = false;
                            break;
                        case 'Space':
                            this.moveState.jump = false;
                            break;
                    }
                });

                // Mouse click events
                document.addEventListener('mousedown', (event) => {
                    if (!this.controls.isLocked) return;
                    
                    if (event.button === 0) { // Left click
                        this.removeBlockAtPointer();
                    } else if (event.button === 2) { // Right click
                        this.placeBlockAtPointer();
                        event.preventDefault();
                    }
                });

                document.addEventListener('contextmenu', (event) => {
                    event.preventDefault();
                });
                
                window.addEventListener('resize', () => {
                    this.camera.aspect = window.innerWidth / window.innerHeight;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                    
                    // Update postprocessing
                    this.composer.setSize(window.innerWidth, window.innerHeight);
                });

                // Auto-save when leaving page
                window.addEventListener('beforeunload', () => {
                    this.saveWorld();
                });
            }

            selectBlockType(type) {
                this.selectedBlockType = type;
                const blockOptions = document.querySelectorAll('.block-option');
                blockOptions.forEach(option => {
                    option.classList.toggle('selected', option.dataset.type === type);
                });
            }

            saveWorld() {
                const worldData = {
                    blocks: this.blocks.map(block => block.serialize()),
                    playerPosition: {
                        x: this.camera.position.x,
                        y: this.camera.position.y,
                        z: this.camera.position.z
                    }
                };
                localStorage.setItem('minecraftWorld', JSON.stringify(worldData));
                console.log('World saved!');
            }

            loadWorld() {
                const saved = localStorage.getItem('minecraftWorld');
                if (saved) {
                    try {
                        const worldData = JSON.parse(saved);
                        
                        // Clear existing blocks
                        this.blocks.forEach(block => block.removeFromScene(this.scene));
                        this.blocks = [];
                        
                        // Load blocks
                        worldData.blocks.forEach(blockData => {
                            const block = new Block(blockData.x, blockData.y, blockData.z, blockData.type);
                            block.addToScene(this.scene);
                            this.blocks.push(block);
                        });
                        
                        // Load player position
                        if (worldData.playerPosition) {
                            this.camera.position.set(
                                worldData.playerPosition.x,
                                worldData.playerPosition.y,
                                worldData.playerPosition.z
                            );
                        }
                        
                        console.log('World loaded!');
                    } catch (e) {
                        console.error('Error loading world:', e);
                        this.createDefaultWorld();
                    }
                } else {
                    this.createDefaultWorld();
                }
            }

            removeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const blockMesh = intersection.object;
                    
                    const blockIndex = this.blocks.findIndex(block => block.mesh === blockMesh);
                    if (blockIndex !== -1) {
                        const block = this.blocks[blockIndex];
                        block.removeFromScene(this.scene);
                        this.blocks.splice(blockIndex, 1);
                        this.saveWorld();
                        console.log('Block removed!');
                    }
                }
            }

            placeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const face = intersection.face;
                    const blockMesh = intersection.object;
                    
                    const normal = intersection.face.normal.clone();
                    normal.transformDirection(blockMesh.matrixWorld);
                    
                    const hitBlock = this.blocks.find(block => block.mesh === blockMesh);
                    if (!hitBlock) return;
                    
                    const newPosition = new THREE.Vector3(
                        hitBlock.x + Math.round(normal.x),
                        hitBlock.y + Math.round(normal.y),
                        hitBlock.z + Math.round(normal.z)
                    );
                    
                    const positionOccupied = this.blocks.some(block => 
                        block.x === newPosition.x && 
                        block.y === newPosition.y && 
                        block.z === newPosition.z
                    );
                    
                    const playerPosition = this.camera.position.clone();
                    const distanceToPlayer = newPosition.distanceTo(playerPosition);
                    
                    if (!positionOccupied && distanceToPlayer > 1.5) {
                        const newBlock = new Block(newPosition.x, newPosition.y, newPosition.z, this.selectedBlockType);
                        newBlock.addToScene(this.scene);
                        this.blocks.push(newBlock);
                        this.saveWorld();
                        console.log(`Block placed at (${newPosition.x}, ${newPosition.y}, ${newPosition.z})`);
                    }
                }
            }
            
            checkCollision(newPosition) {
                const playerBox = new THREE.Box3(
                    new THREE.Vector3(
                        newPosition.x - this.playerRadius,
                        newPosition.y - this.playerHeight,
                        newPosition.z - this.playerRadius
                    ),
                    new THREE.Vector3(
                        newPosition.x + this.playerRadius,
                        newPosition.y,
                        newPosition.z + this.playerRadius
                    )
                );
                
                for (const block of this.blocks) {
                    const blockBox = block.getBoundingBox();
                    if (playerBox.intersectsBox(blockBox)) {
                        return true;
                    }
                }
                return false;
            }
            
            updateMovement(delta) {
                if (!this.controls.isLocked) return;
                
                const speed = 5.0;
                
                const cameraDirection = new THREE.Vector3();
                this.camera.getWorldDirection(cameraDirection);
                cameraDirection.y = 0;
                cameraDirection.normalize();
                
                const cameraRight = new THREE.Vector3();
                cameraRight.crossVectors(this.camera.up, cameraDirection).normalize();
                
                this.velocity.x = 0;
                this.velocity.z = 0;
                
                if (this.moveState.forward) {
                    this.velocity.add(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.backward) {
                    this.velocity.sub(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.left) {
                    this.velocity.add(cameraRight.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.right) {
                    this.velocity.sub(cameraRight.clone().multiplyScalar(speed * delta));
                }
                
                const oldPosition = this.camera.position.clone();
                const newHorizontalPos = oldPosition.clone().add(this.velocity);
                if (!this.checkCollision(newHorizontalPos)) {
                    this.camera.position.x = newHorizontalPos.x;
                    this.camera.position.z = newHorizontalPos.z;
                }
                
                if (this.moveState.jump && this.onGround) {
                    this.velocity.y = this.jumpForce;
                    this.onGround = false;
                    this.moveState.jump = false;
                }
                
                this.velocity.y += this.gravity * delta;
                
                const newVerticalPos = this.camera.position.clone();
                newVerticalPos.y += this.velocity.y * delta;
                
                const gridSize = 10;
                const isOutsideGrid = Math.abs(this.camera.position.x) > gridSize/2 || 
                                    Math.abs(this.camera.position.z) > gridSize/2;
                
                if (isOutsideGrid) {
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                    }
                    this.onGround = false;
                } else {
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                        this.onGround = false;
                    } else {
                        if (this.velocity.y < 0) {
                            this.onGround = true;
                            this.velocity.y = 0;
                        } else {
                            this.velocity.y = 0;
                        }
                    }
                }
                
                if (this.camera.position.y < -10) {
                    this.camera.position.set(0, 5, 0);
                    this.velocity.set(0, 0, 0);
                }

                // Auto-save every 10 seconds
                if (Math.floor(this.clock.getElapsedTime()) % 10 === 0) {
                    this.saveWorld();
                }
            }
            
            animate() {
                requestAnimationFrame(() => this.animate());
                
                const delta = Math.min(this.clock.getDelta(), 0.1);
                
                if (this.controls.isLocked) {
                    this.updateMovement(delta);
                }
                
                // Use composer instead of renderer
                this.composer.render();
            }
        }

        // Start the game
        new MinecraftGame();
    </script>
</body>
</html>
```

### escena amplia

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Minecraft Clone</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial; }
        canvas { display: block; }
        #crosshair {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 20px;
            height: 20px;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }
        #crosshair::before, #crosshair::after {
            content: '';
            position: absolute;
            background: white;
        }
        #crosshair::before {
            width: 2px;
            height: 20px;
            left: 50%;
            transform: translateX(-50%);
        }
        #crosshair::after {
            width: 20px;
            height: 2px;
            top: 50%;
            transform: translateY(-50%);
        }
        #ui {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 10px;
            border-radius: 5px;
            pointer-events: none;
        }
        #block-selector {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.7);
            padding: 10px;
            border-radius: 5px;
            display: flex;
            gap: 10px;
        }
        .block-option {
            width: 40px;
            height: 40px;
            border: 2px solid transparent;
            border-radius: 3px;
            cursor: pointer;
            pointer-events: auto;
        }
        .block-option.selected {
            border-color: white;
        }
        #reset-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(255,0,0,0.7);
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            pointer-events: auto;
        }
        #reset-btn:hover {
            background: rgba(255,0,0,0.9);
        }
    </style>
</head>
<body>
    <div id="crosshair"></div>
    <div id="ui">
        <div>WASD: Move | Mouse: Look</div>
        <div>Space: Jump | LClick: Remove | RClick: Place</div>
        <div>1,2,3: Select Block Type | World auto-saves</div>
    </div>
    <div id="block-selector">
        <div class="block-option selected" data-type="grass" style="background: #4CAF50;"></div>
        <div class="block-option" data-type="dirt" style="background: #795548;"></div>
        <div class="block-option" data-type="stone" style="background: #9E9E9E;"></div>
    </div>
    <button id="reset-btn">Reset World</button>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>
    
    <!-- Postprocessing Dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/SSAOShader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/SAOShader.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/SSAOPass.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/math/SimplexNoise.js"></script>

    <script>
        // Block class
        class Block {
            constructor(x, y, z, type = 'grass') {
                this.x = x;
                this.y = y;
                this.z = z;
                this.type = type;
                this.mesh = null;
                
                this.createMesh();
            }
            
            createMesh() {
                const geometry = new THREE.BoxGeometry(1, 1, 1);
                
                const colors = {
                    'grass': 0x4CAF50,
                    'dirt': 0x795548,
                    'stone': 0x9E9E9E
                };

                // Create canvas for texture
                const canvas = document.createElement('canvas');
                canvas.width = 64;
                canvas.height = 64;
                const context = canvas.getContext('2d');

                // Base color
                const color = colors[this.type] || 0x4CAF50;
                const r = (color >> 16) & 255;
                const g = (color >> 8) & 255;
                const b = color & 255;

                // Fill with base color
                context.fillStyle = `rgb(${r}, ${g}, ${b})`;
                context.fillRect(0, 0, 64, 64);

                // Add texture pattern (simulated noise/pattern)
                context.globalAlpha = 0.3;
                for (let i = 0; i < 200; i++) {
                    const x = Math.random() * 64;
                    const y = Math.random() * 64;
                    const size = Math.random() * 3 + 1;
                    const brightness = Math.random() * 50 - 25;
                    
                    context.fillStyle = `rgb(${Math.max(0, Math.min(255, r + brightness))}, 
                                            ${Math.max(0, Math.min(255, g + brightness))}, 
                                            ${Math.max(0, Math.min(255, b + brightness))})`;
                    context.fillRect(x, y, size, size);
                }

                // Create texture from canvas
                const texture = new THREE.CanvasTexture(canvas);
                texture.wrapS = THREE.RepeatWrapping;
                texture.wrapT = THREE.RepeatWrapping;
                texture.repeat.set(1, 1);
                
                texture.magFilter = THREE.NearestFilter;
                texture.minFilter = THREE.NearestFilter;
                texture.generateMipmaps = false;

                const material = new THREE.MeshPhongMaterial({ 
                    map: texture,
                    color: new THREE.Color(color)
                });
                
                this.mesh = new THREE.Mesh(geometry, material);
                this.mesh.position.set(this.x, this.y, this.z);
                
                // Enable shadows
                this.mesh.castShadow = true;
                this.mesh.receiveShadow = true;
            }
            
            addToScene(scene) {
                if (this.mesh) {
                    scene.add(this.mesh);
                }
            }
            
            removeFromScene(scene) {
                if (this.mesh) {
                    scene.remove(this.mesh);
                }
            }
            
            getBoundingBox() {
                return new THREE.Box3().setFromObject(this.mesh);
            }

            serialize() {
                return {
                    x: this.x,
                    y: this.y,
                    z: this.z,
                    type: this.type
                };
            }
        }

        // Game class
        class MinecraftGame {
            constructor() {
                this.scene = new THREE.Scene();
                this.scene.background = new THREE.Color(0x87CEEB);
                
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                this.camera.position.set(0, 2, 5);
                
                this.renderer = new THREE.WebGLRenderer({ antialias: true });
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                this.renderer.shadowMap.enabled = true;
                this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
                document.body.appendChild(this.renderer.domElement);
                
                // Postprocessing setup
                this.setupPostProcessing();
                
                this.controls = null;
                this.blocks = [];
                this.moveState = { forward: false, backward: false, left: false, right: false, jump: false };
                this.velocity = new THREE.Vector3();
                
                // Block selection
                this.selectedBlockType = 'grass';
                
                // Physics properties
                this.onGround = false;
                this.gravity = -20;
                this.jumpForce = 8;
                this.playerHeight = 1.8;
                this.playerRadius = 0.3;
                
                // Raycasting
                this.raycaster = new THREE.Raycaster();
                this.raycaster.far = 10;
                
                this.setupLights();
                this.setupControls();
                this.setupEventListeners();
                this.setupUI();
                
                // Load saved world or create default
                this.loadWorld();
                
                this.clock = new THREE.Clock();
                this.animate();
            }
            
            setupPostProcessing() {
                // Create effect composer
                this.composer = new THREE.EffectComposer(this.renderer);
                
                // Add render pass
                const renderPass = new THREE.RenderPass(this.scene, this.camera);
                this.composer.addPass(renderPass);
                
                // Add SSAO pass
                this.ssaoPass = new THREE.SSAOPass(this.scene, this.camera, window.innerWidth, window.innerHeight);
                this.ssaoPass.kernelRadius = 16;
                this.ssaoPass.minDistance = 0.005;
                this.ssaoPass.maxDistance = 0.1;
                this.ssaoPass.output = THREE.SSAOPass.OUTPUT.Default;
                
                // Adjust SSAO intensity for better visibility
                this.ssaoPass.kernelSize = 32;
                this.ssaoPass.kernelRadius = 32;
                
                this.composer.addPass(this.ssaoPass);
            }
            
            setupLights() {
                const ambientLight = new THREE.AmbientLight(0x404040, 2);
                this.scene.add(ambientLight);
                
                const directionalLight = new THREE.DirectionalLight(0xffffff, 2);
                directionalLight.position.set(50, 50, 50);
                directionalLight.castShadow = true;
                
                // Shadow properties
                directionalLight.shadow.mapSize.width = 2048;
                directionalLight.shadow.mapSize.height = 2048;
                directionalLight.shadow.camera.near = 0.5;
                directionalLight.shadow.camera.far = 500;
                directionalLight.shadow.camera.left = -50;
                directionalLight.shadow.camera.right = 50;
                directionalLight.shadow.camera.top = 50;
                directionalLight.shadow.camera.bottom = -50;
                
                this.scene.add(directionalLight);
            }
            
            createDefaultWorld() {
                // Clear existing blocks
                this.blocks.forEach(block => block.removeFromScene(this.scene));
                this.blocks = [];
                
                const gridSize = 100;
                
                // Create floor
                for (let x = -gridSize/2; x < gridSize/2; x++) {
                    for (let z = -gridSize/2; z < gridSize/2; z++) {
                        let type = 'grass';
                        if (Math.random() > 0.8) type = 'dirt';
                        if (Math.random() > 0.95) type = 'stone';
                        
                        const block = new Block(x, -0.5, z, type);
                        block.addToScene(this.scene);
                        this.blocks.push(block);
                    }
                }
                
                // Add some raised blocks
                for (let i = 0; i < 5; i++) {
                    const x = Math.floor(Math.random() * 8 - 4);
                    const z = Math.floor(Math.random() * 8 - 4);
                    const block = new Block(x, 0.5, z, 'stone');
                    block.addToScene(this.scene);
                    this.blocks.push(block);
                }
                
                this.saveWorld();
            }
            
            setupControls() {
                this.controls = new THREE.PointerLockControls(this.camera, document.body);
                
                const instructions = document.createElement('div');
                instructions.style.cssText = `
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    font-family: Arial;
                `;
                instructions.innerHTML = `
                    <h2>Minecraft Clone</h2>
                    <p>Click to play</p>
                    <p>WASD: Move | Mouse: Look around</p>
                    <p>Space: Jump | Left Click: Remove | Right Click: Place</p>
                    <p>1,2,3: Select Block Type | World auto-saves</p>
                `;
                document.body.appendChild(instructions);
                
                const startGame = () => {
                    this.controls.lock();
                    instructions.style.display = 'none';
                };
                
                document.body.addEventListener('click', startGame);
                
                this.controls.addEventListener('lock', () => {
                    instructions.style.display = 'none';
                });
                
                this.controls.addEventListener('unlock', () => {
                    instructions.style.display = 'block';
                });
            }
            
            setupUI() {
                // Block selector
                const blockOptions = document.querySelectorAll('.block-option');
                blockOptions.forEach(option => {
                    option.addEventListener('click', () => {
                        blockOptions.forEach(opt => opt.classList.remove('selected'));
                        option.classList.add('selected');
                        this.selectedBlockType = option.dataset.type;
                    });
                });

                // Reset button
                document.getElementById('reset-btn').addEventListener('click', () => {
                    if (confirm('Are you sure you want to reset the world?')) {
                        this.createDefaultWorld();
                    }
                });
            }
            
            setupEventListeners() {
                document.addEventListener('keydown', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = true;
                            break;
                        case 'KeyS':
                            this.moveState.backward = true;
                            break;
                        case 'KeyA':
                            this.moveState.left = true;
                            break;
                        case 'KeyD':
                            this.moveState.right = true;
                            break;
                        case 'Space':
                            if (this.onGround) {
                                this.moveState.jump = true;
                            }
                            event.preventDefault();
                            break;
                        case 'Digit1':
                            this.selectBlockType('grass');
                            break;
                        case 'Digit2':
                            this.selectBlockType('dirt');
                            break;
                        case 'Digit3':
                            this.selectBlockType('stone');
                            break;
                    }
                });
                
                document.addEventListener('keyup', (event) => {
                    switch (event.code) {
                        case 'KeyW':
                            this.moveState.forward = false;
                            break;
                        case 'KeyS':
                            this.moveState.backward = false;
                            break;
                        case 'KeyA':
                            this.moveState.left = false;
                            break;
                        case 'KeyD':
                            this.moveState.right = false;
                            break;
                        case 'Space':
                            this.moveState.jump = false;
                            break;
                    }
                });

                // Mouse click events
                document.addEventListener('mousedown', (event) => {
                    if (!this.controls.isLocked) return;
                    
                    if (event.button === 0) { // Left click
                        this.removeBlockAtPointer();
                    } else if (event.button === 2) { // Right click
                        this.placeBlockAtPointer();
                        event.preventDefault();
                    }
                });

                document.addEventListener('contextmenu', (event) => {
                    event.preventDefault();
                });
                
                window.addEventListener('resize', () => {
                    this.camera.aspect = window.innerWidth / window.innerHeight;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                    
                    // Update postprocessing
                    this.composer.setSize(window.innerWidth, window.innerHeight);
                });

                // Auto-save when leaving page
                window.addEventListener('beforeunload', () => {
                    this.saveWorld();
                });
            }

            selectBlockType(type) {
                this.selectedBlockType = type;
                const blockOptions = document.querySelectorAll('.block-option');
                blockOptions.forEach(option => {
                    option.classList.toggle('selected', option.dataset.type === type);
                });
            }

            saveWorld() {
                const worldData = {
                    blocks: this.blocks.map(block => block.serialize()),
                    playerPosition: {
                        x: this.camera.position.x,
                        y: this.camera.position.y,
                        z: this.camera.position.z
                    }
                };
                localStorage.setItem('minecraftWorld', JSON.stringify(worldData));
                console.log('World saved!');
            }

            loadWorld() {
                const saved = localStorage.getItem('minecraftWorld');
                if (saved) {
                    try {
                        const worldData = JSON.parse(saved);
                        
                        // Clear existing blocks
                        this.blocks.forEach(block => block.removeFromScene(this.scene));
                        this.blocks = [];
                        
                        // Load blocks
                        worldData.blocks.forEach(blockData => {
                            const block = new Block(blockData.x, blockData.y, blockData.z, blockData.type);
                            block.addToScene(this.scene);
                            this.blocks.push(block);
                        });
                        
                        // Load player position
                        if (worldData.playerPosition) {
                            this.camera.position.set(
                                worldData.playerPosition.x,
                                worldData.playerPosition.y,
                                worldData.playerPosition.z
                            );
                        }
                        
                        console.log('World loaded!');
                    } catch (e) {
                        console.error('Error loading world:', e);
                        this.createDefaultWorld();
                    }
                } else {
                    this.createDefaultWorld();
                }
            }

            removeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const blockMesh = intersection.object;
                    
                    const blockIndex = this.blocks.findIndex(block => block.mesh === blockMesh);
                    if (blockIndex !== -1) {
                        const block = this.blocks[blockIndex];
                        block.removeFromScene(this.scene);
                        this.blocks.splice(blockIndex, 1);
                        this.saveWorld();
                        console.log('Block removed!');
                    }
                }
            }

            placeBlockAtPointer() {
                this.raycaster.setFromCamera(new THREE.Vector2(0, 0), this.camera);
                const blockMeshes = this.blocks.map(block => block.mesh);
                const intersects = this.raycaster.intersectObjects(blockMeshes);
                
                if (intersects.length > 0) {
                    const intersection = intersects[0];
                    const face = intersection.face;
                    const blockMesh = intersection.object;
                    
                    const normal = intersection.face.normal.clone();
                    normal.transformDirection(blockMesh.matrixWorld);
                    
                    const hitBlock = this.blocks.find(block => block.mesh === blockMesh);
                    if (!hitBlock) return;
                    
                    const newPosition = new THREE.Vector3(
                        hitBlock.x + Math.round(normal.x),
                        hitBlock.y + Math.round(normal.y),
                        hitBlock.z + Math.round(normal.z)
                    );
                    
                    const positionOccupied = this.blocks.some(block => 
                        block.x === newPosition.x && 
                        block.y === newPosition.y && 
                        block.z === newPosition.z
                    );
                    
                    const playerPosition = this.camera.position.clone();
                    const distanceToPlayer = newPosition.distanceTo(playerPosition);
                    
                    if (!positionOccupied && distanceToPlayer > 1.5) {
                        const newBlock = new Block(newPosition.x, newPosition.y, newPosition.z, this.selectedBlockType);
                        newBlock.addToScene(this.scene);
                        this.blocks.push(newBlock);
                        this.saveWorld();
                        console.log(`Block placed at (${newPosition.x}, ${newPosition.y}, ${newPosition.z})`);
                    }
                }
            }
            
            checkCollision(newPosition) {
                const playerBox = new THREE.Box3(
                    new THREE.Vector3(
                        newPosition.x - this.playerRadius,
                        newPosition.y - this.playerHeight,
                        newPosition.z - this.playerRadius
                    ),
                    new THREE.Vector3(
                        newPosition.x + this.playerRadius,
                        newPosition.y,
                        newPosition.z + this.playerRadius
                    )
                );
                
                for (const block of this.blocks) {
                    const blockBox = block.getBoundingBox();
                    if (playerBox.intersectsBox(blockBox)) {
                        return true;
                    }
                }
                return false;
            }
            
            updateMovement(delta) {
                if (!this.controls.isLocked) return;
                
                const speed = 5.0;
                
                const cameraDirection = new THREE.Vector3();
                this.camera.getWorldDirection(cameraDirection);
                cameraDirection.y = 0;
                cameraDirection.normalize();
                
                const cameraRight = new THREE.Vector3();
                cameraRight.crossVectors(this.camera.up, cameraDirection).normalize();
                
                this.velocity.x = 0;
                this.velocity.z = 0;
                
                if (this.moveState.forward) {
                    this.velocity.add(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.backward) {
                    this.velocity.sub(cameraDirection.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.left) {
                    this.velocity.add(cameraRight.clone().multiplyScalar(speed * delta));
                }
                if (this.moveState.right) {
                    this.velocity.sub(cameraRight.clone().multiplyScalar(speed * delta));
                }
                
                const oldPosition = this.camera.position.clone();
                const newHorizontalPos = oldPosition.clone().add(this.velocity);
                if (!this.checkCollision(newHorizontalPos)) {
                    this.camera.position.x = newHorizontalPos.x;
                    this.camera.position.z = newHorizontalPos.z;
                }
                
                if (this.moveState.jump && this.onGround) {
                    this.velocity.y = this.jumpForce;
                    this.onGround = false;
                    this.moveState.jump = false;
                }
                
                this.velocity.y += this.gravity * delta;
                
                const newVerticalPos = this.camera.position.clone();
                newVerticalPos.y += this.velocity.y * delta;
                
                const gridSize = 10;
                const isOutsideGrid = Math.abs(this.camera.position.x) > gridSize/2 || 
                                    Math.abs(this.camera.position.z) > gridSize/2;
                
                if (isOutsideGrid) {
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                    }
                    this.onGround = false;
                } else {
                    if (!this.checkCollision(newVerticalPos)) {
                        this.camera.position.y = newVerticalPos.y;
                        this.onGround = false;
                    } else {
                        if (this.velocity.y < 0) {
                            this.onGround = true;
                            this.velocity.y = 0;
                        } else {
                            this.velocity.y = 0;
                        }
                    }
                }
                
                if (this.camera.position.y < -10) {
                    this.camera.position.set(0, 5, 0);
                    this.velocity.set(0, 0, 0);
                }

                // Auto-save every 10 seconds
                if (Math.floor(this.clock.getElapsedTime()) % 10 === 0) {
                    this.saveWorld();
                }
            }
            
            animate() {
                requestAnimationFrame(() => this.animate());
                
                const delta = Math.min(this.clock.getDelta(), 0.1);
                
                if (this.controls.isLocked) {
                    this.updateMovement(delta);
                }
                
                // Use composer instead of renderer
                this.composer.render();
            }
        }

        // Start the game
        new MinecraftGame();
    </script>
</body>
</html>
```

### bloques

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Minecraft Clone — Chunks + Instancing + SSAO</title>
  <style>
    html,body { margin:0; height:100%; overflow:hidden; font-family: system-ui, Arial; background:#000; }
    #crosshair {
      position:absolute; top:50%; left:50%; width:20px; height:20px; transform:translate(-50%,-50%); pointer-events:none;
    }
    #crosshair::before, #crosshair::after {
      content:""; position:absolute; background:white;
    }
    #crosshair::before { width:2px; height:20px; left:50%; transform:translateX(-50%); }
    #crosshair::after  { width:20px; height:2px; top:50%; transform:translateY(-50%); }
    #ui {
      position:absolute; top:10px; left:10px; background:rgba(0,0,0,.6); color:#fff; padding:10px 12px; border-radius:8px; font-size:14px; pointer-events:none;
    }
    #block-selector {
      position:absolute; bottom:10px; left:50%; transform:translateX(-50%);
      background:rgba(0,0,0,.6); padding:8px; border-radius:8px; display:flex; gap:8px;
    }
    .block-option { width:36px; height:36px; border:2px solid transparent; border-radius:4px; cursor:pointer; pointer-events:auto; }
    .block-option.selected { border-color:#fff; }
    #reset-btn {
      position:absolute; top:10px; right:10px; background:rgba(255,0,0,.7); color:#fff; border:none; padding:10px 12px; border-radius:8px; cursor:pointer; pointer-events:auto;
    }
    #reset-btn:hover { background:rgba(255,0,0,.9); }
    #overlay {
      position:absolute; inset:0; display:flex; align-items:center; justify-content:center; background:rgba(0,0,0,.7); color:#fff;
    }
    #overlay .card {
      max-width:520px; padding:24px; border-radius:12px; background:rgba(20,20,20,.9); text-align:center; line-height:1.5;
      box-shadow:0 10px 30px rgba(0,0,0,.5);
    }
    #overlay h1 { margin:0 0 8px; font-size:24px; }
    #overlay p { margin:4px 0; opacity:.9; }
  </style>
</head>
<body>
  <div id="crosshair"></div>
  <div id="ui">
    <div><b>WASD</b> move • <b>Mouse</b> look</div>
    <div><b>Space</b> jump • <b>LClick</b> remove • <b>RClick</b> place</div>
    <div><b>1/2/3</b> block type • <b>R</b> respawn • <b>O</b> SSAO • <b>P</b> SSAO scale • Auto-save</div>
  </div>
  <div id="block-selector">
    <div class="block-option selected" data-type="grass" style="background:#4CAF50"></div>
    <div class="block-option" data-type="dirt"  style="background:#795548"></div>
    <div class="block-option" data-type="stone" style="background:#9E9E9E"></div>
  </div>
  <button id="reset-btn">Reset World</button>

  <div id="overlay">
    <div class="card">
      <h1>Minecraft Clone — Chunks + Instancing + SSAO</h1>
      <p>Click to start • Mouse to look</p>
      <p>WASD move • Space jump • LClick remove • RClick place</p>
      <p>1/2/3 block type • O toggle SSAO • P SSAO quality • Auto-saves</p>
    </div>
  </div>

 <!-- Core -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.min.js"></script>

<!-- Post-processing deps (order matters) -->
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/CopyShader.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/shaders/SSAOShader.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/math/SimplexNoise.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/EffectComposer.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/RenderPass.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/ShaderPass.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/postprocessing/SSAOPass.js"></script>



  <script>
  // ----------------- Config -----------------
  const CONFIG = {
    CHUNK_SIZE: 16,
    CHUNK_HEIGHT: 16,
    WORLD_SIZE_CHUNKS: 8,        // 8x8 chunks → 128x128 world
    PLAYER: {
      HEIGHT: 1.8,
      RADIUS: 0.3,
      SPEED: 5.0,
      JUMP: 8.0,
      GRAVITY: -20.0
    },
    CULLING_RADIUS: 70,          // blocks
    SHADOW_RADIUS: 16,           // blocks
    SAVE_KEY: 'voxelWorldChunks_v3',
    MAX_INSTANCES_PER_CHUNK_PER_TYPE: 4096
  };

  const BLOCK_TYPES = ['grass','dirt','stone'];
  const COLORS = { grass: 0x4CAF50, dirt: 0x795548, stone: 0x9E9E9E };

  // ----------------- Utils -----------------
  const key = (x,y,z)=> `${x}|${y}|${z}`;
  const chunkKey = (cx,cy,cz)=> `${cx}|${cy}|${cz}`;
  const floorDiv = (n, d) => Math.floor(n / d);
  const clamp = (v,min,max)=> Math.max(min, Math.min(max,v));

  // Shared resources
  const SHARED = {
    geometry: new THREE.BoxGeometry(1,1,1),
    materials: {},
    textures: {}
  };
  function makeCanvasTexture(hex) {
    if (SHARED.textures[hex]) return SHARED.textures[hex];
    const r=(hex>>16)&255, g=(hex>>8)&255, b=hex&255;
    const c = document.createElement('canvas'); c.width = 64; c.height = 64;
    const ctx = c.getContext('2d');
    ctx.fillStyle = `rgb(${r},${g},${b})`; ctx.fillRect(0,0,64,64);
    ctx.globalAlpha = 0.3;
    for (let i=0;i<200;i++){
      const x=Math.random()*64, y=Math.random()*64, s=Math.random()*3+1;
      const br = Math.random()*50-25;
      ctx.fillStyle = `rgb(${clamp(r+br,0,255)},${clamp(g+br,0,255)},${clamp(b+br,0,255)})`;
      ctx.fillRect(x,y,s,s);
    }
    const tex = new THREE.CanvasTexture(c);
    tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
    tex.magFilter = tex.minFilter = THREE.NearestFilter;
    tex.generateMipmaps = false;
    SHARED.textures[hex] = tex;
    return tex;
  }
  function getMaterial(type){
    if (SHARED.materials[type]) return SHARED.materials[type];
    const color = COLORS[type] || COLORS.grass;
    const mat = new THREE.MeshPhongMaterial({ color, map: makeCanvasTexture(color) });
    SHARED.materials[type] = mat;
    return mat;
  }

  // ----------------- Chunk -----------------
  class Chunk {
    constructor(cx, cy, cz, scene){
      this.cx = cx; this.cy = cy; this.cz = cz;
      this.scene = scene;
      this.size = CONFIG.CHUNK_SIZE;
      this.height = CONFIG.CHUNK_HEIGHT;

      this.voxels = new Map();
      this.meshByType = new Map(); // type -> { mesh, instanceCount, idToPos[], posToId(Map) }
      for (const type of BLOCK_TYPES){
        const mat = getMaterial(type);
        const mesh = new THREE.InstancedMesh(
          SHARED.geometry,
          mat,
          CONFIG.MAX_INSTANCES_PER_CHUNK_PER_TYPE
        );
        mesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
        mesh.castShadow = false;
        mesh.receiveShadow = false;
        mesh.visible = false;
        mesh.frustumCulled = false;
        mesh.count = 0;
        this.scene.add(mesh);
        this.meshByType.set(type, {
          mesh, instanceCount: 0,
          idToPos: [],
          posToId: new Map()
        });
      }

      const min = new THREE.Vector3(
        cx*this.size, cy*this.height, cz*this.size
      );
      const max = new THREE.Vector3(
        (cx+1)*this.size, (cy+1)*this.height, (cz+1)*this.size
      );
      this.aabb = new THREE.Box3(min, max);
    }

    addBlock(x,y,z,type){
      const k = key(x,y,z);
      if (this.voxels.has(k)) return false;
      this.voxels.set(k, type);
      const pack = this.meshByType.get(type);
      const index = pack.instanceCount++;
      const m = new THREE.Matrix4().makeTranslation(x+0.5, y+0.5, z+0.5);
      pack.mesh.setMatrixAt(index, m);
      pack.mesh.instanceMatrix.needsUpdate = true;
      pack.idToPos[index] = {x,y,z};
      pack.posToId.set(k, index);
      pack.mesh.count = pack.instanceCount;
      return true;
    }

    removeBlock(x,y,z){
      const k = key(x,y,z);
      const type = this.voxels.get(k);
      if (!type) return false;
      const pack = this.meshByType.get(type);
      const index = pack.posToId.get(k);
      if (index === undefined) return false;

      const lastIndex = pack.instanceCount - 1;
      if (index !== lastIndex){
        const tmp = new THREE.Matrix4();
        pack.mesh.getMatrixAt(lastIndex, tmp);
        pack.mesh.setMatrixAt(index, tmp);
        const movedPos = pack.idToPos[lastIndex];
        pack.idToPos[index] = movedPos;
        pack.posToId.set(key(movedPos.x, movedPos.y, movedPos.z), index);
      }
      pack.instanceCount--;
      pack.mesh.count = pack.instanceCount;
      pack.idToPos.pop();
      pack.posToId.delete(k);
      pack.mesh.instanceMatrix.needsUpdate = true;
      this.voxels.delete(k);
      return true;
    }

    setVisible(v){
      for (const [,pack] of this.meshByType){
        pack.mesh.visible = v && pack.instanceCount>0;
      }
    }
    setShadowsEnabled(near){
      for (const [,pack] of this.meshByType){
        pack.mesh.castShadow = near;
        pack.mesh.receiveShadow = near;
      }
    }

    raycast(raycaster, intersects){
      for (const [,pack] of this.meshByType){
        if (!pack.mesh.visible || pack.instanceCount===0) continue;
        pack.mesh.raycast(raycaster, intersects);
      }
    }

    instanceInfo(object, instanceId){
      for (const [type, pack] of this.meshByType){
        if (pack.mesh === object){
          const pos = pack.idToPos[instanceId];
          if (!pos) return null;
          return { type, ...pos };
        }
      }
      return null;
    }

    serialize(){
      const list = [];
      for (const [k, t] of this.voxels){
        const [x,y,z] = k.split('|').map(Number);
        list.push([x,y,z,t]);
      }
      return { cx:this.cx, cy:this.cy, cz:this.cz, voxels:list };
    }

    static deserialize(data, scene){
      const ch = new Chunk(data.cx, data.cy, data.cz, scene);
      for (const [x,y,z,t] of data.voxels){
        ch.addBlock(x,y,z,t);
      }
      return ch;
    }
  }

  // ----------------- World -----------------
  class World {
    constructor(scene){
      this.scene = scene;
      this.chunks = new Map();
      this.voxelIndex = new Map();
    }

    getChunkCoords(x,y,z){
      const cs = CONFIG.CHUNK_SIZE, ch = CONFIG.CHUNK_HEIGHT;
      return {
        cx: floorDiv(x, cs),
        cy: floorDiv(y, ch),
        cz: floorDiv(z, cs)
      };
    }
    getChunk(cx,cy,cz, createIfMissing=false){
      const ck = chunkKey(cx,cy,cz);
      let ch = this.chunks.get(ck);
      if (!ch && createIfMissing){
        ch = new Chunk(cx,cy,cz,this.scene);
        this.chunks.set(ck,ch);
      }
      return ch;
    }

    hasBlock(x,y,z){ return this.voxelIndex.has(key(x,y,z)); }

    addBlock(x,y,z,type){
      const {cx,cy,cz} = this.getChunkCoords(x,y,z);
      const ch = this.getChunk(cx,cy,cz,true);
      if (ch.addBlock(x,y,z,type)){
        this.voxelIndex.set(key(x,y,z), { type, cx,cy,cz });
        return true;
      }
      return false;
    }

    removeBlock(x,y,z){
      const v = this.voxelIndex.get(key(x,y,z));
      if (!v) return false;
      const ch = this.getChunk(v.cx, v.cy, v.cz, false);
      if (!ch) return false;
      if (ch.removeBlock(x,y,z)){
        this.voxelIndex.delete(key(x,y,z));
        return true;
      }
      return false;
    }

    neighborsOfAABB(min, max){
      const res = [];
      for (let x=Math.floor(min.x)-1; x<=Math.floor(max.x)+1; x++){
        for (let y=Math.floor(min.y)-1; y<=Math.floor(max.y)+1; y++){
          for (let z=Math.floor(min.z)-1; z<=Math.floor(max.z)+1; z++){
            const v = this.voxelIndex.get(key(x,y,z));
            if (v) res.push({x,y,z});
          }
        }
      }
      return res;
    }

    setChunksVisibilityAndShadows(cameraPos){
      const r2 = CONFIG.CULLING_RADIUS*CONFIG.CULLING_RADIUS;
      const s2 = CONFIG.SHADOW_RADIUS*CONFIG.SHADOW_RADIUS;
      for (const [,ch] of this.chunks){
        const cx = (ch.cx+0.5)*ch.size;
        const cz = (ch.cz+0.5)*ch.size;
        const dx = cx - cameraPos.x;
        const dz = cz - cameraPos.z;
        const d2 = dx*dx + dz*dz;
        const visible = d2 <= r2;
        const nearShadow = d2 <= s2;
        ch.setVisible(visible);
        ch.setShadowsEnabled(nearShadow);
      }
    }

    raycast(raycaster){
      const intersects = [];
      for (const [,ch] of this.chunks){
        ch.raycast(raycaster, intersects);
      }
      if (intersects.length === 0) return null;
      intersects.sort((a,b)=> a.distance - b.distance);
      const hit = intersects[0];
      const ch = this.findChunkByMesh(hit.object);
      if (!ch) return null;
      const info = ch.instanceInfo(hit.object, hit.instanceId);
      if (!info) return null;
      return { ...info, point: hit.point, face: hit.face, object: hit.object, chunk: ch };
    }

    findChunkByMesh(mesh){
      for (const [,ch] of this.chunks){
        for (const [,pack] of ch.meshByType){
          if (pack.mesh === mesh) return ch;
        }
      }
      return null;
    }

    serialize(){
      const data = [];
      for (const [,ch] of this.chunks){
        if (ch.voxels.size>0) data.push(ch.serialize());
      }
      return data;
    }
    static deserialize(arr, scene){
      const w = new World(scene);
      for (const chData of arr){
        const ch = Chunk.deserialize(chData, scene);
        w.chunks.set(chunkKey(ch.cx,ch.cy,ch.cz), ch);
        for (const [k,t] of ch.voxels){
          const [x,y,z] = k.split('|').map(Number);
          w.voxelIndex.set(k, { type:t, cx:ch.cx, cy:ch.cy, cz:ch.cz });
        }
      }
      return w;
    }
  }

  // ----------------- Game -----------------
  class Game {
    constructor(){
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0x87CEEB);

      this.camera = new THREE.PerspectiveCamera(75, innerWidth/innerHeight, 0.1, 1000);
      this.camera.position.set(0, 5, 10);

      this.renderer = new THREE.WebGLRenderer({ antialias:false, powerPreference:'high-performance' });
      this.renderer.setSize(innerWidth, innerHeight);
      this.renderer.shadowMap.enabled = true;
      this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
      document.body.appendChild(this.renderer.domElement);

      // SSAO / Composer
      this.useSSAO = true;
      this.ssaoScale = 0.5; // 0.5 = half-res
      this.composer = null;
      this.renderPass = null;
      this.ssaoPass = null;
      this.setupPostFX();

      // Lights
      const amb = new THREE.AmbientLight(0xffffff, 0.8);
      this.scene.add(amb);
      const sun = new THREE.DirectionalLight(0xffffff, 1.8);
      sun.position.set(60, 80, 40);
      sun.castShadow = true;
      sun.shadow.mapSize.set(1024,1024);
      sun.shadow.camera.near = 0.5;
      sun.shadow.camera.far = 300;
      sun.shadow.camera.left = -100;
      sun.shadow.camera.right = 100;
      sun.shadow.camera.top = 100;
      sun.shadow.camera.bottom = -100;
      this.scene.add(sun);

      // Controls
      this.controls = new THREE.PointerLockControls(this.camera, document.body);
      const overlay = document.getElementById('overlay');
      document.body.addEventListener('click', ()=>{
        if (!this.controls.isLocked) this.controls.lock();
      });
      this.controls.addEventListener('lock', ()=> overlay.style.display='none');
      this.controls.addEventListener('unlock', ()=> overlay.style.display='flex');

      // Input
      this.move = { f:false,b:false,l:false,r:false,j:false };
      addEventListener('keydown', e=>{
        if (e.code==='KeyW') this.move.f=true;
        if (e.code==='KeyS') this.move.b=true;
        if (e.code==='KeyA') this.move.l=true;
        if (e.code==='KeyD') this.move.r=true;
        if (e.code==='Space' && this.onGround) this.move.j=true;
        if (e.code==='Digit1') this.selectBlock('grass');
        if (e.code==='Digit2') this.selectBlock('dirt');
        if (e.code==='Digit3') this.selectBlock('stone');
        if (e.code==='KeyR') this.respawn();

        // SSAO controls
        if (e.code==='KeyO'){ // toggle SSAO
          this.useSSAO = !this.useSSAO;
        }
        if (e.code==='KeyP'){ // cycle quality
          const levels = [1.0, 0.5, 0.33];
          const i = levels.indexOf(this.ssaoScale);
          this.ssaoScale = levels[(i+1) % levels.length];
          if (this.ssaoPass){
            const w = Math.max(1, Math.floor(innerWidth  * this.ssaoScale));
            const h = Math.max(1, Math.floor(innerHeight * this.ssaoScale));
            this.ssaoPass.setSize(w, h);
          }
        }
      });
      addEventListener('keyup', e=>{
        if (e.code==='KeyW') this.move.f=false;
        if (e.code==='KeyS') this.move.b=false;
        if (e.code==='KeyA') this.move.l=false;
        if (e.code==='KeyD') this.move.r=false;
        if (e.code==='Space') this.move.j=false;
      });

      // UI selector
      this.selectedType = 'grass';
      const opts = document.querySelectorAll('.block-option');
      opts.forEach(o=>o.addEventListener('click', ()=>{
        opts.forEach(p=>p.classList.remove('selected'));
        o.classList.add('selected');
        this.selectedType = o.dataset.type;
      }));
      document.getElementById('reset-btn').addEventListener('click', ()=>{
        if (confirm('Reset world?')){
          localStorage.removeItem(CONFIG.SAVE_KEY);
          location.reload();
        }
      });

      // Mouse actions
      addEventListener('contextmenu', e=> e.preventDefault());
      addEventListener('mousedown', (e)=>{
        if (!this.controls.isLocked) return;
        if (e.button===0) this.removeBlockAtPointer();
        if (e.button===2) this.placeBlockAtPointer();
      });

      // Resize
      addEventListener('resize', ()=>{
        this.camera.aspect = innerWidth/innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(innerWidth, innerHeight);
        if (this.composer){
          this.composer.setSize(innerWidth, innerHeight);
          const w = Math.max(1, Math.floor(innerWidth  * this.ssaoScale));
          const h = Math.max(1, Math.floor(innerHeight * this.ssaoScale));
          this.ssaoPass.setSize(w, h);
        }
      });

      // World
      this.world = null;

      // Physics
      this.velocity = new THREE.Vector3();
      this.onGround = false;

      // Raycaster
      this.raycaster = new THREE.Raycaster();
      this.raycaster.far = 10;

      // Clock
      this.clock = new THREE.Clock();

      // Load or create
      this.loadOrCreateWorld();

      // Autosave timer
      this.lastAutoSave = 0;

      this.animate();
    }

    setupPostFX(){
      this.composer = new THREE.EffectComposer(this.renderer);
      this.renderPass = new THREE.RenderPass(this.scene, this.camera);
      this.composer.addPass(this.renderPass);

      const w = Math.max(1, Math.floor(innerWidth  * this.ssaoScale));
      const h = Math.max(1, Math.floor(innerHeight * this.ssaoScale));
      this.ssaoPass = new THREE.SSAOPass(this.scene, this.camera, w, h);
      // tuned for voxel look
      this.ssaoPass.kernelRadius = 5;   // try 8–12
      this.ssaoPass.minDistance  = 0.005;
      this.ssaoPass.maxDistance  = 0.12;

      this.composer.addPass(this.ssaoPass);
    }

    selectBlock(t){ this.selectedType = t; }

    // --------- World generation ----------
    createDefaultWorld(){
      this.world = new World(this.scene);
      const sizeChunks = CONFIG.WORLD_SIZE_CHUNKS;
      const CS = CONFIG.CHUNK_SIZE;
      const worldSize = sizeChunks*CS;

      function noise2(x,z){
        return Math.sin(x*0.07)*0.7 + Math.cos(z*0.09)*0.5 + Math.sin((x+z)*0.03)*0.6;
      }

      for (let x=0; x<worldSize; x++){
        for (let z=0; z<worldSize; z++){
          const h = Math.floor(2 + Math.max(0, noise2(x,z)*2)); // height ≈2..5
          for (let y=0; y<h; y++){
            let type = (y===h-1) ? 'grass' : (y>=h-3 ? 'dirt' : 'stone');
            this.world.addBlock(x, y-1, z, type);
          }
        }
      }
      for (let i=0;i<80;i++){
        const x = Math.floor(Math.random()*worldSize);
        const z = Math.floor(Math.random()*worldSize);
        const h = 1+Math.floor(Math.random()*4);
        for (let y=0;y<h;y++){
          this.world.addBlock(x, y+2, z, 'stone');
        }
      }
    }

    saveWorld(){
      if (!this.world) return;
      const data = {
        chunks: this.world.serialize(),
        player: { x:this.camera.position.x, y:this.camera.position.y, z:this.camera.position.z }
      };
      localStorage.setItem(CONFIG.SAVE_KEY, JSON.stringify(data));
    }

    loadOrCreateWorld(){
      const raw = localStorage.getItem(CONFIG.SAVE_KEY);
      if (raw){
        try{
          const parsed = JSON.parse(raw);
          this.world = World.deserialize(parsed.chunks || [], this.scene);
          if (parsed.player){
            this.camera.position.set(parsed.player.x, parsed.player.y, parsed.player.z);
          }
        }catch(e){
          console.warn('Error loading save, creating new world', e);
          this.createDefaultWorld();
        }
      } else {
        this.createDefaultWorld();
      }
    }

    // --------- Interactions ---------
    removeBlockAtPointer(){
      this.raycaster.setFromCamera(new THREE.Vector2(0,0), this.camera);
      const hit = this.world.raycast(this.raycaster);
      if (!hit) return;
      this.world.removeBlock(hit.x, hit.y, hit.z);
    }

    placeBlockAtPointer(){
      this.raycaster.setFromCamera(new THREE.Vector2(0,0), this.camera);
      const hit = this.world.raycast(this.raycaster);
      if (!hit) return;
      const n = hit.face.normal.clone();
      n.transformDirection(hit.object.matrixWorld);
      const nx = hit.x + Math.round(n.x);
      const ny = hit.y + Math.round(n.y);
      const nz = hit.z + Math.round(n.z);

      const playerPos = this.camera.position;
      const dist = new THREE.Vector3(nx+0.5, ny+0.5, nz+0.5).distanceTo(playerPos);
      if (dist < 1.5) return;

      if (!this.world.hasBlock(nx,ny,nz)){
        this.world.addBlock(nx,ny,nz,this.selectedType);
      }
    }

    // --------- Collision ---------
    playerAABBAt(pos){
      const r = CONFIG.PLAYER.RADIUS;
      const h = CONFIG.PLAYER.HEIGHT;
      return new THREE.Box3(
        new THREE.Vector3(pos.x - r, pos.y - h, pos.z - r),
        new THREE.Vector3(pos.x + r, pos.y,     pos.z + r)
      );
    }
    collidesAt(pos){
      const aabb = this.playerAABBAt(pos);
      const neighbors = this.world.neighborsOfAABB(aabb.min, aabb.max);
      for (const b of neighbors){
        const bb = new THREE.Box3(
          new THREE.Vector3(b.x, b.y, b.z),
          new THREE.Vector3(b.x+1, b.y+1, b.z+1)
        );
        if (aabb.intersectsBox(bb)) return true;
      }
      return false;
    }

    respawn(){
      this.camera.position.set(0, 8, 0);
      this.velocity.set(0,0,0);
    }

    // --------- Loop ---------
    animate(){
      requestAnimationFrame(()=>this.animate());
      const dt = Math.min(this.clock.getDelta(), 0.05);

      // Movement
      if (this.controls.isLocked){
        const dir = new THREE.Vector3();
        this.camera.getWorldDirection(dir);
        dir.y = 0; dir.normalize();
        const right = new THREE.Vector3().crossVectors(this.camera.up, dir).normalize();

        const speed = CONFIG.PLAYER.SPEED;
        let dx=0, dz=0;
        if (this.move.f) { dx += dir.x; dz += dir.z; }
        if (this.move.b) { dx -= dir.x; dz -= dir.z; }
        if (this.move.l) { dx += right.x; dz += right.z; }
        if (this.move.r) { dx -= right.x; dz -= right.z; }

        const horiz = new THREE.Vector3(dx,0,dz);
        if (horiz.lengthSq()>0) horiz.normalize().multiplyScalar(speed*dt);

        const posH = this.camera.position.clone().add(horiz);
        if (!this.collidesAt(posH)){
          this.camera.position.copy(posH);
        }

        if (this.move.j && this.onGround){
          this.velocity.y = CONFIG.PLAYER.JUMP;
          this.onGround = false;
          this.move.j = false;
        }
        this.velocity.y += CONFIG.PLAYER.GRAVITY * dt;

        const posV = this.camera.position.clone();
        posV.y += this.velocity.y * dt;

        if (!this.collidesAt(posV)){
          this.camera.position.y = posV.y;
          this.onGround = false;
        } else {
          if (this.velocity.y < 0) this.onGround = true;
          this.velocity.y = 0;
        }

        if (this.camera.position.y < -20) this.respawn();
      }

      // Visibility & shadows by radius
      this.world.setChunksVisibilityAndShadows(this.camera.position);

      // Autosave every ~10s
      this.lastAutoSave += dt;
      if (this.lastAutoSave >= 10){
        this.lastAutoSave = 0;
        this.saveWorld();
      }

      // Render path
      if (this.useSSAO && this.composer){
        this.composer.render();
      } else {
        this.renderer.render(this.scene, this.camera);
      }
    }
  }

  // ----------------- Start -----------------
  new Game();
  </script>
</body>
</html>
```

<a id="ejercicio-de-final-de-unidad"></a>
## Ejercicio de final de unidad

### ejercicio

```markdown

```

<a id="examen-final"></a>
## Examen final

### crear tablas

```sql
CREATE DATABASE portafolioceac;

USE portafolioceac;


CREATE TABLE Piezas(
  Identificador INT auto_increment PRIMARY KEY,
  titulo VARCHAR(255),
  descripcion VARCHAR(255),
  imagen VARCHAR(255),
  url VARCHAR(255),
  id_categoria INT
);

CREATE TABLE Categorias(
  Identificador INT auto_increment PRIMARY KEY,
  titulo VARCHAR(255),
  descripcion VARCHAR(255)
);
```

### insertar

```sql
INSERT INTO Categorias VALUES(
  NULL,
  'General',
  'Esta es la categoria general'
);

INSERT INTO Piezas VALUES(
  NULL,
  'Primera pieza',
  'Esta es la descripcion de la primera pieza',
  'josevicente.jpg',
  'https://jocarsa.com',
  1
);
```

### fk

```sql
ALTER TABLE Piezas
ADD CONSTRAINT fk_piezas_categorias
FOREIGN KEY (id_categoria) REFERENCES Categorias(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

### selecciones

```sql
SELECT * FROM Categorias;

SELECT * FROM Piezas;
```

### left join

```sql
SELECT 
* 
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;
```

### ahora creo la vista

```sql
CREATE VIEW piezas_y_categorias AS 
SELECT 
Categorias.titulo AS categoriatitulo,
Categorias.descripcion AS categoriadescripcion,
Piezas.titulo AS piezatitulo,
Piezas.descripcion AS piezadescripcion,
imagen,
url
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;

SELECT * FROM piezas_y_categorias;
```

### usuario

```sql
-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER 
'portafolioceac'@'localhost' 
IDENTIFIED  BY 'portafolioceac';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'portafolioceac'@'localhost';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len

-- quitale todos los limites que tenga
ALTER USER 'portafolioceac'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON portafolioceac.* 
TO 'portafolioceac'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
```


<a id="desarrollo-de-juegos-2d-y-3d"></a>
# Desarrollo de juegos 2D y 3D

<a id="tecnicas-de-programacion-2d3d"></a>
## Técnicas de programación 2D3D

En la subunidad "Técnicas de programación 2D3D", nos sumergimos en los fundamentos necesarios para desarrollar juegos en dos y tres dimensiones. Comenzamos por explorar las técnicas básicas de programación que son esenciales para crear contenido visualmente atractivo e interactivo.

La animación 2D y 3D es un aspecto crucial del desarrollo de juegos, ya que permite la creación de personajes, escenas y objetos dinámicos. En esta sección, aprenderemos cómo implementar animaciones fluidas utilizando técnicas como el uso de frames o sprites para representar movimientos suaves en dos dimensiones, y cómo aplicar transformaciones matemáticas para crear efectos 3D.

Además, es importante entender la arquitectura del juego. Un motor de juegos típicamente consta de componentes como renderizado, física, entrada del usuario y gestión de recursos. Cada uno de estos componentes juega un papel crucial en el funcionamiento global del juego, desde la representación visual hasta la interacción con el usuario.

El estudio de motores de juegos es otro tema central. Existen diversos motores disponibles tanto para desarrollo 2D como 3D, cada uno con sus propias ventajas y limitaciones. Algunos son específicos para plataformas móviles, mientras que otros ofrecen una mayor flexibilidad y control sobre los detalles del juego.

Además de la programación básica, es necesario aprender a manejar fuentes de audio y música en juegos 2D y 3D. La adición de efectos de sonido y música puede mejorar significativamente la experiencia del jugador, creando un ambiente más inmersivo y emocionante.

La iluminación y las cámaras son otros elementos fundamentales para crear escenas atractivas en juegos. Aprender cómo controlar la luz y cómo mover las cámaras permite crear perspectivas interesantes y realistas, añadiendo profundidad y dinamismo a los juegos.

El desarrollo de escenas es una habilidad crucial que involucra la creación de entornos visuales complejos. Desde el diseño de niveles hasta la creación de interfaces de usuario interactivas, cada elemento debe ser cuidadosamente planificado para ofrecer una experiencia fluida y atractiva al jugador.

Finalmente, es importante realizar un análisis exhaustivo del rendimiento del juego. Esto implica medir y optimizar aspectos como la velocidad de renderizado, el uso de memoria y la eficiencia energética para asegurar que el juego funcione bien en una amplia gama de dispositivos.

En conclusión, la subunidad "Técnicas de programación 2D3D" proporciona una sólida base para desarrollar habilidades esenciales en el campo del desarrollo de juegos. A través de un enfoque práctico y teórico, los estudiantes aprenderán a crear contenido visualmente impresionante e interactivo, preparándose para enfrentarse a desafíos más complejos en proyectos futuros.

### entorno 3d

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Parallax Box with Head Tracking</title>
  <script src="https://aframe.io/releases/1.5.0/aframe.min.js"></script>

  <!-- Mediapipe Tasks Vision (FaceLandmarker) -->
  <script src="https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/vision_bundle.js"></script>

  <style>
    body, html {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #000;
    }
    #video {
      position: fixed;
      bottom: 10px;
      right: 10px;
      width: 200px;
      transform: scaleX(-1); /* mirror for natural feeling */
      opacity: 0.4;          /* debug; later set to 0 or remove */
      z-index: 10;
    }
  </style>
</head>
<body>
  <video id="video" autoplay playsinline></video>

  <a-scene>
    <!-- Camera rig so we can move the rig instead of the camera alone -->
    <a-entity id="rig" position="0 0 3">
      <a-entity id="cam" camera look-controls="enabled: false"></a-entity>
    </a-entity>

    <!-- Inside of a box -->
    <a-box position="0 0 -2" depth="0.05" height="4" width="6" color="#222"></a-box> <!-- back wall -->
    <a-box position="0 -2 0" rotation="90 0 0" depth="0.05" height="4" width="6" color="#333"></a-box> <!-- floor -->
    <a-box position="0 2 0" rotation="-90 0 0" depth="0.05" height="4" width="6" color="#333"></a-box> <!-- ceiling -->
    <a-box position="-3 0 0" rotation="0 90 0" depth="0.05" height="4" width="4" color="#444"></a-box> <!-- left -->
    <a-box position="3 0 0" rotation="0 -90 0" depth="0.05" height="4" width="4" color="#444"></a-box> <!-- right -->

    <!-- Some primitives inside -->
    <a-sphere position="-1 0 -1" radius="0.4" color="#FF4444"></a-sphere>
    <a-box position="1 -0.5 -1.5" depth="0.6" height="0.6" width="0.6" color="#44FF44"></a-box>
    <a-cylinder position="0 0.5 -2.5" radius="0.3" height="1" color="#4444FF"></a-cylinder>

    <!-- Light -->
    <a-entity light="type: point; intensity: 1.5" position="0 1 1"></a-entity>
  </a-scene>

  <script type="module">
    import {
      FaceLandmarker,
      FilesetResolver,
      DrawingUtils
    } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0";

    const video = document.getElementById("video");
    let faceLandmarker;
    let running = false;
    let lastVideoTime = -1;

    async function initCamera() {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: 640, height: 480 }
      });
      video.srcObject = stream;
      return new Promise(resolve => {
        video.onloadedmetadata = () => resolve();
      });
    }

    async function initFaceLandmarker() {
      const filesetResolver = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
      );

      faceLandmarker = await FaceLandmarker.createFromOptions(filesetResolver, {
        baseOptions: {
          modelAssetPath:
            "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task"
        },
        runningMode: "VIDEO",
        numFaces: 1
      });
    }

    function getHeadCenterFromLandmarks(landmarks) {
      // landmarks: 3D points in image coords [0..1]
      // We’ll simply average some key points (eyes + nose) as a crude head center.
      const indices = [1, 33, 263,  noseIndex()];
      function noseIndex() { return 1; } // You could look up the correct index if you like.

      let x = 0, y = 0;
      let count = 0;
      for (const i of indices) {
        if (!landmarks[i]) continue;
        x += landmarks[i].x;
        y += landmarks[i].y;
        count++;
      }
      if (!count) return null;
      return { x: x / count, y: y / count }; // still in [0..1]
    }

    function mapHeadToCamera(headCenter, videoWidth, videoHeight) {
      // headCenter.x,y in [0..1]; convert to [-1,1]
      const nx = headCenter.x * 2 - 1;   // left=-1, right=1
      const ny = headCenter.y * 2 - 1;   // top=-1, bottom=1

      // Tunable offsets in scene units
      const maxX = 0.6;
      const maxY = 0.4;
      const baseZ = 3;     // base distance
      const maxZOffset = 0.5;

      // For now, fake Z from how off-center they are (just to get some motion)
      const distanceFromCenter = Math.sqrt(nx*nx + ny*ny); // 0..approx1.4
      const nz = Math.min(distanceFromCenter, 1.0);

      // Map: move rig opposite head movement for window effect
      const camX = -nx * maxX;
      const camY = ny * maxY;
      const camZ = baseZ + nz * maxZOffset;

      return { x: camX, y: camY, z: camZ };
    }

    function smooth(prev, next, factor = 0.15) {
      if (!prev) return next;
      return {
        x: prev.x + (next.x - prev.x) * factor,
        y: prev.y + (next.y - prev.y) * factor,
        z: prev.z + (next.z - prev.z) * factor,
      };
    }

    let smoothedCamPos = null;
    const rigEl = document.getElementById("rig");

    async function processVideoFrame() {
      if (!running) return;

      const nowMs = performance.now();
      const videoTime = video.currentTime;
      if (videoTime === lastVideoTime) {
        requestAnimationFrame(processVideoFrame);
        return;
      }
      lastVideoTime = videoTime;

      const results = faceLandmarker.detectForVideo(video, nowMs);

      if (results.faceLandmarks && results.faceLandmarks.length > 0) {
        const landmarks = results.faceLandmarks[0];
        const center = getHeadCenterFromLandmarks(landmarks);
        if (center) {
          const camPos = mapHeadToCamera(
            center,
            video.videoWidth,
            video.videoHeight
          );
          smoothedCamPos = smooth(smoothedCamPos, camPos);
          rigEl.setAttribute(
            "position",
            `${smoothedCamPos.x} ${smoothedCamPos.y} ${smoothedCamPos.z}`
          );
        }
      }

      requestAnimationFrame(processVideoFrame);
    }

    (async () => {
      await initCamera();
      await initFaceLandmarker();
      running = true;
      processVideoFrame();
    })();
  </script>
</body>
</html>
```

### segunda version

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Parallax Box with Head Tracking</title>

  <!-- A-Frame -->
  <script src="https://aframe.io/releases/1.5.0/aframe.min.js"></script>

  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #000;
    }
    #video {
      position: fixed;
      bottom: 10px;
      right: 10px;
      width: 220px;
      transform: scaleX(-1); /* mirror for natural feeling */
      opacity: 0.4;          /* set to 0 or display:none when you no longer need it */
      z-index: 10;
      border: 2px solid #444;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <!-- Debug webcam preview -->
  <video id="video" autoplay playsinline></video>

  <!-- 3D scene -->
  <a-scene>
    <!-- Camera rig near the "window" of the box -->
    <a-entity id="rig" position="0 0 0.8">
      <a-entity id="cam" camera look-controls="enabled: false"></a-entity>
    </a-entity>

    <!-- Front frame (window) of the box at z = -1 -->
    <a-box position="0 0 -1"
           depth="0.03"
           height="3"
           width="4"
           color="#555"
           material="side:double; metalness:0.2; roughness:0.6">
    </a-box>

    <!-- Box interior (walls, floor, ceiling) -->
    <a-box position="0 0 -5"
           depth="0.05"
           height="3"
           width="4"
           color="#222">
    </a-box> <!-- back wall -->

    <a-box position="0 -1.5 -3"
           rotation="90 0 0"
           depth="0.05"
           height="4"
           width="4"
           color="#333">
    </a-box> <!-- floor -->

    <a-box position="0 1.5 -3"
           rotation="-90 0 0"
           depth="0.05"
           height="4"
           width="4"
           color="#333">
    </a-box> <!-- ceiling -->

    <a-box position="-2 0 -3"
           rotation="0 90 0"
           depth="0.05"
           height="3"
           width="4"
           color="#444">
    </a-box> <!-- left wall -->

    <a-box position="2 0 -3"
           rotation="0 -90 0"
           depth="0.05"
           height="3"
           width="4"
           color="#444">
    </a-box> <!-- right wall -->

    <!-- PRIMITIVES: multiple rows and depths for strong parallax -->

    <!-- Row 1 (near) -->
    <a-sphere   position="-1.2 -0.4 -2.0" radius="0.25" color="#ff4444"></a-sphere>
    <a-box      position=" 0.0 -0.6 -2.5" depth="0.5" height="0.5" width="0.5" color="#44ff44"></a-box>
    <a-cylinder position=" 1.2 -0.4 -2.2" radius="0.2" height="0.7" color="#4444ff"></a-cylinder>

    <!-- Row 2 (mid) -->
    <a-torus-knot position="-0.8 0.4 -3.0" radius="0.25" radius-tubular="0.06" color="#ffcc00"></a-torus-knot>
    <a-octahedron position=" 0.6 0.2 -3.3" radius="0.2" color="#00ffcc"></a-octahedron>
    <a-dodecahedron position=" 1.4 0.5 -3.8" radius="0.25" color="#ff00aa"></a-dodecahedron>

    <!-- Row 3 (farther) -->
    <a-sphere   position="-1.5 0.9 -4.2" radius="0.18" color="#ffaa88"></a-sphere>
    <a-box      position="-0.2 1.0 -4.5" depth="0.4" height="0.4" width="0.4" color="#88ffaa"></a-box>
    <a-cylinder position=" 0.9 1.1 -4.8" radius="0.18" height="0.6" color="#88aaff"></a-cylinder>
    <a-torus    position=" 0.0 -1.0 -3.8" radius="0.4" radius-tubular="0.07" color="#ff8888"></a-torus>

    <!-- A path of small spheres going deeper into the box -->
    <a-sphere position="-1.5 -1.0 -2.3" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position="-1.0 -0.9 -2.7" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position="-0.5 -0.8 -3.1" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 0.0 -0.7 -3.5" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 0.5 -0.6 -3.9" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 1.0 -0.5 -4.3" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 1.4 -0.4 -4.7" radius="0.06" color="#ffffff"></a-sphere>

    <!-- Extra primitives for even more visual cues -->
    <a-ring position="-1.4 0.0 -3.4" radius-inner="0.1" radius-outer="0.25" color="#ffdddd"></a-ring>
    <a-ring position=" 1.3 -0.1 -3.0" radius-inner="0.1" radius-outer="0.25" color="#ddffdd"></a-ring>
    <a-cone position=" -0.9 -1.1 -4.0" radius-bottom="0.3" radius-top="0.0" height="0.7" color="#ddddff"></a-cone>
    <a-cone position="  0.9 -1.2 -4.4" radius-bottom="0.3" radius-top="0.0" height="0.7" color="#ffddff"></a-cone>

    <!-- Lights -->
    <a-entity light="type: point; intensity: 1.4; distance: 10" position="0 1 0"></a-entity>
    <a-entity light="type: ambient; intensity: 0.3"></a-entity>
  </a-scene>

  <!-- All JS as an ES module -->
  <script type="module">
    import {
      FaceLandmarker,
      FilesetResolver
    } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/vision_bundle.js";

    const video = document.getElementById("video");
    let faceLandmarker = null;
    let running = false;
    let lastVideoTime = -1;

    // Initialize webcam
    async function initCamera() {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: 640, height: 480 }
      });
      video.srcObject = stream;
      return new Promise(resolve => {
        video.onloadedmetadata = () => resolve();
      });
    }

    // Initialize Mediapipe FaceLandmarker
    async function initFaceLandmarker() {
      const filesetResolver = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
      );

      faceLandmarker = await FaceLandmarker.createFromOptions(filesetResolver, {
        baseOptions: {
          modelAssetPath:
            "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task"
        },
        runningMode: "VIDEO",
        numFaces: 1
      });
    }

    // Compute head center as the average of all landmarks (normalized [0..1])
    function getHeadCenterFromLandmarks(landmarks) {
      if (!landmarks || !landmarks.length) return null;
      let sumX = 0;
      let sumY = 0;
      const n = landmarks.length;
      for (let i = 0; i < n; i++) {
        sumX += landmarks[i].x;
        sumY += landmarks[i].y;
      }
      return { x: sumX / n, y: sumY / n };
    }

    // Map head position -> camera rig position
    // head left  -> camera right
    // head right -> camera left
    // head up    -> camera down
    // head down  -> camera up
    function mapHeadToCamera(headCenter) {
      const nx = headCenter.x * 2 - 1;   // -1 = left, +1 = right
      const ny = headCenter.y * 2 - 1;   // -1 = top,  +1 = bottom

      // Tunable movement range in scene units
      const maxX = 0.5;   // side-to-side camera movement
      const maxY = 0.3;   // up-down camera movement
      const baseZ = 0.8;  // base camera distance
      const maxZOffset = 0.25;

      // Inversion for parallax "window" effect
      const camX = -nx * maxX;   // head left -> camera right
      const camY = ny * maxY;    // head up (ny=-1) -> camY negative (down)

      // Optional: small Z variation depending on distance from screen center
      const distanceFromCenter = Math.min(Math.sqrt(nx * nx + ny * ny), 1.0);
      const camZ = baseZ + distanceFromCenter * maxZOffset;

      return { x: camX, y: camY, z: camZ };
    }

    // Simple exponential smoothing for camera movement
    function smooth(prev, next, factor) {
      if (!prev) return next;
      return {
        x: prev.x + (next.x - prev.x) * factor,
        y: prev.y + (next.y - prev.y) * factor,
        z: prev.z + (next.z - prev.z) * factor
      };
    }

    let smoothedCamPos = null;
    const rigEl = document.getElementById("rig");

    async function processVideoFrame() {
      if (!running) return;

      const nowMs = performance.now();
      const videoTime = video.currentTime;

      // Avoid re-processing the same frame
      if (videoTime === lastVideoTime) {
        requestAnimationFrame(processVideoFrame);
        return;
      }
      lastVideoTime = videoTime;

      const results = faceLandmarker.detectForVideo(video, nowMs);

      if (results.faceLandmarks && results.faceLandmarks.length > 0) {
        const landmarks = results.faceLandmarks[0];
        const center = getHeadCenterFromLandmarks(landmarks);

        if (center) {
          const camPos = mapHeadToCamera(center);
          smoothedCamPos = smooth(smoothedCamPos, camPos, 0.18); // smoothing factor

          rigEl.setAttribute(
            "position",
            smoothedCamPos.x + " " +
            smoothedCamPos.y + " " +
            smoothedCamPos.z
          );
        }
      }

      requestAnimationFrame(processVideoFrame);
    }

    // Bootstrap everything
    (async function start() {
      try {
        await initCamera();
        await initFaceLandmarker();
        running = true;
        processVideoFrame();
      } catch (e) {
        console.error("Error initializing:", e);
      }
    })();
  </script>
</body>
</html>
```

### caja abierta

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Parallax Box with Head Tracking</title>

  <!-- A-Frame -->
  <script src="https://aframe.io/releases/1.5.0/aframe.min.js"></script>

  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #000;
    }
    #video {
      position: fixed;
      bottom: 10px;
      right: 10px;
      width: 220px;
      transform: scaleX(-1); /* mirror for natural feeling */
      opacity: 0.4;          /* set to 0 or display:none when you no longer need it */
      z-index: 10;
      border: 2px solid #444;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <!-- Debug webcam preview -->
  <video id="video" autoplay playsinline></video>

  <!-- 3D scene -->
  <a-scene>
    <!-- Camera rig OUTSIDE the box, looking towards negative Z -->
    <!-- This rig will move to emulate parallax -->
    <a-entity id="rig" position="0 0 1.2">
      <a-entity id="cam" camera look-controls="enabled: false"></a-entity>
    </a-entity>

    <!-- FRONT FRAME at z = 0: pivot plane / "window" (open center) -->
    <!-- Top bar -->
    <a-box position="0 1.5 0"
           depth="0.03"
           height="0.1"
           width="4"
           color="#777"
           material="metalness:0.1; roughness:0.6">
    </a-box>
    <!-- Bottom bar -->
    <a-box position="0 -1.5 0"
           depth="0.03"
           height="0.1"
           width="4"
           color="#777"
           material="metalness:0.1; roughness:0.6">
    </a-box>
    <!-- Left bar -->
    <a-box position="-2 0 0"
           depth="0.03"
           height="3"
           width="0.1"
           color="#777"
           material="metalness:0.1; roughness:0.6">
    </a-box>
    <!-- Right bar -->
    <a-box position="2 0 0"
           depth="0.03"
           height="3"
           width="0.1"
           color="#777"
           material="metalness:0.1; roughness:0.6">
    </a-box>

    <!-- BOX INTERIOR, OPEN TOWARDS CAMERA (no front wall) -->
    <!-- Back wall at z = -4 -->
    <a-box position="0 0 -4"
           depth="0.05"
           height="3"
           width="4"
           color="#222">
    </a-box>

    <!-- Floor and ceiling around z = -2 -->
    <a-box position="0 -1.5 -2"
           rotation="90 0 0"
           depth="0.05"
           height="4"
           width="4"
           color="#333">
    </a-box> <!-- floor -->

    <a-box position="0 1.5 -2"
           rotation="-90 0 0"
           depth="0.05"
           height="4"
           width="4"
           color="#333">
    </a-box> <!-- ceiling -->

    <!-- Left and right walls -->
    <a-box position="-2 0 -2"
           rotation="0 90 0"
           depth="0.05"
           height="3"
           width="4"
           color="#444">
    </a-box> <!-- left wall -->

    <a-box position="2 0 -2"
           rotation="0 -90 0"
           depth="0.05"
           height="3"
           width="4"
           color="#444">
    </a-box> <!-- right wall -->

    <!-- PRIMITIVES: multiple rows and depths for strong parallax -->

    <!-- Row 1 (near, around z ~ -1.5..-2.5) -->
    <a-sphere   position="-1.2 -0.4 -1.8" radius="0.25" color="#ff4444"></a-sphere>
    <a-box      position=" 0.0 -0.6 -2.2" depth="0.5" height="0.5" width="0.5" color="#44ff44"></a-box>
    <a-cylinder position=" 1.2 -0.4 -2.0" radius="0.2" height="0.7" color="#4444ff"></a-cylinder>

    <!-- Row 2 (mid, around z ~ -2.5..-3.5) -->
    <a-torus-knot position="-0.8 0.4 -2.8" radius="0.25" radius-tubular="0.06" color="#ffcc00"></a-torus-knot>
    <a-octahedron position=" 0.6 0.2 -3.0" radius="0.2" color="#00ffcc"></a-octahedron>
    <a-dodecahedron position=" 1.4 0.5 -3.3" radius="0.25" color="#ff00aa"></a-dodecahedron>

    <!-- Row 3 (farther, around z ~ -3.5..-4.5) -->
    <a-sphere   position="-1.5 0.9 -3.6" radius="0.18" color="#ffaa88"></a-sphere>
    <a-box      position="-0.2 1.0 -3.9" depth="0.4" height="0.4" width="0.4" color="#88ffaa"></a-box>
    <a-cylinder position=" 0.9 1.1 -4.1" radius="0.18" height="0.6" color="#88aaff"></a-cylinder>
    <a-torus    position=" 0.0 -1.0 -3.4" radius="0.4" radius-tubular="0.07" color="#ff8888"></a-torus>

    <!-- Path of small spheres going deeper into the box -->
    <a-sphere position="-1.5 -1.0 -2.0" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position="-1.0 -0.9 -2.4" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position="-0.5 -0.8 -2.8" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 0.0 -0.7 -3.2" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 0.5 -0.6 -3.6" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 1.0 -0.5 -4.0" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 1.4 -0.4 -4.4" radius="0.06" color="#ffffff"></a-sphere>

    <!-- Extra primitives -->
    <a-ring position="-1.4 0.0 -3.0" radius-inner="0.1" radius-outer="0.25" color="#ffdddd"></a-ring>
    <a-ring position=" 1.3 -0.1 -2.7" radius-inner="0.1" radius-outer="0.25" color="#ddffdd"></a-ring>
    <a-cone position=" -0.9 -1.1 -3.5" radius-bottom="0.3" radius-top="0.0" height="0.7" color="#ddddff"></a-cone>
    <a-cone position="  0.9 -1.2 -3.9" radius-bottom="0.3" radius-top="0.0" height="0.7" color="#ffddff"></a-cone>

    <!-- Lights -->
    <a-entity light="type: point; intensity: 1.4; distance: 10" position="0 1 0"></a-entity>
    <a-entity light="type: ambient; intensity: 0.3"></a-entity>
  </a-scene>

  <!-- All JS as an ES module (MediaPipe Tasks Vision) -->
  <script type="module">
    import {
      FaceLandmarker,
      FilesetResolver
    } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/vision_bundle.js";

    const video = document.getElementById("video");
    let faceLandmarker = null;
    let running = false;
    let lastVideoTime = -1;

    async function initCamera() {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: 640, height: 480 }
      });
      video.srcObject = stream;
      return new Promise(resolve => {
        video.onloadedmetadata = () => resolve();
      });
    }

    async function initFaceLandmarker() {
      const filesetResolver = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
      );

      faceLandmarker = await FaceLandmarker.createFromOptions(filesetResolver, {
        baseOptions: {
          modelAssetPath:
            "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task"
        },
        runningMode: "VIDEO",
        numFaces: 1
      });
    }

    function getHeadCenterFromLandmarks(landmarks) {
      if (!landmarks || !landmarks.length) return null;
      let sumX = 0;
      let sumY = 0;
      const n = landmarks.length;
      for (let i = 0; i < n; i++) {
        sumX += landmarks[i].x;
        sumY += landmarks[i].y;
      }
      return { x: sumX / n, y: sumY / n };
    }

    // head left  -> camera right
    // head right -> camera left
    // head up    -> camera down
    // head down  -> camera up
    function mapHeadToCamera(headCenter) {
      const nx = headCenter.x * 2 - 1;   // -1 = left, +1 = right
      const ny = headCenter.y * 2 - 1;   // -1 = top,  +1 = bottom

      const maxX = 0.5;   // horizontal camera movement
      const maxY = 0.3;   // vertical camera movement
      const baseZ = 1.2;  // camera distance from pivot plane (z=0)
      const maxZOffset = 0.25;

      const camX = -nx * maxX;  // inversion for parallax
      const camY = ny * maxY;

      const distanceFromCenter = Math.min(Math.sqrt(nx * nx + ny * ny), 1.0);
      const camZ = baseZ + distanceFromCenter * maxZOffset;

      return { x: camX, y: camY, z: camZ };
    }

    function smooth(prev, next, factor) {
      if (!prev) return next;
      return {
        x: prev.x + (next.x - prev.x) * factor,
        y: prev.y + (next.y - prev.y) * factor,
        z: prev.z + (next.z - prev.z) * factor
      };
    }

    let smoothedCamPos = null;
    const rigEl = document.getElementById("rig");

    async function processVideoFrame() {
      if (!running) return;

      const nowMs = performance.now();
      const videoTime = video.currentTime;

      if (videoTime === lastVideoTime) {
        requestAnimationFrame(processVideoFrame);
        return;
      }
      lastVideoTime = videoTime;

      const results = faceLandmarker.detectForVideo(video, nowMs);

      if (results.faceLandmarks && results.faceLandmarks.length > 0) {
        const landmarks = results.faceLandmarks[0];
        const center = getHeadCenterFromLandmarks(landmarks);

        if (center) {
          const camPos = mapHeadToCamera(center);
          smoothedCamPos = smooth(smoothedCamPos, camPos, 0.18);

          rigEl.setAttribute(
            "position",
            smoothedCamPos.x + " " +
            smoothedCamPos.y + " " +
            smoothedCamPos.z
          );
        }
      }

      requestAnimationFrame(processVideoFrame);
    }

    (async function start() {
      try {
        await initCamera();
        await initFaceLandmarker();
        running = true;
        processVideoFrame();
      } catch (e) {
        console.error("Error initializing:", e);
      }
    })();
  </script>
</body>
</html>
```

### exageracion de movimiento

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Parallax Box with Head Tracking</title>

  <!-- A-Frame -->
  <script src="https://aframe.io/releases/1.5.0/aframe.min.js"></script>

  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #000;
      font-family: sans-serif;
      color: #eee;
    }
    #video {
      position: fixed;
      bottom: 10px;
      right: 10px;
      width: 220px;
      transform: scaleX(-1); /* mirror for natural feeling */
      opacity: 0.4;          /* set to 0 or display:none when you no longer need it */
      z-index: 10;
      border: 2px solid #444;
      border-radius: 4px;
    }
    #ui {
      position: fixed;
      top: 10px;
      left: 10px;
      z-index: 20;
      background: rgba(0,0,0,0.6);
      padding: 8px 10px;
      border-radius: 6px;
      border: 1px solid #555;
      font-size: 14px;
    }
    #parallaxRange {
      width: 150px;
      vertical-align: middle;
    }
    label {
      margin-right: 4px;
    }
  </style>
</head>
<body>
  <!-- Simple UI for parallax strength -->
  <div id="ui">
    <label for="parallaxRange">Parallax:</label>
    <input id="parallaxRange" type="range" min="0" max="2" step="0.05" value="1" />
    <span id="parallaxValue">1.00</span>
  </div>

  <!-- Debug webcam preview -->
  <video id="video" autoplay playsinline></video>

  <!-- 3D scene -->
  <a-scene>
    <!-- Camera rig INSIDE the box, slightly behind the window plane -->
    <!-- Window (pivot) at z = -1, camera base around z = -1.2 -->
    <a-entity id="rig" position="0 0 -1.2">
      <a-entity id="cam" camera look-controls="enabled: false"></a-entity>
    </a-entity>

    <!-- FRONT FRAME at z = -1: pivot plane / "window" (open center) -->
    <!-- Top bar -->
    <a-box position="0 1.5 -1"
           depth="0.03"
           height="0.1"
           width="4"
           color="#777"
           material="metalness:0.1; roughness:0.6">
    </a-box>
    <!-- Bottom bar -->
    <a-box position="0 -1.5 -1"
           depth="0.03"
           height="0.1"
           width="4"
           color="#777"
           material="metalness:0.1; roughness:0.6">
    </a-box>
    <!-- Left bar -->
    <a-box position="-2 0 -1"
           depth="0.03"
           height="3"
           width="0.1"
           color="#777"
           material="metalness:0.1; roughness:0.6">
    </a-box>
    <!-- Right bar -->
    <a-box position="2 0 -1"
           depth="0.03"
           height="3"
           width="0.1"
           color="#777"
           material="metalness:0.1; roughness:0.6">
    </a-box>

    <!-- BOX INTERIOR, open towards camera (no solid front wall) -->
    <!-- Back wall deeper inside -->
    <a-box position="0 0 -4"
           depth="0.05"
           height="3"
           width="4"
           color="#222">
    </a-box>

    <!-- Floor and ceiling -->
    <a-box position="0 -1.5 -2.4"
           rotation="90 0 0"
           depth="0.05"
           height="4"
           width="4"
           color="#333">
    </a-box> <!-- floor -->

    <a-box position="0 1.5 -2.4"
           rotation="-90 0 0"
           depth="0.05"
           height="4"
           width="4"
           color="#333">
    </a-box> <!-- ceiling -->

    <!-- Left and right walls -->
    <a-box position="-2 0 -2.4"
           rotation="0 90 0"
           depth="0.05"
           height="3"
           width="4"
           color="#444">
    </a-box> <!-- left wall -->

    <a-box position="2 0 -2.4"
           rotation="0 -90 0"
           depth="0.05"
           height="3"
           width="4"
           color="#444">
    </a-box> <!-- right wall -->

    <!-- PRIMITIVES: multiple rows and depths for strong parallax -->

    <!-- Row 1 (near camera, just behind the window) -->
    <a-sphere   position="-1.2 -0.4 -1.6" radius="0.25" color="#ff4444"></a-sphere>
    <a-box      position=" 0.0 -0.6 -1.8" depth="0.5" height="0.5" width="0.5" color="#44ff44"></a-box>
    <a-cylinder position=" 1.2 -0.4 -1.7" radius="0.2" height="0.7" color="#4444ff"></a-cylinder>

    <!-- Row 2 (mid) -->
    <a-torus-knot position="-0.8 0.4 -2.4" radius="0.25" radius-tubular="0.06" color="#ffcc00"></a-torus-knot>
    <a-octahedron position=" 0.6 0.2 -2.7" radius="0.2" color="#00ffcc"></a-octahedron>
    <a-dodecahedron position=" 1.4 0.5 -3.0" radius="0.25" color="#ff00aa"></a-dodecahedron>

    <!-- Row 3 (farther) -->
    <a-sphere   position="-1.5 0.9 -3.2" radius="0.18" color="#ffaa88"></a-sphere>
    <a-box      position="-0.2 1.0 -3.5" depth="0.4" height="0.4" width="0.4" color="#88ffaa"></a-box>
    <a-cylinder position=" 0.9 1.1 -3.7" radius="0.18" height="0.6" color="#88aaff"></a-cylinder>
    <a-torus    position=" 0.0 -1.0 -3.0" radius="0.4" radius-tubular="0.07" color="#ff8888"></a-torus>

    <!-- Path of small spheres going deeper -->
    <a-sphere position="-1.5 -1.0 -1.9" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position="-1.0 -0.9 -2.3" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position="-0.5 -0.8 -2.7" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 0.0 -0.7 -3.1" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 0.5 -0.6 -3.5" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 1.0 -0.5 -3.9" radius="0.06" color="#ffffff"></a-sphere>
    <a-sphere position=" 1.4 -0.4 -4.3" radius="0.06" color="#ffffff"></a-sphere>

    <!-- Extra primitives -->
    <a-ring position="-1.4 0.0 -2.8" radius-inner="0.1" radius-outer="0.25" color="#ffdddd"></a-ring>
    <a-ring position=" 1.3 -0.1 -2.5" radius-inner="0.1" radius-outer="0.25" color="#ddffdd"></a-ring>
    <a-cone position=" -0.9 -1.1 -3.1" radius-bottom="0.3" radius-top="0.0" height="0.7" color="#ddddff"></a-cone>
    <a-cone position="  0.9 -1.2 -3.5" radius-bottom="0.3" radius-top="0.0" height="0.7" color="#ffddff"></a-cone>

    <!-- Lights -->
    <a-entity light="type: point; intensity: 1.4; distance: 10" position="0 1 -1.2"></a-entity>
    <a-entity light="type: ambient; intensity: 0.3"></a-entity>
  </a-scene>

  <!-- All JS as an ES module (MediaPipe Tasks Vision) -->
  <script type="module">
    import {
      FaceLandmarker,
      FilesetResolver
    } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/vision_bundle.js";

    const video = document.getElementById("video");
    const parallaxRange = document.getElementById("parallaxRange");
    const parallaxValue = document.getElementById("parallaxValue");

    let faceLandmarker = null;
    let running = false;
    let lastVideoTime = -1;

    let parallaxFactor = 1.0; // multiplier for camera movement

    parallaxRange.addEventListener("input", (e) => {
      parallaxFactor = parseFloat(e.target.value);
      parallaxValue.textContent = parallaxFactor.toFixed(2);
    });

    async function initCamera() {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: 640, height: 480 }
      });
      video.srcObject = stream;
      return new Promise(resolve => {
        video.onloadedmetadata = () => resolve();
      });
    }

    async function initFaceLandmarker() {
      const filesetResolver = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
      );

      faceLandmarker = await FaceLandmarker.createFromOptions(filesetResolver, {
        baseOptions: {
          modelAssetPath:
            "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task"
        },
        runningMode: "VIDEO",
        numFaces: 1
      });
    }

    function getHeadCenterFromLandmarks(landmarks) {
      if (!landmarks || !landmarks.length) return null;
      let sumX = 0;
      let sumY = 0;
      const n = landmarks.length;
      for (let i = 0; i < n; i++) {
        sumX += landmarks[i].x;
        sumY += landmarks[i].y;
      }
      return { x: sumX / n, y: sumY / n };
    }

    // head left  -> camera right
    // head right -> camera left
    // head up    -> camera down
    // head down  -> camera up
    //
    // Pivot plane is the window at z = -1.
    // Camera base position is around z = -1.2 (slightly inside box).
    function mapHeadToCamera(headCenter) {
      const nx = headCenter.x * 2 - 1;   // -1 = left, +1 = right
      const ny = headCenter.y * 2 - 1;   // -1 = top,  +1 = bottom

      // Base movement range in scene units
      const baseMaxX = 0.35;
      const baseMaxY = 0.25;
      const baseZ    = -1.2;  // camera depth relative to pivot
      const maxZOffset = 0.20;

      // Apply parallax multiplier from UI
      const maxX = baseMaxX * parallaxFactor;
      const maxY = baseMaxY * parallaxFactor;

      const camX = -nx * maxX;   // inversion for parallax
      const camY =  ny * maxY;   // ny=-1 (up) -> camY negative (down)

      // Optional: small Z variation depending on distance from screen center
      const distanceFromCenter = Math.min(Math.sqrt(nx * nx + ny * ny), 1.0);
      const camZ = baseZ + distanceFromCenter * maxZOffset * parallaxFactor;

      return { x: camX, y: camY, z: camZ };
    }

    function smooth(prev, next, factor) {
      if (!prev) return next;
      return {
        x: prev.x + (next.x - prev.x) * factor,
        y: prev.y + (next.y - prev.y) * factor,
        z: prev.z + (next.z - prev.z) * factor
      };
    }

    let smoothedCamPos = null;
    const rigEl = document.getElementById("rig");

    async function processVideoFrame() {
      if (!running) return;

      const nowMs = performance.now();
      const videoTime = video.currentTime;

      if (videoTime === lastVideoTime) {
        requestAnimationFrame(processVideoFrame);
        return;
      }
      lastVideoTime = videoTime;

      const results = faceLandmarker.detectForVideo(video, nowMs);

      if (results.faceLandmarks && results.faceLandmarks.length > 0) {
        const landmarks = results.faceLandmarks[0];
        const center = getHeadCenterFromLandmarks(landmarks);

        if (center) {
          const camPos = mapHeadToCamera(center);
          smoothedCamPos = smooth(smoothedCamPos, camPos, 0.18);

          rigEl.setAttribute(
            "position",
            smoothedCamPos.x + " " +
            smoothedCamPos.y + " " +
            smoothedCamPos.z
          );
        }
      }

      requestAnimationFrame(processVideoFrame);
    }

    (async function start() {
      try {
        await initCamera();
        await initFaceLandmarker();
        running = true;
        processVideoFrame();
      } catch (e) {
        console.error("Error initializing:", e);
      }
    })();
  </script>
</body>
</html>
```

### sombras

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Parallax 3d</title>

  <!-- A-Frame -->
  <script src="https://aframe.io/releases/1.5.0/aframe.min.js"></script>
  <!-- Environment component for gradient sky etc. -->
  <script src="https://cdn.jsdelivr.net/gh/feiss/aframe-environment-component/dist/aframe-environment-component.min.js"></script>

  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #000;
      font-family: sans-serif;
      color: #eee;
    }
    #video {
      position: fixed;
      bottom: 10px;
      right: 10px;
      width: 220px;
      transform: scaleX(-1); /* mirror horizontally */
      opacity: 0.4;
      z-index: 10;
      border: 2px solid #444;
      border-radius: 4px;
    }
    #ui {
      position: fixed;
      top: 10px;
      left: 10px;
      z-index: 20;
      background: rgba(0,0,0,0.6);
      padding: 8px 10px;
      border-radius: 6px;
      border: 1px solid #555;
      font-size: 14px;
    }
    #parallaxRange {
      width: 150px;
      vertical-align: middle;
    }
    label {
      margin-right: 4px;
    }
  </style>
</head>
<body>
  <!-- UI for parallax strength -->
  <div id="ui">
    <label for="parallaxRange">Parallax:</label>
    <input id="parallaxRange" type="range" min="0" max="5" step="0.05" value="1" />
    <span id="parallaxValue">1.00</span>
  </div>

  <!-- Webcam preview (debug) -->
  <video id="video" autoplay playsinline></video>

  <!-- 3D scene -->
  <a-scene
    renderer="antialias: true; colorManagement: true; physicallyCorrectLights: true; shadowMap.enabled: true; shadowMap.type: pcfsoft"
  >
    <!-- Gradient sky + distant ground (environment component) -->
    <a-entity environment="
      preset: default;
      ground: flat;
      groundYScale: 1;
      groundTexture: none;
      groundColor: #303030;
      groundColor2: #404040;
      skyType: gradient;
      skyColor: #88ccee;
      horizonColor: #ffffff;
      lighting: none;
    "></a-entity>

    <!-- MAIN GROUND PLANE near the camera, receiving shadows -->
    <a-plane position="0 0 0"
             rotation="-90 0 0"
             width="100"
             height="100"
             color="#404040"
             shadow="receive: true">
    </a-plane>

    <!-- Camera rig: above ground, at some distance looking towards origin -->
    <!-- Base camera position will be (0, baseY, baseZ) and we move around that -->
    <a-entity id="rig" position="0 1.6 0">
      <a-entity id="cam" camera look-controls="enabled: false"></a-entity>
    </a-entity>

    <!-- A target entity to orient the sun towards origin -->
    <a-entity id="sunTarget" position="0 0 0"></a-entity>

    <!-- Directional sun light with shadows -->
    <a-entity light="type: directional; intensity: 1.1; castShadow: true"
              position="4 8 6"
              target="#sunTarget">
    </a-entity>

    <!-- Soft ambient/global light -->
    <a-entity light="type: ambient; intensity: 0.35; color: #ffffff"></a-entity>

    <!-- PRIMITIVES SCATTERED ON THE PLANE (all casting / receiving shadows) -->

    <!-- Cluster 1 -->
    <a-sphere position="-2 0.5 -3"
              radius="0.5"
              color="#ff4444"
              shadow="cast: true; receive: true"></a-sphere>

    <a-box position="-0.8 0.4 -2.2"
           depth="0.6" height="0.6" width="0.6"
           color="#44ff44"
           shadow="cast: true; receive: true"></a-box>

    <a-cylinder position="0.6 0.5 -3.2"
                radius="0.3" height="1"
                color="#4444ff"
                shadow="cast: true; receive: true"></a-cylinder>

    <!-- Cluster 2 -->
    <a-torus-knot position="1.8 0.9 -4"
                   radius="0.6"
                   radius-tubular="0.08"
                   color="#ffcc00"
                   shadow="cast: true; receive: true"></a-torus-knot>

    <a-dodecahedron position="3 0.7 -5"
                    radius="0.5"
                    color="#ff00aa"
                    shadow="cast: true; receive: true"></a-dodecahedron>

    <a-octahedron position="-3 0.7 -4.5"
                  radius="0.4"
                  color="#00ffcc"
                  shadow="cast: true; receive: true"></a-octahedron>

    <!-- Cluster 3 -->
    <a-ring position="-1 0.01 -6"
            rotation="-90 0 0"
            radius-inner="0.3"
            radius-outer="0.6"
            color="#ffdddd"
            shadow="cast: true; receive: true"></a-ring>

    <a-cone position="1 0.9 -6.5"
            radius-bottom="0.5"
            radius-top="0.0"
            height="1.2"
            color="#ffddff"
            shadow="cast: true; receive: true"></a-cone>

    <a-torus position="0 0.8 -5.2"
             rotation="0 45 0"
             radius="0.7"
             radius-tubular="0.12"
             color="#88aaff"
             shadow="cast: true; receive: true"></a-torus>

    <!-- Little path of spheres into the distance -->
    <a-sphere position="-1 0.2 -2.5" radius="0.12" color="#ffffff" shadow="cast: true; receive: true"></a-sphere>
    <a-sphere position="-0.5 0.2 -3.5" radius="0.12" color="#ffffff" shadow="cast: true; receive: true"></a-sphere>
    <a-sphere position="0 0.2 -4.5"   radius="0.12" color="#ffffff" shadow="cast: true; receive: true"></a-sphere>
    <a-sphere position="0.5 0.2 -5.5" radius="0.12" color="#ffffff" shadow="cast: true; receive: true"></a-sphere>
    <a-sphere position="1 0.2 -6.5"   radius="0.12" color="#ffffff" shadow="cast: true; receive: true"></a-sphere>
  </a-scene>

  <!-- JS (MediaPipe Tasks Vision) -->
  <script type="module">
    import {
      FaceLandmarker,
      FilesetResolver
    } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/vision_bundle.js";

    const video          = document.getElementById("video");
    const parallaxRange  = document.getElementById("parallaxRange");
    const parallaxValue  = document.getElementById("parallaxValue");
    const rigEl          = document.getElementById("rig");

    let faceLandmarker   = null;
    let running          = false;
    let lastVideoTime    = -1;
    let parallaxFactor   = 1.0;

    // Camera base position (the rig has this as its neutral)
    const baseCam = { x: 0, y: 1.0, z: 0 };

    // For Z from head distance
    let baselineScale = null; // size of face at "neutral" distance

    parallaxRange.addEventListener("input", (e) => {
      parallaxFactor = parseFloat(e.target.value);
      parallaxValue.textContent = parallaxFactor.toFixed(2);
    });

    async function initCamera() {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: 640, height: 480 }
      });
      video.srcObject = stream;
      return new Promise(resolve => {
        video.onloadedmetadata = () => resolve();
      });
    }

    async function initFaceLandmarker() {
      const filesetResolver = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.0/wasm"
      );

      faceLandmarker = await FaceLandmarker.createFromOptions(filesetResolver, {
        baseOptions: {
          modelAssetPath:
            "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task"
        },
        runningMode: "VIDEO",
        numFaces: 1
      });
    }

    // Get center (x,y) and an approximate "scale" (how big the face is), using eye distance
    function getHeadMetrics(landmarks) {
      if (!landmarks || !landmarks.length) return null;

      // Center: average all landmarks (normalized [0..1])
      let sumX = 0;
      let sumY = 0;
      const n = landmarks.length;
      for (let i = 0; i < n; i++) {
        sumX += landmarks[i].x;
        sumY += landmarks[i].y;
      }
      const center = { x: sumX / n, y: sumY / n };

      // Scale: distance between approximate outer eye corners (33 and 263 in FaceMesh / FaceLandmarker)
      let scale = 0.1;
      const leftIdx  = 33;
      const rightIdx = 263;
      if (landmarks[leftIdx] && landmarks[rightIdx]) {
        const lx = landmarks[leftIdx].x;
        const ly = landmarks[leftIdx].y;
        const rx = landmarks[rightIdx].x;
        const ry = landmarks[rightIdx].y;
        scale = Math.hypot(rx - lx, ry - ly);
      }

      return { center, scale };
    }

    // head left  -> camera right
    // head right -> camera left
    // head up    -> camera up      (Y FIXED HERE)
    // head down  -> camera down
    function mapHeadToCamera(center, scale) {
      const nx = center.x * 2 - 1;   // -1 = left, +1 = right
      const ny = center.y * 2 - 1;   // -1 = top,  +1 = bottom

      // Base XY movement range in scene units
      const baseMaxX = 0.5;
      const baseMaxY = 0.3;

      const maxX = baseMaxX * parallaxFactor;
      const maxY = baseMaxY * parallaxFactor;

      // X: invert so head left -> cam right
      const dx = -nx * maxX;
      // Y: invert ny so head up (ny=-1) -> cam up (positive Y)
      const dy = -ny * maxY;

      // Z from face scale (distance to camera)
      // Initialize baseline on first valid frame
      if (scale && !baselineScale) baselineScale = scale;
      let dz = 0;
      if (scale && baselineScale) {
        let rel = scale / baselineScale;         // 1.0 at baseline, >1 closer, <1 farther
        rel = Math.min(Math.max(rel, 0.7), 1.3); // clamp
        const delta = rel - 1.0;
        const maxDepthOffset = 0.8;              // how much we move in/out
        dz = -delta * maxDepthOffset * parallaxFactor;
        // rel>1 (closer)  -> delta>0 -> dz negative -> camera moves closer to scene
        // rel<1 (farther) -> delta<0 -> dz positive -> camera moves away
      }

      return {
        x: baseCam.x + dx,
        y: baseCam.y + dy,
        z: baseCam.z + dz
      };
    }

    function smooth(prev, next, factor) {
      if (!prev) return next;
      return {
        x: prev.x + (next.x - prev.x) * factor,
        y: prev.y + (next.y - prev.y) * factor,
        z: prev.z + (next.z - prev.z) * factor
      };
    }

    let smoothedCamPos = null;

    async function processVideoFrame() {
      if (!running) return;

      const nowMs = performance.now();
      const videoTime = video.currentTime;

      if (videoTime === lastVideoTime) {
        requestAnimationFrame(processVideoFrame);
        return;
      }
      lastVideoTime = videoTime;

      const results = faceLandmarker.detectForVideo(video, nowMs);

      if (results.faceLandmarks && results.faceLandmarks.length > 0) {
        const landmarks = results.faceLandmarks[0];
        const metrics = getHeadMetrics(landmarks);

        if (metrics) {
          const camPos = mapHeadToCamera(metrics.center, metrics.scale);
          smoothedCamPos = smooth(smoothedCamPos, camPos, 0.18);

          rigEl.setAttribute(
            "position",
            `${smoothedCamPos.x} ${smoothedCamPos.y} ${smoothedCamPos.z}`
          );
        }
      }

      requestAnimationFrame(processVideoFrame);
    }

    (async function start() {
      try {
        await initCamera();
        await initFaceLandmarker();
        running = true;
        processVideoFrame();
      } catch (e) {
        console.error("Error initializing:", e);
      }
    })();
  </script>
</body>
</html>
```

<a id="fases-de-desarrollo"></a>
## Fases de desarrollo

El desarrollo de juegos 2D y 3D es un proceso complejo que requiere una planificación cuidadosa y una implementación meticulosa. Comienza con la definición del concepto y el diseño detallado del juego, donde se establecen las reglas, los personajes y los objetivos. A continuación, entra en la fase de codificación, donde se escriben las funciones necesarias para controlar el comportamiento de los personajes y los objetos.

Es importante destacar que cada fase del desarrollo es interconectada y depende de la anterior. Por ejemplo, mientras se está programando, también se realiza un análisis constante del rendimiento del juego para identificar áreas que requieren optimización. Esta fase incluye la creación de escenas, donde los elementos visuales son posicionados y configurados según el diseño.

La codificación es una parte crucial del desarrollo, pero no es el único aspecto a considerar. La gestión del tiempo y la planificación son fundamentales para asegurar que el juego se complete dentro del plazo establecido. Esto implica la creación de un cronograma detallado y la asignación de tareas a los miembros del equipo.

Además, es esencial contar con herramientas adecuadas para facilitar el desarrollo. Estas pueden ser motores de juegos específicos o bibliotecas que proporcionan funciones básicas necesarias para crear contenido multimedia. El uso de estas herramientas puede acelerar significativamente el proceso de codificación y permitir una mayor creatividad.

Una vez que se han completado las fases de codificación y gestión del tiempo, entra en la fase de pruebas. Durante esta etapa, se realizan diversas pruebas para asegurar que el juego funcione correctamente y cumpla con los requisitos establecidos. Esto incluye pruebas de rendimiento, pruebas de seguridad y pruebas de usabilidad.

La fase final del desarrollo implica la publicación del juego en plataformas adecuadas. Esto puede implicar la creación de instaladores para sistemas operativos específicos o la configuración de servidores web para alojar el juego en línea. Además, es importante documentar todo el proceso y las decisiones tomadas durante el desarrollo para facilitar futuras modificaciones o actualizaciones.

En resumen, el desarrollo de juegos 2D y 3D es un proceso que requiere una combinación de diseño creativo, programación meticulosa y gestión eficiente del tiempo. Cada fase es interdependiente y contribuye al éxito final del proyecto.

### red de elementos

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas></canvas>
    <script>
      let anchura = 512;
      let altura = 512;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      
      class Particula{
        constructor(x,y,a){
          this.x = x
          this.y = y
          this.a = a
        }
        dibuja(){
          contexto.beginPath()
          contexto.arc(this.x,this.y,2,0,Math.PI*2)
          contexto.fill()
        }
      }
      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas[i].dibuja();
      }
    </script>
  </body>
</html>
```

### lineas entre las particulas

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
    
      let anchura = 512;
      let altura = 512;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      
      class Particula{
        constructor(x,y,a){
          this.x = x
          this.y = y
          this.a = a
        }
        dibuja(){
          contexto.beginPath()
          contexto.arc(this.x,this.y,5,0,Math.PI*2)
          contexto.fill()
        }
        lineas(){
          for(let i = 0;i<numeroparticulas;i++){
            if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
              contexto.beginPath()
              contexto.moveTo(this.x,this.y)
              contexto.lineTo(particulas[i].x, particulas[i].y)
              contexto.stroke()
            }
          }
        }
      }
      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      // Las particulas
      for(let i = 0;i<numeroparticulas;i++){
        particulas[i].dibuja();
        particulas[i].lineas();
      }
      
    </script>
  </body>
</html>
```

### bucle animado

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
    
      let anchura = 512;
      let altura = 512;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      
      class Particula{
        constructor(x,y,a){
          this.x = x
          this.y = y
          this.a = a
        }
        dibuja(){
          contexto.beginPath()
          contexto.arc(this.x,this.y,5,0,Math.PI*2)
          contexto.fill()
        }
        lineas(){
          for(let i = 0;i<numeroparticulas;i++){
            if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
              contexto.beginPath()
              contexto.moveTo(this.x,this.y)
              contexto.lineTo(particulas[i].x, particulas[i].y)
              contexto.stroke()
            }
          }
        }
      }
      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for(let i = 0;i<numeroparticulas;i++){
          particulas[i].dibuja();
          particulas[i].lineas();
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
      
    </script>
  </body>
</html>
```

### hacemos que las particulas se muevan

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
    
      let anchura = 512;
      let altura = 512;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      
      class Particula{
        constructor(x,y,a){
          this.x = x
          this.y = y
          this.a = a
        }
        dibuja(){
          contexto.beginPath()
          contexto.arc(this.x,this.y,5,0,Math.PI*2)
          contexto.fill()
        }
        lineas(){
          for(let i = 0;i<numeroparticulas;i++){
            if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
              contexto.beginPath()
              contexto.moveTo(this.x,this.y)
              contexto.lineTo(particulas[i].x, particulas[i].y)
              contexto.stroke()
            }
          }
        }
        mueve(){
          this.a += (Math.random()-0.5)*1
          this.x += Math.cos(this.a)
          this.y += Math.sin(this.a)
        }
      }
      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for(let i = 0;i<numeroparticulas;i++){
          particulas[i].mueve();
          particulas[i].dibuja();
          particulas[i].lineas();
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
      
    </script>
  </body>
</html>
```

### rebote en las paredes

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
    
      let anchura = 512;
      let altura = 512;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      
      class Particula{
        constructor(x,y,a){
          this.x = x
          this.y = y
          this.a = a
        }
        dibuja(){
          contexto.beginPath()
          contexto.arc(this.x,this.y,5,0,Math.PI*2)
          contexto.fill()
        }
        lineas(){
          for(let i = 0;i<numeroparticulas;i++){
            if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
              contexto.beginPath()
              contexto.moveTo(this.x,this.y)
              contexto.lineTo(particulas[i].x, particulas[i].y)
              contexto.stroke()
            }
          }
        }
        mueve(){
          this.a += (Math.random()-0.5)*1
          this.x += Math.cos(this.a)
          this.y += Math.sin(this.a)
        }
        rebote(){
          if(this.x > anchura || this.x < 0 || this.y > altura || this.y < 0){
            
          }
        }
      }
      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for(let i = 0;i<numeroparticulas;i++){
          particulas[i].mueve();
          particulas[i].dibuja();
          particulas[i].lineas();
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",100)
      }
      
    </script>
  </body>
</html>
```

### reflejo realista

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
      function bounceAngle(incidentAngle, wallAngle) {
          const relative = incidentAngle - wallAngle;   // angle of incidence
          const reflectedRelative = -relative;          // mirror
          return reflectedRelative + wallAngle;         // return to world space
      }
      let anchura = 512;
      let altura = 512;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      
      class Particula{
          constructor(x,y,a){
              this.x = x;
              this.y = y;
              this.a = a;
          }
          dibuja(){
              contexto.beginPath();
              contexto.arc(this.x,this.y,5,0,Math.PI*2);
              contexto.fill();
          }
          lineas(){
              for(let i = 0;i<numeroparticulas;i++){
                  if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
                      contexto.beginPath();
                      contexto.moveTo(this.x,this.y);
                      contexto.lineTo(particulas[i].x, particulas[i].y);
                      contexto.stroke();
                  }
              }
          }
          mueve(){
              this.a += (Math.random()-0.5) * 0.1;
              this.x += Math.cos(this.a);
              this.y += Math.sin(this.a);
          }

          rebote(){
              // Right wall
              if (this.x > anchura) {
                  this.x = anchura;
                  this.a = bounceAngle(this.a, Math.PI/2); // wall angle = vertical
              }
              // Left wall
              if (this.x < 0) {
                  this.x = 0;
                  this.a = bounceAngle(this.a, Math.PI/2);
              }

              // Bottom wall
              if (this.y > altura) {
                  this.y = altura;
                  this.a = bounceAngle(this.a, 0); // horizontal wall
              }
              // Top wall
              if (this.y < 0) {
                  this.y = 0;
                  this.a = bounceAngle(this.a, 0);
              }
          }
      }

      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for(let i = 0;i<numeroparticulas;i++){
          particulas[i].mueve();
          particulas[i].dibuja();
          particulas[i].lineas();
          particulas[i].rebote();
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",10)
      }
      
    </script>
  </body>
</html>
```

### añadimos velocidad

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{margin:0px;padding:0px;}
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
      function bounceAngle(incidentAngle, wallAngle) {
          const relative = incidentAngle - wallAngle;   // angle of incidence
          const reflectedRelative = -relative;          // mirror
          return reflectedRelative + wallAngle;         // return to world space
      }
      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      
      class Particula{
          constructor(x,y,a){
              this.x = x;
              this.y = y;
              this.a = a;
              this.v = 0.1
          }
          dibuja(){
              contexto.beginPath();
              contexto.arc(this.x,this.y,5,0,Math.PI*2);
              contexto.fill();
          }
          lineas(){
              for(let i = 0;i<numeroparticulas;i++){
                  if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
                      contexto.beginPath();
                      contexto.moveTo(this.x,this.y);
                      contexto.lineTo(particulas[i].x, particulas[i].y);
                      contexto.stroke();
                  }
              }
          }
          mueve(){
              this.a += (Math.random()-0.5) * 0.1;
              this.x += Math.cos(this.a)*this.v;
              this.y += Math.sin(this.a)*this.v;
          }

          rebote(){
              // Right wall
              if (this.x > anchura) {
                  this.x = anchura;
                  this.a = bounceAngle(this.a, Math.PI/2); // wall angle = vertical
              }
              // Left wall
              if (this.x < 0) {
                  this.x = 0;
                  this.a = bounceAngle(this.a, Math.PI/2);
              }

              // Bottom wall
              if (this.y > altura) {
                  this.y = altura;
                  this.a = bounceAngle(this.a, 0); // horizontal wall
              }
              // Top wall
              if (this.y < 0) {
                  this.y = 0;
                  this.a = bounceAngle(this.a, 0);
              }
          }
      }

      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for(let i = 0;i<numeroparticulas;i++){
          particulas[i].mueve();
          particulas[i].dibuja();
          particulas[i].lineas();
          particulas[i].rebote();
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",10)
      }
      
    </script>
  </body>
</html>
```

### un poco de color

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{margin:0px;padding:0px;}
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
      function bounceAngle(incidentAngle, wallAngle) {
          const relative = incidentAngle - wallAngle;   // angle of incidence
          const reflectedRelative = -relative;          // mirror
          return reflectedRelative + wallAngle;         // return to world space
      }
      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      
      class Particula{
          constructor(x,y,a){
              this.x = x;
              this.y = y;
              this.a = a;
              this.v = 0.1
          }
          dibuja(){
              contexto.strokeStyle = "black"
              contexto.beginPath();
              contexto.arc(this.x,this.y,5,0,Math.PI*2);
              contexto.fill();
          }
          lineas(){
            contexto.strokeStyle = "grey"
              for(let i = 0;i<numeroparticulas;i++){
                  if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
                      contexto.beginPath();
                      contexto.moveTo(this.x,this.y);
                      contexto.lineTo(particulas[i].x, particulas[i].y);
                      contexto.stroke();
                  }
              }
          }
          mueve(){
              this.a += (Math.random()-0.5) * 0.1;
              this.x += Math.cos(this.a)*this.v;
              this.y += Math.sin(this.a)*this.v;
          }

          rebote(){
              // Right wall
              if (this.x > anchura) {
                  this.x = anchura;
                  this.a = bounceAngle(this.a, Math.PI/2); // wall angle = vertical
              }
              // Left wall
              if (this.x < 0) {
                  this.x = 0;
                  this.a = bounceAngle(this.a, Math.PI/2);
              }

              // Bottom wall
              if (this.y > altura) {
                  this.y = altura;
                  this.a = bounceAngle(this.a, 0); // horizontal wall
              }
              // Top wall
              if (this.y < 0) {
                  this.y = 0;
                  this.a = bounceAngle(this.a, 0);
              }
          }
      }

      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for(let i = 0;i<numeroparticulas;i++){
          particulas[i].mueve();
          
          particulas[i].lineas();
          particulas[i].dibuja();
          particulas[i].rebote();
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",10)
      }
      
    </script>
  </body>
</html>
```

### array con nombres

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{margin:0px;padding:0px;}
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
      function bounceAngle(incidentAngle, wallAngle) {
          const relative = incidentAngle - wallAngle;   // angle of incidence
          const reflectedRelative = -relative;          // mirror
          return reflectedRelative + wallAngle;         // return to world space
      }
      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";
      let nombres = ['Juan','Julia','Jorge','Jaime','Jose','Julian']
      
      class Particula{
          constructor(x,y,a){
              this.x = x;
              this.y = y;
              this.a = a;
              this.v = 0.1
              this.texto = nombres[Math.floor(Math.random()*nombres.length)]
          }
          dibuja(){
              let anchopastilla = 20
              let altopastilla = 10
              contexto.strokeStyle = "black"
              contexto.beginPath();
              contexto.moveTo(this.x-anchopastilla,this.y-altopastilla)
              contexto.lineTo(this.x+anchopastilla,this.y-altopastilla)
              contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2)
              contexto.lineTo(this.x-anchopastilla,this.y+10)
              contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2)
              contexto.fillStyle = "white"
              contexto.strokeStyle = "black";
              contexto.fill();
              contexto.stroke()
              contexto.fillStyle = "black"
              contexto.fillText(this.texto,this.x,this.y)
          }
          lineas(){
            contexto.strokeStyle = "grey"
              for(let i = 0;i<numeroparticulas;i++){
                  if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
                      contexto.beginPath();
                      contexto.moveTo(this.x,this.y);
                      contexto.lineTo(particulas[i].x, particulas[i].y);
                      contexto.stroke();
                  }
              }
          }
          mueve(){
              this.a += (Math.random()-0.5) * 0.1;
              this.x += Math.cos(this.a)*this.v;
              this.y += Math.sin(this.a)*this.v;
          }

          rebote(){
              // Right wall
              if (this.x > anchura) {
                  this.x = anchura;
                  this.a = bounceAngle(this.a, Math.PI/2); // wall angle = vertical
              }
              // Left wall
              if (this.x < 0) {
                  this.x = 0;
                  this.a = bounceAngle(this.a, Math.PI/2);
              }

              // Bottom wall
              if (this.y > altura) {
                  this.y = altura;
                  this.a = bounceAngle(this.a, 0); // horizontal wall
              }
              // Top wall
              if (this.y < 0) {
                  this.y = 0;
                  this.a = bounceAngle(this.a, 0);
              }
          }
      }

      let particulas = [];
      let numeroparticulas = 50
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for(let i = 0;i<numeroparticulas;i++){
          particulas[i].mueve();
          
          particulas[i].lineas();
          particulas[i].dibuja();
          particulas[i].rebote();
        }
        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",10)
      }
      
    </script>
  </body>
</html>
```

### agrupar particulas con animacion

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{margin:0px;padding:0px;}
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
      function bounceAngle(incidentAngle, wallAngle) {
          const relative = incidentAngle - wallAngle;   // angle of incidence
          const reflectedRelative = -relative;          // mirror
          return reflectedRelative + wallAngle;         // return to world space
      }
      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";
      let nombres = ['Juan','Julia','Jorge','Jaime','Jose','Julian']
      
      class Particula{
          constructor(x,y,a){
              this.x = x;
              this.y = y;
              this.a = a;
              this.v = 0.5
              this.texto = nombres[Math.floor(Math.random()*nombres.length)]
          }
          dibuja(){
              let anchopastilla = 20
              let altopastilla = 10
              contexto.strokeStyle = "black"
              contexto.beginPath();
              contexto.moveTo(this.x-anchopastilla,this.y-altopastilla)
              contexto.lineTo(this.x+anchopastilla,this.y-altopastilla)
              contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2)
              contexto.lineTo(this.x-anchopastilla,this.y+10)
              contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2)
              contexto.fillStyle = "white"
              contexto.strokeStyle = "black";
              contexto.fill();
              contexto.stroke()
              contexto.fillStyle = "black"
              contexto.fillText(this.texto,this.x,this.y)
          }
          lineas(){
            contexto.strokeStyle = "grey"
              for(let i = 0;i<numeroparticulas;i++){
                  if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
                      contexto.beginPath();
                      contexto.moveTo(this.x,this.y);
                      contexto.lineTo(particulas[i].x, particulas[i].y);
                      contexto.stroke();
                  }
              }
          }
          mueve(){
              this.a += (Math.random()-0.5) * 0.1;
              this.x += Math.cos(this.a)*this.v;
              this.y += Math.sin(this.a)*this.v;
          }

          rebote(){
              // Right wall
              if (this.x > anchura) {
                  this.x = anchura;
                  this.a = bounceAngle(this.a, Math.PI/2); // wall angle = vertical
              }
              // Left wall
              if (this.x < 0) {
                  this.x = 0;
                  this.a = bounceAngle(this.a, Math.PI/2);
              }

              // Bottom wall
              if (this.y > altura) {
                  this.y = altura;
                  this.a = bounceAngle(this.a, 0); // horizontal wall
              }
              // Top wall
              if (this.y < 0) {
                  this.y = 0;
                  this.a = bounceAngle(this.a, 0);
              }
          }
          interacciones(particulas) {
              let rango = 340;          // detection radius
              let fuerzaAtraccion = 0.03;
              let fuerzaRepulsion = 0.05;
              let distanciaMin = 135;    // ✔️ minimum spacing between same particles

              let ax = 0;
              let ay = 0;

              for (let p of particulas) {
                  if (p === this) continue;

                  let d = distance2D(this.x, this.y, p.x, p.y);
                  if (d > rango || d === 0) continue;

                  let dx = p.x - this.x;
                  let dy = p.y - this.y;

                  // Normalize direction
                  let ux = dx / d;
                  let uy = dy / d;

                  if (p.texto === this.texto) {

                      if (d > distanciaMin) {
                          // ✔️ Farther than minimum: attract
                          ax += ux;
                          ay += uy;
                      } else {
                          // ❌ Too close: gently push away
                          ax -= ux * 2;
                          ay -= uy * 2;
                      }

                  } else {
                      // ❌ Repel different text
                      ax -= ux * fuerzaRepulsion;
                      ay -= uy * fuerzaRepulsion;
                  }
              }

              // Apply steering
              if (ax !== 0 || ay !== 0) {
                  let targetAngle = Math.atan2(ay, ax);
                  let diff = targetAngle - this.a;
                  diff = Math.atan2(Math.sin(diff), Math.cos(diff)); // normalize
                  this.a += diff * fuerzaAtraccion;
              }
          }


      }

      let particulas = [];
      let numeroparticulas = 250
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for (let i = 0; i < numeroparticulas; i++) {
            particulas[i].interacciones(particulas);
            particulas[i].mueve();
            particulas[i].lineas();
            particulas[i].dibuja();
            particulas[i].rebote();
        }

        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",10)
      }
      
    </script>
  </body>
</html>
```

### movimiento aleatorio fuera

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{margin:0px;padding:0px;}
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
    
      function distance2D(x1, y1, x2, y2) {
            const dx = x2 - x1;
            const dy = y2 - y1;
            return Math.sqrt(dx * dx + dy * dy);
        }
      function bounceAngle(incidentAngle, wallAngle) {
          const relative = incidentAngle - wallAngle;   // angle of incidence
          const reflectedRelative = -relative;          // mirror
          return reflectedRelative + wallAngle;         // return to world space
      }
      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas")
      let contexto = lienzo.getContext("2d")
      lienzo.width = anchura
      lienzo.height = altura
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";
      let nombres = ['Juan','Julia','Jorge','Jaime','Jose','Julian']
      
      class Particula{
          constructor(x,y,a){
              this.x = x;
              this.y = y;
              this.a = a;
              this.v = 0.5
              this.texto = nombres[Math.floor(Math.random()*nombres.length)]
          }
          dibuja(){
              let anchopastilla = 20
              let altopastilla = 10
              contexto.strokeStyle = "black"
              contexto.beginPath();
              contexto.moveTo(this.x-anchopastilla,this.y-altopastilla)
              contexto.lineTo(this.x+anchopastilla,this.y-altopastilla)
              contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2)
              contexto.lineTo(this.x-anchopastilla,this.y+10)
              contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2)
              contexto.fillStyle = "white"
              contexto.strokeStyle = "black";
              contexto.fill();
              contexto.stroke()
              contexto.fillStyle = "black"
              contexto.fillText(this.texto,this.x,this.y)
          }
          lineas(){
            contexto.strokeStyle = "grey"
              for(let i = 0;i<numeroparticulas;i++){
                  if(distance2D(this.x, this.y, particulas[i].x, particulas[i].y) < 100){
                      contexto.beginPath();
                      contexto.moveTo(this.x,this.y);
                      contexto.lineTo(particulas[i].x, particulas[i].y);
                      contexto.stroke();
                  }
              }
          }
          mueve(){
              //this.a += (Math.random()-0.5) * 0.1;
              this.x += Math.cos(this.a)*this.v;
              this.y += Math.sin(this.a)*this.v;
          }

          rebote(){
              // Right wall
              if (this.x > anchura) {
                  this.x = anchura;
                  this.a = bounceAngle(this.a, Math.PI/2); // wall angle = vertical
              }
              // Left wall
              if (this.x < 0) {
                  this.x = 0;
                  this.a = bounceAngle(this.a, Math.PI/2);
              }

              // Bottom wall
              if (this.y > altura) {
                  this.y = altura;
                  this.a = bounceAngle(this.a, 0); // horizontal wall
              }
              // Top wall
              if (this.y < 0) {
                  this.y = 0;
                  this.a = bounceAngle(this.a, 0);
              }
          }
          interacciones(particulas) {
              let rango = 340;          // detection radius
              let fuerzaAtraccion = 0.03;
              let fuerzaRepulsion = 0.05;
              let distanciaMin = 135;    // ✔️ minimum spacing between same particles

              let ax = 0;
              let ay = 0;

              for (let p of particulas) {
                  if (p === this) continue;

                  let d = distance2D(this.x, this.y, p.x, p.y);
                  if (d > rango || d === 0) continue;

                  let dx = p.x - this.x;
                  let dy = p.y - this.y;

                  // Normalize direction
                  let ux = dx / d;
                  let uy = dy / d;

                  if (p.texto === this.texto) {

                      if (d > distanciaMin) {
                          // ✔️ Farther than minimum: attract
                          ax += ux;
                          ay += uy;
                      } else {
                          // ❌ Too close: gently push away
                          ax -= ux * 2;
                          ay -= uy * 2;
                      }

                  } else {
                      // ❌ Repel different text
                      ax -= ux * fuerzaRepulsion;
                      ay -= uy * fuerzaRepulsion;
                  }
              }

              // Apply steering
              if (ax !== 0 || ay !== 0) {
                  let targetAngle = Math.atan2(ay, ax);
                  let diff = targetAngle - this.a;
                  diff = Math.atan2(Math.sin(diff), Math.cos(diff)); // normalize
                  this.a += diff * fuerzaAtraccion;
              }
          }


      }

      let particulas = [];
      let numeroparticulas = 250
      
      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        )
      }
      let temporizador = setTimeout("bucle()",1000)
      function bucle(){
        contexto.clearRect(0,0,anchura,altura)
        // Las particulas
        for (let i = 0; i < numeroparticulas; i++) {
            particulas[i].interacciones(particulas);
            particulas[i].mueve();
            particulas[i].lineas();
            particulas[i].dibuja();
            particulas[i].rebote();
        }

        clearTimeout(temporizador)
        temporizador = setTimeout("bucle()",10)
      }
      
    </script>
  </body>
</html>
```

### busca de estabilidad

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{
        margin:0;
        padding:0;
        background:#ffffff;
      }
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
      function distance2D(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas");
      let contexto = lienzo.getContext("2d");
      lienzo.width = anchura;
      lienzo.height = altura;
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";

      let nombres = ['Juan','Julia','Jorge','Jaime','Jose','Julian'];

      class Particula{
        constructor(x,y,a){
          this.x = x;
          this.y = y;
          this.v = 0.5;        // velocidad base inicial
          // velocidad inicial a partir del ángulo
          this.vx = Math.cos(a) * this.v;
          this.vy = Math.sin(a) * this.v;

          // aceleración (fuerzas acumuladas)
          this.ax = 0;
          this.ay = 0;

          this.texto = nombres[Math.floor(Math.random()*nombres.length)];

          // control de estabilidad
          this.fija = false;
          this.estableFrames = 0;
        }

        dibuja(){
          let anchopastilla = 20;
          let altopastilla = 10;
          contexto.strokeStyle = "black";
          contexto.beginPath();
          contexto.moveTo(this.x-anchopastilla,this.y-altopastilla);
          contexto.lineTo(this.x+anchopastilla,this.y-altopastilla);
          contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2);
          contexto.lineTo(this.x-anchopastilla,this.y+10);
          contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2);
          contexto.fillStyle = "white";
          contexto.strokeStyle = "black";
          contexto.fill();
          contexto.stroke();
          contexto.fillStyle = "black";
          contexto.fillText(this.texto,this.x,this.y);
        }

        lineas(){
          for(let i = 0;i<numeroparticulas;i++){
            const p = particulas[i];
            if (p === this) continue;
            const d = distance2D(this.x, this.y, p.x, p.y);
            if(d < 140){ // rango visual de conexiones
              contexto.strokeStyle = "rgba(128,128,128,0.3)";
              contexto.beginPath();
              contexto.moveTo(this.x,this.y);
              contexto.lineTo(p.x, p.y);
              contexto.stroke();
            }
          }
        }

        interacciones(particulas) {
          if (this.fija) {
            // las partículas fijas no se mueven ni se recalculan fuerzas
            this.ax = 0;
            this.ay = 0;
            return;
          }

          // parámetros de interacción
          let rango = 80;              // radio de influencia general
          let distanciaObjetivo = 220;  // distancia "ideal" entre iguales
          let distanciaMinima = 40;     // distancia mínima para evitar solapamiento
          let kAtraccionIgual = 0.002;  // constante de "muelle" para iguales
          let kRepulsionDistinto = 0.003;
          let kRepulsionCorta = 0.05;   // repulsión fuerte a muy corta distancia

          let fx = 0;
          let fy = 0;

          for (let p of particulas) {
            if (p === this) continue;

            let d = distance2D(this.x, this.y, p.x, p.y);
            if (d === 0) continue;

            let dx = p.x - this.x;
            let dy = p.y - this.y;

            let ux = dx / d;
            let uy = dy / d;

            // repulsión fuerte para evitar solapamiento, independientemente del texto
            if (d < distanciaMinima) {
              let intensidad = (distanciaMinima - d) * kRepulsionCorta;
              fx -= ux * intensidad;
              fy -= uy * intensidad;
              continue;
            }

            if (d < rango) {
              if (p.texto === this.texto) {
                // "muelle" hacia distanciaObjetivo: si están más lejos, atrae; si más cerca, repele
                let delta = d - distanciaObjetivo;
                fx += ux * delta * kAtraccionIgual;
                fy += uy * delta * kAtraccionIgual;
              } else {
                // repulsión suave entre textos distintos
                let intensidad = (rango - d) * kRepulsionDistinto;
                fx -= ux * intensidad;
                fy -= uy * intensidad;
              }
            }
          }

          // limitar la fuerza total para evitar inestabilidades numéricas
          const maxForce = 0.05;
          let fmag = Math.sqrt(fx*fx + fy*fy);
          if (fmag > maxForce) {
            fx = fx / fmag * maxForce;
            fy = fy / fmag * maxForce;
          }

          this.ax = fx;
          this.ay = fy;
        }

        mueve(){
          if (this.fija) return;

          // integrar aceleración -> velocidad
          this.vx += this.ax;
          this.vy += this.ay;

          // fricción para que el sistema tienda a parar
          const friccion = 0.90;
          this.vx *= friccion;
          this.vy *= friccion;

          // integrar velocidad -> posición
          this.x += this.vx;
          this.y += this.vy;

          // comprobar estabilidad
          const speed = Math.sqrt(this.vx*this.vx + this.vy*this.vy);
          const fuerza = Math.sqrt(this.ax*this.ax + this.ay*this.ay);

          if (speed < 0.02 && fuerza < 0.002) {
            this.estableFrames++;
            // tras cierto número de frames casi sin fuerza ni velocidad, se fija
            if (this.estableFrames > 60) {
              this.fija = true;
              this.vx = 0;
              this.vy = 0;
            }
          } else {
            this.estableFrames = 0;
          }
        }

        rebote(){
          if (this.fija) return;

          // choque con paredes con rebote amortiguado
          const reboteFactor = -0.5; // rebote con pérdida de energía

          // paredes verticales
          if (this.x > anchura) {
            this.x = anchura;
            this.vx *= reboteFactor;
          }
          if (this.x < 0) {
            this.x = 0;
            this.vx *= reboteFactor;
          }

          // paredes horizontales
          if (this.y > altura) {
            this.y = altura;
            this.vy *= reboteFactor;
          }
          if (this.y < 0) {
            this.y = 0;
            this.vy *= reboteFactor;
          }
        }
      }

      let particulas = [];
      let numeroparticulas = 50;

      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        );
      }

      function bucle(){
        contexto.clearRect(0,0,anchura,altura);

        // primero calculamos fuerzas de interacción
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].interacciones(particulas);
        }

        // después actualizamos movimiento y dibujo
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].mueve();
          particulas[i].rebote();
        }

        // dibujar conexiones y partículas (separado para que el dibujo use posiciones ya actualizadas)
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].lineas();
        }
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].dibuja();
        }

        requestAnimationFrame(bucle);
      }

      // iniciar animación
      requestAnimationFrame(bucle);
    </script>
  </body>
</html>
```

### libertad para las partículas

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{
        margin:0;
        padding:0;
        background:#ffffff;
      }
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
      function distance2D(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas");
      let contexto = lienzo.getContext("2d");
      lienzo.width = anchura;
      lienzo.height = altura;
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";

      let nombres = ['Juan','Julia','Jorge','Jaime','Jose','Julian'];

      class Particula{
        constructor(x,y,a){
          this.x = x;
          this.y = y;
          this.v = 0.5;        // velocidad base inicial

          // velocidad inicial a partir del ángulo
          this.vx = Math.cos(a) * this.v;
          this.vy = Math.sin(a) * this.v;

          // aceleración (fuerzas acumuladas)
          this.ax = 0;
          this.ay = 0;

          this.texto = nombres[Math.floor(Math.random()*nombres.length)];

          // control de estabilidad
          this.fija = false;
          this.estableFrames = 0;
        }

        dibuja(){
          let anchopastilla = 20;
          let altopastilla = 10;
          contexto.strokeStyle = "black";
          contexto.beginPath();
          contexto.moveTo(this.x-anchopastilla,this.y-altopastilla);
          contexto.lineTo(this.x+anchopastilla,this.y-altopastilla);
          contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2);
          contexto.lineTo(this.x-anchopastilla,this.y+10);
          contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2);
          contexto.fillStyle = "white";
          contexto.strokeStyle = "black";
          contexto.fill();
          contexto.stroke();
          contexto.fillStyle = "black";
          contexto.fillText(this.texto,this.x,this.y);
        }

        lineas(){
          for(let i = 0;i<numeroparticulas;i++){
            const p = particulas[i];
            if (p === this) continue;
            const d = distance2D(this.x, this.y, p.x, p.y);
            if(d < 160){ // rango visual de conexiones
              contexto.strokeStyle = "rgba(128,128,128,0.3)";
              contexto.beginPath();
              contexto.moveTo(this.x,this.y);
              contexto.lineTo(p.x, p.y);
              contexto.stroke();
            }
          }
        }

        interacciones(particulas) {
          if (this.fija) {
            // las partículas fijas no se mueven ni se recalculan fuerzas
            this.ax = 0;
            this.ay = 0;
            return;
          }

          // radio de búsqueda: toda la pantalla (diagonal)
          let rangoGlobal = Math.sqrt(anchura*anchura + altura*altura);

          // parámetros de interacción
          let distanciaObjetivo = 120;         // distancia "ideal" entre iguales
          let distanciaMinima = 80;            // distancia mínima para evitar solapamiento
          let distanciaRepulsionDistinto = 200; // hasta aquí repelen distinto

          let kAtraccionIgual = 0.0012;       // muelle entre iguales
          let kRepulsionDistinto = 0.001;     // repulsión suave entre distintos
          let kRepulsionCorta = 0.06;         // repulsión fuerte muy cercana

          let fx = 0;
          let fy = 0;

          for (let p of particulas) {
            if (p === this) continue;

            let d = distance2D(this.x, this.y, p.x, p.y);
            if (d === 0 || d > rangoGlobal) continue;

            let dx = p.x - this.x;
            let dy = p.y - this.y;

            let ux = dx / d;
            let uy = dy / d;

            // repulsión fuerte para evitar solapamiento, independientemente del texto
            if (d < distanciaMinima) {
              let intensidad = (distanciaMinima - d) * kRepulsionCorta;
              fx -= ux * intensidad;
              fy -= uy * intensidad;
              continue;
            }

            if (p.texto === this.texto) {
              // atracción + ajuste hacia distanciaObjetivo
              let delta = d - distanciaObjetivo; // si d > objetivo, delta > 0 => atrae; si <, repele suave
              fx += ux * delta * kAtraccionIgual;
              fy += uy * delta * kAtraccionIgual;
            } else {
              // repulsión solo si está relativamente cerca
              if (d < distanciaRepulsionDistinto) {
                let intensidad = (distanciaRepulsionDistinto - d) * kRepulsionDistinto;
                fx -= ux * intensidad;
                fy -= uy * intensidad;
              }
            }
          }

          // limitar la fuerza total para evitar inestabilidades numéricas
          const maxForce = 0.05;
          let fmag = Math.sqrt(fx*fx + fy*fy);
          if (fmag > maxForce) {
            fx = fx / fmag * maxForce;
            fy = fy / fmag * maxForce;
          }

          this.ax = fx;
          this.ay = fy;
        }

        mueve(){
          if (this.fija) return;

          // integrar aceleración -> velocidad
          this.vx += this.ax;
          this.vy += this.ay;

          // fricción para que el sistema tienda a parar
          const friccion = 0.93;
          this.vx *= friccion;
          this.vy *= friccion;

          // integrar velocidad -> posición
          this.x += this.vx;
          this.y += this.vy;

          // comprobar estabilidad
          const speed = Math.sqrt(this.vx*this.vx + this.vy*this.vy);
          const fuerza = Math.sqrt(this.ax*this.ax + this.ay*this.ay);

          if (speed < 0.02 && fuerza < 0.002) {
            this.estableFrames++;
            // tras cierto número de frames casi sin fuerza ni velocidad, se fija
            if (this.estableFrames > 60) {
              this.fija = true;
              this.vx = 0;
              this.vy = 0;
            }
          } else {
            this.estableFrames = 0;
          }
        }

        rebote(){
          if (this.fija) return;

          // choque con paredes con rebote amortiguado
          const reboteFactor = -0.5; // rebote con pérdida de energía

          // paredes verticales
          if (this.x > anchura) {
            this.x = anchura;
            this.vx *= reboteFactor;
          }
          if (this.x < 0) {
            this.x = 0;
            this.vx *= reboteFactor;
          }

          // paredes horizontales
          if (this.y > altura) {
            this.y = altura;
            this.vy *= reboteFactor;
          }
          if (this.y < 0) {
            this.y = 0;
            this.vy *= reboteFactor;
          }
        }
      }

      let particulas = [];
      let numeroparticulas = 250;

      for(let i = 0;i<numeroparticulas;i++){
        particulas.push(
          new Particula(
            Math.random()*anchura,
            Math.random()*altura,
            Math.random()*Math.PI*2
          )
        );
      }

      function bucle(){
        contexto.clearRect(0,0,anchura,altura);

        // primero calculamos fuerzas de interacción
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].interacciones(particulas);
        }

        // después actualizamos movimiento y rebote
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].mueve();
          particulas[i].rebote();
        }

        // dibujar conexiones y partículas (con posiciones ya actualizadas)
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].lineas();
        }
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].dibuja();
        }

        requestAnimationFrame(bucle);
      }

      // iniciar animación
      requestAnimationFrame(bucle);
    </script>
  </body>
</html>
```

### asociacion por varios criterios

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{
        margin:0;
        padding:0;
        background:#ffffff;
      }
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
      function distance2D(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas");
      let contexto = lienzo.getContext("2d");
      lienzo.width = anchura;
      lienzo.height = altura;
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";

      let particulas = [];
      let numeroparticulas = 0;

      class Particula{
        // persona: { nombre, hobbie }
        constructor(x,y,a,persona){
          this.x = x;
          this.y = y;
          this.v = 0.5;        // velocidad base inicial

          // velocidad inicial a partir del ángulo
          this.vx = Math.cos(a) * this.v;
          this.vy = Math.sin(a) * this.v;

          // aceleración (fuerzas acumuladas)
          this.ax = 0;
          this.ay = 0;

          this.nombre = persona.nombre;
          this.hobbie = persona.hobbie;

          // control de estabilidad
          this.fija = false;
          this.estableFrames = 0;
        }

        dibuja(){
          let anchopastilla = 35;
          let altopastilla = 12;
          contexto.strokeStyle = "black";
          contexto.beginPath();
          contexto.moveTo(this.x-anchopastilla,this.y-altopastilla);
          contexto.lineTo(this.x+anchopastilla,this.y-altopastilla);
          contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2);
          contexto.lineTo(this.x-anchopastilla,this.y+altopastilla);
          contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2);
          contexto.fillStyle = "white";
          contexto.strokeStyle = "black";
          contexto.fill();
          contexto.stroke();
          contexto.fillStyle = "black";

          // primera línea: nombre
          contexto.fillText(this.nombre, this.x, this.y - 5);
          // segunda línea: hobbie (más pequeño visualmente si se quiere)
          contexto.font = "10px sans-serif";
          contexto.fillText(this.hobbie, this.x, this.y + 7);
          contexto.font = "12px sans-serif"; // restaurar tamaño por defecto
        }

        lineas(){
          for(let i = 0;i<numeroparticulas;i++){
            const p = particulas[i];
            if (p === this) continue;
            const d = distance2D(this.x, this.y, p.x, p.y);
            if(d < 160){ // rango visual de conexiones
              contexto.strokeStyle = "rgba(128,128,128,0.3)";
              contexto.beginPath();
              contexto.moveTo(this.x,this.y);
              contexto.lineTo(p.x, p.y);
              contexto.stroke();
            }
          }
        }

        interacciones(particulas) {
          if (this.fija) {
            this.ax = 0;
            this.ay = 0;
            return;
          }

          // radio de búsqueda: toda la pantalla (diagonal)
          let rangoGlobal = Math.sqrt(anchura*anchura + altura*altura);

          // parámetros de interacción
          let distanciaObjetivo = 120;         // distancia "ideal" entre iguales
          let distanciaMinima = 70;            // distancia mínima para evitar solapamiento
          let distanciaRepulsionDistinto = 220; // hasta aquí repelen distinto

          // factores según coincidencia
          let kAtraccionFuerte = 0.0015;  // mismo nombre + mismo hobbie
          let kAtraccionMedia  = 0.0009;  // mismo nombre o mismo hobbie
          let kRepulsionDistinto = 0.001; // repulsión suave entre distintos
          let kRepulsionCorta = 0.06;     // repulsión fuerte muy cercana

          let fx = 0;
          let fy = 0;

          for (let p of particulas) {
            if (p === this) continue;

            let d = distance2D(this.x, this.y, p.x, p.y);
            if (d === 0 || d > rangoGlobal) continue;

            let dx = p.x - this.x;
            let dy = p.y - this.y;

            let ux = dx / d;
            let uy = dy / d;

            // repulsión fuerte para evitar solapamiento
            if (d < distanciaMinima) {
              let intensidad = (distanciaMinima - d) * kRepulsionCorta;
              fx -= ux * intensidad;
              fy -= uy * intensidad;
              continue;
            }

            const mismoNombre = (p.nombre === this.nombre);
            const mismoHobbie = (p.hobbie === this.hobbie);

            if (mismoNombre && mismoHobbie) {
              // máxima atracción hacia una distancia objetivo
              let delta = d - distanciaObjetivo;
              fx += ux * delta * kAtraccionFuerte;
              fy += uy * delta * kAtraccionFuerte;

            } else if (mismoNombre || mismoHobbie) {
              // atracción media (comparten al menos un factor)
              let delta = d - distanciaObjetivo;
              fx += ux * delta * kAtraccionMedia;
              fy += uy * delta * kAtraccionMedia;

            } else {
              // repulsión entre completamente distintos (solo si están relativamente cerca)
              if (d < distanciaRepulsionDistinto) {
                let intensidad = (distanciaRepulsionDistinto - d) * kRepulsionDistinto;
                fx -= ux * intensidad;
                fy -= uy * intensidad;
              }
            }
          }

          // limitar la fuerza total
          const maxForce = 0.05;
          let fmag = Math.sqrt(fx*fx + fy*fy);
          if (fmag > maxForce) {
            fx = fx / fmag * maxForce;
            fy = fy / fmag * maxForce;
          }

          this.ax = fx;
          this.ay = fy;
        }

        mueve(){
          if (this.fija) return;

          this.vx += this.ax;
          this.vy += this.ay;

          const friccion = 0.93;
          this.vx *= friccion;
          this.vy *= friccion;

          this.x += this.vx;
          this.y += this.vy;

          const speed  = Math.sqrt(this.vx*this.vx + this.vy*this.vy);
          const fuerza = Math.sqrt(this.ax*this.ax + this.ay*this.ay);

          if (speed < 0.02 && fuerza < 0.002) {
            this.estableFrames++;
            if (this.estableFrames > 60) {
              this.fija = true;
              this.vx = 0;
              this.vy = 0;
            }
          } else {
            this.estableFrames = 0;
          }
        }

        rebote(){
          if (this.fija) return;

          const reboteFactor = -0.5;

          if (this.x > anchura) {
            this.x = anchura;
            this.vx *= reboteFactor;
          }
          if (this.x < 0) {
            this.x = 0;
            this.vx *= reboteFactor;
          }

          if (this.y > altura) {
            this.y = altura;
            this.vy *= reboteFactor;
          }
          if (this.y < 0) {
            this.y = 0;
            this.vy *= reboteFactor;
          }
        }
      }

      function bucle(){
        contexto.clearRect(0,0,anchura,altura);

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].interacciones(particulas);
        }

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].mueve();
          particulas[i].rebote();
        }

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].lineas();
        }
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].dibuja();
        }

        requestAnimationFrame(bucle);
      }

      // Cargar JSON y, cuando esté listo, crear partículas y arrancar simulación
      fetch("personas.json")
        .then(respuesta => respuesta.json())
        .then(personas => {
          particulas = [];
          numeroparticulas = personas.length;

          for (let i = 0; i < personas.length; i++) {
            let persona = personas[i];
            particulas.push(
              new Particula(
                Math.random()*anchura,
                Math.random()*altura,
                Math.random()*Math.PI*2,
                persona
              )
            );
          }

          requestAnimationFrame(bucle);
        })
        .catch(error => {
          console.error("Error al cargar personas.json:", error);
        });
    </script>
  </body>
</html>
```

### colores

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{
        margin:0;
        padding:0;
        background:#ffffff;
      }
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
      function distance2D(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      // Simple hash function for strings
      function hashString(str) {
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
          hash = (hash * 31 + str.charCodeAt(i)) | 0; // keep in 32 bits
        }
        return Math.abs(hash);
      }

      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas");
      let contexto = lienzo.getContext("2d");
      lienzo.width = anchura;
      lienzo.height = altura;
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";

      let particulas = [];
      let numeroparticulas = 0;

      class Particula{
        // persona: { nombre, hobbie }
        constructor(x,y,a,persona){
          this.x = x;
          this.y = y;
          this.v = 0.5;        // velocidad base inicial

          // velocidad inicial a partir del ángulo
          this.vx = Math.cos(a) * this.v;
          this.vy = Math.sin(a) * this.v;

          // aceleración (fuerzas acumuladas)
          this.ax = 0;
          this.ay = 0;

          this.nombre = persona.nombre;
          this.hobbie = persona.hobbie;

          // control de estabilidad
          this.fija = false;
          this.estableFrames = 0;
        }

        dibuja(){
          let anchopastilla = 35;
          let altopastilla = 12;
          contexto.strokeStyle = "black";
          contexto.beginPath();
          contexto.moveTo(this.x-anchopastilla,this.y-altopastilla);
          contexto.lineTo(this.x+anchopastilla,this.y-altopastilla);
          contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2);
          contexto.lineTo(this.x-anchopastilla,this.y+altopastilla);
          contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2);
          contexto.fillStyle = "white";
          contexto.strokeStyle = "black";
          contexto.fill();
          contexto.stroke();
          contexto.fillStyle = "black";

          // primera línea: nombre
          contexto.font = "12px sans-serif";
          contexto.fillText(this.nombre, this.x, this.y - 5);
          // segunda línea: hobbie
          contexto.font = "10px sans-serif";
          contexto.fillText(this.hobbie, this.x, this.y + 7);
        }

        lineas(){
          for(let i = 0;i<numeroparticulas;i++){
            const p = particulas[i];
            if (p === this) continue;
            const d = distance2D(this.x, this.y, p.x, p.y);
            if(d < 160){

              const mismoNombre = (p.nombre === this.nombre);
              const mismoHobbie = (p.hobbie === this.hobbie);

              // claves de relación
              let key = "ninguno";
              if (mismoNombre && mismoHobbie) key = "ambos";
              else if (mismoNombre) key = "nombre";
              else if (mismoHobbie) key = "hobbie";

              // hash → color hue
              const h = hashString(key) % 360;
              const alpha = 0.30 + 0.5 * (1 - d / 160);

              contexto.strokeStyle = `hsla(${h}, 70%, 50%, ${alpha})`;
              contexto.beginPath();
              contexto.moveTo(this.x,this.y);
              contexto.lineTo(p.x, p.y);
              contexto.stroke();
            }
          }
        }


        interacciones(particulas) {
          if (this.fija) {
            this.ax = 0;
            this.ay = 0;
            return;
          }

          // radio de búsqueda: toda la pantalla (diagonal)
          let rangoGlobal = Math.sqrt(anchura*anchura + altura*altura);

          // parámetros de interacción
          let distanciaObjetivo = 120;         // distancia "ideal" entre iguales
          let distanciaMinima = 70;            // distancia mínima para evitar solapamiento
          let distanciaRepulsionDistinto = 220; // hasta aquí repelen distinto

          // factores según coincidencia
          let kAtraccionFuerte = 0.0015;  // mismo nombre + mismo hobbie
          let kAtraccionMedia  = 0.0009;  // mismo nombre o mismo hobbie
          let kRepulsionDistinto = 0.001; // repulsión suave entre distintos
          let kRepulsionCorta = 0.06;     // repulsión fuerte muy cercana

          let fx = 0;
          let fy = 0;

          for (let p of particulas) {
            if (p === this) continue;

            let d = distance2D(this.x, this.y, p.x, p.y);
            if (d === 0 || d > rangoGlobal) continue;

            let dx = p.x - this.x;
            let dy = p.y - this.y;

            let ux = dx / d;
            let uy = dy / d;

            // repulsión fuerte para evitar solapamiento
            if (d < distanciaMinima) {
              let intensidad = (distanciaMinima - d) * kRepulsionCorta;
              fx -= ux * intensidad;
              fy -= uy * intensidad;
              continue;
            }

            const mismoNombre = (p.nombre === this.nombre);
            const mismoHobbie = (p.hobbie === this.hobbie);

            if (mismoNombre && mismoHobbie) {
              // máxima atracción hacia una distancia objetivo
              let delta = d - distanciaObjetivo;
              fx += ux * delta * kAtraccionFuerte;
              fy += uy * delta * kAtraccionFuerte;

            } else if (mismoNombre || mismoHobbie) {
              // atracción media (comparten al menos un factor)
              let delta = d - distanciaObjetivo;
              fx += ux * delta * kAtraccionMedia;
              fy += uy * delta * kAtraccionMedia;

            } else {
              // repulsión entre completamente distintos
              if (d < distanciaRepulsionDistinto) {
                let intensidad = (distanciaRepulsionDistinto - d) * kRepulsionDistinto;
                fx -= ux * intensidad;
                fy -= uy * intensidad;
              }
            }
          }

          // limitar la fuerza total
          const maxForce = 0.05;
          let fmag = Math.sqrt(fx*fx + fy*fy);
          if (fmag > maxForce) {
            fx = fx / fmag * maxForce;
            fy = fy / fmag * maxForce;
          }

          this.ax = fx;
          this.ay = fy;
        }

        mueve(){
          if (this.fija) return;

          this.vx += this.ax;
          this.vy += this.ay;

          const friccion = 0.93;
          this.vx *= friccion;
          this.vy *= friccion;

          this.x += this.vx;
          this.y += this.vy;

          const speed  = Math.sqrt(this.vx*this.vx + this.vy*this.vy);
          const fuerza = Math.sqrt(this.ax*this.ax + this.ay*this.ay);

          if (speed < 0.02 && fuerza < 0.002) {
            this.estableFrames++;
            if (this.estableFrames > 60) {
              this.fija = true;
              this.vx = 0;
              this.vy = 0;
            }
          } else {
            this.estableFrames = 0;
          }
        }

        rebote(){
          if (this.fija) return;

          const reboteFactor = -0.5;

          if (this.x > anchura) {
            this.x = anchura;
            this.vx *= reboteFactor;
          }
          if (this.x < 0) {
            this.x = 0;
            this.vx *= reboteFactor;
          }

          if (this.y > altura) {
            this.y = altura;
            this.vy *= reboteFactor;
          }
          if (this.y < 0) {
            this.y = 0;
            this.vy *= reboteFactor;
          }
        }
      }

      function bucle(){
        contexto.clearRect(0,0,anchura,altura);

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].interacciones(particulas);
        }

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].mueve();
          particulas[i].rebote();
        }

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].lineas();
        }
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].dibuja();
        }

        requestAnimationFrame(bucle);
      }

      // Cargar JSON y, cuando esté listo, crear partículas y arrancar simulación
      fetch("personas.json")
        .then(respuesta => respuesta.json())
        .then(personas => {
          particulas = [];
          numeroparticulas = personas.length;

          for (let i = 0; i < personas.length; i++) {
            let persona = personas[i];
            particulas.push(
              new Particula(
                Math.random()*anchura,
                Math.random()*altura,
                Math.random()*Math.PI*2,
                persona
              )
            );
          }

          requestAnimationFrame(bucle);
        })
        .catch(error => {
          console.error("Error al cargar personas.json:", error);
        });
    </script>
  </body>
</html>
```

### anchuras de lineas

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{
        margin:0;
        padding:0;
        background:#ffffff;
      }
    </style>
  </head>
  <body>
    <canvas></canvas>
    <script>
      function distance2D(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      // Simple hash function for strings
      function hashString(str) {
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
          hash = (hash * 31 + str.charCodeAt(i)) | 0; // keep in 32 bits
        }
        return Math.abs(hash);
      }

      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas");
      let contexto = lienzo.getContext("2d");
      lienzo.width = anchura;
      lienzo.height = altura;
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";
      

      let particulas = [];
      let numeroparticulas = 0;

      class Particula{
        // persona: { nombre, hobbie }
        constructor(x,y,a,persona){
          this.x = x;
          this.y = y;
          this.v = 0.5;        // velocidad base inicial

          // velocidad inicial a partir del ángulo
          this.vx = Math.cos(a) * this.v;
          this.vy = Math.sin(a) * this.v;

          // aceleración (fuerzas acumuladas)
          this.ax = 0;
          this.ay = 0;

          this.nombre = persona.nombre;
          this.hobbie = persona.hobbie;

          // control de estabilidad
          this.fija = false;
          this.estableFrames = 0;
        }

        dibuja(){
        contexto.lineWidth = 1;
          let anchopastilla = 35;
          let altopastilla = 12;
          contexto.strokeStyle = "black";
          contexto.beginPath();
          contexto.moveTo(this.x-anchopastilla,this.y-altopastilla);
          contexto.lineTo(this.x+anchopastilla,this.y-altopastilla);
          contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2);
          contexto.lineTo(this.x-anchopastilla,this.y+altopastilla);
          contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2);
          contexto.fillStyle = "white";
          contexto.strokeStyle = "black";
          contexto.fill();
          contexto.stroke();
          contexto.fillStyle = "black";

          // primera línea: nombre
          contexto.font = "12px sans-serif";
          contexto.fillText(this.nombre, this.x, this.y - 5);
          // segunda línea: hobbie
          contexto.font = "10px sans-serif";
          contexto.fillText(this.hobbie, this.x, this.y + 7);
        }

        lineas(){
        contexto.lineWidth = 5;
          for(let i = 0;i<numeroparticulas;i++){
            const p = particulas[i];
            if (p === this) continue;
            const d = distance2D(this.x, this.y, p.x, p.y);
            if(d < 160){

              const mismoNombre = (p.nombre === this.nombre);
              const mismoHobbie = (p.hobbie === this.hobbie);

              // claves de relación
              let key = "ninguno";
              if (mismoNombre && mismoHobbie) key = "ambos";
              else if (mismoNombre) key = "nombre";
              else if (mismoHobbie) key = "hobbie";

              // hash → color hue
              const h = hashString(key) % 360;
              const alpha = 0.30 + 0.5 * (1 - d / 160);

              contexto.strokeStyle = `hsla(${h}, 70%, 50%, ${alpha})`;
              contexto.beginPath();
              contexto.moveTo(this.x,this.y);
              contexto.lineTo(p.x, p.y);
              contexto.stroke();
            }
          }
        }


        interacciones(particulas) {
          if (this.fija) {
            this.ax = 0;
            this.ay = 0;
            return;
          }

          // radio de búsqueda: toda la pantalla (diagonal)
          let rangoGlobal = Math.sqrt(anchura*anchura + altura*altura);

          // parámetros de interacción
          let distanciaObjetivo = 120;         // distancia "ideal" entre iguales
          let distanciaMinima = 70;            // distancia mínima para evitar solapamiento
          let distanciaRepulsionDistinto = 220; // hasta aquí repelen distinto

          // factores según coincidencia
          let kAtraccionFuerte = 0.0015;  // mismo nombre + mismo hobbie
          let kAtraccionMedia  = 0.0009;  // mismo nombre o mismo hobbie
          let kRepulsionDistinto = 0.001; // repulsión suave entre distintos
          let kRepulsionCorta = 0.06;     // repulsión fuerte muy cercana

          let fx = 0;
          let fy = 0;

          for (let p of particulas) {
            if (p === this) continue;

            let d = distance2D(this.x, this.y, p.x, p.y);
            if (d === 0 || d > rangoGlobal) continue;

            let dx = p.x - this.x;
            let dy = p.y - this.y;

            let ux = dx / d;
            let uy = dy / d;

            // repulsión fuerte para evitar solapamiento
            if (d < distanciaMinima) {
              let intensidad = (distanciaMinima - d) * kRepulsionCorta;
              fx -= ux * intensidad;
              fy -= uy * intensidad;
              continue;
            }

            const mismoNombre = (p.nombre === this.nombre);
            const mismoHobbie = (p.hobbie === this.hobbie);

            if (mismoNombre && mismoHobbie) {
              // máxima atracción hacia una distancia objetivo
              let delta = d - distanciaObjetivo;
              fx += ux * delta * kAtraccionFuerte;
              fy += uy * delta * kAtraccionFuerte;

            } else if (mismoNombre || mismoHobbie) {
              // atracción media (comparten al menos un factor)
              let delta = d - distanciaObjetivo;
              fx += ux * delta * kAtraccionMedia;
              fy += uy * delta * kAtraccionMedia;

            } else {
              // repulsión entre completamente distintos
              if (d < distanciaRepulsionDistinto) {
                let intensidad = (distanciaRepulsionDistinto - d) * kRepulsionDistinto;
                fx -= ux * intensidad;
                fy -= uy * intensidad;
              }
            }
          }

          // limitar la fuerza total
          const maxForce = 0.05;
          let fmag = Math.sqrt(fx*fx + fy*fy);
          if (fmag > maxForce) {
            fx = fx / fmag * maxForce;
            fy = fy / fmag * maxForce;
          }

          this.ax = fx;
          this.ay = fy;
        }

        mueve(){
          if (this.fija) return;

          this.vx += this.ax;
          this.vy += this.ay;

          const friccion = 0.93;
          this.vx *= friccion;
          this.vy *= friccion;

          this.x += this.vx;
          this.y += this.vy;

          const speed  = Math.sqrt(this.vx*this.vx + this.vy*this.vy);
          const fuerza = Math.sqrt(this.ax*this.ax + this.ay*this.ay);

          if (speed < 0.02 && fuerza < 0.002) {
            this.estableFrames++;
            if (this.estableFrames > 60) {
              this.fija = true;
              this.vx = 0;
              this.vy = 0;
            }
          } else {
            this.estableFrames = 0;
          }
        }

        rebote(){
          if (this.fija) return;

          const reboteFactor = -0.5;

          if (this.x > anchura) {
            this.x = anchura;
            this.vx *= reboteFactor;
          }
          if (this.x < 0) {
            this.x = 0;
            this.vx *= reboteFactor;
          }

          if (this.y > altura) {
            this.y = altura;
            this.vy *= reboteFactor;
          }
          if (this.y < 0) {
            this.y = 0;
            this.vy *= reboteFactor;
          }
        }
      }

      function bucle(){
        contexto.clearRect(0,0,anchura,altura);

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].interacciones(particulas);
        }

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].mueve();
          particulas[i].rebote();
        }

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].lineas();
        }
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].dibuja();
        }

        requestAnimationFrame(bucle);
      }

      // Cargar JSON y, cuando esté listo, crear partículas y arrancar simulación
      fetch("personas.json")
        .then(respuesta => respuesta.json())
        .then(personas => {
          particulas = [];
          numeroparticulas = personas.length;

          for (let i = 0; i < personas.length; i++) {
            let persona = personas[i];
            particulas.push(
              new Particula(
                Math.random()*anchura,
                Math.random()*altura,
                Math.random()*Math.PI*2,
                persona
              )
            );
          }

          requestAnimationFrame(bucle);
        })
        .catch(error => {
          console.error("Error al cargar personas.json:", error);
        });
    </script>
  </body>
</html>
```

### anchura variable

```html
<!doctype html>
<html>
  <head>
    <style>
      body,html{
        margin:0;
        padding:0;
        background:#ffffff;
        font-family: sans-serif;
      }
      #controls{
        position:fixed;
        top:10px;
        left:10px;
        padding:8px 10px;
        background:rgba(255,255,255,0.9);
        border:1px solid #ccc;
        border-radius:4px;
        font-size:12px;
        z-index:10;
      }
      #controls label{
        display:block;
        margin-bottom:4px;
      }
      #controls input[type=range]{
        width:150px;
      }
      #controls span.value{
        display:inline-block;
        width:24px;
        text-align:right;
        margin-left:4px;
      }
    </style>
  </head>
  <body>
    <div id="controls">
      <label>
        Min thickness
        <input id="minThickness" type="range" min="1" max="10" value="1">
        <span id="minThicknessValue" class="value">1</span>
      </label>
      <label>
        Max thickness
        <input id="maxThickness" type="range" min="1" max="20" value="6">
        <span id="maxThicknessValue" class="value">6</span>
      </label>
    </div>

    <canvas></canvas>

    <script>
      function distance2D(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        return Math.sqrt(dx * dx + dy * dy);
      }

      // Simple hash function for strings
      function hashString(str) {
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
          hash = (hash * 31 + str.charCodeAt(i)) | 0; // keep in 32 bits
        }
        return Math.abs(hash);
      }

      let anchura = window.innerWidth;
      let altura = window.innerHeight;
      let lienzo = document.querySelector("canvas");
      let contexto = lienzo.getContext("2d");
      lienzo.width = anchura;
      lienzo.height = altura;
      contexto.textAlign = "center";
      contexto.textBaseline = "middle";

      // Global line thickness controls
      let minLineThickness = 1;
      let maxLineThickness = 6;

      const minSlider = document.getElementById("minThickness");
      const maxSlider = document.getElementById("maxThickness");
      const minValueSpan = document.getElementById("minThicknessValue");
      const maxValueSpan = document.getElementById("maxThicknessValue");

      minSlider.addEventListener("input", () => {
        minLineThickness = parseFloat(minSlider.value);
        minValueSpan.textContent = minSlider.value;

        // Ensure min <= max
        if (minLineThickness > maxLineThickness) {
          maxLineThickness = minLineThickness;
          maxSlider.value = maxLineThickness;
          maxValueSpan.textContent = maxLineThickness;
        }
      });

      maxSlider.addEventListener("input", () => {
        maxLineThickness = parseFloat(maxSlider.value);
        maxValueSpan.textContent = maxSlider.value;

        // Ensure max >= min
        if (maxLineThickness < minLineThickness) {
          minLineThickness = maxLineThickness;
          minSlider.value = minLineThickness;
          minValueSpan.textContent = minLineThickness;
        }
      });

      let particulas = [];
      let numeroparticulas = 0;

      class Particula{
        // persona: { nombre, hobbie }
        constructor(x,y,a,persona){
          this.x = x;
          this.y = y;
          this.v = 0.5;        // velocidad base inicial

          // velocidad inicial a partir del ángulo
          this.vx = Math.cos(a) * this.v;
          this.vy = Math.sin(a) * this.v;

          // aceleración (fuerzas acumuladas)
          this.ax = 0;
          this.ay = 0;

          this.nombre = persona.nombre;
          this.hobbie = persona.hobbie;

          // control de estabilidad
          this.fija = false;
          this.estableFrames = 0;
        }

        dibuja(){
          contexto.lineWidth = 1;
          contexto.lineCap = "butt";
          let anchopastilla = 35;
          let altopastilla = 12;
          contexto.strokeStyle = "black";
          contexto.beginPath();
          contexto.moveTo(this.x-anchopastilla,this.y-altopastilla);
          contexto.lineTo(this.x+anchopastilla,this.y-altopastilla);
          contexto.arc(this.x+anchopastilla,this.y,altopastilla,0-Math.PI/2,Math.PI-Math.PI/2);
          contexto.lineTo(this.x-anchopastilla,this.y+altopastilla);
          contexto.arc(this.x-anchopastilla,this.y,altopastilla,Math.PI-Math.PI/2,0-Math.PI/2);
          contexto.fillStyle = "white";
          contexto.strokeStyle = "black";
          contexto.fill();
          contexto.stroke();
          contexto.fillStyle = "black";

          // primera línea: nombre
          contexto.font = "12px sans-serif";
          contexto.fillText(this.nombre, this.x, this.y - 5);
          // segunda línea: hobbie
          contexto.font = "10px sans-serif";
          contexto.fillText(this.hobbie, this.x, this.y + 7);
        }

        lineas(){
          // Thickness varies smoothly along each connection:
          // maxLineThickness at the ends, minLineThickness at the middle.
          contexto.lineCap = "round";

          for(let i = 0; i < numeroparticulas; i++){
            const p = particulas[i];
            if (p === this) continue;

            const d = distance2D(this.x, this.y, p.x, p.y);
            if (d < 160){

              const mismoNombre = (p.nombre === this.nombre);
              const mismoHobbie = (p.hobbie === this.hobbie);

              // Tipo de relación -> key
              let key = "ninguno";
              if (mismoNombre && mismoHobbie) key = "ambos";
              else if (mismoNombre)          key = "nombre";
              else if (mismoHobbie)          key = "hobbie";

              // hash → color hue
              const h = hashString(key) % 360;
              const alpha = 0.30 + 0.5 * (1 - d / 160); // más cerca -> más opaco
              contexto.strokeStyle = `hsla(${h}, 70%, 50%, ${alpha})`;

              // Coordenadas de extremo a extremo
              const x1 = this.x;
              const y1 = this.y;
              const x2 = p.x;
              const y2 = p.y;

              // Número de segmentos para el gradiente de grosor
              const segments = 20; // sube/baja para más/menos suavidad

              for (let s = 0; s < segments; s++) {
                const t1 = s / segments;
                const t2 = (s + 1) / segments;

                // puntos extremos del segmento [t1, t2]
                const sx1 = x1 + (x2 - x1) * t1;
                const sy1 = y1 + (y2 - y1) * t1;
                const sx2 = x1 + (x2 - x1) * t2;
                const sy2 = y1 + (y2 - y1) * t2;

                // t central del segmento
                const tc = (t1 + t2) / 2;

                // Grosor: max en los extremos (t≈0 o t≈1), min en el centro (t≈0.5)
                // f(tc) = 4*(tc-0.5)^2 va de 1 en extremos a 0 en el centro
                const factor = 4 * (tc - 0.5) * (tc - 0.5); // [0,1]
                const w = minLineThickness + (maxLineThickness - minLineThickness) * factor;

                contexto.lineWidth = w;
                contexto.beginPath();
                contexto.moveTo(sx1, sy1);
                contexto.lineTo(sx2, sy2);
                contexto.stroke();
              }
            }
          }
        }


        interacciones(particulas) {
          if (this.fija) {
            this.ax = 0;
            this.ay = 0;
            return;
          }

          // radio de búsqueda: toda la pantalla (diagonal)
          let rangoGlobal = Math.sqrt(anchura*anchura + altura*altura);

          // parámetros de interacción
          let distanciaObjetivo = 120;         // distancia "ideal" entre iguales
          let distanciaMinima = 70;            // distancia mínima para evitar solapamiento
          let distanciaRepulsionDistinto = 220; // hasta aquí repelen distinto

          // factores según coincidencia
          let kAtraccionFuerte = 0.0015;  // mismo nombre + mismo hobbie
          let kAtraccionMedia  = 0.0009;  // mismo nombre o mismo hobbie
          let kRepulsionDistinto = 0.001; // repulsión suave entre distintos
          let kRepulsionCorta = 0.06;     // repulsión fuerte muy cercana

          let fx = 0;
          let fy = 0;

          for (let p of particulas) {
            if (p === this) continue;

            let d = distance2D(this.x, this.y, p.x, p.y);
            if (d === 0 || d > rangoGlobal) continue;

            let dx = p.x - this.x;
            let dy = p.y - this.y;

            let ux = dx / d;
            let uy = dy / d;

            // repulsión fuerte para evitar solapamiento
            if (d < distanciaMinima) {
              let intensidad = (distanciaMinima - d) * kRepulsionCorta;
              fx -= ux * intensidad;
              fy -= uy * intensidad;
              continue;
            }

            const mismoNombre = (p.nombre === this.nombre);
            const mismoHobbie = (p.hobbie === this.hobbie);

            if (mismoNombre && mismoHobbie) {
              // máxima atracción hacia una distancia objetivo
              let delta = d - distanciaObjetivo;
              fx += ux * delta * kAtraccionFuerte;
              fy += uy * delta * kAtraccionFuerte;

            } else if (mismoNombre || mismoHobbie) {
              // atracción media (comparten al menos un factor)
              let delta = d - distanciaObjetivo;
              fx += ux * delta * kAtraccionMedia;
              fy += uy * delta * kAtraccionMedia;

            } else {
              // repulsión entre completamente distintos
              if (d < distanciaRepulsionDistinto) {
                let intensidad = (distanciaRepulsionDistinto - d) * kRepulsionDistinto;
                fx -= ux * intensidad;
                fy -= uy * intensidad;
              }
            }
          }

          // limitar la fuerza total
          const maxForce = 0.05;
          let fmag = Math.sqrt(fx*fx + fy*fy);
          if (fmag > maxForce) {
            fx = fx / fmag * maxForce;
            fy = fy / fmag * maxForce;
          }

          this.ax = fx;
          this.ay = fy;
        }

        mueve(){
          if (this.fija) return;

          this.vx += this.ax;
          this.vy += this.ay;

          const friccion = 0.93;
          this.vx *= friccion;
          this.vy *= friccion;

          this.x += this.vx;
          this.y += this.vy;

          const speed  = Math.sqrt(this.vx*this.vx + this.vy*this.vy);
          const fuerza = Math.sqrt(this.ax*this.ax + this.ay*this.ay);

          if (speed < 0.02 && fuerza < 0.002) {
            this.estableFrames++;
            if (this.estableFrames > 60) {
              this.fija = true;
              this.vx = 0;
              this.vy = 0;
            }
          } else {
            this.estableFrames = 0;
          }
        }

        rebote(){
          if (this.fija) return;

          const reboteFactor = -0.5;

          if (this.x > anchura) {
            this.x = anchura;
            this.vx *= reboteFactor;
          }
          if (this.x < 0) {
            this.x = 0;
            this.vx *= reboteFactor;
          }

          if (this.y > altura) {
            this.y = altura;
            this.vy *= reboteFactor;
          }
          if (this.y < 0) {
            this.y = 0;
            this.vy *= reboteFactor;
          }
        }
      }

      function bucle(){
        contexto.clearRect(0,0,anchura,altura);

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].interacciones(particulas);
        }

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].mueve();
          particulas[i].rebote();
        }

        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].lineas();
        }
        for (let i = 0; i < numeroparticulas; i++) {
          particulas[i].dibuja();
        }

        requestAnimationFrame(bucle);
      }

      // Cargar JSON y, cuando esté listo, crear partículas y arrancar simulación
      fetch("personas.json")
        .then(respuesta => respuesta.json())
        .then(personas => {
          particulas = [];
          numeroparticulas = personas.length;

          for (let i = 0; i < personas.length; i++) {
            let persona = personas[i];
            particulas.push(
              new Particula(
                Math.random()*anchura,
                Math.random()*altura,
                Math.random()*Math.PI*2,
                persona
              )
            );
          }

          requestAnimationFrame(bucle);
        })
        .catch(error => {
          console.error("Error al cargar personas.json:", error);
        });
    </script>
  </body>
</html>
```

### personas

```json
[
  { "nombre": "Juan",   "hobbie": "Ajedrez" },
  { "nombre": "Juan",   "hobbie": "Pintura" },
  { "nombre": "Juan",   "hobbie": "Fútbol" },
  { "nombre": "Juan",   "hobbie": "Música" },
  { "nombre": "Juan",   "hobbie": "Lectura" },
  { "nombre": "Juan",   "hobbie": "Cine" },

  { "nombre": "Julia",  "hobbie": "Ajedrez" },
  { "nombre": "Julia",  "hobbie": "Pintura" },
  { "nombre": "Julia",  "hobbie": "Fútbol" },
  { "nombre": "Julia",  "hobbie": "Música" },
  { "nombre": "Julia",  "hobbie": "Lectura" },
  { "nombre": "Julia",  "hobbie": "Cine" },

  { "nombre": "Jorge",  "hobbie": "Ajedrez" },
  { "nombre": "Jorge",  "hobbie": "Pintura" },
  { "nombre": "Jorge",  "hobbie": "Fútbol" },
  { "nombre": "Jorge",  "hobbie": "Música" },
  { "nombre": "Jorge",  "hobbie": "Lectura" },
  { "nombre": "Jorge",  "hobbie": "Cine" },

  { "nombre": "Jaime",  "hobbie": "Ajedrez" },
  { "nombre": "Jaime",  "hobbie": "Pintura" },
  { "nombre": "Jaime",  "hobbie": "Fútbol" },
  { "nombre": "Jaime",  "hobbie": "Música" },
  { "nombre": "Jaime",  "hobbie": "Lectura" },
  { "nombre": "Jaime",  "hobbie": "Cine" },

  { "nombre": "Jose",   "hobbie": "Ajedrez" },
  { "nombre": "Jose",   "hobbie": "Pintura" },
  { "nombre": "Jose",   "hobbie": "Fútbol" },
  { "nombre": "Jose",   "hobbie": "Música" },
  { "nombre": "Jose",   "hobbie": "Lectura" },
  { "nombre": "Jose",   "hobbie": "Cine" },

  { "nombre": "Julian", "hobbie": "Ajedrez" },
  { "nombre": "Julian", "hobbie": "Pintura" },
  { "nombre": "Julian", "hobbie": "Fútbol" },
  { "nombre": "Julian", "hobbie": "Música" },
  { "nombre": "Julian", "hobbie": "Lectura" },
  { "nombre": "Julian", "hobbie": "Cine" },

  { "nombre": "Laura",  "hobbie": "Ajedrez" },
  { "nombre": "Laura",  "hobbie": "Pintura" },
  { "nombre": "Laura",  "hobbie": "Fútbol" },
  { "nombre": "Laura",  "hobbie": "Música" },
  { "nombre": "Laura",  "hobbie": "Lectura" },
  { "nombre": "Laura",  "hobbie": "Cine" },

  { "nombre": "Luis",   "hobbie": "Ajedrez" },
  { "nombre": "Luis",   "hobbie": "Pintura" },
  { "nombre": "Luis",   "hobbie": "Fútbol" },
  { "nombre": "Luis",   "hobbie": "Música" },
  { "nombre": "Luis",   "hobbie": "Lectura" },
  { "nombre": "Luis",   "hobbie": "Cine" },

  { "nombre": "Lucía",  "hobbie": "Ajedrez" },
  { "nombre": "Lucía",  "hobbie": "Pintura" },
  { "nombre": "Lucía",  "hobbie": "Fútbol" },
  { "nombre": "Lucía",  "hobbie": "Música" },
  { "nombre": "Lucía",  "hobbie": "Lectura" },
  { "nombre": "Lucía",  "hobbie": "Cine" },

  { "nombre": "Leo",    "hobbie": "Ajedrez" },
  { "nombre": "Leo",    "hobbie": "Pintura" },
  { "nombre": "Leo",    "hobbie": "Fútbol" },
  { "nombre": "Leo",    "hobbie": "Música" },
  { "nombre": "Leo",    "hobbie": "Lectura" },
  { "nombre": "Leo",    "hobbie": "Cine" },

  { "nombre": "Lola",   "hobbie": "Ajedrez" },
  { "nombre": "Lola",   "hobbie": "Pintura" },
  { "nombre": "Lola",   "hobbie": "Fútbol" },
  { "nombre": "Lola",   "hobbie": "Música" },
  { "nombre": "Lola",   "hobbie": "Lectura" },
  { "nombre": "Lola",   "hobbie": "Cine" },

  { "nombre": "Andrés", "hobbie": "Ajedrez" },
  { "nombre": "Andrés", "hobbie": "Pintura" },
  { "nombre": "Andrés", "hobbie": "Fútbol" },
  { "nombre": "Andrés", "hobbie": "Música" },
  { "nombre": "Andrés", "hobbie": "Lectura" },
  { "nombre": "Andrés", "hobbie": "Cine" },

  { "nombre": "Ana",    "hobbie": "Ajedrez" },
  { "nombre": "Ana",    "hobbie": "Pintura" },
  { "nombre": "Ana",    "hobbie": "Fútbol" },
  { "nombre": "Ana",    "hobbie": "Música" },
  { "nombre": "Ana",    "hobbie": "Lectura" },
  { "nombre": "Ana",    "hobbie": "Cine" },

  { "nombre": "Pablo",  "hobbie": "Ajedrez" },
  { "nombre": "Pablo",  "hobbie": "Pintura" },
  { "nombre": "Pablo",  "hobbie": "Fútbol" },
  { "nombre": "Pablo",  "hobbie": "Música" },
  { "nombre": "Pablo",  "hobbie": "Lectura" },
  { "nombre": "Pablo",  "hobbie": "Cine" }
]
```

<a id="componentes-de-los-objetos"></a>
## Componentes de los objetos

En el desarrollo de juegos 2D y 3D, los componentes de los objetos son fundamentales para su estructura y funcionalidad. Estos componentes pueden variar desde las propiedades básicas como la posición y la rotación hasta elementos más complejos como físicas, animaciones y colisiones.

La primera categoría de componentes es aquellas que definen la apariencia del objeto. En el caso de los juegos 2D, esto puede incluir imágenes o sprites, mientras que en los 3D, implicaría modelos tridimensionales. Cada uno de estos componentes tiene propiedades específicas que pueden ser modificadas para alterar su visualización, como la escala, el color y las texturas.

Los componentes físicos son otro aspecto crucial en el desarrollo de juegos, especialmente cuando se requiere interacción entre objetos. Estos componentes permiten simular comportamientos reales como gravedad, choques y rebotes, añadiendo profundidad a la experiencia del juego. La implementación de estos componentes puede variar dependiendo del motor de juegos utilizado, pero generalmente implican la definición de propiedades como masa, fricción y coeficiente de restitución.

Las animaciones son otro componente fundamental en los juegos 2D y 3D, ya que permiten a los objetos cambiar su estado visual con el tiempo. En los juegos 2D, esto puede implicar la creación de secuencias de sprites o la utilización de gráficos vectoriales. En los 3D, las animaciones pueden ser más complejas y pueden involucrar la manipulación de modelos tridimensionales en tiempo real.

Los componentes de entrada son otro aspecto importante en el desarrollo de juegos, ya que permiten a los jugadores interactuar con los objetos del juego. Esto puede incluir la detección de eventos como clics o pulsaciones de teclas, y la asociación de estas acciones con comportamientos específicos dentro del juego.

Los componentes de control son aquellos que manejan el flujo de ejecución del juego. Estos pueden incluir sistemas de IA para enemigos, mecanismos de combate, y lógica de nivel. Cada uno de estos componentes es responsable de una parte específica del comportamiento del juego y su implementación puede variar dependiendo de la complejidad del juego.

Los componentes de almacenamiento son aquellos que manejan los datos persistentes del juego. Esto puede incluir la gestión de las puntuaciones, el progreso del jugador, y cualquier otra información que necesite ser guardada entre sesiones de juego. Los componentes de almacenamiento pueden interactuar con bases de datos o archivos locales para persistir la información.

Los componentes de red son importantes en los juegos multijugador, permitiendo a los jugadores intercambiar información en tiempo real. Esto puede implicar la transmisión de estados de personajes, eventos del juego y cualquier otra información relevante entre los clientes y el servidor.

Finalmente, los componentes de interfaz de usuario (UI) son aquellos que proporcionan una forma visual para interactuar con el juego. Esto puede incluir botones, menus, indicadores de vida y cualquier otro elemento gráfico que permita a los jugadores controlar el juego o obtener información sobre su progreso.

Cada uno de estos componentes juega un papel crucial en la creación de juegos 2D y 3D, proporcionando la estructura, funcionalidad y experiencia del usuario necesaria para una buena jugabilidad. A través de la comprensión y manipulación de estos componentes, los desarrolladores pueden crear experiencias de juego dinámicas y envolventes que mantengan a los jugadores comprometidos durante largos períodos de tiempo.

<a id="fuentes-de-audio-propiedades"></a>
## Fuentes de audio. Propiedades

En el desarrollo de juegos 2D y 3D, la gestión adecuada de fuentes de audio es crucial para crear una experiencia inmersiva y atractiva. Las fuentes de audio pueden variar desde simples efectos sonoros hasta música ambiental y diálogos, cada uno con sus propias características y propiedades que permiten su integración en el juego.

Las fuentes de audio en los motores de juegos suelen estar compuestas por varias partes, incluyendo la carga del archivo de audio, la configuración de las propiedades del sonido y la gestión de la reproducción. La carga del archivo es un proceso fundamental que implica leer los datos del archivo de audio y almacenarlos en una estructura interna que el motor pueda utilizar para reproducir el sonido.

Una vez cargado el archivo, se pueden configurar varias propiedades del sonido para adaptarlo al contexto del juego. Estas propiedades pueden incluir la volumen, el pitch (o tono), la posición y orientación en el espacio tridimensional, y si el sonido debe reproducirse repetitivamente o solo una vez. Cada uno de estos parámetros juega un papel importante en cómo se percibirá el sonido por parte del jugador.

Además de las propiedades básicas, los motores de juegos también ofrecen funcionalidades avanzadas para controlar la reproducción de los sonidos. Por ejemplo, es posible establecer zonas de sonido donde ciertos efectos o música cambien dinámicamente según el movimiento del jugador o la situación en el juego. También se pueden utilizar eventos de sonido para desencadenar efectos específicos en respuesta a acciones del jugador.

La gestión de la reproducción de los sonidos es otro aspecto importante que debe considerarse. Los motores de juegos suelen implementar sistemas de colas de sonido o canales de audio separados para controlar la prioridad y el orden de reproducción de los efectos y la música. Esto permite evitar situaciones en las que ciertos sonidos se sobrepasan por otros, lo que puede afectar la experiencia del jugador.

En resumen, la gestión de fuentes de audio es una parte integral del desarrollo de juegos 2D y 3D. Desde la carga del archivo hasta la configuración de propiedades avanzadas y la gestión de reproducción, cada paso requiere un enfoque cuidadoso para asegurar que el sonido contribuya de manera efectiva a la experiencia del juego. Comprender estos aspectos es fundamental para crear juegos que sean no solo visualesmente impresionantes, sino también auditivosmente impactantes y envolventes.

<a id="camaras-e-iluminacion"></a>
## Cámaras e iluminación

En la creación de juegos 2D y 3D, las cámaras e iluminación desempeñan un papel crucial en el diseño visual y la experiencia del jugador. Las cámaras son esenciales para controlar desde dónde y cómo se ve el juego, mientras que la iluminación ayuda a crear ambientes realistas y dinámicos.

Las cámaras en los motores de juegos actuales ofrecen una gran variedad de opciones para su configuración, permitiendo al desarrollador ajustar la perspectiva, el zoom y el movimiento según sea necesario. Por ejemplo, una cámara ortográfica es útil para juegos 2D, ya que mantiene un tamaño constante independientemente del desplazamiento. En contraste, las cámaras perspectivas son más apropiadas para juegos 3D, donde la perspectiva cambia según el movimiento de la cámara.

La iluminación en los juegos es otro aspecto fundamental que puede crear o romper la inmersión del jugador. Los motores de juegos modernos ofrecen una amplia gama de técnicas de iluminación, desde la iluminación basada en fuentes hasta las técnicas de iluminación por sombreado realista. La correcta configuración de luces puede hacer que los objetos parezcan más naturales y realistas, lo que es crucial para mantener el interés del jugador.

Además de las cámaras e iluminación, la gestión eficiente de estos elementos es vital para el rendimiento del juego. Los desarrolladores deben estar atentos a cómo se utilizan los recursos gráficos, ya que una mala configuración puede llevar a problemas de rendimiento y un juego que sea difícil de jugar.

En el desarrollo de juegos 2D y 3D, también es importante considerar la interacción del jugador con las cámaras e iluminación. Por ejemplo, en juegos de acción, los jugadores pueden moverse entre diferentes perspectivas para obtener una mejor visión del escenario. En juegos de estrategia, el control preciso de la iluminación puede ayudar a ocultar información o revelar detalles importantes.

La comprensión y aplicación adecuada de cámaras e iluminación no solo mejora la experiencia del jugador, sino que también añade profundidad y realismo a los juegos. Al trabajar en esta área, es fundamental mantener un equilibrio entre la estética visual y el rendimiento del juego, asegurando que ambas cosas funcionen de manera armoniosa.

En resumen, las cámaras e iluminación son herramientas poderosas en el arsenal del desarrollador de juegos. Su correcta configuración puede hacer una gran diferencia en la calidad final del juego, contribuyendo a una experiencia más inmersiva y satisfactoria para los jugadores.

<a id="creacion-de-escenas"></a>
## Creación de escenas.

En el desarrollo de juegos 2D y 3D, la creación de escenas es un paso crucial que permite visualizar y experimentar con los elementos gráficos y narrativos del juego. Esta fase implica la definición de los espacios donde se desarrollará la acción, desde simples niveles hasta complejas ambientes interactivos.

La creación de escenas en juegos 2D a menudo comienza con el diseño de mapas o niveles utilizando herramientas gráficas y editores específicos. Estos mapas pueden incluir plataformas, obstáculos, personajes y elementos ambientales que contribuyen al juego. En el caso de los juegos 3D, la creación de escenas es aún más compleja, ya que implica el diseño de espacios tridimensionales que pueden ser explorados por los jugadores.

Para implementar estas escenas en un juego, se utilizan motores gráficos y bibliotecas específicas. Estos motores proporcionan funciones para cargar modelos 3D, aplicar texturas, manejar la iluminación y animaciones, entre otros aspectos visuales cruciales. La creación de escenas implica no solo el diseño estético, sino también la programación que permite la interacción del jugador con el entorno.

Además de los elementos estáticos, las escenas en juegos 2D y 3D a menudo incluyen elementos dinámicos como personajes móviles, objetos que pueden interactuar con el jugador o otros personajes, y efectos visuales que añaden atmósfera y realismo. La programación de estos elementos requiere una comprensión profunda de la física del juego, la interacción entre objetos y la respuesta al input del usuario.

La creación de escenas también implica considerar la eficiencia gráfica. Los motores de juegos están diseñados para manejar un gran número de elementos en pantalla simultáneamente, lo que requiere una optimización cuidadosa para evitar problemas de rendimiento. Esto incluye la gestión del uso de memoria y la selección de técnicas gráficas apropiadas.

En el contexto de los juegos 2D, las escenas pueden ser diseñadas utilizando herramientas gráficas como Photoshop o GIMP, mientras que en los juegos 3D se utilizan motores gráficos como Unity o Unreal Engine. Estas herramientas ofrecen una variedad de recursos y funcionalidades para crear escenas detalladas y interactivas.

La creación de escenas es un proceso iterativo que implica la prueba y la refinación del diseño. Los diseñadores y programadores trabajan juntos para asegurar que las escenas sean atractivas, funcionales y coherentes con el resto del juego. La retroalimentación del jugador también juega un papel crucial en esta fase, ya que permite identificar áreas donde se pueden mejorar la experiencia de juego.

En resumen, la creación de escenas es una etapa fundamental en el desarrollo de juegos 2D y 3D, que requiere una combinación de diseño creativo, programación eficiente y optimización gráfica. Esta fase no solo contribuye a la apariencia visual del juego, sino también a su jugabilidad y experiencia general para los jugadores.

<a id="analisis-de-ejecucion"></a>
## Análisis de ejecución

Después de definir las técnicas básicas de programación 2D y 3D, es crucial analizar cómo se ejecutan los juegos para optimizar su rendimiento. La fase de análisis de ejecución implica la evaluación del desempeño de un juego en diferentes entornos y bajo distintas condiciones. Este proceso puede incluir la medición de tiempos de carga, velocidad de procesamiento, uso de memoria y gráficos, entre otros factores.

Para realizar este análisis, es fundamental utilizar herramientas específicas que permitan recopilar datos detallados sobre el comportamiento del juego. Estas herramientas pueden variar desde simples monitores de rendimiento incorporados en los IDE hasta software especializado como profilers y analizadores de desempeño. La elección de la herramienta adecuada dependerá del tipo de juego, su complejidad y las plataformas objetivo.

Una vez recopilados los datos, es necesario interpretarlos para identificar áreas de mejora. Esto puede implicar la optimización de algoritmos, la reducción de consumo de recursos o la mejora de la eficiencia gráfica. Es importante recordar que el análisis de ejecución no debe ser un proceso aislado; debe estar integrado en un ciclo continuo de desarrollo y pruebas.

Además del rendimiento técnico, otro aspecto crucial es el análisis de la experiencia del usuario (UX). Esto incluye la medición de tiempos de respuesta, la comodidad del control y la satisfacción general del jugador. Herramientas como analizadores de comportamiento de usuarios pueden proporcionar insights valiosos sobre cómo los jugadores interactúan con el juego.

La fase de análisis de ejecución no solo ayuda a mejorar el rendimiento técnico, sino que también es fundamental para la adaptación del juego a diferentes plataformas y dispositivos. Esto puede implicar ajustes en la resolución de pantalla, la optimización de gráficos o incluso la simplificación de ciertas funcionalidades para mantener un buen desempeño en dispositivos con menor potencia.

En conclusión, el análisis de ejecución es una fase integral del desarrollo de juegos 2D y 3D. A través de la recopilación y análisis detallado de datos sobre el rendimiento técnico y la experiencia del usuario, se pueden identificar y corregir problemas que afecten a la calidad final del juego. Este proceso no solo mejora la eficiencia del código y la utilización de recursos, sino que también asegura una mejor satisfacción del jugador en todas las plataformas objetivo.


<a id="utilizacion-de-librerias-multimedia-integradas"></a>
# Utilización de librerías multimedia integradas

<a id="conceptos-sobre-aplicaciones-multimedia"></a>
## Conceptos sobre aplicaciones multimedia

En este capítulo, nos adentramos en los fundamentos del desarrollo de aplicaciones multimedia integradas, un campo que combina conocimientos de programación con la creación de contenido visual y audio. Comenzamos por definir qué son las aplicaciones multimedia, destacando su naturaleza compleja y multifacética, que va desde el simple reproductor de música hasta los sofisticados motores de juegos.

La arquitectura del API utilizado es un aspecto crucial en este contexto. Un API (Application Programming Interface) es una interfaz que permite a diferentes programas interactuar entre sí. En aplicaciones multimedia, estos APIs proporcionan funciones básicas para el procesamiento y reproducción de contenido multimedia, como la carga de archivos de audio o video, la manipulación de imágenes y la gestión de eventos de entrada del usuario.

Las fuentes de datos multimedia son otro elemento fundamental. Estas pueden ser archivos locales en el dispositivo, streams de internet o incluso dispositivos conectados a través de interfaces como Bluetooth o Wi-Fi. Cada fuente de datos requiere un manejo específico para su acceso y procesamiento dentro de la aplicación, lo que implica una comprensión profunda de las clases y métodos disponibles en el API utilizado.

El procesamiento de objetos multimedia es otro aspecto importante del desarrollo de aplicaciones multimedia integradas. Esto incluye la codificación y decodificación de audio y video, la manipulación de imágenes y la creación de efectos visuales y sonoros. Las clases y métodos proporcionados por el API facilitan este proceso, permitiendo a los desarrolladores crear contenido multimedia interactivo y dinámico.

La reproducción de objetos multimedia es una funcionalidad básica pero crucial en cualquier aplicación multimedia. Esto implica la carga del contenido desde las fuentes de datos, su decodificación y presentación al usuario. La calidad y eficiencia de esta reproducción son factores clave que determinan la experiencia del usuario.

La animación de objetos es otro aspecto emocionante del desarrollo de aplicaciones multimedia integradas. A través de técnicas como el uso de gráficos 2D y 3D, los desarrolladores pueden crear contenido visualmente atractivo e interactivo. Las clases y métodos proporcionados por el API facilitan la creación de animaciones complejas y dinámicas.

En conclusión, el desarrollo de aplicaciones multimedia integradas requiere una comprensión profunda del funcionamiento de APIs, la gestión eficiente de fuentes de datos multimedia, el procesamiento y reproducción de contenido, así como la creación de efectos visuales y sonoros. Cada uno de estos aspectos contribuye a crear experiencias multimedia ricas y envolventes para los usuarios.

### video en html5

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <video src="entrevista.mp4"></video>
  </body>
</html>
```

### video con controles

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <video src="entrevista.mp4" controls></video>
  </body>
</html>
```

### reproducir con javascript

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <video src="entrevista.mp4"></video>
    <button id="reproducir">Reproducir</button>
    <script>
      let video = document.querySelector("video");
      let boton = document.querySelector("button");
      boton.onclick = function(){
        video.play();
      }
      
    </script>
  </body>
</html>
```

### parar

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <video src="entrevista.mp4"></video>
    <button id="reproducir">Reproducir</button>
    <button id="parar">Parar</button>
    <script>
      let video = document.querySelector("video");
      let boton = document.querySelector("#reproducir");
      let botonparar = document.querySelector("#parar");
      boton.onclick = function(){
        video.play();
      }
      botonparar.onclick = function(){
        video.pause();
      }
      
      
    </script>
  </body>
</html>
```

### rebobinar

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <video src="entrevista.mp4"></video>
    <button id="reproducir">Reproducir</button>
    <button id="parar">Parar</button>
    <button id="rebobinar">Rebobinar</button>
    <script>
      let video = document.querySelector("video");
      let boton = document.querySelector("#reproducir");
      let botonparar = document.querySelector("#parar");
      let botonrebobinar = document.querySelector("#rebobinar");
      boton.onclick = function(){
        video.play();
      }
      botonparar.onclick = function(){
        video.pause();
      }
      botonrebobinar.onclick = function(){
        video.currentTime = 0
      }
      
      
    </script>
  </body>
</html>
```

### 10 segundos

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">Rebobinar</button>
        <button id="menosdiez">-10</button>
        <button id="reproducir">Reproducir</button>
        <button id="parar">Parar</button>
        <button id="masdiez">+10</button>
      <div>
    </div>
    
    <script>
      let video = document.querySelector("video");
      let boton = document.querySelector("#reproducir");
      let botonparar = document.querySelector("#parar");
      let botonrebobinar = document.querySelector("#rebobinar");
      let botonmenosdiez = document.querySelector("#menosdiez");
      let botonmasdiez = document.querySelector("#masdiez");
      boton.onclick = function(){
        video.play();
      }
      botonparar.onclick = function(){
        video.pause();
      }
      botonrebobinar.onclick = function(){
        video.currentTime = 0
      }
      botonmenosdiez.onclick = function(){
        video.currentTime -= 10
      }
      botonmasdiez.onclick = function(){
        video.currentTime += 10
      }
      
      
    </script>
  </body>
</html>
```

### estilo

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">R</button>
        <button id="menosdiez">-</button>
        <button id="reproducir">P</button>
        <button id="parar">S</button>
        <button id="masdiez">+</button>
      <div>
    </div>
    
    <script>
      let video = document.querySelector("video");
      let boton = document.querySelector("#reproducir");
      let botonparar = document.querySelector("#parar");
      let botonrebobinar = document.querySelector("#rebobinar");
      let botonmenosdiez = document.querySelector("#menosdiez");
      let botonmasdiez = document.querySelector("#masdiez");
      boton.onclick = function(){
        video.play();
      }
      botonparar.onclick = function(){
        video.pause();
      }
      botonrebobinar.onclick = function(){
        video.currentTime = 0
      }
      botonmenosdiez.onclick = function(){
        video.currentTime -= 10
      }
      botonmasdiez.onclick = function(){
        video.currentTime += 10
      }
      
      
    </script>
  </body>
</html>
```

### mostrar solo al entrar

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:0;
        transition:all 1s;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">R</button>
        <button id="menosdiez">-</button>
        <button id="reproducir">P</button>
        <button id="parar">S</button>
        <button id="masdiez">+</button>
      <div>
    </div>
    
    <script>
      let video = document.querySelector("video");
      let boton = document.querySelector("#reproducir");
      let botonparar = document.querySelector("#parar");
      let botonrebobinar = document.querySelector("#rebobinar");
      let botonmenosdiez = document.querySelector("#menosdiez");
      let botonmasdiez = document.querySelector("#masdiez");
      boton.onclick = function(){
        video.play();
      }
      botonparar.onclick = function(){
        video.pause();
      }
      botonrebobinar.onclick = function(){
        video.currentTime = 0
      }
      botonmenosdiez.onclick = function(){
        video.currentTime -= 10
      }
      botonmasdiez.onclick = function(){
        video.currentTime += 10
      }
      
      
    </script>
  </body>
</html>
```

### refactorizamos javascript

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:0;
        transition:all 1s;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">R</button>
        <button id="menosdiez">-</button>
        <button id="reproducir">P</button>
        <button id="parar">S</button>
        <button id="masdiez">+</button>
      <div>
    </div>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      
      
      
    </script>
  </body>
</html>
```

### boton de play

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>

        </button>
        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>

        </button>
        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>

        </button>
      <div>
    </div>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      
      
      
    </script>
  </body>
</html>
```

### control de volumen

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>

        </button>
        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>

        </button>
        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>

        </button>
      <div>
    </div>
    <input id="volumen" type="range" min=0 max=1 step=0.01>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      let volumen = document.querySelector("#volumen")
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      volumen.onchange = function(){
        video.volume = this.value
      }
      
      
      
    </script>
  </body>
</html>
```

### cargar resoluciones

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>

        </button>
        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>

        </button>
        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>

        </button>
      <div>
    </div>
    <input id="volumen" type="range" min=0 max=1 step=0.01>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      let volumen = document.querySelector("#volumen")
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      volumen.onchange = function(){
        video.volume = this.value
      }
      fetch("video/entrevista_renditions.json")
      .then(function(response){return response.json()})
      .then(function(datos){
        console.log(datos)
      })
      
      
    </script>
  </body>
</html>
```

### select de resoluciones

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>

        </button>
        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>

        </button>
        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>

        </button>
      <div>
    </div>
    <input id="volumen" type="range" min=0 max=1 step=0.01>
    <select id="resoluciones"></select>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      let volumen = document.querySelector("#volumen")
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      volumen.onchange = function(){
        video.volume = this.value
      }
      fetch("video/entrevista_renditions.json")
      .then(function(response){return response.json()})
      .then(function(datos){
        console.log(datos)
      })
      
      
    </script>
  </body>
</html>
```

### relleno el select

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>

        </button>
        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>

        </button>
        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>

        </button>
      <div>
    </div>
    <input id="volumen" type="range" min=0 max=1 step=0.01>
    <select id="resoluciones"></select>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      let volumen = document.querySelector("#volumen")
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      volumen.onchange = function(){
        video.volume = this.value
      }
      fetch("video/entrevista_renditions.json")
      .then(function(response){return response.json()})
      .then(function(datos){
        let selector = document.querySelector("select")
        datos.renditions.forEach(function(dato){
          let opcion = document.createElement("option")
          opcion.value = dato.label
          opcion.textContent = dato.label
          selector.appendChild(opcion)
        })
      })
      
      
    </script>
  </body>
</html>
```

### selecciono video

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>

        </button>
        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>

        </button>
        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>

        </button>
      <div>
    </div>
    <input id="volumen" type="range" min=0 max=1 step=0.01>
    <select id="resoluciones"></select>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      let volumen = document.querySelector("#volumen")
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      volumen.onchange = function(){
        video.volume = this.value
      }
      fetch("video/entrevista_renditions.json")
      .then(function(response){return response.json()})
      .then(function(datos){
        console.log(datos)
        let selector = document.querySelector("select")
        datos.renditions.forEach(function(dato){
          let opcion = document.createElement("option")
          opcion.value = dato.filename
          opcion.textContent = dato.label
          selector.appendChild(opcion)
        })
        selector.onchange = function(){
          video.src= "video/"+this.value
        }
        
      })
      
      
    </script>
  </body>
</html>
```

### cambio dinamico de resolucion

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4" controls></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>

        </button>
        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>

        </button>
        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>

        </button>
      <div>
    </div>
    <input id="volumen" type="range" min=0 max=1 step=0.01>
    <select id="resoluciones"></select>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      let volumen = document.querySelector("#volumen")
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      volumen.onchange = function(){
        video.volume = this.value
      }
      fetch("video/entrevista_renditions.json")
      .then(function(response){return response.json()})
      .then(function(datos){
        console.log(datos)
        let selector = document.querySelector("select")
        datos.renditions.forEach(function(dato){
          let opcion = document.createElement("option")
          opcion.value = dato.filename
          opcion.textContent = dato.label
          selector.appendChild(opcion)
        })
        selector.onchange = function(){
          let tiempoactual = video.currentTime
          video.src= "video/"+this.value
          video.currentTime = tiempoactual
          video.play()
          
        }
        
      })
      
      
    </script>
  </body>
</html>
```

### un poco de estilo para el select

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;}
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
      #contenedorvideo #controlesvideo select{
        width:60px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
      }
      
      
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4"></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>

        </button>
        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>

        </button>
        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>

        </button>
        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>

        </button>
      <div>
    </div>
    <input id="volumen" type="range" min=0 max=1 step=0.01>
    <select id="resoluciones"></select>
    
    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      let volumen = document.querySelector("#volumen")
      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0
              break;
            case "menosdiez":
              video.currentTime -= 10
              break;
            case "reproducir":
              video.play()
              break;
            case "parar":
              video.pause()
              break;
            case "masdiez":
              video.currentTime += 10
              break;
          }
        }
      })
      volumen.onchange = function(){
        video.volume = this.value
      }
      fetch("video/entrevista_renditions.json")
      .then(function(response){return response.json()})
      .then(function(datos){
        console.log(datos)
        let selector = document.querySelector("select")
        datos.renditions.forEach(function(dato){
          let opcion = document.createElement("option")
          opcion.value = dato.filename
          opcion.textContent = dato.label
          selector.appendChild(opcion)
        })
        selector.onchange = function(){
          let tiempoactual = video.currentTime
          video.src= "video/"+this.value
          video.currentTime = tiempoactual
          video.play()
        }
      })
    </script>
  </body>
</html>
```

### por donde va el tiempo

```html
<!doctype html>
<html>
  <head>
    <style>
      #contenedorvideo video{
        border-radius:10px;
        width:100%;
        height:100%;
      }
      #contenedorvideo{
        display:flex;
        position:relative;
        width:800px;
        height:500px;
        justify-content: center;
        align-items: center;
      }
      #contenedorvideo video{
        position:absolute;
        top:0px;
        left:0px;
      }
      #contenedorvideo #controlesvideo{
        position:absolute;
        padding:20px;
        background:rgba(0,0,0,0.5);
        border-radius:40px;
        backdrop-filter:blur(5px);
        opacity:1;
        transition:all 1s;
        display:flex;
        gap:10px;
        align-items:center;
      }
      #contenedorvideo #controlesvideo:hover{
        opacity:1;
      }
      #contenedorvideo #controlesvideo button{
        width:30px;
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px;
        cursor:pointer;
      }
      #contenedorvideo #controlesvideo select{
        height:30px;
        border:none;
        background:white;
        color:black;
        text-align:center;
        border-radius:40px;
        padding:1px 8px;
      }
      #contenedorvideo #controlesvideo input[type="range"]{
        width:120px;
      }
      #tiempo{
        margin-top:10px;
        font-family:monospace;
        color:white;
      }
    </style>
  </head>
  <body>
    <div id="contenedorvideo">
      <video src="entrevista.mp4"></video>
      <div id="controlesvideo">
        <button id="rebobinar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>
        </button>

        <button id="menosdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>
        </button>

        <button id="reproducir">
          <svg width="30" height="30" viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>
        </button>

        <button id="parar">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <rect x="2" y="2" width="4" height="4" />
          </svg>
        </button>

        <button id="masdiez">
          <svg width="30" height="30" viewBox="0 0 8 8" fill="currentColor">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>
        </button>

        <!-- Volumen dentro de controles -->
        <input id="volumen" type="range" min="0" max="1" step="0.01">
<div id="tiempo"></div>
        <!-- Select de resoluciones dentro de controles -->
        <select id="resoluciones"></select>
      </div>
    </div>

    

    <script>
      let video = document.querySelector("video");
      let botones = document.querySelectorAll("button");
      let volumen = document.querySelector("#volumen");
      let selector = document.querySelector("#resoluciones");
      let divTiempo = document.querySelector("#tiempo");

      // Inicializar volumen
      volumen.value = video.volume;

      botones.forEach(function(boton){
        boton.onclick = function(){
          switch(this.getAttribute("id")){
            case "rebobinar":
              video.currentTime = 0;
              break;
            case "menosdiez":
              video.currentTime -= 10;
              break;
            case "reproducir":
              video.play();
              break;
            case "parar":
              video.pause();
              break;
            case "masdiez":
              video.currentTime += 10;
              break;
          }
        }
      });

      volumen.oninput = function(){
        video.volume = this.value;
      };

      fetch("video/renditions.json")
      .then(function(response){return response.json()})
      .then(function(datos){
        console.log(datos);
        datos.renditions.forEach(function(dato){
          let opcion = document.createElement("option");
          opcion.value = dato.filename;
          opcion.textContent = dato.label;
          selector.appendChild(opcion);
        });
        selector.onchange = function(){
          let tiempoactual = video.currentTime;
          video.src= "video/"+this.value;
          video.currentTime = tiempoactual;
          video.play();
        };
      });

      // Actualizar tiempo cada segundo mientras está reproduciendo
      let temporizador = null;

      function formateaTiempo(segundosTotales){
        let s = Math.floor(segundosTotales);
        let minutos = Math.floor(s / 60).toString().padStart(2, "0");
        let segundos = (s % 60).toString().padStart(2, "0");
        return minutos + ":" + segundos;
      }

      function arrancarTemporizador(){
        if (temporizador !== null) return;
        temporizador = setInterval(function(){
          divTiempo.textContent = formateaTiempo(video.currentTime);
          // Aquí podrías hacer cualquier otra cosa "cada segundo"
          // console.log("Segundo actual:", Math.floor(video.currentTime));
        }, 1000);
      }

      function pararTemporizador(){
        if (temporizador !== null){
          clearInterval(temporizador);
          temporizador = null;
        }
      }

      video.addEventListener("play", arrancarTemporizador);
      video.addEventListener("pause", pararTemporizador);
      video.addEventListener("ended", pararTemporizador);

      // Mostrar 00:00 al inicio
      divTiempo.textContent = "00:00";
    </script>
  </body>
</html>
```

### convertido en libreria

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Demo jocarsa|video</title>
    <link rel="stylesheet" href="jocarsa-video.css">
  </head>
  <body>
    <!--
      data-jocarsa-video activa la librería.
      data-renditions es opcional: JSON con { renditions:[ {filename, label}, ... ] }
    -->
    <div data-jocarsa-video data-renditions="video/renditions.json">
      <video src="video/entrevista.mp4"></video>
    </div>

    <script src="jocarsa-video.js"></script>
    <script>
      // Opcional: inicializar manualmente un contenedor concreto
      // window["jocarsa|video"].init(document.querySelector("[data-jocarsa-video]"));
    </script>
  </body>
</html>
```

### jocarsa-video

```css
/* jocarsa-video.css */
/* Contenedor principal */
[data-jocarsa-video].jocarsa-video {
  display: flex;
  position: relative;
  max-width: 800px;
  aspect-ratio: 16 / 10;
  justify-content: center;
  align-items: center;
}

/* Vídeo */
.jocarsa-video__video {
  border-radius: 10px;
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  inset: 0;
}

/* Controles */
.jocarsa-video__controls {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 20px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 40px;
  backdrop-filter: blur(5px);
  opacity: 1;
  transition: opacity 0.5s;
  display: flex;
  gap: 10px;
  align-items: center;
}

.jocarsa-video__controls:hover {
  opacity: 1;
}

/* Botones */
.jocarsa-video__button {
  width: 30px;
  height: 30px;
  border: none;
  background: white;
  color: black;
  text-align: center;
  border-radius: 40px;
  padding: 1px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.jocarsa-video__button svg {
  width: 24px;
  height: 24px;
  fill: currentColor;
}

/* Tiempo */
.jocarsa-video__time {
  color: white;
  font-family: system-ui, sans-serif;
  font-size: 12px;
  min-width: 80px;
  text-align: center;
}

/* Volumen */
.jocarsa-video__volume {
  width: 100px;
}

/* Resoluciones */
.jocarsa-video__resolution {
  width: 80px;
  height: 30px;
  border: none;
  background: white;
  color: black;
  text-align: center;
  border-radius: 40px;
  padding: 1px 6px;
  cursor: pointer;
}

/* Opcional: ocultar controles nativos */
.jocarsa-video__video::-webkit-media-controls {
  display: none !important;
}
.jocarsa-video__video::-moz-media-controls {
  display: none !important;
}
```

### jocarsa-video

```javascript
// jocarsa-video.js
(function () {
  function pad(num) {
    return String(num).padStart(2, "0");
  }

  function formatTime(seconds) {
    if (!isFinite(seconds)) return "00:00";
    const s = Math.floor(seconds);
    const m = Math.floor(s / 60);
    const rs = s % 60;
    return pad(m) + ":" + pad(rs);
  }

  function createButton(type) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "jocarsa-video__button";
    let svg = "";

    switch (type) {
      case "rebobinar":
        svg = `
          <svg viewBox="0 0 8 8">
            <path d="M1 1v6"/>
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>`;
        break;
      case "menos10":
        svg = `
          <svg viewBox="0 0 8 8">
            <path d="M7 1L3.5 4 7 7z"/>
            <path d="M4.5 1L1 4l3.5 3z"/>
          </svg>`;
        break;
      case "play":
        svg = `
          <svg viewBox="0 0 7.9375 7.9375">
            <path d="M2.0150083 2.0150083V5.9224916L5.9224916 3.908733Z" />
          </svg>`;
        break;
      case "pause":
        svg = `
          <svg viewBox="0 0 8 8">
            <rect x="2" y="2" width="1.5" height="4" />
            <rect x="4.5" y="2" width="1.5" height="4" />
          </svg>`;
        break;
      case "mas10":
        svg = `
          <svg viewBox="0 0 8 8">
            <path d="M1 1l3.5 3L1 7z"/>
            <path d="M3.5 1l3.5 3-3.5 3z"/>
          </svg>`;
        break;
    }

    btn.innerHTML = svg;
    btn.dataset.jocarsaVideoButton = type;
    return btn;
  }

  function initContainer(container) {
    if (container.__jocarsaVideoInitialized) return;
    container.__jocarsaVideoInitialized = true;

    const video = container.querySelector("video");
    if (!video) return;

    container.classList.add("jocarsa-video");
    video.classList.add("jocarsa-video__video");
    video.controls = false;

    const controls = document.createElement("div");
    controls.className = "jocarsa-video__controls";

    const timeLabel = document.createElement("div");
    timeLabel.className = "jocarsa-video__time";
    timeLabel.textContent = "00:00 / 00:00";

    const btnRebobinar = createButton("rebobinar");
    const btnMenos10 = createButton("menos10");
    const btnPlay = createButton("play");
    const btnPause = createButton("pause");
    const btnMas10 = createButton("mas10");

    const volume = document.createElement("input");
    volume.type = "range";
    volume.min = "0";
    volume.max = "1";
    volume.step = "0.01";
    volume.value = video.volume ?? 1;
    volume.className = "jocarsa-video__volume";

    const resolution = document.createElement("select");
    resolution.className = "jocarsa-video__resolution";

    controls.appendChild(timeLabel);
    controls.appendChild(btnRebobinar);
    controls.appendChild(btnMenos10);
    controls.appendChild(btnPlay);
    controls.appendChild(btnPause);
    controls.appendChild(btnMas10);
    controls.appendChild(volume);
    controls.appendChild(resolution);

    container.appendChild(controls);

    let tickInterval = null;

    function updateTime() {
      const current = video.currentTime || 0;
      const total = video.duration || 0;
      timeLabel.textContent = `${formatTime(current)} / ${formatTime(total)}`;
      // Detección "cada segundo" mientras reproduce:
      // (esto se puede comentar o adaptar)
      console.log(
        "[jocarsa|video] playing at second",
        Math.floor(current)
      );
    }

    function startTick() {
      if (tickInterval) return;
      updateTime();
      tickInterval = setInterval(updateTime, 1000);
    }

    function stopTick() {
      if (tickInterval) {
        clearInterval(tickInterval);
        tickInterval = null;
      }
    }

    // Eventos de botones
    btnRebobinar.addEventListener("click", () => {
      video.currentTime = 0;
      updateTime();
    });

    btnMenos10.addEventListener("click", () => {
      video.currentTime = Math.max(0, video.currentTime - 10);
      updateTime();
    });

    btnPlay.addEventListener("click", () => {
      video.play();
    });

    btnPause.addEventListener("click", () => {
      video.pause();
    });

    btnMas10.addEventListener("click", () => {
      if (isFinite(video.duration)) {
        video.currentTime = Math.min(
          video.duration,
          video.currentTime + 10
        );
      } else {
        video.currentTime += 10;
      }
      updateTime();
    });

    volume.addEventListener("input", () => {
      video.volume = parseFloat(volume.value);
    });

    // Eventos del vídeo
    video.addEventListener("play", startTick);
    video.addEventListener("pause", stopTick);
    video.addEventListener("ended", stopTick);
    video.addEventListener("loadedmetadata", updateTime);

    // Resoluciones via JSON opcional: data-renditions="ruta/al/json"
    const renditionsUrl = container.dataset.renditions;
    if (renditionsUrl) {
      fetch(renditionsUrl)
        .then((r) => r.json())
        .then((data) => {
          if (!data || !Array.isArray(data.renditions)) return;
          resolution.innerHTML = "";
          data.renditions.forEach((rend) => {
            const opt = document.createElement("option");
            opt.value = rend.filename;
            opt.textContent = rend.label || rend.filename;
            resolution.appendChild(opt);
          });

          resolution.addEventListener("change", () => {
            const currentTime = video.currentTime;
            const wasPlaying = !video.paused && !video.ended;

            const newSrc = resolution.value;
            video.src = newSrc;

            const onLoaded = () => {
              video.currentTime = currentTime;
              if (wasPlaying) video.play();
              video.removeEventListener("loadedmetadata", onLoaded);
            };
            video.addEventListener("loadedmetadata", onLoaded);
          });
        })
        .catch((err) => {
          console.warn("[jocarsa|video] Error loading renditions:", err);
        });
    }
  }

  function initAll() {
    document
      .querySelectorAll("[data-jocarsa-video]")
      .forEach(initContainer);
  }

  // Namespace JS: window["jocarsa|video"]
  window["jocarsa|video"] = {
    init: initContainer,
    initAll: initAll,
  };

  if (
    document.readyState === "complete" ||
    document.readyState === "interactive"
  ) {
    initAll();
  } else {
    document.addEventListener("DOMContentLoaded", initAll);
  }
})();
```

<a id="arquitectura-del-api-utilizado"></a>
## Arquitectura del API utilizado

En este capítulo, exploramos en profundidad la arquitectura del API utilizado para el desarrollo de aplicaciones multimedia integradas. Comenzamos por entender los conceptos básicos sobre aplicaciones multimedia, identificando las diferentes fuentes de datos que pueden ser utilizadas y cómo se procesan estos datos dentro de un entorno de programación.

El primer paso es familiarizarse con la arquitectura del API utilizado, que proporciona una interfaz estándar para interactuar con los recursos multimedia. Este API incluye clases y métodos que facilitan el acceso a fuentes de audio, video y imágenes, así como funciones para su procesamiento y reproducción.

A continuación, profundizamos en la estructura del API, examinando las diferentes clases y objetos que componen su arquitectura. Cada clase tiene un propósito específico, desde la gestión de los recursos multimedia hasta el control de eventos de entrada del usuario. Es importante entender cómo interactúan estas clases entre sí para crear aplicaciones funcionales.

Una vez familiarizados con la estructura básica del API, nos centramos en las fuentes de datos multimedia que se pueden utilizar. Estas fuentes pueden ser archivos locales, streams de red o incluso dispositivos como cámaras web y micrófonos. El API proporciona métodos para cargar y procesar estos recursos, permitiendo a los desarrolladores crear aplicaciones que interactúen con el contenido multimedia en tiempo real.

Además del acceso a fuentes de datos, el API también ofrece herramientas para el procesamiento de objetos multimedia. Esto incluye la edición de imágenes y videos, la generación de efectos visuales y sonoros, y la manipulación de los formatos de archivo. Estas funcionalidades permiten a los desarrolladores crear aplicaciones que ofrezcan una experiencia multimedia rica y dinámica.

El API también proporciona métodos para reproducir objetos multimedia en diferentes formatos y dispositivos. Esto incluye la reproducción de audio y video en aplicaciones móviles, así como la generación de contenido multimedia para presentaciones y publicaciones en línea. La capacidad de adaptar el contenido a diferentes plataformas es crucial para crear aplicaciones multimedia versátiles.

Además del procesamiento y reproducción de objetos multimedia, el API también ofrece herramientas para gestionar las preferencias del usuario dentro de la aplicación. Esto incluye la configuración de opciones como volumen, calidad de imagen y formato de archivo predeterminado. La gestión adecuada de estas preferencias mejora la experiencia del usuario y aumenta la adhesión a la aplicación.

Finalmente, el API proporciona métodos para manejar tareas en segundo plano y servicios dentro de las aplicaciones multimedia. Esto incluye la ejecución de procesos que no interfieren con la interacción principal del usuario, como la actualización de contenido o la sincronización de datos. La gestión eficiente de estas tareas es crucial para mantener una buena experiencia de usuario incluso en aplicaciones intensivas.

En resumen, el API utilizado para el desarrollo de aplicaciones multimedia integradas ofrece una estructura sólida y funcional para interactuar con fuentes de datos multimedia, procesar objetos multimedia y gestionar la preferencia del usuario. Comprender esta arquitectura es fundamental para crear aplicaciones multimedia ricas y eficientes que ofrezcan una experiencia óptima al usuario.

### reproductor personalizado

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Audio</title>
    <style>
      #contieneaudio{
        width:300px;
        height:100px;
        background:lightgrey;
        display:flex;
        flex-direction:column;
        border-radius:10px;
        padding:20px;
      }
      #contieneaudio img{
        border-radius:5px;
      }
    </style>
  </head>
  <body>
    <div id="contieneaudio">
      <audio src="0802.mp3"></audio>
      <img src="0802.png">
      <input type="range" min=0 max=1 step=0.001>
    </div>
  </body>
</html>
```

### script de control

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Audio</title>
    <style>
      #contieneaudio{
        width:300px;
        height:100px;
        background:lightgrey;
        display:flex;
        flex-direction:column;
        border-radius:10px;
        padding:20px;
      }
      #contieneaudio img{
        border-radius:5px;
      }
    </style>
  </head>
  <body>
    <div id="contieneaudio">
      <audio src="0802.mp3"></audio>
      <img src="0802.png">
      <input type="range" min=0 max=1 step=0.001>
      <button>Play</button>
    </div>
    <script>
      var audio = document.querySelector("audio")
      var boton = document.querySelector("button")
      var tiempo = document.querySelector("input")
      

      boton.onclick = function(){
        audio.play()
      }
      tiempo.onchange = function(){
        let duracion = audio.duration
        console.log(duracion)
        audio.currentTime = this.value*duracion
      }
      
    </script>
  </body>
</html>
```

### progreso

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Audio</title>
    <style>
      #contieneaudio{
        width:300px;
        height:150px;
        background:lightgrey;
        display:flex;
        flex-direction:column;
        border-radius:10px;
        padding:20px;
      }
      #contieneaudio img{
        border-radius:5px;
      }
      progress{
        width:100%;
      }
    </style>
  </head>
  <body>
    <div id="contieneaudio">
      <audio src="0802.mp3"></audio>
      <img src="0802.png">
      <input type="range" min=0 max=1 step=0.001>
      <progress value="0.5"></progress>
      <button>Play</button>
    </div>
    <script>
      var audio = document.querySelector("audio")
      var boton = document.querySelector("button")
      var tiempo = document.querySelector("input")
      
      
      boton.onclick = function(){
        audio.play()
      }
      tiempo.onchange = function(){
        let duracion = audio.duration
        console.log(duracion)
        audio.currentTime = this.value*duracion
      }
      
    </script>
  </body>
</html>
```

### bucle

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Audio</title>
    <style>
      #contieneaudio{
        width:300px;
        height:150px;
        background:lightgrey;
        display:flex;
        flex-direction:column;
        border-radius:10px;
        padding:20px;
      }
      #contieneaudio img{
        border-radius:5px;
      }
      progress{
        width:100%;
      }
      #controladores{
        position:relative;
      }
      #controladores input, #controladores progress{
        position:absolute;
        top:0px;
        width:100%;
      }
      #controladores progress{
        z-index:1000;
      }
      #graficos{
        display:flex;
      }
      #graficos button{
        width:50px;
        height:50px;
        border-radius:50px;
      }
      #graficos img{
        width:100%;
      }
    </style>
  </head>
  <body>
    <div id="contieneaudio">
      <div id="graficos">
        <button>P</button>
        <img src="0802.png">
      </div>
      <audio src="0802.mp3"></audio>
      
      <div id="controladores">
        <input type="range" min=0 max=1 step=0.001>
        <progress value="0.5"></progress>
      </div>
      
    </div>
    <script>
      var audio = document.querySelector("audio")
      var boton = document.querySelector("button")
      var tiempo = document.querySelector("input")
      var progreso = document.querySelector("progress")
      
      boton.onclick = function(){
        audio.play()
      }
      tiempo.onchange = function(){
        let duracion = audio.duration
        console.log(duracion)
        audio.currentTime = this.value*duracion
      }
      
      let temporizador = setTimeout("bucle()",1000);
      
      function bucle(){
        let duracion = audio.duration
        progreso.value = audio.currentTime/duracion
        tiempo.value = audio.currentTime/duracion
        clearTimeout(temporizador)
        setTimeout("bucle()",100)
      }
      
      
    </script>
  </body>
</html>
```

### mejoras estéticas

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <title>Audio Player</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        #contieneaudio {
            width: 350px;
            background: white;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        #graficos {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        #graficos button {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            border: none;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            font-size: 24px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 10px rgba(110, 142, 251, 0.4);
            transition: all 0.3s ease;
        }
        
        #graficos button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(110, 142, 251, 0.6);
        }
        
        #graficos button:active {
            transform: scale(0.98);
        }
        
        #graficos img {
            width: 100px;
            height: 100px;
            border-radius: 10px;
            object-fit: cover;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .track-info {
            margin-top: 5px;
        }
        
        .track-title {
            font-weight: 600;
            font-size: 18px;
            color: #333;
        }
        
        .track-artist {
            font-size: 14px;
            color: #777;
        }
        
        #controladores {
            position: relative;
            margin-top: 10px;
        }
        
        #controladores progress {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            overflow: hidden;
            -webkit-appearance: none;
            appearance: none;
            background: #e0e0e0;
        }
        
        #controladores progress::-webkit-progress-bar {
            background: #e0e0e0;
            border-radius: 3px;
        }
        
        #controladores progress::-webkit-progress-value {
            background: linear-gradient(to right, #6e8efb, #a777e3);
            border-radius: 3px;
        }
        
        #controladores progress::-moz-progress-bar {
            background: linear-gradient(to right, #6e8efb, #a777e3);
            border-radius: 3px;
        }
        
        #controladores input[type="range"] {
            position: absolute;
            top: -2px;
            left: 0;
            width: 100%;
            height: 10px;
            margin: 0;
            opacity: 0;
            cursor: pointer;
            z-index: 1000;
        }
        
        .time-display {
            display: flex;
            justify-content: space-between;
            margin-top: 5px;
            font-size: 12px;
            color: #777;
        }
        
        .additional-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 15px;
        }
        
        .volume-control {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .volume-control input[type="range"] {
            width: 80px;
            height: 4px;
            -webkit-appearance: none;
            background: #e0e0e0;
            border-radius: 2px;
            outline: none;
        }
        
        .volume-control input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #6e8efb;
            cursor: pointer;
        }
        
        .playback-rate {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 14px;
        }
        
        .playback-rate select {
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 2px 5px;
            font-size: 12px;
            outline: none;
        }
    </style>
</head>
<body>
    <div id="contieneaudio">
        <div id="graficos">
            <button id="playBtn">▶</button>
            <div>
                <img src="0802.png" alt="Album Art">
                <div class="track-info">
                    <div class="track-title">Canción Ejemplo</div>
                    <div class="track-artist">Artista Desconocido</div>
                </div>
            </div>
        </div>
        
        <audio src="0802.mp3"></audio>
        
        <div id="controladores">
            <progress value="0" max="1"></progress>
            <input type="range" min="0" max="1" step="0.001" value="0">
            <div class="time-display">
                <span id="currentTime">0:00</span>
                <span id="duration">0:00</span>
            </div>
        </div>
        
        <div class="additional-controls">
            <div class="volume-control">
                <span>🔊</span>
                <input type="range" min="0" max="1" step="0.01" value="1" id="volumeControl">
            </div>
            <div class="playback-rate">
                <span>Velocidad:</span>
                <select id="playbackRate">
                    <option value="0.5">0.5x</option>
                    <option value="0.75">0.75x</option>
                    <option value="1" selected>Normal</option>
                    <option value="1.25">1.25x</option>
                    <option value="1.5">1.5x</option>
                    <option value="2">2x</option>
                </select>
            </div>
        </div>
    </div>
    
    <script>
        // Get DOM elements
        const audio = document.querySelector("audio");
        const playBtn = document.getElementById("playBtn");
        const progressBar = document.querySelector("progress");
        const seekBar = document.querySelector("#controladores input[type='range']");
        const currentTimeEl = document.getElementById("currentTime");
        const durationEl = document.getElementById("duration");
        const volumeControl = document.getElementById("volumeControl");
        const playbackRate = document.getElementById("playbackRate");
        
        // Format time from seconds to MM:SS
        function formatTime(seconds) {
            const mins = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
        }
        
        // Update time display
        function updateTimeDisplay() {
            currentTimeEl.textContent = formatTime(audio.currentTime);
            durationEl.textContent = formatTime(audio.duration || 0);
        }
        
        // Update progress bar
        function updateProgress() {
            if (audio.duration) {
                const progress = audio.currentTime / audio.duration;
                progressBar.value = progress;
                seekBar.value = progress;
            }
            updateTimeDisplay();
        }
        
        // Play/Pause functionality
        let isPlaying = false;
        
        playBtn.addEventListener("click", function() {
            if (isPlaying) {
                audio.pause();
                playBtn.textContent = "▶";
            } else {
                audio.play();
                playBtn.textContent = "❚❚";
            }
            isPlaying = !isPlaying;
        });
        
        // Seek functionality
        seekBar.addEventListener("input", function() {
            if (audio.duration) {
                audio.currentTime = this.value * audio.duration;
            }
        });
        
        // Volume control
        volumeControl.addEventListener("input", function() {
            audio.volume = this.value;
        });
        
        // Playback rate control
        playbackRate.addEventListener("change", function() {
            audio.playbackRate = parseFloat(this.value);
        });
        
        // Update progress and time display periodically
        audio.addEventListener("loadedmetadata", updateTimeDisplay);
        audio.addEventListener("timeupdate", updateProgress);
        audio.addEventListener("ended", function() {
            isPlaying = false;
            playBtn.textContent = "▶";
        });
        
        // Initialize
        updateTimeDisplay();
    </script>
</body>
</html>
```

### mejoras

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <title>Audio Player with Waveform</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        #contieneaudio {
            width: 350px;
            background: white;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        #graficos {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        #graficos button {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            border: none;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            font-size: 24px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 10px rgba(110, 142, 251, 0.4);
            transition: all 0.3s ease;
        }
        
        #graficos button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(110, 142, 251, 0.6);
        }
        
        #graficos button:active {
            transform: scale(0.98);
        }
        
        #graficos img {
            width: 100px;
            height: 100px;
            border-radius: 10px;
            object-fit: cover;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .track-info {
            margin-top: 5px;
        }
        
        .track-title {
            font-weight: 600;
            font-size: 18px;
            color: #333;
        }
        
        .track-artist {
            font-size: 14px;
            color: #777;
        }
        
        #controladores {
            position: relative;
            margin-top: 10px;
        }
        
        #controladores progress {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            overflow: hidden;
            -webkit-appearance: none;
            appearance: none;
            background: #e0e0e0;
        }
        
        #controladores progress::-webkit-progress-bar {
            background: #e0e0e0;
            border-radius: 3px;
        }
        
        #controladores progress::-webkit-progress-value {
            background: linear-gradient(to right, #6e8efb, #a777e3);
            border-radius: 3px;
        }
        
        #controladores progress::-moz-progress-bar {
            background: linear-gradient(to right, #6e8efb, #a777e3);
            border-radius: 3px;
        }
        
        #controladores input[type="range"] {
            position: absolute;
            top: 9px;
            left: 0;
            width: 100%;
            height: 10px;
            margin: 0;
            opacity: 0;
            cursor: pointer;
            z-index: 1000;
        }
        
        .time-display {
            display: flex;
            justify-content: space-between;
            margin-top: 5px;
            font-size: 12px;
            color: #777;
        }
        
        .additional-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 15px;
        }
        
        .volume-control {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .volume-control input[type="range"] {
            width: 80px;
            height: 4px;
            -webkit-appearance: none;
            background: #e0e0e0;
            border-radius: 2px;
            outline: none;
        }
        
        .volume-control input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #6e8efb;
            cursor: pointer;
        }
        
        .playback-rate {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 14px;
        }
        
        .playback-rate select {
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 2px 5px;
            font-size: 12px;
            outline: none;
        }
        
        /* Waveform visualization styles */
        .waveform-container {
            position: relative;
            width: 100%;
            height: 80px;
            margin: 15px 0;
            border-radius: 10px;
            overflow: hidden;
            background-color: #f5f5f5;
        }
        
        .waveform-background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, #e0e0e0 0%, #f0f0f0 100%);
            z-index: 1;
        }
        
        .waveform-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 2;
        }
        
        .waveform-progress-mask {
            position: absolute;
            top: 0;
            left: 0;
            width: 0%;
            height: 100%;
            background: linear-gradient(90deg, #6e8efb, #a777e3);
            mix-blend-mode: multiply;
            z-index: 3;
            transition: width 0.1s linear;
        }
        
        .waveform-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.7);
            z-index: 4;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div id="contieneaudio">
        <div id="graficos">
            <button id="playBtn">▶</button>
            <div>
                <img src="0802.png" alt="Album Art">
                <div class="track-info">
                    <div class="track-title">Canción Ejemplo</div>
                    <div class="track-artist">Artista Desconocido</div>
                </div>
            </div>
        </div>
        
        <!-- Waveform visualization -->
        <div class="waveform-container">
            <div class="waveform-background"></div>
            <img src="0802.png" alt="Waveform" class="waveform-image">
            <div class="waveform-progress-mask" id="waveformProgress"></div>
            <div class="waveform-overlay"></div>
        </div>
        
        <audio src="0802.mp3"></audio>
        
        <div id="controladores">
            <progress value="0" max="1"></progress>
            <input type="range" min="0" max="1" step="0.001" value="0">
            <div class="time-display">
                <span id="currentTime">0:00</span>
                <span id="duration">0:00</span>
            </div>
        </div>
        
        <div class="additional-controls">
            <div class="volume-control">
                <span>🔊</span>
                <input type="range" min="0" max="1" step="0.01" value="1" id="volumeControl">
            </div>
            <div class="playback-rate">
                <span>Velocidad:</span>
                <select id="playbackRate">
                    <option value="0.5">0.5x</option>
                    <option value="0.75">0.75x</option>
                    <option value="1" selected>Normal</option>
                    <option value="1.25">1.25x</option>
                    <option value="1.5">1.5x</option>
                    <option value="2">2x</option>
                </select>
            </div>
        </div>
    </div>
    
    <script>
        // Get DOM elements
        const audio = document.querySelector("audio");
        const playBtn = document.getElementById("playBtn");
        const progressBar = document.querySelector("progress");
        const seekBar = document.querySelector("#controladores input[type='range']");
        const currentTimeEl = document.getElementById("currentTime");
        const durationEl = document.getElementById("duration");
        const volumeControl = document.getElementById("volumeControl");
        const playbackRate = document.getElementById("playbackRate");
        const waveformProgress = document.getElementById("waveformProgress");
        
        // Format time from seconds to MM:SS
        function formatTime(seconds) {
            const mins = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
        }
        
        // Update time display
        function updateTimeDisplay() {
            currentTimeEl.textContent = formatTime(audio.currentTime);
            durationEl.textContent = formatTime(audio.duration || 0);
        }
        
        // Update progress bar and waveform
        function updateProgress() {
            if (audio.duration) {
                const progress = audio.currentTime / audio.duration;
                progressBar.value = progress;
                seekBar.value = progress;
                waveformProgress.style.width = `${progress * 100}%`;
            }
            updateTimeDisplay();
        }
        
        // Play/Pause functionality
        let isPlaying = false;
        
        playBtn.addEventListener("click", function() {
            if (isPlaying) {
                audio.pause();
                playBtn.textContent = "▶";
            } else {
                audio.play();
                playBtn.textContent = "❚❚";
            }
            isPlaying = !isPlaying;
        });
        
        // Seek functionality
        seekBar.addEventListener("input", function() {
            if (audio.duration) {
                const progress = this.value;
                audio.currentTime = progress * audio.duration;
                waveformProgress.style.width = `${progress * 100}%`;
            }
        });
        
        // Volume control
        volumeControl.addEventListener("input", function() {
            audio.volume = this.value;
        });
        
        // Playback rate control
        playbackRate.addEventListener("change", function() {
            audio.playbackRate = parseFloat(this.value);
        });
        
        // Update progress and time display periodically
        audio.addEventListener("loadedmetadata", updateTimeDisplay);
        audio.addEventListener("timeupdate", updateProgress);
        audio.addEventListener("ended", function() {
            isPlaying = false;
            playBtn.textContent = "▶";
        });
        
        // Initialize
        updateTimeDisplay();
    </script>
</body>
</html>
```

### desvelar onda

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <title>Audio Player with Waveform</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        #contieneaudio {
            width: 350px;
            background: white;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        #graficos {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        #graficos button {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            border: none;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            font-size: 24px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 10px rgba(110, 142, 251, 0.4);
            transition: all 0.3s ease;
        }
        
        #graficos button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(110, 142, 251, 0.6);
        }
        
        #graficos button:active {
            transform: scale(0.98);
        }
        
        #graficos img {
            width: 100px;
            height: 100px;
            border-radius: 10px;
            object-fit: cover;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .track-info {
            margin-top: 5px;
        }
        
        .track-title {
            font-weight: 600;
            font-size: 18px;
            color: #333;
        }
        
        .track-artist {
            font-size: 14px;
            color: #777;
        }
        
        #controladores {
            position: relative;
            margin-top: 10px;
            transform: translateY(-100px);
    z-index: 100000;
    opacity: 0.5;
        }
        
        #controladores progress {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            overflow: hidden;
            -webkit-appearance: none;
            appearance: none;
            background: #e0e0e0;
        }
        
        #controladores progress::-webkit-progress-bar {
            background: #e0e0e0;
            border-radius: 3px;
        }
        
        #controladores progress::-webkit-progress-value {
            background: linear-gradient(to right, #6e8efb, #a777e3);
            border-radius: 3px;
        }
        
        #controladores progress::-moz-progress-bar {
            background: linear-gradient(to right, #6e8efb, #a777e3);
            border-radius: 3px;
        }
        
        #controladores input[type="range"] {
            position: absolute;
            top: 9px;
            left: 0;
            width: 100%;
            height: 10px;
            margin: 0;
            opacity: 0;
            cursor: pointer;
            z-index: 1000;
        }
        
        .time-display {
            display: flex;
            justify-content: space-between;
            margin-top: 5px;
            font-size: 12px;
            color: #777;
        }
        
        .additional-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 15px;
        }
        
        .volume-control {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .volume-control input[type="range"] {
            width: 80px;
            height: 4px;
            -webkit-appearance: none;
            background: #e0e0e0;
            border-radius: 2px;
            outline: none;
        }
        
        .volume-control input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #6e8efb;
            cursor: pointer;
        }
        
        .playback-rate {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 14px;
        }
        
        .playback-rate select {
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 2px 5px;
            font-size: 12px;
            outline: none;
        }
        
        /* Waveform visualization styles */
        .waveform-container {
            position: relative;
            width: 100%;
            height: 80px;
            margin: 15px 0;
            border-radius: 10px;
            overflow: hidden;
            background-color: #f5f5f5;
        }
        
        .waveform-background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, #e0e0e0 0%, #f0f0f0 100%);
            z-index: 1;
        }
        
        .waveform-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 2;
        }
        
        .waveform-progress-mask {
            position: absolute;
            top: 0;
            right: 0;
            width: 100%;
            height: 100%;
            background: white;
            z-index: 3;
            transition: width 0.1s linear;
        }
        
        .waveform-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.7);
            z-index: 4;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div id="contieneaudio">
        <div id="graficos">
            <button id="playBtn">▶</button>
            <div>
                
                <div class="track-info">
                    <div class="track-title">0802</div>
                    <div class="track-artist">José Vicente Carratalá Sanchis</div>
                </div>
            </div>
        </div>
        
        <!-- Waveform visualization -->
        <div class="waveform-container">
            <div class="waveform-background"></div>
            <img src="0802.png" alt="Waveform" class="waveform-image">
            <div class="waveform-progress-mask" id="waveformProgress"></div>
            <div class="waveform-overlay"></div>
        </div>
        
        <audio src="0802.mp3"></audio>
        
        <div id="controladores">
            <progress value="0" max="1"></progress>
            <input type="range" min="0" max="1" step="0.001" value="0">
            <div class="time-display">
                <span id="currentTime">0:00</span>
                <span id="duration">0:00</span>
            </div>
        </div>
        
        <div class="additional-controls">
            <div class="volume-control">
                <span>🔊</span>
                <input type="range" min="0" max="1" step="0.01" value="1" id="volumeControl">
            </div>
            <div class="playback-rate">
                <span>Velocidad:</span>
                <select id="playbackRate">
                    <option value="0.5">0.5x</option>
                    <option value="0.75">0.75x</option>
                    <option value="1" selected>Normal</option>
                    <option value="1.25">1.25x</option>
                    <option value="1.5">1.5x</option>
                    <option value="2">2x</option>
                </select>
            </div>
        </div>
    </div>
    
    <script>
        // Get DOM elements
        const audio = document.querySelector("audio");
        const playBtn = document.getElementById("playBtn");
        const progressBar = document.querySelector("progress");
        const seekBar = document.querySelector("#controladores input[type='range']");
        const currentTimeEl = document.getElementById("currentTime");
        const durationEl = document.getElementById("duration");
        const volumeControl = document.getElementById("volumeControl");
        const playbackRate = document.getElementById("playbackRate");
        const waveformProgress = document.getElementById("waveformProgress");
        
        // Format time from seconds to MM:SS
        function formatTime(seconds) {
            const mins = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
        }
        
        // Update time display
        function updateTimeDisplay() {
            currentTimeEl.textContent = formatTime(audio.currentTime);
            durationEl.textContent = formatTime(audio.duration || 0);
        }
        
        // Update progress bar and waveform
        function updateProgress() {
            if (audio.duration) {
                const progress = audio.currentTime / audio.duration;
                progressBar.value = progress;
                seekBar.value = progress;
                // The mask shrinks from right to left as audio progresses
                waveformProgress.style.width = `${100 - (progress * 100)}%`;
            }
            updateTimeDisplay();
        }
        
        // Play/Pause functionality
        let isPlaying = false;
        
        playBtn.addEventListener("click", function() {
            if (isPlaying) {
                audio.pause();
                playBtn.textContent = "▶";
            } else {
                audio.play();
                playBtn.textContent = "❚❚";
            }
            isPlaying = !isPlaying;
        });
        
        // Seek functionality
        seekBar.addEventListener("input", function() {
            if (audio.duration) {
                const progress = this.value;
                audio.currentTime = progress * audio.duration;
                waveformProgress.style.width = `${100 - (progress * 100)}%`;
            }
        });
        
        // Volume control
        volumeControl.addEventListener("input", function() {
            audio.volume = this.value;
        });
        
        // Playback rate control
        playbackRate.addEventListener("change", function() {
            audio.playbackRate = parseFloat(this.value);
        });
        
        // Update progress and time display periodically
        audio.addEventListener("loadedmetadata", updateTimeDisplay);
        audio.addEventListener("timeupdate", updateProgress);
        audio.addEventListener("ended", function() {
            isPlaying = false;
            playBtn.textContent = "▶";
        });
        
        // Initialize
        updateTimeDisplay();
    </script>
</body>
</html>
```

<a id="fuentes-de-datos-multimedia-clases"></a>
## Fuentes de datos multimedia. Clases

En este capítulo, nos adentramos en la utilización de librerías multimedia integradas para el desarrollo de aplicaciones que manejan contenido audiovisual. Comenzamos por entender los conceptos básicos sobre aplicaciones multimedia, identificando las diferentes fuentes de datos multimedia y las clases asociadas con su procesamiento.

Las fuentes de datos multimedia son fundamentales en cualquier aplicación que requiera la manipulación de imágenes, audio o video. Estas fuentes pueden ser archivos locales en el dispositivo del usuario, recursos web accesibles a través de URLs, o incluso dispositivos de entrada como cámaras web o micrófonos. Cada fuente de datos multimedia tiene sus propias características y métodos para su acceso y manipulación.

Las clases asociadas con la gestión de fuentes de datos multimedia proporcionan una interfaz uniforme para interactuar con estos recursos, independientemente del tipo de contenido que se esté manejando. Estas clases incluyen funcionalidades como la carga, descarga, procesamiento y reproducción de audio y video. Algunas de las principales clases pueden ser `MediaPlayer`, `MediaRecorder` y `MediaMetadataRetriever`.

El uso de librerías multimedia integradas facilita el desarrollo de aplicaciones que requieren una alta calidad en la presentación del contenido multimedia. Estas librerías ofrecen optimizaciones internas para mejorar el rendimiento y la eficiencia, lo que es crucial cuando se trabaja con recursos intensivos como imágenes y videos.

Además, las clases asociadas con fuentes de datos multimedia suelen proporcionar métodos para manipular los atributos del contenido multimedia. Por ejemplo, pueden permitir ajustar el volumen del audio, cambiar la orientación de una imagen o seleccionar partes específicas de un video para reproducir. Esta funcionalidad es esencial para crear aplicaciones que ofrezcan una experiencia multimedia personalizada y adaptable a las necesidades del usuario.

En este capítulo, hemos explorado los conceptos básicos sobre fuentes de datos multimedia y las clases asociadas con su gestión en librerías multimedia integradas. A medida que avanzamos en el estudio de programación multimedia y dispositivos móviles, es importante comprender estos fundamentos para desarrollar aplicaciones que puedan manejar contenido audiovisual de manera eficiente y efectiva.

<a id="procesamiento-de-objetos-multimedia"></a>
## Procesamiento de objetos multimedia

En este capítulo, nos adentramos en la utilización de librerías multimedia integradas para el procesamiento de objetos multimedia, un aspecto crucial en el desarrollo de aplicaciones multimedia y dispositivos móviles. Comenzamos por entender los conceptos básicos sobre aplicaciones multimedia, que son programas diseñados para manipular y presentar contenido audiovisual de manera eficiente.

La arquitectura del API utilizado es fundamental para interactuar con estas librerías. Cada API tiene sus propias características y clases que facilitan el acceso a funciones específicas como la carga, reproducción y procesamiento de objetos multimedia. Estas clases proporcionan una interfaz uniforme para operaciones comunes, lo que simplifica significativamente el desarrollo.

El procesamiento de objetos multimedia implica manipular datos audiovisuales en tiempo real o almacenados en archivos. Las librerías integradas ofrecen métodos para cargar y analizar estos datos, permitiendo la extracción de información relevante como metadatos, análisis de características sonoras o visualización de imágenes.

La reproducción de objetos multimedia es otro aspecto clave del procesamiento. Librerías como MediaPlayer o AVFoundation proporcionan funcionalidades avanzadas para controlar la reproducción, incluyendo ajustes de volumen, velocidad y sincronización entre diferentes medios audiovisuales.

Además de cargar y reproducir, el procesamiento de objetos multimedia implica también su manipulación. Esto puede implicar la edición de videos, la generación de thumbnails o la creación de efectos visuales en tiempo real. Las librerías integradas ofrecen herramientas para realizar estas operaciones, permitiendo a los desarrolladores crear aplicaciones multimedia interactivas y dinámicas.

El contexto gráfico es otro elemento importante en el procesamiento de objetos multimedia. Librerías como OpenGL o Core Animation proporcionan APIs para renderizar gráficos 2D y 3D, lo que es esencial para la creación de interfaces de usuario multimedia sofisticadas.

Métodos de entrada también son cruciales en el procesamiento de objetos multimedia. Eventos como toques, gestos y cambios de orientación del dispositivo móvil deben ser capturados y respondidos adecuadamente para una experiencia de usuario fluida.

La gestión de las preferencias de la aplicación es otro aspecto que los desarrolladores deben considerar. Las librerías integradas ofrecen funcionalidades para almacenar y recuperar preferencias del usuario, lo que permite personalizar la experiencia de uso según las preferencias individuales.

El almacenamiento y persistencia de datos multimedia son otros temas importantes en el procesamiento de objetos multimedia. Librerías como SQLite o Core Data proporcionan herramientas para almacenar metadatos y configuraciones de aplicaciones, asegurando que los datos sean accesibles y seguros entre sesiones.

Finalmente, las tareas en segundo plano y servicios también son aspectos clave en el procesamiento de objetos multimedia. Librerías como BackgroundTask o JobScheduler permiten ejecutar operaciones importantes incluso cuando la aplicación no está en primer plano, asegurando que los usuarios experimenten una alta calidad de servicio.

En resumen, la utilización de librerías multimedia integradas para el procesamiento de objetos multimedia es un aspecto fundamental del desarrollo de aplicaciones multimedia y dispositivos móviles. Estas librerías proporcionan una amplia gama de funcionalidades que facilitan la manipulación y presentación de contenido audiovisual, permitiendo a los desarrolladores crear experiencias interactivas y dinámicas para sus usuarios.

<a id="reproduccion-de-objetos-multimedia"></a>
## Reproducción de objetos multimedia

En este capítulo, nos centraremos en la reproducción de objetos multimedia utilizando librerías integradas. Comenzamos por entender qué son los objetos multimedia y cómo se pueden representar gráficamente en aplicaciones. A continuación, exploramos las principales características de las librerías multimedia disponibles para el desarrollo de aplicaciones móviles, destacando sus ventajas y desventajas.

A medida que avanzamos, introducimos la teoría detrás del procesamiento de objetos multimedia, desde la carga hasta la visualización. Aprenderemos cómo manejar diferentes formatos de audio y video, así como cómo controlar su reproducción en tiempo real. También nos familiarizaremos con las técnicas de optimización para mejorar el rendimiento durante la reproducción.

Continuamos con una sección práctica donde aplicaremos lo aprendido a través de ejemplos de código. Estos ejemplos demuestran cómo integrar librerías multimedia en proyectos reales, desde la creación de interfaces de usuario hasta la implementación de funciones de control avanzadas como pausa, detener y ajuste de volumen.

A medida que nos acercamos al final del capítulo, reflexionamos sobre las mejores prácticas para el manejo de errores durante la reproducción multimedia. Aprenderemos cómo detectar y gestionar excepciones comunes, así como cómo implementar políticas de seguridad para proteger los recursos multimedia sensibles.

Finalmente, concluimos con una visión general de cómo las librerías multimedia integradas pueden ser utilizadas en el desarrollo de aplicaciones móviles complejas. Aprenderemos cómo aprovechar las capacidades de estas herramientas para crear experiencias multimedia atractivas y funcionales que mejoren la interacción del usuario.

Este capítulo proporciona una base sólida para entender y aplicar técnicas avanzadas de reproducción de objetos multimedia en aplicaciones móviles, preparando al lector para enfrentar desafíos más complejos en el futuro.

<a id="animacion-de-objetos"></a>
## Animación de objetos

En este capítulo, nos adentramos en la animación de objetos mediante librerías multimedia integradas, una técnica esencial para crear aplicaciones interactivas y dinámicas. Comenzamos explorando los conceptos básicos de animación 2D y 3D, comprendiendo cómo estos elementos pueden ser manipulados dentro del contexto de un programa multimedia.

A medida que avanzamos, nos familiarizamos con la arquitectura típica de una aplicación multimedia, identificando los componentes clave que contribuyen a su funcionamiento. Estos componentes incluyen fuentes de audio, cámaras e iluminación, y escenas, todos los cuales son fundamentales para crear un entorno visualmente atractivo y funcional.

El estudio de librerías multimedia integradas es una parte crucial de este proceso. Exploramos cómo estas herramientas proporcionan las funciones básicas necesarias para la animación de objetos, desde el manejo de imágenes hasta la reproducción de audio y la creación de efectos visuales. Aprenderemos a utilizar estas librerías no solo para crear animaciones estáticas, sino también para implementar interacciones dinámicas que respondan a eventos del usuario.

Además, dedicamos tiempo a entender cómo procesar objetos multimedia en aplicaciones móviles. Esto implica aprender sobre la gestión de imágenes y videos, así como técnicas avanzadas de animación que pueden ser utilizadas para mejorar la experiencia del usuario. A través de ejemplos prácticos, veremos cómo implementar estas técnicas en proyectos reales.

Finalmente, exploramos el uso de sensores y posicionamiento en aplicaciones móviles, aprendiendo cómo estos dispositivos pueden ser integrados para crear experiencias interactivas que respondan a la realidad del usuario. Esto incluye el manejo de conexiones HTTP y HTTPS, lo cual es crucial para la comunicación entre la aplicación y los servicios web.

En resumen, este capítulo proporciona una visión integral sobre cómo utilizar librerías multimedia integradas para animar objetos en aplicaciones multimedia y dispositivos móviles. A través de un enfoque práctico y detallado, hemos cubierto desde los conceptos básicos hasta técnicas avanzadas, preparando a los lectores para desarrollar aplicaciones interactivas y dinámicas que ofrecan una experiencia de usuario excepcional.


<a id="analisis-de-tecnologias-para-aplicaciones-en-dispositivos-moviles"></a>
# Análisis de tecnologías para aplicaciones en dispositivos móviles

<a id="dispositivos-moviles"></a>
## Dispositivos móviles

En este capítulo, nos adentramos en la exploración de los dispositivos móviles como plataforma para el desarrollo de aplicaciones. Comenzamos por definir qué son los dispositivos móviles y sus características distintivas que hacen de ellos una herramienta tan versátil y accesible.

Los dispositivos móviles, también conocidos como teléfonos inteligentes o tablets, se caracterizan por su portabilidad, conectividad constante a Internet y procesamiento potente. Estas características los convierten en el principal medio para la interacción con internet en la actualidad. El hardware de estos dispositivos incluye un procesador rápido, memoria RAM suficiente, almacenamiento interno y externo, pantalla táctil o sensor de voz, cámara y batería duradera.

El software que ejecutan los dispositivos móviles es el sistema operativo, que puede ser Android o iOS. Cada uno tiene sus propias características y APIs (Interfaces de Programación de Aplicaciones) específicas que permiten a los desarrolladores crear aplicaciones nativas para cada plataforma. Esta dualidad en la creación de aplicaciones móviles ofrece una gran flexibilidad pero también plantea desafíos en términos de mantenimiento y actualización.

Además de las plataformas Android e iOS, existen otras tecnologías emergentes como Flutter o React Native que permiten el desarrollo de aplicaciones multiplataforma. Estas soluciones utilizan lenguajes de programación como Dart o JavaScript respectivamente, lo que facilita la creación de aplicaciones para múltiples plataformas con un solo códigobase.

El hardware y software de los dispositivos móviles están en constante evolución, lo que implica que las tecnologías utilizadas en el desarrollo también deben adaptarse a estas nuevas realidades. Desde el uso de sensores más precisos hasta la implementación de funciones avanzadas como la realidad aumentada o la inteligencia artificial, los dispositivos móviles están cambiando drásticamente y con ellos lo está haciendo su software.

En este contexto, es crucial entender cómo funcionan estos dispositivos para desarrollar aplicaciones que no solo sean funcionalmente correctas sino también eficientes y agradables de usar. Esto implica conocer cómo se organiza el código, cómo se manejan los eventos, cómo se gestionan las preferencias del usuario y cómo se optimizan las operaciones en segundo plano.

Además, la seguridad es un aspecto fundamental al desarrollar aplicaciones para dispositivos móviles. Los usuarios confían sus datos a estas plataformas, por lo que es imperativo implementar medidas de seguridad robustas desde el inicio del desarrollo. Esto incluye la protección contra malware, la gestión adecuada de las credenciales y la conformidad con los estándares de privacidad y seguridad.

En resumen, el análisis de tecnologías para aplicaciones en dispositivos móviles es un campo dinámico que requiere una comprensión profunda del hardware y software de estos dispositivos. Al entender cómo funcionan y cómo se pueden aprovechar sus características, los desarrolladores pueden crear experiencias de usuario innovadoras y seguras que satisfagan las necesidades cambiantes de los usuarios en el mundo digital actual.

### Tecnologias

```markdown
Android
  Es de Google
  -Se programan controladores en Kotlin/Java
  -Se programan vistas en XML
  -Se puede programar, desde Windows, macOS, Linux
iOS
  Es de Apple
  -Se programan controladores en Swift
  -Se programan vistas en XML
  -Solo se puede programar desde macOS
Harmony OS
  Es de Huawei
  -Se programan controladores en Java
  -Se programan vistas en Java/XML
  -Se puede programar desde Windows, Linux (limitado), macOS
  
```

### prototipo

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos<button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
    </section>
  </body>
</html>
```

### estilo

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <style>
      body,html{background:#121212;color:white;}
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos<button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
    </section>
  </body>
</html>
```

### no reescalar

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;}
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos<button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
    </section>
  </body>
</html>
```

### botones

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
    </section>
  </body>
</html>
```

### articulos

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section id="favoritas">
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
    </section>
  </body>
</html>
```

### descarga de android studio

```markdown
https://developer.android.com/studio?hl=es-419

Nuevo proyecto

Empty Views activity

Nombre: AplicacionMovil1
Package: com.jocarsa.aplicacionmovil1

Ubicacion: /home/josevicente/AndroidStudioProjects/AplicacionMovil1

API Nougat Android 7

MainActivity.kt = Controlador
activity_main.xml = vista
```

### reproduccion

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        bottom:20px;
        box-sizing:border-box;
      }
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section id="favoritas">
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
    </section>
    <section id="reproductor">
    </section>
  </body>
</html>
```

### ocupa el 100

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section id="favoritas">
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
    </section>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <script>
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
    </script>
  </body>
</html>
```

<a id="hardware-para-dispositivos-moviles"></a>
## Hardware para dispositivos móviles

En este capítulo, nos adentramos en la comprensión del hardware que forma la base de los dispositivos móviles modernos. Comenzamos por explorar el hardware básico que todos los teléfonos móviles poseen: la placa base, que es el cerebro del dispositivo y contiene los componentes fundamentales como el procesador, la memoria RAM y el almacenamiento interno.

La placa base se comunica con otros componentes a través de una serie de puertos y interfaces. El procesador, también conocido como CPU (Central Processing Unit), es el encargado de ejecutar todas las instrucciones del sistema operativo y las aplicaciones. Su velocidad y capacidad son fundamentales para la rendimiento general del dispositivo.

La memoria RAM almacena temporalmente los datos que se están utilizando en ese momento, lo que permite una rápida accesibilidad a estos datos cuando el usuario interactúa con la aplicación. A diferencia de la memoria interna, la RAM es volátil, lo que significa que se pierde su contenido cuando el dispositivo se apaga.

El almacenamiento interno del teléfono móvil almacena los archivos y aplicaciones permanentemente. Los teléfonos móviles modernos también pueden tener una tarjeta microSD para aumentar su capacidad de almacenamiento si es necesario.

Además de estos componentes básicos, los dispositivos móviles contienen otros elementos cruciales como la pantalla táctil, que permite al usuario interactuar con el dispositivo mediante gestos y toques. La batería es otro componente fundamental, proporcionando energía continua a todo el sistema mientras se utiliza.

La cámara del teléfono móvil es otro elemento importante, ya que ha convertido los teléfonos móviles en herramientas de fotografía y videografía portátiles. Las cámaras modernas pueden capturar imágenes y videos con alta calidad, gracias a sus sensores fotográficos y al software de procesamiento incorporado.

El microprocesador de audio es otro componente que permite la grabación y reproducción de música y otros sonidos en el teléfono móvil. Además, los dispositivos móviles modernos contienen un amplio rango de sensores adicionales, como acelerómetros, giroscopios y sensores de proximidad, que mejoran la experiencia del usuario al proporcionar funciones como la detección de orientación y el bloqueo automático.

En resumen, el hardware de los dispositivos móviles es una combinación compleja de componentes que trabajan juntos para ofrecer a los usuarios una experiencia digital fluida y funcional. Cada uno de estos componentes desempeña un papel crucial en la operación del dispositivo y su capacidad para satisfacer las necesidades del usuario.

### Comenzamos

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section id="favoritas">
      
     
    </section>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="lista">
        <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
      })
    </script>
  </body>
</html>
```

### cargamos datos de ap

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section id="favoritas">
      
     
    </section>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img src="josevicente.jpg">
        <p>Artista</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          contenedor.appendChild(instancia)
        })
      })
    </script>
  </body>
</html>
```

### personalizamos la plantilla

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section id="favoritas">
      
     
    </section>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img src="...">
        <p>...</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          instancia.querySelector("p").textContent = dato.artist
          instancia.querySelector("img").setAttribute("src",dato.image)
          contenedor.appendChild(instancia)
        })
      })
    </script>
  </body>
</html>
```

### on error

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section id="favoritas">
      
     
    </section>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img 
          src="..."
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
          >
        <p>...</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          instancia.querySelector("p").textContent = dato.artist
          instancia.querySelector("img").setAttribute("src",dato.image)
          contenedor.appendChild(instancia)
        })
      })
    </script>
  </body>
</html>
```

### click en articulo

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
    </style>
  </head>
  <body>
    <header>  
      <button>J</button>
      <button>Todos</button>
      <button>Música</button>
      <button>Podcasts</button>
    </header>
    <section id="favoritas">
      
     
    </section>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img 
          src="..."
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
          >
        <p>...</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          let articulo = instancia.querySelector("article")
          articulo.querySelector("p").textContent = dato.artist
          articulo.querySelector("img").setAttribute("src",dato.image)
          contenedor.appendChild(instancia)
          articulo.onclick = function(){
            console.log("Has hecho click en un articulo");
          }
        })
      })
    </script>
  </body>
</html>
```

### pantalla siguiente

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
      #pantalla_lista{display:none;}
    </style>
  </head>
  <body>
    <div id="pantallas">
      <div id="pantalla_inicio">
        <header>  
          <button>J</button>
          <button>Todos</button>
          <button>Música</button>
          <button>Podcasts</button>
        </header>
        <section id="favoritas">
          
         
        </section>
      </div>
      <div id="pantalla_lista">
        Yo soy la lista
      </div>
    </div>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img 
          src="..."
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
          >
        <p>...</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          let articulo = instancia.querySelector("article")
          articulo.querySelector("p").textContent = dato.artist
          articulo.querySelector("img").setAttribute("src",dato.image)
          contenedor.appendChild(instancia)
          articulo.onclick = function(){
            console.log("Has hecho click en un articulo");
          }
        })
      })
    </script>
  </body>
</html>
```

### muestro la pantalla lista

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
      #pantalla_lista{display:none;}
    </style>
  </head>
  <body>
    <div id="pantallas">
      <div id="pantalla_inicio">
        <header>  
          <button>J</button>
          <button>Todos</button>
          <button>Música</button>
          <button>Podcasts</button>
        </header>
        <section id="favoritas">
          
         
        </section>
      </div>
      <div id="pantalla_lista">
        Yo soy la lista
      </div>
    </div>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img 
          src="..."
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
          >
        <p>...</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          let articulo = instancia.querySelector("article")
          articulo.querySelector("p").textContent = dato.artist
          articulo.querySelector("img").setAttribute("src",dato.image)
          contenedor.appendChild(instancia)
          articulo.onclick = function(){
            console.log("Has hecho click en un articulo");
            document.querySelector("#pantalla_inicio").style.display = "none"
            document.querySelector("#pantalla_lista").style.display = "block"
          }
        })
      })
    </script>
  </body>
</html>
```

### plantilla de la lista

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:absolute;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
      #pantalla_lista{display:none;}
    </style>
  </head>
  <body>
    <div id="pantallas">
      <div id="pantalla_inicio">
        <header>  
          <button>J</button>
          <button>Todos</button>
          <button>Música</button>
          <button>Podcasts</button>
        </header>
        <section id="favoritas">
          
         
        </section>
      </div>
      <div id="pantalla_lista">
        <img 
          src=""
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
        >
        <h3>Titulo de la lista</h3>
        
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
      </div>
    </div>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img 
          src="..."
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
          >
        <p>...</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          let articulo = instancia.querySelector("article")
          articulo.querySelector("p").textContent = dato.artist
          articulo.querySelector("img").setAttribute("src",dato.image)
          contenedor.appendChild(instancia)
          articulo.onclick = function(){
            console.log("Has hecho click en un articulo");
            document.querySelector("#pantalla_inicio").style.display = "none"
            document.querySelector("#pantalla_lista").style.display = "block"
          }
        })
      })
    </script>
  </body>
</html>
```

### estilo de la lista

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:fixed;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
      #pantalla_lista{display:none;}
      #pantalla_lista img{
        width:100%;
      }
      .cancion{
        display:flex;
      }
      .cancion .datostexto{flex:7;}
      .cancion>p{flex:1;}
    </style>
  </head>
  <body>
    <div id="pantallas">
      <div id="pantalla_inicio">
        <header>  
          <button>J</button>
          <button>Todos</button>
          <button>Música</button>
          <button>Podcasts</button>
        </header>
        <section id="favoritas">
          
         
        </section>
      </div>
      <div id="pantalla_lista">
        <img 
          src=""
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
        >
        <h3>Titulo de la lista</h3>
        
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
      </div>
    </div>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img 
          src="..."
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
          >
        <p>...</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          let articulo = instancia.querySelector("article")
          articulo.querySelector("p").textContent = dato.artist
          articulo.querySelector("img").setAttribute("src",dato.image)
          contenedor.appendChild(instancia)
          articulo.onclick = function(){
            console.log("Has hecho click en un articulo");
            document.querySelector("#pantalla_inicio").style.display = "none"
            document.querySelector("#pantalla_lista").style.display = "block"
          }
        })
      })
    </script>
  </body>
</html>
```

### footer

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

    <style>
      body,html{background:#121212;color:white;font-family:sans-serif;padding:5px;}
      body{display:flex;flex-direction:column;gap:20px;}
      header button{background:magenta;color:white;padding:10px;border:none;border-radius:30px;min-width:40px;}
      #favoritas{
        display:grid;
        grid-template-columns:auto auto;
        gap:10px;
      }
      section article img{
        height:40px;
      }
      section article{
        gap:20px;
        display:flex;
        align-items:center;
        background:#292929;
        border-radius:10px;
      }
      section article p{
        font-weight:bold;
      }
      #reproductor{
        width:91%;
        background:#541010;
        height:50px;
        border-radius:10px;
        padding:10px;
        position:fixed;
        top:80%;
        box-sizing:border-box;
        transition:all 1s;
        overflow:hidden;
      }
      .pantallacompleta{
        position:absolute !important;
        top:0px !important;
        left:0px;
        width:100% !important;
        height:100% !important;
      }
      #pantalla_lista{display:none;}
      #pantalla_lista img{
        width:100%;
      }
      .cancion{
        display:flex;
      }
      .cancion .datostexto{flex:7;}
      .cancion>p{flex:1;}
      footer{
        display:flex;
        position:fixed;
        width:100%;
        bottom:0px;
        left:0px;
      }
      footer button{
        width:100%;
        border:none;
        background:black;
        color:white;
      }
      footer button .emoji{
        font-size:32px;
      }
      #pantalla_inicio{
        display:flex;
        flex-direction:column;
        gap:20px;
      }
    </style>
  </head>
  <body>
    <div id="pantallas">
      <div id="pantalla_inicio">
        <header>  
          <button>J</button>
          <button>Todos</button>
          <button>Música</button>
          <button>Podcasts</button>
        </header>
        <section id="favoritas">
          
         
        </section>
      </div>
      <div id="pantalla_lista">
        <img 
          src=""
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
        >
        <h3>Titulo de la lista</h3>
        
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
        <article class="cancion">
          <div class="datostexto">
            <h4>Titulo de la cancion</h4>
            <p>Titulo del disco</p>
          </div>
          <p>...</p>
        </article>
      </div>
    </div>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
    <footer>
      <button>
        <div class="emoji">🏠</div>
        <p>Inicio</p>
      </button>
      <button>
        <div class="emoji">🔍</div>
        <p>Buscar</p>
      </button>
      <button>
        <div class="emoji">📚</div>
        <p>Tu biblioteca</p>
      </button>
      <button>
        <div class="emoji">➕</div>
        <p>Crear</p>
      </button>
    </footer>
    <div id="templates">
      <template id="elemento_lista">
        <article>
        <img 
          src="..."
          onerror="this.onerror=null; this.src='img/placeholder.png';"
          alt="Miniatura de la lista"
          >
        <p>...</p>
      </article>
      </template>
    </div>
    <script>
      /////////////////////////// REPRODUCTOR
      let reproductor = document.querySelector("#reproductor");
      reproductor.onclick = function(){
        this.classList.add("pantallacompleta")
      }
      /////////////////////////// POBLAR LISTA
      let contenedor = document.querySelector("#favoritas")
      
      fetch("api/favoritos.json")
      .then(function(respuesta){return respuesta.json()})
      .then(function(datos){
        console.log(datos)
        datos.favorites.forEach(function(dato){
          let plantilla = document.querySelector("#elemento_lista")
          let instancia = plantilla.content.cloneNode(true)
          let articulo = instancia.querySelector("article")
          articulo.querySelector("p").textContent = dato.artist
          articulo.querySelector("img").setAttribute("src",dato.image)
          contenedor.appendChild(instancia)
          articulo.onclick = function(){
            console.log("Has hecho click en un articulo");
            document.querySelector("#pantalla_inicio").style.display = "none"
            document.querySelector("#pantalla_lista").style.display = "block"
          }
        })
      })
    </script>
  </body>
</html>
```

<a id="tecnologias-de-desarrollo"></a>
## Tecnologías de desarrollo

En este capítulo, exploramos las tecnologías clave utilizadas para el desarrollo de aplicaciones en dispositivos móviles, abordando tanto los aspectos técnicos como los desafíos específicos que enfrentan estas plataformas. Comenzamos por una visión general del hardware y software que componen un dispositivo móvil, destacando las características distintivas que influyen en la elección de tecnologías para su desarrollo.

A continuación, nos sumergimos en el análisis de los principales motores de juegos existentes, examinando sus arquitecturas y componentes. Este estudio no solo nos proporciona conocimientos sobre cómo funcionan estos sistemas complejos, sino que también nos ayuda a entender las mejores prácticas para su desarrollo propio.

El capítulo continúa con una revisión detallada de las tecnologías utilizadas en el desarrollo de aplicaciones multimedia integradas. Desde la selección del API hasta el procesamiento y reproducción de objetos multimedia, cada paso es crucial para garantizar una experiencia óptima al usuario. También exploramos cómo estas tecnologías pueden ser adaptadas a diferentes formatos de contenido, desde imágenes hasta videos en 3D.

Además, dedicamos un espacio significativo a la análisis de las tecnologías más recientes y emergentes para el desarrollo de aplicaciones móviles. Esto incluye una visión de los dispositivos móviles actuales, su hardware y software, así como las últimas tendencias en tecnología que están transformando el mundo móvil.

Finalmente, concluimos con un análisis de cómo se pueden modificar aplicaciones existentes para adaptarlas a nuevas tecnologías. Este proceso requiere una comprensión profunda del código y la arquitectura de la aplicación, así como habilidades en programación y debugging avanzadas.

A lo largo de este capítulo, hemos cubierto un espectro completo de temas relacionados con el desarrollo de aplicaciones móviles, desde las tecnologías básicas hasta los conceptos más avanzados. Cada sección ha sido diseñada para proporcionar una comprensión profunda y práctica de cómo desarrollar aplicaciones que sean eficientes, seguras y atractivas para los usuarios finales.

<a id="emuladores-configuraciones"></a>
## Emuladores. Configuraciones

La configuración adecuada de emuladores es un paso crucial para desarrollar y probar aplicaciones móviles de manera eficiente. Los emuladores nos permiten ejecutar nuestras aplicaciones en entornos virtuales que imitan los sistemas operativos y las características específicas de dispositivos móviles, como Android o iOS. En esta subunidad, exploraremos cómo seleccionar el emulador adecuado para nuestro proyecto y cómo configurarlo correctamente.

El primer paso es elegir el emulador que mejor se adapte a nuestras necesidades. Para proyectos basados en Android, herramientas como Android Studio proporcionan un emulador integrado que ofrece una alta fielidad al sistema operativo real. Este emulador permite crear y gestionar múltiples dispositivos virtuales con diferentes configuraciones de hardware y software.

Una vez seleccionado el emulador, la configuración es esencial para garantizar que nuestra aplicación funcione correctamente en el entorno virtual. Esto implica establecer las características del dispositivo, como la resolución de pantalla, el tipo de almacenamiento interno y externo, y las aplicaciones instaladas por defecto. Además, es importante configurar las opciones de red para simular diferentes escenarios de conexión, lo que nos ayuda a probar cómo nuestra aplicación se comporta en condiciones reales.

La configuración del emulador también incluye la definición de variables de entorno y permisos específicos. Esto es crucial para asegurar que nuestras aplicaciones puedan acceder a los recursos necesarios y funcionen según lo esperado. Por ejemplo, si nuestra aplicación requiere acceso a la cámara o a las funciones de localización, debemos configurar estos permisos en el emulador.

Además de la configuración básica, es importante realizar pruebas exhaustivas para asegurar que nuestro emulador esté funcionando correctamente. Esto implica verificar que todos los servicios y funcionalidades están disponibles y que no hay errores o incompatibilidades. Además, es recomendable realizar pruebas de rendimiento para evaluar la capacidad del emulador para manejar carga de trabajo intensa.

La configuración del emulador también puede incluir la instalación de aplicaciones adicionales o el ajuste de las preferencias del sistema operativo. Esto nos permite simular diferentes escenarios de uso y probar cómo nuestra aplicación se comporta en condiciones reales. Por ejemplo, podemos instalar aplicaciones competenciales para evaluar la eficiencia de nuestro código o ajustar las preferencias del sistema para simular diferentes niveles de consumo de recursos.

La configuración del emulador es un proceso iterativo que requiere ajustes y refinamientos constantes. Es importante realizar pruebas frecuentes y recopilar feedback para mejorar la calidad de nuestra aplicación. Además, es recomendable mantener el emulador actualizado con las últimas versiones del sistema operativo y las herramientas de desarrollo para garantizar su funcionamiento óptimo.

En conclusión, la configuración adecuada de emuladores es un paso crucial para desarrollar y probar aplicaciones móviles de manera eficiente. Al seleccionar el emulador adecuado, configurarlo correctamente y realizar pruebas exhaustivas, podemos asegurar que nuestra aplicación funcione correctamente en diferentes entornos virtuales. Esta habilidad es fundamental para el desarrollo exitoso de aplicaciones móviles y nos permite probar nuestras aplicaciones en condiciones reales antes de su lanzamiento.

### compilado

```html
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="css/estilos.css">
  </head>
  <body>
    <div id="pantallas">
      <div id="pantalla_inicio">
  <header>  
    <button>J</button>
    <button>Todos</button>
    <button>Música</button>
    <button>Podcasts</button>
  </header>
  <section id="favoritas">
    
   
  </section>
</div>
<script>
  let contenedor = document.querySelector("#favoritas")
  
  fetch("api/favoritos.json")
  .then(function(respuesta){return respuesta.json()})
  .then(function(datos){
    console.log(datos)
    datos.favorites.forEach(function(dato){
      let plantilla = document.querySelector("#elemento_lista")
      let instancia = plantilla.content.cloneNode(true)
      let articulo = instancia.querySelector("article")
      articulo.querySelector("p").textContent = dato.artist
      articulo.querySelector("img").setAttribute("src",dato.image)
      contenedor.appendChild(instancia)
      articulo.onclick = function(){
        console.log("Has hecho click en un articulo");
        document.querySelector("#pantalla_inicio").style.display = "none"
        document.querySelector("#pantalla_lista").style.display = "block"
      }
    })
  })
</script>
      <style>
#pantalla_lista{display:none;}
#pantalla_lista img{
  width:100%;
}
.cancion{
  display:flex;
}
.cancion .datostexto{flex:7;}
.cancion>p{flex:1;}  
</style>
<div id="pantalla_lista">
  <img 
    src=""
    onerror="this.onerror=null; this.src='img/placeholder.png';"
    alt="Miniatura de la lista"
  >
  <h3>Titulo de la lista</h3>
  
  <article class="cancion">
    <div class="datostexto">
      <h4>Titulo de la cancion</h4>
      <p>Titulo del disco</p>
    </div>
    <p>...</p>
  </article>
  <article class="cancion">
    <div class="datostexto">
      <h4>Titulo de la cancion</h4>
      <p>Titulo del disco</p>
    </div>
    <p>...</p>
  </article>
  <article class="cancion">
    <div class="datostexto">
      <h4>Titulo de la cancion</h4>
      <p>Titulo del disco</p>
    </div>
    <p>...</p>
  </article>
  <article class="cancion">
    <div class="datostexto">
      <h4>Titulo de la cancion</h4>
      <p>Titulo del disco</p>
    </div>
    <p>...</p>
  </article>
  <article class="cancion">
    <div class="datostexto">
      <h4>Titulo de la cancion</h4>
      <p>Titulo del disco</p>
    </div>
    <p>...</p>
  </article>
  <article class="cancion">
    <div class="datostexto">
      <h4>Titulo de la cancion</h4>
      <p>Titulo del disco</p>
    </div>
    <p>...</p>
  </article>
</div>
    </div>
    <section id="reproductor">
      <h3>Artista</h3>
      <img src="josevicente.jpg">
      <audio src="0802.mp3" controls>
    </section>
<script>
  let reproductor = document.querySelector("#reproductor");
  reproductor.onclick = function(){
    this.classList.add("pantallacompleta")
  }  
</script>
    <style>
  footer{
    display:flex;
    position:fixed;
    width:100%;
    bottom:0px;
    left:0px;
  }
  footer button{
    width:100%;
    border:none;
    background:black;
    color:white;
  }
  footer button .emoji{
    font-size:32px;
  }
</style>
<footer>
  <button>
    <div class="emoji">🏠</div>
    <p>Inicio</p>
  </button>
  <button>
    <div class="emoji">🔍</div>
    <p>Buscar</p>
  </button>
  <button>
    <div class="emoji">📚</div>
    <p>Tu biblioteca</p>
  </button>
  <button>
    <div class="emoji">➕</div>
    <p>Crear</p>
  </button>
</footer>
    <div id="templates">
  <template id="elemento_lista">
    <article>
    <img 
      src="..."
      onerror="this.onerror=null; this.src='img/placeholder.png';"
      alt="Miniatura de la lista"
      >
    <p>...</p>
  </article>
  </template>
</div>
  </body>
</html>
```

### compilador

```
<?php
  ob_start();                  // Start capturing output
  include "index.php";        // Execute the PHP file
  $html = ob_get_clean();      // Get the generated HTML
  file_put_contents("compilado.html", $html);
?>
```

### index

```
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="css/estilos.css">
  </head>
  <body>
    <div id="pantallas">
      <?php include "componentes/pantalla_inicio.php";?>
      <?php include "componentes/pantalla_lista.php";?>
    </div>
    <?php include "componentes/reproductor.php";?>
    <?php include "componentes/footer.php" ?>
    <?php include "componentes/templates.php" ?>
  </body>
</html>
```

<a id="aplicaciones-moviles"></a>
## Aplicaciones móviles

En este capítulo, nos adentramos en la exploración de las aplicaciones móviles, un campo que ha experimentado una explosión en el último decenio. Las aplicaciones móviles han transformado nuestras vidas diarias, desde la forma en que consumimos noticias y entretenimiento hasta cómo interactuamos con nuestros bancos y servicios médicos. 

La arquitectura de las aplicaciones móviles es una combinación de elementos tecnológicos que permiten su desarrollo y ejecución en dispositivos móviles. El sistema operativo del dispositivo, como iOS o Android, proporciona la plataforma sobre la cual se construyen estas aplicaciones. Los lenguajes de programación utilizados para desarrollar aplicaciones móviles incluyen Java para Android y Swift para iOS, aunque existen otras opciones como Kotlin y Objective-C.

Las aplicaciones móviles pueden ser clasificadas en dos tipos principales: las que son nativas y las que son híbridas. Las aplicaciones nativas se compilan directamente en código específico del sistema operativo del dispositivo, lo que les permite acceder a todas sus funcionalidades y ofrecer una experiencia de usuario fluida y eficiente. Por otro lado, las aplicaciones híbridas utilizan frameworks como React Native o Flutter para construir interfaces de usuario utilizando lenguajes web como HTML, CSS y JavaScript, pero se ejecutan en un entorno nativo.

La seguridad es un aspecto crucial en el desarrollo de aplicaciones móviles. Los dispositivos móviles son a menudo menos seguros que los ordenadores de escritorio debido a su portabilidad y la naturaleza más limitada de su hardware. Por lo tanto, es fundamental implementar medidas de seguridad como autenticación fuerte, encriptación de datos y actualizaciones regulares del software.

Además de las aplicaciones móviles tradicionales que se ejecutan en teléfonos inteligentes, también hay una creciente popularidad de las aplicaciones basadas en realidad aumentada (AR) y realidad virtual (VR). Estas tecnologías utilizan los sensores del dispositivo para superponer información digital sobre el mundo físico, lo que abre nuevas posibilidades en áreas como la educación, el entretenimiento y la asistencia médica.

El desarrollo de aplicaciones móviles requiere un flujo de trabajo específico. A partir de la concepción inicial hasta la publicación final, los desarrolladores siguen una serie de pasos que incluyen la planificación del proyecto, la codificación, las pruebas, la depuración y la implementación en tiendas de aplicaciones como Google Play o la App Store.

En conclusión, el análisis de tecnologías para aplicaciones móviles es un campo diverso e interesante que abarca desde el desarrollo de software hasta la seguridad y la experiencia del usuario. Con el crecimiento constante del mercado de las aplicaciones móviles, es crucial mantenerse al día con las últimas tendencias y tecnologías para poder crear soluciones innovadoras y eficientes en este campo tan dinámico.

### Android Studio

```markdown
# Descargar Android Studio

https://developer.android.com/studio?hl=es-419

Paso 1: Instalar Android Studio
Paso 2: Arrancarlo

Paso 3: Creamos un empty activity

Nombre: AplicacionWeb
Nombre del paquete: com.jocarsa.aplicacionweb

1.-MainActivity.kt - Controlador

package com.jocarsa.aplicacionweb2

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
    }
}


acitivity_main.xml - vista

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

### Creo vista web

```markdown
1.-Arrastro Webview:

2.-Le  pongo id: mivistaweb

3.-Codigo resultante de la vista:
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Button"
        tools:layout_editor_absoluteX="160dp"
        tools:layout_editor_absoluteY="787dp" />

    <WebView
        android:id="@+id/mivistaweb"
        android:layout_width="409dp"
        android:layout_height="729dp"
        android:layout_marginStart="1dp"
        android:layout_marginTop="1dp"
        android:layout_marginEnd="1dp"
        android:layout_marginBottom="1dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>

Nuevo controlador:

package com.jocarsa.aplicacionweb2

import android.annotation.SuppressLint
import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        // Mantener el comportamiento de bordes del template
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        // Referencia al WebView definido en tu XML
        val webView = findViewById<WebView>(R.id.mivistaweb)

        // Para que los enlaces se abran dentro del WebView y no en el navegador externo
        webView.webViewClient = WebViewClient()

        // Muchas webs modernas necesitan JavaScript
        val settings = webView.settings
        settings.javaScriptEnabled = true

        // Cargar la página
        webView.loadUrl("https://jocarsa.com")
    }

    // Opcional pero recomendable: botón atrás navega en el historial del WebView
    override fun onBackPressed() {
        val webView = findViewById<WebView>(R.id.mivistaweb)
        if (webView.canGoBack()) {
            webView.goBack()
        } else {
            super.onBackPressed()
        }
    }
}
```

### creo html local

```markdown
app/
 └─ src/
     └─ main/
         ├─ java/
         ├─ res/
         └─ assets/
              └─ index.html
              
<!doctype html>
<html>
    <head>
        <style>
            h1{color:red;}
        </style>
    </head>
    <body>
        <h1>Hola mundo</h1>
        <script>
            let titulo = document.querySelector("h1")
            titulo.onclick = function(){
                titulo.style.color = "green";
            }
        </script>
    </body>
</html>
```

<a id="modelo-de-estados-de-una-aplicacion-movil-activo-pausa-y-destruido"></a>
## Modelo de estados de una aplicación móvil activo, pausa y destruido

En un entorno móvil, las aplicaciones pueden experimentar cambios de estado que afectan su comportamiento y funcionalidad. El modelo de estados de una aplicación móvil activo, pausa y destruido es fundamental para entender cómo se manejan estos cambios y mantener la eficiencia del sistema.

Cuando una aplicación entra en el estado activo, está lista para interactuar con el usuario y realizar operaciones como la carga de datos o la ejecución de procesos intensivos. Este estado es típicamente el inicial después de que la aplicación ha sido iniciada o restaurada desde un estado pausado o destruido.

El estado pausa ocurre cuando una aplicación pierde el foco pero aún está en ejecución. Esto puede suceder cuando otro aplicativo se pone en primer plano, como cuando el usuario navega a otra pantalla dentro del mismo dispositivo. Durante este estado, la aplicación debe liberar recursos y minimizar su consumo de energía para no afectar negativamente la experiencia del usuario.

El estado destruido es el final del ciclo de vida de una aplicación móvil. Ocurre cuando un sistema operativo decide cerrar una aplicación para liberar memoria o cuando el usuario cierra manualmente la aplicación a través de los controles de la interfaz del dispositivo. En este estado, toda la información y recursos utilizados por la aplicación se liberan, preparando el camino para su reinicio en el futuro.

La transición entre estos estados es controlada por el sistema operativo del dispositivo móvil, que asegura una gestión eficiente de los recursos y una experiencia fluida para el usuario. Durante la pausa, la aplicación puede guardar su estado actual para poder recuperarlo rápidamente cuando vuelva a estar activa, lo que mejora la continuidad del flujo de trabajo.

Es importante destacar que cada estado tiene sus propias implicaciones en términos de funcionalidad y rendimiento. Por ejemplo, una aplicación en pausa debe ser capaz de responder rápidamente a un cambio de estado a activo sin perder datos o estado interno. En el caso del estado destruido, la aplicación debe estar preparada para reiniciarse desde cero o desde un punto de guardado previo.

La comprensión y gestión adecuada de estos estados son cruciales para desarrollar aplicaciones móviles eficientes y responsivas. Al diseñar e implementar las funcionalidades de una aplicación, es necesario considerar cómo se comportará en cada estado del ciclo de vida, asegurando que la experiencia del usuario sea coherente y sin interrupciones innecesarias.

En resumen, el modelo de estados activo, pausa y destruido en aplicaciones móviles proporciona una estructura clara para gestionar los cambios de estado y optimizar el uso de recursos. Al entender y aprovechar estos estados, los desarrolladores pueden crear aplicaciones que ofrezcan un rendimiento óptimo y una experiencia de usuario fluida, adaptándose a las necesidades cambiantes del dispositivo y del usuario.

### compilador

```
<?php

// ---- CONFIG ----
$destination = "/home/josevicente/AndroidStudioProjects/Aplicacionweb2/app/src/main/assets/";

// Ensure destination exists
if (!is_dir($destination)) {
    mkdir($destination, 0777, true);
}

// ---- 1. Compile index.php into index.html ----
ob_start();
include "index.php";
$html = ob_get_clean();

// Save compiled html
file_put_contents($destination . "index.html", $html);


// ---- 2. Recursive copy function ----
function copyRecursive($source, $dest) {
    if (is_dir($source)) {
        if (!is_dir($dest)) {
            mkdir($dest, 0777, true);
        }

        $items = scandir($source);
        foreach ($items as $item) {
            if ($item == "." || $item == "..") continue;

            $srcPath = $source . "/" . $item;
            $destPath = $dest . "/" . $item;

            if (is_dir($srcPath)) {
                copyRecursive($srcPath, $destPath);
            } else {
                copy($srcPath, $destPath);
            }
        }
    } else {
        copy($source, $dest);
    }
}


// ---- 3. Copy folders ----
$folders = ["static"];

foreach ($folders as $folder) {
    if (is_dir($folder)) {
        copyRecursive($folder, $destination . $folder);
    }
}

echo "✅ Compilation complete\n";

?>
```

### index

```
<!doctype html>
<html lang="es">
  <head>
    <title>TAMEify</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="static/css/estilos.css">
  </head>
  <body>
    <div id="pantallas">
      <?php include "componentes/pantalla_inicio.php";?>
      <?php include "componentes/pantalla_lista.php";?>
    </div>
    <?php include "componentes/reproductor.php";?>
    <?php include "componentes/footer.php" ?>
    <?php include "componentes/templates.php" ?>
  </body>
</html>
```

<a id="ciclo-de-vida-de-una-aplicacion"></a>
## Ciclo de vida de una aplicación

El ciclo de vida de una aplicación móvil es un proceso dinámico que abarca desde su creación hasta su desinstalación del dispositivo del usuario. Este ciclo incluye varias fases cruciales que son fundamentales para el correcto funcionamiento y la experiencia del usuario final.

La fase inicial del ciclo de vida comienza con la instalación de la aplicación en el dispositivo. Durante este proceso, se verifica la compatibilidad del sistema operativo con las necesidades de la aplicación, se instalan los recursos necesarios y se configuran los parámetros iniciales. Es importante que esta fase sea eficiente para evitar retrasos innecesarios en la experiencia del usuario.

Una vez instalada, la aplicación entra en el estado "activo". En este modo, la aplicación está lista para interactuar con el usuario. El sistema operativo asigna recursos como memoria y CPU a la aplicación, permitiendo que funcione correctamente. Es durante esta fase donde se realizan las operaciones principales de la aplicación, como la carga de datos, la ejecución de procesos y la respuesta a los eventos del usuario.

El ciclo de vida también incluye el estado "pausa". Este ocurre cuando la aplicación pierde el foco pero aún está en el dispositivo. En este estado, la aplicación puede seguir consumiendo recursos, lo que es útil para mantener su estado actual sin necesidad de reiniciarla desde cero. Sin embargo, es importante optimizar el uso de recursos durante esta fase para evitar sobrecargas del sistema.

La fase final del ciclo de vida es el "destrucción". Este ocurre cuando la aplicación se cierra o se desinstala del dispositivo. Durante este proceso, se libera toda la memoria y los recursos asignados a la aplicación, asegurando que no queden residuos en el sistema operativo. Es crucial que esta fase sea eficiente para mantener el rendimiento general del dispositivo.

Además de estas fases principales, existen otros estados intermedios como "inactiva" o "suspendida". En el estado inactiva, la aplicación sigue consumiendo recursos pero no está procesando ninguna operación. En el estado suspendida, la aplicación puede ser reanudada rápidamente sin necesidad de reiniciarla.

El manejo adecuado del ciclo de vida es crucial para optimizar la experiencia del usuario y mantener el rendimiento del dispositivo. Al implementar correctamente las fases activo, pausa y destrucción, se asegura que la aplicación funcione eficientemente incluso en entornos con recursos limitados.

Además, es importante considerar los eventos que pueden interrumpir el ciclo de vida de una aplicación, como cambios de orientación del dispositivo o la entrada de un nuevo usuario. El manejo adecuado de estos eventos permite a la aplicación mantener su estado y proporcionar una experiencia fluida para el usuario.

En resumen, el ciclo de vida de una aplicación móvil es un proceso complejo que implica varias fases cruciales desde la instalación hasta la desinstalación. Cada fase tiene sus propias consideraciones y optimizaciones importantes para garantizar una buena experiencia del usuario y mantener el rendimiento del dispositivo.

<a id="modificacion-de-aplicaciones-existentes"></a>
## Modificación de aplicaciones existentes

En la evolución constante del desarrollo de aplicaciones para dispositivos móviles, el análisis de tecnologías existentes es una habilidad crucial que permite a los desarrolladores adaptarse rápidamente a nuevas plataformas y herramientas. Esta subunidad se centra específicamente en cómo modificar aplicaciones existentes, un proceso fundamental para mantener la relevancia y eficiencia de las soluciones tecnológicas.

La modificación de aplicaciones existentes implica no solo actualizar el código fuente, sino también considerar aspectos como la interfaz de usuario, la funcionalidad adicional y la optimización del rendimiento. Para lograr esto, es esencial entender los fundamentos de las plataformas móviles en las que se desarrollan las aplicaciones, ya sean Android o iOS.

En el caso de Android, una aplicación existente puede ser modificada utilizando lenguajes como Java o Kotlin, dependiendo del proyecto y las preferencias del equipo. Los desarrolladores pueden utilizar herramientas como Android Studio para realizar cambios en la interfaz gráfica de usuario (UI) y en el código fuente, asegurándose de que los cambios sean coherentes con las mejores prácticas de diseño y rendimiento.

Para iOS, el proceso es similar pero se utiliza Swift o Objective-C. Xcode es la herramienta principal para desarrollar aplicaciones iOS, proporcionando una plataforma robusta para modificar y mejorar las aplicaciones existentes. Los desarrolladores pueden utilizar Storyboards o Interface Builder para actualizar la UI de manera visual, mientras que el código fuente puede ser modificado directamente en los archivos del proyecto.

Además de la actualización del código y la interfaz, es importante considerar la integración con nuevas funcionalidades y servicios. Esto puede implicar agregar soporte para nuevas APIs o bibliotecas, lo cual requiere un conocimiento profundo de las plataformas móviles y sus características. Por ejemplo, si una aplicación necesita utilizar el GPS para determinar la ubicación del usuario, los desarrolladores deberán aprender sobre las API de geolocalización disponibles en Android e iOS.

La modificación de aplicaciones existentes también implica la gestión de dependencias y bibliotecas externas. Es crucial mantener un control riguroso sobre estas dependencias para evitar conflictos de versión y problemas de rendimiento. Herramientas como Gradle (para Android) o CocoaPods (para iOS) pueden ser utilizadas para gestionar eficientemente las dependencias, asegurando que todas las bibliotecas estén actualizadas y funcionen correctamente.

Además de los cambios técnicos, la modificación de aplicaciones existentes también requiere una comprensión profunda del negocio y del usuario final. Los desarrolladores deben trabajar en estrecha colaboración con equipos de negocio y marketing para entender las necesidades cambiantes del mercado y adaptar las aplicaciones a estas demandas. Esto puede implicar la implementación de nuevas características, la optimización de flujos de trabajo o incluso el cambio de arquitecturas completas si es necesario.

La modificación de aplicaciones existentes también implica la realización de pruebas exhaustivas para asegurar que los cambios no introduzcan errores. Los desarrolladores pueden utilizar herramientas como Espresso (para Android) o XCTest (para iOS) para realizar pruebas automatizadas, lo cual ayuda a garantizar que las aplicaciones sigan funcionando correctamente después de las modificaciones.

En conclusión, la modificación de aplicaciones existentes es un proceso complejo pero fundamental en el desarrollo de software para dispositivos móviles. Requiere una combinación de conocimientos técnicos profundos, habilidades de adaptación y colaboración con equipos de negocio y marketing. A través del análisis de tecnologías existentes, los desarrolladores pueden mantener su competencia y ofrecer soluciones innovadoras y eficientes a las necesidades cambiantes del mercado.

<a id="utilizacion-del-entorno-de-ejecucion-del-administrador-de-aplicaciones"></a>
## Utilización del entorno de ejecución del administrador de aplicaciones

En el mundo digital actual, los dispositivos móviles desempeñan un papel crucial en la interacción con las aplicaciones. El entorno de ejecución del administrador de aplicaciones es una parte fundamental de esta interacción, proporcionando las herramientas necesarias para que las aplicaciones funcionen correctamente y de manera segura.

El administrador de aplicaciones es el encargado de gestionar todas las aplicaciones instaladas en un dispositivo móvil. Su principal función es mantener las aplicaciones actualizadas, instalar nuevas versiones cuando sean disponibles, y manejar la memoria disponible para asegurar que cada aplicación tenga lo necesario para funcionar sin problemas.

Para interactuar con el administrador de aplicaciones desde una aplicación propia, se utilizan APIs (Interfaces de Programación de Aplicaciones) específicas. Estas APIs proporcionan métodos y funciones que permiten a las aplicaciones realizar tareas como iniciar o detener otras aplicaciones, solicitar permisos adicionales, gestionar la preferencia del usuario y acceder a ciertas funcionalidades del sistema.

Es importante destacar que el entorno de ejecución del administrador de aplicaciones también es responsable de la gestión de los recursos del dispositivo. Esto incluye la asignación de memoria, la control de la batería y la optimización del rendimiento para mantener las aplicaciones funcionando eficientemente incluso cuando se están ejecutando varias al mismo tiempo.

Además, el administrador de aplicaciones es un punto crucial en la seguridad de las aplicaciones móviles. Algunas de sus funciones incluyen la verificación de los permisos solicitados por una aplicación y la capacidad de desinstalar aplicaciones que puedan estar causando problemas o amenazando la seguridad del dispositivo.

La utilización del entorno de ejecución del administrador de aplicaciones requiere un conocimiento profundo de las APIs específicas disponibles para cada plataforma móvil (iOS, Android, etc.). Cada plataforma tiene sus propias características y restricciones, lo que significa que los desarrolladores deben adaptarse a estas diferencias para asegurar que sus aplicaciones funcionen correctamente en cualquier dispositivo.

En resumen, el entorno de ejecución del administrador de aplicaciones es un componente integral del desarrollo de aplicaciones móviles. Proporciona las herramientas necesarias para gestionar y optimizar la ejecución de las aplicaciones, asegurando que estas funcione de manera eficiente y segura en los dispositivos móviles modernos.


<a id="desarrollo-de-aplicaciones-para-dispositivos-moviles"></a>
# Desarrollo de aplicaciones para dispositivos móviles

<a id="herramientas-flujo-de-trabajo"></a>
## Herramientas. Flujo de trabajo

En este capítulo, exploramos las herramientas y técnicas esenciales para desarrollar aplicaciones móviles, abordando desde el entorno de desarrollo hasta los flujos de trabajo que facilitan la creación eficiente de software para dispositivos móviles. Comenzamos por introducir las principales herramientas disponibles en el mercado, destacando su funcionalidad y cómo pueden optimizar el proceso de codificación y depuración.

A medida que avanzamos, nos sumergimos en los flujos de trabajo recomendados para el desarrollo de aplicaciones móviles. Estos procesos incluyen la planificación del proyecto, la definición de requisitos, el diseño de interfaces de usuario, la implementación del código y las pruebas exhaustivas. Cada paso es crucial para garantizar que la aplicación sea funcional, segura y atractiva para los usuarios finales.

Además, examinamos cómo integrar diferentes componentes dentro de un proyecto móvil, como bases de datos locales, servicios web y sensores del dispositivo. Estas integraciones requieren una comprensión profunda de las APIs disponibles y la capacidad de gestionar eficazmente los recursos limitados de los dispositivos móviles.

El capítulo también aborda el tema de la seguridad en aplicaciones móviles, destacando la importancia de implementar medidas de protección adecuadas desde el principio del desarrollo. Esto incluye la gestión segura de datos, la autenticación y autorización de usuarios y la prevención de vulnerabilidades comunes.

Finalmente, concluimos con una reflexión sobre los desafíos y mejores prácticas en el desarrollo de aplicaciones móviles. Aprenderemos cómo adaptarse a las variadas plataformas (iOS y Android) y cómo mantenerse al día con las últimas tendencias y tecnologías en el campo del desarrollo móvil.

Este capítulo es un punto de partida valioso para cualquier desarrollador que quiera comenzar su viaje en la creación de aplicaciones móviles, proporcionando una base sólida en herramientas y procesos que facilitan el desarrollo eficiente y exitoso.

<a id="componentes-de-una-aplicacion-recursos"></a>
## Componentes de una aplicación. Recursos

En el desarrollo de aplicaciones para dispositivos móviles, los componentes de una aplicación y sus recursos son fundamentales para su estructura y funcionamiento. Los componentes representan las partes individuales que componen la interfaz del usuario y su funcionalidad, mientras que los recursos proporcionan los elementos necesarios para su visualización y operación.

Los componentes principales de una aplicación móvil incluyen Activity, Fragment, Service y BroadcastReceiver. Cada uno desempeña un papel específico en el ciclo de vida de la aplicación y en la interacción con el usuario. Por ejemplo, las Activities son pantallas individuales que se ven al usuario, mientras que los Fragments son partes reutilizables dentro de una Activity. Los Services ejecutan tareas en segundo plano sin necesidad de interactuar directamente con el usuario, y los BroadcastReceivers escuchan eventos del sistema y pueden responder a ellos.

Además de estos componentes, las aplicaciones móviles requieren recursos para su funcionamiento. Estos recursos incluyen archivos de texto, imágenes, sonidos y videos que se utilizan en la interfaz gráfica y en el procesamiento multimedia. Los recursos se organizan en carpetas específicas dentro del proyecto, como `res/drawable` para las imágenes, `res/layout` para los diseños de pantalla y `res/values` para los strings y otros valores constantes.

La gestión eficiente de estos componentes y recursos es crucial para el rendimiento y la experiencia del usuario. Es importante entender cómo se crean, utilizan y liberan estos recursos para evitar fugas de memoria y problemas de rendimiento. Además, la organización adecuada de los componentes en diferentes Activity o Fragment permite una estructura modular y fácil mantenimiento del código.

En resumen, el desarrollo de aplicaciones móviles implica un equilibrio entre la creación de componentes funcionalidades y la gestión eficiente de recursos para garantizar una buena experiencia al usuario. Cada componente y recurso desempeña un papel importante en la construcción y funcionamiento de las aplicaciones móviles, y su comprensión es fundamental para desarrolladores que quieran crear software de alta calidad y rendimiento.

<a id="interfaces-de-usuario-clases-asociadas"></a>
## Interfaces de usuario. Clases asociadas

En este capítulo, nos adentramos en la creación de interfaces de usuario para aplicaciones móviles, una tarea fundamental que requiere un equilibrio entre funcionalidad y experiencia del usuario. Las interfaces de usuario (UI) son el punto de contacto directo con los usuarios finales, por lo que su diseño debe ser intuitivo, atractivo y eficiente.

Las interfaces de usuario en aplicaciones móviles se construyen utilizando clases asociadas que proporcionan una estructura y funcionalidad predefinida. Estas clases son fundamentales para definir la apariencia y el comportamiento de los elementos gráficos como botones, cajas de texto, listas desplegables y más. Cada clase tiene atributos y métodos que permiten personalizar su apariencia y funcionalidad según las necesidades del proyecto.

Una de las clases más importantes en la creación de interfaces de usuario es `View`, que es la superclase de todos los elementos visuales en una interfaz de usuario. Cada vista tiene propiedades como el tamaño, la posición, el color de fondo y el texto, entre otros, que pueden ser modificados para adaptarla a las preferencias del diseño.

Además de `View`, existen clases específicas para diferentes tipos de elementos gráficos. Por ejemplo, `Button` es una clase que representa un botón en la interfaz de usuario. Los botones son elementos interactivos que permiten al usuario realizar acciones como enviar datos o navegar entre pantallas. Cada botón tiene propiedades adicionales como el texto del botón y los eventos asociados a su presión.

Otra clase importante es `TextView`, que se utiliza para mostrar texto en la interfaz de usuario. Los textos pueden ser estáticos, dinámicos o interactivos, dependiendo de cómo se configuren las propiedades del objeto `TextView`. Esta clase también permite el uso de diferentes fuentes y estilos de texto, lo que facilita la creación de interfaces de usuario atractivas.

Además de estas clases básicas, existen otras clases que proporcionan funcionalidades adicionales para mejorar la experiencia del usuario. Por ejemplo, la clase `RecyclerView` es utilizada para mostrar listas desplegables con un gran número de elementos. Esta clase optimiza el rendimiento al reutilizar vistas ya infladas en lugar de crear nuevas cada vez que se necesita mostrar un nuevo elemento.

La creación de interfaces de usuario también implica el manejo de eventos, como los clics y las pulsaciones. Las clases asociadas proporcionan métodos para detectar estos eventos y ejecutar acciones correspondientes. Por ejemplo, la clase `Button` tiene un método `onClick()` que se ejecuta cuando el botón es presionado por el usuario.

En resumen, la creación de interfaces de usuario en aplicaciones móviles implica el uso de clases asociadas que proporcionan una estructura y funcionalidad predefinida. Cada clase tiene atributos y métodos que permiten personalizar su apariencia y comportamiento según las necesidades del proyecto. Comprender estas clases es crucial para crear interfaces de usuario eficientes, atractivas y funcionales que mejoren la experiencia del usuario final.

<a id="contexto-grafico-imagenes"></a>
## Contexto gráfico. Imágenes

En el desarrollo de aplicaciones para dispositivos móviles, el contexto gráfico desempeña un papel crucial ya que define cómo se presentan los elementos visuales a los usuarios. Este aspecto es fundamental para crear interfaces intuitivas y atractivas, lo que puede influir significativamente en la experiencia del usuario final.

El contexto gráfico se refiere a las características de la pantalla en la que se ejecuta la aplicación, incluyendo su tamaño, resolución y orientación. Cada dispositivo móvil tiene especificidades técnicas que deben ser consideradas al diseñar una interfaz gráfica adaptada. Por ejemplo, los teléfonos inteligentes tienen pantallas táctiles de diferentes tamaños y densidades de píxeles, lo que requiere un diseño flexible que se ajuste a estas variaciones.

La gestión del contexto gráfico en aplicaciones móviles implica la utilización de bibliotecas y APIs específicas para cada plataforma. Por ejemplo, en Android, se utiliza el sistema de recursos (Resources) para gestionar diferentes layouts y estilos según el tamaño de pantalla o la orientación del dispositivo. En iOS, el Auto Layout es una herramienta poderosa que permite crear interfaces gráficas que se ajusten automáticamente a cualquier tamaño de pantalla.

Además del contexto gráfico, los diseños de aplicaciones móviles deben considerar otros factores como la accesibilidad y la eficiencia en términos de rendimiento. La utilización de imágenes es una parte integral de estos aspectos, ya que las imágenes pueden mejorar significativamente la experiencia del usuario al proporcionar información visual clara y atractiva.

Las imágenes en aplicaciones móviles pueden ser cargadas desde diferentes fuentes, como archivos locales o servicios web. Es importante optimizar estas imágenes para asegurar un rendimiento óptimo, lo que puede implicar reducir su tamaño sin afectar su calidad visual. Herramientas de compresión de imágenes y técnicas de codificación adecuadas son esenciales en este proceso.

La gestión del contexto gráfico también implica la consideración de los estados de vida de una aplicación móvil. Durante el desarrollo, es común que las aplicaciones pasen por diferentes estados como activo, pausado o destruido. Es importante manejar adecuadamente estos estados para evitar pérdidas de datos y mantener la consistencia del estado de la interfaz gráfica.

En conclusión, el contexto gráfico es un aspecto fundamental en el desarrollo de aplicaciones móviles. Al considerar las características específicas de los dispositivos, utilizar bibliotecas adecuadas y optimizar imágenes, se pueden crear interfaces gráficas que ofrezcan una experiencia óptima al usuario final. Además, la gestión eficiente del contexto gráfico es crucial para mantener el rendimiento y la funcionalidad de las aplicaciones en diferentes entornos.

<a id="metodos-de-entrada-eventos"></a>
## Métodos de entrada. Eventos

En este capítulo, nos adentramos en los fundamentos del desarrollo de aplicaciones para dispositivos móviles, con un énfasis especial en los métodos de entrada y eventos. Comenzamos por entender el contexto gráfico, que es crucial para cualquier aplicación móvil, ya que define cómo se presentan los elementos visuales al usuario. Aprenderemos sobre las clases asociadas a la interfaz gráfica de usuario (GUI), como `View` y `Activity`, que son los bloques fundamentales de cualquier aplicación Android.

Continuamos explorando el concepto de eventos, que son acciones realizadas por el usuario o por el sistema operativo que provocan una respuesta en la aplicación. Aprenderemos cómo manejar diferentes tipos de eventos, como clics, desplazamientos y cambios de orientación del dispositivo, utilizando los listeners correspondientes. Esto nos permitirá crear aplicaciones interactivas y responsivas.

Además, profundizaremos en el procesamiento de entrada, que implica capturar y interpretar las acciones del usuario para realizar tareas específicas dentro de la aplicación. Aprenderemos sobre los diferentes tipos de sensores disponibles en los dispositivos móviles, como acelerómetros, giroscopios y cámaras, y cómo utilizarlos para mejorar la funcionalidad de nuestra aplicación.

A medida que avanzamos, nos familiarizaremos con el ciclo de vida de una aplicación móvil, comprendiendo las diferentes fases en las que puede estar (activa, pausada, detenida) y cómo manejar estas transiciones para optimizar el rendimiento y la eficiencia del dispositivo. También aprenderemos sobre la gestión de preferencias de la aplicación, lo cual es fundamental para personalizar la experiencia del usuario sin necesidad de reiniciar la aplicación.

Continuamos con una exploración detallada de las bases de datos y almacenamiento en aplicaciones móviles, comprendiendo cómo utilizar SQLite o Firebase Realtime Database para persistir datos de manera segura y eficiente. Aprenderemos sobre el manejo de transacciones y la implementación de estrategias de sincronización para mantener los datos actualizados en diferentes dispositivos.

Además, nos adentramos en el tema de tareas en segundo plano y servicios, aprendiendo cómo ejecutar operaciones que no interfieren con la experiencia del usuario principal. Esto es crucial para aplicaciones que requieren realizar descargas de archivos, envíos de notificaciones o actualizaciones periódicas.

Finalmente, exploramos aspectos de seguridad y permisos en aplicaciones móviles, comprendiendo cómo gestionar los permisos necesarios para acceder a características del dispositivo (como la cámara o el GPS) y cómo proteger la información sensible almacenada en la aplicación. Aprenderemos sobre las mejores prácticas de programación segura y cómo implementar mecanismos de control de acceso para prevenir accesos no autorizados.

A lo largo de este capítulo, hemos cubierto una amplia gama de temas relacionados con el desarrollo de aplicaciones móviles, desde los métodos de entrada hasta la gestión de permisos y seguridad. Cada concepto ha sido presentado en un contexto práctico, preparándonos para desarrollar aplicaciones móviles interactivas, eficientes y seguras.

<a id="gestion-de-las-preferencias-de-la-aplicacion"></a>
## Gestión de las preferencias de la aplicación

En el desarrollo de aplicaciones para dispositivos móviles, la gestión de las preferencias del usuario es un aspecto crucial que aporta una mejor experiencia al usuario. Las preferencias pueden incluir opciones como idioma, tema de interfaz, tamaño de texto, notificaciones y más. La gestión efectiva de estas preferencias no solo mejora la usabilidad del software, sino que también aumenta su adaptabilidad a diferentes tipos de usuarios.

Para implementar la gestión de las preferencias en una aplicación móvil, se pueden utilizar los mecanismos proporcionados por el sistema operativo o frameworks específicos. En Android, por ejemplo, se puede utilizar la clase `SharedPreferences` para almacenar y recuperar preferencias de manera sencilla. Esta clase permite guardar pares clave-valor que pueden ser accedidos y modificados en cualquier parte de la aplicación.

La gestión de las preferencias implica no solo el almacenamiento, sino también su recuperación y actualización. Al iniciar la aplicación, se debe cargar la configuración del usuario desde `SharedPreferences` y aplicarla a los elementos de interfaz correspondientes. Además, es importante proporcionar una forma para el usuario de modificar sus preferencias, lo que puede hacerse mediante opciones en un menú o pantalla de ajustes.

Además de las preferencias generales, algunas aplicaciones pueden requerir preferencias específicas relacionadas con la funcionalidad del software. Por ejemplo, si se está desarrollando una aplicación de música, podría ser útil almacenar preferencias como el volumen actual, la lista de reproducción favorita o los artistas recientes escuchados.

La gestión de las preferencias también debe considerar la seguridad y privacidad del usuario. Es importante que las preferencias no contengan información sensible y que se implementen medidas para proteger la integridad y confidencialidad de estos datos.

En el contexto de aplicaciones móviles, la gestión de las preferencias es un componente integral del flujo de trabajo de desarrollo. Desde la planificación inicial hasta la implementación y pruebas, es necesario considerar cómo se almacenarán y utilizarán las preferencias del usuario para asegurar una experiencia óptima y personalizada.

La gestión efectiva de las preferencias no solo mejora la usabilidad del software, sino que también aumenta su adaptabilidad a diferentes tipos de usuarios. Al proporcionar opciones para personalizar la aplicación, se permite a los usuarios experimentar con diferentes configuraciones hasta encontrar aquella que les resulte más cómoda y eficiente.

En resumen, la gestión de las preferencias es un aspecto fundamental en el desarrollo de aplicaciones móviles. Permite una mejor experiencia al usuario, aumenta la adaptabilidad del software y contribuye a su éxito en el mercado competitivo. Al implementar esta funcionalidad con cuidado y consideración por la seguridad y privacidad del usuario, se puede crear aplicaciones que sean no solo funcionales, sino también bien recibidas y utilizadas por los usuarios finales.

<a id="bases-de-datos-y-almacenamiento"></a>
## Bases de datos y almacenamiento

En este capítulo, nos adentramos en los fundamentos del almacenamiento de datos dentro de aplicaciones móviles, un aspecto crucial para el desarrollo eficiente y funcional de estas plataformas. Comenzamos por explorar las diferentes formas de almacenamiento de datos, desde la utilización de archivos locales hasta la integración con bases de datos en la nube.

El primer método que vemos es el almacenamiento local mediante archivos. Este enfoque permite guardar información persistente en el dispositivo del usuario, lo que es ideal para aplicaciones que requieren acceso rápido y offline. A través de clases como `SharedPreferences` en Android o `UserDefaults` en iOS, podemos leer, escribir y eliminar datos de manera sencilla.

Sin embargo, cuando la cantidad de datos a almacenar aumenta o necesitamos una mayor flexibilidad y funcionalidad, el uso de bases de datos locales se convierte en una opción más adecuada. En Android, SQLite es la base de datos relacional por defecto, mientras que iOS utiliza Core Data para manejar sus objetos persistentes. Estas herramientas nos permiten crear tablas, insertar registros, realizar consultas y gestionar transacciones con facilidad.

La integración con bases de datos en la nube es otro camino valioso, especialmente cuando nuestras aplicaciones necesitan sincronizar datos entre diferentes dispositivos o incluso plataformas. Firebase Database y Firestore son opciones populares que ofrecen una solución escalable y fácil de usar para almacenar y recuperar información en tiempo real.

Además de los métodos de almacenamiento tradicionales, también debemos considerar el uso de bases de datos orientadas a documentos como MongoDB Atlas o Firebase Realtime Database. Estas bases de datos nos permiten almacenar y consultar datos de manera flexible, adaptándose mejor a las necesidades cambiantes de nuestras aplicaciones.

La gestión de la persistencia en aplicaciones móviles es un aspecto que requiere atención especial. Debemos considerar factores como la eficiencia del acceso a los datos, la seguridad de la información y la capacidad de manejar cambios en el diseño de las tablas o colecciones. Utilizar patrones de diseño como Singleton para gestionar la conexión con la base de datos puede ayudar a optimizar el rendimiento.

Finalmente, es importante mencionar que la gestión de los permisos de acceso a la información es un aspecto crucial cuando trabajamos con bases de datos en aplicaciones móviles. Debemos asegurarnos de que solo se acceda a los datos necesarios y que se implementen políticas de seguridad adecuadas para proteger la privacidad del usuario.

En resumen, el almacenamiento de datos es un componente fundamental en el desarrollo de aplicaciones móviles. Al comprender las diferentes opciones disponibles y cómo gestionarlos eficazmente, podemos crear aplicaciones que ofrezcan una experiencia fluida y segura al usuario.

<a id="persistencia"></a>
## Persistencia

En la subunidad "Persistencia" del desarrollo de aplicaciones para dispositivos móviles, se aborda el aspecto crucial de almacenar datos de manera segura y eficiente. La persistencia es fundamental para mantener la funcionalidad y la experiencia del usuario, permitiendo que los datos no se pierdan cuando la aplicación se cierra o el dispositivo reinicia.

La primera consideración en la persistencia es identificar qué tipo de datos necesita ser almacenado. Los datos pueden clasificarse en dos categorías principales: datos estructurados y datos no estructurados. Los datos estructurados, como registros de usuarios o preferencias del usuario, se almacenan generalmente en bases de datos relacionales o NoSQL. Por otro lado, los datos no estructurados, como imágenes o videos, requieren un almacenamiento más complejo.

Para el almacenamiento de datos estructurados, las aplicaciones móviles pueden utilizar SQLite, una base de datos ligera y eficiente que se integra bien con la mayoría de los entornos de desarrollo. SQLite permite crear tablas, insertar registros, realizar consultas y gestionar transacciones, lo que es esencial para mantener la consistencia y la integridad de los datos.

Los datos no estructurados son un desafío mayor debido a su naturaleza compleja y variada. Para almacenar imágenes o videos, las aplicaciones pueden utilizar el sistema de archivos del dispositivo, donde se pueden crear carpetas específicas para cada tipo de archivo. Además, existen bibliotecas que facilitan la manipulación de estos tipos de datos, como Glide para imágenes en Android o AVFoundation para videos en iOS.

La persistencia también implica la seguridad de los datos. Es crucial implementar medidas de cifrado y protección contra accesos no autorizados. Las aplicaciones móviles pueden utilizar librerías de criptografía para cifrar datos sensibles antes de almacenarlos, asegurando que incluso si el dispositivo es robado o infectado, los datos no puedan ser accedidos sin la clave correcta.

Además de la persistencia local, las aplicaciones móviles también pueden utilizar servicios en la nube para almacenar y sincronizar datos. Los servicios como Firebase o AWS Amplify ofrecen soluciones robustas para el almacenamiento de datos en la nube, permitiendo una fácil implementación y escalabilidad.

La gestión de la persistencia también implica la optimización del espacio de almacenamiento. Las aplicaciones deben ser conscientes de su uso de memoria y almacenamiento, eliminando archivos temporales o no utilizados regularmente para mantener el dispositivo limpio y eficiente.

En conclusión, la persistencia es un aspecto integral del desarrollo de aplicaciones móviles que requiere una consideración cuidadosa. Desde la elección del tipo de datos a almacenar hasta la implementación de medidas de seguridad y optimización, cada paso debe ser meticulosamente planificado para garantizar una aplicación funcional, segura y eficiente.

<a id="tareas-en-segundo-plano-servicios"></a>
## Tareas en segundo plano. Servicios

En el desarrollo de aplicaciones para dispositivos móviles, los conceptos de tareas en segundo plano y servicios son fundamentales para crear experiencias fluidas y respuestas rápidas a los usuarios. Los servicios permiten que ciertas operaciones continúen ejecutándose incluso cuando la aplicación no está en primer plano, lo que es crucial para mantener la funcionalidad del dispositivo y mejorar la experiencia del usuario.

Un servicio en Android, por ejemplo, es un componente de fondo que realiza tareas continuas o largas sin interacción directa con el usuario. Pueden ser servicios que realizan operaciones como descargar archivos, reproducir música, gestionar notificaciones o mantener una conexión activa a Internet. Los servicios pueden ejecutarse en segundo plano y no interfieren con la experiencia del usuario mientras se están ejecutando.

Para implementar un servicio en Android, es necesario crear una clase que extienda `Service`. Esta clase puede contener métodos para iniciar, detener y gestionar el ciclo de vida del servicio. Además, los servicios pueden interactuar con otras partes de la aplicación a través de intents o mediante el uso de interfaces de comunicación.

La gestión eficiente de tareas en segundo plano es crucial para mantener la batería del dispositivo y evitar que las aplicaciones interfieran con la experiencia del usuario. Para optimizar el rendimiento, los servicios pueden utilizar técnicas como el manejo de hilos, la programación asincrónica y la gestión de recursos de forma eficiente.

Además de los servicios tradicionales, Android también ofrece la posibilidad de crear servicios en segundo plano basados en trabajadores (Worker Services). Estos trabajadores son componentes que pueden ejecutar tareas largas o complejas en un hilo separado, lo que permite mantener el flujo principal de la aplicación fluido y responsive.

La programación de aplicaciones para dispositivos móviles requiere una comprensión profunda de los conceptos de tareas en segundo plano y servicios. Estos componentes permiten crear aplicaciones que ofrecen una experiencia fluida y confiable, incluso cuando el usuario interactúa con otras aplicaciones o realiza otras actividades en el dispositivo.

En resumen, la programación de aplicaciones para dispositivos móviles implica el uso de tareas en segundo plano y servicios para mantener la funcionalidad del dispositivo y mejorar la experiencia del usuario. La implementación eficiente de estos componentes requiere una comprensión profunda de los conceptos de hilos, programación asincrónica y gestión de recursos, lo que permite crear aplicaciones robustas y eficientes.

<a id="seguridad-y-permisos"></a>
## Seguridad y permisos

En la subunidad "Seguridad y permisos" del desarrollo de aplicaciones para dispositivos móviles, se aborda un aspecto crucial que afecta tanto la funcionalidad como la privacidad de las aplicaciones. La seguridad es una prioridad fundamental en cualquier sistema informático, y en el contexto móvil, esto se refuerza aún más debido a la naturaleza portable y accesible de estos dispositivos.

La gestión adecuada de los permisos es un componente integral de esta seguridad. Los usuarios esperan que las aplicaciones soliciten solo los datos e información necesarios para funcionar correctamente, sin comprometer su privacidad o seguridad personal. Por lo tanto, el diseño de aplicaciones móviles debe incluir mecanismos claros y transparentes para solicitar permisos a los usuarios.

Los sistemas operativos móviles como Android y iOS tienen políticas estrictas sobre la solicitud y gestión de permisos. En Android, por ejemplo, cada aplicación puede solicitar acceso a diferentes tipos de datos del dispositivo, como la ubicación, la cámara o el almacenamiento interno. El usuario tiene la opción de aceptar o rechazar estas solicitudes, lo que permite un control preciso sobre qué información se comparte con las aplicaciones.

Para implementar correctamente los permisos en una aplicación móvil, es crucial seguir ciertas prácticas recomendadas. Primero, debe ser claro y conciso en la solicitud de permisos, explicando por qué son necesarios para el funcionamiento de la aplicación. Segundo, se deben manejar adecuadamente las respuestas del usuario, ya sea permitiendo o denegando los permisos solicitados. Finalmente, es importante proporcionar opciones para que los usuarios cambien sus preferencias de permisos en cualquier momento.

Además de los permisos individuales, también hay conceptos como la privacidad y el encriptado que son esenciales en el desarrollo seguro de aplicaciones móviles. La privacidad implica garantizar que solo se acceda a información personal si es absolutamente necesario y con el consentimiento del usuario. El encriptado, por otro lado, protege los datos almacenados y transmitidos, asegurando su integridad y confidencialidad.

En la práctica, la implementación de estos conceptos puede variar según las plataformas móviles y las necesidades específicas de cada aplicación. En Android, por ejemplo, se pueden utilizar las clases `Context` y `PackageManager` para solicitar y gestionar permisos. En iOS, el sistema utiliza un enfoque basado en bloques que permite una gestión más segura y eficiente.

Es importante recordar que la seguridad no es solo una cuestión técnica; también implica una buena práctica de diseño y comunicación con los usuarios. Una aplicación que solicita permisos de manera transparente, respetuosa y útil es más probable que reciba el consentimiento del usuario y, por lo tanto, sea más segura.

En conclusión, la gestión adecuada de los permisos en aplicaciones móviles es un aspecto fundamental de su seguridad. Al seguir prácticas recomendadas y mantener una comunicación clara con los usuarios, se puede crear una experiencia segura y confiable que cumpla con las expectativas del público móvil.

<a id="conectividad-tipos"></a>
## Conectividad. Tipos.

La conectividad es un elemento fundamental en el desarrollo de aplicaciones para dispositivos móviles, ya que permite la comunicación entre diferentes componentes del sistema o con otros sistemas externos. En esta subunidad, exploraremos los tipos de conectividad disponibles y cómo utilizarlas eficazmente en nuestras aplicaciones.

Primero, es importante distinguir entre las distintas formas de conectividad que pueden emplearse en dispositivos móviles. La más común es la red inalámbrica Wi-Fi, que permite una conexión rápida y segura a Internet o a otros dispositivos. Además, el acceso a datos 4G y 5G ha revolucionado la velocidad y la eficiencia de las aplicaciones móviles, permitiendo transmisiones más rápidas y menos latencia.

Otra forma de conectividad es el uso de redes celulares, que son especialmente útiles en áreas donde no se dispone de cobertura Wi-Fi. Estos sistemas utilizan una infraestructura de antenas y torres para proporcionar servicios móviles a largas distancias. Además, los dispositivos móviles pueden utilizar múltiples bandas de frecuencia simultáneamente para mejorar la velocidad y la calidad de la conexión.

Además de las redes inalámbricas y celulares, también es posible establecer conexiones Bluetooth para comunicarse con dispositivos cercanos como auriculares, teclados o dispositivos IoT. Esta tecnología permite una comunicación rápida y baja en términos de energía, lo que es crucial en dispositivos móviles.

La conectividad a través de la red móvil 4G/5G es especialmente relevante para aplicaciones que requieren alta velocidad y baja latencia, como juegos, aplicaciones de streaming o aplicaciones de realidad aumentada. Estas tecnologías utilizan una infraestructura de redes basadas en microdatos y femtoceldas, lo que permite proporcionar servicios móviles a gran escala.

Para implementar la conectividad en nuestras aplicaciones móviles, es necesario utilizar las APIs proporcionadas por los sistemas operativos. En Android, por ejemplo, se pueden utilizar las clases `ConnectivityManager` y `NetworkInfo` para obtener información sobre la conexión actual del dispositivo y determinar si hay acceso a Internet. En iOS, se utiliza la clase `Reachability` para realizar comprobaciones de conectividad.

Es importante tener en cuenta que la eficiencia de la conexión es un factor clave en el rendimiento de las aplicaciones móviles. Por lo tanto, es recomendable utilizar técnicas como la paginación y la carga diferida para optimizar el uso de los datos y reducir la latencia.

Además, es crucial considerar la seguridad al establecer conexiones en dispositivos móviles. Los dispositivos móviles son targets frecuentes para ataques cibernéticos, por lo que es importante utilizar protocolos seguros como HTTPS para las comunicaciones web y implementar medidas de autenticación y autorización adecuadas.

En conclusión, la conectividad es un aspecto crucial en el desarrollo de aplicaciones móviles. Al entender los diferentes tipos de conectividad disponibles y cómo utilizarlas eficazmente, podemos crear aplicaciones que ofrezcan una experiencia óptima a nuestros usuarios, independientemente del entorno en el que se encuentren.

<a id="manejo-de-conexiones-http-y-https"></a>
## Manejo de conexiones HTTP y HTTPS

En el desarrollo de aplicaciones para dispositivos móviles, la gestión eficiente de conexiones HTTP y HTTPS es un aspecto fundamental que garantiza una comunicación segura y rápida con los servidores. La HTTP (Hypertext Transfer Protocol) es el protocolo utilizado para transferir datos en la web, mientras que HTTPS (HTTP Secure) añade una capa adicional de seguridad mediante el cifrado SSL/TLS.

La implementación de conexiones HTTP y HTTPS en aplicaciones móviles requiere un conocimiento profundo de las bibliotecas y frameworks disponibles para cada plataforma. En Android, por ejemplo, se puede utilizar la clase `HttpURLConnection` o la biblioteca Retrofit para manejar solicitudes HTTP y HTTPS. Estas herramientas facilitan el envío de peticiones y la recepción de respuestas, proporcionando métodos para configurar cabeceras, enviar datos y gestionar cookies.

Para implementar conexiones HTTPS en aplicaciones móviles, es crucial considerar la seguridad del tráfico. Esto implica validar los certificados SSL/TLS presentados por el servidor, lo que se puede hacer mediante la configuración de un `TrustManager` personalizado. Además, es recomendable utilizar protocolos TLS 1.2 o superior para asegurar una comunicación segura y resistente a ataques como el downgrade attack.

En iOS, las aplicaciones pueden utilizar la clase `URLSession` para gestionar conexiones HTTP y HTTPS. Esta clase proporciona un alto nivel de abstracción y flexibilidad, permitiendo configurar solicitudes personalizadas y manejar respuestas de manera eficiente. Además, iOS ofrece funcionalidades adicionales como el almacenamiento en caché de datos y la gestión de cookies.

La gestión de conexiones HTTP y HTTPS también implica considerar los aspectos de rendimiento. Para mejorar el tiempo de respuesta de las aplicaciones, es recomendable utilizar técnicas como la conexión persistente (keep-alive) y la compresión de datos. Además, se debe optimizar el tamaño de los paquetes enviados para evitar congestiones en la red.

En el contexto de aplicaciones móviles, la gestión de conexiones HTTP y HTTPS también implica considerar la seguridad del almacenamiento de credenciales. Es crucial utilizar métodos seguros para almacenar y recuperar datos sensibles como contraseñas o tokens de autenticación. Esto puede implicar el uso de encriptación local o la integración con servicios de gestión de secretos.

En resumen, la gestión eficiente de conexiones HTTP y HTTPS es un aspecto crucial del desarrollo de aplicaciones móviles. Al utilizar las bibliotecas y frameworks adecuados, validar certificados SSL/TLS, considerar los aspectos de rendimiento y seguridad del almacenamiento de credenciales, se puede garantizar una comunicación segura y eficiente con los servidores.

<a id="sensores"></a>
## Sensores

En este capítulo, nos adentramos en la fascinante y multifacética temática del desarrollo de aplicaciones para dispositivos móviles, con un especial énfasis en el uso de sensores. Los sensores son componentes clave que permiten a las aplicaciones interactuar directamente con el entorno físico alrededor del dispositivo, proporcionando datos cruciales sobre movimientos, luz, temperatura y más.

La integración de sensores en nuestras aplicaciones móviles abre un mundo de posibilidades. Desde la detección de movimientos para juegos y aplicaciones de fitness hasta la medición de la luminosidad para ajustar automáticamente los contratos de pantalla, los sensores son herramientas poderosas que añaden valor y funcionalidad a nuestras aplicaciones.

Para comenzar, es importante entender cómo funcionan los sensores en un dispositivo móvil. Los sensores se comunican con el sistema operativo mediante una interfaz específica, como la API de Android o iOS, proporcionando datos digitales que pueden ser interpretados por la aplicación. Cada sensor tiene sus propias características y especificaciones técnicas, lo que significa que es crucial conocer cómo configurar y utilizar cada uno según su funcionalidad.

El desarrollo de aplicaciones que utilicen sensores implica un enfoque integral en el manejo de los datos generados por estos dispositivos. Es necesario considerar la eficiencia del uso de recursos, ya que la recopilación y procesamiento de datos sensoriales puede consumir significativamente la batería del dispositivo. Además, es fundamental garantizar la privacidad y seguridad de los datos sensibles que se recopilan, implementando medidas adecuadas para proteger la información personal.

En el mundo de la programación móvil, existen varias bibliotecas y frameworks que facilitan el acceso a los sensores del dispositivo. En Android, por ejemplo, podemos utilizar la clase `SensorManager` para interactuar con diferentes tipos de sensores como acelerómetro, giroscopio, magnetómetro y más. Cada sensor tiene su propio conjunto de métodos que permiten leer datos en tiempo real, lo que es crucial para aplicaciones que requieren una respuesta rápida a los cambios ambientales.

Además de la recopilación de datos, el desarrollo de aplicaciones con sensores implica también la interpretación y visualización de estos datos. Por ejemplo, un juego de realidad aumentada puede utilizar el sensor de orientación del dispositivo para superponer información digital sobre el mundo físico alrededor del usuario. O una aplicación de fitness puede usar el acelerómetro para rastrear los movimientos del usuario durante un entrenamiento.

La importancia de la precisión y confiabilidad en la medición con sensores no debe ser subestimada. Cualquier error o inexactitud en los datos sensoriales puede llevar a resultados incorrectos en la aplicación, por lo que es crucial calibrar y validar estos datos según sea necesario.

En conclusión, el uso de sensores en aplicaciones móviles representa una oportunidad significativa para mejorar la experiencia del usuario y añadir funcionalidades innovadoras. Desde juegos hasta aplicaciones educativas y de salud, los sensores son herramientas versátiles que pueden ser utilizados de muchas maneras diferentes. A medida que avanzamos en el desarrollo de estas aplicaciones, es crucial mantener un enfoque integral en la eficiencia, privacidad y seguridad para garantizar una experiencia óptima y segura para nuestros usuarios.

<a id="posicionamiento-localizacion-mapas"></a>
## Posicionamiento. Localización. Mapas

En este capítulo, nos adentramos en la fascinante y compleja temática del posicionamiento, localización y mapas en el desarrollo de aplicaciones para dispositivos móviles. Estos temas son fundamentales para crear experiencias interactivas y útiles que utilicen la geografía como una herramienta central.

El posicionamiento es un proceso que permite determinar la ubicación exacta de un dispositivo móvil en el espacio tridimensional. Este proceso se realiza mediante la combinación de diferentes tecnologías, como GPS (Global Positioning System), Wi-Fi y Bluetooth, cada una con sus propias ventajas y limitaciones. El objetivo es proporcionar precisión suficiente para aplicaciones que requieren localización precisa, como los servicios de entrega o las aplicaciones de turismo.

La localización, por otro lado, implica la interpretación y el uso de la información geográfica obtenida a través del posicionamiento. Esto puede implicar la búsqueda de lugares cercanos, la generación de rutas, la identificación de puntos de interés o incluso la personalización de contenido según la ubicación del usuario. La localización es una habilidad clave en aplicaciones que buscan ofrecer servicios relevantes y personalizados.

Los mapas son una representación visual de la información geográfica. En el contexto móvil, los mapas pueden ser estáticos o dinámicos, y pueden mostrar una variedad de datos, desde calles y edificios hasta puntos de interés turísticos y eventos en tiempo real. La creación de mapas interactivos que respondan a las acciones del usuario es un desafío interesante, ya que requiere una buena comprensión de la geografía y la programación.

En el desarrollo de aplicaciones móviles para dispositivos como smartphones y tablets, el posicionamiento, localización y mapas son herramientas poderosas. Estos elementos permiten a los usuarios interactuar con su entorno de manera más natural y eficiente, facilitando tareas diarias como la navegación, el seguimiento de eventos o la búsqueda de información geográfica.

Además, el uso del posicionamiento y localización en aplicaciones móviles ha llevado a la creación de nuevas oportunidades de negocio. Las empresas pueden utilizar esta tecnología para ofrecer servicios personalizados basados en la ubicación del usuario, como recomendaciones de negocios locales o publicidad contextualizada.

En conclusión, el posicionamiento, localización y mapas son elementos cruciales en el desarrollo de aplicaciones móviles. A través de estas tecnologías, los desarrolladores pueden crear experiencias interactivas y útiles que utilizan la geografía como una herramienta central, mejorando así la calidad de vida de los usuarios y creando nuevas oportunidades de negocio.


<a id="actividad-libre-de-final-de-evaluacion-la-milla-extra"></a>
# Actividad libre de final de evaluación - La milla extra

<a id="la-milla-extra-primera-evaluacion"></a>
## La Milla Extra - Primera evaluación

### ejercicio

```markdown

```
