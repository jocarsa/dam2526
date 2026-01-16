# Programación

**Author:** Jose Vicente Carratala Sanchis

## Table of contents

- [Identificación de los elementos de un programa informático](#identificacion-de-los-elementos-de-un-programa-informatico)
  - [Estructura y bloques fundamentales](#estructura-y-bloques-fundamentales)
  - [Variables](#variables)
  - [Tipos de datos](#tipos-de-datos)
  - [Literales](#literales)
  - [Constantes](#constantes)
  - [Operadores y expresiones](#operadores-y-expresiones)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad)
- [Utilización de objetos](#utilizacion-de-objetos)
  - [Características de los objetos](#caracteristicas-de-los-objetos)
  - [Instanciación de objetos](#instanciacion-de-objetos)
  - [Utilización de métodos. Parámetros](#utilizacion-de-metodos-parametros)
  - [Utilización de propiedades](#utilizacion-de-propiedades)
  - [Utilización de métodos estáticos](#utilizacion-de-metodos-estaticos)
  - [Constructores](#constructores)
  - [Destrucción de objetos y liberación de memoria](#destruccion-de-objetos-y-liberacion-de-memoria)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad-1)
- [Uso de estructuras de control](#uso-de-estructuras-de-control)
  - [Estructuras de selección](#estructuras-de-seleccion)
  - [Estructuras de repetición](#estructuras-de-repeticion)
  - [Estructuras de salto](#estructuras-de-salto)
  - [Control de excepciones](#control-de-excepciones)
  - [Aserciones](#aserciones)
  - [Prueba, depuración y documentación de la aplicación](#prueba-depuracion-y-documentacion-de-la-aplicacion)
  - [Ejercicio](#ejercicio)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad-2)
- [Desarrollo de clases](#desarrollo-de-clases)
  - [Concepto de clase](#concepto-de-clase)
  - [Estructura y miembros de una clase. Visibilidad](#estructura-y-miembros-de-una-clase-visibilidad)
  - [Creación de propiedades](#creacion-de-propiedades)
  - [Creación de métodos](#creacion-de-metodos)
  - [Creación de constructores](#creacion-de-constructores)
  - [Utilización de clases y objetos](#utilizacion-de-clases-y-objetos)
  - [Utilización de clases heredadas](#utilizacion-de-clases-heredadas)
- [Lectura y escritura de información](#lectura-y-escritura-de-informacion)
  - [Flujos. Tipos bytes y caracteres. Clases relacionadas](#flujos-tipos-bytes-y-caracteres-clases-relacionadas)
  - [Ficheros de datos. Registros](#ficheros-de-datos-registros)
  - [Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros](#apertura-y-cierre-de-ficheros-modos-de-acceso-escritura-y-lectura-de-informacion-en-ficheros)
  - [Utilización de los sistemas de ficheros](#utilizacion-de-los-sistemas-de-ficheros)
  - [Creación y eliminación de ficheros y directorios](#creacion-y-eliminacion-de-ficheros-y-directorios)
  - [Entrada desde teclado. Salida a pantalla. Formatos de visualización](#entrada-desde-teclado-salida-a-pantalla-formatos-de-visualizacion)
  - [Interfaces gráficas](#interfaces-graficas)
  - [Concepto de evento](#concepto-de-evento)
  - [Creación de controladores de eventos](#creacion-de-controladores-de-eventos)
  - [Simulacro examen programacion](#simulacro-examen-programacion)
  - [Simulacro de examen 2](#simulacro-de-examen-2)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad-3)
  - [Examen final](#examen-final)
  - [Carpeta sin título](#carpeta-sin-titulo)
- [Aplicación de las estructuras de almacenamiento](#aplicacion-de-las-estructuras-de-almacenamiento)
  - [Estructuras estáticas y dinámicas](#estructuras-estaticas-y-dinamicas)
  - [Creación de matrices (arrays)](#creacion-de-matrices-arrays)
  - [Matrices (arrays) multidimensionales](#matrices-arrays-multidimensionales)
  - [Genericidad](#genericidad)
  - [Cadenas de caracteres. Expresiones regulares](#cadenas-de-caracteres-expresiones-regulares)
  - [Colecciones Listas, Conjuntos y Diccionarios](#colecciones-listas-conjuntos-y-diccionarios)
  - [Operaciones agregadas filtrado, reducción y recolección](#operaciones-agregadas-filtrado-reduccion-y-recoleccion)
- [Utilización avanzada de clases](#utilizacion-avanzada-de-clases)
  - [Composición de clases](#composicion-de-clases)
  - [Herencia y polimorfismo](#herencia-y-polimorfismo)
  - [Jerarquía de clases Superclases y subclases](#jerarquia-de-clases-superclases-y-subclases)
  - [Clases y métodos abstractos y finales](#clases-y-metodos-abstractos-y-finales)
  - [Interfaces](#interfaces)
  - [Sobreescritura de métodos](#sobreescritura-de-metodos)
  - [Constructores y herencia](#constructores-y-herencia)
- [Mantenimiento de la persistencia de los objetos](#mantenimiento-de-la-persistencia-de-los-objetos)
  - [Bases de datos orientadas a objetos](#bases-de-datos-orientadas-a-objetos)
  - [Características de las bases de datos orientadas a objetos](#caracteristicas-de-las-bases-de-datos-orientadas-a-objetos)
  - [Instalación del gestor de bases de datos](#instalacion-del-gestor-de-bases-de-datos)
  - [Creación de bases de datos](#creacion-de-bases-de-datos)
  - [Mecanismos de consulta](#mecanismos-de-consulta)
  - [El lenguaje de consultas sintaxis, expresiones, operadores](#el-lenguaje-de-consultas-sintaxis-expresiones-operadores)
  - [Recuperación, modificación y borrado de información](#recuperacion-modificacion-y-borrado-de-informacion)
  - [Tipos de datos objeto; atributos y métodos](#tipos-de-datos-objeto-atributos-y-metodos)
  - [Tipos de datos colección](#tipos-de-datos-coleccion)
- [Gestión de bases de datos](#gestion-de-bases-de-datos)
  - [Acceso a bases de datos. Estándares. Características](#acceso-a-bases-de-datos-estandares-caracteristicas)
  - [Establecimiento de conexiones](#establecimiento-de-conexiones)
  - [Almacenamiento, recuperación, actualización y eliminación de información en bases de datos](#almacenamiento-recuperacion-actualizacion-y-eliminacion-de-informacion-en-bases-de-datos)
- [Proyectos](#proyectos)
  - [Proyecto formulario](#proyecto-formulario)
  - [Panel de control de tienda online](#panel-de-control-de-tienda-online)
  - [Libreria requests](#libreria-requests)
  - [shorttags php](#shorttags-php)
  - [salvapantallas](#salvapantallas)
- [Inteligencia Artificial](#inteligencia-artificial)
  - [IA inicial](#ia-inicial)
- [Milla Extra Evaluacion 1](#milla-extra-evaluacion-1)
- [Actividad libre de final de evaluación - La milla extra](#actividad-libre-de-final-de-evaluacion-la-milla-extra)
  - [La Milla Extra - Primera evaluación](#la-milla-extra-primera-evaluacion)

---

<a id="identificacion-de-los-elementos-de-un-programa-informatico"></a>
# Identificación de los elementos de un programa informático

<a id="estructura-y-bloques-fundamentales"></a>
## Estructura y bloques fundamentales

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/001-Identificaci%C3%B3n%20de%20los%20elementos%20de%20un%20programa%20inform%C3%A1tico/001-Estructura%20y%20bloques%20fundamentales)

### Introducción a los ejercicios

En esta carpeta, encontrarás ejercicios básicos destinados a familiarizarte con los elementos fundamentales del lenguaje de programación Python. Los problemas incluyen cómo descargar e instalar Python, imprimir y solicitar datos al usuario, así como la creación de comentarios en un código fuente. Estos ejercicios te ayudarán a entender las estructuras básicas de un programa en Python, incluyendo docstrings para documentar tu código, importaciones de módulos y funciones principales que actúan como punto de partida del programa. Al completar estos ejercicios, mejorarás tus habilidades en la escritura de programas claros y mantenibles en Python.

### Salida
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

El código que se muestra imprime el texto "Hola mundo desde Python" en la pantalla cuando se ejecuta. La función `print()` es una de las más básicas y fundamentales en Python, utilizada para mostrar información o resultados por pantalla durante la ejecución del programa. En este caso específico, se está utilizando para imprimir un mensaje simple que confirma el inicio exitoso de cualquier programa Python, lo cual es útil tanto para los principiantes como para desarrolladores experimentados al probar rápidamente sus entornos de desarrollo.

ÚLTIMO PÁRRAFO: Comparado con el código anterior que era más informativo y guía textual sobre cómo descargar Python, este archivo proporciona un primer ejemplo práctico de programación real en Python, mostrando cómo imprimir texto en la consola. Esto representa una transición importante hacia la aplicación práctica del lenguaje después de configurar el entorno de desarrollo.

`001-Salida.py`

```python
print("Hola mundo desde Python")
```

### entrada
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python es muy sencillo y está diseñado para pedir al usuario que ingrese su nombre. Primero, se muestra un mensaje diciendo "Ahora te voy a preguntar el nombre". Luego, la función `input("Introduce tu nombre: ")` espera que el usuario teclee su nombre en la consola y presione enter. Aunque captura el nombre del usuario, no almacena esa información en ninguna variable, por lo que se pierde después de que el programa continúa. Finalmente, imprime "Ahora ya sé tu nombre", aunque técnicamente el programa no ha guardado ni usado la entrada proporcionada por el usuario.

Este código es importante para entender cómo interactuar con los usuarios a través del teclado en Python y ver cómo se usa `print` para mostrar texto y `input` para recibir datos. Sin embargo, sería útil guardar la entrada del usuario en una variable para poder usarla más adelante en tu programa.

`002-entrada.py`

```python
print("Ahora te voy a preguntar el nombre")
input("Introduce tu nombre: ")
print("Ahora ya sé tu nombre")
```

### comentarios de tipo docstring
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra cómo se utiliza un comentario de tipo docstring en Python. Una docstring (document string) es una cadena de texto que aparece inmediatamente después del inicio de una definición de función, clase o módulo y sirve para documentar el propósito y la funcionalidad del elemento. En este caso, aunque no se está dentro de una función o clase específica, simplemente ilustra cómo puedes escribir comentarios extensos que son claramente distintos del código debido a sus triples comillas simples al inicio y al final.

Este tipo de comentario es importante porque permite documentar el código de manera clara y detallada sin mezclar la documentación con el flujo normal del programa. Esto facilita su lectura y entendimiento para otros desarrolladores que trabajen en el mismo proyecto o revisen tu código más adelante.

`003-comentarios de tipo docstring.py`

```python
'''
    Esto es un comentario
    de tipo docstring
    Y se pueden poner tantas líneas como se quiera
'''
```

### Comentarios de una linea
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código es un ejemplo muy simple en Python que muestra cómo se utilizan los comentarios de una línea. Los comentarios son textos que el programador añade al código para explicar qué hace cada parte del programa, pero estos textos no son ejecutados por el ordenador. En este caso, la línea `# Esto es un comentario de una linea` está precedida por el símbolo `#`, lo que indica que toda la línea es un comentario y será ignorada por el intérprete de Python al ejecutar el programa.

Los comentarios son muy importantes en programación porque ayudan a otros desarrolladores (o incluso a ti mismo después de un tiempo) a entender rápidamente qué está haciendo una parte específica del código. Esto facilita la colaboración en proyectos grupales y hace que sea más fácil mantener o actualizar el código en el futuro.

`004-Comentarios de una linea.py`

```python
# Esto es un comentario de una linea
```

### Actividades propuestas

### Actividad 1: Instalación y Configuración del Entorno de Trabajo

**Descripción:** Los estudiantes deben descargar e instalar Python siguiendo las instrucciones proporcionadas en el archivo "001-Descarga de Python.md". El objetivo es configurar su entorno de desarrollo para poder ejecutar los ejercicios.

### Actividad 2: Salida Estándar

**Descripción:** Los estudiantes deben escribir un programa que muestre por pantalla un mensaje personalizado utilizando la función `print()`. Esta actividad busca familiarizar a los alumnos con la salida estándar en Python.

### Actividad 3: Introducción de Datos por Teclado

**Descripción:** Los estudiantes deben crear un programa que pida al usuario su nombre y luego lo muestre por pantalla. Se espera que aprendan cómo utilizar la función `input()` para introducir datos desde el teclado.

### Actividad 4: Comentarios en Python

**Descripción:** Los alumnos deberán escribir comentarios de diferentes tipos (docstrings y comentarios de una sola línea) en un programa sencillo. Esta actividad tiene como objetivo que comprendan la importancia y los beneficios de añadir comentarios a su código.

### Actividad 5: Estructura Básica del Programa

**Descripción:** Los estudiantes deben crear un archivo Python que siga la estructura básica descrita en el archivo "005-Estructura recomendada de los programas.md". Se espera que aprendan cómo organizar y documentar su código.

### Actividad 6: Uso de Docstrings

**Descripción:** Los alumnos deben añadir docstrings a las funciones o módulos en un programa existente. Esta actividad busca enseñarles la importancia de documentar sus funciones utilizando comentarios de tipo docstring.

### Actividad 7: Variables y Tipos de Datos Básicos

**Descripción:** Se les pide a los estudiantes que creen variables con diferentes tipos de datos (enteros, flotantes, cadenas) y realicen operaciones básicas con ellas. El objetivo es familiarizarlos con la gestión de tipos de datos en Python.

### Actividad 8: Estructura de Control If

**Descripción:** Los estudiantes deben escribir un programa que utilice estructuras condicionales (if-else). Se les pedirá que tomen decisiones basadas en la entrada del usuario. Esta actividad busca enseñarles cómo implementar lógica condicional en sus programas.

### Actividad 9: Creación de Funciones Simples

**Descripción:** Los alumnos deben crear funciones simples que realizan tareas como sumar dos números, encontrar el mayor entre ellos o invertir un string. El objetivo es enseñarles cómo definir y llamar a funciones en Python.

### Actividad 10: Organización de Códigos en Archivos

**Descripción:** Los estudiantes deben organizar códigos largos en múltiples archivos, importando las partes necesarias desde otros módulos. Esta actividad busca que aprendan a manejar proyectos más grandes y complejos utilizando el sistema de importaciones en Python.


<a id="variables"></a>
## Variables

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/001-Identificaci%C3%B3n%20de%20los%20elementos%20de%20un%20programa%20inform%C3%A1tico/002-Variables)

### Introducción a los ejercicios

Esta carpeta contiene ejercicios básicos sobre el uso de variables en Python, orientados a estudiantes de Formación Profesional. Los problemas se centran en la creación y manipulación de variables para almacenar e imprimir información como números enteros y cadenas de texto. Estos ejercicios ayudan a comprender cómo declarar correctamente las variables siguiendo las reglas del lenguaje, así como cómo usarlas dentro de programas simples para mostrar datos en pantalla.

### Contenedor de informacion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python es muy sencillo y ayuda a entender cómo se utilizan las variables. Primero, el programa establece que la variable `edad` tiene un valor entero, que en este caso es 47. Al definir una variable como `edad = 47`, estás diciendo al programa que cada vez que menciones `edad`, está haciendo referencia al número 47.

Luego, el código utiliza la función `print()` para mostrar el contenido de la variable `edad` en la pantalla o en la salida del programa. Al ejecutar este código, simplemente se imprimirá el número 47.

Este ejemplo es importante porque muestra cómo declarar una variable y luego utilizarla en otra parte del código, lo cual es fundamental cuando empiezas a programar.

`001-Contenedor de informacion.py`

```python
edad = 47

print(edad)
```

### varias variables
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código en Python muestra cómo se declaran y utilizan variables para almacenar información, como un número entero (la edad) y una cadena de texto (el nombre). La variable `edad` almacena el número 47, que representa la edad de alguien. Por otro lado, la variable `nombre` contiene la cadena "Jose Vicente", que es el nombre de esa persona.

El código utiliza la función `print()` para mostrar en pantalla los valores almacenados en las variables. Primero imprime un mensaje descriptivo seguido del valor de cada variable. Esto ayuda a entender claramente qué información se está mostrando, lo cual es importante para mejorar la legibilidad y el mantenimiento del código.

Este tipo de declaración de variables y uso de `print()` es fundamental en programación ya que permite al programa interactuar con el usuario y presentar datos de manera estructurada.

`002-varias variables.py`

```python
edad = 47
nombre = "Jose Vicente"

print("Mi edad es de:")
print(edad)
print("Mi nombre es:")
print(nombre)
```

### reglas de declaracion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python muestra diferentes formas correctas e incorrectas de declarar variables. Las líneas válidas son `edad = 47`, `miedad = 47`, `mi_edad = 47`, `edad2 = 47` y `e2dad = 47`. Estos ejemplos ilustran que los nombres de las variables pueden contener letras, números y el carácter subrayado `_`, pero no pueden comenzar con un número. Además, hay dos líneas comentadas que muestran declaraciones incorrectas: `# mi edad = 47` (porque contiene un espacio) y `# mi-edad = 47` (porque usa un guion en lugar de un subrayado). La línea `#2edad = 47` también es inválida porque comienza con un número. Este código te ayuda a entender las reglas básicas para nombrar variables en Python, lo que es crucial para escribir programas legibles y funcionales.

`003-reglas de declaracion.py`

```python
edad = 47
miedad = 47
mi_edad = 47
# mi edad = 47
# mi-edad = 47
edad2 = 47
e2dad = 47
#2edad = 47
```

### Actividades propuestas

### Actividad 1: Crear una variable y mostrar su contenido
**Descripción:** El estudiante deberá crear una variable que almacene un dato numérico o texto y luego imprimir el valor de esa variable en la consola. **Objetivo:** Aprender a declarar variables y utilizar la función `print()` para mostrar información.

### Actividad 2: Creación e impresión de varias variables
**Descripción:** Los estudiantes deben escribir un programa que declare dos o más variables (una numérica y otra de texto) e imprimir su contenido en la consola. **Objetivo:** Familiarizarse con la declaración múltiple de variables y el uso del operador `print()`.

### Actividad 3: Manipulación de cadenas de texto
**Descripción:** Los estudiantes deben crear una variable que almacene un nombre completo, luego imprimir en consola partes específicas del nombre (por ejemplo, solo el primer nombre o el apellido). **Objetivo:** Comprender cómo manipular y acceder a elementos dentro de una cadena de texto.

### Actividad 4: Reglas de declaración de variables
**Descripción:** Los estudiantes deben crear un programa que declare varias variables con diferentes nombres (usando letras, números, guiones bajos) e intentar declarar algunas que no sean válidas según las reglas del lenguaje Python. **Objetivo:** Identificar y entender las restricciones para nombrar variables en Python.

### Actividad 5: Operaciones básicas con variables numéricas
**Descripción:** Los estudiantes deben crear un programa donde se declaren dos variables numéricas, realizar operaciones matemáticas básicas entre ellas (suma, resta), y luego imprimir los resultados. **Objetivo:** Practicar la creación de variables y el uso de operadores aritméticos en Python.

### Actividad 6: Uso de comillas en cadenas de texto
**Descripción:** Los estudiantes deben escribir un programa que declare una variable con un texto dentro, utilizando tanto comillas simples como dobles para ver cómo se comporta la salida. **Objetivo:** Entender las diferencias y similitudes entre el uso de comillas simples y dobles en Python.

### Actividad 7: Introducir datos por teclado
**Descripción:** Los estudiantes deben crear un programa que pida al usuario que introduzca su edad o nombre, almacenar la entrada del usuario en una variable y luego mostrar el valor de esa variable. **Objetivo:** Practicar la lectura de datos desde el teclado y la manipulación de variables.

### Actividad 8: Uso de comentarios
**Descripción:** Los estudiantes deben escribir un programa que incluya varias líneas de código con comentarios explicando lo que hace cada parte del código. **Objetivo:** Aprender a documentar el código usando comentarios para mejorar la legibilidad y la colaboración en proyectos.

### Actividad 9: Uso de comillas en nombres no válidos
**Descripción:** Los estudiantes deben crear un programa donde intenten declarar variables con nombres que contengan espacios, guiones o caracteres especiales (y que generarán errores). **Objetivo:** Aprender a identificar y corregir errores comunes relacionados con la declaración de variables en Python.

### Actividad 10: Creación de un juego sencillo
**Descripción:** Los estudiantes deben crear un programa básico donde el usuario debe adivinar un número generado aleatoriamente por el sistema. El programa debe almacenar el número a adivinar y usar bucles para permitir al usuario intentarlo varias veces hasta acertar. **Objetivo:** Integrar los conocimientos de variables, estructuras de control (condicionales y bucles) en un contexto práctico y entretenido.

Estas actividades buscan reforzar el entendimiento de conceptos básicos sobre la declaración y uso de variables en Python, además de introducir aspectos como las reglas de nomenclatura y cómo interactuar con el usuario mediante entradas de teclado.


<a id="tipos-de-datos"></a>
## Tipos de datos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/001-Identificaci%C3%B3n%20de%20los%20elementos%20de%20un%20programa%20inform%C3%A1tico/003-Tipos%20de%20datos)

### Introducción a los ejercicios

En esta carpeta, encontrarás ejercicios diseñados para ayudarte a comprender los diferentes tipos de datos en Python y cómo trabajar con ellos. Los archivos te permitirán identificar variables que contienen cadenas, números enteros, números decimales y valores booleanos. Además, explorarás la conversión implícita y explícita entre tipos de datos, lo cual es crucial para manipular correctamente los datos en programas informáticos.

### diferentes tipos de datos
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código es una introducción al uso de diferentes tipos de datos en Python. Cada línea define una variable y le asigna un valor concreto, mostrando cómo se manejan distintos tipos de datos:

1. `nombre` es una cadena de texto (string), que aquí contiene el nombre "Jose Vicente". Las cadenas son utilizadas para almacenar cualquier tipo de información textual.
2. `edad` es un número entero (integer) con el valor 47. Este tipo de dato se utiliza para representar números enteros sin parte decimal, como por ejemplo la edad o la cantidad de elementos en una lista.
3. `altura` es un número decimal o flotante (float), que en este caso tiene el valor 1.78. Los números decimales son importantes cuando necesitas representar valores que incluyen una fracción o parte decimal, como medidas métricas como altura o peso.
4. `guapo` es una variable booleana con el valor True. Los datos booleanos pueden tener solo dos valores: True (verdadero) o False (falso). Este tipo de dato es útil para expresar estados binarios, por ejemplo, si algo está activado o desactivado.

Este código sirve como un buen ejemplo inicial de cómo Python maneja diferentes tipos de datos y cómo puedes almacenar distintos tipos de información en variables.

`001-diferentes tipos de datos.py`

```python
nombre = "Jose Vicente" # cadena
edad = 47 # entero
altura = 1.78 # decimal
guapo = True # booleana
```

### conversion de tipo de dato implicita
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código muestra cómo Python maneja la conversión de tipos de dato de forma automática en algunas situaciones, aunque no siempre lo hace. Comenzamos definiendo una variable llamada `edad` y le asignamos el valor "47", pero este valor está entre comillas, por lo que es un string (cadena de texto) en lugar de un número entero.

Cuando imprimimos el tipo de dato de la variable `edad` usando `print(type(edad))`, se muestra que `edad` es de tipo str (string).

Luego, cuando multiplicamos `edad*2` y lo imprimimos, no estamos haciendo una operación matemática. En su lugar, Python entiende esto como una concatenación o repetición del string, por lo que "47" se imprime dos veces seguida: "4747".

A continuación, cuando multiplicamos `edad*1`, aunque no imprimimos el resultado directamente, esta operación intenta convertir la cadena de texto en un número para poder hacer una multiplicación matemática. Sin embargo, como no se imprime este resultado o se le asigna a otra variable, no vemos los cambios.

Finalmente, al imprimir `edad*2` nuevamente, obtenemos el mismo resultado que antes: "4747". Esto demuestra que la operación anterior de multiplicar por 1 no cambió realmente cómo Python interpreta la variable `edad`.

Este código es importante porque muestra que aunque algunas conversiones entre tipos de datos pueden ocurrir automáticamente en ciertas situaciones, otras requieren una acción explícita del programador para asegurar el tipo correcto de dato.

`002-conversion de tipo de dato implicita.py`

```python
edad = "47"
print(type(edad))

print(edad*2) # encadena

edad*1 # Conversión implícita de los datos

print(edad*2)
```

### conversión explicita de los datos
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código te enseña cómo convertir tipos de datos en Python y cómo esto afecta el comportamiento del programa. Inicialmente, la variable `edad` almacena un número (47), pero está guardado como una cadena de texto (`str`). Esto significa que cuando intentas imprimir el tipo de dato con `print(type(edad))`, obtienes `<class 'str'>`.

Luego, cuando ejecutas `print(edad*2)`, Python entiende esto como la concatenación de cadenas (es decir, "47" repetido dos veces), no como una operación matemática. Por eso se muestra "4747" en lugar de un número.

Finalmente, el código convierte `edad` a un número entero usando `int(edad)`. Ahora, cuando imprimes `edad*2`, Python entiende que debes multiplicar los números y te dará 94. Esto demuestra la importancia de entender cómo se manipulan y converten los tipos de datos en tu programa para evitar errores y obtener el resultado deseado.

`003-conversión explicita de los datos.py`

```python
edad = "47"
print(type(edad))

print(edad*2) # encadena

edad = int(edad)

print(edad*2) # se trata como multiplicación
```

### Actividades propuestas

### Actividad 1: Identificación y Uso de Tipos de Datos Básicos
**Descripción:** 
Identifica los diferentes tipos de datos presentes en un programa dado (cadenas, enteros, decimales y booleanos). Asegúrate de entender cómo se declaran e inicializan estos tipos de datos. Esta actividad te ayudará a familiarizarte con las características básicas de cada tipo.

### Actividad 2: Conversión Implícita entre Tipos de Datos
**Descripción:** 
Practica la conversión implícita en Python al tratar diferentes tipos de datos, como el cambio automático de una cadena a un número entero o decimal cuando se realiza una operación matemática. Observa cómo los resultados varían dependiendo del tipo utilizado.

### Actividad 3: Conversión Exáctica entre Tipos de Datos
**Descripción:** 
Ejercita la conversión explícita entre tipos de datos en Python, convirtiendo cadenas a enteros y viceversa. Entiende cómo las conversiones manuales pueden afectar el flujo y resultado del programa.

### Actividad 4: Operaciones con Datos Numéricos
**Descripción:** 
Realiza operaciones matemáticas básicas (suma, resta, multiplicación) utilizando datos numéricos enteros y decimales. Aprende a manejar correctamente los tipos de datos para evitar errores de ejecución.

### Actividad 5: Comparaciones con Tipos Booleanos
**Descripción:** 
Ejercita el uso del tipo booleano en comparaciones y operaciones lógicas. Identifica cómo se manipulan las variables booleanas para controlar la lógica del programa y tomar decisiones basadas en condiciones.

### Actividad 6: Manipulación de Cadenas de Texto
**Descripción:** 
Practica operaciones básicas con cadenas como concatenar, dividir y buscar subcadenas. Aprende a manipular el texto según las necesidades del programa.

### Actividad 7: Ejemplos Prácticos de Conversión Implícita
**Descripción:** 
Crea ejemplos que demuestren la conversión implícita entre tipos de datos en Python, identificando situaciones comunes donde esta operación ocurre naturalmente durante el desarrollo.

### Actividad 8: Ejemplos Prácticos de Conversión Explícita
**Descripción:** 
Desarrolla ejemplos que ilustren la conversión explícita entre tipos de datos, comprendiendo cuándo y por qué es necesario realizar estas conversiones para garantizar el correcto funcionamiento del programa.

### Actividad 9: Identificación de Errores Tipológicos
**Descripción:** 
Analiza ejemplos que incluyen errores relacionados con la incompatibilidad entre tipos de datos (por ejemplo, sumar una cadena y un entero). Aprende a identificar y corregir estos problemas para mejorar la robustez del código.

### Actividad 10: Integración Completa de Tipos de Datos
**Descripción:** 
Desarrolla pequeños programas que integren varios tipos de datos en operaciones matemáticas, comparaciones lógicas y manipulación de texto. Asegúrate de incluir conversiones explícitas e implícitas para manejar diferentes situaciones del programa.


<a id="literales"></a>
## Literales

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/001-Identificaci%C3%B3n%20de%20los%20elementos%20de%20un%20programa%20inform%C3%A1tico/004-Literales)

### Introducción a los ejercicios

En esta carpeta, se encuentran dos ejercicios básicos destinados a ayudar a los estudiantes a comprender y identificar literales en Python. Los literales son representaciones directas de valores que aparecen en el código sin la necesidad de ser calculados o declarados previamente. En el primer ejercicio, se trabajan con literales de cadena, mostrando cómo se representa texto directamente en el código. El segundo ejercicio enfatiza los literales numéricos, ilustrando la forma directa en que se introducen números enteros y flotantes en Python. Estos ejercicios son fundamentales para desarrollar una comprensión sólida de los elementos básicos del lenguaje y sentar las bases para estructuras más complejas.

### literales de cadena
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra un ejemplo simple de un literal de cadena en Python. Un literal de cadena es una secuencia de caracteres entre comillas, como se ve aquí con "esto es un literal". Este tipo de dato se utiliza para almacenar y manipular texto en programas informáticos. En este caso específico, el programa simplemente está definiendo una cadena que contiene las palabras "esto es un literal", pero no hace nada más con ella, por lo que su utilidad práctica sería limitada a menos que sea asignado a una variable o utilizado de alguna otra manera en el contexto de un programa completo. Es importante entender cómo se escriben y utilizan los literales de cadena porque son fundamentales para muchas operaciones básicas en programación, como mostrar mensajes en pantalla o trabajar con datos de texto.

`001-literales de cadena.py`

```python
"esto es un literal"
```

### literales numericos
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código es muy simple y consiste en solo un número: el número 47. En programación, cuando ves un número sin estar dentro de una operación o asociado con alguna función específica, se trata de un literal numérico. Un literal numérico como este se considera una constante que no cambia su valor durante la ejecución del programa.

En el contexto del archivo y la ruta proporcionada, este código probablemente está siendo utilizado para ilustrar cómo los números sin comillas en Python son directamente interpretados como enteros. Es importante entender esto porque ayuda a diferenciar entre diferentes tipos de datos que puedes usar en un programa informático, como cadenas de texto (strings) y números.

Este tipo de código simple es útil cuando se están explicando conceptos básicos de programación, ya que permite centrarse específicamente en la naturaleza de los literales numéricos sin complicaciones adicionales.

`002-literales numericos.py`

```python
47
```

### Actividades propuestas

### Actividad 1: Identificación y Creación de Literales en Python

**Descripción:** Los estudiantes deben identificar los diferentes tipos de literales presentes en dos archivos de código proporcionados (uno con literales de cadena y otro con literales numéricos). La tarea consiste en escribir una breve descripción sobre cada literal encontrado y crear ejemplos similares a partir de sus propias ideas.

**Objetivo:** Aprender a distinguir entre diferentes tipos de literales en Python (cadenas, números enteros) y cómo usarlos correctamente en programas simples.

### Actividad 2: Ejercicios Prácticos con Literales

**Descripción:** Los estudiantes deben completar ejercicios prácticos donde tienen que combinar literales numéricos y de cadena para formar sentencias más complejas. Por ejemplo, sumar dos números enteros o concatenar cadenas.

**Objetivo:** Mejorar la comprensión sobre cómo se usan los literales en expresiones y declaraciones en Python.

### Actividad 3: Creación de Código Basado en Literales

**Descripción:** Los alumnos deben crear pequeños programas que utilizan literales para realizar operaciones básicas (suma, resta) con números enteros y concatenar cadenas para formar frases completas.

**Objetivo:** Practicar la creación de código simple que utiliza diferentes tipos de literales en contextos prácticos.

### Actividad 4: Evaluación del Uso de Literales

**Descripción:** Se propone un conjunto de ejemplos de código donde los estudiantes deben evaluar si se están utilizando correctamente los literales. Deben señalar cualquier error y proponer correcciones.

**Objetivo:** Aprender a identificar y corregir errores comunes en el uso de literales.

### Actividad 5: Análisis Comparativo

**Descripción:** Los estudiantes deben comparar y contrastar cómo se utilizan los literales numéricos y de cadena en diferentes situaciones. Deben discutir las diferencias y similitudes entre ambos tipos de literales.

**Objetivo:** Mejorar la comprensión sobre la flexibilidad y versatilidad del uso de literales en Python.

### Actividad 6: Práctica Interactiva

**Descripción:** Los alumnos trabajan en parejas para explicarse mutuamente cómo los diferentes tipos de literales (numéricos y cadenas) se utilizan en programas. Cada pareja debe crear ejemplos interactivos basados en lo que han aprendido.

**Objetivo:** Facilitar la comprensión a través del trabajo colaborativo y la enseñanza recíproca.

### Actividad 7: Desafío de Literales

**Descripción:** Se les presenta un problema donde deben crear una secuencia de literales (numéricos y cadenas) para cumplir con ciertos requisitos. Por ejemplo, generar una lista que incluya números enteros y cadenas.

**Objetivo:** Poner a prueba la comprensión sobre el uso de múltiples tipos de literales en conjuntos más complejos.

### Actividad 8: Documentación Personalizada

**Descripción:** Los estudiantes deben escribir notas personales explicando cómo se utilizan los literales numéricos y de cadena. Estas notas incluirán ejemplos propios, errores comunes a evitar y consejos sobre su uso eficaz.

**Objetivo:** Mejorar las habilidades de reflexión y documentación personal en relación con el aprendizaje del código.

### Actividad 9: Revisión Colaborativa

**Descripción:** Los alumnos revisan entre sí los documentos escritos por sus compañeros sobre literales. Se pide que hagan correcciones, añadan ejemplos adicionales y den feedback constructivo.

**Objetivo:** Proporcionar una oportunidad para la crítica creativa y el aprendizaje colectivo de conceptos clave.

### Actividad 10: Creación de Ejercicios

**Descripción:** Los estudiantes deben diseñar sus propios ejercicios (con su solución) usando literales. Estos ejercicios deberían cubrir tanto literales numéricos como de cadena, y ser adecuados para los compañeros que están aprendiendo sobre estos conceptos.

**Objetivo:** Desafiar a los estudiantes a aplicar sus conocimientos en la creación de material educativo útil para otros.


<a id="constantes"></a>
## Constantes

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/001-Identificaci%C3%B3n%20de%20los%20elementos%20de%20un%20programa%20inform%C3%A1tico/005-Constantes)

### Introducción a los ejercicios

En esta serie de ejercicios, centraremos nuestra atención en el concepto de constantes en programación utilizando Python. El objetivo principal es enseñar a los estudiantes la importancia y el uso correcto de las constantes, que son valores que deberían permanecer invariables durante toda la ejecución del programa. Sin embargo, el ejercicio también muestra cómo se puede modificar un valor supuestamente constante, lo cual ilustra por qué es una mala práctica en programación cambiar estos valores después de su inicialización. Además, los estudiantes aprenderán la convención de usar mayúsculas para nombrar constantes en Python y entenderán las implicaciones de no seguir esta regla.

A través de estos ejercicios, los alumnos desarrollarán competencias en la identificación y uso adecuado de variables y constantes, así como en la aplicación de buenas prácticas de programación para garantizar la consistencia y claridad del código.

### Las constantes no deberian cambiar
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código muestra la diferencia entre el uso de variables y constantes en Python. En primer lugar, se establece una variable llamada `edad` con un valor inicial de 47. Luego, se imprime esa edad utilizando una sentencia `print`. Después, el valor de `edad` cambia a 48 y vuelve a imprimirse. Esto demuestra que las variables pueden modificarse durante la ejecución del programa.

Posteriormente, el código define un valor constante llamado `PI`, inicializado con el valor 3.1416, lo cual es típico para representar el número pi en matemáticas y programación. Se imprime este valor de PI. Sin embargo, a continuación se intenta cambiar el valor de `PI` a 4, mostrando nuevamente que esto funciona en Python, pero no debería hacerse porque las constantes, por definición, son valores que no deben cambiarse durante la ejecución del programa.

Este ejemplo ilustra por qué es importante usar nombres en mayúsculas para identificar los valores de constante y respetar el propósito de dichos valores, manteniéndolos invariables.

`001-Las constantes no deberian cambiar.py`

```python
edad = 47
print("tengo",edad,"años")
edad = 48 # se puede variar el valor de una variable
print("tengo",edad,"años")

# variables en minúscula, constantes en mayúscula
PI = 3.1416
print("El valor de PI es:",PI)
PI = 4
print("El valor de PI es:",PI) # Funciona, pero no debe ocurrir
```

### Actividades propuestas

### Actividad 1: Identificación y Uso de Constantes

**Descripción:** Los estudiantes deben identificar las diferencias entre variables y constantes en el código proporcionado. La actividad consiste en analizar por qué es importante no modificar el valor de una constante, a pesar de que técnicamente se puede hacer. El objetivo es entender la importancia del uso correcto de constantes para mantener la integridad del programa.

### Actividad 2: Creación de Constantes Propias

**Descripción:** Los estudiantes deben crear un nuevo script Python donde definan varias constantes propias y expliquen su significado. La actividad incluye el uso correcto de las convenciones de nomenclatura para constantes (mayúsculas). Se espera que los alumnos comprendan la necesidad de mantener valores invariables en ciertos contextos del programa.

### Actividad 3: Implementación de Reglas de Uso de Constantes

**Descripción:** Los estudiantes deben revisar el código proporcionado y aplicar las buenas prácticas para el uso de constantes, como evitar cambiar su valor durante la ejecución del programa. Se les pide que modifiquen el código existente según estas reglas y expliquen sus cambios.

### Actividad 4: Programa Sencillo con Constantes

**Descripción:** Los estudiantes deben crear un programa simple en Python que use al menos tres constantes para representar valores invariables, como las dimensiones de una figura geométrica. El objetivo es practicar la declaración y uso efectivo de constantes en situaciones reales.

### Actividad 5: Documentación de Constantes

**Descripción:** Los estudiantes deben documentar cada constante utilizada en un programa simple, explicando su significado e importancia. La actividad busca mejorar las habilidades de documentación y comentarios en el código, ayudando a otros desarrolladores a entender fácilmente la lógica del programa.

### Actividad 6: Ejecución y Análisis de Código con Constantes

**Descripción:** Los estudiantes recibirán un archivo Python que incluye constantes mal utilizadas. Se les pedirá ejecutar el código, analizar por qué algunas decisiones son inadecuadas y sugerir correcciones. La actividad busca mejorar la capacidad de análisis y depuración del código.

### Actividad 7: Comparación entre Variables y Constantes

**Descripción:** Los estudiantes deben escribir un breve ensayo comparando el uso de variables con constantes en Python, incluyendo ejemplos prácticos para cada caso. Se espera que los alumnos comprendan las diferencias conceptuales y su importancia en la programación.

### Actividad 8: Crear una Aplicación Mini-Real

**Descripción:** Los estudiantes deben crear una aplicación mini-real (como un programa de cálculos geométricos) que utilice al menos cinco constantes. Se espera que demuestren el uso correcto y efectivo de las constantes en la resolución de problemas reales.

Estas actividades buscan mejorar tanto los conocimientos teóricos como prácticos sobre el uso adecuado de constantes en Python, adaptadas a estudiantes de Formación Profesional.


<a id="operadores-y-expresiones"></a>
## Operadores y expresiones

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/001-Identificaci%C3%B3n%20de%20los%20elementos%20de%20un%20programa%20inform%C3%A1tico/006-Operadores%20y%20expresiones)

### Introducción a los ejercicios

En esta carpeta de ejercicios, se exploran los fundamentos del lenguaje Python centrándose en el uso y la comprensión de operadores y expresiones. Los estudiantes aprenderán a utilizar diferentes tipos de operadores aritméticos para realizar cálculos matemáticos básicos y avanzados, así como operadores de comparación para evaluar condiciones lógicas. Además, se practicarán los operadores de asignación abreviada que facilitan la modificación de variables en una sola línea de código. También se introducirá el uso de operadores booleanos (AND y OR) para combinar múltiples expresiones condicionales. Estos ejercicios ayudarán a mejorar las habilidades fundamentales necesarias para resolver problemas mediante programación.

### operadores aritmeticos
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python muestra cómo se utilizan diferentes operadores aritméticos básicos. El programa imprime cinco resultados diferentes, cada uno calculado con un tipo distinto de operación matemática:

1. La primera línea suma dos números: `4 + 3`, lo que resulta en el número `7`.
2. En la segunda línea, resta un número del otro: `4 - 3`, dando como resultado `1`.
3. La tercera línea multiplica dos números entre sí: `4 * 3`, lo cual es igual a `12`.
4. Luego, en la cuarta línea, divide el primer número por el segundo: `4 / 3`. El resultado será un punto flotante (`1.33333333333`), ya que Python devuelve una división con decimales.
5. Por último, utiliza el operador módulo `%`, que retorna el resto de la división entre dos números: `4 % 3`, dando como resultado `1`.

Estos ejemplos son fundamentales para entender cómo funcionan las operaciones aritméticas básicas en Python y son esenciales cuando se está empezando a programar.

`001-operadores aritmeticos.py`

```python
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(4%3)
```

### operadores de comparacion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código en Python muestra cómo funcionan los operadores de comparación entre dos números. En específico, compara el número 4 con el número 3 utilizando diferentes tipos de operadores: menor que (`<`), menor o igual que (`<=`), mayor que (`>`), mayor o igual que (`>=`), igual a (`==`) y diferente de (`!=`). Cada línea del código imprime en la pantalla si una cierta condición es verdadera (True) o falsa (False). Por ejemplo, cuando se compara `4 < 3`, el resultado es False porque cuatro no es menor que tres. Este tipo de comparaciones son fundamentales para controlar el flujo de programas y tomar decisiones basadas en condiciones específicas.

`002-operadores de comparacion.py`

```python
print(4 < 3)
print(4 <= 3)
print(4 > 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```

### Operadores aritmeticos abreviados
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra cómo modificar y trabajar con una variable llamada `edad` utilizando operadores aritméticos abreviados en Python. En primer lugar, la variable `edad` se inicializa con el valor 47. Luego, se utilizan diferentes operaciones para cambiar este valor: suma (`+=`), resta (`-=`), multiplicación (`*=`) y división (`/=`). Estos operadores permiten realizar una operación matemática directamente sobre la variable existente sin necesidad de escribir el nombre de la variable dos veces.

Por ejemplo, cuando se usa `edad += 5`, lo que realmente está haciendo es sumar 5 a la edad actual y luego asignar ese nuevo valor a `edad`. De manera similar, los otros operadores abreviados reducen la cantidad de código necesario para realizar cálculos comunes. Al final de cada operación, el programa imprime en pantalla el nuevo valor de `edad`, permitiéndonos ver cómo cambia con cada operación.

Estas técnicas son útiles porque hacen que el código sea más conciso y fácil de leer, especialmente cuando se necesitan realizar ajustes repetidos a una variable.

`003-Operadores aritmeticos abreviados.py`

```python
edad = 47
print(edad)

# edad = edad + 5
edad += 5
print(edad)

# edad = edad - 5
edad -= 5
print(edad)

# edad = edad * 5
edad *= 5
print(edad)

# edad = edad / 5
edad /= 5
print(edad)
```

### booleanos
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código te muestra cómo funcionan los operadores lógicos "and" y "or" en Python. Estos operadores se utilizan para combinar o comparar múltiples condiciones booleanas (verdaderas o falsas).

En las primeras dos líneas, el código compara tres igualdades usando el operador "and". El resultado será verdadero solo si todas las comparaciones son ciertas. En la primera línea, todos los números se comparan consigo mismos, por lo que el resultado es verdadero. Sin embargo, en la segunda línea, al menos una de las comparaciones (2 == 1) es falsa, por lo que todo el resultado será falso.

Las siguientes líneas usan el operador "or" para combinar tres condiciones booleanas. Con "or", si cualquiera de las comparaciones es verdadera, entonces la expresión completa será verdadera. En la línea donde todos son iguales a sí mismos, todo sale verdadero. Pero en otras líneas, cuando algunas comparaciones son falsas, el resultado final dependerá de si alguna de ellas era verdadera o no.

Este tipo de código es fundamental para entender cómo se evalúan condiciones múltiples en programas más grandes y complejos, como por ejemplo en bucles (ciclos) y estructuras condicionales.

`004-booleanos.py`

```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)


print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)
```

### Actividades propuestas

### Actividad 1: Operaciones Aritméticas Básicas

**Descripción:** 
Los estudiantes deben crear un programa que realice operaciones aritméticas básicas (suma, resta, multiplicación, división y módulo) entre dos números dados por el usuario. Se espera que los alumnos comprendan cómo usar correctamente los operadores aritméticos en Python.

### Actividad 2: Evaluación de Expresiones Lógicas

**Descripción:** 
Los estudiantes deben escribir un programa que evalúe varias expresiones lógicas utilizando operadores de comparación (como `<`, `>`, `==`). El objetivo es aprender a manipular y comprender la evaluación condicional en Python.

### Actividad 3: Operaciones Aritméticas Abreviadas

**Descripción:** 
Los alumnos deben desarrollar un código que implemente operadores de asignación abreviados (como `+=`, `-=`) para realizar diferentes tipos de cálculos. Esta actividad permite familiarizarse con la sintaxis más concisa para realizar operaciones aritméticas en variables.

### Actividad 4: Ejercicio de Operadores Lógicos

**Descripción:** 
Los estudiantes deben crear un programa que utilice los operadores lógicos `and` y `or`. El objetivo es entender cómo combinar expresiones booleanas para evaluar condiciones más complejas.

### Actividad 5: Cálculo de Promedio con Operadores Aritméticos

**Descripción:** 
Los alumnos deben diseñar un programa que calcule el promedio de una lista de números ingresados por el usuario, utilizando operaciones aritméticas. Esto ayuda a reforzar el uso de operadores en situaciones prácticas.

### Actividad 6: Juego Simple con Operadores y Comparaciones

**Descripción:** 
Los estudiantes deben crear un juego sencillo (como adivinar un número) que utilice expresiones lógicas basadas en comparaciones. El objetivo es aplicar los conceptos aprendidos de forma divertida.

### Actividad 7: Calculadora Básica con Operadores Aritméticos

**Descripción:** 
Los alumnos deben implementar una calculadora básica que permita al usuario realizar operaciones aritméticas y mostrar el resultado. Esto mejora la comprensión del uso de operadores en contextos interactivos.

### Actividad 8: Combinación de Operadores Lógicos y Aritméticos

**Descripción:** 
Los estudiantes deben escribir un programa que combina operadores lógicos con aritméticos para resolver problemas más complejos. Por ejemplo, determinar si un número es par o impar utilizando una combinación de ambos tipos de operadores.

### Actividad 9: Resolución de Problemas con Operadores

**Descripción:** 
Los alumnos deben identificar y corregir errores en fragmentos de código dados que utilizan operadores. Esto ayuda a desarrollar habilidades de depuración y mejora la comprensión del uso correcto de los operadores.

### Actividad 10: Simulación de Cálculos Financieros

**Descripción:** 
Los estudiantes deben crear un programa que simule cálculos financieros básicos (como intereses simples o tasa anual) utilizando operadores aritméticos y comparativos. Esto permite aplicar los conceptos aprendidos en situaciones del mundo real.

Estas actividades están diseñadas para complementar el contenido de la carpeta proporcionada, enfatizando la práctica y comprensión de los operadores y expresiones en Python a nivel de Formación Profesional.


<a id="ejercicio-de-final-de-unidad"></a>
## Ejercicio de final de unidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/001-Identificaci%C3%B3n%20de%20los%20elementos%20de%20un%20programa%20inform%C3%A1tico/101-Ejercicio%20de%20final%20de%20unidad)

### Introducción a los ejercicios

El archivo en esta carpeta, "001-actividad.md", contiene un ejercicio diseñado para ayudarte a consolidar tus conocimientos sobre los elementos fundamentales de la programación informática. Este tipo de ejercicios te permitirá aplicar y revisar conceptos clave como algoritmos, variables, estructuras de control (condicionales y bucles), funciones y manejo básico de entrada/salida en un programa. La finalidad es que comprendas cómo estos elementos interactúan para crear programas completos, así como mejorar tus habilidades de resolución de problemas y lógica computacional.

### Actividades propuestas

### Actividades Propuestas:

1. **Análisis de Elementos del Programa**
   - Los estudiantes deben identificar y clasificar los diferentes elementos de un programa informático presentes en el archivo proporcionado.
   - Se pretende que reconozcan conceptos básicos como variables, estructuras de control, bucles, entre otros.

2. **Diagramas de Flujo**
   - Los estudiantes deberán crear diagramas de flujo que representen el flujo lógico del programa analizado en la carpeta.
   - Se busca que comprendan cómo se visualiza un algoritmo y las relaciones entre sus componentes.

3. **Resolución de Problemas Básicos**
   - Los estudiantes deben plantear problemas sencillos (como cálculos matemáticos) y resolverlos utilizando el mismo lenguaje de programación del archivo.
   - El objetivo es que aprendan a aplicar los conceptos básicos de la programación para resolver tareas cotidianas.

4. **Modificación de Código**
   - Los estudiantes modificarán pequeños detalles en el código proporcionado (cambiar variables, añadir o quitar líneas) y observarán cómo afecta su funcionamiento.
   - El objetivo es que comprendan la relación entre el código escrito y su resultado.

5. **Documentación del Código**
   - Los estudiantes redactarán comentarios en el código proporcionado para explicar las funcionalidades de cada sección, así como describir variables y funciones clave.
   - Se busca mejorar sus habilidades en la documentación técnica y la comunicación clara sobre aspectos técnicos.

6. **Creación de Algoritmos**
   - Los estudiantes diseñarán algoritmos para tareas específicas (por ejemplo, calcular el área de diferentes figuras geométricas) basándose en los conceptos presentes en el ejercicio.
   - Se busca que apliquen lo aprendido sobre estructuras lógicas y control del flujo.

7. **Comparación de Estructuras**
   - Los estudiantes analizarán cómo cambiar la estructura (por ejemplo, de un bucle while a for) puede afectar al rendimiento o simplicidad del código.
   - Se pretende que entiendan las ventajas y desventajas de diferentes enfoques.

8. **Pruebas Unitarias Básicas**
   - Los estudiantes crearán pruebas unitarias básicas para el código proporcionado, verificando la correcta ejecución de cada función o bloque.
   - El objetivo es que aprendan a asegurar la funcionalidad del software antes de su implementación.

9. **Refactorización de Código**
   - Los estudiantes refactorizarán el código existente para mejorar su legibilidad y eficiencia, manteniendo las mismas funciones.
   - Se busca que comprendan cómo mejorar un programa sin cambiar su comportamiento observable.

10. **Presentación Oral del Proyecto**
    - Los estudiantes prepararán una presentación oral explicando los conceptos clave aprendidos a partir de la práctica y su proyecto individual o en grupo.
    - El objetivo es practicar sus habilidades de comunicación técnica y defensa de propuestas técnicas.



<a id="utilizacion-de-objetos"></a>
# Utilización de objetos

<a id="caracteristicas-de-los-objetos"></a>
## Características de los objetos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/002-Utilizaci%C3%B3n%20de%20objetos/001-Caracter%C3%ADsticas%20de%20los%20objetos)

### Introducción a los ejercicios

En esta subunidad, se centra en la comprensión y utilización de objetos predefinidos en el lenguaje de programación, sin entrar en la creación de clases personalizadas. Los ejercicios trabajan con las características fundamentales de los objetos, como sus propiedades (atributos estáticos), métodos (funciones dinámicas) y constructores (función que se ejecuta al inicializar el objeto). Asimismo, se explorará cómo estos elementos pueden ser utilizados en operaciones avanzadas como la herencia y el polimorfismo. Estos ejercicios ayudarán a los estudiantes a modularizar y reutilizar bloques de código, lo cual es crucial para crear programas más complejos y mantenibles.

### Actividades propuestas

### Actividad 1: Exploración de Objetos Predeterminados
**Descripción:** Los alumnos deben identificar y explorar los objetos predeterminados disponibles en el lenguaje de programación que están estudiando. Se espera que documenten las principales características, métodos y propiedades de al menos tres objetos diferentes. Esta actividad permitirá a los estudiantes familiarizarse con la utilidad y funcionalidades básicas de estos objetos.

### Actividad 2: Creación de Instancias
**Descripción:** Los alumnos deben crear varias instancias (objetos) utilizando los tipos de datos predeterminados del lenguaje, como cadenas o números. Se espera que se familiaricen con cómo inicializar y acceder a las propiedades y métodos básicos de estos objetos.

### Actividad 3: Uso de Métodos
**Descripción:** Los estudiantes deben utilizar varios métodos proporcionados por los objetos predeterminados para realizar operaciones como formatear cadenas, manipular números o gestionar fechas. Se espera que aprendan a aplicar los métodos adecuadamente y observen cómo cambian las propiedades del objeto después de la ejecución.

### Actividad 4: Comparación de Objetos
**Descripción:** Los alumnos deben escribir código para comparar objetos basados en sus propiedades y métodos. Esto incluye verificar la igualdad, buscar diferencias entre instancias o realizar operaciones que involucren múltiples objetos. Se pretende que comprendan las implicaciones de trabajar con objetos mutables e inmutables.

### Actividad 5: Uso del Constructor
**Descripción:** Los estudiantes deben crear una instancia de un objeto utilizando un constructor y luego modificar sus propiedades a través de métodos proporcionados por el lenguaje. Se espera que entiendan cómo inicializarse y manipular objetos desde su creación hasta su uso final.

### Actividad 6: Documentación y Ejemplos
**Descripción:** Los alumnos deben buscar en documentación oficial del lenguaje ejemplos de utilización de los objetos predeterminados. Se espera que generen un resumen o guía simple con las características más comunes y cómo usarlas, ayudando así a otros compañeros a entender mejor el uso de estos objetos.

### Actividad 7: Integración en Proyectos
**Descripción:** Los estudiantes deben incorporar objetos predeterminados dentro de proyectos pequeños que ya estén desarrollando. Se pretende que integren funciones y características existentes para ahorrar tiempo y mejorar la eficiencia del código.

### Actividad 8: Pruebas Unitarias
**Descripción:** Los alumnos deben escribir pruebas unitarias para verificar el correcto funcionamiento de las propiedades y métodos de los objetos predeterminados que estén utilizando en sus proyectos. Se espera que comprendan la importancia de la prueba exhaustiva y la verificación del código.

### Actividad 9: Análisis Crítico
**Descripción:** Los estudiantes deben analizar ejemplos proporcionados por el profesor, identificando cómo se utiliza eficazmente la programación orientada a objetos con los tipos de datos predeterminados. Se espera que hagan sugerencias sobre mejoras y discutan las ventajas y desventajas del uso de estos objetos.

### Actividad 10: Aplicaciones Prácticas
**Descripción:** Los alumnos deben diseñar e implementar una aplicación simple utilizando los conocimientos adquiridos sobre la creación, manipulación y utilización de objetos predeterminados. Se espera que apliquen sus habilidades en un contexto práctico y realista, integrando diferentes conceptos aprendidos durante el curso.


<a id="instanciacion-de-objetos"></a>
## Instanciación de objetos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/002-Utilizaci%C3%B3n%20de%20objetos/002-Instanciaci%C3%B3n%20de%20objetos)

### Introducción a los ejercicios

En esta subunidad se enfatiza la utilización y manipulación de objetos predeterminados disponibles en el lenguaje Python, con especial énfasis en módulos como `math`. Los ejercicios aquí proporcionan práctica en cómo importar módulos, acceder a sus funciones y métodos, y utilizarlos para resolver problemas matemáticos y científicos. Estos ejercicios son cruciales para entender la integración de herramientas ya existentes en el ecosistema Python, lo que permite a los estudiantes concentrarse en la resolución de problemas concretos sin necesidad de crear sus propias clases desde cero.

### importamos math
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código es muy simple pero fundamental. La línea `import math` importa el módulo matemático estándar de Python en tu programa. Este módulo contiene muchas funciones útiles para cálculos matemáticos, como raíces cuadradas, exponenciales y senos, cosenos entre otros. Al importarlo, puedes utilizar todas estas funciones directamente en tu código, lo que te permite hacer operaciones matemáticas complejas sin tener que escribir toda la lógica desde cero.

Es importante entender cómo usar los módulos de Python porque esto hace que el desarrollo de software sea más eficiente y menos propenso a errores. En lugar de reinventar ruedas, puedes aprovechar las soluciones ya probadas y disponibles en estos módulos estándar o incluso creados por la comunidad.

`001-importamos math.py`

```python
import math
```

### Actividades propuestas

### Actividad 1: Utilización del Módulo Math
**Descripción:** Los estudiantes deben importar y utilizar funciones específicas del módulo `math` para resolver cálculos matemáticos comunes. Se pretende que comprendan cómo se importan y utilizan bibliotecas de Python.

### Actividad 2: Cálculo de Área y Perímetro
**Descripción:** Los alumnos deben utilizar funciones del módulo math para calcular el área y el perímetro de diferentes figuras geométricas. El objetivo es que dominen la manipulación de fórmulas matemáticas en Python.

### Actividad 3: Operaciones con Números Aproximados
**Descripción:** Los estudiantes deben realizar cálculos que involucren números aproximados utilizando funciones como `round()` o `floor()`. Se espera que aprendan a manejar resultados numéricos precisamente.

### Actividad 4: Comparación de Números
**Descripción:** Utilizando operaciones matemáticas, los alumnos deben comparar dos números y determinar cuál es mayor. Esta actividad busca reforzar el uso de funciones como `max()` en Python.

### Actividad 5: Conversión entre Grados y Radianes
**Descripción:** Los estudiantes deben escribir un programa que convierta grados a radianes y viceversa, utilizando las funciones adecuadas del módulo math. Se pretende mejorar su comprensión de unidades en matemáticas.

### Actividad 6: Cálculo de Potencia y Raíz Cuadrada
**Descripción:** Los alumnos deben crear un programa que calcule la potencia y la raíz cuadrada de números dados, utilizando las funciones pertinentes del módulo math. El objetivo es practicar con operaciones matemáticas avanzadas.

### Actividad 7: Generación de Números Aleatorios
**Descripción:** Los estudiantes deben usar el módulo `random` (similar al math en estructura) para generar números aleatorios y crear un programa que simule lanzamientos de dados. Se espera mejorar su capacidad de programar simulaciones simples.

### Actividad 8: Resolución de Problemas Matemáticos Complejos
**Descripción:** Utilizando las funciones del módulo math, los alumnos deben resolver problemas matemáticos complejos como ecuaciones cuadráticas o cálculos trigonométricos. Se busca que apliquen lo aprendido a situaciones prácticas.

### Actividad 9: Creación de Funciones Personalizadas
**Descripción:** Los estudiantes deben crear funciones personalizadas que usan métodos del módulo math para resolver problemas específicos, como calcular la hipotenusa en un triángulo rectángulo. Se pretende que practiquen el desarrollo y uso de funciones propias.

### Actividad 10: Análisis Estadístico Básico
**Descripción:** Los alumnos deben utilizar las funciones del módulo math para realizar cálculos estadísticos básicos como promedios, medias geométricas y desviaciones estándar. Se espera que comprendan cómo aplicar matemáticas en análisis de datos simples.


<a id="utilizacion-de-metodos-parametros"></a>
## Utilización de métodos. Parámetros

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/002-Utilizaci%C3%B3n%20de%20objetos/003-Utilizaci%C3%B3n%20de%20m%C3%A9todos.%20Par%C3%A1metros)

### Introducción a los ejercicios

Esta carpeta contiene ejercicios diseñados para que los estudiantes de Formación Profesional practiquen la utilización de métodos y parámetros en objetos predefinidos del lenguaje Python. Los ejercicios se centran en cómo llamar a funciones específicas (métodos) desde bibliotecas existentes, como `math`, para realizar operaciones matemáticas complejas con objetos numéricos básicos. Estos ejercicios ayudan a los estudiantes a comprender la importancia de las librerías predefinidas y cómo interactuar efectivamente con ellas mediante la invocación adecuada de métodos.

### Metodos de un objeto
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código importa el módulo `math` de Python y le da un alias `matematicas`. Luego, utiliza la función `sqrt`, que está dentro del módulo `matematicas`, para calcular la raíz cuadrada del número 16. La función `sqrt` devuelve el valor de la raíz cuadrada, que en este caso es 4, y ese resultado se imprime en pantalla mediante el uso de la función `print`. Es importante usar aliases como `matematicas` para evitar confusiones si estás utilizando múltiples módulos o funciones con nombres similares.

`001-Metodos de un objeto.py`

```python
import math as matematicas

print(matematicas.sqrt(16))
```

### ejemplo más esparcido
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python importa el módulo `math` bajo el alias `matematicas`. Luego, se define una variable llamada `numero` y se le asigna el valor 16. A continuación, se calcula la raíz cuadrada del número utilizando la función `sqrt()` del módulo `matematicas`, y el resultado de esta operación es almacenado en la variable `raiz`. Finalmente, el código imprime en pantalla el valor que contiene la variable `raiz`.

Este ejemplo demuestra cómo importar un paquete externo para realizar cálculos matemáticos más complejos y cómo utilizar una función específica del paquete. Es importante conocer estas funciones porque simplifican mucho los cálculos, como calcular raíces cuadradas en este caso, sin tener que programar la fórmula desde cero.

`002-ejemplo más esparcido.py`

```python
import math as matematicas

numero = 16
raiz = matematicas.sqrt(numero)
print(raiz)
```

### Actividades propuestas

### Actividad 1: Utilización de Métodos en Objetos Matemáticos
**Descripción:** Los estudiantes deberán importar el módulo `math` y utilizar métodos como `sqrt()` para calcular la raíz cuadrada de varios números. Esta actividad les permitirá familiarizarse con cómo acceder a métodos existentes dentro del lenguaje Python.

### Actividad 2: Creación de Variables Intermedias
**Descripción:** Los estudiantes deben modificar el código proporcionado para que las operaciones matemáticas se realicen sobre variables intermedias, lo cual les ayudará a entender la importancia de almacenar resultados parciales antes de imprimirlos.

### Actividad 3: Métodos Numéricos Variados
**Descripción:** Los estudiantes tendrán que investigar y utilizar otros métodos matemáticos del módulo `math`, como `sin()`, `cos()` o `tan()`, para calcular funciones trigonométricas de diferentes valores.

### Actividad 4: Introducción a la Interactividad
**Descripción:** Se pedirá a los estudiantes que modifiquen el código para solicitar al usuario que introduzca un número, y luego calculen su raíz cuadrada utilizando `sqrt()`. Esta actividad les enseñará cómo integrar conceptos de entrada/salida en sus programas.

### Actividad 5: Redondeo Numérico
**Descripción:** Los estudiantes tendrán que utilizar el método `round()` para redondear un número decimal proporcionado por ellos mismos o a través de la entrada del usuario. Esto les ayudará a entender cómo manejar números con precisión en Python.

### Actividad 6: Comparación Numérica
**Descripción:** Se pide a los estudiantes que creen una función simple que compare dos números utilizando métodos numéricos para determinar cuál es mayor, lo cual les permitirá aprender sobre operaciones condicionales y comparativas con objetos matemáticos.

### Actividad 7: Utilización del Módulo Random
**Descripción:** Los estudiantes deben importar el módulo `random` junto a `math`, generar un número aleatorio entre dos valores especificados, y calcular su raíz cuadrada. Esto familiarizará a los alumnos con la generación de números pseudoaleatorios.

### Actividad 8: Documentación de Códigos
**Descripción:** Se les solicita a los estudiantes que escriban comentarios en sus códigos para explicar cada método y función utilizadas, así como su propósito dentro del programa. Esto reforzará la importancia de la documentación clara y detallada en el desarrollo de software.

### Actividad 9: Uso de Métodos con Parámetros
**Descripción:** Los estudiantes deben identificar métodos que aceptan parámetros, como `math.pow(x, y)` para calcular potencias, e implementarlos en sus programas. Esto les permitirá comprender cómo pasar argumentos a funciones y métodos.

### Actividad 10: Integración de Métodos Matemáticos
**Descripción:** Los estudiantes deben combinar varios métodos matemáticos (por ejemplo, `sin()`, `cos()` y `tan()`) en un único programa para resolver problemas más complejos. Esto les ayudará a aprender cómo integrar múltiples conceptos matemáticos mediante programación.


<a id="utilizacion-de-propiedades"></a>
## Utilización de propiedades

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/002-Utilizaci%C3%B3n%20de%20objetos/004-Utilizaci%C3%B3n%20de%20propiedades)

### Introducción a los ejercicios

En esta subcarpeta de ejercicios, los estudiantes se centrarán en la utilización y manipulación de objetos predeterminados que existen en el lenguaje Python, con énfasis especial en sus propiedades. Los ejercicios buscan desarrollar habilidades para trabajar con módulos incorporados del sistema y entender cómo acceder a valores predefinidos como constantes matemáticas. A través de estos problemas, los estudiantes aprenderán a importar paquetes y utilizar propiedades específicas dentro del contexto de la programación orientada a objetos en Python.

### tiene propiedades
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código es muy sencillo y te muestra cómo acceder a una constante específica en el módulo de matemáticas en Python. Lo que hace este fragmento es importar la biblioteca `math` con un alias, llamándola simplemente `matematicas`. Luego, se guarda el valor de la constante π (pi) en una variable también llamada `PI`, que obtiene su valor desde `matematicas.pi`. Finalmente, el código imprime el valor de `PI` en pantalla. Esto es importante porque te permite utilizar constantes matemáticas predefinidas y hacer cálculos más precisos en tus programas.

El uso de alias para bibliotecas largas como `math` facilita la lectura del código y lo hace menos tedioso, permitiéndote centrarte en el propósito específico del programa.

`001-tiene propiedades.py`

```python
import math as matematicas

PI = matematicas.pi

print(PI)
```

### Actividades propuestas

### Actividades Propuestas:

#### 1. **Identificación y Uso de Constantes Matemáticas**
**Descripción:** Identifica y utiliza constantes matemáticas como `math.pi` en Python para calcular el área de un círculo dado su radio. Se pretende que los estudiantes comprendan cómo acceder a las propiedades predefinidas del módulo math.

#### 2. **Comparación de Constantes Matemáticas**
**Descripción:** Escribe una función que compare dos valores numéricos, uno proporcionado por el usuario y otro obtenido mediante una propiedad del módulo `math`. Se espera que los estudiantes aprendan a utilizar propiedades matemáticas en comparaciones.

#### 3. **Cálculo de Longitud con Propiedades Matemáticas**
**Descripción:** Utiliza la constante `math.pi` para calcular y mostrar la longitud de una circunferencia dada su radio. Esta actividad busca que los estudiantes comprendan cómo aplicar propiedades matemáticas en cálculos geométricos.

#### 4. **Impresión de Varias Propiedades Matemáticas**
**Descripción:** Modifica el código existente para imprimir varias constantes del módulo `math`, como pi y e, en un solo bloque de código. El objetivo es que los estudiantes practiquen la importación y uso múltiple de propiedades.

#### 5. **Cálculo de Ángulos con Trigonometría**
**Descripción:** Implementa funciones para calcular el seno y coseno de diferentes ángulos utilizando las propiedades del módulo `math`. Se busca que los estudiantes trabajen con funciones trigonométricas predefinidas.

#### 6. **Conversión de Grados a Radianes**
**Descripción:** Escribe un programa que convierta grados en radianes usando la constante pi y las fórmulas matemáticas adecuadas. Se espera que los estudiantes utilicen correctamente propiedades matemáticas para conversiones.

#### 7. **Comparación de Números con Propiedades**
**Descripción:** Crea una función que compare dos números proporcionados por el usuario utilizando propiedades del módulo `math`, como raíz cuadrada o logaritmo, y determine cuál es mayor. Se busca mejorar la comprensión sobre el uso de propiedades matemáticas en operaciones.

#### 8. **Generación de Sequencias Numéricas**
**Descripción:** Utiliza funciones del módulo `math` para generar una secuencia numérica (por ejemplo, números primos menores a un número dado) y almacenarla en una lista o tupla. Esta actividad busca que los estudiantes apliquen varias propiedades matemáticas de manera coherente.

#### 9. **Uso de Propiedades en Cálculos Complejos**
**Descripción:** Desarrolla un programa que realice cálculos más complejos utilizando múltiples propiedades del módulo `math`, como potencias, logaritmos y funciones trigonométricas. Se pretende reforzar la comprensión de cómo combinar varias propiedades en una misma tarea.

#### 10. **Creación de Tablas Numéricas**
**Descripción:** Crea un programa que genere tablas numéricas basadas en cálculos matemáticos utilizando constantes y funciones del módulo `math`. Se espera que los estudiantes aprendan a organizar e imprimir resultados matemáticos complejos.


<a id="utilizacion-de-metodos-estaticos"></a>
## Utilización de métodos estáticos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/002-Utilizaci%C3%B3n%20de%20objetos/005-Utilizaci%C3%B3n%20de%20m%C3%A9todos%20est%C3%A1ticos)

### Introducción a los ejercicios

En esta carpeta de ejercicios, se exploran los conceptos básicos del uso de métodos estáticos y la manipulación de objetos predefinidos en Python. Los estudiantes aprenderán a trabajar con estructuras de datos como listas y diccionarios, utilizando sus métodos integrados para realizar operaciones como ordenar elementos o crear diccionarios iniciales. El objetivo es familiarizarse con las funcionalidades incorporadas del lenguaje sin la necesidad de definir clases personalizadas, centrando así el enfoce en la aplicación práctica y directa de estos objetos predefinidos en soluciones programáticas cotidianas.

### instanciacion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python muestra cómo trabajar con listas y ordenar sus elementos. Primero, se crea una lista llamada `frutas` que contiene tres tipos diferentes de frutas: 'platano', 'fresa' e 'naranja'. Luego, se imprime la lista original usando el comando `print(frutas)`, lo que te muestra cómo están dispuestas inicialmente las frutas en la lista.

Después, se utiliza el método `sort()` que ordena los elementos de la lista alfabéticamente (de A a Z). Este método cambia directamente la lista existente sin necesidad de crear una nueva. Finalmente, el código imprime nuevamente la lista después de que ha sido ordenada.

Este ejemplo es importante porque demuestra cómo manipular y organizar datos en Python utilizando métodos integrados para trabajar con listas, lo cual es fundamental cuando se trabaja con colecciones de información en programas más grandes.

`001-instanciacion.py`

```python
frutas = ['platano','fresa','naranja']
print(frutas)
frutas.sort()
print(frutas)
```

### no instancio estatico
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código crea un diccionario en Python y luego imprime dicho diccionario. El diccionario se inicializa usando el método estático `fromkeys()` que pertenece a la clase dict (dictionario). Este método toma dos argumentos: una lista de claves ("manzana", "pera" y "platano") y un valor predeterminado (5 en este caso). Lo que hace es crear un diccionario donde cada clave se asigna al mismo valor por defecto. En este ejemplo, el resultado será un diccionario con tres elementos: {"manzana": 5, "pera": 5, "platano": 5}. Luego, la función `print(frutas)` muestra en pantalla el contenido del diccionario recién creado.

Este código es útil porque demuestra cómo utilizar métodos estáticos de una clase para crear objetos (en este caso, un diccionario) sin necesidad de instanciar explícitamente un objeto primero. Es decir, no se crea una variable que sea un objeto dict, sino que directamente se usa el nombre de la clase (`dict`) junto con su método estático (`fromkeys()`) para crear el diccionario. Esto simplifica la creación de estructuras de datos complejas en Python y es una forma concisa y eficiente de trabajar con los tipos integrados del lenguaje.

`002-no instancio estatico.py`

```python
frutas = dict.fromkeys(["manzana","pera","platano"],5)
print(frutas)
```

### Actividades propuestas

### Actividad 1: Manipulación de Listas con Métodos Estáticos

**Descripción:** Crea una lista de frutas y utiliza métodos para ordenarla y mostrar sus elementos. Aprenderás a usar los métodos estáticos integrados en Python para manipular listas.

### Actividad 2: Creación de Diccionarios usando Métodos Estáticos

**Descripción:** Utiliza el método `dict.fromkeys` para crear un diccionario con claves específicas y un valor inicial. Aprenderás a usar métodos estáticos para simplificar la creación de estructuras de datos.

### Actividad 3: Comparación de Listas y Diccionarios

**Descripción:** Crea una lista y un diccionario, muestra sus elementos e investiga las diferencias entre ambos tipos de colección. Aprenderás a seleccionar el tipo de dato adecuado según la necesidad.

### Actividad 4: Ordenamiento Personalizado en Listas

**Descripción:** Escribe código para ordenar una lista de frutas de forma personalizada (por ejemplo, alfabéticamente inverso). Aprenderás cómo aplicar métodos estáticos con funcionalidades más avanzadas.

### Actividad 5: Acceso a Métodos Estáticos en Clases Predefinidas

**Descripción:** Investiga y utiliza los métodos estáticos disponibles para las listas y diccionarios. Aprenderás la importancia de conocer el API integrado del lenguaje.

### Actividad 6: Uso de Funciones Builtin con Objetos

**Descripción:** Utiliza funciones incorporadas como `len()` o `sorted()` sobre listas y diccionarios para manipular sus elementos. Aprenderás a combinar métodos estáticos y funciones predefinidas.

### Actividad 7: Iteración sobre Colecciones de Datos

**Descripción:** Escribe un bucle que itere sobre una lista o un diccionario, mostrando cada elemento. Aprenderás la importancia del uso de iteradores con colecciones de datos en Python.

### Actividad 8: Crear y Modificar Diccionarios

**Descripción:** Crea un diccionario inicialmente vacío y añade elementos a él utilizando métodos estáticos. Aprenderás cómo manipular y modificar los diccionarios dinámicamente.

### Actividad 9: Utilización de Métodos Estáticos para Transformación de Datos

**Descripción:** Convierte una lista en un diccionario usando métodos estáticos, luego transforma el diccionario nuevamente a una lista. Aprenderás las ventajas y aplicaciones de estos métodos en la manipulación de datos.

### Actividad 10: Resolución de Problemas con Objetos Predefinidos

**Descripción:** Propón soluciones para problemas comunes utilizando objetos predefinidos (listas, diccionarios) y sus métodos estáticos. Aprenderás a aplicar tus conocimientos en contextos prácticos del mundo real.


<a id="constructores"></a>
## Constructores

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/002-Utilizaci%C3%B3n%20de%20objetos/006-Constructores)

### Introducción a los ejercicios

En esta subunidad de Programación, te enfocarás en aprender a utilizar objetos predeterminados que existen en el lenguaje de programación elegido, sin necesidad de crear clases personalizadas. El objetivo principal es entender y aplicar correctamente los constructores de estos objetos para inicializarlos con valores específicos. Durante la realización de estos ejercicios, practicarás tus habilidades en la manipulación de objetos estándar, configurando sus propiedades iniciales de manera efectiva y segura.

### Actividades propuestas

### Actividades Propuestas

1. **Uso de Constructores Predeterminados**
   - **Descripción**: Los estudiantes deben identificar y explicar cómo se utilizan los constructores predeterminados en objetos predefinidos del lenguaje de programación.
   - **Objetivo**: Aprender a utilizar correctamente los objetos existentes sin necesidad de definir nuevos constructores.

2. **Creación de Instancias de Clases**
   - **Descripción**: Los estudiantes crearán instancias de clases predefinidas y manipularán sus propiedades y métodos.
   - **Objetivo**: Familiarizarse con la creación y manipulación de objetos utilizando constructores predeterminados.

3. **Comparar Instancias de Objetos**
   - **Descripción**: Los estudiantes deben crear instancias de una clase predefinida, compararlas entre sí para verificar su igualdad e imprimir los resultados.
   - **Objetivo**: Aprender a utilizar operadores de comparación con objetos y entender la importancia de los constructores en esta tarea.

4. **Manipulación de Colecciones**
   - **Descripción**: Los estudiantes trabajarán con colecciones predefinidas (arrays, listas, etc.) para añadir, eliminar o buscar elementos.
   - **Objetivo**: Practicar la manipulación eficiente de estructuras de datos utilizando constructores predeterminados.

5. **Trabajar con Fechas y Tiempo**
   - **Descripción**: Crear objetos que representen fechas y tiempos, realizar operaciones como añadir días o calcular diferencias.
   - **Objetivo**: Familiarizarse con las clases de fecha y hora predefinidas del lenguaje.

6. **Uso de Objetos Matemáticos**
   - **Descripción**: Utilizar objetos matemáticos (números complejos, matrices) para realizar operaciones aritméticas.
   - **Objetivo**: Aprender a trabajar con tipos de datos matemáticos avanzados proporcionados por el lenguaje.

7. **Representación de Texto**
   - **Descripción**: Crear objetos String y manipularlos (concatenar, dividir, buscar subcadenas).
   - **Objetivo**: Dominar las operaciones básicas sobre cadenas de texto usando métodos predefinidos.

8. **Manejo de Archivos**
   - **Descripción**: Los estudiantes deben leer y escribir archivos utilizando objetos específicos para el manejo de archivos.
   - **Objetivo**: Aprender a utilizar los constructores adecuados para abrir, cerrar y manipular archivos desde el código.

9. **Uso de Módulos Predefinidos**
   - **Descripción**: Utilizar módulos predefinidos del lenguaje para realizar tareas como manejo de excepciones o acceso a la red.
   - **Objetivo**: Conocer y aplicar las clases proporcionadas por los módulos integrados.

10. **Aplicación Práctica**
    - **Descripción**: Desarrollar una pequeña aplicación que use varios objetos predefinidos para resolver un problema práctico (por ejemplo, gestión de contactos).
    - **Objetivo**: Integrar el conocimiento adquirido aplicándolo en un contexto real y desafiante.

Estas actividades permitirán a los estudiantes comprender y manipular correctamente los objetos predefinidos del lenguaje de programación, desarrollando habilidades fundamentales para la resolución de problemas prácticos.


<a id="destruccion-de-objetos-y-liberacion-de-memoria"></a>
## Destrucción de objetos y liberación de memoria

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/002-Utilizaci%C3%B3n%20de%20objetos/007-Destrucci%C3%B3n%20de%20objetos%20y%20liberaci%C3%B3n%20de%20memoria)

### Introducción a los ejercicios

En esta subunidad se enfatiza la comprensión y manejo adecuado de la gestión de objetos en el lenguaje de programación, centrándose específicamente en la destrucción de objetos y la liberación de memoria. Los estudiantes aprenderán a identificar cuándo es necesario que un objeto sea eliminado para optimizar los recursos del sistema y evitar problemas como fugas de memoria. Esta práctica es crucial para desarrollar programas eficientes y sostenibles, especialmente en proyectos más grandes o en entornos donde la gestión de memoria es crítica.

### Actividades propuestas

### Actividad 1: Creación y Destrucción de Objetos Básicos

**Descripción:** Los estudiantes deben implementar un programa que cree, utilice y luego destruya objetos básicos proporcionados por el lenguaje. Se espera que comprendan la importancia de liberar recursos una vez que ya no son necesarios.

### Actividad 2: Uso de Context Managers

**Descripción:** Los estudiantes deben utilizar context managers para asegurar que los objetos se destruyen adecuadamente al final del bloque con, evitando fugas de memoria.

### Actividad 3: Manejo de Recursos Conexión a BD

**Descripción:** Implementar una conexión a base de datos utilizando un objeto y luego liberar correctamente dicha conexión para evitar problemas de rendimiento y seguridad.

### Actividad 4: Destrucción Automática de Objetos Temporales

**Descripción:** Los estudiantes deben crear objetos temporales dentro de funciones o métodos que sean automáticamente destruidos al finalizar la ejecución del bloque. Esto ayudará a comprender el manejo automático de memoria en Python.

### Actividad 5: Identificación y Corrección de Fugas de Memoria

**Descripción:** Los estudiantes analizan código con potenciales fugas de memoria y corrigiendo estos problemas para asegurar la eficiencia del programa.

### Actividad 6: Comparación de Eficacia entre Diferentes Mecanismos de Liberación

**Descripción:** Comparar la eficacia en términos de rendimiento y seguridad entre diferentes métodos de liberación de memoria, como el uso explícito del método `del` o context managers.

### Actividad 7: Documentación sobre Buenas Prácticas de Uso de Memoria

**Descripción:** Los estudiantes redactan un breve documento explicando las mejores prácticas para el manejo de objetos y liberación de memoria en Python, basándose en ejemplos de código proporcionados.

### Actividad 8: Implementación de Clases con Métodos `__enter__` y `__exit__`

**Descripción:** Los estudiantes deben diseñar una clase personalizada que incluya métodos `__enter__` y `__exit__`, demostrando así cómo un objeto puede ser usado dentro de un bloque with para gestionar su ciclo de vida.

### Actividad 9: Pruebas Unitarias con Destrucción Automática

**Descripción:** Creación y ejecución de pruebas unitarias que validen el correcto funcionamiento del método `__del__` o la liberación automática de objetos cuando no se utilizan más.


<a id="ejercicio-de-final-de-unidad-1"></a>
## Ejercicio de final de unidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/002-Utilizaci%C3%B3n%20de%20objetos/101-Ejercicio%20de%20final%20de%20unidad)

### Introducción a los ejercicios

En esta unidad de programación, centraremos nuestra atención en la utilización eficiente de objetos, un concepto fundamental en el desarrollo orientado a objetos. El ejercicio proporcionado te permitirá aplicar y consolidar tus conocimientos sobre cómo crear, manipular y interactuar con diferentes tipos de objetos en tu programa. A través de este trabajo, practicarás competencias clave como la definición de clases, creación de instancias, uso de métodos y atributos, así como la gestión de relaciones entre objetos. Este ejercicio es un punto culminante que integra los temas aprendidos a lo largo del módulo, preparándote para proyectos más complejos en el futuro.

### Actividades propuestas

### Actividades Propuestas:

#### 1. **Clase y Objetos Básicos**
Descripción: Los estudiantes deben crear una clase simple en Python que represente un objeto básico (por ejemplo, un libro con atributos como título y autor). Se espera que aprendan a definir clases y objetos, así como a acceder a sus propiedades.

#### 2. **Métodos de Instancia**
Descripción: Los estudiantes deben añadir métodos a la clase del ejercicio anterior para manipular los datos (por ejemplo, método para mostrar detalles del libro). Se pretende que comprendan cómo implementar y usar métodos dentro de una clase.

#### 3. **Atributos Protegidos y Privados**
Descripción: Los estudiantes deben modificar la clase creada en el ejercicio anterior para incluir atributos protegidos y privados, e implementar métodos getter y setter para acceder a estos atributos. Se espera que comprendan la importancia de encapsulación.

#### 4. **Herencia entre Clases**
Descripción: Los estudiantes deben crear una nueva clase derivada (hija) que herede de la clase base del ejercicio anterior, añadiendo nuevas características o métodos específicos. Se pretende que entiendan cómo funciona la herencia en programación orientada a objetos.

#### 5. **Polimorfismo**
Descripción: Los estudiantes deben implementar el principio del polimorfismo creando un método abstracto en una clase base y sobrescribiéndolo en clases derivadas para que cada subclase tenga su propia funcionalidad única. Se espera que aprendan a usar interfaces o métodos virtuales.

#### 6. **Manejo de Excepciones**
Descripción: Los estudiantes deben añadir manejadores de excepciones a los ejercicios anteriores, asegurándose de que el programa pueda manejar errores comunes como la invocación de un método no existente o la manipulación de datos incorrectos. Se pretende que comprendan cómo proteger su código de fallos inesperados.

#### 7. **Iteradores y Generadores**
Descripción: Los estudiantes deben crear una clase iterable para listar todos los elementos de una colección (por ejemplo, libros en un catálogo) y luego implementar generadores para generar estos elementos sobre la marcha. Se espera que aprendan a utilizar iteradores y generadores eficientemente.

#### 8. **Decoradores**
Descripción: Los estudiantes deben diseñar decoradores que puedan aplicarse a las funciones o métodos de sus clases, añadiendo funcionalidades como registro de tiempo de ejecución para métodos críticos. Se pretende que comprendan el uso y la implementación de decoradores en Python.

#### 9. **Interfaz Gráfica Simple**
Descripción: Los estudiantes deben crear una interfaz gráfica simple usando Tkinter, mostrando objetos creados a partir de las clases anteriores (por ejemplo, mostrar detalles del libro en un formulario). Se espera que aprendan a combinar programación orientada a objetos con interfaces gráficas.

#### 10. **Documentación y Codificación Limpias**
Descripción: Los estudiantes deben escribir documentación para todos los métodos de las clases creadas y mejorar la limpieza del código (por ejemplo, usando convenciones de nombres claros). Se pretende que entiendan la importancia de mantener un código bien documentado y estructurado.



<a id="uso-de-estructuras-de-control"></a>
# Uso de estructuras de control

<a id="estructuras-de-seleccion"></a>
## Estructuras de selección

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/003-Uso%20de%20estructuras%20de%20control/001-Estructuras%20de%20selecci%C3%B3n)

### Introducción a los ejercicios

En esta carpeta, encontrarás una serie de ejercicios que te ayudarán a entender y aplicar las estructuras de selección en Python. Los ejercicios comienzan con simples condicionales `if` para evaluar condiciones básicas, como determinar si alguien es joven o no basándose en su edad. A medida que avances, se introducirán estructuras más complejas que incluyen cláusulas `else` y `elif` para manejar múltiples casos posibles. Además, practicarás la entrada de datos por consola para clasificar a personas o objetos según ciertos criterios. Estos ejercicios te permitirán mejorar tus habilidades en la toma de decisiones programáticas y el control del flujo de un programa basado en condiciones específicas.

### programacion paso a paso
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra tres instrucciones `print` seguidas entre sí. Cada una imprime en la consola un mensaje diferente, indicando los pasos 1, 2 y 3 del programa respectivamente. En este caso, no hay ninguna estructura de control ni condicional que afecte el flujo de ejecución; simplemente se realizan tres acciones secuenciales.

Esta parte del código es importante porque ilustra cómo imprimir texto en la consola, lo cual es una habilidad básica para proporcionar retroalimentación al usuario y visualizar los resultados intermedios de un programa. Es útil durante el desarrollo para verificar que las partes individuales del programa estén funcionando correctamente antes de avanzar a estructuras más complejas.

`001-programacion paso a paso.py`

```python
print("este es el paso 1")
print("este es el paso 2")
print("este es el paso 3")
```

### estructura if
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código muestra cómo utilizar la estructura `if` en Python para realizar una acción condicional. La línea `edad = 47` establece que la variable `edad` tiene el valor de 47 años. Luego, el programa verifica si esta edad es menor a 30 años utilizando la expresión `edad < 30`. Si esto es verdadero (lo cual no lo es en este caso, ya que 47 es mayor que 30), entonces se imprimiría "Eres un joven!". En resumen, el código evalúa una condición y ejecuta un bloque de código solo si dicha condición es cierta. Es importante entender estas estructuras de control porque permiten a los programas tomar decisiones basadas en diferentes condiciones durante su ejecución.

`002-estructura if.py`

```python
print("Mi nombre es Jose Vicente")
edad = 47

if edad < 30:
  print("Eres un joven!")
```

### else
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra cómo usar una estructura condicional `if-else` en Python. Primero, el programa imprime un mensaje que indica el nombre de la persona ("Mi nombre es Jose Vicente"). Luego, se establece una variable llamada `edad` con valor 47.

La línea clave aquí es el bloque `if-else`. El código verifica si la edad es menor a 30 años. Si este condicional es verdadero (es decir, si la persona tiene menos de 30 años), imprime "Eres un joven!". En caso contrario, cuando la condición no se cumple (la persona tiene 30 o más años), se ejecuta el bloque `else` y muestra el mensaje "Ya no eres un joven". Esta estructura permite que el programa tome decisiones basadas en diferentes condiciones, lo cual es fundamental para controlar el flujo de la lógica en programas más complejos.

`003-else.py`

```python
print("Mi nombre es Jose Vicente")
edad = 47

if edad < 30:
  print("Eres un joven!")
else:
  print("Ya no eres un joven")
```

### else if
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código es una secuencia que utiliza estructuras de selección (condicionales) para determinar en qué categoría se clasifica a una persona basándose en su edad. Primero, imprime el nombre "Mi nombre es Jose Vicente". Luego, establece la variable `edad` con un valor de 47 años.

El código usa varias estructuras `if`, `elif` (que significa "else if" o "sino si") y una estructura final `else`. Cada uno de estos bloques comprueba condiciones específicas sobre el valor de la edad:

1. Si `edad` es menor que 10, imprime "Eres un niño!".
2. Si no cumple con la condición anterior pero `edad` está entre 10 y 20 (inclusive), imprime "Eres un adolescente".
3. Si aún no se cumplen las condiciones anteriores pero `edad` está entre 20 y 30 (inclusive), imprime "Eres un joven".
4. Si ninguna de las condiciones anteriores es verdadera, lo que significa que la edad es mayor o igual a 30 años, entonces imprime "Ya no eres un joven".

Este tipo de estructuras condicionales son fundamentales en programación para tomar decisiones basadas en diferentes situaciones y permiten al programa ejecutar diferentes bloques de código dependiendo de las condiciones que se presentan.

`004-else if.py`

```python
print("Mi nombre es Jose Vicente")
edad = 47

if edad < 10:
  print("Eres un niño!")
elif edad >= 10 and edad < 20:
  print("Eres un adolescente")
elif edad >= 20 and edad < 30:
  print("Eres un joven")
else:
  print("Ya no eres un joven")
```

### entrada
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código es un ejemplo básico de cómo usar estructuras condicionales en Python para clasificar la edad de una persona. El programa comienza pidiendo al usuario que introduzca su edad. Es importante destacar que la función `input()` siempre devuelve un valor tipo cadena (string), por lo que se debe convertir a número entero con `int()` antes de poder hacer comparaciones numéricas.

Después, el código utiliza una estructura condicional compuesta por varias cláusulas `if`, `elif` y `else`. Si la edad es menor que 10, imprime "Eres un niño!". Si la edad está entre 10 y 20 años (inclusive), imprime "Eres un adolescente". Para edades de 20 a 30 años, se imprime "Eres un joven". Y si ninguna de estas condiciones se cumple, es decir, si la edad es mayor o igual que 30, el programa informa que "Ya no eres un joven".

Este tipo de código es útil en situaciones donde necesitas tomar decisiones basadas en rangos específicos de datos numéricos, como clasificar información demográfica por grupos etarios.

`005-entrada.py`

```python
print("Clasificador incómodo por edades")
edad = input("Introduce tu edad: ")         # Por defecto devuelve string
edad = int(edad)

if edad < 10:
  print("Eres un niño!")
elif edad >= 10 and edad < 20:
  print("Eres un adolescente")
elif edad >= 20 and edad < 30:
  print("Eres un joven")
else:
  print("Ya no eres un joven")
```

### simulacro de actividad
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código es un programa sencillo que clasifica a los pilotos de carreras basándose en la posición final en la que quedaron. El programa comienza pidiéndote que introduzcas tu posición en una carrera, y luego compara esta posición con diferentes rangos para determinar un mensaje específico.

El programa utiliza estructuras de control `if` y `elif` (que significa "else if" o "si no") para clasificar la posición del piloto. Si el piloto quedó en primera posición, se le felicita diciendo que es el campeón. Para las posiciones 2 y 3, el mensaje indica que ha subido al podio y hace un reconocimiento de su trabajo. Para los lugares entre el cuarto lugar y el décimo, el programa informa que el piloto ha conseguido puntos en el campeonato. Finalmente, si la posición es mayor o igual a la undécima, se le anima a seguir entrenando ya que no consiguió puntos.

La importancia de este código radica en cómo utiliza condiciones y comparaciones lógicas para clasificar información y proporcionar retroalimentación basada en una entrada del usuario. Esto es útil tanto para el aprendizaje de estructuras condicionales como para la creación de programas que toman decisiones basadas en entradas numéricas o categorías específicas.

`006-simulacro de actividad.py`

```python
'''
  Programa clasificador de pilotos
  (c) 2025 Jose Vicente Carratala
  Este programa clasifica a los pilotos de carreras
'''

# Importaciones: Este programa no necesita importaciones


# Variables  globales
posicion_final = ""
mensaje = ""

# Clases / funciones: este programa no necesita clases o funciones

## Método o función principal
# Introducción de datos
posicion_final = input("Introduce la posición en la que has quedado: ")
posicion_final = int(posicion_final) # Tengo que convertir la cadena a numero entero
# Realización de cálculos
if posicion_final == 1:
  mensaje = "¡Eres el campeón de la carrera!"
elif posicion_final == 2 or posicion_final == 3:
  mensaje = "Subes al podio, gran trabajo."
elif posicion_final >=4 and posicion_final <=10:
  mensaje = "Has puntuado en el campeonato."
elif posicion_final >=11:
  mensaje = "No conseguiste puntos esta vez, sigue entrenando."
  
# Impresión de respuestas
print(mensaje)
```

### Actividades propuestas

### Actividades Propuestas

#### 1. Clasificación por Edad Simples
**Descripción:** Diseña un programa que solicite al usuario su edad y clasifique si es niño, adolescente o adulto basándose en los criterios de edades presentes en el ejercicio `004-else if.py`. El objetivo es reforzar la comprensión del uso múltiple de estructuras condicionales.

#### 2. Mejora del Clasificador
**Descripción:** A partir del programa existente en `005-entrada.py`, modifica el clasificador para que además de "niño", "adolescente" y "joven", incluya nuevas categorías como "adulto mayor". Se espera que los estudiantes aprendan a manejar condiciones anidadas.

#### 3. Posición Final en Carrera
**Descripción:** Replica la lógica del programa presentado en `006-simulacro de actividad.py` pero cambia las clasificaciones y mensajes para una competencia deportiva diferente (por ejemplo, ciclismo). Esto ayudará a entender cómo se aplica el uso de condiciones en situaciones prácticas.

#### 4. Evaluación Académica
**Descripción:** Crea un programa que permita al usuario ingresar su calificación académica y muestre su nivel basándose en rangos de puntuación (ejemplo: excelente, bueno, regular). Se pretende enseñar la aplicación práctica del uso de `elif`.

#### 5. Comprobar Año Bisiesto
**Descripción:** Diseña un programa que solicite al usuario ingresar un año y determine si es bisiesto o no. Este ejercicio ayudará a los estudiantes a practicar el uso de condiciones complejas.

#### 6. Clasificación de Temperaturas
**Descripción:** Elabora un script que permita clasificar las temperaturas ingresadas por el usuario en categorías como frío, templado y calor, basándose en umbrales establecidos previamente. El objetivo es mejorar la comprensión del uso condicional con rangos de valores.

#### 7. Cálculo de Impuestos
**Descripción:** Desarrolla un programa que solicite al usuario su ingreso anual y calcule el monto del impuesto a pagar basándose en diferentes tarifas según el nivel del ingreso (por ejemplo, porcentajes progresivos). Se espera que los estudiantes aprendan la aplicación de múltiples condiciones para manejar escalas.

#### 8. Evaluación Final del Curso
**Descripción:** Crea un programa que solicite al usuario ingresar su calificación final en el curso y muestre si aprobó, reprobó o obtuvo matrícula con honores, basándose en rangos específicos de puntuaciones. Esto ayudará a los estudiantes a entender cómo se aplica la estructura condicional para realizar evaluaciones.

Estas actividades buscan refinar las habilidades básicas y avanzadas en el uso de estructuras condicionales (`if`, `elif`, `else`) a través de ejercicios prácticos que simulan situaciones reales.


<a id="estructuras-de-repeticion"></a>
## Estructuras de repetición

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/003-Uso%20de%20estructuras%20de%20control/002-Estructuras%20de%20repetici%C3%B3n)

### Introducción a los ejercicios

En esta carpeta, encontrarás una serie de ejercicios en Python diseñados para practicar el uso de estructuras de repetición, específicamente los bucles `for` y `while`. Los ejercicios comienzan con bucles simples que recorren un rango determinado de días del mes y avanzan hacia bucles anidados que permiten la iteración sobre múltiples años, meses y días. Estos ejercicios te ayudarán a entender cómo controlar el flujo del programa mediante estructuras repetitivas complejas, mejorando así tus habilidades en la programación orientada a la resolución de problemas diarios con bucles anidados y condicionales.

### for
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código muestra cómo utilizar un bucle `for` en Python para repetir una acción durante varios días. En este caso, el bucle se ejecuta desde el día 1 hasta el día 30 (no incluye al día 31). La función `range(1, 31)` genera una secuencia de números que van del 1 al 30. Dentro del bucle, la variable `dia` toma cada uno de estos valores en orden y se imprime un mensaje que indica qué día es del mes actual.

Este tipo de estructura es muy útil cuando necesitas realizar tareas repetitivas con una cantidad específica de iteraciones conocidas, como en este caso contar los días de un mes. Es importante entender cómo funcionan las secuencias `range` para poder crear rangos numéricos personalizados que se ajusten a nuestras necesidades específicas.

`001-for.py`

```python
for dia in range(1,31):
  print("Hoy es el dia",dia,"del mes")
```

### primera anidacion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código utiliza dos bucles anidados para imprimir la fecha en formato "día del mes" para cada día de un año. El bucle externo `for mes in range(1, 13):` recorre los meses del 1 al 12, es decir, desde enero hasta diciembre. Dentro de este bucle, hay otro bucle `for dia in range(1, 31):` que itera sobre los días del 1 al 30.

El bucle interno imprime la fecha actual en cada iteración, mostrando "Hoy es el día X del mes Y", donde X y Y son valores numéricos correspondientes al día y mes actuales en las respectivas variables `dia` e `mes`. 

Es importante notar que este código asume todos los meses tienen 31 días para simplificar la ilustración, lo cual no es correcto desde el punto de vista real (algunos meses tienen menos). Sin embargo, esta aproximación sirve bien como ejemplo didáctico de cómo anidar bucles en Python.

`002-primera anidacion.py`

```python
for mes in range(1,13):
  for dia in range(1,31):
    print("Hoy es el dia",dia,"del mes",mes)
```

### segunda anidacion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python muestra un ejemplo de cómo se utilizan las estructuras de repetición anidadas (uno dentro del otro) para recorrer fechas en un rango específico. En este caso, el programa imprime la fecha actual en formato "Hoy es el día [día] del mes [mes] del año [año]" para cada combinación de día, mes y año dentro de los rangos especificados.

El código empieza con un bucle `for` que recorre todos los años desde 1978 hasta 2025 (el límite superior no se incluye). Dentro del bucle anidado para el año, hay otro bucle `for` que va de enero a diciembre. Finalmente, dentro del bucle para el mes, hay un tercer bucle `for` que recorre los días desde 1 hasta 30. Esta estructura permite iterar sobre todas las posibles combinaciones de día, mes y año dentro del rango especificado.

Es importante notar que este código imprime fechas incluso cuando no son válidas (como el 31 de febrero), ya que no se ha implementado ninguna lógica para verificar la validez de cada fecha. Sin embargo, es útil como ejemplo didáctico sobre cómo funcionan los bucles anidados en Python.

`003-segunda anidacion.py`

```python
for anio in range(1978,2026):
  for mes in range(1,13):
    for dia in range(1,31):
      print("Hoy es el dia",dia,"del mes",mes,"del año",anio)
```

### while
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código utiliza un bucle `while` para imprimir una frase que indica el día actual del mes durante los primeros 30 días. El programa comienza estableciendo la variable `dia` en 1 y luego entra en el ciclo `while`, que se repetirá mientras `dia` sea menor a 31. En cada iteración, imprime en pantalla un mensaje que indica cuál es el día actual del mes (por ejemplo, "hoy es el dia 1 del mes"). Después de imprimir este mensaje, el valor de `dia` aumenta en uno, permitiendo que se siga cumpliendo la condición del bucle hasta llegar al día 30. Este tipo de estructura es útil cuando necesitas realizar una acción repetidamente hasta alcanzar un límite específico.

`004-while.py`

```python
dia = 1
while dia < 31:
  print("hoy es el dia",dia,"del mes")
```

### le tenemos que decir cual es el final
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código utiliza un bucle `while` para imprimir la frase "hoy es el día [número] del mes" desde el día 1 hasta el día 30. La variable `dia` inicialmente se establece en 1 y luego, dentro del bucle, se incrementa en 1 con cada iteración gracias a la línea `dia += 1`. El bucle continúa ejecutándose mientras `dia` sea menor que 31, lo que garantiza que imprima el número correcto de días. Esta estructura es útil para tareas que requieren un recorrido específico por una serie de números en orden secuencial, como contar los días del mes o realizar acciones diarias repetitivas.

`005-le tenemos que decir cual es el final.py`

```python
dia = 1
while dia < 31:
  print("hoy es el dia",dia,"del mes")
  dia += 1
```

### Actividades propuestas

### Actividad 1: Contar Días del Mes con un Bucle `for`
**Descripción:** Escribe una secuencia de comandos que imprima cada día del mes utilizando un bucle `for`. Este ejercicio te ayudará a entender cómo funciona la estructura de control `for` en Python y cómo iterar sobre una serie numérica.

### Actividad 2: Anidar Bucles para Representar Días y Meses
**Descripción:** Usa anidación de bucles para imprimir la fecha completa (día del mes) por cada día durante todo el año. Este ejercicio te permitirá entender cómo se pueden combinar múltiples estructuras de control para resolver problemas más complejos.

### Actividad 3: Anidar Bucles en Tres Niveles
**Descripción:** Escribir un programa que muestre las fechas completas (día, mes y año) por cada día del año. Este ejercicio profundiza el uso de bucles anidados para la representación temporal detallada.

### Actividad 4: Contar Días con Bucle `while`
**Descripción:** Usa un bucle `while` para contar los días de un mes dado. Esto te ayudará a entender cómo funciona la estructura condicional `while` y cómo se maneja el conteo manual.

### Actividad 5: Usando Condición `while` con Incremento Manual
**Descripción:** Escribe un programa que imprima los números del uno al treinta usando un bucle `while`. Este ejercicio muestra cómo controlar la finalización de un bucle en función de una condición y cómo incrementar el contador manualmente dentro del mismo.

### Actividad 6: Imprimir Números Pares con Bucle `for`
**Descripción:** Crea un programa que imprima los números pares desde el uno hasta el treinta. Aprenderás a usar condiciones en bucles para filtrar y mostrar solo ciertos tipos de valores (en este caso, números pares).

### Actividad 7: Contador Desendente con Bucle `while`
**Descripción:** Usa un bucle `while` para contar hacia atrás desde el treinta hasta el uno. Este ejercicio te enseñará a manejar contadores en desenso y a usar condiciones de finalización.

### Actividad 8: Anidar Bucles Para Imprimir Tabla del Número
**Descripción:** Escribe un programa que imprima la tabla de multiplicar de cualquier número dado hasta el quince. Utilizarás anidación de bucles para resolver este problema, lo cual te permitirá aprender cómo combinar estructuras en un solo código.

### Actividad 9: Contador Dinámico con Bucle `while`
**Descripción:** Crea un programa que cuente los días del mes pero permite al usuario introducir el número final. Esto te enseñará a integrar la entrada de datos y a manejar valores dinámicos dentro de estructuras condicionales.

### Actividad 10: Bucle `for` con Condición Interna
**Descripción:** Escribir un programa que use bucles `for` para imprimir solo los números impares del uno al treinta. Aprenderás a combinar bucles con condiciones internas para controlar la salida basada en criterios específicos.


<a id="estructuras-de-salto"></a>
## Estructuras de salto

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/003-Uso%20de%20estructuras%20de%20control/003-Estructuras%20de%20salto)

### Introducción a los ejercicios

Esta carpeta contiene una serie de ejercicios diseñados para introducir y practicar el uso de estructuras de control y funciones en Python. Los estudiantes aprenderán sobre la implementación del bucle `while` junto con la sentencia `break`, que permite salir anticipadamente de un ciclo cuando se cumple cierta condición, como finalizar la impresión de días una vez alcanzado el día 31. Además, los ejercicios abordan cómo definir y utilizar funciones en Python, desde su creación básica hasta pasar parámetros y devolver valores con la sentencia `return`. Estos ejercicios son fundamentales para desarrollar las habilidades necesarias para manejar flujos de control complejos y organizar el código en estructuras reutilizables.

### break
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código muestra cómo usar la estructura `break` en un bucle `while`. La función principal de este fragmento es imprimir los números del 1 al 31, que representan los días de un mes. 

El código comienza estableciendo una variable llamada `dia` a 1. Luego entra en un bucle infinito (`while True:`) que se ejecutará indefinidamente hasta que se cumpla la condición para salir del bucle con el comando `break`. Dentro del bucle, se imprime el número actual de día y luego incrementa este valor en 1. Si después de la suma, el valor de `dia` es mayor que 31, se ejecuta la instrucción `break`, lo cual hace que el programa salga inmediatamente del bucle.

Esta estructura es útil cuando necesitas detener un ciclo repetitivo prematuramente basado en una condición específica. En este caso, evita que el código imprima días "ficticios" más allá de los 31 días típicos de un mes.

`001-break.py`

```python
dia = 1
while True:
  print("hoy es el dia",dia,"del mes")
  dia += 1
  if dia > 31:
    break
```

### mi primera funcion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código define una función llamada `dihola` en Python. Una función es como un pequeño programa dentro de tu programa principal que realiza tareas específicas cuando se le llama. En este caso, la función `dihola` no recibe ningún dato de entrada y su tarea es imprimir el mensaje "Hola, yo te saludo" cada vez que se ejecuta.

La línea `def dihola():` indica que estamos definiendo una nueva función llamada `dihola`. Todo lo que está indentado después de esta línea (en este caso, la línea con `print`) es parte de esta función. Cuando en tu código llamas a esta función usando `dihola()`, el programa ejecuta el contenido de esa función, es decir, imprime "Hola, yo te saludo".

Es importante porque permite organizar el código en partes manejables y reutilizables, lo que facilita la escritura y lectura del código al descomponer tareas complejas en pasos más pequeños.

`002-mi primera funcion.py`

```python
def dihola():
  print("Hola, yo te saludo")
  
```

### ejecuto la funcion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código es muy sencillo y está diseñado para introducir el concepto de funciones en Python. En primer lugar, se define una función llamada `diHola` que, cuando se ejecuta, imprime un mensaje "Hola, yo te saludo" en la pantalla. La definición de la función comienza con la palabra clave `def`, seguida del nombre de la función y paréntesis vacíos, ya que esta función no necesita recibir ningún dato adicional (también conocidos como argumentos o parámetros). Después de esto, se coloca un bloque de código indentado dentro del cual está el comando `print()` que imprime el saludo en la consola.

Después de definir la función, el código llama a esta función con el nombre seguido de paréntesis vacíos (`diHola()`). Esto ejecuta todas las instrucciones que están dentro de la función `diHola`, lo que significa que se imprime el mensaje "Hola, yo te saludo". Es importante porque muestra cómo podemos reutilizar un bloque de código específico en diferentes partes del programa simplemente llamando a su nombre, lo cual mejora la organización y legibilidad del código.

`003-ejecuto la funcion.py`

```python
def diHola():
  print("Hola, yo te saludo")
  
diHola()
```

### parametros
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una función llamada `diHola` que toma un parámetro llamado `nombre`. La función imprime en la pantalla un mensaje de saludo que incluye el nombre proporcionado como argumento. Por ejemplo, si se llama a `diHola("Jose Vicente")`, el programa imprimirá "Hola, Jose Vicente yo te saludo". De manera similar, al llamar a `diHola("Juan")`, se imprime "Hola, Juan yo te saludo".

El uso de funciones en Python es importante porque permite organizar y reutilizar código de una manera clara y eficiente. En este caso, la función `diHola` encapsula el comportamiento específico de saludar a alguien usando su nombre, lo que hace que sea fácil llamarla con diferentes nombres sin tener que escribir todo el código nuevamente para cada persona.

`004-parametros.py`

```python
def diHola(nombre):
  print("Hola,",nombre," yo te saludo")
  
diHola("Jose Vicente")
diHola("Juan")
```

### varios parametros
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código muestra cómo definir e invocar una función en Python. La función se llama `diHola` y tiene dos parámetros: `nombre` y `edad`. Dentro de la función, el programa imprime un saludo personalizado que incluye el nombre proporcionado y la edad del usuario.

La función es llamada dos veces con diferentes argumentos: primero con "Jose Vicente" como nombre y 47 como edad, y luego con "Juan" como nombre y 48 como edad. Esto significa que cada vez que se llama a la función `diHola` con estos datos, el programa imprime un saludo personalizado según los valores pasados.

Este tipo de estructura es importante porque permite reutilizar código de manera eficiente y organizar el programa en partes más manejables, facilitando así la modificación y mantenimiento del mismo.

`005-varios parametros.py`

```python
def diHola(nombre,edad):
  print("Hola,",nombre,"tienes",edad,"años y yo te saludo")
  
diHola("Jose Vicente",47)
diHola("Juan",48)
```

### las funciones deben retornar
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra cómo funciona una función en Python que devuelve un mensaje personalizado. La función se llama `diHola` y necesita dos piezas de información para funcionar: el nombre de la persona y su edad. Cuando llamas a esta función, le das estos detalles y ella te responde con un saludo amigable que incluye tanto el nombre como la edad.

En este caso, después de definir la función, se utilizan dos llamadas distintas a `diHola`. La primera vez, le decimos al programa que use "Jose Vicente" como nombre y 47 como edad. La segunda vez, usa "Juan" como nombre y 48 como edad. Ambas veces, el resultado de la función se imprime en pantalla con un saludo específico para cada persona.

Es importante entender cómo las funciones pueden tomar datos, procesarlos, y luego devolver una respuesta útil. En este ejemplo, `diHola` toma los parámetros (nombre y edad), construye un mensaje personalizado que incluye estos detalles, y luego lo devuelve al lugar donde fue llamada para que se pueda usar o mostrar el resultado.

`006-las funciones deben retornar.py`

```python
def diHola(nombre,edad):
  return "Hola, "+nombre+" tienes "+str(edad)+" años y yo te saludo"
  
print(diHola("Jose Vicente",47))
print((diHola("Juan",48)))
```

### Actividades propuestas

### Actividad 1: Uso de la instrucción `break`
**Descripción:** Implementa un programa que imprima los números del 1 al 50, pero cuando llegues al número 30, usa la instrucción `break` para terminar el ciclo. El objetivo es entender cómo detener un bucle antes de completarlo.

### Actividad 2: Definición y uso de funciones sin parámetros
**Descripción:** Crea una función en Python que se llame `saludar()` y dentro imprima "¡Hola, buen día!". Luego, ejecuta la función para ver el resultado. Esta actividad te ayudará a entender cómo definir y usar funciones básicas.

### Actividad 3: Definición de funciones con parámetros
**Descripción:** Escribe una función llamada `saludar_usuario()` que acepte un nombre como parámetro e imprima un saludo personalizado. Ejecuta esta función varias veces con diferentes nombres para ver cómo funcionan los parámetros.

### Actividad 4: Uso de múltiples parámetros en funciones
**Descripción:** Define una función `informar_usuario()` que tome dos argumentos, el nombre y la edad del usuario, e imprima un mensaje que incluya ambos datos. Ejecuta esta función con al menos tres parejas diferentes de nombres y edades para practicar.

### Actividad 5: Funciones con retorno
**Descripción:** Crea una función `mensaje_saludo()` que reciba dos parámetros, el nombre y la edad del usuario, y retorne un mensaje formado por estos datos. Luego, utiliza la función dentro de un bloque `print()` para mostrar el resultado en pantalla.

### Actividad 6: Juego con condiciones
**Descripción:** Diseña un programa que permita al usuario ingresar su edad. Si la edad es menor a 18 años, imprime "Eres menor de edad". De lo contrario, si es mayor o igual a 18, imprime "Eres mayor de edad". Utiliza una estructura condicional para controlar el flujo del programa.

### Actividad 7: Contador de días
**Descripción:** Escribe un bucle que cuente hasta 365 simulando los días del año. Usa la instrucción `break` para finalizar el conteo cuando llegues al día número 200, imprimiendo un mensaje indicativo.

### Actividad 8: Juego de adivinanza
**Descripción:** Crea un juego simple que genere un número aleatorio entre 1 y 50. Luego pide al usuario que adivine el número. Utiliza una estructura de control condicional para verificar si la respuesta es correcta e indica cuántos intentos ha hecho antes de acertar.

### Actividad 9: Suma con bucles
**Descripción:** Implementa un programa que sume los primeros 50 números naturales (1+2+3...+50) utilizando un bucle `for`. Utiliza una variable para acumular la suma total y finalmente imprime el resultado.

### Actividad 10: Tabla de multiplicar
**Descripción:** Crea una función que genere una tabla de multiplicar para cualquier número dado. La función debe imprimir los resultados de multiplicar este número por cada número del 1 al 10. Ejecuta la función con varios números para probar su funcionalidad.


<a id="control-de-excepciones"></a>
## Control de excepciones

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/003-Uso%20de%20estructuras%20de%20control/004-Control%20de%20excepciones)

### Introducción a los ejercicios

En esta carpeta, trabajaremos con ejercicios básicos de manejo de excepciones en Python. Los archivos proporcionan una introducción a cómo los programas pueden lidiar con errores durante la ejecución, como dividir entre cero, utilizando bloques `try` y `except`. A través de estos ejemplos, aprenderás a identificar situaciones problemáticas y a implementar estrategias para garantizar que tu programa no se interrumpa bruscamente en caso de errores.

### dvision legal
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código es muy simple y ejecuta una única operación matemática. Imprime el resultado de la división entre 4 y 3. El resultado que se muestra en pantalla será aproximadamente 1.3333, ya que 4 dividido por 3 no es un número entero sino un decimal.

Esta línea de código demuestra cómo Python puede realizar cálculos aritméticos básicos y mostrar el resultado directamente en la consola o terminal donde se ejecuta el programa. Es importante notar que esta operación no tiene errores ni excepciones, ya que los dos números son válidos para una división sin problemas.

Este tipo de código básico es útil para entender las operaciones matemáticas fundamentales en Python y cómo imprimir resultados en la consola, lo cual es un paso inicial antes de pasar a estructuras más complejas como bucles o condicionales.

`001-dvision legal.py`

```python
print(4/3)
```

### division por cero
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código intenta realizar una operación matemática muy especial y problemática: dividir un número por cero. Cuando se ejecuta la línea `print(4/0)`, Python generará un error porque no es posible dividir cualquier número entre cero en matemáticas. Este error paraliza el programa y hace que deje de funcionar inmediatamente.

A pesar del error, después de intentar la división por cero, el código imprime "Bueno pero por lo menos el programa continua". Esto es solo para mostrar que aunque se ejecuta esa línea con un error, otras líneas de código pueden seguir siendo procesadas si están escritas después en el archivo. Sin embargo, en este caso específico, el intento de dividir por cero causará la interrupción del programa y no permitirá imprimir ese mensaje.

Es importante aprender a manejar estos errores en programación para asegurar que tus programas puedan seguir funcionando incluso cuando ocurren situaciones inesperadas.

`002-division por cero.py`

```python
print(4/0)

print("Bueno pero por lo menos el programa continua")
```

### try
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra cómo manejar errores en Python usando una estructura llamada `try-except`. La idea principal es que cuando se intenta realizar una operación que no puede ser ejecutada (en este caso, dividir un número entre cero), el programa no se detiene sino que entra al bloque `except` y muestra un mensaje de error personalizado. Aquí, la línea `print(4/0)` provocaría un error porque no es posible dividir por cero matemáticamente. Sin embargo, gracias a la estructura `try-except`, el programa sigue funcionando después de este fallo, imprimiendo el mensaje "Hay un error pero por lo menos continuo con el programa". Luego del bloque `except`, el código continúa normalmente y se imprime "Bueno pero por lo menos el programa continua", demostrando que aunque hubo un problema, gracias a la gestión de errores, el programa sigue en ejecución.

`003-try.py`

```python
try:
  print(4/0)
except:
  print("Hay un error pero por lo menos continuo con el programa")

print("Bueno pero por lo menos el programa continua")
```

### Actividades propuestas

### Actividad 1: Manejo de Excepciones Básicas

**Descripción:** 
Los estudiantes deben identificar y capturar la excepción que se produce cuando intentan dividir un número entre cero. Se espera que implementen una estructura `try-except` para manejar este error y continuar con el resto del código.

### Actividad 2: Mejora de Mensajes de Error

**Descripción:** 
Los estudiantes deben mejorar la legibilidad del programa capturando excepciones específicas (como `ZeroDivisionError`) en lugar de usar una excepción general. Además, deben imprimir un mensaje personalizado cuando se produzca esta excepción.

### Actividad 3: Manejo de Múltiples Excepciones

**Descripción:** 
Los estudiantes deben modificar el código para capturar y manejar diferentes tipos de excepciones (por ejemplo, `ZeroDivisionError`, `TypeError`). Deben proporcionar mensajes claros para cada tipo de error que puedan ocurrir.

### Actividad 4: Bloque Else en Manejo de Excepciones

**Descripción:** 
Los estudiantes deben añadir un bloque `else` a la estructura `try-except`. Este bloque debería ejecutarse solo si no se produce ninguna excepción durante el intento de división. Se espera que proporcionen una salida adicional para indicar que todo ha ido bien.

### Actividad 5: Bloque Finally en Manejo de Excepciones

**Descripción:** 
Los estudiantes deben agregar un bloque `finally` a la estructura `try-except`. Este bloque debería ejecutarse siempre, independientemente de si se produjeron excepciones o no. Los estudiantes deberán describir qué tipo de operaciones son adecuadas para colocar en este bloque.

### Actividad 6: Trabajando con Múltiples Try-Except

**Descripción:** 
Los estudiantes deben escribir un código que incluya múltiples bloques `try-except` para manejar diferentes tipos de errores. Cada bloque debería estar diseñado específicamente para capturar y manejar una excepción diferente.

### Actividad 7: Uso del As en Manejo de Excepciones

**Descripción:** 
Los estudiantes deben introducir la palabra clave `as` dentro de sus bloques `try-except`. Esto les permitirá acceder a los detalles de las excepciones capturadas y mostrarlos en mensajes personalizados.

### Actividad 8: Implementación de un Menú de Opciones

**Descripción:** 
Los estudiantes deben crear un programa que presenta al usuario opciones para realizar diferentes operaciones matemáticas. Las opciones incluirán división, multiplicación y suma. Cada opción debe manejar sus propias excepciones específicas.

### Actividad 9: Documentación del Manejo de Excepciones

**Descripción:** 
Los estudiantes deben escribir comentarios en el código que expliquen por qué ciertas partes están dentro de bloques `try-except` y cómo estas estructuras ayudan a mejorar la robustez del programa.


<a id="aserciones"></a>
## Aserciones

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/003-Uso%20de%20estructuras%20de%20control/005-Aserciones)

### Introducción a los ejercicios

En esta carpeta de ejercicios, centraremos nuestra atención en la utilización y comprensión de las aserciones en Python. Las aserciones son una herramienta útil para verificar condiciones que deben cumplirse durante la ejecución del programa; si dichas condiciones no se cumplen, el programa genera un error inmediatamente. A través de estos ejercicios, los estudiantes practicarán cómo incorporar aserciones en su código para mejorar la robustez y legibilidad de sus programas, así como aprender a identificar y corregir errores que podrían pasar desapercibidos con solo pruebas básicas.

### asercion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código utiliza una estructura llamada `assert`, que es útil para comprobar si ciertas condiciones son verdaderas en el desarrollo de programas. En este caso, la condición a verificar es si el número 3 es igual al número 3, lo cual obviamente siempre será verdad.

La parte después de la coma ("hay un error") es el mensaje que se mostrará si la afirmación (assert) no se cumple. Si cambiamos la comparación por algo falso, como `assert 3 == 2`, entonces veríamos el mensaje "hay un error" en pantalla, lo que nos ayudaría a identificar rápidamente algún problema en nuestro código.

Esta estructura es muy útil para los desarrolladores durante la fase de pruebas y depuración del software, ya que permite asegurar que ciertos valores o situaciones ocurren como se esperaba.

`001-asercion.py`

```python
assert 3 == 3, "hay un error"
```

### si que hay un error
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código utiliza la palabra clave `assert` en Python para verificar si una condición es verdadera. En este caso, el programa comprueba si el número 3 es igual al número 2, lo cual obviamente no es cierto. Si la condición evaluada por `assert` es falsa, el programa genera un error con el mensaje "hay un error". Las afirmaciones (`assert`) son útiles para comprobar condiciones que deben ser verdaderas durante la ejecución del código y ayudan a identificar problemas rápidamente durante el desarrollo. En este ejemplo, si alguien está depurando el código o revisándolo, inmediatamente sabrá que algo va mal cuando se lance este error específico.

`002-si que hay un error.py`

```python
assert 3 == 2, "hay un error"
```

### Actividades propuestas

### Actividad 1: Entendiendo Aserciones Simples
**Descripción:** Implementa aserciones para comprobar condiciones básicas en tu código. Aprende a utilizar aserciones de manera efectiva para garantizar la correcta ejecución del programa.

### Actividad 2: Identificar Errores con Aserciones
**Descripción:** Analiza el uso incorrecto de las aserciones y modifica los ejemplos proporcionados para corregir errores lógicos. Aprende a detectar y solucionar problemas en tu código mediante aserciones.

### Actividad 3: Aserciones Condicionales
**Descripción:** Crea una función que utilice aserciones condicionales basadas en variables de entrada. Obtiene experiencia en cómo usar aserciones para validar condiciones cambiantes durante la ejecución del programa.

### Actividad 4: Uso de Aserciones con Listas
**Descripción:** Implementa aserciones para comprobar las propiedades de listas, como su longitud o contenido. Aprende a asegurar que tus estructuras de datos cumplen con los requisitos esperados antes de proceder en el código.

### Actividad 5: Aserciones y Manejo de Excepciones
**Descripción:** Combina aserciones con bloques try-except para mejorar la robustez del programa. Aprende a manejar errores lógicos y excepciones de manera coordinada.

### Actividad 6: Automatización de Pruebas con Aserciones
**Descripción:** Escribe un script que automatice pruebas utilizando aserciones, generando reportes para cada caso de prueba. Mejora tu habilidad en la escritura de código eficiente y mantenible.

### Actividad 7: Uso de Aserciones para Validar Inputs del Usuario
**Descripción:** Implementa un programa que solicite datos al usuario y utilice aserciones para validar dichos datos antes de continuar con el procesamiento. Mejora tus habilidades en la interacción entre el código y el usuario final.

### Actividad 8: Uso de Aserciones para Validar Rangos
**Descripción:** Diseña un programa que use aserciones para verificar si una variable está dentro de un rango específico. Aprende a asegurar que tus variables respeten los límites necesarios durante la ejecución.

### Actividad 9: Uso de Aserciones en Clases y Métodos
**Descripción:** Incluye aserciones en la definición de métodos de una clase para garantizar las condiciones iniciales antes del procesamiento. Mejora tus habilidades en el desarrollo orientado a objetos.

### Actividad 10: Documentación de Aserciones
**Descripción:** Escribe documentación clara y concisa que explique cada aserción utilizada en tu código, incluyendo por qué se usó y cómo afecta la lógica del programa. Aprende a mejorar la legibilidad y mantenimiento de tus programas mediante la documentación adecuada.


<a id="prueba-depuracion-y-documentacion-de-la-aplicacion"></a>
## Prueba, depuración y documentación de la aplicación

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/003-Uso%20de%20estructuras%20de%20control/006-Prueba%2C%20depuraci%C3%B3n%20y%20documentaci%C3%B3n%20de%20la%20aplicaci%C3%B3n)

### Introducción a los ejercicios

Este conjunto de ejercicios en Python se enfoca en la creación, prueba y depuración de una función que realiza divisiones entre dos números. Los estudiantes aprenderán a manejar excepciones para evitar errores como divisiones por cero o tipos no numéricos, y también a documentar adecuadamente sus funciones. A través de estos ejercicios, se practican competencias esenciales en programación como la resiliencia del código frente a situaciones inesperadas y la capacidad de verificar el correcto funcionamiento de las aplicaciones mediante pruebas exhaustivas.

### division
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una función en Python llamada `creaDivision` que toma dos parámetros: `dividendo` y `divisor`. La función calcula el resultado de la división entre estos dos números y retorna este valor. Luego, se llama a esta función con los valores 4 y 3 como argumentos para dividir 4 por 3, y se imprime el resultado en pantalla.

Esta pequeña pieza de código es útil porque demuestra cómo definir funciones sencillas que realizan operaciones matemáticas básicas y luego cómo utilizarlas. Es una buena introducción al concepto de modularización en programación, donde puedes empaquetar un trozo de lógica específica dentro de una función para reutilizarla fácilmente con diferentes valores.

`001-division.py`

```python
def creaDivision(dividendo,divisor):
  return dividendo/divisor;
  
print(creaDivision(4,3))
```

### prueba de carga
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código está diseñado para probar una función llamada `creaDivision`, que realiza divisiones matemáticas simples entre dos números. La función toma dos parámetros: el dividendo y el divisor, y devuelve el resultado de la división.

El código principal utiliza un bloque `try` para intentar ejecutar un bucle anidado que itera sobre una gama de valores desde -100 hasta 99 tanto para el dividendo como para el divisor. Durante cada iteración, se llama a la función `creaDivision` con los valores actuales del dividendo y el divisor, y luego imprime el resultado.

El bloque `except` captura cualquier error que pueda ocurrir durante la ejecución del bucle, como una división por cero. Si ocurre un error, se imprime "No ha aguantado", indicando que el programa no pudo completar su tarea sin errores.

Este tipo de prueba es importante para asegurar que las funciones en tu código manejen correctamente diferentes situaciones y valores, especialmente los casos límite como divisiones por cero.

`002-prueba de carga.py`

```python
def creaDivision(dividendo,divisor):
  return dividendo/divisor;
  
try:
  for divid in range(-100,100):
    for divis in range(-100,100):
      print(creaDivision(divid,divis))
except:
  print("No ha aguantado")
```

### correccion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python define una función llamada `creaDivision` que recibe dos parámetros: `dividendo` y `divisor`. La función calcula el resultado de dividir el dividendo entre el divisor. Si el divisor no es cero, la función devuelve el cociente; si el divisor es cero, la función retorna la cadena "infinidad", ya que matemáticamente no se puede dividir por cero y esto produciría un error en el programa.

Después de definir la función, el código utiliza un bucle `for` anidado para probar la función `creaDivision` con una gran cantidad de pares de números (dividendos y divisores) que van desde -100 hasta 99. Si durante este proceso no ocurre ningún error (como intentar dividir por cero), el programa imprimirá "Ha pasado la prueba". Sin embargo, si se produce algún tipo de excepción o error, el código captura ese problema con una estructura `try-except` y muestra en pantalla "No ha aguantado", indicando que hubo un fallo durante las pruebas.

Este fragmento es útil para aprender sobre manejo de errores, especialmente cuando se trabaja con operaciones matemáticas como la división que pueden generar excepciones si no se controlan adecuadamente.

`003-correccion.py`

```python
def creaDivision(dividendo,divisor):
  if divisor != 0:
    return dividendo/divisor;
  else:
    return "infinidad"
  
try:
  for divid in range(-100,100):
    for divis in range(-100,100):
      print(creaDivision(divid,divis))
  print("Ha pasado la prueba")
except:
  print("No ha aguantado")
```

### mas pruebas
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una función en Python llamada `creaDivision` que toma dos parámetros: `dividendo` y `divisor`. La función intenta convertir estos parámetros a números flotantes para realizar la división. Si el divisor es diferente de cero, la función devuelve el resultado de la división entre los dos valores. Sin embargo, si el divisor es cero, en lugar de generar un error, retorna una cadena que dice "infinidad", lo cual indica matemáticamente que dividir por cero no está definido y se puede interpretar como infinito.

Además, si durante la conversión a números flotantes o en cualquier otro momento ocurre algún tipo de error (por ejemplo, si `dividendo` es una cadena que no representa un número válido), el código captura ese error usando la estructura `try-except`, y devuelve simplemente 0.

La línea final del código muestra cómo se llama a esta función pasándole como argumentos el número 4 y la letra "a". Esto debería lanzar un error al intentar convertir "a" en un número, pero debido a la estructura de manejo de excepciones, la función simplemente retornará 0. Este código es importante para entender cómo Python maneja errores y cómo se pueden proteger las funciones contra valores inesperados o incorrectos.

`004-mas pruebas.py`

```python
def creaDivision(dividendo,divisor):
  try:
    dividendo = float(dividendo)
    divisor = float(divisor)
    if divisor != 0:
      return dividendo/divisor;
    else:
      return "infinidad"
  except:
    return 0
  
  
print(creaDivision(4,"a"))
```

### documentacion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una función llamada `creaDivision` en Python que realiza la operación de división entre dos números. La función toma dos parámetros: el dividendo y el divisor. Primero, intenta convertir ambos valores a floats para asegurarse de que sean numéricos. Luego verifica si el divisor es diferente de cero; si lo es, realiza la división y devuelve el resultado como un número. Si el divisor es cero, en lugar del resultado de la división devuelve la cadena "infinidad", ya que matemáticamente no se puede dividir por cero. En caso de que ocurra algún error durante la conversión a float o la operación, captura la excepción y devuelve 0.

Es importante este tipo de validaciones para prevenir errores en el programa cuando los valores ingresados no sean numéricos o cuando intente realizar una división por cero. Esto hace que la aplicación sea más robusta y manejable.

`005-documentacion.py`

```python
def creaDivision(dividendo,divisor):
  '''
    Esta función realiza una división
    Entradas: el divisor y el dividendo
    Salidas: El resultado como número
    Notas: La función realiza validación de número e infinidad
  '''
  try:
    dividendo = float(dividendo)
    divisor = float(divisor)
    if divisor != 0:
      return dividendo/divisor;
    else:
      return "infinidad"
  except:
    return 0
  
  
print(creaDivision(4,"a"))
```

### llamada a la funcion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código está haciendo una llamada a una función llamada `creaDivision` que se encuentra en un archivo externo denominado `funciondividir.py`. La función `creaDivision` recibe dos parámetros: el dividendo (4) y el divisor (3). El programa imprime el resultado devuelto por la función `creaDivision`.

Lo importante aquí es entender que este código no contiene toda la lógica, sino que se limita a llamar a una función definida en otro archivo. Esto demuestra cómo puedes organizar tu código en diferentes archivos y utilizar funciones de otros módulos para mantener el código limpio y modular.

Esta práctica es crucial cuando trabajas en proyectos más grandes o colaboras con otros programadores, ya que permite dividir la tarea en partes manejables y reutilizar piezas de código en distintos lugares del programa.

`006-llamada a la funcion.py`

```python
from funciondividir import creaDivision

print(creaDivision(4,3))
```

### funciondividir
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una función en Python llamada `creaDivision` que realiza la operación matemática de división entre dos números dados. La función toma dos parámetros: el dividendo y el divisor, que son los números que se van a dividir.

Dentro de la función, primero intenta convertir ambos parámetros en números decimales utilizando un bloque `try`. Esto es importante porque asegura que las operaciones matemáticas que siguen puedan realizarse correctamente. Si alguno de los valores no puede ser convertido en un número decimal (por ejemplo, si se proporciona una cadena de texto), el programa manejará esta situación mediante la línea `return 0`, lo cual indica que hubo algún error en la entrada.

Después de convertir ambos números, la función verifica si el divisor es diferente de cero. Si no es cero, realiza la división entre dividendo y divisor, devolviendo el resultado como un número decimal. Sin embargo, si el divisor es igual a cero (lo que matemáticamente significa una división por cero), en lugar de generar un error, la función devuelve la cadena "infinidad" para indicar esta situación especial.

Esta función es útil porque maneja cuidadosamente los posibles errores y situaciones especiales que podrían ocurrir durante la ejecución, lo cual ayuda a hacer el programa más robusto y fácil de usar.

`funciondividir.py`

```python
def creaDivision(dividendo,divisor):
  '''
    Esta función realiza una división
    Entradas: el divisor y el dividendo
    Salidas: El resultado como número
    Notas: La función realiza validación de número e infinidad
  '''
  try:
    dividendo = float(dividendo)
    divisor = float(divisor)
    if divisor != 0:
      return dividendo/divisor;
    else:
      return "infinidad"
  except:
    return 0
```

### Actividades propuestas

### Actividades para Estudiantes de Formación Profesional (FP)

#### Actividad 1: Mejora la Función División
**Descripción:** Los estudiantes deben mejorar la función `creaDivision` en el archivo `division.py` para que maneje divisiones por cero y valores no numéricos. Se espera que los alumnos comprendan cómo usar bloques try-except y condiciones.

#### Actividad 2: Prueba Exhaustiva
**Descripción:** Los estudiantes deben diseñar pruebas exhaustivas para la función de división, cubriendo una amplia gama de casos de entrada (positivos, negativos, cero). El objetivo es que los alumnos entiendan la importancia de las pruebas unitarias y cómo realizarlas.

#### Actividad 3: Corrección de Errores
**Descripción:** Basándose en el archivo `correccion.py`, los estudiantes deben identificar y corregir errores potenciales en una función existente que realiza divisiones. Se espera que los alumnos comprendan la importancia de manejar excepciones para evitar interrupciones no deseadas.

#### Actividad 4: Manejo de Excepciones Mejorado
**Descripción:** Los estudiantes deben mejorar el manejo de excepciones en la función `creaDivision` del archivo `mas pruebas.py`. Se espera que los alumnos aprendan a capturar y tratar diferentes tipos de errores específicos (por ejemplo, conversiones incorrectas).

#### Actividad 5: Documentación de Código
**Descripción:** Los estudiantes deben documentar adecuadamente la función de división en el archivo `documentacion.py` utilizando comentarios claros y precisos. Se espera que los alumnos aprendan a escribir documentación útil para otros desarrolladores.

#### Actividad 6: Importando Funciones desde Otros Archivos
**Descripción:** Los estudiantes deben importar y utilizar la función de división definida en el archivo `funciondividir.py` dentro del archivo `llamada a la funcion.py`. Se espera que los alumnos comprendan cómo modularizar el código y trabajar con múltiples archivos.

#### Actividad 7: Pruebas Parametrizadas
**Descripción:** Los estudiantes deben implementar pruebas parametrizadas para la función de división en un archivo nuevo. Deben probar distintos casos utilizando diferentes parámetros (dividendos y divisores). Se espera que los alumnos aprendan a automatizar pruebas con diversas entradas.

#### Actividad 8: Mejora del Manejo de Excepciones
**Descripción:** Basándose en `mas pruebas.py`, los estudiantes deben mejorar la función para proporcionar mensajes más descriptivos cuando se producen excepciones. Se espera que los alumnos aprendan a manejar excepciones de manera eficiente y útil.

Estas actividades están diseñadas para ayudar a los estudiantes a dominar las estructuras de control, manejo de errores y documentación en Python, habilidades esenciales para su futuro desarrollo profesional.


<a id="ejercicio"></a>
## Ejercicio

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/003-Uso%20de%20estructuras%20de%20control/007-Ejercicio)


<a id="ejercicio-de-final-de-unidad-2"></a>
## Ejercicio de final de unidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/003-Uso%20de%20estructuras%20de%20control/101-Ejercicio%20de%20final%20de%20unidad)

### Introducción a los ejercicios

En esta unidad, te enfocarás en consolidar tus habilidades con las estructuras de control fundamentales del lenguaje de programación que estés utilizando. El ejercicio principal en este conjunto se centra en aplicar bucles, condicionales y otras estrategias para resolver un problema práctico de manera eficiente. Practicarás la resolución de problemas complejos mediante la combinación y el uso correcto de estas estructuras, mejorando así tu capacidad para controlar el flujo del programa y tomar decisiones lógicas en código. Este ejercicio es ideal para estudiantes de Formación Profesional que buscan afianzar sus conocimientos previos antes de avanzar a temas más avanzados.

### Actividades propuestas

### Actividad 1: Análisis y Resolución de Problemas Básicos

**Descripción:** Los estudiantes deben analizar un problema proporcionado en el archivo y diseñar una solución utilizando estructuras de control como condicionales (if, else) y bucles (for, while). Se espera que los alumnos comprendan cómo aplicar estas estructuras para resolver problemas prácticos.

### Actividad 2: Comparación de Estructuras de Control

**Descripción:** Los estudiantes deben comparar el uso de diferentes estructuras de control en la resolución del mismo problema. La actividad busca que entiendan las ventajas y desventajas de usar if-else, switch-case o bucles para determinados tipos de problemas.

### Actividad 3: Mejora de Código Existente

**Descripción:** A partir del código existente proporcionado, los estudiantes deben identificar áreas de mejora y aplicar cambios para hacer el código más eficiente. Esto puede implicar la simplificación de condicionales o bucles anidados.

### Actividad 4: Implementación de Lógica Condicional Compleja

**Descripción:** Los alumnos se enfrentan a un problema que requiere el uso de estructuras condicionales complejas, incluyendo operadores lógicos y comparaciones múltiples. Se espera que diseñen algoritmos capaces de manejar diferentes casos y condiciones.

### Actividad 5: Bucle For vs Bucle While

**Descripción:** Los estudiantes deben implementar la misma funcionalidad usando tanto el bucle for como el while, con el objetivo de comparar su uso en contextos específicos. Se espera que reflexionen sobre cuándo es más apropiado usar cada tipo de estructura.

### Actividad 6: Estructuras Anidadas

**Descripción:** Los alumnos trabajan con problemas que requieren la anidación de bucles y condicionales para resolverlos correctamente. Esta actividad busca mejorar sus habilidades en la aplicación de estructuras de control complejas.

### Actividad 7: Optimización del Código

**Descripción:** Se les pide a los estudiantes que revisen el código proporcionado y encuentren formas de optimizarlo, minimizando las líneas de código y mejorando su eficiencia sin cambiar su funcionalidad básica.

### Actividad 8: Codificación Eficiente en Problemas Prácticos

**Descripción:** Los alumnos deben aplicar sus conocimientos sobre estructuras de control para resolver un problema práctico relevante a la vida real. Esto incluye el uso eficaz de condicionales y bucles según sea necesario.

Estas actividades están diseñadas para ayudar a los estudiantes a dominar las estructuras de control en programación, adaptándose al nivel y el contexto de sus estudios en Formación Profesional.



<a id="desarrollo-de-clases"></a>
# Desarrollo de clases

<a id="concepto-de-clase"></a>
## Concepto de clase

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/004-Desarrollo%20de%20clases/001-Concepto%20de%20clase)

### Introducción a los ejercicios

Este conjunto de ejercicios se enfoca en introducir y practicar el concepto de clases en programación, partiendo desde la codificación básica hasta su aplicación avanzada. Inicia con ejemplos de código sin reutilización y luego evoluciona hacia el uso de funciones y parámetros para encapsular y modularizar el código. Finalmente, introduce la creación de clases y objetos (en este caso, gatos) para demostrar cómo se pueden crear instancias personalizadas que encapsulan atributos específicos.

A través de estos ejercicios, los estudiantes adquieren competencias fundamentales como la reutilización del código, el uso efectivo de funciones con parámetros y argumentos, y la creación de clases para modelar objetos complejos. Se les enseña a pasar gradualmente desde prácticas no óptimas hasta una programación orientada a objetos más eficiente.

### codigo sin reutilizacion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python muestra un ejemplo muy básico y repetitivo de cómo se imprime información personal para diferentes personas. En este caso, el programa imprime saludos y detalles sobre tres individuos: Pepe, Juan y Jorge. Para cada persona, se realizan tres impresiones separadas que incluyen un saludo amistoso, una pregunta acerca de su estado actual y una notificación con la edad de esa persona.

Lo importante aquí es entender que este código está escrito sin ninguna reutilización del código, lo cual significa que si tuviéramos que agregar más personas o cambiar cualquier detalle sobre estas tres, tendríamos que modificar manualmente cada parte correspondiente. Esto no solo hace el programa difícil de mantener y actualizar, sino también propenso a errores debido a la repetición.

Este ejemplo ilustra por qué es importante aprender cómo encapsular comportamientos similares en funciones (que serán discutidas en ejercicios posteriores) para evitar la redundancia y mejorar la eficiencia del código.

`001-codigo sin reutilizacion.py`

```python
print("hola, pepe")
print("como estás")
print("que sepas que tienes 45 años")

print("hola, juan")
print("como estás")
print("que sepas que tienes 34 años")

print("hola, jorge")
print("como estás")
print("que sepas que tienes 56 años")
```

### funciones para encapsular
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python muestra cómo se define y utiliza una función llamada `saluda`. La función simplemente imprime tres mensajes en la pantalla: un saludo, una pregunta sobre el estado del usuario y una declaración acerca de su edad. Cuando llamas a esta función tres veces con los comandos `saluda()`, cada vez que se ejecuta muestra esos mismos tres mensajes.

Este tipo de estructura es importante porque permite reutilizar código en lugar de escribir las mismas líneas de código varias veces, lo cual hace el programa más limpio y fácil de mantener. Además, si en algún momento necesitas cambiar los mensajes, solo tendrás que hacerlo dentro de la función `saluda`, sin tener que modificar cada llamada individual a la función.

`002-funciones para encapsular.py`

```python
def saluda():
  print("hola, pepe")
  print("como estás")
  print("que sepas que tienes 45 años")

saluda()
saluda()
saluda()
```

### parametros de la funcion
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código está diseñado para explicar cómo funcionan las funciones en Python, específicamente con parámetros. La función se llama `saluda` y tiene dos parámetros: `nombre` y `edad`. Cuando la función es llamada (ejecutada), necesita que le proporcionen un nombre y una edad como argumentos para poder imprimir saludos personalizados.

Lo que hace la función es imprimir en pantalla tres mensajes. El primer mensaje incluye el nombre del usuario, mientras que el segundo es independiente de los parámetros dados. El tercer mensaje indica cuántos años tiene la persona proporcionando su edad, que es uno de los argumentos que se le pasan a la función.

Este tipo de código es importante porque muestra cómo reutilizar bloques de código para diferentes valores, lo cual es una parte fundamental del desarrollo de software y de las buenas prácticas en programación. En lugar de escribir el mismo bloque de código tres veces (una vez por cada persona), usamos la función `saluda` que puede ser llamada con cualquier nombre y edad que deseemos. Esto no solo hace que nuestro código sea más corto, sino también más fácil de mantener y actualizar si necesitamos cambiar cómo se muestra un saludo en el futuro.

`003-parametros de la funcion.py`

```python
def saluda(nombre,edad):
  print("hola, ",nombre)
  print("como estás")
  print("que sepas que tienes ",edad," años")

saluda("juan",54)
saluda("jorge",45)
saluda("jaime",67)
```

### clases
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra el inicio de la definición de una clase llamada `Gato` en Python. Una clase es como un plan o diseño para crear objetos, que son instancias concretas basadas en ese diseño. En este caso, la clase tiene un método especial llamado `__init__`, que se ejecuta automáticamente cuando creamos (o instanciamos) un nuevo objeto de tipo `Gato`.

El método `__init__` recibe un parámetro por defecto `self`, que es una referencia al propio objeto que estamos creando. Sin embargo, en el código proporcionado, la función no está asignando valores a las propiedades del gato (color, edad y raza) que se mencionan dentro de este método. Para que estas variables (`self.color`, `self.edad`, `self.raza`) sean útiles, deben inicializarse con algún valor específico cuando se crea un objeto de la clase `Gato`. Por ejemplo, podríamos permitir al usuario especificar el color, edad y raza del gato al crear una nueva instancia de la clase. Esto es importante porque sin esta inicialización, estas variables no tendrían ningún valor asignado y causarían un error en el código si intentáramos usarlas más adelante.

Es fundamental completar este método para que la clase `Gato` funcione correctamente y podamos crear objetos gato con características específicas.

`004-clases.py`

```python
class Gato:
  def __init__(self):
    self.color
    self.edad
    self.raza
    
```

### creo un primer gato
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código es una introducción al concepto de clases en Python, específicamente creando una clase llamada `Gato`. La clase define un constructor (`__init__`), que es un método especial que se ejecuta automáticamente cuando se crea una nueva instancia del objeto. En este caso, el constructor inicializa tres atributos vacíos: `color`, `edad`, y `raza`. Estos atributos representan características del gato como su color de pelo, cuántos años tiene, y qué raza pertenece.

Después de definir la clase, se crea una instancia llamada `gato1` utilizando el constructor de la clase `Gato()`. Al imprimir `gato1`, Python mostrará información sobre este objeto en particular, pero por defecto no es muy detallado y solo muestra algo como `<__main__.Gato object at 0x7f2c3d4a8b80>`, que indica la ubicación de memoria del objeto.

Es importante entender cómo se crean objetos basados en clases porque permite organizar el código de manera más estructurada, facilitando la reutilización y mantenimiento del mismo.

`005-creo un primer gato.py`

```python
class Gato:
  def __init__(self):
    self.color = ""
    self.edad = ""
    self.raza = ""
    
gato1 = Gato()
print(gato1)
```

### puedo crear los gatos que quiera
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código está creando una clase en Python llamada `Gato`. Una clase es como un modelo o plantilla que define las características y comportamientos de los objetos relacionados con ella. En este caso, la clase `Gato` tiene un método especial llamado `__init__`, que se ejecuta cada vez que creamos un nuevo objeto `Gato`.

En el método `__init__`, se inicializan tres atributos: `color`, `edad` y `raza`. Estos son características del gato que podrían variar de un gato a otro. Sin embargo, en este código, estos atributos no están recibiendo valores específicos cuando se crean los objetos, por lo que quedarán como cadenas vacías (`""`). 

Después de definir la clase `Gato`, el código crea dos instancias o objetos de esta clase: `gato1` y `gato2`. Luego imprime ambos objetos. En Python, al imprimir un objeto simplemente verás cómo está representado internamente, lo que incluye su tipo (en este caso, `<__main__.Gato object at ...>`) y una referencia a la ubicación en memoria del objeto.

Este código es importante porque muestra cómo se definen las clases y cómo se crean instancias de dichas clases. Sin embargo, para hacer que los objetos `gato1` y `gato2` sean realmente útiles, necesitarías proporcionarles valores específicos cuando son creados o después, por ejemplo, asignándoles un color, edad y raza adecuados a cada uno.

`006-puedo crear los gatos que quiera.py`

```python
class Gato:
  def __init__(self):
    self.color = ""
    self.edad = ""
    self.raza = ""
    
gato1 = Gato()
print(gato1)
    
gato2 = Gato()
print(gato2)
```

### Actividades propuestas

### Actividad 1: Creación de una Clase Sencilla

**Descripción:** Crea una clase simple en Python que represente a un estudiante. La clase debe tener atributos como nombre, edad y curso actual. Los estudiantes deben poder ser instanciados con estos datos.

---

### Actividad 2: Personalización del Constructor de Estudiantes

**Descripción:** Modifica la clase `Estudiante` creada en la actividad anterior para que el constructor tome los valores del nombre, la edad y el curso al momento de crear un objeto. Además, incluye un método que imprima estos datos.

---

### Actividad 3: Creación de Varios Estudiantes

**Descripción:** Crea varios objetos `Estudiante` usando diferentes datos proporcionados (nombre, edad y curso) y muestra en pantalla la información de cada estudiante al instanciarlos.

---

### Actividad 4: Añadir Métodos a la Clase Estudiante

**Descripción:** Agrega métodos dentro de la clase `Estudiante` que permitan cambiar el nombre y el curso del estudiante. Luego, prueba estos métodos modificando las propiedades de los estudiantes creados anteriormente.

---

### Actividad 5: Clase para Gestión de Notas

**Descripción:** Diseña una nueva clase llamada `Nota`, la cual debe tener atributos como materia y calificación. Implementa un método que permita asignar estas notas a cada estudiante creado en las actividades anteriores.

---

### Actividad 6: Clase para Gestión de Grupo de Estudiantes

**Descripción:** Crea una clase llamada `GrupoEstudiantes` que contenga objetos del tipo `Estudiante`. Implementa métodos que permitan agregar, eliminar y listar estudiantes del grupo.

---

### Actividad 7: Personalización de Atributos en la Clase Gato

**Descripción:** Tomando como base el archivo `005-creo un primer gato.py`, personaliza los atributos de los gatos para que puedan ser inicializados con valores específicos (color, edad y raza) al instanciarlos.

---

### Actividad 8: Creación de Múltiples Instancias de Gato

**Descripción:** Con la clase `Gato` personalizada en la actividad anterior, crea múltiples gatos con diferentes datos. Luego, imprime las características de cada uno para verificar que se han inicializado correctamente.

---

Estas actividades están diseñadas para ayudar a los estudiantes a familiarizarse gradualmente con el concepto de clases y objetos en Python, desde lo básico hasta la creación de clases más complejas que incluyen métodos y atributos personalizados.


<a id="estructura-y-miembros-de-una-clase-visibilidad"></a>
## Estructura y miembros de una clase. Visibilidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/004-Desarrollo%20de%20clases/002-Estructura%20y%20miembros%20de%20una%20clase.%20Visibilidad)

### Introducción a los ejercicios

Esta carpeta contiene ejercicios que te ayudarán a entender los fundamentos de cómo crear y manipular clases en Python, centrándote específicamente en los miembros de una clase (propiedades y métodos) y su visibilidad. En estos ejercicios, aprenderás a definir una clase con un constructor (`__init__`) para inicializar propiedades como el color, edad y raza del gato. Además, explorarás cómo los métodos permiten a las instancias de la clase realizar acciones, en este caso, maullar. También te enseñará sobre la visibilidad de estos miembros, mostrándote ejemplos donde algunas propiedades son públicas (accesibles desde fuera de la clase) y otras privadas (__color), protegidas del acceso directo externo para mantener una mejor estructura y encapsulamiento en tu código.

### miembros
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python define una clase llamada `Gato` que representa las características y acciones de un gato. La función especial `__init__()` es el constructor, lo que significa que se ejecuta automáticamente cuando se crea (o instanciar) un objeto de la clase `Gato`. En este constructor, se inicializan tres propiedades del gato: `color`, `edad` y `raza`, todas establecidas como cadenas vacías.

Además, la clase contiene un método llamado `maulla()`, que simplemente imprime "miau" en pantalla. Este método representa una acción típica de los gatos que puede ser invocada desde cualquier instancia de la clase `Gato`.

En el código, se crea una instancia del objeto `Gato` llamada `gato1`. Luego, se imprimen los detalles de este objeto (lo cual generalmente mostrará algo como `<__main__.Gato object at 0x7f8e4c52b6a0>` que no es muy informativo) y finalmente se llama al método `maulla()` para que el gato haga un sonido. Este ejemplo simple demuestra cómo definir una clase con propiedades e implementar métodos en Python, proporcionando una estructura clara para objetos más complejos en aplicaciones de programación.

`001-miembros.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = ""
    self.raza = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    print("miau")
    
gato1 = Gato()
print(gato1)
gato1.maulla()
```

### visibilidad de los miembros
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python crea una clase llamada `Gato` que simula las características y comportamiento básico de un gato. La clase tiene tres propiedades: `color`, `edad` y `raza`. Estas propiedades son públicas, lo que significa que puedes acceder a ellas desde fuera de la clase tanto para leer como para modificar sus valores.

Además, la clase incluye un método llamado `maulla()` que simplemente imprime el sonido "miau" en pantalla. En este ejemplo, se crea una instancia de la clase `Gato` denominada `gato1`, y luego se establece su propiedad `color` como "naranja". Finalmente, se imprime un mensaje que muestra el color del gato utilizando la propiedad modificada.

Este código es importante porque demuestra cómo crear clases en Python con propiedades públicas y métodos, así como cómo instanciar objetos a partir de estas clases y manipular sus atributos.

`002-visibilidad de los miembros.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = ""    # La visibilidad por defecto es pública
    self.raza = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    print("miau")
    
gato1 = Gato()
gato1.color = "naranja"          # Desde fuera puedo escribir la propiedad
print("El gato es de color",gato1.color)  # Desde fuera puedo leer la propiedad
```

### propiedad privada
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python define una clase llamada `Gato` que tiene propiedades como el color, edad y raza. La propiedad `__color` está marcada con dos guiones bajos al principio del nombre (`__color`), lo cual en Python indica que esta propiedad es privada (no visible desde fuera de la clase). Sin embargo, en este código se intenta cambiar el valor de `__color` directamente desde el exterior y también imprimirlo, lo que no debería ser posible si realmente fuera un atributo privado correctamente implementado.

Lo importante aquí es entender cómo Python trata los métodos y propiedades públicas y privadas: cuando una propiedad comienza con dos guiones bajos, normalmente se espera que su uso sea restringido dentro de la clase. Pero en este caso específico, el código ignora esta convención y aún así accede a `__color` directamente desde fuera de la clase.

Es esencial entender esto porque si hubieras implementado correctamente la propiedad como privada (por ejemplo, con métodos getter y setter), no podrías modificarla desde afuera. Esto ayuda a proteger el estado interno del objeto de modificaciones accidentales o malintencionadas.

`003-propiedad privada.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.__color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = ""    # La visibilidad por defecto es pública
    self.raza = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    print("miau")
    
gato1 = Gato()
gato1.__color = "naranja"          # Desde fuera puedo escribir la propiedad
print("El gato es de color",gato1.__color)  # Desde fuera puedo leer la propiedad
```

### Actividades propuestas

### Actividad 1: Crear una clase simple
**Descripción:** Diseña y crea una nueva clase en Python que modele un objeto "Perro". Debe tener al menos un método y tres atributos. La idea es que entiendas cómo estructurar una clase básica con propiedades y métodos.

### Actividad 2: Implementación de un constructor
**Descripción:** Modifica la clase del perro para incluir un constructor (__init__) que inicialice sus atributos. Esto te permitirá entender mejor cómo se manejan los objetos en Python desde su creación.

### Actividad 3: Añadir métodos a una clase
**Descripción:** Agrega al menos dos métodos diferentes a tu clase "Perro". Estos métodos deben representar acciones que un perro podría realizar. Esto te ayudará a entender cómo se define y utiliza la funcionalidad de una clase.

### Actividad 4: Modificar propiedades públicas
**Descripción:** Cambia el color del perro en tu código, demostrando cómo las propiedades públicas pueden modificarse desde fuera de la clase. Asegúrate de imprimir el nuevo valor para verificar que se ha cambiado correctamente.

### Actividad 5: Propiedades privadas y visibilidad
**Descripción:** Cambia uno de los atributos de tu clase "Perdo" a una propiedad privada (__color) y muestra cómo no puedes modificarla directamente desde fuera de la clase. Explica por qué es útil tener propiedades privadas.

### Actividad 6: Encapsulamiento básico
**Descripción:** Implementa métodos getter y setter para tu atributo privado "__color". Estos métodos permitirán leer y escribir el valor del color de manera controlada, mostrando cómo el encapsulamiento protege las propiedades internas.

### Actividad 7: Clase con herencia
**Descripción:** Crea una nueva clase "RazaPerro" que herede de la clase "Perdo". Añade nuevas características específicas a esta subclase para entender los conceptos básicos de la herencia en Python.

### Actividad 8: Ejecutar métodos desde objetos
**Descripción:** Crea varias instancias de tu clase principal y ejecuta diferentes métodos en cada instancia. Observa cómo las acciones se reflejan específicamente según las propiedades individuales de cada objeto.

### Actividad 9: Documentación con docstrings
**Descripción:** Añade docstrings a tus clases, métodos y funciones para mejorar la documentación del código. Esto te ayudará a entender cómo proporcionar información útil sobre los objetos y acciones en tu programa.

### Actividad 10: Refactorización de código
**Descripción:** Toma el código existente para la clase "Perro" y realiza mejoras como la eliminación de redundancias, mejora de estructura interna y simplificación del uso de métodos. Esto te ayudará a entender cómo mantener un código limpio y eficiente.


<a id="creacion-de-propiedades"></a>
## Creación de propiedades

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/004-Desarrollo%20de%20clases/003-Creaci%C3%B3n%20de%20propiedades)

### Introducción a los ejercicios

En esta carpeta, trabajaremos con ejercicios enfocados en la creación y manejo de propiedades dentro de clases utilizando Python. El archivo proporcionado muestra cómo definir una clase `Gato` con varias propiedades como color, edad, raza, nombre y color de ojos. Además, se incluye un método `maulla()` que ilustra cómo las instancias de la clase pueden realizar acciones específicas.

El objetivo principal es entender qué son las propiedades en programación orientada a objetos, su función dentro de una clase y cómo inicializarlas adecuadamente. A través de estos ejercicios, los estudiantes practicarán la creación de clases, el uso de constructores para inicializar propiedades y definir métodos que interactúan con estas propiedades.

### propiedades
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una clase en Python llamada `Gato`. Una clase es como un plano o diseño para crear objetos, y este caso específico se centra en las características de un gato. Dentro de la clase, hay un método especial llamado `__init__` que se llama automáticamente cada vez que se crea (o "instantiate" en inglés) una nueva instancia del objeto Gato. En esta función inicializadora, se definen varias propiedades del gato: color, edad, raza, nombre y color de ojos. Todas estas propiedades inician como cadenas vacías ("").

Además de las propiedades, hay un método llamado `maulla` que imprime "miau" en pantalla cada vez que se llama. Este método simula la acción que realiza el objeto Gato, es decir, emitir el sonido característico del gato.

Este tipo de definición de clases y métodos es fundamental en programación orientada a objetos porque permite encapsular información (las propiedades) y comportamiento (los métodos) relacionados dentro de un solo contenedor llamado clase.

`001-propiedades.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = ""    # La visibilidad por defecto es pública
    self.raza = ""
    self.nombre = ""
    self.color_ojos = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    print("miau")
    
```

### Actividades propuestas

### Actividad 1: Instanciación de Clases y Propiedades

**Descripción:** Crea un objeto `Gato` a partir de la clase proporcionada en el archivo. Llena las propiedades del gato con datos específicos (color, edad, raza, nombre y color de ojos). Esta actividad te ayudará a entender cómo se crean instancias de una clase y cómo se inicializan sus propiedades.

### Actividad 2: Agregar un Método

**Descripción:** Añade un nuevo método a la clase `Gato` que permita alimentar al gato. Este método debería modificar el estado del gato (por ejemplo, aumentando su energía). Esta actividad te ayudará a comprender cómo se pueden añadir métodos para manipular los atributos de una instancia.

### Actividad 3: Personalizar Constructor

**Descripción:** Modifica la clase `Gato` para que acepte parámetros en el constructor (`__init__`). Estos parámetros permitirán inicializar las propiedades del gato al crear un objeto. Esta actividad te permitirá entender cómo personalizar constructores y pasar argumentos a una clase durante su creación.

### Actividad 4: Getter y Setter

**Descripción:** Implementa métodos `get_nombre` y `set_nombre` en la clase `Gato`. Estos métodos permiten obtener el valor de la propiedad nombre (`get`) y establecer un nuevo valor para la misma (`set`). Esta actividad te ayudará a conocer cómo se gestionan los accesos a las propiedades de una clase.

### Actividad 5: Herencia Simples

**Descripción:** Crea una subclase `GatoSiberiano` que herede de la clase `Gato`. Añade un nuevo método específico para gatos siberianos. Esta actividad te permitirá comprender cómo funciona la herencia y cómo puedes especializar clases existentes.

### Actividad 6: Propiedades Privadas

**Descripción:** Modifica las propiedades del gato en la clase `Gato` para que sean privadas (prefijándolas con un guión bajo, `_`). Implementa métodos getter y setter para acceder a estas propiedades de forma controlada. Esta actividad te enseñará cómo ocultar los atributos internos de una clase.

### Actividad 7: Método Mágico `__str__`

**Descripción:** Añade un método especial llamado `__str__` en la clase `Gato`. Este método debe devolver una cadena que describa el objeto gato. Esta actividad te ayudará a comprender cómo se puede sobrescribir este método para mostrar información útil sobre los objetos.

### Actividad 8: Instanciar Multiples Gatos

**Descripción:** Crea un programa principal en Python donde instancies varios objetos de la clase `Gato`, cada uno con diferentes propiedades. Luego, utiliza estos gatos y llama a sus métodos para demostrar su funcionalidad. Esta actividad te permitirá practicar la creación de múltiples instancias y el uso de los métodos definidos en una clase.

### Actividad 9: Uso del Método `maulla`

**Descripción:** Implementa un programa que cree varios objetos de tipo gato e invoque al método `maulla` para cada uno. Esto permitirá a los estudiantes entender cómo se invocan métodos dentro de las instancias de una clase.

### Actividad 10: Modificar el Método `maulla`

**Descripción:** Añade un parámetro al método `maulla()` que indique la cantidad de veces que el gato debe maullar. Esto permitirá a los estudiantes aprender cómo modificar y extender las capacidades de los métodos existentes en una clase.


<a id="creacion-de-metodos"></a>
## Creación de métodos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/004-Desarrollo%20de%20clases/004-Creaci%C3%B3n%20de%20m%C3%A9todos)

### Introducción a los ejercicios

En esta carpeta, encontrarás ejercicios que te ayudarán a comprender y practicar la creación de métodos en Python. Estos ejemplos se centran en cómo implementar acciones dentro de una clase (métodos), como hacer que un objeto "gato" maulle o cambie su edad mediante funciones setter y getter. A través de estos ejercicios, podrás aprender a manipular las propiedades de los objetos de manera segura y controlada, lo cual es fundamental en el desarrollo orientado a objetos.

### metodo miau
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python crea una clase llamada `Gato` y muestra cómo definir tanto propiedades como métodos dentro de ella. La función `__init__` es lo que se conoce como el constructor de la clase; es un método especial que se llama automáticamente cuando creas una nueva instancia del objeto `Gato`. En este caso, inicializa las propiedades del gato como color, edad, raza, nombre y color de ojos, asignándoles cadenas vacías.

Además, la clase define un método llamado `maulla`, que simplemente imprime "miau" en pantalla cuando se llama. Al final, el código crea una instancia de la clase `Gato` llamada `gato1` y luego llama al método `maulla` sobre esta instancia para que el gato haga ruido.

Este ejemplo es útil porque demuestra cómo estructurar una clase con atributos (propiedades) y comportamientos (métodos), lo cual es fundamental en la programación orientada a objetos.

`001-metodo miau.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = ""    # La visibilidad por defecto es pública
    self.raza = ""
    self.nombre = ""
    self.color_ojos = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    print("miau")
    
gato1 = Gato()
gato1.maulla()
```

### funcion con return
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una clase en Python llamada `Gato`. Una clase es como un modelo o plantilla para crear objetos, y en este caso, está diseñado específicamente para representar características de un gato. La clase tiene un constructor (`__init__`), que es el método especial que se ejecuta automáticamente cada vez que se crea (o "instantiate" en inglés) un objeto `Gato`. En este constructor, se definen varias propiedades del gato como color, edad, raza, nombre y color de ojos, todas inicializadas con cadenas vacías (`""`).

Además del constructor, la clase tiene otro método llamado `maulla`, que simplemente retorna la cadena `"miau"`. Este método simula el sonido que hace un gato. Cuando se llama a este método en una instancia de la clase (como `gato1.maulla()`), devuelve la palabra "miau", lo cual es importante porque permite que los objetos creados con esta clase interactúen y realicen acciones que se esperarían de un gato, como maullar. Al final del código, se crea una instancia de la clase `Gato` llamada `gato1`, y luego se imprime el resultado de llamar al método `maulla()`, lo cual es "miau". Esto demuestra cómo los métodos dentro de una clase pueden ser utilizados para hacer que nuestros objetos realizan acciones específicas.

`002-funcion con return.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = ""    # La visibilidad por defecto es pública
    self.raza = ""
    self.nombre = ""
    self.color_ojos = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
    
gato1 = Gato()
print(gato1.maulla())
```

### setter
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una clase llamada `Gato` en Python, que representa a un gato con varias características como color, edad, raza, nombre y color de ojos. La función `__init__()` es el constructor de la clase, que se ejecuta automáticamente cuando se crea (o "instancia") un objeto del tipo `Gato`. En este constructor, inicializamos las propiedades del gato a valores vacíos o cero.

Además, la clase tiene dos métodos: `maulla()` y `setEdad()`. El método `maulla()` simplemente devuelve el sonido "miau" cuando se llama. Por otro lado, el método `setEdad(nuevaedad)` permite cambiar la edad del gato estableciendo un nuevo valor para la propiedad `edad`.

En la parte inferior del código, se crea una instancia de la clase `Gato` llamada `gato1`. Luego se imprime el sonido que hace el gato usando el método `maulla()`, y también se muestra su edad actual. Después, se cambia la edad del gato mediante dos formas diferentes: directamente asignando un nuevo valor a `gato1.edad` (lo cual no es recomendable porque no permite controlar cómo se realiza el cambio), y luego usando el método `setEdad(1)`, que es una forma más segura ya que puede añadir validaciones adicionales en el futuro si fuera necesario.

Este ejemplo ilustra cómo usar métodos para manipular los datos de un objeto de manera controlada, lo cual es importante para mantener la integridad del estado de tu programa.

`003-setter.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = 0    # La visibilidad por defecto es pública
    self.raza = ""
    self.nombre = ""
    self.color_ojos = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
  def setEdad(self,nuevaedad):
    self.edad = nuevaedad
    
gato1 = Gato()
print(gato1.maulla())
print("ahora mismo el gato tiene",gato1.edad,"años")
gato1.edad = 1    # Esto no se recomienda
gato1.setEdad(1)  # Esto es mucho más seguro
print("ahora mismo el gato tiene",gato1.edad,"años")
```

### seteando sin control
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python define una clase llamada `Gato` que representa las características y acciones de un gato. La clase incluye un constructor (`__init__`) donde se inicializan las propiedades del objeto, como el color, la edad, la raza, el nombre y los ojos del gato.

Además del constructor, hay un método llamado `maulla` que simplemente devuelve la cadena "miau", representando el sonido que hace un gato. También existe un método `setEdad` que permite establecer la edad del gato, pero con una condición: si la nueva edad es exactamente uno más que la edad actual, se cambia de manera segura; en caso contrario, imprime "operación no permitida".

El código posterior a la definición de la clase crea un objeto `gato1` de tipo `Gato`, muestra el sonido que hace y luego intenta cambiar su edad usando el método `setEdad`. Esto demuestra cómo se puede controlar y validar los cambios en las propiedades del objeto para mantener la integridad de los datos. Es importante destacar que este ejemplo tiene un mecanismo limitado para asegurar que sólo ciertos tipos de cambios (en este caso, incrementos de una unidad) sean permitidos, lo cual es útil para prevenir errores y garantizar que las propiedades del objeto estén en un estado válido siempre.

`004-seteando sin control.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = 0    # La visibilidad por defecto es pública
    self.raza = ""
    self.nombre = ""
    self.color_ojos = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1:
      self.edad = nuevaedad
    else:
      print("operación no permitida")
    
gato1 = Gato()
print(gato1.maulla())
print("ahora mismo el gato tiene",gato1.edad,"años")
gato1.setEdad(5)  # Esto es mucho más seguro
print("ahora mismo el gato tiene",gato1.edad,"años")
```

### control en el set
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una clase llamada `Gato` en Python, que simula las características de un gato real. La clase incluye un constructor (`__init__`) donde se inicializan varias propiedades del gato como su color, edad, raza, nombre y color de ojos. Además, la clase tiene dos métodos: `maulla()`, que devuelve el sonido "miau", y `setEdad(nuevaedad)`, que permite cambiar la edad del gato bajo ciertas condiciones.

El método `setEdad` es particularmente interesante porque incluye un control para asegurar que solo se pueda aumentar la edad en un año a la vez. Esto significa que si intentas establecer una nueva edad que no sea exactamente un año más grande que la edad actual, el programa imprimirá "operación no permitida" en lugar de cambiar la edad.

En las últimas líneas del código, se crea una instancia de `Gato` llamada `gato1`. Se imprime el sonido que hace y la edad inicial del gato (que es 0 según cómo está definida la clase). Luego, se intenta establecer la edad en 5 años usando el método `setEdad`, lo cual es permitido porque incrementa la edad en un solo año desde su estado inicial. Por último, vuelve a imprimir la nueva edad del gato.

Este ejemplo ilustra cómo los métodos pueden ser utilizados para controlar y manipular las propiedades de una clase de manera segura y lógica, asegurando que el objeto se mantenga en un estado consistente con reglas específicas.

`005-control en el set.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = 0    # La visibilidad por defecto es pública
    self.raza = ""
    self.nombre = ""
    self.color_ojos = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1:
      self.edad = nuevaedad
    else:
      print("operación no permitida")
    
gato1 = Gato()
print(gato1.maulla())
print("ahora mismo el gato tiene",gato1.edad,"años")
gato1.setEdad(5)  # Esto es mucho más seguro
print("ahora mismo el gato tiene",gato1.edad,"años")
```

### getter edad
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una clase llamada `Gato` en Python, que es un modelo de un objeto real. Dentro de esta clase, hay varias partes importantes:

- El método especial `__init__`, también conocido como constructor, se utiliza para inicializar las propiedades del gato (como color, edad, raza, nombre y color de ojos) cuando creamos una instancia del objeto `Gato`.

- Otros métodos incluyen `maulla()`, que simplemente devuelve el sonido "miau" cuando se llama.

- Los métodos `setEdad()` y `getEdad()` permiten establecer (asignar) y obtener la edad del gato, respectivamente. Estos métodos ayudan a controlar cómo se manipulan los datos dentro de la clase, proporcionando seguridad adicional al evitar que se cambien de forma incorrecta.

Finalmente, el código crea una instancia del objeto `Gato` llamada `gato1`, llama a algunos métodos y muestra en pantalla información sobre este gato, demostrando cómo funcionan los métodos para obtener la edad del gato y establecer su nueva edad. Esto es útil porque permite controlar cómo se modifican las propiedades del objeto de manera segura y coherente.

Este tipo de diseño orientado a objetos ayuda a organizar el código y protege los datos, lo cual es fundamental en programación avanzada.

`006-getter edad.py`

```python
class Gato:
  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = 0    # La visibilidad por defecto es pública
    self.raza = ""
    self.nombre = ""
    self.color_ojos = ""
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1:
      self.edad = nuevaedad
    else:
      print("operación no permitida")
  def getEdad(self):
    return self.edad
    
gato1 = Gato()
print(gato1.maulla())
print("ahora mismo el gato tiene",gato1.getEdad(),"años")
gato1.setEdad(5)  # Esto es mucho más seguro
print("ahora mismo el gato tiene",gato1.getEdad(),"años")
```

### Actividades propuestas

### Actividad 1: Creación de un método de acción básica

**Descripción:** Crea una clase `Perro` que incluya un método llamado `ladrar()` que imprima "guau". La actividad se centra en la creación y uso básico de métodos dentro de las clases.

### Actividad 2: Método con retorno

**Descripción:** Diseña un método `ladrar()` en tu clase `Perro` que retorne una cadena "guau" en lugar de imprimirlo directamente. El objetivo es aprender a utilizar funciones con retorno.

### Actividad 3: Creación y uso de setter

**Descripción:** Añade un método llamado `setColor()` a la clase `Perro`, permitiendo cambiar el color del perro (que se inicializa en vacío). Este ejercicio enseña cómo gestionar propiedades mediante métodos setters.

### Actividad 4: Implementación de getter y setter

**Descripción:** Añade un método `getColor()` a tu clase `Perro` que devuelva el color actual del perro. Luego, prueba ambos métodos (getter y setter) en el código principal para comprobar su funcionamiento.

### Actividad 5: Restricción de modificaciones con setters

**Descripción:** Implementa un método `setEdad()` similar al visto en los ejemplos pero que controle la edad permitida solo si la nueva es mayor que la actual. Este ejercicio refuerza el entendimiento de las validaciones dentro de métodos setters.

### Actividad 6: Métodos getter y setter avanzados

**Descripción:** Añade un método `getRaza()` y otro `setRaza(razanueva)` a tu clase `Perro`. Después, modifica su raza desde el código principal utilizando ambos métodos. Este ejercicio profundiza en la manipulación de atributos mediante getters y setters.

### Actividad 7: Crear una instancia y ejecutar métodos

**Descripción:** Crea varias instancias del objeto `Perro` con diferentes propiedades iniciales, luego utiliza los métodos getter y setter para modificarlas. Este ejercicio combina la creación de clases y objetos con el uso de métodos.

### Actividad 8: Integrar múltiples funciones

**Descripción:** Añade un método `mostrarInfo()` a tu clase `Perro` que imprima todos los detalles del perro (color, edad, raza). Luego prueba este método desde el código principal. Esta actividad mejora la comprensión de cómo integrar múltiples métodos en una sola clase.

### Actividad 9: Personalización y validación de setters

**Descripción:** Modifica los métodos `setEdad()` e `setColor()` para que acepten solo edades menores a 15 años y colores válidos (como "negro", "blanco"). Este ejercicio refuerza la importancia de las validaciones dentro de los setters.

### Actividad 10: Implementación completa del objeto

**Descripción:** Combina todas las funcionalidades aprendidas hasta ahora en una clase `Perro` completamente funcional con métodos getter, setter y acción. Utiliza esta clase para simular interacciones con un perro (como cambiar su edad o raza) en el código principal.

Cada actividad debe permitir a los estudiantes entender gradualmente cómo se diseñan y utilizan las clases y métodos en Python, desde lo básico hasta aplicaciones más complejas.


<a id="creacion-de-constructores"></a>
## Creación de constructores

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/004-Desarrollo%20de%20clases/005-Creaci%C3%B3n%20de%20constructores)

### Introducción a los ejercicios

En esta carpeta, trabajaremos con ejercicios que te ayudarán a entender cómo crear y utilizar constructores en la programación orientada a objetos utilizando Python. Los ejemplos proporcionados centran su atención en una clase llamada `Gato`, donde aprenderás a inicializar propiedades de un objeto al momento de su creación usando diferentes métodos de construcción, incluyendo aquellos que no requieren todos los parámetros desde el principio. A través de estos ejercicios, adquirirás competencias clave como la definición de atributos y métodos dentro de una clase, así como la importancia de inicializar adecuadamente las instancias al crearlas para evitar problemas futuros en tu código.

### constructor
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python crea una clase llamada `Gato` que simula las propiedades y acciones de un gato en forma de objeto. Cuando creas una instancia de la clase `Gato`, como se hace con `gato1 = Gato()`, el constructor `__init__()` inicializa automáticamente algunas características del gato, tales como su color, edad, raza, nombre y color de ojos, estableciendo estas a valores vacíos (`""`) para el color y la raza, y `0` para la edad.

La clase también incluye dos métodos: `maulla()` que devuelve "miau" cuando se llama (representando el sonido que hace un gato) y `setEdad(nuevaedad)` que permite establecer una nueva edad al objeto gato solo si la nueva edad es exactamente un año mayor que la actual. Esto garantiza que no puedes establecer retroactivamente una edad menor, lo cual sería ilógico para un animal real.

Además, hay otro método `getEdad()` que simplemente devuelve la edad del gato como entero. En el código dado, después de crear el objeto `gato1`, se llama a estos métodos y funciones para demostrar cómo funcionan. Primero, imprime el sonido del gato con `maulla()`, luego muestra su edad actual (que es 0 por defecto), cambia la edad a 5 años usando `setEdad(5)`, y finalmente imprime de nuevo la edad del gato después de que se ha modificado.

`001-constructor.py`

```python
class Gato:

  def __init__(self): # El constructor se llama cuando se instancia el objeto
    self.color = ""   # Una clase tiene propiedades (estáticas)
    self.edad = 0    # La visibilidad por defecto es pública
    self.raza = ""
    self.nombre = ""
    self.color_ojos = ""
    
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
    
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1:
      self.edad = nuevaedad
    else:
      print("operación no permitida")
      
  def getEdad(self):
    return self.edad
    
gato1 = Gato()
print(gato1.maulla())
print("ahora mismo el gato tiene",gato1.getEdad(),"años")
gato1.setEdad(5)  # Esto es mucho más seguro
print("ahora mismo el gato tiene",gato1.getEdad(),"años")
```

### constructor con parameteros
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python muestra cómo crear una clase llamada `Gato` que simula las características y acciones de un gato. La parte más importante es el método especial `__init__`, conocido como constructor, que se llama automáticamente cuando creamos un nuevo objeto del tipo `Gato`. En este caso, el constructor necesita dos parámetros: `nuevocolor` (que define el color del gato) y `nuevaedad` (la edad inicial del gato).

Además de definir las propiedades (`color` y `edad`) en el constructor, la clase también tiene métodos que describen acciones del gato. Por ejemplo, `maulla()` devuelve "miau", lo cual es un comportamiento esperado para cualquier gato. Otros métodos como `setEdad(nuevaedad)` permiten cambiar la edad del gato solo si cumple con una condición específica (si la nueva edad es exactamente uno más que la edad actual), y `getEdad()` permite obtener el valor de la propiedad `edad`.

El último renglón, `gato1 = Gato("naranja",0)`, crea un nuevo objeto del tipo `Gato` con un color naranja y una edad inicial de 0. Este es un ejemplo de cómo se utiliza el constructor para inicializar las propiedades del gato cuando se crea el objeto.

Este código es importante porque demuestra cómo utilizar constructores en Python para establecer valores iniciales en objetos, así como cómo definir métodos que manipulan y acceden a estas propiedades.

`002-constructor con parameteros.py`

```python
class Gato:

  def __init__(self,nuevocolor,nuevaedad): # El constructor se llama cuando se instancia el objeto
    self.color = nuevocolor   # Una clase tiene propiedades (estáticas)
    self.edad = nuevaedad    # La visibilidad por defecto es pública
    
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
    
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1:
      self.edad = nuevaedad
    else:
      print("operación no permitida")
      
  def getEdad(self):
    return self.edad
    
gato1 = Gato("naranja",0)       # La edad no tiene sentido si cubrimos el nacimiento de un gato
```

### no todos los parametros en el constructor
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python muestra cómo crear una clase llamada `Gato` que simula las características y acciones de un gato en un programa. La clase incluye un constructor (`__init__`) que inicializa la propiedad `color` con el valor proporcionado cuando se crea un objeto del tipo `Gato`. Además, define otras propiedades como `edad`, que se inicializa en 0.

El código también contiene métodos para representar acciones típicas de los gatos. El método `maulla()` simplemente retorna la cadena "miau", imitando el sonido que hace un gato al maullar. Hay otro método llamado `setEdad()`, el cual permite cambiar la edad del gato, pero solo si la nueva edad es exactamente uno más que la edad actual. Si no se cumple esta condición, imprime un mensaje indicando que la operación no está permitida.

Por último, el código crea una instancia de la clase `Gato` llamada `gato1`, especificando su color como "naranja". Sin embargo, hay un comentario al final del archivo que sugiere que inicializar la edad en cero cuando se nombra un gato no tiene mucho sentido desde una perspectiva realista (ya que los gatos tienen una edad desde el momento de su nacimiento), lo cual es un punto a considerar para mejorar este modelo.

`003-no todos los parametros en el constructor.py`

```python
class Gato:

  def __init__(self,nuevocolor): # El constructor se llama cuando se instancia el objeto
    self.color = nuevocolor   # Una clase tiene propiedades (estáticas)
    self.edad = 0    # La visibilidad por defecto es pública
    
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
    
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1:
      self.edad = nuevaedad
    else:
      print("operación no permitida")
      
  def getEdad(self):
    return self.edad
    
gato1 = Gato("naranja")       # La edad no tiene sentido si cubrimos el nacimiento de un gato
```

### Actividades propuestas

### Actividades Propuestas

#### 1. **Constructor Sencillo: Crear una Clase con Constructor Vacío**
- **Descripción:** Diseña una clase en Python que represente a un estudiante (Ejemplo: `Estudiante`). Incluye atributos como nombre, curso y media de notas. Implementa el constructor vacío para inicializar dichos atributos.
- **Objetivo:** Aprender cómo se define e implementa un constructor sin parámetros en una clase.

#### 2. **Constructor con Parámetros: Clase Libro**
- **Descripción:** Crea una clase `Libro` que tenga atributos como título, autor y año de publicación. Implementa el constructor para aceptar estos tres parámetros al crear un objeto del tipo `Libro`.
- **Objetivo:** Familiarizarse con la creación de constructores que toman múltiples argumentos.

#### 3. **Constructor Completo: Clase Empleado**
- **Descripción:** Define una clase en Python llamada `Empleado` que tenga atributos como nombre, cargo y salario. Implementa un constructor completo que permita inicializar todos estos atributos al crear un objeto de la clase.
- **Objetivo:** Aprender a manejar múltiples parámetros dentro del constructor para inicialización.

#### 4. **Uso del Método `set` y `get`: Clase Automóvil**
- **Descripción:** Crea una clase `Automovil` con atributos como marca, modelo y año de fabricación. Implementa métodos `set_marca`, `set_modelo`, `get_marca`, y `get_modelo`. Realiza algunas operaciones utilizando estos métodos.
- **Objetivo:** Practicar la creación y uso de métodos getter y setter para gestionar el acceso a los atributos del objeto.

#### 5. **Constructor con Valores por Defecto: Clase Alumno**
- **Descripción:** Diseña una clase `Alumno` que tenga un constructor con parámetros pero también defina valores por defecto para algunos de ellos (por ejemplo, el curso puede tener un valor por defecto si no se proporciona).
- **Objetivo:** Aprender a utilizar argumentos opcionales en los constructores.

#### 6. **Combinación Constructor y Métodos: Clase Estacionamiento**
- **Descripción:** Crea una clase `Estacionamiento` que tenga atributos como número de plazas totales, ocupadas y libres. Implementa un constructor para inicializar el estacionamiento vacío, junto con métodos para registrar entradas/salidas y verificar disponibilidad.
- **Objetivo:** Practicar la combinación del uso de constructores con otros métodos en una clase.

#### 7. **Manejo de Errores en Constructores: Clase CuentaBancaria**
- **Descripción:** Define una clase `CuentaBancaria` que tenga atributos como número de cuenta, saldo y límite diario de retiros. Implementa un constructor que valide parámetros (por ejemplo, el saldo inicial no puede ser negativo) y genere un mensaje de error en caso de incompatibilidad.
- **Objetivo:** Aprender a manejar errores dentro del constructor para garantizar la integridad de los objetos creados.

#### 8. **Herencia y Constructores: Clase Estudiante y Profesor**
- **Descripción:** Crea dos clases `Estudiante` e `Instructor`, donde `Profesor` hereda de `Persona`. Define un constructor en `Persona` para atributos comunes (nombre, edad) y añade constructores específicos en las subclases que incluyan características únicas.
- **Objetivo:** Practicar la implementación de constructores tanto en clases base como en sus heredadas.

Estas actividades están diseñadas para ayudarte a dominar los conceptos de creación y uso de constructores en Python, así como las mejores prácticas al trabajar con objetos y métodos.


<a id="utilizacion-de-clases-y-objetos"></a>
## Utilización de clases y objetos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/004-Desarrollo%20de%20clases/006-Utilizaci%C3%B3n%20de%20clases%20y%20objetos)

### Introducción a los ejercicios

Esta carpeta contiene una serie de ejercicios diseñados para ayudarte a familiarizarte con el concepto de clases y objetos en Python. Cada ejercicio se centra en la creación de instancias de clase, manejo de atributos (propiedades) y métodos dentro del contexto de un programa realista, como gestionar información de clientes. A través de estos ejercicios, aprenderás a crear una clase `Cliente` con atributos como nombre, email y dirección, y verás cómo interactuar con objetos que se crean a partir de esta clase.

Los ejercicios también exploran conceptos más avanzados, como la manipulación directa del diccionario interno del objeto para acceder a sus atributos, lo cual te dará una comprensión más profunda sobre la estructura y funcionamiento de las clases en Python. Estos ejercicios no solo te ayudarán a dominar los fundamentos de la orientación a objetos sino que también mejorarán tu capacidad para aplicar estos conceptos en situaciones prácticas de programación.

### Multiples instancias
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una clase llamada `Gato` en Python, que es un ejemplo básico de cómo crear y usar objetos basados en clases. La clase tiene varias partes importantes:

1. **Constructor (`__init__`)**: Este método especial se ejecuta automáticamente cuando creamos (o "instanciamos") un objeto de la clase `Gato`. Recibe un parámetro que es el color del gato y establece este valor en una propiedad llamada `color`. También inicializa otra propiedad, `edad`, a 0.

2. **Métodos**: La clase incluye métodos como `maulla()` (que simplemente retorna "miau", representando un maullido de gato) y `setEdad()`, que permite establecer la edad del gato pero solo si está incrementándose en una unidad respecto a su valor actual. Esto impide disminuir artificialmente la edad del gato, lo cual no tiene sentido biológicamente.

3. **Instancia de objetos**: Al final del código se crean dos instancias de `Gato`: `gato1` con color naranja y `gato2` con color negro. Ambas tienen inicialmente una edad de 0.

Este ejemplo ilustra cómo usar clases para definir plantillas de objetos (en este caso, gatos) que pueden tener propiedades únicas (como el color) y métodos que describen sus acciones o comportamiento. Es importante entender esto porque permite organizar el código de manera más estructurada y reutilizable al crear múltiples instancias basadas en la misma clase.

`001-Multiples instancias.py`

```python
class Gato:

  def __init__(self,nuevocolor): # El constructor se llama cuando se instancia el objeto
    self.color = nuevocolor   # Una clase tiene propiedades (estáticas)
    self.edad = 0    # La visibilidad por defecto es pública
    
  def maulla(self):   # Un método es una acción que realiza el objeto
    return "miau"
    
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1:
      self.edad = nuevaedad
    else:
      print("operación no permitida")
      
  def getEdad(self):
    return self.edad
    
gato1 = Gato("naranja")       # La edad no tiene sentido si cubrimos el nacimiento de un gato
gato2 = Gato("negro")       # La edad no tiene sentido si cubrimos el nacimiento de un gato
```

### ejercicio practico clientes
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código define una clase en Python llamada `Cliente`. La clase tiene un método especial llamado `__init__` que se ejecuta automáticamente cada vez que creamos una nueva instancia o objeto de la clase `Cliente`. Este método `__init__` recibe tres parámetros adicionales: `nuevonombre`, `nuevoemail`, y `nuevadireccion`.

Dentro del método `__init__`, estos parámetros se usan para asignar valores a los atributos (o propiedades) de la clase. Por ejemplo, `self.nombre = nuevonombre` establece el nombre del cliente que se pasa como argumento al crear un nuevo objeto de tipo `Cliente`. Esto significa que cada vez que creamos un nuevo cliente en nuestro programa, podemos proporcionar su nombre, correo electrónico y dirección para inicializar adecuadamente este nuevo objeto.

Es importante porque nos permite organizar la información de los clientes de una manera estructurada, facilitando operaciones como agregar nuevos clientes, modificar sus datos o acceder a la información de un cliente específico.

`002-ejercicio practico clientes.py`

```python
class Cliente:
  def __init__(self,nuevonombre,nuevoemail,nuevadireccion):
    self.nombre = nuevonombre
    self.email = nuevoemail
    self.direccion = nuevadireccion
    
```

### ahora introduccion por el usuario
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código crea una clase llamada `Cliente` en Python, que es una plantilla para objetos que representan información sobre clientes. La función `__init__` dentro de la clase se utiliza para inicializar los atributos del cliente como el nombre, email y dirección cuando un objeto `Cliente` es creado.

Después de definir la clase, hay un mensaje que imprime en la pantalla indicando quién creó el programa (en este caso, "Jose Vicente Carratala"). Luego, se solicita al usuario que introduzca los datos del cliente: nombre, email y dirección. Estos datos son leídos desde el teclado usando la función `input()`. Finalmente, se crea un objeto de tipo `Cliente` utilizando estos datos proporcionados por el usuario.

Este código es importante porque demuestra cómo crear e inicializar objetos en Python a partir de una clase definida por el programador. Permite almacenar y manipular información estructurada sobre los clientes de manera organizada y eficiente.

`003-ahora introduccion por el usuario.py`

```python
class Cliente:
  def __init__(self,nuevonombre,nuevoemail,nuevadireccion):
    self.nombre = nuevonombre
    self.email = nuevoemail
    self.direccion = nuevadireccion
    
print("Programa clientes por Jose Vicente Carratala")

nombrecliente = input("Introduce el nombre de un cliente: ")
emailcliente = input("Introduce el email de un cliente: ")
direccioncliente = input("Introduce la dirección de un cliente: ")

cliente1 = Cliente(nombrecliente,emailcliente,direccioncliente)
```

### print cliente
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código es una sencilla aplicación en Python que crea objetos basados en clases. La clase se llama `Cliente` y tiene tres atributos importantes: nombre, email y dirección. Estos atributos son establecidos cuando creamos un nuevo objeto de la clase `Cliente`, proporcionando valores para ellos a través del método `__init__`.

El programa comienza mostrándonos un mensaje en pantalla que indica el propósito del código (un programa de clientes). Luego, pide al usuario que ingrese información sobre un cliente: nombre, email y dirección. Esta información se utiliza para crear una nueva instancia de la clase `Cliente`, guardada en la variable `cliente1`.

Finalmente, el programa muestra por pantalla toda la información del objeto `cliente1`. Esto es útil porque nos permite ver fácilmente cómo los datos proporcionados han sido encapsulados dentro de un objeto y cómo podemos acceder a ellos de manera organizada.

`004-print cliente.py`

```python
class Cliente:
  def __init__(self,nuevonombre,nuevoemail,nuevadireccion):
    self.nombre = nuevonombre
    self.email = nuevoemail
    self.direccion = nuevadireccion
    
print("Programa clientes por Jose Vicente Carratala")

nombrecliente = input("Introduce el nombre de un cliente: ")
emailcliente = input("Introduce el email de un cliente: ")
direccioncliente = input("Introduce la dirección de un cliente: ")

cliente1 = Cliente(nombrecliente,emailcliente,direccioncliente)

print(cliente1)
```

### recorrer claves
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código en Python te enseña cómo crear y utilizar objetos desde una clase. La clase se llama `Cliente` y tiene tres atributos importantes: nombre, email y dirección. Cuando creas un objeto del tipo `Cliente`, debes proporcionar estos tres datos.

Primero, el programa muestra un mensaje para indicar de quién es este código. Luego, pide al usuario que introduzca los detalles de un cliente (nombre, email y dirección). Estos datos son después usados para crear una instancia del objeto `Cliente`.

Finalmente, el programa recorre todas las propiedades (o atributos) del objeto `cliente1` utilizando un bucle `for`. Aquí es donde se utiliza `__dict__`, que es un diccionario incorporado en Python que contiene todos los atributos de un objeto como pares clave-valor. En cada iteración, muestra por pantalla el nombre y valor de cada atributo del cliente creado.

Este código es importante porque demuestra cómo definir una clase, crear objetos a partir de ella y luego acceder a sus propiedades de manera dinámica, lo que te permite manipular fácilmente los datos del objeto.

`005-recorrer claves.py`

```python
class Cliente:
  def __init__(self,nuevonombre,nuevoemail,nuevadireccion):
    self.nombre = nuevonombre
    self.email = nuevoemail
    self.direccion = nuevadireccion
    
print("Programa clientes por Jose Vicente Carratala")

nombrecliente = input("Introduce el nombre de un cliente: ")
emailcliente = input("Introduce el email de un cliente: ")
direccioncliente = input("Introduce la dirección de un cliente: ")

cliente1 = Cliente(nombrecliente,emailcliente,direccioncliente)

for clave in cliente1.__dict__:
  print("La pieza de información ",clave,"vale: ",cliente1.__dict__[clave])
```

### Actividades propuestas

### Actividad 1: Creación y Manipulación de Instancias de Clase

**Descripción:** Crea una clase `Perro` similar a la clase `Gato` vista en el ejercicio. La clase debe tener un método para establecer la edad del perro y otro para maullar (en este caso, sustituir "miau" por algún sonido propio de los perros). Aprenderás a instanciar objetos y usar métodos y propiedades.

### Actividad 2: Creación de Clientes Personalizados

**Descripción:** Implementa una clase `Cliente` similar al ejercicio proporcionado, pero añade un método que permita modificar la dirección del cliente. Esto te ayudará a entender cómo se gestionan los cambios en las propiedades de un objeto.

### Actividad 3: Interacción con el Usuario para Crear Objetos

**Descripción:** Desarrolla una aplicación que permite al usuario introducir datos por consola para crear instancias de la clase `Cliente`. Aprenderás a utilizar funciones como `input` en combinación con clases y objetos.

### Actividad 4: Visualización Detallada del Cliente

**Descripción:** Extiende el ejercicio de la actividad anterior añadiendo un método que imprima todos los detalles del cliente (nombre, email, dirección) una vez se haya creado la instancia. Esto te permitirá aprender a combinar métodos y atributos en objetos.

### Actividad 5: Recorrido de Atributos

**Descripción:** Crea una función o método dentro de tu clase `Cliente` que recorra todos los atributos del objeto (como hizo el ejercicio con `__dict__`) e imprima cada uno. Esto te enseñará a trabajar directamente con las propiedades internas de un objeto.

### Actividad 6: Gestión de Múltiples Instancias

**Descripción:** A partir de la clase `Gato` vista en el ejercicio, desarrolla una aplicación que permita crear múltiples instancias del mismo y realizar acciones sobre ellas (por ejemplo, cambiar su color o edad). Esto te ayudará a entender cómo manejar varios objetos de la misma clase.

### Actividad 7: Modificar Atributos Privados

**Descripción:** Implementa un método dentro de tu clase `Perro` para modificar atributos privados. Esto te enseñará sobre el control de acceso en las propiedades de una clase y cómo manejar errores o restricciones cuando se intentan cambiar ciertas variables.

### Actividad 8: Interacción entre Objetos

**Descripción:** Crea un programa donde dos objetos (por ejemplo, instancias de `Cliente`) puedan interactuar entre sí. Por ejemplo, podrías implementar métodos que permitan a los clientes compartir información o realizar transacciones entre ellos.

### Actividad 9: Documentación y Pruebas Básicas

**Descripción:** Escribir documentación para cada método en tus clases y crear pruebas básicas (usando prints o funciones de depuración) para verificar el funcionamiento correcto de tu código. Aprenderás a seguir prácticas de programación profesionales.

### Actividad 10: Clase Compleja con Herencia

**Descripción:** Diseña una clase `VIPCliente` que herede de la clase `Cliente`. La clase `VIPCliente` debe tener métodos y atributos adicionales para gestionar beneficios especiales del cliente VIP. Esto te ayudará a entender conceptos avanzados como herencia en Python.


<a id="utilizacion-de-clases-heredadas"></a>
## Utilización de clases heredadas

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/004-Desarrollo%20de%20clases/007-Utilizaci%C3%B3n%20de%20clases%20heredadas)

### Introducción a los ejercicios

Esta carpeta contiene una serie de ejercicios que te ayudarán a comprender y practicar la herencia en programación orientada a objetos utilizando Python. Los ejercicios se centran en crear una jerarquía de clases, donde las clases `Gato` y `Perro` heredan propiedades y métodos de una clase base llamada `Animal`. En estos ejercicios, trabajarás con conceptos como inicialización de atributos, uso correcto del método `super()`, manejo de propiedades privadas, validación de datos ingresados por el usuario, e implementación de lógica condicional para clasificar animales según su edad. Estos ejercicios te permitirán mejorar tus habilidades en la creación y manipulación de clases heredadas y reforzar tu comprensión sobre cómo estructurar programas con arquitecturas orientadas a objetos más complejas.

### clase gato
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define una clase llamada `Gato` en Python. La función `__init__` es un método especial que se utiliza para inicializar las características de cada gato cuando se crea un nuevo objeto de la clase. En este caso, el método `__init__` establece dos atributos para los gatos: `color`, que será una cadena vacía (`""`) y `edad`, que será cero (`0`). Estos atributos representan características básicas del gato, como su color y su edad, pero no se les proporciona un valor específico en este punto. El objetivo es permitir a otros programas o usuarios asignar estos valores más tarde cuando creen objetos de la clase `Gato`.

`001-clase gato.py`

```python
class Gato:
  def __init__(self):
    self.color = ""
    self.edad = 0
```

### clase perro
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código define dos clases en Python: `Gato` y `Perro`. Cada una de estas clases tiene un método especial llamado `__init__`, que se ejecuta automáticamente cuando creamos (o inicializamos) un objeto de la clase. En el caso del gato y del perro, este método establece dos características o atributos: `color` y `edad`. Ambas características son cadenas vacías (`""`) para `color`, lo que significa que no se ha especificado ningún color al principio, y `0` para la edad, lo que indica que no se ha definido ninguna edad inicialmente. Esto es importante porque nos permite crear objetos de tipo gato o perro sin necesidad de proporcionar información sobre el color o la edad en ese momento; más tarde podemos cambiar estos valores según sea necesario.

Esencialmente, este código te da las bases para comenzar a trabajar con animales específicos como gatos y perros en tu programa, permitiéndote añadir detalles adicionales conforme lo necesites.

`002-clase perro.py`

```python
class Gato:
  def __init__(self):
    self.color = ""
    self.edad = 0
    
class Perro:
  def __init__(self):
    self.color = ""
    self.edad = 0
```

### clase madre
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código muestra cómo se crean y relacionan diferentes clases en Python. La clase `Animal` es una clase base que contiene dos atributos: `color`, que almacena el color del animal, y `edad`, que indica la edad del animal. Estos atributos son inicializados a cadenas vacías y cero respectivamente cuando se crea un objeto de la clase `Animal`.

Las clases `Gato` y `Perro` heredan de la clase `Animal`. Esto significa que las clases `Gato` y `Perro` obtienen todos los métodos y atributos de la clase `Animal`. Sin embargo, en este ejemplo, no se especifica cómo inicializar estos atributos al crear un objeto gato o perro. El uso de `super()` dentro del método `__init__` de las clases hijas debería ayudar a llamar al constructor de la clase padre para inicializar los atributos heredados, pero en Python 3 se debe usar correctamente como `super().__init__()`. Sin esta llamada explícita a `super().__init__()`, los atributos `color` y `edad` no se inicializan correctamente cuando se crean objetos de tipo `Gato` o `Perro`.

Es importante entender que la herencia permite reutilizar código existente (en este caso, el contenido de la clase `Animal`) y modificar o extender su comportamiento según sea necesario para cada subclase.

`003-clase madre.py`

```python
class Animal():
  def __init__(self):
    self.color = ""
    self.edad = 0

class Gato(Animal):
  def __init__(self):
    super()
    
class Perro(Animal):
  def __init__(self):
    super()
```

### usando la clase madre
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código muestra cómo se crean y utilizan clases en Python, específicamente enfocándose en la herencia de clases. La clase `Animal` es definida primero y contiene dos atributos: color y edad. Luego, se definen dos nuevas clases, `Gato` y `Perro`, que heredan de la clase `Animal`. Esto significa que tanto los gatos como los perros tienen por defecto el color y la edad desde la clase madre `Animal`.

En las definiciones de las clases `Gato` y `Perro`, se llama a `super().__init__()` en sus métodos `__init__`, lo cual es una forma de llamar al constructor de la clase padre (`Animal`). De esta manera, aunque no se especifican valores para color o edad cuando se crea un objeto gato (como ocurre con el objeto `gato1`), estos atributos heredados estarán presentes y pueden ser accedidos posteriormente.

Finalmente, se crea una instancia de la clase `Gato`, llamada `gato1`, y se imprime su edad. Como no se especificó ningún valor para `edad` al crear este objeto gato, el resultado del print será 0, que es el valor por defecto establecido en la clase padre `Animal`. Este ejemplo demuestra cómo la herencia permite reutilizar código de una clase base y agregar o modificar comportamientos específicos en clases derivadas.

`004-usando la clase madre.py`

```python
class Animal():
  def __init__(self):
    self.color = ""
    self.edad = 0

class Gato(Animal):
  def __init__(self):
    super().__init__()
    
class Perro(Animal):
  def __init__(self):
    super().__init__()
    
gato1 = Gato()
print(gato1.edad)
```

### Roca
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código muestra cómo se crean clases en Python y cómo una clase puede heredar atributos de otra clase. Primero, se define una clase llamada `Animal` que tiene dos propiedades: `color` y `edad`. Estas propiedades son inicializadas con valores vacíos cuando se crea un objeto de la clase `Animal`.

Luego, se definen dos clases más, `Gato` y `Perro`, ambas heredan de la clase `Animal`. Esto significa que tanto el gato como el perro tienen acceso a los atributos (`color` y `edad`) y métodos (no mostrados en este fragmento) de la clase `Animal`. En el constructor (`__init__`) de cada una de estas clases, se usa la función `super()` para llamar al constructor de la clase base `Animal`, asegurando que las propiedades del animal sean inicializadas correctamente.

Finalmente, se crea un objeto `gato1` de tipo `Gato` y se imprime su edad. Aunque no se especifica explícitamente una edad cuando se crea el gato (lo cual significa que la edad es 0 por defecto en la clase base `Animal`), este código demuestra cómo acceder a los atributos heredados de la clase padre.

`005-Roca.py`

```python
class Animal():
  def __init__(self):
    self.color = ""
    self.edad = 0

class Gato(Animal):
  def __init__(self):
    super().__init__()
    
class Perro(Animal):
  def __init__(self):
    super().__init__()
    
gato1 = Gato()
print(gato1.edad)
```

### nivel superior de herencia
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código en Python muestra cómo se implementa la herencia entre clases. Comenzamos con una clase base llamada `Objeto`, que tiene un método especial `__init__` que inicializa tres atributos: `x`, `y` y `z`. Luego, creamos dos nuevas clases derivadas de `Objeto`: `Roca` e `Animal`. La clase `Roca` no agrega nada nuevo a la clase base, pero sigue el patrón de herencia al llamar al constructor de la clase padre usando `super().__init__()`. Por otro lado, la clase `Animal` añade dos atributos adicionales: `color` y `edad`, también llamando al constructor de su clase padre para inicializar los atributos que hereda.

Además, se definen dos clases más (`Gato` y `Perro`) que derivan de la clase `Animal`. Estas clases simplemente llaman a `super().__init__()` para asegurar que todos los atributos heredados desde `Objeto` y `Animal` se inicialicen correctamente.

Finalmente, el código crea una instancia de la clase `Gato`, llamada `gato1`, e imprime su atributo `edad`. Esto demuestra cómo las clases hijas pueden acceder a los métodos y atributos proporcionados por sus clases padre.

`006-nivel superior de herencia.py`

```python
class Objeto():
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0  

class Roca(Objeto):
  def __init__(self):
    super().__init__()

class Animal(Objeto):
  def __init__(self):
    super().__init__()
    self.color = ""
    self.edad = 0
    
class Gato(Animal):
  def __init__(self):
    super().__init__()
    
class Perro(Animal):
  def __init__(self):
    super().__init__()
    
gato1 = Gato()
print(gato1.edad)
```

### Ejercicio acumulativo
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código define una clase en Python llamada `Animal`. Una clase es como un plan o plantilla para crear objetos, y en este caso, el objeto que se puede crear a partir de esta clase sería un animal. Dentro de la clase, hay un método especial denominado `__init__`, que se ejecuta automáticamente cada vez que se crea una nueva instancia del objeto `Animal`. Este método inicializa los atributos del objeto.

Los atributos son características o propiedades del objeto. En este caso, el código establece tres atributos: `color`, `edad` y `raza`. El atributo `color` es un string vacío, lo que significa que no tiene ningún color asignado al principio. La edad se inicializa en 0, indicando que la edad del animal no ha sido especificada al crearlo. Es importante notar el uso de doble guión bajo antes de `raza`, lo cual indica que este atributo es privado, significando que solo puede ser accedido dentro de la clase y no desde fuera de ella.

Esta estructura básica en una clase como esta permite a otros programadores crear objetos animales con propiedades similares, facilitando así el desarrollo de aplicaciones más grandes donde se puedan trabajar con varios tipos de animales.

`007-Ejercicio acumulativo.py`

```python
class Animal():
  def __init__(self):
    self.color = ""
    self.edad = 0
    self.__raza = 0
```

### metodos
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código define una clase llamada `Animal` en Python. La clase `Animal` tiene atributos como color, edad y raza que describen las características generales de un animal. El método `__init__` es el constructor que inicializa estos atributos cuando se crea un nuevo objeto del tipo `Animal`. Es importante notar que el atributo `raza` está definido con dos guiones bajos al principio (`__raza`), lo cual en Python indica que este atributo es privado, y solo puede ser accedido dentro de la misma clase.

La clase también incluye métodos para establecer y obtener los valores de edad y raza del animal. Por ejemplo, `setEdad(nuevaedad)` intenta incrementar la edad si el parámetro proporcionado es exactamente uno mayor que la edad actual, aunque esta lógica parece tener un error de sintaxis (falta dos puntos al final de la condición). Los métodos `getEdad()` y `getRaza()` permiten obtener los valores actuales de estos atributos. Además, hay un método llamado `descripcion()`, que intenta devolver una cadena combinada con la edad, color y raza del animal, aunque también presenta problemas debido a la falta de dos puntos al final de su definición y por no tener en cuenta que el atributo `__raza` es privado.

Es fundamental corregir estos errores para que la clase funcione correctamente.

`008-metodos.py`

```python
class Animal():
  '''
    Clase Animal, define edad, color y raza
  '''
  def __init__(self):
    self.color = ""
    self.edad = 0
    self.__raza = 0
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1
      self.edad += 1
  def getEdad(self):
    return self.edad
  def setRaza(self,nuevaraza)
    self.raza = nuevaraza
  def getRaza(self):
    return self.raza
  def descripcion():
    return str(self.edad)+self.color+self.__raza
    
```

### clases hijas
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este fragmento de código define una jerarquía básica en programación orientada a objetos utilizando clases y herencia en Python. La clase principal es `Animal`, que contiene propiedades como el color, la edad y la raza del animal. Esta clase tiene métodos para establecer (`setEdad` y `setRaza`) y obtener (`getEdad` y `getRaza`) los valores de estas propiedades.

Además, hay dos clases derivadas (clases hijas): `Gato` e `Perro`, que heredan de la clase `Animal`. Estas clases añaden comportamientos específicos a partir del modelo general proporcionado por `Animal`. Por ejemplo, el método `maulla()` en la clase `Gato` hace que un objeto gato emita el sonido "miau", mientras que en la clase `Perro`, el método `ladra()` permite al perro emitir un ladrido.

Es importante notar que hay algunos errores en este código, como la falta de dos puntos (`:`) después del nombre de las funciones y métodos (por ejemplo, en `setEdad(self,nuevaedad):`), lo cual es necesario para definir correctamente los métodos en Python. También hay un error de sintaxis en el método `descripcion()`, donde no se está devolviendo la raza ya que la variable ha sido encapsulada con doble guion bajo (`__raza`). Además, falta una coma después del parámetro `self` en los métodos de las clases hijas y la implementación del constructor (`__init__`) en estas clases no está completa.

Este código es una introducción a cómo se pueden definir comportamientos comunes para un grupo de objetos (clase Animal) y luego especializar estos comportamientos según el tipo específico de objeto (Gato o Perro).

`009-clases hijas.py`

```python
'''
  Programa refugio
  (c) 2025 Jose Vicente Carratala
  Este programa gestiona un refugio
'''

class Animal():
  '''
    Clase Animal, define edad, color y raza
  '''
  def __init__(self):
    self.color = ""
    self.edad = 0
    self.__raza = 0
  def setEdad(self,nuevaedad):
    if self.edad == nuevaedad - 1
      self.edad += 1
  def getEdad(self):
    return self.edad
  def setRaza(self,nuevaraza)
    self.raza = nuevaraza
  def getRaza(self):
    return self.raza
  def descripcion():
    return str(self.edad)+self.color+self.__raza

def Gato(Animal):
  def __init__():
    super().__init__()
  def maulla(self):
    print("miau")

def Perro(Animal):
  def __init__():
    super().__init__()
  def ladra(self):
    print("guau")
    
    
    
    
```

### continuamos con el ejercicio
<small>Creado: 2025-09-26 16:20</small>

#### Explicación

Este código Python implementa un programa sencillo para gestionar animales en un refugio. Define una clase base llamada `Animal` que incluye atributos como color y edad, así como métodos para manipular estos atributos. La clase `Gato` y la clase `Perro` heredan de la clase `Animal`, añadiendo características específicas a cada tipo de animal, como el maullido del gato o el ladrido del perro.

El programa permite al usuario introducir datos sobre un gato y un perro, incluyendo color, raza e edad. Luego, realiza una clasificación básica basada en la edad de cada animal (cachorro, adulto joven o adulto). El código también simula el crecimiento del gato hasta una edad máxima permitida y muestra las propiedades públicas del perro usando su diccionario interno `__dict__`.

Este ejemplo es útil para aprender cómo crear clases en Python, heredar de estas clases y manejar atributos privados mediante encapsulamiento. Específicamente, el uso de métodos setter como `setEdad` ayuda a controlar cómo se modifica la edad del animal, evitando modificaciones no deseadas o incoherentes.

`010-continuamos con el ejercicio.py`

```python
'''
  Programa refugio
  (c) 2025 Jose Vicente Carratala
  Este programa gestiona un refugio
'''

class Animal:
  '''
    Clase Animal: define color (str), edad (int) y raza (privada)
  '''
  def __init__(self):
    self.color = ""
    self.edad = 0
    self.__raza = ""

  def setEdad(self, nuevaedad):
    # Solo permite incrementos de 1 en 1
    if self.edad == nuevaedad - 1:
      self.edad += 1
    else:
      print("operación no permitida")

  def getEdad(self):
    return self.edad

  def setRaza(self, nuevaraza):
    self.__raza = str(nuevaraza)

  def getRaza(self):
    return self.__raza

  def descripcion(self):
    return "Edad: " + str(self.edad) + ", Color: " + self.color + ", Raza: " + self.__raza


class Gato(Animal):
  def __init__(self):
    super().__init__()
  def maulla(self):
    print("miau")


class Perro(Animal):
  def __init__(self):
    super().__init__()
  def ladra(self):
    print("guau")


EDAD_MAX_GATO = 25
EDAD_MAX_PERRO = 30

print("Hoy soy Jose Vicente y bienvenido a mi refugio")

perro = Perro()
gato = Gato()

# --- Entrada de datos con validación básica ---
gato.color = input("Introduce el color del gato: ")
perro.color = input("Introduce el color del perro: ")

gato.setRaza(input("Introduce la raza del gato: "))
perro.setRaza(input("Introduce la raza del perro: "))

try:
  gato.edad = int(input("Introduce la edad del gato (entero): "))
except:
  print("Edad del gato inválida, se establece a 0")
  gato.edad = 0

try:
  perro.edad = int(input("Introduce la edad del perro (entero): "))
except:
  print("Edad del perro inválida, se establece a 0")
  perro.edad = 0

# Aserciones: no negativas
assert gato.edad >= 0 and perro.edad >= 0, "hay un error: edad negativa"

# --- Clasificación por edad ---
def clasifica_edad(edad):
  if edad < 1:
    return "cachorro"
  elif edad < 7:
    return "adulto joven"
  else:
    return "adulto"

print("El gato es:", clasifica_edad(gato.edad))
print("El perro es:", clasifica_edad(perro.edad))

# --- Simulación de crecimiento del gato respetando setEdad ---
try:
  edad_maxima = int(input("¿Hasta qué edad quieres simular para el gato? "))
except:
  print("Edad de simulación inválida, se usará la edad actual del gato")
  edad_maxima = gato.edad

if edad_maxima > EDAD_MAX_GATO:
  print("Aviso: superaría EDAD_MAX_GATO, se limitará a", EDAD_MAX_GATO)
  edad_maxima = EDAD_MAX_GATO

edad_actual = gato.getEdad()
# Avanza de uno en uno usando setEdad (desde la siguiente edad)
objetivo = edad_maxima
siguiente = edad_actual + 1
while siguiente <= objetivo:
  gato.setEdad(siguiente)
  print("Gato ahora tiene:", gato.getEdad())
  siguiente += 1

# --- Mostrar descripciones finales ---
print("Ficha del gato:", gato.descripcion())
print("Ficha del perro:", perro.descripcion())

# --- Recorrer propiedades públicas del perro ---
print("Propiedades públicas del perro:")
for clave in perro.__dict__:
  # __raza está name-mangled y no aparecerá como clave simple, mostramos lo visible
  print(clave, ":", perro.__dict__[clave])
```

### Actividades propuestas

### Actividades Propuestas

1. **Creación de Clases Básicas**
   - **Descripción:** Crea una clase base llamada `Animal` con propiedades como color y edad. Luego, heredará la clase `Gato` y `Perro`. Los estudiantes deben entender cómo inicializar objetos y definir atributos.

2. **Herencia Simples de Clases**
   - **Descripción:** Los alumnos deberán crear una estructura básica de clases donde `Animal` es la superclase, mientras que `Gato` y `Perro` son subclases. El objetivo es aprender a implementar constructores con herencia.

3. **Uso de Propiedades Privadas**
   - **Descripción:** Los estudiantes deben incorporar propiedades privadas en una clase base (`Animal`) y luego utilizar el método `super()` para inicializarlas correctamente en las subclases (`Gato` y `Perro`).

4. **Validación y Control de Edad**
   - **Descripción:** Diseñar un sistema que permita incrementar la edad del animal solo si es posible (edad actual + 1) usando el método `setEdad()`. Los alumnos deben aprender a manejar condiciones y lógica dentro de métodos.

5. **Metodología con Docstrings**
   - **Descripción:** Implementar docstrings en las clases y métodos para documentar la funcionalidad, especialmente en métodos como `descripcion()` que devuelven información acerca del objeto.

6. **Manejo de Excepciones (Validación de Edad)**
   - **Descripción:** Los alumnos deben implementar el manejo de excepciones para asegurar que las entradas de edad se conviertan correctamente a enteros, utilizando bloques `try/except`.

7. **Clasificación por Edades y Categorización**
   - **Descripción:** Diseñar un método o función que clasifique la edad del animal en categorías como "cachorro", "adulto joven" y "adulto". Utilizar estructuras de control como `if/elif` para realizar esta tarea.

8. **Simulación de Crecimiento**
   - **Descripción:** Implementar un bucle que simule el crecimiento del gato incrementando su edad hasta una edad máxima establecida por el usuario, utilizando el método `setEdad()` y controlando la entrada para evitar operaciones no permitidas.

9. **Funciones Auxiliares**
   - **Descripción:** Crear funciones auxiliares como `formatea_ficha(animal)` que devuelvan una descripción formateada del animal, utilizando el método `descripcion()`. Los alumnos deben aprender a utilizar argumentos y retornos de valores.

10. **Revisión de Propiedades**
    - **Descripción:** Los estudiantes deben crear una función que recorra las propiedades públicas de un objeto (en este caso, el perro) usando su diccionario `__dict__` para mostrar todas sus características. Esto les enseña cómo acceder a la información interna del objeto.

Estas actividades proporcionan un enfoque gradual y progresivo que va desde conceptos básicos hasta aplicaciones más avanzadas de programación orientada a objetos, adaptado al nivel y estilo de aprendizaje de los estudiantes de Formación Profesional.



<a id="lectura-y-escritura-de-informacion"></a>
# Lectura y escritura de información

<a id="flujos-tipos-bytes-y-caracteres-clases-relacionadas"></a>
## Flujos. Tipos bytes y caracteres. Clases relacionadas

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/001-Flujos.%20Tipos%20bytes%20y%20caracteres.%20Clases%20relacionadas)

### Introducción a los ejercicios

Esta carpeta contiene una serie de ejercicios en Python que te ayudarán a comprender cómo leer y escribir información en archivos, tanto en formato texto como binario. Los ejercicios iniciales te enseñan a trabajar con flujos de caracteres (archivos de texto) utilizando métodos básicos para la escritura y lectura de líneas individuales. Posteriormente, introduces el uso del módulo `pickle` para manejar datos en formato binario, lo cual es útil cuando necesitas guardar estructuras de datos más complejas que simples cadenas de texto. A través de estos ejercicios, mejorarás tus habilidades en la manipulación de archivos y entenderás mejor cómo Python facilita el almacenamiento y recuperación de información en diferentes formatos.

### flujo de caracteres
<small>Creado: 2025-10-02 15:14</small>

#### Explicación

Este código Python muestra cómo escribir información en un archivo de texto existente o nuevo. En primer lugar, el programa abre un archivo llamado "clientes.txt" en modo de escritura ('w'), lo que significa que cualquier dato que se escriba en él sobrescribirá el contenido anterior si ya existe algún texto dentro del archivo. Luego, utiliza la función `write` para añadir una cadena específica ("Esto es un contenido desde python") al archivo. Finalmente, cierra el archivo con la función `close`, lo cual es importante porque asegura que todos los cambios se guardan correctamente y libera recursos del sistema.

Este tipo de operaciones son fundamentales en programación ya que permiten almacenar datos permanentemente en archivos para su uso posterior o compartición.

`001-flujo de caracteres.py`

```python
archivo = open("clientes.txt",'w')
archivo.write("Esto es un contenido desde python")
archivo.close()
```

### leer
<small>Creado: 2025-10-02 15:15</small>

#### Explicación

Este código Python te enseña cómo abrir y leer el contenido de un archivo. Primero, se abre el archivo llamado "clientes.txt" en modo lectura ('r'). Luego, lee la primera línea del archivo utilizando la función `readline()`, que devuelve una cadena con los caracteres desde el comienzo del archivo hasta el primer salto de línea encontrado. Finalmente, imprime esa línea y cierra el archivo para asegurar que todos los cambios se guarden correctamente y liberar recursos del sistema.

Es importante entender este proceso porque te permite interactuar con archivos de texto en Python, lo cual es fundamental cuando necesitas manipular datos almacenados en archivos o analizar información externa.

`002-leer.py`

```python
archivo = open("clientes.txt",'r')
linea = archivo.readline()
print(linea)
archivo.close()
```

### uso de pickle para binario
<small>Creado: 2025-10-02 15:18</small>

#### Explicación

Este fragmento de código muestra cómo guardar una cadena de texto en un archivo binario utilizando el módulo `pickle` en Python. El programa comienza importando el módulo `pickle`, que es útil para serializar y deserializar objetos de Python a formatos binarios y viceversa.

Luego, se define una variable llamada `mensaje` con el texto "esto es un mensaje". A continuación, se abre un archivo binario llamado `"cliente.bin"` en modo escritura binaria (`'wb'`). Este modo de apertura del archivo es importante porque indica que vamos a escribir datos binarios y no simples caracteres.

Finalmente, la función `pickle.dump()` se utiliza para guardar el contenido de la variable `mensaje` en el archivo recién creado. La última línea cierra el archivo después de haber guardado los datos para asegurar que todos los cambios han sido escritos correctamente y liberar cualquier recurso asociado al archivo.

Este tipo de operaciones es importante porque permite almacenar objetos complejos, como listas, diccionarios o incluso clases personalizadas, en archivos de manera eficiente, lo cual puede ser muy útil para guardar estados de la aplicación entre sesiones.

`003-uso de pickle para binario.py`

```python
import pickle

mensaje = "esto es un mensaje"
archivo = open("cliente.bin",'wb')

pickle.dump(mensaje, archivo)
archivo.close()
```

### pickle para leer
<small>Creado: 2025-10-02 15:19</small>

#### Explicación

Este fragmento de código está utilizando la biblioteca `pickle` en Python para leer datos serializados desde un archivo binario. Primero, el programa abre el archivo llamado "cliente.bin" en modo de lectura binaria (`'rb'`). Luego, utiliza la función `pickle.load()` para cargar los datos almacenados en este archivo y los almacena en una variable llamada `mensaje`. Finalmente, imprime el contenido de `mensaje` en la consola. Este proceso es importante porque permite recuperar objetos complejos creados previamente (como listas, diccionarios, etc.) directamente desde un archivo binario, facilitando así la persistencia y manipulación de datos estructurados en Python.

`004-pickle para leer.py`

```python
import pickle

archivo = open("cliente.bin",'rb')

mensaje = pickle.load(archivo)
print(mensaje)
archivo.close()
```

### clientes
<small>Creado: 2025-10-02 15:14</small>

#### Explicación

El fragmento que has proporcionado no contiene realmente código Python; en su lugar, parece ser una simple cadena de texto. Esta línea indica que hay un comentario o un string (cadena de caracteres) que dice "Esto es un contenido desde python". En el contexto de archivos de programa, este tipo de texto podría aparecer como un ejemplo inicial o como un marcador para señalar dónde debería ir el código real en una plantilla. No realiza ninguna acción y su función principal sería proporcionar información al desarrollador sobre qué se espera que contenga ese archivo.

En el caso de un ejercicio relacionado con la lectura y escritura de archivos, este texto podría ser simplemente una nota para indicar que el objetivo es reemplazar esta línea con código real que lea o escriba en un archivo. Es importante entender que mientras que esta línea no ejecuta ninguna operación funcional dentro del programa, puede desempeñar un papel crucial en la organización y documentación del proyecto.

`clientes.txt`

```
Esto es un contenido desde python
```

### Actividades propuestas

### Actividades Propuestas:

1. **Lectura y Escritura Básica**
   - **Descripción:** Los estudiantes deben escribir y luego leer de un archivo de texto sin usar bibliotecas adicionales. El objetivo es que comprendan cómo interactuar con archivos en Python.

2. **Manipulación de Archivos en Modo Lectura**
   - **Descripción:** Se requiere que los alumnos lean el contenido completo del archivo `clientes.txt` y lo muestren por pantalla línea a línea. La actividad busca mejorar sus habilidades en manejo de archivos en modo lectura.

3. **Uso de Pickle para Serialización**
   - **Descripción:** Los estudiantes deben serializar un diccionario personalizado en formato binario usando el módulo `pickle` y luego guardarlo en un archivo `.bin`. Esta actividad ayuda a entender la importancia de la serialización.

4. **Lectura desde Archivos Binarios**
   - **Descripción:** Se pide que los alumnos levan contenido previamente serializado con pickle desde un archivo binario, mostrándolo por pantalla. Busca familiarizarlos con lecturas binarias en Python.

5. **Manejo de Excepciones con Archivos**
   - **Descripción:** Los estudiantes deben añadir manejo de excepciones para la apertura y cierre de archivos, aprendiendo a gestionar errores comunes como la falta de existencia del archivo o problemas durante la escritura/lectura.

6. **Escribir y Leer Información Compleja**
   - **Descripción:** Los alumnos deben escribir una estructura compleja (como una lista de diccionarios) en un archivo de texto, luego leerla y mostrarla por pantalla para validar su contenido. La actividad busca mejorar la habilidad para manejar datos estructurados.

7. **Escritura y Lectura Binaria Avanzada**
   - **Descripción:** Se pide que los estudiantes escriban e implementen una función para serializar/deserializar objetos personalizados en archivos binarios usando `pickle`, mejorando su comprensión de serialización avanzada.

8. **Generación Automática de Archivos**
   - **Descripción:** Los alumnos deben crear un script que genere automáticamente varios archivos `.txt` con contenido específico (como nombres y correos electrónicos), para practicar la automatización en manejo de archivos.

9. **Lectura y Procesamiento de Datos JSON**
   - **Descripción:** Se requiere que los estudiantes escriban un script para leer datos desde un archivo `.json` y luego manipularlos (por ejemplo, contar cuántas entradas hay), introduciendo el formato JSON en su arsenal.

10. **Comparación de Contenidos entre Archivos**
    - **Descripción:** Los alumnos deben crear una función que compare el contenido de dos archivos textuales identificados por el usuario y reporte cualquier diferencia encontrada, mejorando sus habilidades en procesamiento y comparación de datos.


<a id="ficheros-de-datos-registros"></a>
## Ficheros de datos. Registros

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/002-Ficheros%20de%20datos.%20Registros)

### Introducción a los ejercicios

Este es un proyecto de una aplicación de agenda de clientes en Python, que ha evolucionado significativamente a lo largo del desarrollo. Aquí hay un resumen de las principales características y mejoras:

1. Estructura inicial:
   - Clase Cliente básica con atributos nombre, apellidos y email.
   - Menú principal con opciones para insertar, listar, actualizar, eliminar y guardar clientes.

2. Persistencia de datos:
   - Usando el módulo pickle para guardar la lista de clientes en un archivo binario "clientes.bin" al salir y cargarlo al inicio.

3. Mejora estética:
   - Funciones para limpiar pantalla (limpiaPantalla()), poner negrita (ponNegrita()) y reiniciar estilo (reiniciaEstilo()).
   - Colores ANSI para resaltar opciones en el menú.

4. Separación de responsabilidades:
   - Definición de funciones separadas para tareas específicas como limpiar pantalla y aplicar estilos.

5. Manejo de archivos externos:
   - Archivos CSV (clientes.csv) y JSON (clientes.json) que podrían ser utilizados para cargar datos adicionales o exportar la base de clientes.

6. Estado actual:
   - El código final en archivo 015-funciones.py implementa una interfaz con colores, negrita y limpieza de pantalla.
   - Las opciones actualizar y eliminar no están implementadas completamente aún.

7. Posibles mejoras futuras:
   - Implementar funcionalidades para actualizar y eliminar clientes.
   - Añadir opciones para importar/exportar datos a partir de archivos CSV o JSON.
   - Mejorar la interfaz (por ejemplo, usando ANSI para marcar campos requeridos).
   - Agregar validaciones más robustas en las entradas del usuario.

Este proyecto muestra un buen desarrollo progresivo de una aplicación simple pero funcional, con mejoras estéticas y estructurales a lo largo del camino.

### escribir un txt
<small>Creado: 2025-10-02 15:21</small>

#### Explicación

Este código Python se utiliza para escribir información en un archivo de texto llamado "clientes.txt". Primero, el programa abre el archivo en modo escritura ('w'), lo que significa que cualquier contenido existente en el archivo será borrado y se preparará para recibir nueva información. Luego, escribe la frase "Esto es un contenido desde python" dentro del archivo recién abierto. Finalmente, cierra el archivo para asegurarse de que toda la información haya sido guardada correctamente.

Es importante destacar que al abrir un archivo en modo escritura ('w'), cualquier dato previo en ese archivo será eliminado. Si deseas agregar contenido a un archivo existente sin borrar su contenido anterior, debes usar otro modo de apertura, como 'a' (append) para añadir información al final del archivo sin eliminar el contenido ya presente.

`001-escribir un txt.py`

```python
archivo = open("clientes.txt",'w')
archivo.write("Esto es un contenido desde python")
archivo.close()
```

### escribir un csv
<small>Creado: 2025-10-02 15:23</small>

#### Explicación

Este código Python te enseña cómo escribir información en un archivo CSV (separado por comas). En este caso, el programa abre el archivo llamado "clientes.csv" en modo de escritura adicional ('a'). Esto significa que si el archivo ya existe, el nuevo contenido se añadirá al final del archivo existente. Si no existe, Python lo creará.

Luego, el código escribe dos líneas de información sobre clientes en el archivo. Cada línea contiene un nombre, una dirección y un número (posiblemente un teléfono). Por ejemplo, la primera línea representa a Juan con su dirección y número telefónico.

Finalmente, se cierra el archivo para asegurarse de que toda la información se guarda correctamente y para liberar los recursos del sistema.

Este código es importante porque te muestra cómo interactuar con archivos en Python, lo cual es fundamental para almacenar y recuperar datos persistentes en tus aplicaciones.

`002-escribir un csv.py`

```python
archivo = open("clientes.csv",'a')
archivo.write("Juan,Calle de Juan,5325434\n")
archivo.write("Jorge,Calle de Jorge,5234535\n")
archivo.close()
```

### creo un diccionario y lo guardo como json
<small>Creado: 2025-10-02 15:28</small>

#### Explicación

Este fragmento de código en Python tiene como objetivo guardar una lista de clientes en un archivo JSON. Primero, importamos el módulo `json`, que nos proporciona funciones para trabajar con datos en formato JSON.

Luego, creamos una lista llamada `clientes` que contiene dos diccionarios. Cada diccionario representa a un cliente y tiene tres claves: "nombre", "apellidos" y "email". Estos diccionarios almacenan información sobre cada uno de los clientes, como su nombre completo y correo electrónico.

El siguiente paso es abrir el archivo `clientes.json` en modo escritura (`"w"`). Si el archivo ya existe, será sobrescrito. Si no existe, se creará un nuevo archivo con ese nombre.

Finalmente, utilizamos la función `json.dump()` para escribir la lista de clientes en el archivo que acabamos de abrir. La opción `indent=4` añade sangrías a los datos JSON para hacerlos más legibles, y `ensure_ascii=False` asegura que caracteres no ASCII (como acentos) se guarden correctamente sin ser convertidos.

Este código es importante porque nos permite almacenar información estructurada de una manera fácilmente accesible y modificable en el futuro. Al guardar los datos como JSON, podemos recuperarlos fácilmente para realizar consultas o hacer actualizaciones a la base de datos de clientes más adelante.

`003-creo un diccionario y lo guardo como json.py`

```python
import json

clientes = [
  {
    "nombre":"jose Vicente",
    "apellidos":"Carratala Sanchis",
    "email":"info@jocarsa.com"
  },
  {
    "nombre":"Juan",
    "apellidos":"Garcia Lopez",
    "email":"juan@jocarsa.com"
  }
]

archivo = open("clientes.json","w")

json.dump(clientes, archivo, indent=4, ensure_ascii=False)
```

### agenda de clientes
<small>Creado: 2025-10-02 15:31</small>

#### Explicación

Este código es el inicio de un programa en Python llamado "Agenda de clientes", que se utiliza para gestionar información sobre diferentes clientes. El programa presenta al usuario un menú con varias opciones, como insertar, listar, actualizar y eliminar clientes.

Cuando ejecutas este código, primero aparece en la pantalla un mensaje que indica el nombre del programa: "Agenda de clientes". Luego, muestra un menú interactivo que ofrece cuatro opciones a elegir. El usuario debe ingresar un número correspondiente a la acción que desea realizar (1 para insertar un cliente, 2 para listar todos los clientes, etc.). El programa captura esta entrada mediante la función `input()`, la guarda en la variable `opcion` y después convierte el valor ingresado por el usuario de texto (string) a número entero usando `int(opcion)`.

Esta parte del código es fundamental porque establece cómo interactuará el usuario con el programa, permitiendo que realice diferentes acciones según lo que necesite.

`004-agenda de clientes.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

print("Agenda de clientes")

print("Selecciona una opcion:")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")
opcion = input("Selecciona una opcion")
opcion = int(opcion)
```

### actuar en cada caso
<small>Creado: 2025-10-02 15:32</small>

#### Explicación

Este fragmento de código es una pequeña aplicación en Python que permite gestionar una agenda de clientes. Primero, muestra un menú con cuatro opciones: insertar, listar, actualizar y eliminar clientes. Luego, pide al usuario que seleccione una opción introduciendo un número del 1 al 4.

El programa lee la entrada del usuario como texto (con `input()`) y luego convierte esa entrada a un número entero (con `int()`). Después de esto, el programa utiliza una estructura condicional `if-elif` para determinar qué acción realizar en función del número que ha seleccionado el usuario. Si se selecciona la opción 1, por ejemplo, se muestra un mensaje indicando que vamos a insertar un nuevo cliente.

Este código es importante porque establece la base de interacción entre el usuario y el programa, permitiendo al usuario elegir qué acción desea realizar en relación con los datos de clientes. Es un paso fundamental para construir aplicaciones más complejas donde el usuario tiene opciones de manejo del dato.

`005-actuar en cada caso.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

print("Agenda de clientes")

print("Selecciona una opcion:")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")
opcion = input("Selecciona una opcion")
opcion = int(opcion)

if opcion == 1:
  print("Vamos a insertar un cliente")
elif opcion == 2:
  print("Vamos a listar los clientes")
elif opcion == 3:
  print("Vamos a actualizar los clientes")
elif opcion == 4:
  print("Vamos a eliminar clientes")
  
```

### para definir un cliente creo una clase
<small>Creado: 2025-10-02 15:34</small>

#### Explicación

Este código es el comienzo de una pequeña aplicación en Python que gestiona una agenda de clientes. La aplicación permite al usuario elegir entre varias acciones, como insertar un nuevo cliente, listar todos los clientes existentes, actualizar la información de un cliente o eliminar un cliente.

La clase `Cliente` se define para almacenar información básica sobre cada cliente, incluyendo su nombre, apellidos y correo electrónico. Sin embargo, en esta parte del código, no se está usando aún la clase `Cliente`.

El programa muestra al usuario una lista de opciones (insertar, listar, actualizar o eliminar clientes) e invita a introducir el número que corresponde con la acción deseada. El valor ingresado por el usuario se guarda en la variable `opcion` y luego se convierte en un entero para facilitar su uso en las comparaciones posteriores.

Dependiendo de la opción seleccionada, el programa imprime una frase correspondiente a la acción que va a realizar. Esto es solo una interfaz básica y no realiza ninguna operación real sobre los clientes todavía; en futuras partes del código se implementará la lógica para cada una de estas acciones.

Este tipo de estructura es común al inicio de aplicaciones interactivas, donde el usuario tiene diferentes opciones para manipular datos.

`006-para definir un cliente creo una clase.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""

print("Agenda de clientes")

print("Selecciona una opcion:")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")
opcion = input("Selecciona una opcion")
opcion = int(opcion)

if opcion == 1:
  print("Vamos a insertar un cliente")
elif opcion == 2:
  print("Vamos a listar los clientes")
elif opcion == 3:
  print("Vamos a actualizar los clientes")
elif opcion == 4:
  print("Vamos a eliminar clientes")
```

### y creo una lista de clientes
<small>Creado: 2025-10-02 15:35</small>

#### Explicación

Este código es el comienzo de una pequeña aplicación en Python que permite gestionar una lista de clientes. La aplicación crea una clase llamada `Cliente` que define un objeto con tres atributos: nombre, apellidos y email. Estos atributos se inicializan vacíos cuando se crea un nuevo cliente.

Luego, el programa define una lista vacía llamada `clientes`, donde almacenará objetos del tipo `Cliente`. Después de esto, muestra un menú en pantalla que ofrece al usuario opciones para insertar, listar, actualizar o eliminar clientes. El usuario debe seleccionar una opción ingresando un número del 1 al 4.

Dependiendo de la opción elegida por el usuario, se imprime un mensaje correspondiente. Sin embargo, este código solo muestra los mensajes y no realiza ninguna acción real con los datos de los clientes todavía. La intención es que en versiones posteriores del programa se añadan funciones para manejar cada una de estas operaciones.

Esta estructura básica es importante porque establece la base sobre la cual podrás construir funcionalidades más complejas, como la creación y manipulación de objetos `Cliente` dentro de la lista.

`007-y creo una lista de clientes.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""
    
clientes = []

print("Agenda de clientes")

print("Selecciona una opcion:")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")
opcion = input("Selecciona una opcion")
opcion = int(opcion)

if opcion == 1:
  print("Vamos a insertar un cliente")
elif opcion == 2:
  print("Vamos a listar los clientes")
elif opcion == 3:
  print("Vamos a actualizar los clientes")
elif opcion == 4:
  print("Vamos a eliminar clientes")
```

### añado un elemento a la lista
<small>Creado: 2025-10-02 15:37</small>

#### Explicación

Este fragmento de código es una parte de un programa llamado "Agenda de clientes" que gestiona información sobre diferentes personas. El código comienza definiendo una clase llamada `Cliente`, la cual contiene tres atributos importantes: nombre, apellidos y email. Estos atributos se inicializan vacíos cuando se crea un nuevo objeto del tipo cliente.

Después, el programa crea una lista vacía llamada `clientes` donde almacenará todos los objetos de clientes que se creen. Luego, muestra al usuario un menú con cuatro opciones: insertar un cliente, listar clientes, actualizar clientes y eliminar clientes. El usuario debe seleccionar una opción escribiendo un número del 1 al 4.

Si el usuario elige la primera opción (insertar un cliente), el programa pide al usuario que introduzca el nombre, apellidos y email de un nuevo cliente. Estos datos se asignan a los atributos correspondientes de un objeto `Cliente` recién creado. Finalmente, este objeto se añade a la lista `clientes`.

Este código es importante porque muestra cómo manejar objetos en Python y cómo utilizar listas para almacenar colecciones de estos objetos. Además, ilustra el uso de menús interactivos con los usuarios y las diferentes formas de gestionar datos en un programa simple pero funcional.

`008-añado un elemento a la lista.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""
    
clientes = []

print("Agenda de clientes")

print("Selecciona una opcion:")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")
opcion = input("Selecciona una opcion")
opcion = int(opcion)

if opcion == 1:
  print("Vamos a insertar un cliente")
  nuevocliente = Cliente()
  nuevocliente.nombre = input("Indica el nombre del cliente: ")
  nuevocliente.apellidos = input("Indica los apellidos del cliente: ")
  nuevocliente.email = input("Indica el email del cliente: ")
  clientes.append(nuevocliente) # a la lista de clientes le ponemos el nuevo cliente
elif opcion == 2:
  print("Vamos a listar los clientes")
elif opcion == 3:
  print("Vamos a actualizar los clientes")
elif opcion == 4:
  print("Vamos a eliminar clientes")
```

### Meto al usuario en un bucle infinito
<small>Creado: 2025-10-02 15:38</small>

#### Explicación

Este código es una pequeña aplicación en Python que permite gestionar una base de datos simple de clientes. El programa utiliza un bucle infinito (`while True`) para permitir al usuario interactuar con la lista de clientes hasta que decida salir del programa. Dentro del bucle, el programa muestra al usuario un menú con opciones como insertar, listar, actualizar y eliminar clientes.

Cuando el usuario selecciona una opción, el programa ejecuta las acciones correspondientes. Por ejemplo, si elige "Insertar un cliente", se crea una instancia de la clase `Cliente`, se solicitan los datos del nuevo cliente al usuario (nombre, apellidos, email), y luego esta información se añade a una lista global llamada `clientes`.

Es importante destacar que el código solo muestra la interfaz para seleccionar acciones pero no implementa completamente las funcionalidades de actualizar o eliminar clientes. Estas partes están reservadas para futuras implementaciones según parece.

Este tipo de estructura de programa es común en aplicaciones interactivas donde se necesita mantener un registro de datos y permitir operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre esos datos.

`009-Meto al usuario en un bucle infinito.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""
    
clientes = []

print("Agenda de clientes")
while True:
  print("Selecciona una opcion:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar clientes")
  print("4.-Eliminar clientes")
  opcion = input("Selecciona una opcion")
  opcion = int(opcion)

  if opcion == 1:
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Indica el nombre del cliente: ")
    nuevocliente.apellidos = input("Indica los apellidos del cliente: ")
    nuevocliente.email = input("Indica el email del cliente: ")
    clientes.append(nuevocliente) # a la lista de clientes le ponemos el nuevo cliente
  elif opcion == 2:
    print("Vamos a listar los clientes")
  elif opcion == 3:
    print("Vamos a actualizar los clientes")
  elif opcion == 4:
    print("Vamos a eliminar clientes")
```

### listamos clientes
<small>Creado: 2025-10-02 15:41</small>

#### Explicación

Este código es una simple interfaz de línea de comandos para gestionar una lista de clientes. Comienza creando una clase llamada `Cliente`, que tiene tres atributos: nombre, apellidos y email. La variable `clientes` es una lista vacía donde se almacenará cada objeto cliente creado.

El programa entra en un bucle infinito (`while True:`) que muestra un menú de opciones al usuario para interactuar con la base de datos de clientes. Las opciones disponibles son insertar, listar, actualizar y eliminar clientes. Cuando el usuario selecciona una opción, el programa realiza la acción correspondiente:

- Si se selecciona "1.-Insertar un cliente", el código crea una nueva instancia de `Cliente`, solicita al usuario que introduzca los detalles del nuevo cliente (nombre, apellidos y email), y luego agrega esta nueva instancia a la lista `clientes`.
  
- Si se selecciona "2.-Listar clientes", el programa recorre la lista `clientes` e imprime en pantalla la información de cada cliente.

Las opciones para actualizar y eliminar clientes están implementadas pero no tienen código que las complete. Esto significa que, aunque muestran mensajes indicando qué deberían hacer, aún falta programar la lógica para permitir a los usuarios modificar o borrar registros existentes.

Este tipo de programa es útil en escenarios donde se necesita mantener una base de datos simple y fácil de usar desde la línea de comandos.

`010-listamos clientes.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""
    
clientes = []

print("Agenda de clientes")
while True:
  print("Selecciona una opcion:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar clientes")
  print("4.-Eliminar clientes")
  opcion = input("Selecciona una opcion")
  opcion = int(opcion)

  if opcion == 1:
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Indica el nombre del cliente: ")
    nuevocliente.apellidos = input("Indica los apellidos del cliente: ")
    nuevocliente.email = input("Indica el email del cliente: ")
    clientes.append(nuevocliente) # a la lista de clientes le ponemos el nuevo cliente
  elif opcion == 2:
    print("Vamos a listar los clientes")
    for cliente in clientes:
      print("Nombre: ",cliente.nombre)
      print("Apellidos: ",cliente.apellidos)
      print("Email: ",cliente.email)
      print("##############################")
  elif opcion == 3:
    print("Vamos a actualizar los clientes")
  elif opcion == 4:
    print("Vamos a eliminar clientes")
```

### limpiar la pantalla
<small>Creado: 2025-10-02 15:46</small>

#### Explicación

Este código es un programa sencillo en Python que gestiona una base de datos básica de clientes. El programa utiliza una clase llamada `Cliente` para almacenar información sobre cada cliente, como su nombre, apellidos y correo electrónico. La lista `clientes` almacena objetos de la clase `Cliente`.

El programa entra en un bucle infinito (`while True:`) que muestra un menú con cuatro opciones: insertar un nuevo cliente, listar todos los clientes existentes, actualizar información de un cliente y eliminar un cliente.

Una característica importante es cómo se limpia la pantalla al principio de cada iteración del bucle y antes de mostrar cada opción. Esto ayuda a mantener una interfaz de usuario clara y legible. La secuencia `\033[2J\033[H`, que se imprime sin saltar línea (`end=""`), es un comando de escape que limpia la pantalla del terminal y coloca el cursor en la posición inicial.

Al seleccionar la opción 1, el programa crea una instancia nueva de `Cliente`, solicita al usuario los detalles del cliente (nombre, apellidos, correo electrónico) y luego añade este nuevo cliente a la lista `clientes`.

Si se selecciona la opción 2, se imprimen en pantalla todos los clientes almacenados en la lista, mostrando el nombre, apellidos y email de cada uno. Después de mostrar esta información, el programa solicita al usuario que presione una tecla antes de continuar.

Las opciones 3 y 4 están implementadas pero no tienen lógica asociada todavía (solo indican qué se haría si estuvieran completas), lo que sugiere que aún faltan detalles por añadir para permitir la actualización y eliminación de clientes.

`011-limpiar la pantalla.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""
    
clientes = []
print("\033[2J\033[H", end="")
print("Agenda de clientes")
while True:
  print("\033[2J\033[H", end="")
  print("Selecciona una opcion:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar clientes")
  print("4.-Eliminar clientes")
  opcion = input("Selecciona una opcion: ")
  opcion = int(opcion)

  if opcion == 1:
    print("\033[2J\033[H", end="")
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Indica el nombre del cliente: ")
    nuevocliente.apellidos = input("Indica los apellidos del cliente: ")
    nuevocliente.email = input("Indica el email del cliente: ")
    clientes.append(nuevocliente) # a la lista de clientes le ponemos el nuevo cliente
  elif opcion == 2:
    print("\033[2J\033[H", end="")
    print("Vamos a listar los clientes")
    print("Listado de clientes:")
    print("##############################")
    for cliente in clientes:
      print("Nombre: ",cliente.nombre)
      print("Apellidos: ",cliente.apellidos)
      print("Email: ",cliente.email)
      print("##############################")
    input("Pulsa una tecla para continuar....")
  elif opcion == 3:
    print("Vamos a actualizar los clientes")
  elif opcion == 4:
    print("Vamos a eliminar clientes")
```

### guardar clientes
<small>Creado: 2025-10-02 15:48</small>

#### Explicación

Este fragmento de código es un programa en Python que gestiona una agenda de clientes. El programa permite al usuario interactuar con los datos de los clientes a través de varias opciones: insertar, listar, actualizar y eliminar registros, además de guardar la lista completa de clientes en un archivo binario.

El código comienza importando el módulo `pickle`, que es útil para serializar objetos Python. Luego, se define una clase llamada `Cliente` con atributos como nombre, apellidos y email. A continuación, se crea una lista vacía llamada `clientes` donde almacenarán los objetos de tipo cliente.

El programa entra en un bucle infinito (`while True:`) que muestra al usuario un menú interactivo para seleccionar entre las diferentes operaciones disponibles. Cuando el usuario elige la opción 5 (guardar clientes), se abre un archivo binario llamado `clientes.bin` en modo escritura binaria y se utiliza `pickle.dump()` para guardar la lista de objetos `Cliente` en ese archivo.

La función de guardar los datos es importante porque permite que la información persista más allá de las ejecuciones del programa, permitiendo a los usuarios acceder a ella en sesiones futuras. Utilizar el módulo `pickle` para este propósito asegura que los objetos complejos como instancias de clase se pueden almacenar y recuperar con precisión.

Este tipo de código es común en aplicaciones CRUD (Crear, Leer, Actualizar, Borrar) básicas y enseña conceptos fundamentales del manejo de archivos y clases en Python.

`012-guardar clientes.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

import pickle

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""
    
clientes = []
print("\033[2J\033[H", end="")
print("Agenda de clientes")
while True:
  print("\033[2J\033[H", end="")
  print("Selecciona una opcion:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar clientes")
  print("4.-Eliminar clientes")
  print("5.-Guardar clientes")
  opcion = input("Selecciona una opcion: ")
  opcion = int(opcion)

  if opcion == 1:
    print("\033[2J\033[H", end="")
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Indica el nombre del cliente: ")
    nuevocliente.apellidos = input("Indica los apellidos del cliente: ")
    nuevocliente.email = input("Indica el email del cliente: ")
    clientes.append(nuevocliente) # a la lista de clientes le ponemos el nuevo cliente
  elif opcion == 2:
    print("\033[2J\033[H", end="")
    print("Vamos a listar los clientes")
    print("Listado de clientes:")
    print("##############################")
    for cliente in clientes:
      print("Nombre: ",cliente.nombre)
      print("Apellidos: ",cliente.apellidos)
      print("Email: ",cliente.email)
      print("##############################")
    input("Pulsa una tecla para continuar....")
  elif opcion == 3:
    print("Vamos a actualizar los clientes")
  elif opcion == 4:
    print("Vamos a eliminar clientes")
  elif opcion == 5:
    print("Vamos a guardar los clientes")
    archivo = open("clientes.bin",'wb')
    pickle.dump(clientes, archivo)
    archivo.close()
    input("Pulsa una tecla para continuar...")
```

### cuando abro el programa carga la lista de clientes
<small>Creado: 2025-10-02 15:55</small>

#### Explicación

Este fragmento de código es un programa básico en Python que gestiona una base de datos de clientes. Al iniciar el programa, carga automáticamente la lista de clientes desde un archivo binario llamado `clientes.bin` utilizando el módulo `pickle`. El programa permite al usuario realizar diferentes acciones como insertar, listar, actualizar y eliminar clientes.

La clase `Cliente()` define los atributos básicos que cada cliente tiene: nombre, apellidos y email. La lista `clientes` es una colección de objetos de tipo `Cliente`.

El bucle `while True:` crea un menú interactivo en la consola donde el usuario puede seleccionar entre varias opciones para gestionar la información del cliente. Cuando se selecciona la opción 1 (insertar un cliente), se pide al usuario que introduzca los detalles del nuevo cliente y luego se añade este nuevo objeto `Cliente` a la lista `clientes`.

Para listar los clientes, el programa recorre cada objeto en la lista `clientes`, imprime sus atributos y espera a que el usuario pulse una tecla antes de volver al menú principal.

La opción 5 guarda cualquier cambio hecho en la lista de clientes volviéndola a guardar en el archivo binario `clientes.bin` utilizando nuevamente `pickle`.

Este tipo de programa es importante para entender cómo se manejan archivos externos, las estructuras de datos como listas y clases en Python, así como cómo implementar interfaces interactivas con el usuario.

`013-cuando abro el programa carga la lista de clientes.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

import pickle

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""

clientes = []

archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)
archivo.close()

print("\033[2J\033[H", end="")

while True:
  print("\033[2J\033[H", end="")
  print("\u001b[1mBold")
  print("Agenda de clientes")
  print("\u001b[0m")
  print("Selecciona una opcion:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar clientes")
  print("4.-Eliminar clientes")
  print("5.-Guardar clientes")
  opcion = input("Selecciona una opcion: ")
  opcion = int(opcion)

  if opcion == 1:
    print("\033[2J\033[H", end="")
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Indica el nombre del cliente: ")
    nuevocliente.apellidos = input("Indica los apellidos del cliente: ")
    nuevocliente.email = input("Indica el email del cliente: ")
    clientes.append(nuevocliente) # a la lista de clientes le ponemos el nuevo cliente
  elif opcion == 2:
    print("\033[2J\033[H", end="")
    print("Vamos a listar los clientes")
    print("Listado de clientes:")
    print("##############################")
    for cliente in clientes:
      print("Nombre: ",cliente.nombre)
      print("Apellidos: ",cliente.apellidos)
      print("Email: ",cliente.email)
      print("##############################")
    input("Pulsa una tecla para continuar....")
  elif opcion == 3:
    print("Vamos a actualizar los clientes")
  elif opcion == 4:
    print("Vamos a eliminar clientes")
  elif opcion == 5:
    print("Vamos a guardar los clientes")
    archivo = open("clientes.bin",'wb')
    pickle.dump(clientes, archivo)
    archivo.close()
    input("Pulsa una tecla para continuar...")
```

### estetica de la consola
<small>Creado: 2025-10-02 15:56</small>

#### Explicación

Este código es un programa en Python que gestiona una base de datos simple de clientes. El programa carga los datos desde un archivo binario cuando se inicia y permite al usuario realizar operaciones básicas como insertar, listar, actualizar y eliminar registros de clientes.

El código comienza importando el módulo `pickle`, que se utiliza para guardar y cargar objetos en archivos binarios. Define una clase llamada `Cliente` con atributos para el nombre, apellidos y email del cliente. Luego, crea una lista vacía llamada `clientes`.

Cuando se inicia el programa, abre el archivo `"clientes.bin"` y carga la lista de clientes previamente guardados en esta lista. Para mejorar la usabilidad, el código utiliza comandos ANSI para limpiar la pantalla cada vez que muestra un nuevo menú o mensaje al usuario.

El programa entra en un bucle infinito (`while True`) donde muestra opciones al usuario (insertar, listar, actualizar, eliminar y guardar clientes) y actúa según la opción seleccionada. Si el usuario elige "guardar clientes", los datos se vuelven a serializar utilizando `pickle` y se guardan de nuevo en `"clientes.bin"`.

Este tipo de programa es útil para aprender cómo gestionar interfaces simples con Python, trabajar con archivos binarios y usar estructuras de datos como listas. Es una forma práctica de entender la persistencia de datos en aplicaciones de software.

`014-estetica de la consola.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

import pickle

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""

clientes = []

archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)
archivo.close()

print("\033[2J\033[H", end="")

while True:
  print("\033[2J\033[H", end="")  # Limpiar pantalla
  print("\u001b[1m")  # Negrita
  print("Agenda de clientes")
  print("\u001b[0m")  # Reiniciamos estilo
  print("Selecciona una opcion:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar clientes")
  print("4.-Eliminar clientes")
  print("5.-Guardar clientes")
  opcion = input("Selecciona una opcion: ")
  opcion = int(opcion)

  if opcion == 1:
    print("\033[2J\033[H", end="")
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Indica el nombre del cliente: ")
    nuevocliente.apellidos = input("Indica los apellidos del cliente: ")
    nuevocliente.email = input("Indica el email del cliente: ")
    clientes.append(nuevocliente) # a la lista de clientes le ponemos el nuevo cliente
  elif opcion == 2:
    print("\033[2J\033[H", end="")
    print("Vamos a listar los clientes")
    print("Listado de clientes:")
    print("##############################")
    for cliente in clientes:
      print("Nombre: ",cliente.nombre)
      print("Apellidos: ",cliente.apellidos)
      print("Email: ",cliente.email)
      print("##############################")
    input("Pulsa una tecla para continuar....")
  elif opcion == 3:
    print("Vamos a actualizar los clientes")
  elif opcion == 4:
    print("Vamos a eliminar clientes")
  elif opcion == 5:
    print("Vamos a guardar los clientes")
    archivo = open("clientes.bin",'wb')
    pickle.dump(clientes, archivo)
    archivo.close()
    input("Pulsa una tecla para continuar...")
```

### funciones
<small>Creado: 2025-10-02 16:03</small>

#### Explicación

Este fragmento de código es parte de un programa en Python que gestiona una agenda de clientes. El programa permite al usuario realizar varias operaciones como insertar nuevos clientes, listar todos los clientes registrados, actualizar información y eliminar clientes. También incluye la opción de guardar los datos de los clientes en un archivo binario para mantenerlos persistentes entre diferentes sesiones del programa.

El código comienza importando el módulo `pickle` que se utiliza para serializar y deserializar objetos Python. Se define una clase llamada `Cliente`, la cual contiene atributos como nombre, apellidos y email. Luego, varias funciones son declaradas para manipular la pantalla: `limpiaPantalla()` limpia la pantalla del terminal, mientras que `ponNegrita()`, `reiniciaEstilo()` y `ponColor(r,b,g)` permiten formatear el texto con diferentes estilos y colores.

El programa carga una lista de clientes desde un archivo binario llamado "clientes.bin" usando `pickle.load()`. Después de cargar los datos, entra en un bucle infinito que muestra al usuario un menú interactivo para seleccionar la operación a realizar. Dependiendo de la opción elegida por el usuario, se ejecuta una acción específica: insertar un nuevo cliente, listar todos los clientes existentes, actualizar información (esta función está incompleta), eliminar clientes y guardar los cambios realizados en el archivo "clientes.bin".

Este código es importante porque enseña cómo manejar datos complejos a través de archivos binarios, interactividad con el usuario mediante menús y la utilización de clases para organizar datos.

`015-funciones.py`

```python
'''
  Agenda de clientes v.0.1 por Jose Vicente Carratala
  Este programa gestiona y mantiene una base de datos de clientes
'''

import pickle

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""

def limpiaPantalla():
  print("\033[2J\033[H", end="")  # Limpiar pantalla

def ponNegrita():
  print("\u001b[1m")  # Negrita
  
def reiniciaEstilo():
  print("\u001b[0m")  # Reiniciamos estilo

def ponColor(r,b,g):
  print("\u001b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m", end="")

clientes = []

archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)
archivo.close()

limpiaPantalla()

while True:
  limpiaPantalla()
  ponNegrita()
  ponColor(255,0,0)
  print("Agenda de clientes")
  reiniciaEstilo()
  print("Selecciona una opcion:")
  ponColor(255,0,0)
  print("1.-Insertar un cliente")
  ponColor(0,255,0)
  print("2.-Listar clientes")
  ponColor(0,0,255)
  print("3.-Actualizar clientes")
  ponColor(255,255,0)
  print("4.-Eliminar clientes")
  ponColor(0,255,255)
  print("5.-Guardar clientes")
  opcion = input("Selecciona una opcion: ")
  opcion = int(opcion)

  if opcion == 1:
    limpiaPantalla()
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Indica el nombre del cliente: ")
    nuevocliente.apellidos = input("Indica los apellidos del cliente: ")
    nuevocliente.email = input("Indica el email del cliente: ")
    clientes.append(nuevocliente) # a la lista de clientes le ponemos el nuevo cliente
  elif opcion == 2:
    limpiaPantalla()
    print("Vamos a listar los clientes")
    print("Listado de clientes:")
    print("##############################")
    for cliente in clientes:
      print("Nombre: ",cliente.nombre)
      print("Apellidos: ",cliente.apellidos)
      print("Email: ",cliente.email)
      print("##############################")
    input("Pulsa una tecla para continuar....")
  elif opcion == 3:
    print("Vamos a actualizar los clientes")
  elif opcion == 4:
    print("Vamos a eliminar clientes")
  elif opcion == 5:
    print("Vamos a guardar los clientes")
    archivo = open("clientes.bin",'wb')
    pickle.dump(clientes, archivo)
    archivo.close()
    input("Pulsa una tecla para continuar...")
```

### clientes
<small>Creado: 2025-10-02 15:23</small>

#### Explicación

Este fragmento es un archivo CSV (Comma-Separated Values), que es un tipo común de formato de archivo usado para almacenar datos tabulares como hojas de cálculo. En este caso, el archivo contiene información sobre clientes y está guardado en la ruta `/var/www/html/dam2526/Primero/Programación/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/clientes.csv`.

Cada línea del archivo representa un registro o cliente con tres campos separados por comas: el nombre del cliente, la dirección y un número (que puede ser un teléfono o alguna otra identificación). El formato estándar para cada cliente es "nombre, dirección, número". Es importante notar que hay algunas líneas en blanco entre registros, lo cual no es necesario pero puede facilitar la lectura manual del archivo.

Este tipo de archivo es muy útil porque permite almacenar datos de manera simple y estructurada, y es fácilmente legible tanto por humanos como por programas informáticos. Los archivos CSV son comunes en aplicaciones de programación que manejan bases de datos sencillas o información tabular.

`clientes.csv`

```
Juan,Calle de Juan,5325434Jorge,Calle de Jorge,5234535Juan,Calle de Juan,5325434
Jorge,Calle de Jorge,5234535
```

### clientes
<small>Creado: 2025-10-02 15:28</small>

#### Explicación

Este fragmento de código es un archivo JSON que contiene una lista con información sobre clientes. En este caso, el archivo almacena dos registros o entradas de clientes, cada uno representado como un diccionario en Python.

Cada cliente tiene tres campos: "nombre", "apellidos" y "email". Estos campos contienen la información personal de cada cliente. El formato JSON es útil porque permite almacenar datos estructurados de una manera clara y fácilmente legible tanto por humanos como por máquinas. Es importante en el ámbito de la programación ya que facilita la transferencia y el almacenamiento de datos complejos, permitiendo a diferentes programas y sistemas intercambiar información de forma sencilla.

En este contexto del ejercicio, el archivo `clientes.json` sirve para guardar una lista persistente de clientes. Esto significa que cuando un programa lea este archivo, podrá recuperar la información de los clientes que ya han sido registrados, lo cual es muy útil en aplicaciones como bases de datos de clientes o registros de usuarios.

`clientes.json`

```json
[
    {
        "nombre": "jose Vicente",
        "apellidos": "Carratala Sanchis",
        "email": "info@jocarsa.com"
    },
    {
        "nombre": "Juan",
        "apellidos": "Garcia Lopez",
        "email": "juan@jocarsa.com"
    }
]
```

### Actividades propuestas

El código que has proporcionado es una evolución de un programa simple para gestionar la agenda de clientes. La versión final incluye:

1. **Lectura y Escritura con Pickle**: El programa carga los datos almacenados en `clientes.bin` al iniciar y guarda los cambios en el mismo archivo cuando se selecciona guardar.

2. **Funciones Personalizadas**: 
   - `limpiaPantalla()`: Limpia la pantalla de consola.
   - `ponNegrita()`: Cambia a negrita el texto en consola.
   - `reiniciaEstilo()`: Reinicia los estilos al valor por defecto.
   - `ponColor(r, g, b)`: Cambia el color del texto usando RGB.

3. **Interfaz de Usuario Mejorada**: 
   - La pantalla se limpia y refresca cada vez que cambias entre opciones.
   - Se usa negrita y colores para destacar las opciones en la consola.

4. **Carga y Almacenamiento en Ficheros Externos**:
   - Cuando el programa inicia, carga los datos previamente guardados desde `clientes.bin`.
   - Los cambios se almacenan de nuevo en `clientes.bin` cuando seleccionas guardar.

5. **Interacción con el Usuario**:
   - Muestra opciones para insertar, listar, actualizar y eliminar clientes.
   - Permite a los usuarios interactuar con la base de datos almacenada en memoria.

### Sugerencias de Mejora:

1. **Manejo de Errores**: Añadir control de errores para mejorar la robustez del programa (por ejemplo, manejar excepciones al leer o escribir archivos).
2. **Interfaz Avanzada**:
   - Agregar opciones para actualizar y eliminar clientes.
   - Mejorar la interfaz con colores y estilos más detallados.
3. **Validación de Datos**: Asegurarse de que los datos ingresados por el usuario sean válidos antes de guardarlos (por ejemplo, verificar si un correo electrónico tiene formato correcto).
4. **Persistencia en CSV o JSON**:
   - Opcionalmente, puedes implementar la opción para exportar a otros formatos como `clientes.csv` y `clientes.json`.

### Ejemplo de Mejora:

Aquí hay un ejemplo simple de cómo podrías mejorar el manejo de errores al cargar archivos binarios usando `try-except`:

```python
import pickle

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""

def limpiaPantalla():
  print("\033[2J\033[H", end="")  # Limpiar pantalla

def ponNegrita():
  print("\u001b[1m")  # Negrita
  
def reiniciaEstilo():
  print("\u001b[0m")  # Reiniciamos estilo

def ponColor(r,b,g):
  print("\u001b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m", end="")

clientes = []

try:
    archivo = open("clientes.bin",'rb')
    clientes = pickle.load(archivo)
    archivo.close()
except FileNotFoundError:
    print("No se encontró el archivo clientes.bin. Comenzando con una lista vacía.")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
finally:
    limpiaPantalla()

while True:
  # Tu lógica aquí
```

Esto asegura que si no existe `clientes.bin` o hay un error durante la carga, se maneja adecuadamente y sigue funcionando.


<a id="apertura-y-cierre-de-ficheros-modos-de-acceso-escritura-y-lectura-de-informacion-en-ficheros"></a>
## Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/003-Apertura%20y%20cierre%20de%20ficheros.%20Modos%20de%20acceso.%20Escritura%20y%20lectura%20de%20informaci%C3%B3n%20en%20ficheros)

### Introducción a los ejercicios

En esta carpeta, trabajamos con ejercicios que te enseñan a manipular archivos tanto en formato texto como binario utilizando Python. Se exploran diferentes modos de apertura y escritura de archivos para almacenar e interactuar con información estructurada o no estructurada. Además, aprenderás cómo guardar datos en un archivo XML y realizar operaciones básicas en una base de datos MySQL, incluyendo la inserción de nuevos registros a partir de la entrada del usuario. Estos ejercicios te ayudarán a dominar las habilidades fundamentales necesarias para manejar almacenamiento y recuperación de datos en entornos de programación realistas.

### apertura de escritura
<small>Creado: 2025-10-02 16:05</small>

#### Explicación

Este código Python se encarga de abrir un archivo llamado "clientes.txt" en modo escritura. Cuando se abre un archivo con el modo "w", lo que significa "write" (escritura), si el archivo ya existe, su contenido anterior será borrado y se creará una nueva versión vacía del mismo. Si el archivo no existe, Python lo crea automáticamente.

Luego de abrir el archivo, el código escribe la frase "Información de cliente" dentro del archivo recién abierto o creado. Esta línea añade texto al archivo que acabamos de abrir.

Finalmente, se cierra el archivo utilizando la función `archivo.close()`. Es importante cerrar los archivos después de trabajar con ellos para asegurarse de que todos los cambios sean guardados y para liberar cualquier recurso del sistema operativo que pueda estar siendo utilizado por este archivo. Esto es crucial para evitar problemas como pérdida de datos o colisiones entre diferentes programas que intenten acceder al mismo archivo.

`001-apertura de escritura.py`

```python
archivo = open("clientes.txt","w")
archivo.write("Información de cliente")
archivo.close()
```

### apertura de apendizaje
<small>Creado: 2025-10-02 16:05</small>

#### Explicación

Este fragmento de código se enfoca en la manipulación de archivos en Python, específicamente en la apertura y escritura de información en un archivo existente. La línea `archivo = open("clientes.txt", "a")` abre el archivo llamado "clientes.txt" en modo de apendizaje ("a"), lo que significa que cualquier texto nuevo que escribas será añadido al final del archivo sin borrar el contenido previo.

Luego, la línea `archivo.write("Información de cliente")` escribe una cadena de texto específica, "Información de cliente", dentro del archivo que acabamos de abrir. Esta información se agrega al final del archivo existente gracias a que utilizamos el modo de apertura en modo apendizaje.

Finalmente, `archivo.close()` cierra el archivo después de haber completado todas las operaciones necesarias con él. Es fundamental cerrar los archivos una vez terminadas las tareas relacionadas para asegurar que todos los cambios se guardan correctamente y liberar recursos del sistema.

`002-apertura de apendizaje.py`

```python
archivo = open("clientes.txt","a")
archivo.write("Información de cliente")
archivo.close()
```

### bajada de linea
<small>Creado: 2025-10-02 16:07</small>

#### Explicación

Este fragmento de código en Python se utiliza para escribir información en un archivo existente llamado "clientes.txt". Primero, el programa abre el archivo en modo de append ("a"), lo que significa que cualquier texto nuevo será añadido al final del archivo sin borrar lo que ya está allí. Luego, usa la función `write` para agregar una línea que dice "Información de cliente" seguida de un salto de línea (\n), asegurando así que el siguiente texto escrito comenzará en una nueva línea. Finalmente, cierra el archivo con `close()` para guardar los cambios y liberar cualquier recurso asociado al archivo.

Esta técnica es importante porque permite añadir información incrementalmente a archivos existentes sin necesidad de sobrescribir todo el contenido previo, lo que es muy útil cuando se registra datos en un sistema.

`003-bajada de linea.py`

```python
archivo = open("clientes.txt","a")
archivo.write("Información de cliente \n")
archivo.close()
```

### abrir archivo para leer UNA linea
<small>Creado: 2025-10-02 16:08</small>

#### Explicación

Este código en Python te enseña cómo abrir un archivo existente llamado "clientes.txt" en modo de lectura y luego leer una línea específica del archivo. Primero, se usa la función `open()` para abrir el archivo en modo de lectura ("r"), lo que permite acceder a su contenido pero no permitir cambios en él. A continuación, la función `readline()` lee la primera línea del archivo recién abierto y almacena esa línea en la variable `linea`. Finalmente, se imprime el contenido de `linea`, mostrando así la primera línea del archivo "clientes.txt" en la consola.

Es importante cerrar el archivo después de leer su contenido para liberar los recursos del sistema que estaban siendo utilizados por el programa. Esto se hace con la función `close()`. El manejo adecuado de archivos es crucial para prevenir problemas como pérdida de datos o colapsos en sistemas donde se gestionan muchos archivos simultáneamente.

Este fragmento de código demuestra cómo interactuar con ficheros de texto existentes y extraer información específica, una habilidad fundamental en programación.

`004-abrir archivo para leer UNA linea.py`

```python
archivo = open("clientes.txt","r")
linea = archivo.readline()
print(linea)
archivo.close()
```

### ahora quiero leer todas las lineas
<small>Creado: 2025-10-02 16:09</small>

#### Explicación

Este código Python se utiliza para leer todas las líneas de un archivo llamado "clientes.txt". Comienza abriendo el archivo en modo lectura ("r"), lo que significa que solo puedes ver los datos y no modificarlos. Luego, la función `readlines()` lee cada línea del archivo y las almacena en una lista llamada `linea`. Finalmente, imprime esta lista de líneas en la consola para que puedas visualizar el contenido del archivo. Al finalizar estas operaciones, se cierra el archivo con `archivo.close()` para liberar los recursos.

Es importante cerrar un archivo después de usarlo porque mantener archivos abiertos puede consumir memoria y otros recursos valiosos del sistema. Además, leer todas las líneas a la vez es una buena práctica cuando sabes que el archivo no es muy grande y necesitas procesarlo línea por línea en el futuro.

`005-ahora quiero leer todas las lineas.py`

```python
archivo = open("clientes.txt","r")
linea = archivo.readlines()
print(linea)
archivo.close()
```

### recorro la lista
<small>Creado: 2025-10-02 16:10</small>

#### Explicación

Este código Python abre un archivo llamado `clientes.txt` en modo lectura (`"r"`), lo que significa que solo va a leer el contenido del archivo. Luego, utiliza la función `readlines()` para leer todas las líneas del archivo y almacenarlas en una lista llamada `lineas`. Cada elemento de esta lista es una línea completa del archivo.

A continuación, el código itera sobre cada elemento de la lista `lineas` usando un bucle `for`, imprimiendo cada línea en pantalla con la función `print()`. Esto permite visualizar todo el contenido del archivo `clientes.txt` linea por linea. Finalmente, cierra el archivo para liberar los recursos del sistema que estaba utilizando.

Es importante cerrar archivos después de haber terminado de leerlos o escribir en ellos para evitar problemas de acceso y garantizar que todos los cambios se hayan guardado correctamente.

`006-recorro la lista.py`

```python
archivo = open("clientes.txt","r")
lineas = archivo.readlines()
for linea in lineas:
  print(linea)
archivo.close()
```

### escribo en modo binario
<small>Creado: 2025-10-02 16:12</small>

#### Explicación

Este código Python realiza la apertura y escritura en un archivo llamado "clientes.txt" utilizando el modo binario. Primero, se abre el archivo en modo escritura binaria ("wb"), lo que significa que cualquier contenido existente en el archivo será borrado si ya existe. Luego, se escribe una cadena de texto "Información de cliente", pero antes de escribirla en el archivo, la cadena se codifica en formato UTF-8 para convertirla en bytes apropiados para el almacenamiento binario. Finalmente, se cierra el archivo para asegurarse de que toda la información haya sido escrita y los recursos del sistema estén disponibles nuevamente.

La utilización del modo binario es importante cuando se trabaja con datos no textuales o cuando es necesario garantizar una representación exacta en bytes sin interpretar caracteres especiales o codificaciones.

`007-escribo en modo binario.py`

```python
archivo = open("clientes.txt","wb")
archivo.write("Información de cliente".encode("utf-8"))
archivo.close()
```

### leo de un archivo binario
<small>Creado: 2025-10-02 16:13</small>

#### Explicación

Este fragmento de código en Python se utiliza para leer información desde un archivo binario y mostrarla en pantalla. En primer lugar, el programa abre un archivo llamado "clientes.txt" en modo lectura binaria ("rb"). Esto significa que el archivo se manejará como si contuviera datos en formato binario (como imágenes o archivos de base de datos) en lugar de texto.

Luego, lee una línea del archivo utilizando la función `readline()`, lo cual es similar a leer una línea de un archivo normal, pero teniendo en cuenta que el contenido está en formato binario. Después de leer los bytes desde el archivo, el programa usa el método `decode("utf-8")` para convertir esos datos binarios en texto legible por humanos utilizando la codificación UTF-8.

Finalmente, imprime esa línea decodificada y cierra el archivo con `archivo.close()`. Es importante cerrar los archivos después de terminar de trabajar con ellos para liberar recursos del sistema.

`008-leo de un archivo binario.py`

```python
archivo = open("clientes.txt","rb")
linea = archivo.readline()
print(linea.decode("utf-8"))
archivo.close()
```

### guardar en formato xml
<small>Creado: 2025-10-02 16:15</small>

#### Explicación

Este código Python se utiliza para crear un archivo XML a partir de una lista de diccionarios que representan información sobre clientes. Primero, importa el módulo `xml.etree.ElementTree` que es útil para trabajar con archivos XML en Python.

El código define una lista llamada `clientes`, donde cada elemento de la lista es un diccionario que contiene los datos de un cliente, como nombre, apellidos y correo electrónico. Luego, crea un objeto raíz llamado "clientes" usando `ET.Element`.

A continuación, el código itera sobre cada cliente en la lista `clientes`. Para cada cliente, se crea un subelemento en el XML llamado "cliente". Dentro de este elemento "cliente", se crean tres subelementos adicionales: "nombre", "apellidos" y "email". Estos elementos toman los valores correspondientes del diccionario actual de la lista `clientes`.

Finalmente, el código crea un objeto `ElementTree` que encapsula todo el contenido XML. Utiliza la función `ET.indent()` para mejorar la legibilidad del archivo XML al agregar sangrías (espacios en blanco) donde es necesario. Por último, utiliza el método `write()` de `ElementTree` para guardar toda esta estructura XML en un archivo llamado "clientes.xml". El parámetro `encoding="utf-8"` asegura que el archivo se guarde con codificación UTF-8 y `xml_declaration=True` agrega la declaración XML al principio del archivo, lo cual es importante para indicar que el documento es un archivo XML válido.

Este tipo de código es útil cuando necesitas exportar datos estructurados en formato XML para uso en otros sistemas o aplicaciones.

`009-guardar en formato xml.py`

```python
import xml.etree.ElementTree as ET

clientes = [
    {
        "nombre": "jose Vicente",
        "apellidos": "Carratala Sanchis",
        "email": "info@jocarsa.com"
    },
    {
        "nombre": "Juan",
        "apellidos": "Garcia Lopez",
        "email": "juan@jocarsa.com"
    }
]

root = ET.Element("clientes")

for c in clientes:
    cliente = ET.SubElement(root, "cliente")
    ET.SubElement(cliente, "nombre").text = c["nombre"]
    ET.SubElement(cliente, "apellidos").text = c["apellidos"]
    ET.SubElement(cliente, "email").text = c["email"]

tree = ET.ElementTree(root)
ET.indent(tree, space="  ")
tree.write("clientes.xml", encoding="utf-8", xml_declaration=True)
```

### conexion rapida con bases de datos
<small>Creado: 2025-10-02 16:23</small>

#### Explicación

Este fragmento de código muestra cómo realizar una conexión rápida con una base de datos MySQL utilizando Python y luego recuperar información de ella. Primero, se importa el módulo `mysql.connector`, que es una herramienta para conectar a bases de datos MySQL desde Python.

Luego, se establece la conexión proporcionando detalles como el host (en este caso, localhost), el nombre del usuario con los permisos necesarios y la contraseña correspondiente, así como el nombre de la base de datos. Esto crea una conexión que permite interactuar con la base de datos especificada.

A continuación, se crea un objeto cursor a partir de esta conexión, que es un recurso fundamental para ejecutar consultas SQL y manipular resultados en Python. El código ejecuta una consulta SQL simple (`SELECT * FROM clientes`) para recuperar todos los registros del tablero 'clientes'. Los resultados obtenidos son almacenados en la variable `resultados`.

Finalmente, el código recorre cada fila de los resultados utilizando un bucle `for` y los imprime uno a uno. Es importante notar que después de terminar con el cursor y obtener todos los datos necesarios, se cierran tanto el cursor como la conexión para liberar recursos.

Este tipo de operaciones es crucial en aplicaciones web o cualquier sistema que requiera acceso rápido y seguro a bases de datos MySQL desde Python, permitiendo así la manipulación eficiente de grandes cantidades de información.

`010-conexion rapida con bases de datos.py`

```python
# pip install mysql-connector-python - Si estoy en Windows
# pip3 install mysql-connector-python - Si estoy en Linux o macOS

# Primero importo el conector
import mysql.connector
# Ahora establezco una conexión con un usuario con permisos
conexion = mysql.connector.connect(
    host="localhost",       # or IP of your MySQL server
    user="usuarioempresarial",      # replace with your MySQL user
    password="usuarioempresarial",  # replace with your MySQL password
    database="empresarial"       # replace with your database name
)
# Creo un cursor para pedir cosas
cursor = conexion.cursor()
# En el el cursor, ejecuto una petición
cursor.execute("SELECT * FROM clientes")
# Obtengo los resultados de la petición
resultados = cursor.fetchall()
# Como hay muchos resultados, voy uno a uno
for fila in resultados:
    print(fila)
# Cierro el cursor
cursor.close() 
# Cierro la conexion
conexion.close()
```

### Recojo información y la llevo a MySQL
<small>Creado: 2025-10-02 16:29</small>

#### Explicación

Este código en Python se utiliza para conectar a una base de datos MySQL y agregar nuevos registros en la tabla llamada `clientes`. Primero, el programa solicita al usuario que introduzca información sobre un cliente: nombre, apellidos, teléfono, email y localidad. Esta información es recogida mediante entradas del usuario.

Luego, se establece una conexión a la base de datos MySQL usando los detalles proporcionados (host, usuario, contraseña y nombre de la base de datos). Una vez que se ha conectado correctamente, el código crea un objeto cursor, que actúa como intermediario entre el programa y la base de datos. 

El fragmento ejecuta una sentencia SQL `INSERT INTO` para añadir los datos del cliente proporcionados por el usuario en la tabla `clientes`. Es importante destacar que cada campo en la tabla recibe su valor correspondiente desde las variables definidas anteriormente, con la excepción del primer campo (`NULL`) que probablemente representa un identificador automático generado por la base de datos.

Finalmente, se confirma la transacción para guardar los cambios y luego cierra tanto el cursor como la conexión a la base de datos. Este proceso es crucial para mantener la integridad de los datos en la base de datos MySQL y garantizar que toda la información proporcionada por el usuario sea almacenada correctamente.

`011-Recojo información y la llevo a MySQL.py`

```python
# pip install mysql-connector-python - Si estoy en Windows
# pip3 install mysql-connector-python - Si estoy en Linux o macOS


import mysql.connector

nombre = input("Introduce el nombre del cliente")
apellidos = input("Introduce los apellidos del cliente")
telefono = input("Introduce el telefono del cliente")
email = input("Introduce el email del cliente")
localidad = input("Introduce la localidad del cliente")

conexion = mysql.connector.connect(
    host="localhost",      
    user="usuarioempresarial",    
    password="usuarioempresarial",  
    database="empresarial"      
)

cursor = conexion.cursor()

cursor.execute('''
  INSERT INTO clientes
  VALUES (
    NULL,
    "'''+nombre+'''",
    "'''+apellidos+'''",
    "'''+telefono+'''",
    "'''+email+'''",
    "'''+localidad+'''"
  )
''')
conexion.commit()

cursor.close() 

conexion.close()
```

### clientes
<small>Creado: 2025-10-02 16:12</small>

#### Explicación

El fragmento "Información de cliente" no es un código en sí, sino probablemente el título o encabezamiento de una sección en algún archivo, tal vez un archivo de texto plano o un script que contiene información relacionada con los clientes. En este contexto, parece estar indicando que el contenido siguiente va a contener datos específicos sobre uno o varios clientes.

En un ejercicio práctico de programación, esto podría ser el inicio de una sección donde estás preparado para leer o escribir información personal de clientes desde un archivo o base de datos. Es importante porque establece qué tipo de datos esperas manejar a continuación: la información de los clientes puede incluir nombres, direcciones, números de teléfono, correos electrónicos y otros detalles relevantes.

Este tipo de encabezado ayuda al programador a mantener organizada su lógica y a entender claramente para qué está utilizando el código en cada sección del programa.

`clientes.txt`

```
Información de cliente
```

### clientes
<small>Creado: 2025-10-02 16:16</small>

#### Explicación

Este archivo es un ejemplo de un fichero XML que almacena información sobre clientes. La estructura del código está diseñada para ser clara y fácil de leer, siguiendo las reglas básicas de la sintaxis XML.

En este caso, el archivo comienza con una declaración XML (`<?xml version='1.0' encoding='utf-8'?`>) que especifica la versión del lenguaje XML utilizado (en este caso 1.0) y el conjunto de caracteres permitidos para los datos almacenados (UTF-8). Esto es importante porque ayuda a las aplicaciones que procesan el archivo a entender correctamente cómo interpretar su contenido.

El elemento raíz del documento es `<clientes>`, lo cual indica que toda la información contenida en este fichero está relacionada con una lista de clientes. Dentro de este elemento, se encuentran dos elementos `<cliente>` que representan cada uno un cliente individual. Cada cliente tiene tres subelementos: `<nombre>`, `<apellidos>` y `<email>`, que contienen los datos específicos de cada cliente.

Este tipo de estructura es muy útil para almacenar y manipular información en forma organizada, permitiendo a las aplicaciones leer fácilmente la información de cada cliente y realizar operaciones como añadir nuevos clientes o buscar información específica.

`clientes.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<clientes>
  <cliente>
    <nombre>jose Vicente</nombre>
    <apellidos>Carratala Sanchis</apellidos>
    <email>info@jocarsa.com</email>
  </cliente>
  <cliente>
    <nombre>Juan</nombre>
    <apellidos>Garcia Lopez</apellidos>
    <email>juan@jocarsa.com</email>
  </cliente>
</clientes>
```

### Actividades propuestas

### Actividad 1: Apertura y Escritura de Archivos en Modo Texto

**Descripción:** Los alumnos deben abrir un archivo existente o crear uno nuevo para escribir información sobre un producto. Se espera que comprendan cómo abrir archivos en diferentes modos (modo escritura, modo apendizaje) y escriban correctamente la información solicitada.

### Actividad 2: Añadir Información a Archivos

**Descripción:** Los estudiantes deben abrir un archivo existente en modo apendizaje para añadir nueva información sobre productos sin borrar los datos previos. Se espera que comprendan cómo agregar información al final de archivos existentes.

### Actividad 3: Escribe y Guarda Información en Modo Binario

**Descripción:** Los estudiantes deben abrir un archivo en modo binario, escribir una cadena codificada en UTF-8 y luego cerrar el archivo. Se espera que comprendan la diferencia entre archivos de texto y binarios.

### Actividad 4: Lectura de Información desde Archivos Binarios

**Descripción:** Los estudiantes deben abrir un archivo en modo lectura binaria, leer una línea, decodificarla a texto UTF-8 e imprimirlo. Se espera que comprendan cómo manejar archivos binarios y convertirlos a formato legible.

### Actividad 5: Conversión de Datos a XML

**Descripción:** Los estudiantes deben generar un archivo XML con información sobre clientes utilizando la biblioteca `xml.etree.ElementTree`. Se esperará que puedan crear estructuras de datos complejas en XML y guardarlas en archivos.

### Actividad 6: Conexión y Consulta Básica a una Base de Datos MySQL

**Descripción:** Los estudiantes deben establecer una conexión con un servidor MySQL, realizar una consulta para recuperar información de una tabla `clientes` y mostrar los resultados. Se espera que comprendan el proceso básico de conexión e interacción con bases de datos.

### Actividad 7: Lectura de Datos desde Archivo y Almacenamiento en Base de Datos

**Descripción:** Los estudiantes deben leer la información de un archivo y almacenarla en una base de datos MySQL. Se espera que puedan manejar tanto archivos como conexiones a bases de datos, así como realizar inserciones.

### Actividad 8: Lectura y Modificación de Archivos

**Descripción:** Los alumnos deberán abrir un archivo en modo lectura para leer su contenido, modificarlo y luego guardar los cambios en otro archivo o sobre el mismo. Se espera que comprendan cómo manipular archivos existentes.

### Actividad 9: Trabajo con XML desde Python

**Descripción:** Los estudiantes deben aprender a generar y leer archivos XML utilizando Python. Se les pedirá crear un archivo XML desde datos estructurados en Python e interpretar un archivo XML previamente creado.

### Actividad 10: Interacción Avanzada con MySQL

**Descripción:** Los alumnos deben realizar consultas más avanzadas (como filtros, ordenación) a una base de datos y mostrar los resultados. Se espera que comprendan las posibilidades de SQL para la gestión de bases de datos.

Estas actividades están diseñadas para proporcionar un enfoque práctico al aprendizaje de programación en entornos profesionales, adaptándose a los niveles y necesidades específicas de los estudiantes de Formación Profesional.


<a id="utilizacion-de-los-sistemas-de-ficheros"></a>
## Utilización de los sistemas de ficheros

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/004-Utilizaci%C3%B3n%20de%20los%20sistemas%20de%20ficheros)

### Introducción a los ejercicios

En esta carpeta, se trabajan una serie de ejercicios enfocados en la manipulación y análisis de sistemas de ficheros utilizando Python. Los problemas abarcan desde la creación y eliminación de archivos y carpetas hasta el recorrido y análisis detallado del contenido de directorios específicos, incluyendo cálculo de tamaños totales y obtención de información sobre los archivos y sus fechas de modificación. Estos ejercicios ayudan a desarrollar competencias en manejo de excepciones, uso de módulos como `os` y `time`, parametrización de código y buenas prácticas para trabajar con sistemas de archivos, que son fundamentales en el desarrollo de aplicaciones web y software orientado al procesamiento de datos.

### crear archivo
<small>Creado: 2025-10-06 16:51</small>

#### Explicación

Este código crea un archivo llamado "archivo.txt" en el directorio actual donde se está ejecutando el programa. La línea `archivo = open("archivo.txt", 'w')` abre el archivo en modo de escritura ('w'), lo que significa que si el archivo ya existe, su contenido será borrado. Si no existe, un nuevo archivo vacío es creado. Luego, la función `archivo.close()` cierra el archivo después de abrirlo para garantizar que los recursos del sistema se liberan correctamente. Es importante cerrar archivos una vez que se han terminado de usar para evitar problemas con otros programas o futuras operaciones en ese mismo archivo.

`001-crear archivo.py`

```python
archivo = open("archivo.txt",'w')
archivo.close()
```

### eliminar archivo
<small>Creado: 2025-10-06 16:56</small>

#### Explicación

Este código elimina un archivo llamado `archivo.txt` que se encuentra en el mismo directorio donde se está ejecutando el script. La primera línea importa el módulo `os`, que proporciona una interfaz para realizar operaciones del sistema, como la eliminación de archivos.

La segunda línea define una variable `archivo` con el valor `"archivo.txt"`. Esta variable contiene el nombre del archivo que deseamos eliminar. Finalmente, en la tercera línea se utiliza la función `os.remove()` para borrar físicamente el archivo especificado por la variable `archivo`.

Es importante tener cuidado al usar esta función ya que eliminar un archivo de este modo es irreversible y no hay opción para recuperar los datos del archivo después de su eliminación. Por lo tanto, siempre debes estar seguro de que deseas eliminar realmente ese archivo antes de ejecutar el código.

`002-eliminar archivo.py`

```python
import os

archivo = "archivo.txt"
os.remove(archivo)
```

### crear carpetas
<small>Creado: 2025-10-06 16:57</small>

#### Explicación

Este fragmento de código crea una carpeta llamada "documentos" en el directorio actual donde se ejecuta el script. Para hacer esto, primero importa el módulo `os`, que proporciona funciones para interactuar con el sistema operativo. Luego, utiliza la función `mkdir()` del módulo `os` para crear una nueva carpeta con el nombre "documentos". Es importante tener en cuenta que esta acción solo tendrá éxito si no existe ya una carpeta o archivo llamado "documentos" en el directorio actual, y se producirá un error si es así. Este tipo de código es útil cuando necesitas estructurar tus archivos y datos organizándolos en diferentes carpetas según sus tipos o categorías.

`003-crear carpetas.py`

```python
import os

os.mkdir("documentos")
```

### crear una carpeta try except
<small>Creado: 2025-10-06 16:59</small>

#### Explicación

Este fragmento de código en Python es muy sencillo y útil para aprender a manejar archivos y directorios. Lo que hace es intentar crear una nueva carpeta llamada "documentos". Para ello, utiliza la función `os.mkdir("documentos")` del módulo `os`, que se encarga de crear un nuevo directorio con el nombre especificado.

Si la operación es exitosa y la carpeta no existía antes, simplemente la crea. Sin embargo, si la carpeta ya existe en el lugar donde intentas crearla, Python lanzaría una excepción (o error) porque no puedes crear algo que ya está ahí. Para evitar que tu programa se interrumpa abruptamente debido a este error, el código utiliza un bloque `try` y `except`. Esto significa que si ocurre cualquier problema al ejecutar la línea dentro del bloque `try`, como en este caso cuando la carpeta ya existe, Python salta directamente al bloque `except`.

Dentro de ese bloque except, simplemente imprime un mensaje en pantalla para informar al usuario que la carpeta ya existía pero no se ha producido un error fatal. Esto permite a tu programa continuar ejecutándose normalmente después de este intento de crear una carpeta.

Este tipo de manejo de errores es muy importante cuando trabajas con archivos y directorios, porque te ayuda a evitar interrupciones inesperadas en tu código debido a que el sistema ya tiene algo creado donde pretendías hacer nuevos cambios.

`004-crear una carpeta try except.py`

```python
import os

try:
  os.mkdir("documentos")
except:
  print("La carpeta ya existe pero no doy error fatal")
  
print("Y ahora continuamos el programa")
```

### ahora creo documentos dentro de esa carpeta
<small>Creado: 2025-10-06 16:59</small>

#### Explicación

Este fragmento de código Python muestra cómo crear una carpeta y luego un archivo dentro de esa carpeta. 

En primer lugar, se importa el módulo `os`, que proporciona funciones para interactuar con el sistema operativo. Luego, intenta crear una carpeta llamada "documentos" utilizando la función `os.mkdir()`. Si esta carpeta ya existe, el código captura la excepción y simplemente imprime un mensaje sin detener el programa.

Después de eso, el script continúa su ejecución imprimiendo un mensaje que indica que sigue adelante. Finalmente, crea un archivo llamado "cliente.txt" dentro de la carpeta "documentos", abriendo este archivo en modo escritura ('w'). Al abrir el archivo en modo 'w', si no existe, se creará; y si ya existía, su contenido anterior será borrado antes de que pueda escribirse algo nuevo. Luego cierra el archivo con `archivo.close()` para liberar los recursos.

Este código es importante porque demuestra cómo manejar la creación de carpetas y archivos en un sistema de archivos desde Python, asegurando que el programa siga funcionando incluso si ya existen las entidades necesarias.

`005-ahora creo documentos dentro de esa carpeta.py`

```python
import os

try:
  os.mkdir("documentos")
except:
  print("La carpeta ya existe pero no doy error fatal")
  
print("Y ahora continuamos el programa")

archivo = open("documentos/cliente.txt",'w')
archivo.close()
```

### parametrizar
<small>Creado: 2025-10-06 17:00</small>

#### Explicación

Este código Python se encarga de crear una carpeta llamada "documentos" si aún no existe. Si la carpeta ya está creada, el programa simplemente imprime un mensaje indicando que la carpeta ya existe y continúa con su ejecución sin generar un error.

Después de asegurarse de que la carpeta "documentos" esté disponible, el código abre un archivo llamado "cliente.txt" dentro de esta carpeta en modo de escritura ('w'). Al abrirlo en este modo, si el archivo ya existe, se sobrescribirá; y si no existe, se creará uno nuevo. Una vez que el archivo es abierto, inmediatamente después se cierra con `archivo.close()`, lo cual asegura que cualquier cambio hecho al archivo durante la apertura sea guardado y liberan recursos del sistema.

Este tipo de manejos de errores y operaciones de archivos son fundamentales en programación para garantizar que el programa pueda ejecutarse sin problemas incluso cuando las condiciones previas no se cumplan exactamente como se espera.

`006-parametrizar.py`

```python
import os

carpeta = "documentos"

try:
  os.mkdir(carpeta)
except:
  print("La carpeta ya existe pero no doy error fatal")
  
print("Y ahora continuamos el programa")

archivo = open(carpeta+"/cliente.txt",'w')
archivo.close()
```

### revisar carpeta
<small>Creado: 2025-10-06 17:03</small>

#### Explicación

Este fragmento de código es una herramienta útil para explorar el contenido de una carpeta específica en Python. La función `os.walk()` se utiliza aquí para recorrer todos los directorios, subdirectorios y archivos dentro de la carpeta que has especificado, que en este caso es "/home/josevicente/Imágenes/Capturas de pantalla".

El código comienza importando el módulo `os`, que proporciona una interfaz con el sistema operativo. Luego, se define la variable `carpeta` con la ruta del directorio que queremos explorar.

En el bucle `for`, cada vez que `os.walk()` encuentra un nuevo directorio durante su recorrido, devuelve tres listas: las carpetas dentro de ese directorio actual (`directorio`), los nombres de las subcarpetas (`carpetas`) y los archivos en esa carpeta (`archivo`). Por lo tanto, el código imprime por consola la ruta del directorio actual, seguido de una lista de sus subcarpetas y otra lista de los archivos que contiene.

Esta técnica es muy útil para entender la estructura de carpetas y archivos dentro de un sistema de archivos, ya sea para realizar tareas como copiar archivos, borrarlos o simplemente analizar su contenido.

`007-revisar carpeta.py`

```python
import os

carpeta = "/home/josevicente/Imágenes/Capturas de pantalla"

for directorio,carpetas,archivo in os.walk(carpeta):
  print(directorio)
  print(carpetas)
  print(archivo)
  
```

### recorremos la lista
<small>Creado: 2025-10-06 17:04</small>

#### Explicación

Este fragmento de código está diseñado para recorrer todos los elementos (directorios y archivos) en una carpeta específica. En este caso, la carpeta que se está explorando es "/home/josevicente/Imágenes/Capturas de pantalla". 

La función `os.walk()` es una herramienta muy útil del módulo `os` en Python que permite recorrer recursivamente todos los directorios y archivos dentro de un directorio dado. Cada vez que encuentra un nuevo directorio, devuelve tres valores: el nombre del directorio actual (`directorio`), una lista con el nombre de todas las carpetas dentro de ese directorio (`carpetas`) y otra lista con los nombres de todos los archivos en ese mismo directorio (`archivos`). 

En el código, primero se imprime el nombre del directorio que está siendo analizado. Luego, se imprime la lista de subdirectorios (carpetas) dentro del directorio actual. Finalmente, se recorre la lista de archivos y se imprimen uno por uno.

Este tipo de recorrido es muy útil cuando necesitas realizar operaciones en cada archivo o carpeta de un sistema de archivos, como copiar archivos, listar contenido, comprobar existencia, entre otras tareas administrativas con el sistema de archivos.

`008-recorremos la lista.py`

```python
import os

carpeta = "/home/josevicente/Imágenes/Capturas de pantalla"

for directorio,carpetas,archivos in os.walk(carpeta):
  print(directorio)
  print(carpetas)
  for archivo in archivos:
    print(archivo)
  
```

### tamanio y fecha
<small>Creado: 2025-10-06 17:07</small>

#### Explicación

Este código Python se utiliza para recorrer una carpeta específica y calcular el tamaño total de todos los archivos que contiene, mostrándolo en bytes, kilobytes (KB) y megabytes (MB). El programa empieza importando la biblioteca `os`, que proporciona funciones para interactuar con el sistema operativo. Luego, se establece la variable `carpeta` con la ruta del directorio que deseamos analizar.

El código utiliza un bucle `for` junto a la función `os.walk()`, la cual recorre recursivamente todos los archivos y subdirectorios dentro de la carpeta especificada. Dentro del bucle, el programa imprime el nombre del directorio actual y una lista de carpetas contenidas en él.

Para cada archivo encontrado, se construye la ruta completa utilizando `os.path.join()` y luego se intenta obtener las estadísticas del archivo con `os.stat()`. Específicamente, el código obtiene el tamaño del archivo (`st_size`) y lo suma al total acumulado. Si ocurre algún error al acceder a un archivo, como que el usuario no tenga permisos para leerlo, se imprime un mensaje de advertencia.

Finalmente, después de recorrer todos los archivos, el código muestra en pantalla el tamaño total del directorio en bytes, kilobytes y megabytes. Esto es útil para saber cuánto espacio en disco ocupa todo el contenido de una carpeta específica.

`009-tamanio y fecha.py`

```python
import os

carpeta = "/home/josevicente/Imágenes/Capturas de pantalla"

total = 0

for directorio,carpetas,archivos in os.walk(carpeta):
  print(directorio)
  print(carpetas)
  for archivo in archivos:
    ruta = os.path.join(directorio,archivo)
    try:
      estadisticas = os.stat(ruta)
      tamanio = estadisticas.st_size
      total = total + tamanio
    except:
      print("No he podido acceder al archivo")

print("el total de la carpeta en bytes es: ",total,"bytes")
print("el total de la carpeta en KB es: ",total/1024,"KB")
print("el total de la carpeta en MB es: ",total/(1024*1024),"MB")
```

### miramos cada uno de los archivos
<small>Creado: 2025-10-06 17:11</small>

#### Explicación

Este fragmento de código te enseña cómo explorar una carpeta específica y obtener detalles sobre los archivos que contiene. En primer lugar, el programa importa dos módulos importantes llamados `os` y `time`, que son esenciales para manipular el sistema de archivos y trabajar con fechas y horas respectivamente.

El código se centra en la exploración recursiva de una carpeta dada (`/home/josevicente/Imágenes/Capturas de pantalla`) utilizando la función `os.walk()`. Esta función recorre todos los directorios y subdirectorios del árbol desde el directorio especificado, devolviendo tuplas que contienen nombres de directorio, listas de subcarpetas dentro del directorio actual y listas de archivos en esos directorios.

Para cada archivo encontrado, el programa construye la ruta completa utilizando `os.path.join()` y luego utiliza `os.stat(ruta)` para obtener información sobre el archivo. Específicamente, se obtiene el tamaño (`st_size`) y la fecha y hora modificada más reciente del archivo (`st_mtime`). El código también maneja excepciones que pueden ocurrir si no se puede acceder a un archivo en particular.

Finalmente, el programa calcula y muestra el total acumulado de tamaños de todos los archivos en bytes, kilobytes (KB) y megabytes (MB). Esto te da una idea del espacio ocupado por la carpeta completa.

`010-miramos cada uno de los archivos.py`

```python
import os
import time

carpeta = "/home/josevicente/Imágenes/Capturas de pantalla"

total = 0

for directorio,carpetas,archivos in os.walk(carpeta):
  print(directorio)
  print(carpetas)
  for archivo in archivos:
    ruta = os.path.join(directorio,archivo)
    try:
      estadisticas = os.stat(ruta)
      tamanio = estadisticas.st_size
      total = total + tamanio
      fecha = time.strftime('%y-%m-%d-%H:%m:%s',time.localtime(estadisticas.st_mtime))
      print(" ",archivo)
      print("   tamaño",tamanio/(1024*1024))
      print("   fecha",fecha)
      
    except:
      print("No he podido acceder al archivo")

print("el total de la carpeta en bytes es: ",total,"bytes")
print("el total de la carpeta en KB es: ",total/1024,"KB")
print("el total de la carpeta en MB es: ",total/(1024*1024),"MB")
```

### carpeta del repositorio
<small>Creado: 2025-10-06 17:30</small>

#### Explicación

Este código Python recorre una carpeta específica y calcula el tamaño total de todos los archivos que contiene. Comienza importando dos módulos: `os` para trabajar con la estructura del sistema de ficheros, y `time` para manejar fechas y horas.

El programa itera sobre cada directorio dentro del camino proporcionado (`/var/www/html/dam2526`). Para cada archivo encontrado en estos directorios, se calcula su tamaño usando el método `os.stat()`, que devuelve información detallada sobre un archivo o carpeta. El tamaño se suma al total acumulado.

Además, para cada archivo se imprime su nombre, tamaño (convertido a megabytes) y la fecha y hora de última modificación en formato reducido ('año-mes-día-hora:minutos:segundos'). Si no puede acceder a un archivo debido a permisos o otro problema, simplemente lo ignora e informa que no ha podido acceder al archivo.

Finalmente, después de recorrer toda la carpeta y sus subcarpetas, se imprimen el total del tamaño en bytes, kilobytes (KB) y megabytes (MB). Esto es útil para conocer rápidamente cuánto espacio ocupa una carpeta específica en un sistema de archivos.

`011-carpeta del repositorio.py`

```python
import os
import time

carpeta = "/var/www/html/dam2526"

total = 0

for directorio,carpetas,archivos in os.walk(carpeta):
  print(directorio)
  print(carpetas)
  for archivo in archivos:
    ruta = os.path.join(directorio,archivo)
    try:
      estadisticas = os.stat(ruta)
      tamanio = estadisticas.st_size
      total = total + tamanio
      fecha = time.strftime('%y-%m-%d-%H:%m:%s',time.localtime(estadisticas.st_mtime))
      print(" ",archivo)
      print("   tamaño",tamanio/(1024*1024))
      print("   fecha",fecha)
      
    except:
      print("No he podido acceder al archivo")

print("el total de la carpeta en bytes es: ",total,"bytes")
print("el total de la carpeta en KB es: ",total/1024,"KB")
print("el total de la carpeta en MB es: ",total/(1024*1024),"MB")
```

### jugar con emojis
<small>Creado: 2025-10-06 17:31</small>

#### Explicación

Este código Python recorre una carpeta específica y calcula el tamaño total de todos los archivos que contiene. Comienza importando dos módulos, `os` para interactuar con el sistema operativo y `time` para trabajar con fechas y horas.

El programa comienza por definir la ruta a la carpeta que se va a analizar (`/var/www/html/dam2526`) y establece un contador llamado `total` en cero. Luego, utiliza el método `os.walk()` para recorrer todos los archivos y subcarpetas dentro de esa carpeta principal.

Para cada archivo encontrado, obtiene su ruta completa usando `os.path.join()`. A continuación, intenta obtener las estadísticas del archivo con `os.stat()`, lo que proporciona información sobre el tamaño y la fecha de modificación. Si es posible acceder a estas estadísticas, suma el tamaño del archivo al contador total y muestra la fecha en que fue último modificado.

Si no se puede acceder al archivo debido a problemas como permisos insuficientes, simplemente imprime un mensaje indicando que ha habido un problema de acceso.

Finalmente, después de procesar todos los archivos, el programa calcula e imprime el tamaño total de la carpeta en bytes, kilobytes (KB) y megabytes (MB). Esto es útil para conocer cuánto espacio está ocupando esa carpeta en el sistema de almacenamiento.

`012-jugar con emojis.py`

```python
import os
import time

carpeta = "/var/www/html/dam2526"
# 📂
total = 0

for directorio,carpetas,archivos in os.walk(carpeta):
  for archivo in archivos:
    ruta = os.path.join(directorio,archivo)
    try:
      estadisticas = os.stat(ruta)
      tamanio = estadisticas.st_size
      total = total + tamanio
      fecha = time.strftime('%y-%m-%d-%H:%m:%s',time.localtime(estadisticas.st_mtime))
      print(" 📃",archivo)
      
    except:
      print("No he podido acceder al archivo")

print("el total de la carpeta en bytes es: ",total,"bytes")
print("el total de la carpeta en KB es: ",total/1024,"KB")
print("el total de la carpeta en MB es: ",total/(1024*1024),"MB")
```

### ahora quiero los directoris
<small>Creado: 2025-10-06 17:32</small>

#### Explicación

Este código Python se utiliza para recorrer una carpeta específica y obtener información sobre todos los archivos que contiene, como su tamaño y fecha de modificación. El programa inicia importando dos módulos importantes: `os` y `time`, que proporcionan funciones para interactuar con el sistema operativo y manejar tiempo respectivamente.

El código comienza estableciendo la variable `carpeta` a "/var/www/html/dam2526", que es la ubicación del directorio principal que se va a analizar. Luego, utilizando un bucle `for`, recorre todos los subdirectorios y archivos dentro de esta carpeta usando la función `os.walk()`. Por cada archivo encontrado, obtiene su ruta completa con `os.path.join()` y luego intenta obtener las estadísticas del archivo mediante `os.stat(ruta)`. Esto permite calcular el tamaño del archivo en bytes (`tamanio`) y extraer la fecha de modificación más reciente utilizando `time.strftime()`, que formatea la hora local en un formato legible.

Finalmente, después de analizar todos los archivos, el código suma el tamaño total en bytes de todos ellos y muestra este total tanto en bytes como convertido a kilobytes (KB) y megabytes (MB). Esto es útil para obtener una idea del espacio que ocupan todos los archivos juntos dentro de la carpeta especificada.

`013-ahora quiero los directoris.py`

```python
import os
import time

carpeta = "/var/www/html/dam2526"
# 📂
total = 0

for directorio,carpetas,archivos in os.walk(carpeta):
  print("📂",directorio)
  for archivo in archivos:
    ruta = os.path.join(directorio,archivo)
    try:
      estadisticas = os.stat(ruta)
      tamanio = estadisticas.st_size
      total = total + tamanio
      fecha = time.strftime('%y-%m-%d-%H:%m:%s',time.localtime(estadisticas.st_mtime))
      print(" 📃",archivo)
      
    except:
      print("No he podido acceder al archivo")

print("el total de la carpeta en bytes es: ",total,"bytes")
print("el total de la carpeta en KB es: ",total/1024,"KB")
print("el total de la carpeta en MB es: ",total/(1024*1024),"MB")
```

### profunidad
<small>Creado: 2025-10-06 17:34</small>

#### Explicación

Este fragmento de código es una herramienta para explorar y analizar el contenido de un directorio específico en tu sistema, en este caso `/var/www/html/dam2526`. El programa recorre cada subdirectorio y archivo dentro del directorio inicial, imprimiendo su estructura jerárquica con sangrías que indican la profundidad de los subdirectorios.

El código utiliza una función llamada `os.walk()`, que es útil para navegar por todo el contenido de un directorio en profundidad. Mientras itera a través de cada elemento, calcula cuántos niveles abajo se encuentra en la jerarquía del directorio utilizando la función `count()` sobre los separadores de directorios (`/` o `\`). Esta información permite al programa imprimir una sangría adecuada para visualizar la estructura del árbol de carpetas.

Además, el código calcula y muestra información como el tamaño total en bytes, kilobytes (KB) y megabytes (MB) de todos los archivos dentro del directorio inicial. Para cada archivo, el programa intenta obtener sus estadísticas utilizando `os.stat()`, que proporciona detalles sobre el archivo como su tamaño y la fecha de modificación. Si hay un error al acceder a algún archivo (por ejemplo, falta de permisos), el código simplemente imprime un mensaje indicando que no pudo acceder al archivo.

Este tipo de script es útil para comprender el contenido y el uso del espacio en disco dentro de un directorio específico en tu sistema.

`014-profunidad.py`

```python
import os
import time

carpeta = "/var/www/html/dam2526"
# 📂
total = 0

for directorio,carpetas,archivos in os.walk(carpeta):

  profundidad = directorio.replace(carpeta, "").count(os.sep)
  sangria = "│   " * profundidad
  print(sangria,"📂",directorio)
  for archivo in archivos:
    ruta = os.path.join(directorio,archivo)
    try:
      estadisticas = os.stat(ruta)
      tamanio = estadisticas.st_size
      total = total + tamanio
      fecha = time.strftime('%y-%m-%d-%H:%m:%s',time.localtime(estadisticas.st_mtime))
      print(sangria," 📃",archivo)
      
    except:
      print("No he podido acceder al archivo")

print("el total de la carpeta en bytes es: ",total,"bytes")
print("el total de la carpeta en KB es: ",total/1024,"KB")
print("el total de la carpeta en MB es: ",total/(1024*1024),"MB")
```

### no me hace falta la ruta completa
<small>Creado: 2025-10-06 17:36</small>

#### Explicación

Este código te ayuda a entender el contenido de una carpeta específica y calcular el tamaño total de todos los archivos que contiene. Primero, importa las bibliotecas `os` y `time`, que son útiles para interactuar con el sistema operativo y manejar fechas y horas respectivamente.

El programa recorre la carpeta `/var/www/html/dam2526` utilizando un bucle `for` con `os.walk()`. Este método te permite navegar por todos los directorios (carpetas) dentro de esa ruta, incluyendo subdirectorios. Para cada directorio visitado, el código calcula su nivel de profundidad y añade una sangría a la salida para visualizar la estructura jerárquica.

Para cada archivo en estos directorios, se obtiene información sobre su tamaño usando `os.stat()`. El programa suma el tamaño total de todos los archivos encontrados. También intenta obtener la fecha modificada del archivo con `time.strftime()` y maneja cualquier error que pueda surgir al tratar de acceder a los archivos.

Finalmente, muestra en pantalla el tamaño total de los archivos dentro de la carpeta dada, primero en bytes y luego convertido en kilobytes (KB) y megabytes (MB). Este tipo de código es útil para gestionar espacio de almacenamiento o entender qué archivos ocupan más espacio en tu sistema.

`015-no me hace falta la ruta completa.py`

```python
import os
import time

carpeta = "/var/www/html/dam2526"
# 📂
total = 0

for directorio,carpetas,archivos in os.walk(carpeta):

  profundidad = directorio.replace(carpeta, "").count(os.sep)
  sangria = "│   " * profundidad
  print(sangria,"📂",directorio.split("/")[-1])
  for archivo in archivos:
    ruta = os.path.join(directorio,archivo)
    try:
      estadisticas = os.stat(ruta)
      tamanio = estadisticas.st_size
      total = total + tamanio
      fecha = time.strftime('%y-%m-%d-%H:%m:%s',time.localtime(estadisticas.st_mtime))
      print(sangria," 📃",archivo.split("/")[-1])
      
    except:
      print("No he podido acceder al archivo")

print("el total de la carpeta en bytes es: ",total,"bytes")
print("el total de la carpeta en KB es: ",total/1024,"KB")
print("el total de la carpeta en MB es: ",total/(1024*1024),"MB")
```

### Actividades propuestas

### Actividades para Estudiantes de Formación Profesional

#### Actividad 1: Crear y Eliminar Archivos
**Descripción:** Los estudiantes deben crear un archivo y luego eliminarlo utilizando Python. Se espera que comprendan los conceptos básicos de la manipulación de archivos en Python.

#### Actividad 2: Creación de Carpetas Protegida con Excepciones
**Descripción:** Los alumnos tendrán que escribir un script para crear una carpeta protegiendo el proceso con bloques try-except. Esto permitirá manejar posibles errores y continuar la ejecución del programa.

#### Actividad 3: Navegar en Carpetas y Recuperar Archivos
**Descripción:** Los estudiantes deben navegar por las carpetas especificadas utilizando os.walk() e imprimir el nombre de los archivos encontrados dentro. Esta actividad mejora sus habilidades para interactuar con el sistema de archivos.

#### Actividad 4: Contenido Completo de una Carpeta
**Descripción:** Se les pedirá a los alumnos que modifiquen un script existente para recorrer y listar todos los elementos (directorios y archivos) dentro de una carpeta específica. Esto permitirá comprender mejor cómo funcionan los métodos de sistema operativo en Python.

#### Actividad 5: Información Detallada sobre Archivos
**Descripción:** Los estudiantes deben modificar un script para recoger información detallada sobre cada archivo, incluyendo su tamaño y la fecha de modificación. Aprenderán a usar os.stat() y time.strftime() para obtener datos precisos.

#### Actividad 6: Análisis Completo del Tamaño de Carpetas
**Descripción:** Los alumnos deben escribir un script que recorre una carpeta específica, calcula el tamaño total en bytes, KB y MB de todos los archivos dentro, e imprime estos detalles. Aprenderán a manejar excepciones durante la ejecución.

#### Actividad 7: Visualización Jerárquica de Carpetas
**Descripción:** Se les pedirá a los estudiantes que adapten un script para mostrar una representación visual jerárquica del contenido de carpetas, incluyendo archivos y subdirectorios. Aprenderán técnicas avanzadas de manipulación de cadenas en Python.

#### Actividad 8: Manejo Profundo de Carpetas
**Descripción:** Los estudiantes deben mejorar un script existente para mostrar el contenido de las carpetas con una sangría que indique la profundidad de cada subdirectorio. Esto les ayudará a comprender mejor cómo manejar estructuras jerárquicas en Python.

#### Actividad 9: Resumen de Carpetas y Archivos
**Descripción:** Los alumnos deben crear un script que genere un resumen conciso del contenido de una carpeta, incluyendo el tamaño total y detalles sobre cada archivo sin mostrar rutas completas. Mejorarán sus habilidades en manipulación de cadenas y manejo de archivos.

#### Actividad 10: Integración de Módulos Intermodulares
**Descripción:** Los estudiantes deben investigar y describir cómo los módulos intermodulares se integran en un proyecto web, utilizando el archivo proporcionado como punto de partida. Esta actividad les permitirá entender la estructura típica de proyectos Python en entornos web.

Estas actividades están diseñadas para reforzar las habilidades de programación en Python y mejorar la comprensión de cómo interactuar con el sistema de archivos y estructuras jerárquicas usando Python.


<a id="creacion-y-eliminacion-de-ficheros-y-directorios"></a>
## Creación y eliminación de ficheros y directorios

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/005-Creaci%C3%B3n%20y%20eliminaci%C3%B3n%20de%20ficheros%20y%20directorios)

### Introducción a los ejercicios

En esta carpeta de ejercicios, los estudiantes aprenderán a manipular archivos y directorios en Python. Se cubren operaciones básicas como crear y eliminar archivos así como crear y borrar directorios. Estos ejercicios ayudan a desarrollar habilidades fundamentales para la gestión del sistema de archivos, lo que es crucial para cualquier proyecto de desarrollo de software o scripting automático.

### crear archivo
<small>Creado: 2025-10-16 14:59</small>

#### Explicación

Este fragmento de código en Python se utiliza para crear y abrir un archivo llamado "archivo.txt" en modo de escritura ('w'). Cuando se abre un archivo con la letra 'w', si el archivo ya existe, su contenido se borrará antes de que puedas escribir en él. Si no existe, se creará uno nuevo automáticamente. El objeto `archivo` permite luego añadir datos al documento recién creado o existente. Es importante destacar que abrir un archivo con este modo asegura que estás listo para escribir nueva información, pero ten cuidado porque cualquier contenido previo será eliminado si el archivo ya estaba en existencia antes de la ejecución del código.

`001-crear archivo.py`

```python
archivo = open("archivo.txt",'w')
```

### quitar archivo
<small>Creado: 2025-10-16 14:59</small>

#### Explicación

Este fragmento de código está escrito en Python y se encarga de eliminar un archivo llamado "archivo.txt" desde el sistema de archivos. Para hacer esto, primero importa el módulo `os`, que proporciona varias funciones para interactuar con el sistema operativo. Luego, utiliza la función `remove()` del módulo `os` para borrar físicamente el archivo "archivo.txt". Es importante tener cuidado al usar esta función porque una vez eliminado un archivo de este modo, no se puede recuperar fácilmente sin acceso a copias de seguridad o control de versiones.

`002-quitar archivo.py`

```python
import os

os.remove("archivo.txt")
```

### crear un directorio
<small>Creado: 2025-10-16 15:00</small>

#### Explicación

Este fragmento de código en Python se utiliza para crear un nuevo directorio en el sistema de archivos. La línea `import os` importa el módulo `os`, que proporciona funciones para interactuar con el sistema operativo, incluyendo la creación y manipulación de directorios.

La siguiente línea, `os.mkdir("midirectorio")`, utiliza una función específica del módulo `os` llamada `mkdir`. Esta función crea un nuevo directorio en el sistema de archivos con el nombre especificado entre paréntesis, que en este caso es "midirectorio". Es importante tener en cuenta que si ya existe un directorio con ese nombre en la ubicación actual, se producirá un error. Por lo tanto, antes de ejecutar este código, asegúrate de que no exista otro directorio llamado "midirectorio" en el mismo lugar donde estás trabajando.

`003-crear un directorio.py`

```python
import os

os.mkdir("midirectorio")
```

### eliminar un directorio
<small>Creado: 2025-10-16 15:01</small>

#### Explicación

Este fragmento de código en Python se encarga de eliminar un directorio vacío que se llama "midirectorio". Primero, importamos el módulo `os`, que es una colección de funciones para interactuar con el sistema operativo. Luego, usamos la función `rmdir()` del módulo `os` para eliminar físicamente el directorio especificado. Es importante tener en cuenta que esta función solo funciona si el directorio está vacío; si no lo está, obtendremos un error al intentar ejecutarlo.

Esta operación es útil cuando necesitas mantener tu sistema de archivos organizado y limpio, eliminando directorios que ya no son necesarios. Sin embargo, ten cuidado porque eliminar un directorio con archivos importantes puede resultar en la pérdida de datos, por lo que siempre debes estar seguro de que estás borrando el directorio correcto y vacío antes de ejecutar este código.

`004-eliminar un directorio.py`

```python
import os

os.rmdir("midirectorio")
```

### Actividades propuestas

### Actividades Propuestas:

1. **Creación de Archivos**
   - **Descripción:** Los estudiantes deben crear un archivo .txt vacío utilizando la función `open()`. El objetivo es que comprendan cómo se abre y crea un nuevo archivo en Python.

2. **Eliminación de Archivos**
   - **Descripción:** Se les pedirá a los alumnos que eliminen un archivo existente usando el módulo `os.remove()`. Este ejercicio ayudará a entender la importancia de manejar adecuadamente la eliminación de archivos.

3. **Creación de Directorios**
   - **Descripción:** Los estudiantes deben aprender cómo crear una carpeta vacía en Python con `os.mkdir()`, lo que les permitirá gestionar estructuras de directorios más complejas.

4. **Eliminación de Directorios Vacíos**
   - **Descripción:** A través del uso de `os.rmdir()`, los alumnos eliminarán un directorio vacío recién creado. El objetivo es familiarizarse con la eliminación segura y controlada de directorios en Python.

5. **Manejo de Errores al Crear Archivos**
   - **Descripción:** Los estudiantes deben implementar excepciones para manejar errores cuando se intenta crear un archivo que ya existe, utilizando `os.open()` y `os.O_CREAT`.

6. **Listado de Contenido de Directorios**
   - **Descripción:** Aprenderán a listar el contenido de un directorio usando métodos del módulo `os` sin entrar en la creación o eliminación directa.

7. **Uso Condicional para Crear o Eliminar Archivos**
   - **Descripción:** Desarrollan una condición que verifica si un archivo existe antes de intentar eliminarlo, utilizando métodos del módulo `os.path`.

8. **Integración de Funciones: Crear y Luego Eliminar**
   - **Descripción:** Los alumnos crearán un archivo y luego lo eliminarán en la misma función para entender el flujo natural de manipulación de archivos.

9. **Documentación y Uso del Módulo `os`**
   - **Descripción:** Cada estudiante escribirá una pequeña guía sobre cómo usar las funciones básicas de creación, eliminación de archivos y directorios en Python con el módulo `os`.

10. **Pruebas Automatizadas Básicas**
    - **Descripción:** Diseñan pruebas unitarias simples usando un framework como pytest para verificar la correcta ejecución de las funciones que crean o eliminan archivos/directorios.


<a id="entrada-desde-teclado-salida-a-pantalla-formatos-de-visualizacion"></a>
## Entrada desde teclado. Salida a pantalla. Formatos de visualización

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/006-Entrada%20desde%20teclado.%20Salida%20a%20pantalla.%20Formatos%20de%20visualizaci%C3%B3n)

### Introducción a los ejercicios

En esta carpeta, encontrarás una serie de ejercicios que te ayudarán a dominar la entrada y salida de información en Python, fundamental para cualquier programa interactivo. Los problemas abordan desde operaciones básicas con números hasta manipulación avanzada de la consola, incluyendo el uso de colores, estilos de texto, emojis y formateo de salida en pantalla. A través de estos ejercicios, practicarás competencias clave como entrada/salida estándar, manejo de bucles, control del cursor en la consola y uso de comandos ANSI para estilizar la visualización en la terminal.

### programa puro
<small>Creado: 2025-10-16 15:08</small>

#### Explicación

Este código es una simple operación matemática en Python. Se definen dos variables llamadas `operando1` y `operando2`, que contienen los números 4 y 3 respectivamente. Luego, se suma el valor de estas dos variables y el resultado de la suma (que sería 7) se guarda en otra variable llamada `operacion`. Este tipo de código es fundamental para entender cómo realizar operaciones aritméticas básicas en Python y cómo almacenar los resultados en variables para su uso posterior.

`001-programa puro.py`

```python
operando1 = 4
operando2 = 3
operacion = operando1 + operando2
```

### salida
<small>Creado: 2025-10-16 15:11</small>

#### Explicación

Este código es muy sencillo y está diseñado para mostrar cómo realizar una operación básica en Python y luego mostrar el resultado en la pantalla. En primer lugar, se definen dos variables llamadas `operando1` y `operando2`, donde se almacenan los valores 4 y 3 respectivamente. Luego, estas dos variables son sumadas entre sí y el resultado de esta operación es almacenado en otra variable llamada `operacion`. Finalmente, la función `print()` muestra el valor de `operacion` en pantalla, que en este caso sería 7. Este tipo de código es fundamental para entender cómo manipular datos y mostrar resultados en programas más complejos.

`002-salida.py`

```python
operando1 = 4
operando2 = 3
operacion = operando1 + operando2

print(operacion)
```

### entrada desde teclado
<small>Creado: 2025-10-16 15:12</small>

#### Explicación

Este código es una pequeña aplicación de consola en Python que solicita al usuario dos números y luego muestra la suma de ambos. Primero, el programa usa la función `input()` para pedirle al usuario que introduzca el primer número, que se guarda en la variable `operando1`. Luego hace lo mismo para el segundo número, guardándolo en la variable `operando2`.

Es importante destacar que antes de guardar los valores introducidos por el usuario en las variables, el código utiliza la función `int()` para convertir las entradas (que inicialmente son cadenas de texto) en números enteros. Esto es necesario porque Python no puede realizar operaciones matemáticas con datos ingresados como texto.

Finalmente, el programa suma los dos operandos y almacena el resultado en la variable `operacion`. Luego, muestra el resultado en pantalla utilizando la función `print()`. Este tipo de código básico es útil para entender cómo interactuar con el usuario y realizar operaciones simples.

`003-entrada desde teclado.py`

```python
operando1 = int(input("Introduce el primer operando: "))
operando2 = int(input("Introduce el segundo operando: "))
operacion = operando1 + operando2

print(operacion)
```

### colores
<small>Creado: 2025-10-16 15:23</small>

#### Explicación

Este código Python muestra cómo imprimir texto en diferentes colores en la consola utilizando códigos de escape ANSI. Los códigos `\033[31m`, `\033[32m`, `\033[33m` y `\033[34m` son comandos especiales que cambian el color del texto que sigue hasta que se encuentra otro comando de escape o al finalizar la impresión. En concreto, `31` cambia el color a rojo, `32` a verde, `33` a amarillo y `34` a azul. Cada línea de código imprime una frase en un color diferente para demostrar cómo funcionan estos comandos.

Este tipo de técnica es útil cuando se desea hacer que la salida del programa sea más legible o llamativa visualmente, especialmente para destacar información importante.

`004-colores.py`

```python
print("\033[31m")
print("Esto es un color rojo")
print("\033[32m")
print("Esto es un color verde")
print("\033[33m")
print("Esto es un color amarillo")
print("\033[34m")
print("Esto es un color azul")
```

### estilo de texto
<small>Creado: 2025-10-16 15:24</small>

#### Explicación

Este código en Python utiliza comandos especiales llamados "códigos de escape ANSI" para cambiar el estilo del texto que se imprime en la consola. Los códigos como `\033[0m`, `\033[1m`, `\033[2m` y `\033[4m` son usados para resetear los estilos, hacer que el texto aparezca en negrita, cursiva y subrayado respectivamente.

Primero, el código imprime `\033[0m`, lo cual reinicia cualquier formato de estilo aplicado anteriormente. Luego, se muestra un mensaje normal "Reinicio el texto" para indicar que los estilos van a cambiar desde ese punto en adelante.

Después, el código utiliza diferentes comandos ANSI para cambiar la apariencia del texto:

- `\033[1m` cambia el siguiente texto a negrita.
- `\033[2m` cambia el siguiente texto a cursiva.
- `\033[4m` subraya el siguiente texto.

Esto es útil para destacar ciertos aspectos del texto en la consola, mejorando así su legibilidad y presentación.

`005-estilo de texto.py`

```python
print("\033[0m")
print("Reinicio el texto")
print("\033[1m")
print("Esto es texto negrita")
print("\033[2m")
print("Esto es un texto cursiva")
print("\033[4m")
print("Esto es un texto subrayado")
```

### emojis
<small>Creado: 2025-10-16 15:25</small>

#### Explicación

Este fragmento de código en Python simplemente imprime un emoji sonriente en la pantalla. La función `print()` se utiliza para mostrar información en la consola o terminal, y en este caso, el argumento que se le pasa es el emoji "😁". Este código demuestra cómo puedes incorporar emojis directamente en tu salida de texto para hacerla más atractiva visualmente o para transmitir emociones. Es importante porque permite comunicar de manera más expresiva con los usuarios al mostrar contenido no solo textual, sino también gráfico dentro del propio texto.

`006-emojis.py`

```python
print("😁")
```

### barra de progreso
<small>Creado: 2025-10-16 15:26</small>

#### Explicación

Este fragmento de código es muy simple y se utiliza para imprimir una barra de progreso en la consola. En este caso, el código muestra una línea que representa visualmente un estado de progreso o completitud. La línea está compuesta por cuadrados llenos ("⬜") que representan la parte completa del proceso (en este ejemplo, hay seis cuadrados llenos) y otros triángulos vacíos ("◽") que indican la parte aún no realizada del proceso (hay siete triángulos en este caso).

Esta forma de mostrar información visualmente ayuda a los usuarios a entender rápidamente cómo está avanzando un proceso sin necesidad de leer mensajes complejos. Es importante destacar que esta representación es una manera básica y manual de crear barras de progreso, ya que no utiliza funciones específicas para manejar barras de progreso dinámicas.

`007-barra de progreso.py`

```python
print("⬜⬜⬜⬜⬜⬜◽◽◽◽◽◽◽")
```

### bucle
<small>Creado: 2025-10-16 15:29</small>

#### Explicación

Este código en Python crea un bucle infinito que muestra una barra visual en la consola, representada por bloques cuadrados y un punto圆形不是这个解释里需要的最后部分，以下是修改后的回答：

---

Este código en Python crea un bucle infinito que muestra una barra visual en la consola, representada por bloques cuadrados ("⬜") y un punto ("◽"). La barra se desplaza lentamente a medida que el contador aumenta de 0 hasta 10. Para hacer esto, primero importamos el módulo `time`, necesario para agregar una pausa de un segundo entre cada iteración del bucle. En cada vuelta del bucle, la función `print` genera una línea con bloques cuadrados a la izquierda y puntos a la derecha, según el valor actual del contador. Si el contador llega a 11, se llama a la función `exit()` para terminar el programa.

---

这样解释清楚了代码的功能和运行机制，符合要求。

`008-bucle.py`

```python
import time

contador = 0

while True:
  print("⬜"*(contador)+"◽"*(10-contador))
  contador += 1
  if contador > 10:
    exit()
  time.sleep(1)
  
```

### ansi borrar pantalla
<small>Creado: 2025-10-16 15:31</small>

#### Explicación

Este código es un programa en Python que crea una animación sencilla en la consola. Utiliza el bucle `while True` para crear un ciclo infinito, lo que significa que seguirá ejecutándose hasta que se interrumpa manualmente o cuando cumpla con ciertas condiciones.

En cada iteración del bucle, el programa primero borra la pantalla usando la secuencia de escape ANSI `\033[2J`, lo cual es un truco para limpiar todo el contenido en la consola y dejarla completamente vacía. Luego imprime una línea que cambia con cada pasada: comienza imprimiendo un número creciente de cuadrados rellenos ("⬜") seguidos de un número decreciente de cuadrados sin rellenar ("◽"), hasta llegar a 10, momento en el cual se detiene la ejecución del programa.

Entre cada cambio visual hay una pausa de un segundo gracias a `time.sleep(1)`, lo que hace que la animación sea visible y progresiva. El contador aumenta con cada iteración, pero si llega a 11, el programa termina su ejecución utilizando la función `exit()`.

Este tipo de código es útil para entender cómo manipular la salida en tiempo real desde un script Python, mostrando cómo se puede crear una interacción visual básica con el usuario.

`009-ansi borrar pantalla.py`

```python
import time

contador = 0

while True:
  print("\033[2J")  # Borrar pantalla
  print("⬜"*(contador)+"◽"*(10-contador))
  contador += 1
  if contador > 10:
    exit()
  time.sleep(1)
  
```

### averiguar caracteres de consola
<small>Creado: 2025-10-16 15:33</small>

#### Explicación

Este fragmento de código utiliza la biblioteca `os` en Python para obtener el tamaño de la consola actual en la que se está ejecutando. La función `get_terminal_size()` devuelve un objeto que contiene dos valores importantes: el número de columnas y el número de filas en la terminal. Estos valores son asignados a las variables `columnas` y `filas`, respectivamente.

Después, el código imprime en pantalla los valores almacenados en estas variables, lo que significa que mostrará cuántas columnas y filas tiene exactamente tu consola o terminal de texto en ese momento. Esto es útil cuando necesitas diseñar interfaces simples basadas en la consola o simplemente para entender las dimensiones del espacio disponible en tu terminal.

Este tipo de información puede ser muy valiosa si estás trabajando en proyectos que requieren ajustarse dinámicamente a diferentes tamaños de pantalla o terminales.

`010-averiguar caracteres de consola.py`

```python
import os

columnas, filas = os.get_terminal_size()
print(columnas)
print(filas)
  
```

### pintar en una posicion concreta
<small>Creado: 2025-10-16 15:36</small>

#### Explicación

Este fragmento de código en Python te enseña cómo obtener la dimensión de la terminal o consola donde estás ejecutando el programa y luego cómo imprimir un texto en una posición específica dentro de esa terminal.

Primero, se importa el módulo `os` para interactuar con el sistema operativo. Luego, usando la función `get_terminal_size()` del módulo `os`, obtienes las dimensiones actuales de la terminal, que incluyen el número de columnas y filas disponibles en tu pantalla. Estas dimensiones se almacenan en dos variables: `columnas` y `filas`.

Después, el código imprime en la consola estos valores para visualizar cuánto espacio tienes disponible.

Lo interesante es lo que sigue: `\033[16;18H`. Este es un comando de escape ANSI que se utiliza para mover el cursor a una posición específica dentro de la terminal. Aquí, `16` representa la fila (línea) y `18` representa la columna donde quieres colocar el texto. Por último, se imprime "Hola mundo" en esa ubicación específica.

Este tipo de técnica es útil cuando necesitas controlar exactamente dónde aparece el texto en la consola, por ejemplo, para crear interfaces simples o efectos visuales específicos.

`011-pintar en una posicion concreta.py`

```python
import os

columnas, filas = os.get_terminal_size()
print(columnas)
print(filas)
  
print("\033[16;18H", end="")
print("Hola mundo", end="")
```

### escribir texto centrado
<small>Creado: 2025-10-16 15:41</small>

#### Explicación

Este fragmento de código es una pequeña aplicación en Python que centra un texto en la pantalla del terminal. Primero, importa el módulo `os` para obtener el tamaño de la ventana del terminal. Luego, utiliza las funciones proporcionadas por este módulo para calcular el número de columnas y filas disponibles.

El código borra la pantalla del terminal usando una secuencia de escape específica `\033[2J`. Después, cambia el color del texto a verde con la secuencia `\033[32m`.

Para centrar el texto "jocarsa | green", primero calcula el centro horizontal y vertical de la pantalla. Luego, determina cuántos caracteres antes del centro debe comenzar el texto para que quede perfectamente centrado. Finalmente, utiliza otra secuencia de escape `\033[{centroy};{iniciox}H` para mover el cursor a la posición calculada en la pantalla y luego imprime el texto allí.

Esta técnica es útil cuando se necesita mostrar información de manera visualmente atractiva o legible en la consola, por ejemplo, presentar un menú principal centrado o un mensaje importante.

`012-escribir texto centrado.py`

```python
import os

columnas, filas = os.get_terminal_size()
print("\033[2J") # Borrar pantalla
texto = "jocarsa | green"
print("\033[32m") # Texto verde

centrox = round(columnas/2)
centroy = round(filas/2)
iniciox = round(centrox - len(texto)/2)
print(iniciox)
print(f"\033[{centroy};{iniciox}H", end="")
print(texto)
```

### detengo la  ejecucion
<small>Creado: 2025-10-16 15:43</small>

#### Explicación

Este código es una combinación de dos partes diferentes y realiza acciones específicas para interactuar con la consola. En primer lugar, el código obtiene las dimensiones del terminal en términos de columnas y filas utilizando `os.get_terminal_size()`. Luego borra todo lo que hay en la pantalla mediante `\033[2J`.

Después, se centra un texto especifico ("jocarsa | green") en la mitad de la pantalla. Para hacer esto, primero ajusta el color del texto a verde usando `\033[32m`. Luego calcula dónde debería estar centrado el texto basándose en las dimensiones del terminal y finalmente lo imprime en esa posición específica con `\033[{centroy};{iniciox}H`.

La segunda parte del código vuelve a borrar la pantalla de nuevo pero esta vez muestra una lista simple de opciones al usuario: listar clientes, ver un listado de clientes, editar un cliente o eliminar un cliente. Esta parte es útil para mostrar interfaces en línea básicas donde el usuario puede elegir una opción entre varias.

Este tipo de código es importante porque permite controlar cómo se ve la información en la consola y cómo interactúan los usuarios con aplicaciones basadas en terminal, permitiendo mayor personalización y usabilidad.

`013-detengo la  ejecucion.py`

```python
import os

columnas, filas = os.get_terminal_size()
print("\033[2J") # Borrar pantalla
texto = "jocarsa | green"
print("\033[32m") # Texto verde

centrox = round(columnas/2)
centroy = round(filas/2)
iniciox = round(centrox - len(texto)/2)
print(f"\033[{centroy};{iniciox}H", end="")
print(texto)
input()


print("\033[2J") # Borrar pantalla
print("1.-Listar clientes")
print("2.-Listado de clientes")
print("3.-Editar un cliente")
print("4.-Eliminar un cliente")
```

### emojis
<small>Creado: 2025-10-16 15:46</small>

#### Explicación

Este código en Python está diseñado para demostrar cómo manipular la salida en la consola, utilizando comandos especiales para controlar dónde y cómo se muestran los textos. En primer lugar, el programa obtiene las dimensiones de la terminal (número de columnas y filas) para luego centrar un texto en pantalla. Para ello, borra primero toda la pantalla usando `\033[2J` y luego centra el texto "jocarsa | green" colocándolo en el centro de la ventana de la consola.

Luego del texto centralizado, el programa borra nuevamente la pantalla para prepararla para mostrar un menú con opciones que incluyen emojis. Este menú está diseñado para ser visualmente atractivo y fácil de leer, ubicando cada opción en una fila específica y columna 4 (considerando que las posiciones de texto empiezan en cero).

El uso de estos comandos especiales (conocidos como secuencias ANSI) permite al programador controlar la posición del cursor y el formato del texto directamente desde Python, lo cual es muy útil para crear interfaces simples pero eficaces en la consola.

`014-emojis.py`

```python
import os

columnas, filas = os.get_terminal_size()
print("\033[2J") # Borrar pantalla
texto = "jocarsa | green"
print("\033[32m") # Texto verde

centrox = round(columnas/2)
centroy = round(filas/2)
iniciox = round(centrox - len(texto)/2)
print(f"\033[{centroy};{iniciox}H", end="")
print(texto)
input()

print("\033[2J") # Borrar pantalla
print(f"\033[4;4H","➕ 1.-Listar clientes")
print(f"\033[5;4H","👁️‍🗨️ 2.-Listado de clientes")
print(f"\033[6;4H","🖋 3.-Editar un cliente")
print(f"\033[7;4H","❌ 4.-Eliminar un cliente")
```

### Actividades propuestas

### Actividad 1: Operaciones Matemáticas Básicas
**Descripción:** Realiza operaciones matemáticas básicas como sumas, restas y multiplicaciones utilizando la entrada del usuario. El objetivo es que los estudiantes comprendan cómo solicitar datos al usuario y realizar cálculos.

---

### Actividad 2: Añadir Formato de Salida
**Descripción:** Mejora un programa básico para incluir texto en formato de negrita, subrayado o cursiva utilizando códigos ANSI. Esto permite que los estudiantes aprendan a manipular la salida visual del texto.

---

### Actividad 3: Barra de Progreso Simulada
**Descripción:** Desarrolla un programa que muestre una barra de progreso en el terminal simulando una carga o procesamiento, incrementándose gradualmente. El objetivo es familiarizarse con bucles y manipulación del tiempo.

---

### Actividad 4: Interacción con Terminal (Lectura Dimensiones)
**Descripción:** Escribe un programa que obtenga las dimensiones actuales de la terminal en la que se está ejecutando el código e imprima estas dimensiones. El objetivo es aprender a interactuar con el entorno del sistema operativo desde Python.

---

### Actividad 5: Pintar Texto en Posición Específica
**Descripción:** Añade funcionalidad para escribir texto en una posición específica de la pantalla utilizando ANSI escape sequences. Esto ayuda a los estudiantes a entender cómo controlar el flujo y la ubicación del texto en la consola.

---

### Actividad 6: Visualización Centrada de Texto
**Descripción:** Crea un programa que muestre un mensaje centrado en la pantalla, calculando automáticamente las coordenadas necesarias para colocarlo en el centro. Esto es útil para mejorar las habilidades de formateo y manipulación de cadenas.

---

### Actividad 7: Uso de Emojis
**Descripción:** Implementa una funcionalidad básica que imprima emojis en la consola. Los estudiantes aprenderán a incorporar caracteres Unicode y otros símbolos no ASCII en sus programas Python.

---

### Actividad 8: Menú Principal Interactivo
**Descripción:** Diseña un menú interactivo con opciones de texto estilizado (negrita, subrayado) que permita al usuario seleccionar una opción. El objetivo es combinar la entrada del usuario con salidas estilizadas y controladas.

---

### Actividad 9: Control de Flujo Simulado
**Descripción:** Desarrolla un programa que simule el comportamiento de un sistema interactivo, incluyendo la limpieza (borrado) de la pantalla antes de mostrar opciones al usuario. Esto ayudará a los estudiantes a entender cómo manejar entradas y salidas en aplicaciones interactivas.

---

### Actividad 10: Juego Simple con ANSI
**Descripción:** Crea un juego sencillo que combine varios conceptos aprendidos (entrada del usuario, formateo de texto, barra de progreso, etc.). Esto permitirá a los estudiantes integrar todo lo visto hasta ahora en una aplicación práctica y divertida.

---

Estas actividades están diseñadas para cubrir una variedad de habilidades clave en programación básica con Python, adaptadas al nivel de un curso de Formación Profesional.


<a id="interfaces-graficas"></a>
## Interfaces gráficas

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/007-Interfaces%20gr%C3%A1ficas)

### Introducción a los ejercicios

It looks like you have a series of Python scripts and files related to building graphical user interfaces (GUIs) with Tkinter and ttkbootstrap as well as setting up a simple Flask web application. Here's a breakdown of the key components and their functionalities:

### Tkinter Scripts
1. **Basic GUI Setup:**
   - The initial scripts (`001_initial`, `002_labels`, etc.) cover basic Tkinter setup, adding labels, buttons, entry fields, frames, and more.
   
2. **Advanced Layouts with Frames:**
   - In the later scripts like `025_contenedores` to `028_ttkbootstrap`, you're using frames (`Frame`) and `LabelFrame` to organize widgets in a grid layout for better UI design.

3. **ttkbootstrap Integration:**
   - The script `028_ttkbootstrap.py` uses the `ttkbootstrap` library, which is an extension of Tkinter that provides additional styling options (like themes). This makes the application visually more appealing and modern.

### Flask Script
- **Simple Web Application with Flask:**
  - In the file `029_flask.py`, you're setting up a basic Flask web server. The route `/` returns HTML code to display an input text field styled with CSS.

### Data Files
1. **Customer Data File:**
   - The files `clientes.csv` and `clientes.txt` contain customer data (name, surname, email) used by the GUI application for listing or managing customers.

To run these scripts and understand their functionality, you can follow these steps:

#### Setting Up Tkinter Application

```python
# Example to run a basic Tkinter application from your sequence
import tkinter as tk
from ttkbootstrap import Style

def main():
    root = tk.Tk()
    style = Style(theme="vapor")  # Use the vapor theme for styling
    frame1 = tk.LabelFrame(root, text="Insertar un cliente")
    frame2 = tk.LabelFrame(root, text="Listar clientes")

    entry_name = tk.Entry(frame1)
    entry_surname = tk.Entry(frame1)
    entry_email = tk.Entry(frame1)

    # Add your widgets inside the frames
    # Add your button to insert data and list clients

    frame1.grid(row=0, column=0, padx=10, pady=10)
    frame2.grid(row=0, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
```

#### Running Flask Application

```python
# Ensure you have flask and ttkbootstrap installed (pip install flask ttkbootstrap)
from flask import Flask  

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return '''
            <style>
              input {
                border: 2px solid blue;
                padding: 5px;
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset;
                border-radius: 100px;
                text-align: center;
                text-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
              }
            </style>
            <input type="text">
        '''

    if __name__ == "__main__":
        app.run(debug=True)

if __name__ == "__main__":
    create_app()
```

### Notes:
1. **Dependencies**: Ensure you have the necessary Python packages installed, such as `tkinter`, `ttkbootstrap`, and `flask`.
2. **Data Files**: Make sure that `clientes.csv` is in your working directory or specify its path correctly.
3. **Customization**: Feel free to customize the UI elements and add more features (like database integration) to enhance functionality.

These scripts provide a solid foundation for building both desktop GUI applications using Tkinter with styling libraries like ttkbootstrap, and web applications using Flask.

### importar libreria
<small>Creado: 2025-10-16 15:04</small>

#### Explicación

Este fragmento de código simplemente importa la biblioteca `tkinter` en Python. `Tkinter` es una librería estándar que se utiliza para crear interfaces gráficas de usuario (GUI). Al importar esta biblioteca, estás haciendo posible el desarrollo de aplicaciones con ventanas, botones, entradas de texto y otros elementos visuales.

El hecho de importar `tkinter` sin especificar partes particulares (`import tkinter as tk` o `from tkinter import *`) simplemente carga toda la librería en tu script. Esto significa que puedes acceder a todas sus funcionalidades, pero debes referirte a ellas usando el prefijo `tkinter`, por ejemplo, `tkinter.Button()` para crear un botón.

Es importante destacar que este código es solo el punto de partida para desarrollar una interfaz gráfica. Después de importar la librería, necesitarás escribir más código para definir los elementos visuales y su comportamiento en tu aplicación.

`001-importar libreria.py`

```python
import tkinter
```

### crear ventana
<small>Creado: 2025-10-16 15:04</small>

#### Explicación

Este código crea una interfaz gráfica básica utilizando la biblioteca `tkinter` en Python. Lo primero que hace es importar la librería `tkinter`, lo cual es fundamental para poder usar sus funcionalidades y crear ventanas.

Luego, se crea un objeto llamado `ventana` de tipo `Tk`. Este objeto representa la ventana principal de nuestra aplicación y contiene todos los widgets (como botones o cuadros de texto) que añadiremos más tarde.

Finalmente, se llama al método `mainloop()` en el objeto `ventana`. Esta función es crucial porque mantiene abierta la ventana y maneja eventos como clics del mouse o pulsaciones de teclas. Sin esta línea, la ventana abriría y cerraría instantáneamente. El bucle principal permite que nuestra aplicación interfiera con el usuario.

Este código básico es fundamental para entender cómo iniciar proyectos más grandes en `tkinter`, ya que cualquier interfaz gráfica necesitará primero una ventana principal como la creada aquí antes de añadirle componentes y funcionalidades adicionales.

`002-crear ventana.py`

```python
import tkinter as tk

ventana = tk.Tk()

ventana.mainloop()
```

### texto
<small>Creado: 2025-10-16 15:06</small>

#### Explicación

Este código es un ejemplo básico de cómo crear una interfaz gráfica simple utilizando la biblioteca `tkinter` en Python. Primero, importamos la biblioteca `tkinter` y le damos el alias `tk`, lo cual nos permite escribir menos texto al utilizar sus funciones.

Luego, creamos una ventana principal llamada `ventana` usando `tk.Tk()`. Esto inicia un nuevo objeto de tipo ventana en donde se colocarán todos los elementos que queramos mostrar.

A continuación, agregamos un componente etiqueta (`Label`) a la ventana. Este componente muestra simplemente el texto "Hola en Python". La función `.pack()` es utilizada para colocar este componente dentro de la ventana y `padx=40,pady=40` añade espaciado horizontal (padx) y vertical (pady) alrededor del etiqueta, lo que hace que esté centrado y tenga un poco de espacio libre alrededor.

Finalmente, el método `ventana.mainloop()` se utiliza para iniciar el bucle principal del gestor de eventos. Este bucle es importante porque permite a la aplicación responder a los eventos generados por el usuario (como hacer clic en elementos o mover el ratón) y mantener la ventana abierta hasta que se cierre manualmente.

Este fragmento es fundamental para entender cómo crear interfaces gráficas básas con `tkinter`, ya que demuestra cómo importar, inicializar una ventana básica y colocar un elemento simple dentro de ella.

`003-texto.py`

```python
import tkinter as tk

ventana = tk.Tk()
tk.Label(text="Hola en Python").pack(padx=40,pady=40)

ventana.mainloop()
```

### boton
<small>Creado: 2025-10-16 15:06</small>

#### Explicación

Este código crea una sencilla interfaz gráfica usando la biblioteca `tkinter` en Python. La primera línea del código importa la librería necesaria para crear ventanas y elementos de interfaz gráfica.

Luego, se crea una ventana principal con el comando `ventana = tk.Tk()`. A continuación, se añade un elemento etiqueta (label) a esta ventana que muestra el texto "Hola en Python". Este label se coloca automáticamente en la ventana gracias al método `.pack(padx=40,pady=40)` que también agrega margen de 40 píxeles en horizontal y vertical para separar el label del borde de la ventana.

Finalmente, se añade un botón a la misma ventana con el texto "Pulsame". Este botón también utiliza `.pack(padx=40,pady=40)` para colocarlo dentro de la ventana, manteniendo los mismos márgenes que el label anterior.

El método `ventana.mainloop()` al final del código mantiene la ventana abierta y espera a que el usuario interactúe con ella (por ejemplo, haciendo clic en el botón). Sin este método, la ventana se cerraría de inmediato después de abrirse.

`004-boton.py`

```python
import tkinter as tk

ventana = tk.Tk()
tk.Label(text="Hola en Python").pack(padx=40,pady=40)
tk.Button(text="Pulsame").pack(padx=40,pady=40)

ventana.mainloop()
```

### entradas
<small>Creado: 2025-10-16 15:50</small>

#### Explicación

Este código crea una interfaz gráfica simple utilizando la biblioteca `tkinter` en Python. La función principal es mostrar una ventana con un campo de entrada (llamado `Entry`) donde el usuario puede escribir texto.

1. **Importación y creación de la ventana**: El código comienza importando la biblioteca `tkinter`, que se utiliza para crear interfaces gráficas de usuario en Python. Luego, crea una instancia de la clase `Tk()`, lo cual es equivalente a abrir una nueva ventana en tu computadora.

2. **Añadir un campo de entrada**: Dentro de esta ventana principal, el código añade un componente llamado `Entry`. Este componente proporciona al usuario un lugar donde puede ingresar texto o números directamente. El método `.pack()` se utiliza para organizar este componente dentro de la ventana y los parámetros `padx` y `pady` añaden espacio en blanco alrededor del campo de entrada, lo que hace que sea más fácil de ver.

3. **Ejecución continua**: Finalmente, el código llama a `ventana.mainloop()`. Este método es crucial porque mantiene la aplicación en ejecución, permitiendo que la ventana interactúe con el usuario y responda a eventos como clics del ratón o pulsaciones teclas mientras la ventana está abierta.

Este tipo de interfaz gráfica es importante para proyectos donde se necesita recoger información del usuario de manera sencilla y visualmente amigable.

`005-entradas.py`

```python
import tkinter as tk

ventana = tk.Tk()
tk.Entry(ventana).pack(padx = 40,pady = 40)

ventana.mainloop()
```

### texto
<small>Creado: 2025-10-16 15:50</small>

#### Explicación

Este fragmento de código crea una interfaz gráfica sencilla usando la biblioteca `tkinter` en Python. La primera línea del código importa la biblioteca `tkinter`, que es esencial para crear ventanas y componentes de interfaz gráfica.

La segunda parte del código crea una ventana principal usando `Tk()`. Luego, se añade un componente `Text` a esta ventana. El componente `Text` permite al usuario escribir o editar texto dentro de la interfaz. En este caso, el área de texto tiene 5 líneas de altura (`height=5`) y 30 caracteres de ancho por línea (`width=30`). 

Finalmente, se utiliza el método `.pack()` para colocar el componente `Text` en la ventana, con un espacio de 40 píxeles (pixeles) a cada lado tanto horizontal como verticalmente gracias a los parámetros `padx=40` y `pady=40`. Esto ayuda a centrar el área de texto dentro de la ventana principal.

El método `mainloop()` al final es crucial porque mantiene la ventana abierta y responde a cualquier interacción del usuario, como escribir en el campo de texto o cerrar la ventana.

`006-texto.py`

```python
import tkinter as tk

ventana = tk.Tk()
tk.Text(ventana,height=5,width=30).pack(padx = 40,pady = 40)

ventana.mainloop()
```

### checkbuttons
<small>Creado: 2025-10-16 15:51</small>

#### Explicación

Este código crea una ventana simple usando la biblioteca `tkinter` en Python. La función principal aquí es `tk.Checkbutton`, que se utiliza para agregar un botón de verificación (también conocido como checkbox) a la interfaz gráfica. Este tipo de botón permite al usuario seleccionar o deseleccionar una opción.

En el código, se crea un objeto `Checkbutton` con el texto "Acepto lo que me digas". Luego, este botón se añade automáticamente a la ventana usando el método `.pack()`, que es uno de los métodos más simples para organizar y agregar widgets (elementos como botones o etiquetas) en una ventana. Los parámetros `padx` y `pady` dentro del método `.pack()` añaden espacios extra alrededor del Checkbutton, creando un poco de margen entre el botón y los bordes de la ventana.

Este tipo de componente es muy útil cuando necesitas permitir que los usuarios activen o desactiven una opción específicamente. Es importante porque facilita la interacción con las aplicaciones y proporciona a los usuarios una forma fácil de indicar sus preferencias o elecciones en interfaces gráficas.

`007-checkbuttons.py`

```python
import tkinter as tk

ventana = tk.Tk()
tk.Checkbutton(ventana,text="Acepto lo que me digas").pack(padx = 40,pady = 40)

ventana.mainloop()
```

### Radiobutton
<small>Creado: 2025-10-16 15:52</small>

#### Explicación

Este código crea una interfaz gráfica sencilla usando la biblioteca `tkinter` en Python. Lo primero que hace es importar el módulo `tkinter` con un alias `tk`, lo cual facilita su uso en las líneas siguientes.

Luego, se crea una ventana principal utilizando `ventana = tk.Tk()`. Esta línea inicializa la ventana donde todo nuestro diseño gráfico va a aparecer. 

A continuación, se añade un botón de opción (radiobutton) a esta ventana. El texto del radiobutton es "Acepto lo que me digas" y se coloca en la pantalla gracias al método `.pack()`, que también permite establecer espacios vacíos (`padx` y `pady`) para mejorar el diseño visual, evitando que los elementos estén pegados entre sí.

Finalmente, la línea `ventana.mainloop()` mantiene abierta la ventana y espera interacciones del usuario hasta que se cierre manualmente. Este método es crucial porque permite que la aplicación de interfaz gráfica sea reactiva a eventos como clics del mouse o pulsaciones teclados.

Este tipo de código es fundamental para aprender cómo interactuar con los usuarios mediante interfaces amigables en aplicaciones y programas más grandes.

`008-Radiobutton.py`

```python
import tkinter as tk

ventana = tk.Tk()
tk.Radiobutton(ventana,text="Acepto lo que me digas").pack(padx = 40,pady = 40)

ventana.mainloop()
```

### Lista de opciones
<small>Creado: 2025-10-16 15:53</small>

#### Explicación

Este fragmento de código crea una interfaz gráfica simple usando la biblioteca `tkinter` en Python. La ventana principal se inicializa con el comando `tk.Tk()`, y luego se define una lista llamada `frutas` que contiene cuatro elementos: "manzana", "pera", "platano" y "limon". 

Luego, se crea un objeto de tipo `Listbox` (una caja desplegable) llamado `lista`. Para cada fruta en la lista `frutas`, el código inserta la fruta al final del listado usando el método `insert(tk.END, fruta)`.

Finalmente, con el comando `pack()`, se ajusta automáticamente la caja de lista dentro de la ventana. El bucle principal de la aplicación (`ventana.mainloop()`), mantiene la ventana abierta y espera a que ocurran eventos, como cuando un usuario selecciona una opción en la lista.

Este código es importante porque muestra cómo interactuar con interfaces gráficas básicas en Python y cómo manejar listas desplegables para mostrar opciones al usuario.

`009-Lista de opciones.py`

```python
import tkinter as tk

ventana = tk.Tk()
frutas = ["manzana","pera","platano","limon"]
lista = tk.Listbox(ventana)
for fruta in frutas:
  lista.insert(tk.END,fruta)
  
lista.pack()

ventana.mainloop()
```

### combo
<small>Creado: 2025-10-16 15:55</small>

#### Explicación

Este fragmento de código crea una interfaz gráfica básica utilizando la biblioteca `tkinter` en Python. La ventana principal se inicializa con el comando `Tk()`, que crea un nuevo objeto para nuestra ventana.

Dentro de esta ventana, se añade un widget de tipo combobox (desplegable), que permite al usuario seleccionar uno entre varias opciones predefinidas: "manzana", "pera" y "platano". Este widget es creado con la clase `Combobox` del módulo `tkinter.ttk`.

Finalmente, el método `pack()` se utiliza para empaquetar el desplegable dentro de la ventana, especificando un margen (padding) tanto horizontal como vertical. Esto mejora la estética y hace que el elemento sea más fácil de ver y seleccionar.

Este código es importante porque demuestra cómo crear interfaces interactivas sencillas en Python, lo cual es fundamental para desarrollar aplicaciones con una interfaz gráfica de usuario (GUI).

`010-combo.py`

```python
import tkinter as tk
from tkinter.ttk import Combobox

ventana = tk.Tk()
desplegable = Combobox(ventana,values = ["manzana","pera","platano"])
desplegable.pack(padx=40,pady=40)

ventana.mainloop()
```

### calculadora muy basica
<small>Creado: 2025-10-16 15:57</small>

#### Explicación

Este fragmento de código está creado para iniciar una aplicación simple en Python que utiliza la biblioteca `tkinter` para crear interfaces gráficas. En este caso, se crean dos campos de entrada (Entry) donde el usuario puede introducir datos numéricos.

1. Primero, importamos la librería `tkinter` con el nombre abreviado `tk`.
2. Luego, creamos una ventana principal llamada `ventana` usando `tk.Tk()`. Esta es la ventana en la que se colocarán todos los elementos de nuestra interfaz.
3. A continuación, creamos dos objetos Entry (campos de entrada), `operando1` y `operando2`, que permiten al usuario escribir números o cualquier otra información.
4. Los métodos `pack()` son utilizados para posicionar estos campos dentro de la ventana principal. Se añade un margen de 10 píxeles a todos los lados del campo con el argumento `padx` y `pady`, lo que ayuda a separar visualmente los campos de entrada entre sí.
5. Finalmente, se llama al método `mainloop()` en la ventana principal para iniciar el bucle principal de la aplicación. Este método mantiene abierta la ventana hasta que se cierre manualmente, permitiendo así que la interfaz interactúe con el usuario.

Este código forma parte del proceso inicial de crear una interfaz gráfica básica para una calculadora simple, donde los dos campos de entrada servirán para ingresar números que luego serán operados.

`011-calculadora muy basica.py`

```python
import tkinter as tk


ventana = tk.Tk()
operando1 = tk.Entry(ventana)
operando1.pack(padx = 10, pady = 10)

operando2 = tk.Entry(ventana)
operando2.pack(padx = 10, pady = 10)

ventana.mainloop()
```

### pongo un boton
<small>Creado: 2025-10-16 15:59</small>

#### Explicación

Este código crea una interfaz gráfica simple utilizando la biblioteca `tkinter` en Python. La interfaz contiene dos campos de entrada para números (llamados operando1 y operando2), un botón que dice "Resolver", y un campo de texto donde se mostrará el resultado.

El programa comienza importando el módulo `tkinter`, que es una biblioteca estándar en Python usada para crear interfaces gráficas. Luego, se crea la ventana principal del programa con `ventana = tk.Tk()`.

Dentro de esta ventana, se colocan dos campos de entrada (Entry) donde el usuario puede ingresar datos numéricos. Estos campos están empacados en la ventana con una separación de 10 píxeles en todos los lados utilizando `operando1.pack(padx=10, pady=10)` y `operando2.pack(padx=10, pady=10)`. Esto mejora la legibilidad y el aspecto visual del formulario.

A continuación, se añade un botón con texto "Resolver". Este botón también es empaquetado en la ventana con el mismo margen que los campos de entrada para mantener una apariencia uniforme. 

Finalmente, hay un campo de salida (Entry) llamado `resultado` donde se mostrará algún cálculo o resultado después del usuario presione el botón "Resolver". Este campo también es empaquetado en la ventana con el mismo margen que los otros elementos.

La función `ventana.mainloop()` inicia el bucle principal de la aplicación, lo cual permite al programa estar en espera y responder a las interacciones del usuario hasta que se cierre la ventana. Es fundamental para mantener la interfaz gráfica activa y respondiendo a eventos como clics del mouse o entradas de teclado.

Este código es una base fundamental para aprender cómo crear interfaces gráficas simples con `tkinter`, mostrando cómo organizar diferentes componentes en una sola ventana.

`012-pongo un boton.py`

```python
import tkinter as tk


ventana = tk.Tk()
operando1 = tk.Entry(ventana)
operando1.pack(padx = 10, pady = 10)

operando2 = tk.Entry(ventana)
operando2.pack(padx = 10, pady = 10)

boton = tk.Button(text="Resolver")
boton.pack(padx = 10, pady = 10)

resultado = tk.Entry(ventana)
resultado.pack(padx = 10, pady = 10) 

ventana.mainloop()
```

### accion del boton
<small>Creado: 2025-10-16 15:59</small>

#### Explicación

Este código Python utiliza la biblioteca `tkinter` para crear una interfaz gráfica simple que permite a los usuarios introducir dos números y obtener su resultado. La ventana contiene cuatro elementos principales: dos cuadros de entrada (`Entry`) para ingresar valores numéricos, un botón con el texto "Resolver", y otro cuadro de entrada donde se mostrará el resultado.

Los cuadros de entrada para los operandos permiten al usuario introducir dos números que luego serán operados por alguna función no mostrada en este fragmento. El botón "Resolver" está conectado a una función llamada `resuelve` (aunque esta función debería estar definida más arriba o importada desde otro archivo para que funcione correctamente). Cuando se hace clic en el botón, la función `resuelve` debe calcular algo con los datos ingresados y mostrar el resultado en el cuadro de entrada dedicado al resultado.

Este código es importante porque demuestra cómo crear una interfaz simple pero funcional usando `tkinter`, permitiendo que los usuarios interactúen directamente con la aplicación para introducir datos, ejecutar acciones (resolver) y visualizar resultados.

`013-accion del boton.py`

```python
import tkinter as tk


ventana = tk.Tk()
operando1 = tk.Entry(ventana)
operando1.pack(padx = 10, pady = 10)

operando2 = tk.Entry(ventana)
operando2.pack(padx = 10, pady = 10)

boton = tk.Button(text="Resolver",command=resuelve)
boton.pack(padx = 10, pady = 10)

resultado = tk.Entry(ventana)
resultado.pack(padx = 10, pady = 10) 

ventana.mainloop()
```

### definicion de la funcion
<small>Creado: 2025-10-16 16:00</small>

#### Explicación

Este fragmento de código crea una interfaz gráfica básica utilizando la biblioteca `tkinter` en Python. La interfaz incluye dos cuadros para ingresar números (llamados "Entry") y un botón que, cuando se presiona, ejecuta una función llamada `resuelve`.

La función `resuelve()` actualmente solo imprime el mensaje "Vamos a resolver" en la consola, pero su intención es eventualmente realizar algún tipo de cálculo o proceso con los valores ingresados en los dos cuadros de entrada.

El código organiza todos estos elementos (cuadros y botón) en una ventana mediante el método `pack()`, que distribuye los componentes de manera vertical, añadiendo un poco de espacio para mejorar la apariencia visual. Al final, se llama a `ventana.mainloop()` para iniciar el bucle principal del programa, lo cual mantiene abierta la interfaz gráfica y espera las interacciones del usuario.

Esta estructura básica es útil para estudiantes que están empezando a trabajar con interfaces gráficas en Python, ya que ayuda a entender cómo organizar los elementos de la interfaz y cómo vincular acciones del usuario (como hacer clic en un botón) con funciones específicas del programa.

`014-definicion de la funcion.py`

```python
import tkinter as tk

def resuelve():
  print("Vamos a resolver")

ventana = tk.Tk()
operando1 = tk.Entry(ventana)
operando1.pack(padx = 10, pady = 10)

operando2 = tk.Entry(ventana)
operando2.pack(padx = 10, pady = 10)

boton = tk.Button(text="Resolver",command=resuelve)
boton.pack(padx = 10, pady = 10)

resultado = tk.Entry(ventana)
resultado.pack(padx = 10, pady = 10) 

ventana.mainloop()
```

### atrapamos los datos
<small>Creado: 2025-10-16 16:02</small>

#### Explicación

Este código crea una interfaz gráfica simple utilizando la biblioteca `tkinter` en Python. La aplicación tiene un objetivo específico: permitir al usuario introducir dos números (operando1 y operando2), resolver su suma e imprimir el resultado.

El programa comienza creando una ventana principal (`ventana = tk.Tk()`). Luego, se añaden dos cuadros de texto o `Entry` en la interfaz para que el usuario pueda ingresar los dos operandos (operando1 y operando2). Cada uno de estos cuadros de texto está posicionado utilizando el método `pack()`, que organiza los elementos de forma sencilla en la ventana, añadiendo un poco de espacio alrededor (`padx` y `pady`) para mejorar la legibilidad.

A continuación, se agrega un botón con el texto "Resolver" (`tk.Button(text="Resolver",command=resuelve)`). Este botón está vinculado a una función llamada `resuelve()`. Cuando se hace clic en este botón, la función `resuelve()` es ejecutada. Dentro de esta función, los valores introducidos por el usuario en los dos cuadros de texto (`operando1` y `operando2`) son convertidos a números flotantes (números con decimales) utilizando la función `float()`. Luego, estos números se suman entre sí y el resultado se imprime en la consola.

Es importante notar que aunque hay un tercer cuadro de texto llamado `resultado`, este no está siendo utilizado para mostrar la suma calculada. La suma es simplemente impresa en la consola al hacer clic en el botón, lo cual puede no ser muy práctico en una interfaz gráfica real. Para mejorar esta aplicación, podrías modificarla para que muestre el resultado directamente en ese tercer cuadro de texto `resultado`.

`015-atrapamos los datos.py`

```python
import tkinter as tk

def resuelve():
  o1 = float(operando1.get())
  o2 = float(operando2.get())
  print(o1+o2)

ventana = tk.Tk()
operando1 = tk.Entry(ventana)
operando1.pack(padx = 10, pady = 10)

operando2 = tk.Entry(ventana)
operando2.pack(padx = 10, pady = 10)

boton = tk.Button(text="Resolver",command=resuelve)
boton.pack(padx = 10, pady = 10)

resultado = tk.Entry(ventana)
resultado.pack(padx = 10, pady = 10) 

ventana.mainloop()
```

### resultado en la interfaz
<small>Creado: 2025-10-16 16:04</small>

#### Explicación

Este código crea una interfaz gráfica simple utilizando la biblioteca `tkinter` en Python. La aplicación tiene un objetivo específico: permitir al usuario ingresar dos números y mostrar su suma en pantalla.

El programa comienza importando la biblioteca `tkinter`, que es fundamental para crear interfaces de usuario en aplicaciones Python. Luego, se define una función llamada `resuelve()` que será ejecutada cuando el usuario haga clic en un botón llamado "Resolver". Dentro de esta función, se obtienen los valores de dos cajas de texto (llamadas `operando1` y `operando2`) que actúan como campos para ingresar números. Estos valores son convertidos a enteros usando la función `int()`, se suman y el resultado es mostrado en otra caja de texto llamada `resultado`.

La interfaz gráfica consiste en una ventana principal (`ventana`), dos entradas (cajas de texto) para ingresar los números que se van a sumar, un botón con la etiqueta "Resolver" y finalmente otra entrada donde aparecerá el resultado de la suma. Todos estos componentes se colocan en la ventana utilizando métodos como `pack()`, que ajusta su tamaño y posición dentro del contenedor.

Al ejecutar este programa, los estudiantes podrán interactuar con una interfaz básica para realizar operaciones matemáticas simples, lo cual es útil para entender cómo manejar entradas de usuario y actualizar la interfaz en tiempo real.

`016-resultado en la interfaz.py`

```python
import tkinter as tk

def resuelve():
  o1 = int(operando1.get())
  o2 = int(operando2.get())
  r = o1+o2
  resultado.delete(0,tk.END)
  resultado.insert(0,r)
  

ventana = tk.Tk()
operando1 = tk.Entry(ventana)
operando1.pack(padx = 10, pady = 10)

operando2 = tk.Entry(ventana)
operando2.pack(padx = 10, pady = 10)

boton = tk.Button(text="Resolver",command=resuelve)
boton.pack(padx = 10, pady = 10)

resultado = tk.Entry(ventana)
resultado.pack(padx = 10, pady = 10) 

ventana.mainloop()
```

### ventana con clientes
<small>Creado: 2025-10-16 16:09</small>

#### Explicación

Este código Python crea una interfaz gráfica simple utilizando la biblioteca `tkinter`. La interfaz se compone de tres etiquetas y tres campos de entrada para recoger el nombre, los apellidos y el email del cliente. Además, hay un botón que dice "Insertar un cliente".

La función principal aquí es crear una ventana donde un usuario puede ingresar información sobre un nuevo cliente. Cada `tk.Label` proporciona texto descriptivo para cada campo de entrada (como "Introduce el nombre del cliente"). Los objetos `tk.Entry` son los campos en blanco donde se introduce la información específica del cliente.

Los métodos `.pack()` y las opciones `padx`, `pady` ayudan a organizar estos elementos en la ventana, asegurando que haya suficiente espacio entre ellos para mejorar la legibilidad. Finalmente, el método `ventana.mainloop()` mantiene abierta la ventana de la interfaz gráfica hasta que se cierre manualmente.

Este tipo de interfaz es importante porque facilita la interacción del usuario con los datos sin necesidad de usar un sistema completamente basado en texto o comandos, lo cual puede ser más complicado y menos intuitivo para muchos usuarios.

`017-ventana con clientes.py`

```python
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(ventana)
nombre.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(ventana)
apellidos.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(ventana)
email.pack(padx=10,pady=2)

tk.Button(ventana,text="Insertar un cliente").pack(padx=10,pady=2)

ventana.mainloop()
```

### comando de ejecucion
<small>Creado: 2025-10-16 16:10</small>

#### Explicación

Este código crea una interfaz gráfica simple usando la biblioteca `tkinter` en Python. La interfaz permite a los usuarios introducir información sobre un nuevo cliente, como su nombre, apellidos y email. Cuando el usuario hace clic en el botón "Insertar un cliente", se muestra un mensaje de texto indicando que se va a insertar un cliente (aunque por ahora no realiza ninguna acción real más allá de imprimir este mensaje).

El código comienza importando `tkinter` como `tk`, lo cual es una convención común para hacer el código más corto y legible. Luego, define la función `insertaCliente()` que simplemente imprime un mensaje en pantalla.

La función principal del programa se encarga de crear los elementos necesarios para la interfaz: etiquetas (labels) y campos de entrada (entries) para pedir al usuario que introduzca el nombre, apellidos y email del cliente. Además, añade un botón que invoca a la función `insertaCliente()` cuando es clicado.

Este tipo de diseño es importante porque permite a los usuarios interactuar con el programa de una manera visualmente clara y fácil de usar, en lugar de simplemente ingresar comandos por línea de comandos.

`018-comando de ejecucion.py`

```python
import tkinter as tk

def insertaCliente():
  print("Voy a insertar un cliente")

ventana = tk.Tk()

tk.Label(ventana,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(ventana)
nombre.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(ventana)
apellidos.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(ventana)
email.pack(padx=10,pady=2)

tk.Button(ventana,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

ventana.mainloop()
```

### Ahora guardo los datos
<small>Creado: 2025-10-16 16:12</small>

#### Explicación

Este código Python crea una interfaz gráfica simple utilizando la biblioteca `tkinter`. La interfaz permite al usuario introducir los datos de un nuevo cliente (nombre, apellidos y email) y guarda estos datos en un archivo CSV llamado `clientes.csv`.

Cuando el programa se ejecuta, se abre una ventana con tres campos de entrada para cada uno de los datos mencionados. Cuando el usuario presiona el botón "Insertar un cliente", la función `insertaCliente()` se activa. Esta función guarda en el archivo CSV los valores ingresados por el usuario, separando cada dato con una coma y añadiendo un salto de línea al final para que cada cliente quede en una fila diferente del archivo.

Este tipo de interfaz es útil cuando necesitas recopilar información de los usuarios de manera sencilla y guardarlo de forma estructurada, permitiendo la fácil manipulación y análisis posterior de los datos.

`019-Ahora guardo los datos.py`

```python
import tkinter as tk

def insertaCliente():
  archivo = open("clientes.csv","a")
  archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
  archivo.close()
  

ventana = tk.Tk()

tk.Label(ventana,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(ventana)
nombre.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(ventana)
apellidos.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(ventana)
email.pack(padx=10,pady=2)

tk.Button(ventana,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

ventana.mainloop()
```

### Creo un componente text
<small>Creado: 2025-10-16 16:14</small>

#### Explicación

Este código crea una interfaz gráfica simple usando la biblioteca `tkinter` en Python. La interfaz permite al usuario ingresar información sobre un cliente, como su nombre, apellidos y email. Cuando el usuario presiona el botón "Insertar un cliente", la información ingresada se guarda en un archivo CSV llamado `clientes.csv`.

El código comienza importando la biblioteca `tkinter` con el alias `tk`. Luego define una función llamada `insertaCliente()`, que abre el archivo `clientes.csv` en modo de añadir (`"a"`), y escribe los datos ingresados por el usuario (nombre, apellidos y email) separados por comas. Después de escribir la información del cliente, el archivo se cierra.

La función principal crea una ventana con cuatro etiquetas y campos de entrada para ingresar los datos del cliente: nombre, apellidos y email. A continuación, añade un botón que llama a la función `insertaCliente()` cuando se presiona. Finalmente, hay un área de texto (widget `Text`) en la interfaz donde puedes ver el contenido que se ha guardado.

Este tipo de código es importante porque ayuda a los usuarios a interactuar con datos de forma visual y sencilla, permitiéndoles agregar información fácilmente sin necesidad de lidiar directamente con archivos.

`020-Creo un componente text.py`

```python
import tkinter as tk

def insertaCliente():
  archivo = open("clientes.csv","a")
  archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
  archivo.close()
  

ventana = tk.Tk()

tk.Label(ventana,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(ventana)
nombre.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(ventana)
apellidos.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(ventana)
email.pack(padx=10,pady=2)

tk.Button(ventana,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

texto = tk.Text(ventana,height=5,width=30)
texto.pack(padx=10,pady=2)

ventana.mainloop()
```

### listar clientes
<small>Creado: 2025-10-16 16:17</small>

#### Explicación

Este código Python utiliza la biblioteca `tkinter` para crear una interfaz gráfica sencilla que permite añadir y listar clientes a partir de un archivo CSV. La interfaz incluye campos de entrada para el nombre, apellidos y email del cliente, así como un botón "Insertar un cliente" que guarda los datos en un archivo llamado `clientes.csv`. Cuando se inserta un nuevo cliente o cuando la aplicación se inicia, todos los clientes existentes del archivo CSV son cargados en una área de texto dentro de la interfaz gráfica. Esto permite a los usuarios ver la lista completa de clientes registrados.

El código define dos funciones principales: `insertaCliente()` y `listaClientes()`. La función `insertaCliente()` abre el archivo `clientes.csv` en modo de escritura (añadiendo al final) para guardar nuevos registros, mientras que `listaClientes()` lee todos los registros existentes del archivo CSV e inserta cada línea en un área de texto dentro de la interfaz gráfica. Esto ayuda a mantener una visión actualizada de los clientes registrados.

En resumen, este código proporciona una forma simple pero efectiva para gestionar una lista de clientes desde una interfaz gráfica básica utilizando Tkinter y archivos CSV.

`021-listar clientes.py`

```python
import tkinter as tk

def insertaCliente():
  archivo = open("clientes.csv","a")
  archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
  archivo.close()
  listaClientes()
  
def listaClientes():
  texto.delete(1.0,tk.END)
  archivo = open("clientes.csv","r")
  lineas = archivo.readlines()
  for linea in lineas:
    texto.insert(tk.END,linea)
  archivo.close()
  
ventana = tk.Tk()

tk.Label(ventana,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(ventana)
nombre.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(ventana)
apellidos.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(ventana)
email.pack(padx=10,pady=2)

tk.Button(ventana,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

texto = tk.Text(ventana,height=5,width=30)
texto.pack(padx=10,pady=2)

listaClientes()

ventana.mainloop()
```

### rejilla
<small>Creado: 2025-10-16 16:21</small>

#### Explicación

Este código crea una interfaz gráfica simple utilizando la biblioteca `tkinter` en Python. La aplicación principal es una ventana que contiene cuatro botones, cada uno con un texto diferente ("Pulsame1", "Pulsame2", etc.). Los botones se colocan automáticamente en la ventana gracias al método `.pack()`, que organiza los elementos de forma vertical por defecto, añadiendo espacios (padding) a izquierda y derecha (`padx`) y arriba y abajo (`pady`) para separar visualmente cada botón. Al ejecutar este código, se abre una ventana con los cuatro botones dispuestos uno debajo del otro, lo que facilita la interacción del usuario sin necesidad de disposiciones complejas.

Este tipo de diseño es sencillo y efectivo para interfaces básicas, permitiendo a los estudiantes centrarse en aprender cómo crear elementos gráficos antes de abordar técnicas más avanzadas de disposición.

`022-rejilla.py`

```python
import tkinter as tk
  
ventana = tk.Tk()

boton1 = tk.Button(text="Pulsame1")
boton1.pack(padx=10,pady=10)

boton2 = tk.Button(text="Pulsame2")
boton2.pack(padx=10,pady=10)

boton3 = tk.Button(text="Pulsame3")
boton3.pack(padx=10,pady=10)

boton4 = tk.Button(text="Pulsame4")
boton4.pack(padx=10,pady=10)

ventana.mainloop()
```

### rejilla en lugar de pack
<small>Creado: 2025-10-16 16:23</small>

#### Explicación

Este código crea una interfaz gráfica simple utilizando la biblioteca `tkinter` en Python. La ventana principal se inicializa con el comando `tk.Tk()`, lo que genera una nueva ventana en tu pantalla.

El código luego define cuatro botones, cada uno con un texto diferente: "Pulsame1", "Pulsame2", "Pulsame3" y "Pulsame4". Estos botones se ubican dentro de la ventana principal usando el método `grid()`, que permite organizar los elementos en una cuadrícula. Los dos primeros botones, "Pulsame1" y "Pulsame2", están en la fila 0, columna 0 y columna 1 respectivamente; mientras que los dos últimos botones, "Pulsame3" y "Pulsame4", se colocan en la fila 1, columna 0 y columna 1.

El uso de `grid()` es muy importante porque permite organizar elementos de forma estructurada en filas y columnas, lo cual facilita el diseño y mantenimiento de interfaces gráficas más complejas. Al final del código, se llama a la función `ventana.mainloop()`, que inicia un bucle de eventos para mantener abierta la ventana hasta que el usuario decida cerrarla.

Este ejemplo es fundamental para entender cómo posicionar elementos en una interfaz gráfica con Tkinter y cómo estructurar visualmente los componentes.

`023-rejilla en lugar de pack.py`

```python
import tkinter as tk
  
ventana = tk.Tk()

boton1 = tk.Button(text="Pulsame1")
boton1.grid(row=0,column=0)

boton2 = tk.Button(text="Pulsame2")
boton2.grid(row=0,column=1)

boton3 = tk.Button(text="Pulsame3")
boton3.grid(row=1,column=0)

boton4 = tk.Button(text="Pulsame4")
boton4.grid(row=1,column=1)

ventana.mainloop()
```

### replanteo la interfaz
<small>Creado: 2025-10-16 16:24</small>

#### Explicación

Este código es una aplicación sencilla que usa la biblioteca `tkinter` para crear una interfaz gráfica en Python. La función principal de esta aplicación es permitir al usuario introducir datos sobre clientes (nombre, apellidos y email) y guardar estos datos en un archivo CSV llamado "clientes.csv". Además, muestra los registros existentes del archivo CSV en una sección de texto dentro de la misma interfaz.

Cuando el usuario introduce los datos y presiona el botón "Insertar un cliente", los datos son añadidos al final del archivo "clientes.csv" con cada dato separado por comas. Luego, la función `listaClientes()` es llamada automáticamente para actualizar la vista de texto en la interfaz y mostrar todos los registros existentes en el archivo CSV.

La parte importante de este código es cómo se maneja la interacción entre la ventana gráfica y las operaciones de lectura/escritura del archivo. Las etiquetas (`tk.Label`), cuadros de entrada (`tk.Entry`) y botones (`tk.Button`) proporcionan una forma amigable para que el usuario introduzca los datos, mientras que funciones como `insertaCliente()` y `listaClientes()` manejan la lógica subyacente.

Este tipo de aplicación es útil en situaciones donde necesitas capturar información de entrada del usuario y guardarla permanentemente. Además, muestra cómo integrar operaciones de archivo con una interfaz gráfica para proporcionar un flujo de trabajo más fluido y conveniente para el usuario final.

`024-replanteo la interfaz.py`

```python
import tkinter as tk

def insertaCliente():
  archivo = open("clientes.csv","a")
  archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
  archivo.close()
  listaClientes()
  
def listaClientes():
  texto.delete(1.0,tk.END)
  archivo = open("clientes.csv","r")
  lineas = archivo.readlines()
  for linea in lineas:
    texto.insert(tk.END,linea)
  archivo.close()
  
ventana = tk.Tk()

tk.Label(ventana,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(ventana)
nombre.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(ventana)
apellidos.pack(padx=10,pady=2)

tk.Label(ventana,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(ventana)
email.pack(padx=10,pady=2)

tk.Button(ventana,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

texto = tk.Text(ventana,height=5,width=30)
texto.pack(padx=10,pady=2)

listaClientes()

ventana.mainloop()
```

### contenedores
<small>Creado: 2025-10-16 16:26</small>

#### Explicación

Este fragmento de código en Python utiliza la biblioteca `tkinter` para crear una interfaz gráfica sencilla que permite a los usuarios introducir información sobre clientes y ver esa información registrada. 

El programa crea una ventana principal (`ventana = tk.Tk()`) donde se colocan dos contenedores principales: un marco (`marco1`) en la columna 0 y un área de texto (`texto`) en la columna 1. En el primer marco, el código añade tres etiquetas para pedir al usuario que introduzca el nombre, apellidos y email del cliente, junto con campos de entrada correspondientes a cada uno de estos datos. También incluye un botón que, cuando se presiona, llama a la función `insertaCliente()`. 

La función `insertaCliente()` abre el archivo `clientes.csv` en modo de escritura para añadir al final del mismo los valores introducidos por el usuario (nombre, apellidos y email), separados por comas. Luego, esta función llama a otra función llamada `listaClientes()`, que borra cualquier contenido anterior del área de texto (`texto.delete(1.0,tk.END)`) y lee todos los registros existentes en `clientes.csv`. Cada línea leída se inserta al final del área de texto, mostrando así una lista actualizada de clientes registrados.

Este código es importante porque demuestra cómo interactuar con archivos desde una interfaz gráfica sencilla y cómo organizar elementos en la ventana utilizando contenedores (`Frame`) para mantener un diseño limpio y fácil de entender.

`025-contenedores.py`

```python
import tkinter as tk

def insertaCliente():
  archivo = open("clientes.csv","a")
  archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
  archivo.close()
  listaClientes()
  
def listaClientes():
  texto.delete(1.0,tk.END)
  archivo = open("clientes.csv","r")
  lineas = archivo.readlines()
  for linea in lineas:
    texto.insert(tk.END,linea)
  archivo.close()
  
ventana = tk.Tk()

marco1 = tk.Frame()

tk.Label(marco1,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(marco1)
nombre.pack(padx=10,pady=2)

tk.Label(marco1,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(marco1)
apellidos.pack(padx=10,pady=2)

tk.Label(marco1,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(marco1)
email.pack(padx=10,pady=2)

tk.Button(marco1,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

marco1.grid(row=0,column=0)

texto = tk.Text(ventana,height=5,width=30)
texto.grid(row=0,column=1)

listaClientes()

ventana.mainloop()
```

### frame con label
<small>Creado: 2025-10-16 16:28</small>

#### Explicación

Este código crea una interfaz gráfica simple usando la biblioteca `tkinter` en Python. La aplicación permite a los usuarios ingresar información de un cliente (nombre, apellidos y email) y luego guarda esa información en un archivo CSV llamado "clientes.csv". Después de guardar el nuevo cliente, se actualiza automáticamente una zona de texto que muestra todos los clientes almacenados en el archivo.

La interfaz tiene dos partes principales: un marco donde ingresas la información del cliente y otra parte donde puedes ver una lista de todos los clientes registrados. Cuando haces clic en el botón "Insertar un cliente", se guarda la nueva entrada y se refresca automáticamente la lista para mostrar al nuevo cliente.

Este código es importante porque demuestra cómo manejar entradas de usuario, guardar información externamente y actualizar dinámicamente una interfaz gráfica. Es útil entender estos conceptos básicos antes de pasar a interfaces más complejas o aplicaciones con funcionalidades avanzadas.

`026-frame con label.py`

```python
import tkinter as tk

def insertaCliente():
  archivo = open("clientes.csv","a")
  archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
  archivo.close()
  listaClientes()
  
def listaClientes():
  texto.delete(1.0,tk.END)
  archivo = open("clientes.csv","r")
  lineas = archivo.readlines()
  for linea in lineas:
    texto.insert(tk.END,linea)
  archivo.close()
  
ventana = tk.Tk()

marco1 = tk.LabelFrame(text="Insertar un cliente")

tk.Label(marco1,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(marco1)
nombre.pack(padx=10,pady=2)

tk.Label(marco1,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(marco1)
apellidos.pack(padx=10,pady=2)

tk.Label(marco1,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(marco1)
email.pack(padx=10,pady=2)

tk.Button(marco1,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

marco1.grid(row=0,column=0,padx=10,pady=10)

texto = tk.Text(ventana,height=5,width=30)
texto.grid(row=0,column=1)

listaClientes()

ventana.mainloop()
```

### creamos un segundo marco
<small>Creado: 2025-10-16 16:30</small>

#### Explicación

Este código crea una interfaz gráfica sencilla usando la biblioteca `tkinter` en Python, que permite a los usuarios insertar y listar clientes. La ventana principal contiene dos marcos: uno para introducir información de un cliente nuevo y otro para mostrar la lista actualizada de todos los clientes registrados.

En el primer marco (marco1), hay campos de entrada para el nombre, apellidos y email del cliente junto con un botón que, al ser presionado, llama a la función `insertaCliente()`. Esta función abre el archivo "clientes.csv" en modo de escritura adicional (`a`), añade los datos ingresados por el usuario (nombre, apellidos y email) separados por comas, y luego cierra el archivo.

La segunda parte del código define la función `listaClientes()` que actualiza un área de texto ubicada dentro del segundo marco (marco2). Esta función abre "clientes.csv" en modo lectura (`r`), lee todas las líneas y las inserta al final del área de texto, mostrando así una lista ordenada de todos los clientes registrados hasta el momento.

El código también utiliza un bucle principal `ventana.mainloop()` que mantiene la interfaz gráfica activa y responde a los eventos generados por el usuario. Esta es una técnica común para interfaces gráficas en Python, permitiendo interactuar con ella de forma continua hasta que se cierra.

Esta práctica combina elementos básicos de programación orientada a objetos (POO) y manejo de archivos en un entorno gráfico interactivivo, lo cual es muy útil para comprender cómo las aplicaciones reales procesan y presentan información.

`027-creamos un segundo marco.py`

```python
import tkinter as tk

def insertaCliente():
  archivo = open("clientes.csv","a")
  archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
  archivo.close()
  listaClientes()
  
def listaClientes():
  texto.delete(1.0,tk.END)
  archivo = open("clientes.csv","r")
  lineas = archivo.readlines()
  for linea in lineas:
    texto.insert(tk.END,linea)
  archivo.close()
  
ventana = tk.Tk()

marco1 = tk.LabelFrame(text="Insertar un cliente")

tk.Label(marco1,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(marco1)
nombre.pack(padx=10,pady=2)

tk.Label(marco1,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(marco1)
apellidos.pack(padx=10,pady=2)

tk.Label(marco1,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(marco1)
email.pack(padx=10,pady=2)

tk.Button(marco1,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

marco1.grid(row=0,column=0)

marco2 = tk.LabelFrame(text="Listar clientes")

texto = tk.Text(marco2,height=5,width=30)
texto.pack(padx=10,pady=10)

marco2.grid(row=0,column=1,padx=10,pady=10)

listaClientes()

ventana.mainloop()
```

### ttkbootstrap
<small>Creado: 2025-10-16 16:34</small>

#### Explicación

Este código Python crea una interfaz gráfica simple utilizando la biblioteca `ttkbootstrap`, que es un complemento de `tkinter`. La aplicación permite al usuario introducir información de clientes (nombre, apellidos y email) y guardarla en un archivo CSV. También proporciona la funcionalidad para listar todos los clientes almacenados en este archivo.

El programa comienza creando una ventana principal con un tema llamado "vapor". Luego, se definen dos marcos principales: `marco1` y `marco2`. El primer marco (`marco1`) contiene campos de entrada (Entry) para el nombre, apellidos y email del cliente, así como un botón que al ser presionado guarda la información en un archivo CSV llamado "clientes.csv". La función `insertaCliente()` se encarga de abrir el archivo, escribir los datos proporcionados por el usuario y luego cerrar el archivo.

El segundo marco (`marco2`) contiene una caja de texto (Text) donde se lista toda la información almacenada en el archivo CSV. La función `listaClientes()` lee cada línea del archivo CSV e inserta esta información en la caja de texto, permitiendo al usuario visualizar todos los clientes registrados.

Esta interfaz es útil para aplicaciones que requieren mantener una base de datos simple y fácil de actualizar directamente desde un entorno gráfico.

`028-ttkbootstrap.py`

```python
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def insertaCliente():
  archivo = open("clientes.csv","a")
  archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
  archivo.close()
  listaClientes()
  
def listaClientes():
  texto.delete(1.0,tk.END)
  archivo = open("clientes.csv","r")
  lineas = archivo.readlines()
  for linea in lineas:
    texto.insert(tk.END,linea)
  archivo.close()
  
#ventana = tk.Tk()
ventana = tb.Window(themename = "vapor")

marco1 = tk.LabelFrame(text="Insertar un cliente")

tk.Label(marco1,text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(marco1)
nombre.pack(padx=10,pady=2)

tk.Label(marco1,text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(marco1)
apellidos.pack(padx=10,pady=2)

tk.Label(marco1,text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(marco1)
email.pack(padx=10,pady=2)

tk.Button(marco1,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

marco1.grid(row=0,column=0)

marco2 = tk.LabelFrame(text="Listar clientes")

texto = tk.Text(marco2,height=5,width=30)
texto.pack(padx=10,pady=10)

marco2.grid(row=0,column=1,padx=10,pady=10)

listaClientes()

ventana.mainloop()
```

### flask
<small>Creado: 2025-10-16 16:38</small>

#### Explicación

Este fragmento de código crea una aplicación web simple utilizando Flask, un marco ligero para Python que permite desarrollar aplicaciones web con facilidad. El código comienza importando la clase `Flask` desde el módulo flask.

Luego, se instancia un objeto llamado `aplicacion`, que es una instancia de la clase `Flask`. Este objeto representa tu aplicación web y el parámetro `__name__` indica a Flask cómo configurar la ruta para los recursos estáticos y las plantillas HTML. 

El código define una ruta principal ("/") con la función `raiz()`. Dentro de esta función, se crea un bloque de código HTML que incluye CSS para estilizar un campo de entrada (`input type="text"`). Este estilo añade sombreado al borde del campo de texto y le da un aspecto más atractivo. La función devuelve este bloque HTML como respuesta cuando alguien visita la página principal de tu aplicación.

Finalmente, si el script se está ejecutando directamente (no es importado como módulo en otro lugar), se llama al método `run()` del objeto `aplicacion` para iniciar el servidor web. Este servidor escucha en la dirección local (`127.0.0.1`) y utiliza el puerto 5000, además está habilitada la depuración para facilitar la identificación de errores durante el desarrollo.

Este código es importante porque demuestra cómo utilizar Flask para crear una aplicación web básica con capacidad para añadir estilos personalizados directamente en tu lógica de servidor.

`029-flask.py`

```python
from flask import Flask  

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
    <style>
      input{
        border:2px solid blue;
        padding:5px;
        box-shadow:0px 2px 4px rgba(0,0,0,0.3) inset;
        border-radius:100px;
        text-align:center;
        text-shadow:0px 2px 2px rgba(0,0,0,0.3);
      }
    </style>
    <input type="text">
  '''
  return cadena
  
if __name__ == "__main__":
  aplicacion.run(host="127.0.0.1", port=5000,debug=True)
```

### clientes
<small>Creado: 2025-10-16 16:18</small>

#### Explicación

El fragmento de código que has proporcionado no es realmente un bloque de código ejecutable ni una pieza de software. Es simplemente el contenido del archivo `clientes.csv`, que parece ser un archivo de texto plano utilizado para almacenar datos en formato CSV (Valores Separados por Comas). En este caso, cada línea contiene tres elementos idénticos separados por comas y rodeados de comillas, como "aaa", "bbb", "ccc" y así sucesivamente. Este tipo de archivo es comúnmente utilizado para almacenar datos tabulares, donde cada fila representa un registro o entrada y cada columna almacena una característica específica del registro (como nombre, apellido, edad, etc.).

Es importante entender que este archivo está siendo probablemente leído por algún programa en Python utilizando bibliotecas como `csv` o `pandas`, con el objetivo de manejar los datos relacionados con clientes. Esto puede ser parte de un ejercicio para aprender a leer y manipular archivos CSV usando interfaces gráficas en Python, posiblemente empleando la librería Tkinter u otras similares.

Este archivo es crucial porque proporciona los datos que el programa necesita para mostrar en una interfaz gráfica, almacenar información del usuario o realizar cualquier tipo de procesamiento con respecto a la lista de clientes.

`clientes.csv`

```
aaa,aaa,aaa
bbb,bbb,bbb
ccc,ccc,ccc
ddd,ddd,ddd
```

### clientes
<small>Creado: 2025-10-16 16:12</small>

#### Explicación

El fragmento de código que has proporcionado es una línea con tres valores separados por comas, cada uno representando "aaa". Este tipo de formato se conoce comúnmente como CSV (Valores Separados por Comas) o en este caso, un texto simple donde los datos están organizados de manera tabular. En el contexto del archivo `clientes.txt`, esta línea probablemente representa información básica sobre un cliente o podría ser una estructura simplificada para pruebas antes de agregar más detalles.

En programas que manejan archivos como éste, esta línea puede servir como un encabezado o como la entrada de datos para un único registro. Si es un archivo `.txt` usado en una aplicación de programación, probablemente estás trabajando con interfaces gráficas donde necesitas leer información de este archivo y mostrarla a los usuarios.

Es importante entender cómo se estructuran estos archivos porque permiten que tu programa maneje grandes cantidades de datos de manera eficiente. Aprender a leer y escribir en formatos como éste es fundamental cuando trabajas con bases de datos simples o archivado de información en aplicaciones más complejas.

`clientes.txt`

```
aaa,aaa,aaa
```

### Actividades propuestas

It appears you have a series of Python scripts and files related to creating graphical user interfaces (GUIs) using `tkinter` and `ttkbootstrap`, along with basic web development using Flask. You also have data files (`clientes.csv` and `clientes.txt`) that are used within your GUI application.

Let's break down each script in order:

### 1. **001-tkinter.py**
This is a simple `tkinter` window creation:
```python
import tkinter as tk

ventana = tk.Tk()
ventana.mainloop()
```
- This script creates and runs an empty Tk window.

### 2. **002-cuadro-de-texto.py**
Adding a text input widget to the Tk window:
```python
import tkinter as tk

def escribir(event):
    entrada.config(text="Texto: " + entrada.get())
    
ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack(pady=20)

boton = tk.Button(ventana, text="Escribir")
boton.bind("<Button-1>", escribir)
boton.pack()

ventana.mainloop()
```
- This script adds an entry widget (a text input box) and a button that displays the entered text when clicked.

### 3. **003-cuadro-de-texto-dos.py**
Improving the previous script by changing event handling:
```python
import tkinter as tk

def escribir():
    entrada.config(text="Texto: " + entrada.get())
    
ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack(pady=20)

boton = tk.Button(ventana, text="Escribir", command=escribir)
boton.pack()

ventana.mainloop()
```
- This script simplifies the event handling and uses a function to display the entered text.

### 4. **004-cuadro-de-texto-dos.py**
Adding functionality to clear input:
```python
import tkinter as tk

def escribir():
    entrada.config(text="Texto: " + entrada.get())

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack(pady=20)

boton1 = tk.Button(ventana, text="Escribir", command=escribir)
boton1.pack(side=tk.LEFT)

boton2 = tk.Button(ventana, text="Limpiar")
boton2.config(command=lambda: entrada.delete(0,"end"))
boton2.pack(side=tk.RIGHT)

ventana.mainloop()
```
- This script includes a button to clear the input field.

### 5. **006-cuadro-de-texto-tres.py**
Adding label and padding:
```python
import tkinter as tk

def escribir():
    entrada.config(text="Texto: " + entrada.get())

ventana = tk.Tk()

tk.Label(ventana, text="Escribe algo").pack(pady=20)
entrada = tk.Entry(ventana)
entrada.pack(padx=15)

boton1 = tk.Button(ventana, text="Escribir", command=escribir).pack(side=tk.LEFT,padx=2)
boton2 = tk.Button(ventana, text="Limpiar").pack(side=tk.RIGHT,padx=2)
#boton3 = tk.Button(ventana, text="Salir")
#boton3.pack(side=tk.BOTTOM,pady=5)

ventana.mainloop()
```
- This script adds padding around the entry and buttons.

### 6. **014-frame.py**
Using frames to organize widgets:
```python
import tkinter as tk

def escribir():
    entrada.config(text="Texto: " + entrada.get())

marco = tk.Frame()
marco.pack(padx=5,pady=5)

tk.Label(marco, text="Escribe algo").pack(pady=20)
entrada = tk.Entry(marco)
entrada.pack()

boton1 = tk.Button(marco, text="Escribir", command=escribir)
boton1.pack(side=tk.LEFT,padx=2)
boton2 = tk.Button(marco, text="Limpiar")
boton2.config(command=lambda: entrada.delete(0,"end"))
boton2.pack(side=tk.RIGHT,padx=2)

ventana.mainloop()
```
- This script organizes the widgets into a frame for better layout management.

### 7. **015-frame.py**
Further organizing widgets with frames:
```python
import tkinter as tk

def escribir():
    entrada.config(text="Texto: " + entrada.get())

marco = tk.Frame(relief=tk.SUNKEN)
marco.pack(padx=5,pady=5)

tk.Label(marco, text="Escribe algo").pack(pady=20)
entrada = tk.Entry(marco)
entrada.pack()

boton1 = tk.Button(marco, text="Escribir", command=escribir)
boton1.pack(side=tk.LEFT,padx=2)
boton2 = tk.Button(marco, text="Limpiar")
boton2.config(command=lambda: entrada.delete(0,"end"))
boton2.pack(side=tk.RIGHT,padx=2)

ventana.mainloop()
```
- This script adds a border to the frame and uses padding.

### 8. **016-label-frame.py**
Using `LabelFrame` for better organization:
```python
import tkinter as tk

def escribir():
    entrada.config(text="Texto: " + entrada.get())

marco = tk.LabelFrame(text="Prueba de Label Frame")
marco.pack(padx=5,pady=5)

tk.Label(marco, text="Escribe algo").pack(pady=20)
entrada = tk.Entry(marco)
entrada.pack()

boton1 = tk.Button(marco, text="Escribir", command=escribir)
boton1.pack(side=tk.LEFT,padx=2)
boton2 = tk.Button(marco, text="Limpiar")
boton2.config(command=lambda: entrada.delete(0,"end"))
boton2.pack(side=tk.RIGHT,padx=2)

ventana.mainloop()
```
- This script uses `LabelFrame` to add a title and better manage widgets.

### 9. **017-label-frame.py**
Using multiple frames for layout management:
```python
import tkinter as tk

def escribir():
    entrada.config(text="Texto: " + entrada.get())

marco = tk.LabelFrame(text="Prueba de Label Frame")
marco.pack(padx=5,pady=5)

tk.Label(marco, text="Escribe algo").pack(pady=20)
entrada = tk.Entry(marco)
entrada.pack()

boton1 = tk.Button(marco, text="Escribir", command=escribir)
boton1.pack(side=tk.LEFT,padx=2)
boton2 = tk.Button(marco, text="Limpiar")
boton2.config(command=lambda: entrada.delete(0,"end"))
boton2.pack(side=tk.RIGHT,padx=2)

marco = tk.LabelFrame(text="Prueba de Label Frame 2", relief=tk.GROOVE)
marco.pack(padx=5,pady=5,side=tk.BOTTOM)

ventana.mainloop()
```
- This script uses multiple `LabelFrames` for better organization.

### 10. **028-ttkbootstrap.py**
Using `ttkbootstrap` to enhance the GUI:
```python
import tkinter as tk
import ttkbootstrap as tb

def insertaCliente():
    archivo = open("clientes.csv","a")
    archivo.write(nombre.get()+","+apellidos.get()+","+email.get()+"\n")
    archivo.close()
    listaClientes()

def listaClientes():
    texto.delete(1.0,tk.END)
    archivo = open("clientes.csv","r")
    lineas = archivo.readlines()
    for linea in lineas:
        texto.insert(tk.END,linea)
    archivo.close()

ventana = tb.Window(themename="vapor")

marco1 = tk.LabelFrame(text="Insertar un cliente")

tk.Label(marco1, text="Introduce el nombre del cliente").pack(padx=10,pady=2)
nombre = tk.Entry(marco1)
nombre.pack(padx=10,pady=2)

tk.Label(marco1, text="Introduce los apellidos del cliente").pack(padx=10,pady=2)
apellidos = tk.Entry(marco1)
apellidos.pack(padx=10,pady=2)

tk.Label(marco1, text="Introduce el email del cliente").pack(padx=10,pady=2)
email = tk.Entry(marco1)
email.pack(padx=10,pady=2)

tk.Button(marco1,text="Insertar un cliente",command=insertaCliente).pack(padx=10,pady=2)

marco1.grid(row=0,column=0)

marco2 = tk.LabelFrame(text="Listar clientes")

texto = tk.Text(marco2,height=5,width=30)
texto.pack(padx=10,pady=10)

marco2.grid(row=0,column=1,padx=10,pady=10)

listaClientes()

ventana.mainloop()
```
- This script uses `ttkbootstrap` to create a more visually appealing GUI with themes.

### Data Files
- **clientes.csv**: Contains customer data in CSV format.
  ```plaintext
  aaa,aaa,aaa
  bbb,bbb,bbb
  ccc,ccc,ccc
  ddd,ddd,ddd
  ```
  
- **clientes.txt**: A simple text file that appears to be empty or incomplete.

### Flask Application
The `001-tkinter.py` script is not related to the Flask application. However, if you need to create a web server using Flask, you could use something like:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Summary
Each of these scripts builds on the previous one to enhance GUI functionality, improve layout management, and use more advanced widgets like `LabelFrame` and themes from `ttkbootstrap`. The data files are used in some of the later scripts for storing customer information. If you need further assistance with a specific script or concept, feel free to ask! 🚀


<a id="concepto-de-evento"></a>
## Concepto de evento

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/008-Concepto%20de%20evento)

### Introducción a los ejercicios

### Comparación de las dos versiones del código:

1. **Estructura y Comentarios**:
   - La primera versión tiene comentarios más extensos y explicativos, lo que facilita la comprensión del código.
   - La segunda versión también incluye comentarios, pero son menos detallados.

2. **Separación de Responsabilidades**:
   - En la primera versión, las funciones `construir_where_y_params`, `llenar_tree` y otras están bien separadas en función de su responsabilidad.
   - En la segunda versión, las funciones y métodos se han integrado mejor para simplificar el flujo del código.

3. **Interfaz Gráfica**:
   - La primera versión tiene una interfaz más básica con un solo campo de búsqueda y botones "Limpiar" y "Buscar".
   - En la segunda versión, hay barra de filtros por columna que permite filtrar cada columna individualmente. Esto proporciona mayor flexibilidad en la búsqueda.

4. **Ordenación**:
   - La primera versión no incluye ordenación basada en columnas.
   - La segunda versión implementa ordenación automática cuando se hace clic en los encabezados de las columnas y también permite cambiar entre ASC y DESC manualmente.

5. **Dinámica del Estado**:
   - En la primera versión, el estado (como "Sin resultados aún.") no cambia dinámicamente.
   - La segunda versión actualiza el texto del estado en tiempo real según los filtros activos y la cantidad de resultados encontrados.

6. **Optimización de Consultas SQL**:
   - Ambas versiones utilizan LIKE para realizar búsquedas, pero la segunda versión utiliza una consulta más dinámica que puede ajustarse a diferentes columnas.
   
7. **Funcionalidades Adicionales**:
   - La primera versión no incluye copiar ruta completa al portapapeles al doble clic en un item del treeview.
   - La segunda versión implementa esta funcionalidad, proporcionando una interacción más sencilla con los resultados.

### Conclusiones:

- **Primera Versión**: Más básica pero bien documentada. Ideal para aquellos que quieren entender paso a paso cómo funciona la aplicación.
  
- **Segunda Versión**: Mejor en términos de flexibilidad y funcionalidades adicionales, aunque podría ser un poco menos fácil de leer inicialmente debido a la integración más estrecha entre componentes.

### Recomendaciones:

Si necesitas una versión muy clara para el aprendizaje o documentación, opta por la primera. Si prefieres una aplicación con mayor funcionalidad y que es más amigable con el usuario en términos de interacción, utiliza la segunda versión.

### repasamos tkinter
<small>Creado: 2025-10-23 15:00</small>

#### Explicación

Este código es muy básico y se utiliza para crear una ventana simple utilizando la biblioteca `tkinter` en Python. La línea `import tkinter as tk` importa el módulo `tkinter`, que es una biblioteca estándar de Python utilizada para crear interfaces gráficas de usuario (GUI por sus siglas en inglés). Se le da un alias 'tk' para hacer la escritura del código más concisa.

Luego, se crea una instancia de la clase `Tk` mediante el comando `ventana = tk.Tk()`. Esto genera una nueva ventana emergente en tu pantalla. Cada aplicación tkinter necesita tener al menos un objeto `Tk`, que actúa como la raíz o punto central de toda la interfaz gráfica.

Finalmente, se llama a `ventana.mainloop()` para iniciar el bucle principal del programa. Este método maneja eventos como clics del mouse y teclas presionadas. Mientras está en ejecución, espera interacciones del usuario con la ventana recién creada, permitiendo que esta permanezca abierta hasta que se cierre manualmente.

Este código es fundamental para entender cómo iniciar una aplicación simple con tkinter y es un buen punto de partida para empezar a aprender sobre interfaces gráficas en Python.

`001-repasamos tkinter.py`

```python
import tkinter as tk

ventana = tk.Tk()

ventana.mainloop()
```

### creamos tabla
<small>Creado: 2025-10-23 15:02</small>

#### Explicación

Este fragmento de código SQL crea una tabla llamada `clientes` en una base de datos. La tabla tiene cuatro columnas: `Identificador`, `nombre`, `apellidos` y `email`. 

La columna `Identificador` es del tipo `INTEGER` y actúa como la clave primaria de la tabla, lo que significa que cada registro en esta tabla tendrá un valor único en este campo. El uso de `AUTOINCREMENT` asegura que el sistema manejará automáticamente el incremento del número para cada nuevo registro que se inserte, lo que simplifica mucho el proceso de añadir nuevos clientes sin tener que preocuparse por proporcionar un identificador único.

Las columnas `nombre`, `apellidos` y `email` son del tipo `TEXT`, lo que significa que pueden almacenar cualquier texto, como nombres completos o direcciones de correo electrónico. Este diseño permite guardar información detallada sobre cada cliente de manera organizada y estructurada en la base de datos.

Crear esta tabla es un paso crucial para establecer una base sólida al trabajar con datos de clientes en aplicaciones que requieren almacenar y gestionar información personalizada por usuario.

`002-creamos tabla.sql`

```sql
CREATE TABLE "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
```

### formulario
<small>Creado: 2025-10-23 15:05</small>

#### Explicación

Este código Python utiliza la biblioteca `tkinter` para crear una interfaz gráfica sencilla que permite al usuario ingresar información sobre un cliente. La ventana principal se crea con el comando `tk.Tk()`, lo que inicia la aplicación.

En seguida, se añaden tres cuadros de entrada (Entry) a la ventana: uno para el nombre del cliente, otro para los apellidos y otro para el correo electrónico. Cada cuadro de entrada se coloca en la pantalla usando el método `pack()`, que también agrega un margen de 20 píxeles alrededor de cada cuadro tanto horizontal como verticalmente, lo cual mejora la legibilidad y hace más agradable la interfaz.

Por último, se añade un botón a la ventana con el texto "Insertar cliente". Este botón también se posiciona en la pantalla utilizando `pack()`.

El bucle principal de la aplicación (`ventana.mainloop()`) asegura que la ventana permanezca abierta y responda adecuadamente a cualquier interacción del usuario, como mover ventanas o cerrarla. El programa seguirá ejecutándose hasta que el usuario cierre manualmente la ventana.

Este tipo de interfaz es común en aplicaciones donde se necesitan recoger datos del usuario antes de realizar alguna acción con ellos, como insertar un nuevo cliente en una base de datos.

`003.formulario.py`

```python
import tkinter as tk

ventana = tk.Tk()

nombre = tk.Entry(ventana)
nombre.pack(padx = 20,pady = 20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx = 20,pady = 20)

email = tk.Entry(ventana)
email.pack(padx = 20,pady = 20)

boton = tk.Button(ventana,text="Insertar cliente")
boton.pack(padx = 20,pady = 20)

ventana.mainloop()
```

### comando del boton
<small>Creado: 2025-10-23 15:05</small>

#### Explicación

Este fragmento de código crea una interfaz gráfica simple usando la biblioteca `tkinter` en Python. La ventana principal se inicia con `ventana = tk.Tk()`. Luego, el programa añade tres cuadros de texto (Entry) para ingresar el nombre, apellidos y email del usuario, cada uno de los cuales es colocado dentro de la ventana con un margen de 20 píxeles en las direcciones horizontal (`padx`) y vertical (`pady`). 

Después, se añade un botón que dice "Insertar cliente". Este botón tiene asociado una acción llamada `insertaCliente`, lo cual significa que cuando el usuario hace clic en el botón, la función `insertaCliente` será ejecutada. Esta función (que no está definida en este código) probablemente se encargará de tomar los datos ingresados por el usuario y hacer algo con ellos, como guardarlos en una base de datos o procesarlos de alguna manera.

Finalmente, `ventana.mainloop()` inicia un ciclo principal que permite a la ventana detectar eventos del usuario (como clics del mouse) y actualizar su estado según sea necesario. Este método es crucial para mantener abierta la ventana y responder a las interacciones del usuario hasta que esta sea cerrada manualmente.

`004-comando del boton.py`

```python
import tkinter as tk

ventana = tk.Tk()

nombre = tk.Entry(ventana)
nombre.pack(padx = 20,pady = 20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx = 20,pady = 20)

email = tk.Entry(ventana)
email.pack(padx = 20,pady = 20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx = 20,pady = 20)

ventana.mainloop()
```

### defino la funcion de insercion
<small>Creado: 2025-10-23 15:06</small>

#### Explicación

Este código crea una simple interfaz gráfica de usuario (GUI) utilizando la biblioteca Tkinter en Python. La función principal es permitir al usuario ingresar datos sobre un cliente, como nombre, apellidos y email, y luego insertar estos datos cuando se presiona el botón "Insertar cliente".

El programa comienza creando una ventana básica con `tk.Tk()`. Luego, define tres campos de entrada (Entry) para que el usuario pueda introducir el nombre, los apellidos y el email del cliente. Cada uno de estos elementos es empaquetado (`pack`) en la ventana principal, añadiendo un margen (`padx`, `pady`) para mejorar su visualización.

Además, se define una función llamada `insertaCliente()` que por ahora simplemente imprime un mensaje ("Voy a insertar un cliente") cuando el botón asociado con ella es clickeado. Esta función no realiza ninguna operación real de inserción en este momento, pero establece la estructura para futuras implementaciones donde realmente se insertarían los datos del cliente.

Finalmente, se llama al método `mainloop()` sobre la ventana, lo que mantiene el programa ejecutándose y permite que Tkinter maneje eventos como clics de ratón y entradas de teclado.

`005-defino la funcion de insercion.py`

```python
import tkinter as tk

ventana = tk.Tk()

def insertaCliente():
  print("Voy a insertar un cliente")

nombre = tk.Entry(ventana)
nombre.pack(padx = 20,pady = 20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx = 20,pady = 20)

email = tk.Entry(ventana)
email.pack(padx = 20,pady = 20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx = 20,pady = 20)

ventana.mainloop()
```

### abro base de datos e inserto
<small>Creado: 2025-10-23 15:09</small>

#### Explicación

Este fragmento de código en Python crea una sencilla interfaz gráfica utilizando la librería `tkinter`, y permite a un usuario insertar datos de un cliente (nombre, apellidos y email) en una base de datos SQLite. 

Primero, el programa conecta con una base de datos llamada "clientes.db" y crea un cursor para ejecutar comandos SQL. Luego, se inicializa la ventana principal usando `tk.Tk()`.

El código define una función llamada `insertaCliente()`, que cuando es llamada insertará automáticamente un nuevo registro en la tabla "clientes" de la base de datos, pero sin llenar los campos con ningún dato específico (los valores por defecto son cadenas vacías).

En la ventana principal, se crean tres campos de entrada (`Entry`) para el nombre, apellidos y email del cliente. Estos campos permiten al usuario ingresar datos manualmente.

Finalmente, se añade un botón a la interfaz que llama a la función `insertaCliente()` cuando es presionado por el usuario. Este botón facilita la inserción de nuevos registros en la base de datos directamente desde la interfaz gráfica.

Este código es importante porque demuestra cómo interactuar con una base de datos SQLite y cómo crear interfaces gráficas sencillas utilizando `tkinter`, combinando dos tecnologías importantes para el desarrollo web y aplicaciones móviles.

`006-abro base de datos e inserto.py`

```python
import tkinter as tk
import sqlite3

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor()

ventana = tk.Tk()

def insertaCliente():
  cursor.execute('INSERT INTO clientes VALUES(NULL,"","","")')
  conexion.commit()

nombre = tk.Entry(ventana)
nombre.pack(padx = 20,pady = 20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx = 20,pady = 20)

email = tk.Entry(ventana)
email.pack(padx = 20,pady = 20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx = 20,pady = 20)

ventana.mainloop()
```

### inserto de verdad
<small>Creado: 2025-10-23 15:11</small>

#### Explicación

Este código es una pequeña aplicación en Python que utiliza las bibliotecas `tkinter` y `sqlite3`. La aplicación crea una ventana sencilla donde un usuario puede ingresar el nombre, apellidos y email de un cliente. Cuando se presiona el botón "Insertar cliente", la información ingresada se inserta en una base de datos SQLite.

El código comienza conectándose a una base de datos SQLite llamada `clientes.db` y crea un cursor para ejecutar comandos SQL. Luego, se inicializa una ventana con `tk.Tk()`. Dentro de esta ventana, el código define tres campos de entrada (`Entry`) donde el usuario puede introducir el nombre, apellidos y email del cliente.

El botón "Insertar cliente" está vinculado a la función `insertaCliente()`, que toma los valores ingresados en los campos de entrada y los inserta como un nuevo registro en una tabla llamada `clientes`. Este comando SQL se ejecuta usando el cursor, y luego se hace commit para guardar los cambios en la base de datos.

Esta aplicación es útil porque demuestra cómo interactuar con una base de datos desde una interfaz gráfica simple utilizando Python.

`007-inserto de verdad.py`

```python
import tkinter as tk
import sqlite3

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor()

ventana = tk.Tk()

def insertaCliente():
  cursor.execute('INSERT INTO clientes VALUES(NULL,"'+nombre.get()+'","'+apellidos.get()+'","'+email.get()+'")')
  conexion.commit()

nombre = tk.Entry(ventana)
nombre.pack(padx = 20,pady = 20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx = 20,pady = 20)

email = tk.Entry(ventana)
email.pack(padx = 20,pady = 20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx = 20,pady = 20)

ventana.mainloop()
```

### ttkbootstrap
<small>Creado: 2025-10-23 15:18</small>

#### Explicación

Este fragmento de código es un ejemplo básico de una aplicación en Python que utiliza la biblioteca `ttkbootstrap` para crear una interfaz gráfica sencilla con el estilo "darkly". El objetivo principal del programa es permitir al usuario insertar datos de clientes en una base de datos SQLite.

El código comienza por importar las bibliotecas necesarias, incluyendo `tkinter`, `sqlite3` y `ttkbootstrap`. Luego, establece una conexión a la base de datos SQLite llamada "clientes.db" y crea un cursor para ejecutar consultas SQL. A diferencia del uso común de `Tk()` en tkinter, aquí se utiliza `tb.Window(themename="darkly")` que proporciona una ventana con un tema oscuro.

En el cuerpo principal del programa, se crean tres campos de entrada (`Entry`) donde el usuario puede ingresar los datos del cliente: nombre, apellidos y email. Estos campos son ubicados en la ventana mediante `pack()`, especificando márgenes para espaciar visualmente los elementos. 

Además, se define una función llamada `insertaCliente()` que toma los valores de los campos de entrada (`nombre`, `apellidos` y `email`) y ejecuta una consulta SQL para insertar estos datos en la tabla "clientes" de la base de datos. Finalmente, un botón es creado con el texto "Insertar cliente", vinculado a esta función mediante `command=insertaCliente`. Cuando se hace clic en este botón, se llama automáticamente a la función `insertaCliente()`.

Este código es importante para aprender cómo interactuar entre interfaces gráficas y bases de datos en aplicaciones Python, además de introducir el uso del tema oscuro proporcionado por `ttkbootstrap` para mejorar la estética de las aplicaciones.

`008-ttkbootstrap.py`

```python
import tkinter as tk
import sqlite3
import ttkbootstrap as tb
from ttkbootstrap import ttk

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor()

#ventana = tk.Tk()
ventana = tb.Window(themename="darkly")

def insertaCliente():
  cursor.execute('INSERT INTO clientes VALUES(NULL,"'+nombre.get()+'","'+apellidos.get()+'","'+email.get()+'")')
  conexion.commit()

nombre = tk.Entry(ventana)
nombre.pack(padx = 20,pady = 20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx = 20,pady = 20)

email = tk.Entry(ventana)
email.pack(padx = 20,pady = 20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx = 20,pady = 20)

ventana.mainloop()
```

### indexador parte 1
<small>Creado: 2025-10-23 15:22</small>

#### Explicación

Este código es un ejemplo básico de cómo se inicializa y ejecuta una aplicación sencilla con la biblioteca `tkinter` en Python. La primera línea importa el módulo `tkinter`, que es utilizado para crear interfaces gráficas de usuario (GUI). Luego, se crea una ventana principal utilizando `tk.Tk()`. Finalmente, `ventana.mainloop()` inicia el bucle principal del programa, lo cual permite que la aplicación interactúe con los eventos generados por el usuario, como clics de ratón o pulsaciones de teclas. Este bucle es crucial porque mantiene a la aplicación en ejecución y responde a las interacciones del usuario hasta que se cierra la ventana.

`009-indexador parte 1.py`

```python
import tkinter as tk

ventana = tk.Tk()


ventana.mainloop()
```

### insertar carpeta
<small>Creado: 2025-10-23 15:24</small>

#### Explicación

Este código Python utiliza la biblioteca `tkinter` para crear una interfaz gráfica de usuario (GUI) simple que solicita al usuario que ingrese el nombre de una carpeta y un disco. La ventana principal se crea con `ventana = tk.Tk()`.

El código añade dos etiquetas (`Label`) a la ventana, cada una solicitando diferentes piezas de información: el nombre de la carpeta a indexar y el nombre del disco. Ambas etiquetas están seguidas por un campo de entrada de texto (`Entry`), donde el usuario puede escribir la respuesta.

Además, se añade un botón con el texto "Procesar" que probablemente debería tener una función `procesar()` asociada para manejar lo que ocurre después de que el usuario presione el botón. Sin embargo, en este fragmento falta definir esta función, y por tanto la aplicación no funcionará correctamente.

Finalmente, se llama a `ventana.mainloop()`, lo cual es crucial porque hace que la ventana sea visible e interactuable para el usuario, permitiendo así la entrada de datos y la respuesta al evento del botón.

`010-insertar carpeta.py`

```python
import tkinter as tk

ventana = tk.Tk()

tk.Label("Indica el nombre de la carpeta a indexar").pack(padx = 20,pady = 20)
carpeta = tk.Entry()
carpeta.pack(padx = 20,pady = 20)

tk.Label("Indica el nombre del disco").pack(padx = 20,pady = 20)
disco = tk.Entry()
disco.pack(padx = 20,pady = 20)

tk.Button(text="Procesar",command = procesar)

ventana.mainloop()
```

### ejecuto comando
<small>Creado: 2025-10-23 15:25</small>

#### Explicación

Este código Python utiliza la biblioteca `tkinter` para crear una interfaz gráfica simple que permite al usuario ingresar información y ejecutar un comando. La aplicación crea una ventana donde se muestran dos etiquetas y dos campos de entrada (entradas), uno para el nombre de la carpeta a indexar y otro para el nombre del disco. Además, hay un botón "Procesar" que, cuando se hace clic, llama a una función llamada `procesar()`, que en este caso solo imprime en la consola el mensaje "Voy a procesar". 

El código establece cómo los elementos de la interfaz (etiquetas, campos de entrada y botones) deben estar posicionados en la ventana mediante el uso del método `.pack()` con márgenes (`padx` para margen horizontal y `pady` para vertical). Esto ayuda a organizar visualmente los elementos en la pantalla.

Este tipo de interfaz es importante porque permite al usuario interactuar directamente con un programa, ingresando datos y ejecutando acciones específicas. Es una parte fundamental del desarrollo de aplicaciones que necesitan interacción humana.

`011-ejecuto comando.py`

```python
import tkinter as tk

ventana = tk.Tk()

def procesar():
  print("Voy a procesar")

tk.Label(text="Indica el nombre de la carpeta a indexar").pack(padx = 20,pady = 20)
carpeta = tk.Entry()
carpeta.pack(padx = 20,pady = 20)

tk.Label(text="Indica el nombre del disco").pack(padx = 20,pady = 20)
disco = tk.Entry()
disco.pack(padx = 20,pady = 20)

tk.Button(text="Procesar",command = procesar).pack(padx = 20,pady = 20)

ventana.mainloop()
```

### sql crear discos
<small>Creado: 2025-10-23 15:27</small>

#### Explicación

Este fragmento de código SQL se utiliza para crear una tabla en una base de datos. La tabla se llama "archivos" y tiene varias columnas que almacenan información sobre archivos específicos, como su identificador único, ubicación en el disco, tamaño, y fechas de creación y modificación.

- **identificador**: Es un número entero (INTEGER) que funciona como clave primaria. AUTOINCREMENT asegura que cada nuevo registro tenga un valor único e incremental automáticamente.
- **disco**, **ruta**, **archivo**, **tamanio**, **creacion** y **modificacion**: Estas son columnas de texto (TEXT) donde se almacenan detalles sobre el archivo, como la ubicación del disco en el que reside, la ruta completa al archivo, su nombre, tamaño en formato de cadena, y fechas de creación y modificación.

Esta tabla es importante porque permite organizar y almacenar datos estructurados relacionados con archivos en un sistema informático, facilitando operaciones como búsqueda, filtrado y análisis posterior.

`012-sql crear discos.sql`

```sql
CREATE TABLE "archivos" (
	"identificador"	INTEGER,
	"disco"	TEXT,
	"ruta"	TEXT,
	"archivo"	TEXT,
	"tamanio"	TEXT,
	"creacion"	TEXT,
	"modificacion"	TEXT,
	PRIMARY KEY("identificador" AUTOINCREMENT)
);
```

### insertar
<small>Creado: 2025-10-23 15:32</small>

#### Explicación

Este código es una pequeña aplicación de interfaz gráfica que utiliza la biblioteca `tkinter` para interactuar con el usuario. Su función principal es recoger los datos introducidos por el usuario en dos campos: uno para especificar la ruta de una carpeta y otro para indicar un nombre de disco, y luego procesar esa información para insertar registros en una base de datos SQLite.

El programa primero establece una conexión con una base de datos llamada `discos.db` y crea un cursor (`cur`) que se utiliza para ejecutar comandos SQL. Luego, recorre todos los archivos dentro de la carpeta especificada por el usuario utilizando la función `os.walk()`. Para cada archivo encontrado, obtiene su tamaño en bytes y las fechas de creación y modificación desde el sistema operativo, convirtiéndolas a un formato estándar. Estas informaciones se insertan en una tabla llamada `archivos` dentro de la base de datos SQLite, con campos para el nombre del disco, ruta, nombre del archivo, tamaño, fecha de creación y modificación.

Esta aplicación es útil porque permite indexar automáticamente toda la información sobre los archivos de un directorio específico a través de una interfaz gráfica simple. Esto puede ser muy valioso para hacer inventarios o backups de datos de manera sistemática en sistemas informáticos más grandes.

`013-insertar.py`

```python
import tkinter as tk
import os
import sqlite3
from datetime import datetime

ventana = tk.Tk()

def procesar():
    carpeta_inicial = carpeta.get().strip()
    nombre_disco = disco.get().strip()

    if not carpeta_inicial or not os.path.isdir(carpeta_inicial) or not nombre_disco:
        print("Carpeta o disco no válidos")
        return

    conn = sqlite3.connect("discos.db")
    cur = conn.cursor()

    for raiz, subdirs, archivos in os.walk(carpeta_inicial):
        for arch in archivos:
            ruta_completa = os.path.join(raiz, arch)
            try:
                tamanio = os.path.getsize(ruta_completa)
                creacion = datetime.fromtimestamp(os.path.getctime(ruta_completa)).isoformat(timespec="seconds")
                modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa)).isoformat(timespec="seconds")

                cur.execute(
                    "INSERT INTO archivos (disco, ruta, archivo, tamanio, creacion, modificacion) VALUES (?,?,?,?,?,?)",
                    (nombre_disco, raiz, arch, str(tamanio), creacion, modificacion)
                )
            except Exception as e:
                # si algún archivo no se puede leer, lo saltamos
                continue

    conn.commit()
    conn.close()
    print("Proceso completado")


tk.Label(text="Indica el nombre de la carpeta a indexar").pack(padx = 20,pady = 20)
carpeta = tk.Entry()
carpeta.pack(padx = 20,pady = 20)

tk.Label(text="Indica el nombre del disco").pack(padx = 20,pady = 20)
disco = tk.Entry()
disco.pack(padx = 20,pady = 20)

tk.Button(text="Procesar",command = procesar).pack(padx = 20,pady = 20)

ventana.mainloop()
```

### tree
<small>Creado: 2025-10-23 15:42</small>

#### Explicación

Este fragmento de código es una aplicación sencilla utilizando la biblioteca `tkinter` en Python para crear una interfaz gráfica que muestra información tabulada. La aplicación crea un componente llamado `Treeview`, que es similar a una tabla, donde puedes visualizar datos estructurados y realizar acciones sobre ellos.

El código inicializa una lista `DATA` con información de productos, incluyendo ID, nombre del producto y precio en euros. Luego, define una función `make_table()` que construye la interfaz gráfica. Dentro de esta función se crea un marco (`frm`) que contiene el `Treeview`. Se añade también un control deslizante vertical para navegar por los datos cuando haya demasiados para mostrar en pantalla.

El componente `Treeview` tiene tres columnas: ID, Producto y Precio (€). La función configura encabezados para cada columna y permite ordenarlos al hacer clic. Los registros de la lista `DATA` se insertan en el `Treeview`, alternando entre dos estilos diferentes de fila ("odd" y "even") para mejorar la legibilidad.

Además, el código incluye un manejador de eventos que imprime los valores del registro seleccionado cuando se hace doble clic sobre una fila. Finalmente, el programa define una función auxiliar `sort_by()` que permite ordenar las filas del `Treeview` al hacer clic en los encabezados de columna.

Este tipo de aplicación es importante porque muestra cómo crear interfaces tabulares interactivas utilizando Python y Tkinter, lo cual es útil para presentar datos estructurados a los usuarios de una manera clara y manejable.

`014-tree.py`

```python
#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

DATA = [
    (1, "Manzana", 0.99),
    (2, "Banana", 0.59),
    (3, "Cereza", 2.49),
    (4, "Durazno", 1.49),
    (5, "Uva", 2.99),
    (6, "Kiwi", 1.09),
    (7, "Mango", 1.89),
    (8, "Naranja", 0.79),
    (9, "Pera", 1.19),
    (10, "Sandía", 3.99),
]

def make_table(root):
    root.title("Minimal Treeview Table (Tkinter)")

    # --- container frame
    frm = ttk.Frame(root, padding=8)
    frm.grid(sticky="nsew")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # --- treeview (table)
    columns = ("id", "producto", "precio")
    tree = ttk.Treeview(frm, columns=columns, show="headings", height=12)
    tree.grid(row=0, column=0, sticky="nsew")

    # --- scrollbar
    vsb = ttk.Scrollbar(frm, orient="vertical", command=tree.yview)
    vsb.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=vsb.set)

    # --- table sizing behavior
    frm.rowconfigure(0, weight=1)
    frm.columnconfigure(0, weight=1)

    # --- headings & columns
    tree.heading("id", text="ID", command=lambda c="id": sort_by(tree, c))
    tree.heading("producto", text="Producto", command=lambda c="producto": sort_by(tree, c))
    tree.heading("precio", text="Precio (€)", command=lambda c="precio": sort_by(tree, c))

    tree.column("id", width=60, anchor="e")
    tree.column("producto", width=200, anchor="w")
    tree.column("precio", width=100, anchor="e")

    # --- striped rows
    tree.tag_configure("odd", background="#f7f7f7")
    tree.tag_configure("even", background="#ffffff")

    # --- populate
    for i, row in enumerate(DATA):
        tags = ("even",) if i % 2 == 0 else ("odd",)
        tree.insert("", "end", values=row, tags=tags)

    # --- double click handler
    def on_open(event):
        item_id = tree.focus()
        if not item_id:
            return
        print("Selected row:", tree.item(item_id, "values"))

    tree.bind("<Double-1>", on_open)

    return tree

# --- sorting helper
_sort_state = {}  # column -> bool (True asc, False desc)
def sort_by(tree: ttk.Treeview, column: str):
    # Extract column values
    rows = [(tree.set(k, column), k) for k in tree.get_children("")]
    # Try numeric sort if possible, else lexical (casefold for nicer results)
    def cast(x):
        try:
            return float(x.replace(",", "."))
        except Exception:
            return x.casefold()
    rows.sort(key=lambda t: cast(t[0]), reverse=_sort_state.get(column, False))
    _sort_state[column] = not _sort_state.get(column, False)

    # Reinsert in new order
    for index, (_, iid) in enumerate(rows):
        tree.move(iid, "", index)

if __name__ == "__main__":
    root = tk.Tk()
    make_table(root)
    root.mainloop()
```

### arbol sencillo
<small>Creado: 2025-10-23 15:46</small>

#### Explicación

Este código crea una interfaz gráfica sencilla usando la biblioteca `tkinter` en Python. La aplicación muestra un árbol de datos (Treeview) que es similar a una tabla con varias columnas donde puedes organizar información jerárquicamente o simplemente como una lista estructurada.

El código comienza importando las librerías necesarias y definiendo algunos datos de ejemplo en forma de tuplas, donde cada tupla representa un artículo con su ID, nombre y precio. Luego, se crea una ventana principal utilizando `tk.Tk()` que será el contenedor para nuestro árbol.

A continuación, se inicializa el componente Treeview dentro de esta ventana, configurándolo con las columnas "id", "producto" y "precio". Después, se establece el texto para cada columna en la parte superior del árbol (es decir, se configuran los encabezados).

Finalmente, el bucle `for` recorre todas las tuplas de datos e inserta una fila nueva al final del Treeview con estos valores. Al llamar a `ventana.mainloop()`, se ejecuta un bucle infinito que maneja eventos en la interfaz gráfica, permitiendo así que la ventana esté siempre lista para recibir interacciones del usuario.

Este tipo de estructura es útil cuando necesitas mostrar datos tabulares o jerárquicos de manera clara y manejable.

`015-arbol sencillo.py`

```python
#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

# Datos de muestra
datos = [
    (1, "Manzana", 0.99),
    (2, "Banana", 0.59),
    (3, "Cereza", 2.49),
    (4, "Durazno", 1.49),
]

ventana = tk.Tk()

# Creo una vista de arbol que me sirve para jerarquias y para tablas
columnas = ("id", "producto", "precio")
arbol = ttk.Treeview(ventana, columns=columnas)

# --- Defino las cabeceras
arbol.heading("id", text="ID")
arbol.heading("producto", text="Producto")
arbol.heading("precio", text="Precio (€)")


for fila in datos:
    arbol.insert("", "end", values=fila)

arbol.pack(padx=10, pady=10)

ventana.mainloop()
```

### recuperamos aplicacion discos
<small>Creado: 2025-10-23 15:47</small>

#### Explicación

Este código es una aplicación simple en Python que utiliza la biblioteca `tkinter` para crear una interfaz gráfica de usuario (GUI) y permite al usuario ingresar el nombre de un directorio y el nombre de un disco. La función principal del programa es recorrer todos los archivos dentro del directorio especificado, obtener información sobre cada archivo como su tamaño y fechas de creación y modificación, e insertar esta información en una base de datos SQLite.

El código comienza importando las bibliotecas necesarias para manejar la GUI (`tkinter`), el sistema operativo (`os`), y las bases de datos SQLite (`sqlite3`). Además, se utiliza la clase `datetime` para trabajar con fechas. La función principal del programa es la función `procesar()`, que primero obtiene los valores introducidos por el usuario en dos campos de entrada: uno para el nombre de la carpeta a indexar y otro para el nombre del disco.

Si los datos ingresados son válidos, el código establece una conexión con una base de datos SQLite llamada "discos.db". Luego, utilizando `os.walk()`, recorre todos los archivos en el directorio especificado por el usuario. Para cada archivo encontrado, se extrae información como su tamaño y las fechas de creación y modificación. Esta información se guarda en la tabla "archivos" de la base de datos SQLite.

El uso de esta aplicación es importante para mantener un registro detallado de todos los archivos dentro de un directorio específico, lo que puede ser útil para el seguimiento del almacenamiento, la administración de sistemas o incluso auditorías.

`016-recuperamos aplicacion discos.py`

```python
import tkinter as tk
import os
import sqlite3
from datetime import datetime

ventana = tk.Tk()

def procesar():
    carpeta_inicial = carpeta.get().strip()
    nombre_disco = disco.get().strip()

    if not carpeta_inicial or not os.path.isdir(carpeta_inicial) or not nombre_disco:
        print("Carpeta o disco no válidos")
        return

    conn = sqlite3.connect("discos.db")
    cur = conn.cursor()

    for raiz, subdirs, archivos in os.walk(carpeta_inicial):
        for arch in archivos:
            ruta_completa = os.path.join(raiz, arch)
            try:
                tamanio = os.path.getsize(ruta_completa)
                creacion = datetime.fromtimestamp(os.path.getctime(ruta_completa)).isoformat(timespec="seconds")
                modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa)).isoformat(timespec="seconds")

                cur.execute(
                    "INSERT INTO archivos (disco, ruta, archivo, tamanio, creacion, modificacion) VALUES (?,?,?,?,?,?)",
                    (nombre_disco, raiz, arch, str(tamanio), creacion, modificacion)
                )
            except Exception as e:
                # si algún archivo no se puede leer, lo saltamos
                continue

    conn.commit()
    conn.close()
    print("Proceso completado")


tk.Label(text="Indica el nombre de la carpeta a indexar").pack(padx = 20,pady = 20)
carpeta = tk.Entry()
carpeta.pack(padx = 20,pady = 20)

tk.Label(text="Indica el nombre del disco").pack(padx = 20,pady = 20)
disco = tk.Entry()
disco.pack(padx = 20,pady = 20)

tk.Button(text="Procesar",command = procesar).pack(padx = 20,pady = 20)

ventana.mainloop()
```

### aplicacion completa indexacion
<small>Creado: 2025-10-23 15:52</small>

#### Explicación

Este código es una aplicación de Python que utiliza la biblioteca `tkinter` para crear una interfaz gráfica (GUI) y `sqlite3` para manejar una base de datos SQLite. La app permite al usuario indexar archivos en un sistema de directorios específico, almacenando información sobre estos archivos en una base de datos SQLite, y proporciona herramientas para buscar dichos archivos.

El programa comienza creando la estructura necesaria en la base de datos SQLite, incluyendo la tabla `archivos` donde se almacenan los detalles de cada archivo indexado (nombre del disco, ruta completa, nombre del archivo, tamaño, fechas de creación y modificación). Además, crea índices para mejorar la velocidad de búsqueda.

La interfaz gráfica se divide en dos partes principales:

1. **Lado izquierdo**: Permite al usuario especificar una carpeta que desea indexar y un nombre para el disco asociado a esa carpeta. Cuando se presiona el botón "Procesar", la app recorre recursivamente todos los archivos dentro de la carpeta proporcionada, extrae información relevante sobre cada archivo y lo inserta en la base de datos.

2. **Lado derecho**: Proporciona una herramienta para buscar archivos indexados por nombre o ruta parcial utilizando un cuadro de búsqueda y un widget `Treeview` que muestra los resultados. Los usuarios pueden escribir consultas en el cuadro de entrada y presionar "Buscar" o usar la tecla Enter para ejecutar la consulta.

La aplicación también maneja eventos como doble clic en las filas del `Treeview`, copiando automáticamente la ruta completa del archivo seleccionado al portapapeles. Esto facilita a los usuarios acceder rápidamente a los archivos encontrados mediante el motor de búsqueda.

Esta app es útil para realizar búsquedas eficientes en sistemas con grandes cantidades de archivos, permitiendo una rápida indexación y recuperación de información basada en la estructura del sistema de archivos.

`017-aplicacion completa indexacion.py`

```python
#!/usr/bin/env python3
import os
import sqlite3
from datetime import datetime
import tkinter as tk

# ttkbootstrap para mejorar el aspecto
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox, filedialog

DB_NAME = "discos.db"

# -------------------- utilidades --------------------
def asegurar_bd():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS archivos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disco TEXT,
            ruta  TEXT,
            archivo TEXT,
            tamanio INTEGER,
            creacion TEXT,
            modificacion TEXT
        )
    """)
    # Índices útiles para acelerar búsquedas
    cur.execute("CREATE INDEX IF NOT EXISTS idx_archivos_archivo ON archivos(archivo)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_archivos_ruta ON archivos(ruta)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_archivos_disco ON archivos(disco)")
    conn.commit()
    conn.close()

def formato_tam(bytes_):
    try:
        bytes_ = int(bytes_)
    except:
        return str(bytes_)
    for unidad in ("B","KB","MB","GB","TB"):
        if bytes_ < 1024:
            return f"{bytes_:.0f} {unidad}" if unidad=="B" else f"{bytes_:.2f} {unidad}"
        bytes_ /= 1024
    return f"{bytes_:.2f} PB"

# -------------------- app --------------------
def main():
    asegurar_bd()

    # Ventana con tema (elige: flatly, darkly, lumen, vapor, etc.)
    root = tb.Window(themename="flatly")
    root.title("Indexador y Buscador de Archivos (SQLite + ttkbootstrap)")
    root.geometry("1100x650")

    # PanedWindow para dividir 50/50
    paned = ttk.PanedWindow(root, orient=HORIZONTAL)
    paned.pack(fill=BOTH, expand=True, padx=8, pady=8)

    # Frames izquierdo y derecho
    left = ttk.Frame(paned, padding=16)
    right = ttk.Frame(paned, padding=16)
    paned.add(left, weight=1)
    paned.add(right, weight=1)

    # -------------------- LADO IZQUIERDO (indexación) --------------------
    ttk.Label(left, text="Indica la carpeta a indexar", font=("Ubuntu", 11, "bold")).pack(anchor="w")

    carpeta_frame = ttk.Frame(left)
    carpeta_frame.pack(fill=X, pady=6)
    carpeta_var = tk.StringVar()
    carpeta_entry = ttk.Entry(carpeta_frame, textvariable=carpeta_var)
    carpeta_entry.pack(side=LEFT, fill=X, expand=True)
    def elegir_carpeta():
        path = filedialog.askdirectory()
        if path:
            carpeta_var.set(path)
    ttk.Button(carpeta_frame, text="Elegir…", command=elegir_carpeta, bootstyle=SECONDARY).pack(side=LEFT, padx=6)

    ttk.Label(left, text="Indica el nombre del disco", font=("Ubuntu", 11, "bold")).pack(anchor="w", pady=(10,0))
    disco_var = tk.StringVar()
    ttk.Entry(left, textvariable=disco_var).pack(fill=X, pady=6)

    estado_var = tk.StringVar(value="Listo.")
    barra = ttk.Label(left, textvariable=estado_var, bootstyle=INFO)
    barra.pack(fill=X, pady=(8,0))

    def procesar():
        carpeta_inicial = carpeta_var.get().strip()
        nombre_disco = disco_var.get().strip()

        if not carpeta_inicial or not os.path.isdir(carpeta_inicial) or not nombre_disco:
            messagebox.showwarning("Datos inválidos", "Carpeta o disco no válidos")
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        total = 0
        saltados = 0
        estado_var.set("Indexando… esto puede tardar según la cantidad de archivos.")
        root.update_idletasks()

        for raiz, subdirs, archivos in os.walk(carpeta_inicial):
            for arch in archivos:
                ruta_completa = os.path.join(raiz, arch)
                try:
                    tamanio = os.path.getsize(ruta_completa)
                    creacion = datetime.fromtimestamp(os.path.getctime(ruta_completa)).isoformat(timespec="seconds")
                    modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa)).isoformat(timespec="seconds")
                    cur.execute(
                        "INSERT INTO archivos (disco, ruta, archivo, tamanio, creacion, modificacion) VALUES (?,?,?,?,?,?)",
                        (nombre_disco, raiz, arch, int(tamanio), creacion, modificacion)
                    )
                    total += 1
                    if total % 1000 == 0:
                        conn.commit()
                        estado_var.set(f"Indexados {total:,}…")
                        root.update_idletasks()
                except Exception:
                    saltados += 1
                    continue

        conn.commit()
        conn.close()
        estado_var.set(f"Proceso completado. Indexados: {total:,}. Saltados: {saltados:,}.")
        messagebox.showinfo("Completado", f"Indexación finalizada.\nIndexados: {total:,}\nSaltados: {saltados:,}")

    ttk.Button(left, text="Procesar", command=procesar, bootstyle=SUCCESS).pack(pady=16, fill=X)

    # Separador estético
    ttk.Separator(left, orient=HORIZONTAL).pack(fill=X, pady=8)
    ttk.Label(left, text="Consejo: puedes indexar varios discos; luego búscalos por su nombre.",
              wraplength=420, bootstyle=SECONDARY).pack(anchor="w")

    # -------------------- LADO DERECHO (búsqueda + Treeview) --------------------
    top_right = ttk.Frame(right)
    top_right.pack(fill=X)

    ttk.Label(top_right, text="Buscar en SQLite", font=("Ubuntu", 11, "bold")).pack(anchor="w")

    search_row = ttk.Frame(top_right)
    search_row.pack(fill=X, pady=6)

    query_var = tk.StringVar()
    entry_buscar = ttk.Entry(search_row, textvariable=query_var)
    entry_buscar.pack(side=LEFT, fill=X, expand=True)

    def ejecutar_busqueda(event=None):
        q = query_var.get().strip()
        llenar_tree(q)

    ttk.Button(search_row, text="Buscar", command=ejecutar_busqueda, bootstyle=PRIMARY).pack(side=LEFT, padx=6)
    entry_buscar.bind("<Return>", ejecutar_busqueda)

    # Tree + Scrollbar
    cols = ("disco", "ruta", "archivo", "tamanio", "creacion", "modificacion")
    tree_frame = ttk.Frame(right)
    tree_frame.pack(fill=BOTH, expand=True, pady=(8,0))

    tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=18)
    vsb = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    hsb = ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    tree_frame.rowconfigure(0, weight=1)
    tree_frame.columnconfigure(0, weight=1)

    # Encabezados y anchos
    tree.heading("disco", text="Disco")
    tree.heading("ruta", text="Ruta")
    tree.heading("archivo", text="Archivo")
    tree.heading("tamanio", text="Tamaño")
    tree.heading("creacion", text="Creación")
    tree.heading("modificacion", text="Modificación")

    tree.column("disco", width=100, anchor=W)
    tree.column("ruta", width=280, anchor=W)
    tree.column("archivo", width=220, anchor=W)
    tree.column("tamanio", width=100, anchor=E)
    tree.column("creacion", width=150, anchor=W)
    tree.column("modificacion", width=150, anchor=W)

    # estado derecha
    estado_busq = tk.StringVar(value="Sin resultados aún.")
    ttk.Label(right, textvariable=estado_busq, bootstyle=INFO).pack(fill=X, pady=(6,0))

    def limpiar_tree():
        for i in tree.get_children():
            tree.delete(i)

    def llenar_tree(q):
        limpiar_tree()
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        if q:
            like = f"%{q}%"
            cur.execute(
                """
                SELECT disco, ruta, archivo, CAST(tamanio AS INTEGER) AS tamanio, creacion, modificacion
                FROM archivos
                WHERE archivo LIKE ? OR ruta LIKE ? OR disco LIKE ?
                ORDER BY rowid DESC
                LIMIT 1000
                """,
                (like, like, like)
            )
        else:
            cur.execute(
                """
                SELECT disco, ruta, archivo, CAST(tamanio AS INTEGER) AS tamanio, creacion, modificacion
                FROM archivos
                ORDER BY rowid DESC
                LIMIT 1000
                """
            )

        filas = cur.fetchall()
        conn.close()

        for d, r, a, t, c, m in filas:
            tree.insert("", "end", values=(d, r, a, formato_tam(t), c, m))

        if q:
            estado_busq.set(f"{len(filas)} resultados para «{q}» (máx 1000).")
        else:
            estado_busq.set(f"Mostrando {len(filas)} últimos registros (máx 1000).")


    # Doble clic: copiar ruta completa al portapapeles (útil)
    def on_double_click(event):
        item = tree.selection()
        if not item:
            return
        vals = tree.item(item[0], "values")
        # vals: (disco, ruta, archivo, tamanio, creacion, modificacion)
        ruta_completa = os.path.join(vals[1], vals[2])
        root.clipboard_clear()
        root.clipboard_append(ruta_completa)
        messagebox.showinfo("Ruta copiada", ruta_completa)

    tree.bind("<Double-1>", on_double_click)

    # Carga inicial
    llenar_tree("")

    root.mainloop()

if __name__ == "__main__":
    main()
```

### mejoras ia
<small>Creado: 2025-10-23 15:59</small>

#### Explicación

Este código es una aplicación de programación en Python que utiliza la biblioteca `ttkbootstrap` para crear una interfaz gráfica de usuario (GUI) y SQLite para gestionar una base de datos. La aplicación permite al usuario indexar archivos y carpetas en un sistema de ficheros, así como buscarlos a través de esta base de datos.

El programa se divide principalmente en dos partes:

1. **Indexación**: El lado izquierdo del panel horizontal permitirá al usuario indicar la carpeta que desea indexar y el nombre del disco correspondiente (por ejemplo, "C:", "D:"). Al seleccionar una carpeta con el botón "Elegir…" se abre un explorador de archivos. Luego, cuando el usuario presiona el botón "Procesar", el programa recorre toda la estructura de directorios y archivos dentro de la carpeta indicada, registrando en una base de datos SQLite (llamada `discos.db`) información sobre cada archivo indexado como su nombre, ruta completa, tamaño, fecha de creación y modificación. Esta información se usa para buscar más tarde.

2. **Búsqueda**: El lado derecho del panel permite al usuario buscar archivos dentro de la base de datos creada a través de varios filtros, que pueden incluir el disco en el que residen los archivos, su ruta, nombre o incluso su tamaño y fechas de creación y modificación. Los resultados se muestran en un widget `Treeview`, donde cada fila representa un archivo indexado con sus respectivos metadatos.

La importancia de este código radica en cómo integra operaciones del sistema de ficheros (como listar directorios, obtener propiedades de archivos) con una base de datos para proporcionar una búsqueda rápida y eficiente. Esto es especialmente útil cuando se trabaja con grandes cantidades de archivos y necesitas encontrarlos rápidamente por sus metadatos.

Esta herramienta puede ser muy práctica en entornos donde los usuarios manejan muchos archivos y necesitan una forma sencilla pero potente para buscar dentro de sus sistemas de ficheros.

`018-mejoras ia.py`

```python
#!/usr/bin/env python3
import os
import sqlite3
from datetime import datetime
import tkinter as tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox, filedialog

DB_NAME = "discos.db"

# -------------------- utilidades --------------------
def asegurar_bd():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS archivos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disco TEXT,
            ruta  TEXT,
            archivo TEXT,
            tamanio INTEGER,
            creacion TEXT,
            modificacion TEXT
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_archivos_archivo ON archivos(archivo)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_archivos_ruta ON archivos(ruta)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_archivos_disco ON archivos(disco)")
    conn.commit()
    conn.close()

def formato_tam(bytes_):
    try:
        bytes_ = int(bytes_)
    except:
        return str(bytes_)
    for unidad in ("B","KB","MB","GB","TB"):
        if bytes_ < 1024:
            return f"{bytes_:.0f} {unidad}" if unidad=="B" else f"{bytes_:.2f} {unidad}"
        bytes_ /= 1024
    return f"{bytes_:.2f} PB"

# -------------------- app --------------------
def main():
    asegurar_bd()

    root = tb.Window(themename="flatly")
    root.title("Indexador y Buscador de Archivos (SQLite + ttkbootstrap)")
    root.geometry("1250x700")

    paned = ttk.PanedWindow(root, orient=HORIZONTAL)
    paned.pack(fill=BOTH, expand=True, padx=8, pady=8)

    left = ttk.Frame(paned, padding=16)
    right = ttk.Frame(paned, padding=16)
    paned.add(left, weight=1)
    paned.add(right, weight=2)

    # -------------------- LADO IZQUIERDO (indexación) --------------------
    ttk.Label(left, text="Indica la carpeta a indexar", font=("Ubuntu", 11, "bold")).pack(anchor="w")

    carpeta_frame = ttk.Frame(left)
    carpeta_frame.pack(fill=X, pady=6)
    carpeta_var = tk.StringVar()
    carpeta_entry = ttk.Entry(carpeta_frame, textvariable=carpeta_var)
    carpeta_entry.pack(side=LEFT, fill=X, expand=True)
    def elegir_carpeta():
        path = filedialog.askdirectory()
        if path:
            carpeta_var.set(path)
    ttk.Button(carpeta_frame, text="Elegir…", command=elegir_carpeta, bootstyle=SECONDARY).pack(side=LEFT, padx=6)

    ttk.Label(left, text="Indica el nombre del disco", font=("Ubuntu", 11, "bold")).pack(anchor="w", pady=(10,0))
    disco_var = tk.StringVar()
    ttk.Entry(left, textvariable=disco_var).pack(fill=X, pady=6)

    estado_var = tk.StringVar(value="Listo.")
    barra = ttk.Label(left, textvariable=estado_var, bootstyle=INFO)
    barra.pack(fill=X, pady=(8,0))

    def procesar():
        carpeta_inicial = carpeta_var.get().strip()
        nombre_disco = disco_var.get().strip()

        if not carpeta_inicial or not os.path.isdir(carpeta_inicial) or not nombre_disco:
            messagebox.showwarning("Datos inválidos", "Carpeta o disco no válidos")
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        total = 0
        saltados = 0
        estado_var.set("Indexando… esto puede tardar según la cantidad de archivos.")
        root.update_idletasks()

        for raiz, subdirs, archivos in os.walk(carpeta_inicial):
            for arch in archivos:
                ruta_completa = os.path.join(raiz, arch)
                try:
                    tamanio = os.path.getsize(ruta_completa)
                    creacion = datetime.fromtimestamp(os.path.getctime(ruta_completa)).isoformat(timespec="seconds")
                    modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa)).isoformat(timespec="seconds")
                    cur.execute(
                        "INSERT INTO archivos (disco, ruta, archivo, tamanio, creacion, modificacion) VALUES (?,?,?,?,?,?)",
                        (nombre_disco, raiz, arch, int(tamanio), creacion, modificacion)
                    )
                    total += 1
                    if total % 1000 == 0:
                        conn.commit()
                        estado_var.set(f"Indexados {total:,}…")
                        root.update_idletasks()
                except Exception:
                    saltados += 1
                    continue

        conn.commit()
        conn.close()
        estado_var.set(f"Proceso completado. Indexados: {total:,}. Saltados: {saltados:,}.")
        messagebox.showinfo("Completado", f"Indexación finalizada.\nIndexados: {total:,}\nSaltados: {saltados:,}")

    ttk.Button(left, text="Procesar", command=procesar, bootstyle=SUCCESS).pack(pady=16, fill=X)
    ttk.Separator(left, orient=HORIZONTAL).pack(fill=X, pady=8)
    ttk.Label(left, text="Consejo: puedes indexar varios discos; luego búscalos por su nombre.",
              wraplength=420, bootstyle=SECONDARY).pack(anchor="w")

    # -------------------- LADO DERECHO (búsqueda + Treeview) --------------------
    ttk.Label(right, text="Buscar en SQLite", font=("Ubuntu", 11, "bold")).pack(anchor="w")

    # Estado búsqueda
    estado_busq = tk.StringVar(value="Sin resultados aún.")

    # --- Barra de filtros por columna (alineadas con el orden de columnas)
    filter_frame = ttk.Frame(right)
    filter_frame.pack(fill=X, pady=(8,4))

    # Definimos columnas (mismo orden en Treeview y filtros)
    cols = ("disco", "ruta", "archivo", "tamanio", "creacion", "modificacion")

    # Variables de filtro
    filtro_vars = {c: tk.StringVar() for c in cols}

    # grid headers (pequeño label sobre cada entry)
    labels = {
        "disco": "Disco",
        "ruta": "Ruta",
        "archivo": "Archivo",
        "tamanio": "Tamaño",
        "creacion": "Creación",
        "modificacion": "Modificación",
    }
    # creamos una cuadrícula con 6 columnas iguales
    for i, c in enumerate(cols):
        ttk.Label(filter_frame, text=labels[c]).grid(row=0, column=i, sticky="w", padx=4)
        ttk.Entry(filter_frame, textvariable=filtro_vars[c]).grid(row=1, column=i, sticky="ew", padx=4)
        filter_frame.columnconfigure(i, weight=1)

    # Botones Buscar/Limpiar a la derecha
    btns_frame = ttk.Frame(right)
    btns_frame.pack(fill=X, pady=(4,8))
    def limpiar_filtros():
        for v in filtro_vars.values():
            v.set("")
        llenar_tree()  # sin filtros

    def ejecutar_busqueda(event=None):
        llenar_tree()

    ttk.Button(btns_frame, text="Buscar", command=ejecutar_busqueda, bootstyle=PRIMARY).pack(side=RIGHT, padx=6)
    ttk.Button(btns_frame, text="Limpiar", command=limpiar_filtros, bootstyle=SECONDARY).pack(side=RIGHT)

    # --- Tree + Scrollbars
    tree_frame = ttk.Frame(right)
    tree_frame.pack(fill=BOTH, expand=True)

    tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=20)
    vsb = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    hsb = ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    tree_frame.rowconfigure(0, weight=1)
    tree_frame.columnconfigure(0, weight=1)

    # Encabezados y anchos
    tree.heading("disco", text="Disco")
    tree.heading("ruta", text="Ruta")
    tree.heading("archivo", text="Archivo")
    tree.heading("tamanio", text="Tamaño")
    tree.heading("creacion", text="Creación")
    tree.heading("modificacion", text="Modificación")

    tree.column("disco", width=120, anchor=W)
    tree.column("ruta", width=360, anchor=W)
    tree.column("archivo", width=260, anchor=W)
    tree.column("tamanio", width=120, anchor=E)
    tree.column("creacion", width=160, anchor=W)
    tree.column("modificacion", width=160, anchor=W)

    # --- Estado visual
    ttk.Label(right, textvariable=estado_busq, bootstyle=INFO).pack(fill=X, pady=(6,0))

    # --- Ordenación por columnas (estado global)
    sort_col = tk.StringVar(value="rowid")   # por defecto
    sort_dir = tk.StringVar(value="DESC")    # DESC/ASC

    # Mapa de columnas Tree -> expresión SQL de ORDER BY
    # Para tamanio conviene cast numérico; fechas ISO ordenan bien lexicográficamente
    order_expr = {
        "disco": "disco",
        "ruta": "ruta",
        "archivo": "archivo",
        "tamanio": "CAST(tamanio AS INTEGER)",
        "creacion": "creacion",
        "modificacion": "modificacion",
        "rowid": "rowid"
    }

    # Asignar comando a cada encabezado
    def on_sort(col_clicked):
        current_col = sort_col.get()
        current_dir = sort_dir.get()
        if current_col == col_clicked:
            sort_dir.set("ASC" if current_dir == "DESC" else "DESC")
        else:
            sort_col.set(col_clicked)
            sort_dir.set("ASC")  # primera vez ascendente
        llenar_tree()

    for c in cols:
        tree.heading(c, text=labels[c], command=lambda cc=c: on_sort(cc))

    # --- utilidades tree
    def limpiar_tree():
        for i in tree.get_children():
            tree.delete(i)

    # Construye WHERE dinámico con LIKE para todos los filtros
    def construir_where_y_params():
        where = []
        params = []
        for c in cols:
            val = filtro_vars[c].get().strip()
            if val != "":
                where.append(f"{c} LIKE ?")
                params.append(f"%{val}%")
        where_clause = ("WHERE " + " AND ".join(where)) if where else ""
        return where_clause, params

    def llenar_tree():
        limpiar_tree()
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        where_clause, params = construir_where_y_params()
        order = order_expr.get(sort_col.get(), "rowid")
        direction = "ASC" if sort_dir.get() == "ASC" else "DESC"

        sql = f"""
            SELECT disco, ruta, archivo, tamanio, creacion, modificacion
            FROM archivos
            {where_clause}
            ORDER BY {order} {direction}
            LIMIT 1000
        """
        cur.execute(sql, params)
        filas = cur.fetchall()
        conn.close()

        for d, r, a, t, c, m in filas:
            tree.insert("", "end", values=(d, r, a, formato_tam(t), c, m))

        # Texto de estado
        filtros_activos = [f"{labels[c]}='{filtro_vars[c].get().strip()}'"
                           for c in cols if filtro_vars[c].get().strip() != ""]
        filtros_txt = " | ".join(filtros_activos) if filtros_activos else "sin filtros"
        estado_busq.set(
            f"{len(filas)} resultados ({filtros_txt}). Orden: {order} {direction}. Máx 1000."
        )

    # Doble clic: copiar ruta completa al portapapeles
    def on_double_click(event):
        item = tree.selection()
        if not item:
            return
        vals = tree.item(item[0], "values")
        ruta_completa = os.path.join(vals[1], vals[2])
        root.clipboard_clear()
        root.clipboard_append(ruta_completa)
        messagebox.showinfo("Ruta copiada", ruta_completa)

    tree.bind("<Double-1>", on_double_click)

    # Enter en cualquier filtro = buscar
    for c in cols:
        entry = filter_frame.grid_slaves(row=1, column=cols.index(c))[0]
        entry.bind("<Return>", lambda e: ejecutar_busqueda())

    # Carga inicial
    llenar_tree()

    root.mainloop()

if __name__ == "__main__":
    main()
```

### Actividades propuestas

El código que has proporcionado es una aplicación de búsqueda y gestión de archivos en un sistema SQLite utilizando la biblioteca `ttk` para crear interfaces gráficas. La aplicación permite al usuario indexar discos o directorios enteros, luego buscar archivos en esa base de datos indexada con criterios flexibles como disco, ruta, nombre del archivo, tamaño, fecha de creación y modificación.

### Análisis del Código

#### 1. **Interfaz de Indexación:**
   - **Widgets:** La interfaz izquierda permite al usuario introducir el nombre del disco o directorio que desea indexar.
   - **Proceso de Indexación:** Al hacer clic en "Procesar", la aplicación recorre todos los archivos y directorios del disco o directorio especificado, insertándolos en una base de datos SQLite con información sobre su tamaño, fecha de creación y modificación.

#### 2. **Interfaz de Búsqueda:**
   - **Filtros:** La interfaz derecha ofrece un panel superior para filtrar por diferentes campos (disco, ruta, archivo, etc.) usando el operador `LIKE` con `%`.
   - **Ordenación:** Permite ordenar los resultados por cualquier columna y cambiar entre ascensor y descensor.
   - **Resultado de Búsqueda:** Los resultados se muestran en un widget `Treeview`, donde cada fila representa un archivo o directorio indexado, mostrando sus atributos relevantes.

#### 3. **Funcionalidades Adicionales:**
   - **Doble-Clic en Resultados:** Al hacer doble clic en una entrada del resultado de búsqueda, la ruta completa se copia al portapapeles para facilitar el acceso directo.
   - **Estado y Información:** La aplicación proporciona un estado visual que refleja los parámetros de búsqueda actualmente activos, incluyendo filtros aplicados, número de resultados y ordenamiento.

### Aspectos Importantes a Notar:

- **Optimización:** Para grandes volúmenes de datos, la indexación podría ser mejor optimizada. Por ejemplo, se podrían usar índices en SQLite para acelerar consultas.
  
- **Seguridad:** Como está trabajando con archivos del sistema y bases de datos locales, es importante asegurarse de que el usuario tenga los permisos necesarios y que no haya riesgos de sobrescritura accidental o inyección SQL.

- **Interfaz Amigable:** La interfaz es clara e intuitiva, aunque se podría mejorar con más documentación en la aplicación para ayudar a los usuarios nuevos. Por ejemplo, incluir un mensaje emergente al iniciar que explique brevemente cómo usar cada sección de la UI.

### Mejoras Potenciales:

1. **Optimización:** Considera agregar índices a tu base de datos SQLite para mejorar el rendimiento en consultas frecuentes.
   
2. **Interfaz Avanzada:** Agrega más widgets como botones de radio o desplegables que permitan al usuario seleccionar rápidamente diferentes opciones sin necesidad de teclear.

3. **Ayuda In-App:** Añadir una ventana emergente de ayuda con explicaciones sobre cómo usar cada sección, por ejemplo, al iniciar la aplicación o cuando un widget requiere más contexto (como doble clic).

4. **Soporte para Archivos en Tiempo Real:** Considerar añadir funcionalidades que permitan actualizar el índice automáticamente al detectar cambios en el sistema de archivos.

### Código y Uso

Para ejecutar este código, necesitarás tener instalada la biblioteca `tkinter` en tu entorno Python. Si estás utilizando una versión reciente de Python (3.10+), esta debería estar incluida por defecto. La aplicación se ejecuta al llamar a `main()` y abre una ventana gráfica donde puedes empezar a indexar tus discos o directorios, así como buscar archivos en la base de datos resultante.

Este tipo de herramienta puede ser muy útil para administración de sistemas, gestión de datos históricos sobre archivos, etc., permitiendo un fácil acceso rápido y filtrado por múltiples criterios.


<a id="creacion-de-controladores-de-eventos"></a>
## Creación de controladores de eventos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/009-Creaci%C3%B3n%20de%20controladores%20de%20eventos)

### Introducción a los ejercicios

El código que has proporcionado es una secuencia de pasos para crear un blog básico utilizando Python y Flask, con datos almacenados en una base de datos MySQL. Vamos a revisar el flujo de trabajo desde la creación del entorno hasta la implementación final.

### 1. Configuración Inicial
- **Instalación de dependencias**: Se instala `flask` para crear la aplicación web y `mysql.connector-python` para conectarse a MySQL.
  
```sh
pip install flask mysql-connector-python
```

### 2. Crear la Base de Datos
- En la línea de comandos, se crea un usuario y una base de datos llamada `blogexamen`.

```sql
CREATE DATABASE blogexamen;
CREATE USER 'blogexamen'@'localhost';
GRANT ALL PRIVILEGES ON blogexamen.* TO 'blogexamen'@'localhost' IDENTIFIED BY 'Blogexamen123$';
```

### 3. Crear Tablas en MySQL
- Se crea una tabla `posts` para almacenar los artículos del blog y otra tabla `usuarios` para gestionar los usuarios.

```sql
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(50) NOT NULL,
    contenido TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(30),
    email VARCHAR(60)
);
```

### 4. Crear una Vista en MySQL para Consultas Complejas
- Se crea una vista llamada `posts_completos` que incluye información adicional, como el autor y la fecha del artículo.

```sql
CREATE VIEW posts_completos AS
SELECT p.id AS id_post, 
       p.titulo, 
       p.contenido,
       u.nombre_usuario AS autor,
       u.email
FROM posts p
JOIN usuarios u ON u.id = p.autor_id;
```

### 5. Crear la Aplicación Flask
- Se crea una aplicación básica con Flask que muestra un archivo HTML estático.

```python
from flask import Flask  

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return "Hola mundo"

if __name__ == "__main__":
    aplicacion.run()
```

### 6. Conectar a MySQL desde la Aplicación Flask
- Se conecta a la base de datos y se consulta la vista `posts_completos` para mostrar los artículos en el HTML.

```python
from flask import Flask 
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor() 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
        <!doctype html>
        <html>
          ...
    '''

    cursor.execute("SELECT * FROM posts_completos ORDER BY fecha DESC;")
    filas = cursor.fetchall()
    
    for fila in filas:
        # Construcción de la cadena HTML
        cadena += f'''
            <article>
                <h3>{fila[0]}</h3>
                <time>{fila[1]}</time>
                <p>{fila[3]} {fila[4]}</p>
                <p>{fila[2]}</p>
            </article>
    '''

    return cadena
  
if __name__ == "__main__":
    aplicacion.run()
```

### 7. Mejorar el Estilo y la Funcionalidad
- Se mejora el estilo del HTML utilizando CSS.
- Se ordenan los artículos por fecha de manera descendente para mostrar los más recientes primero.

```python
from flask import Flask 
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor() 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
        <!doctype html>
        <html>
          ...
    '''

    cursor.execute("SELECT * FROM posts_completos ORDER BY fecha DESC;")
    filas = cursor.fetchall()
    
    for fila in filas:
        # Construcción de la cadena HTML
        cadena += f'''
            <article>
                <h3>{fila[0]}</h3>
                <time>{fila[1]}</time>
                <p>{fila[3]} {fila[4]}</p>
                <p>{fila[2]}</p>
            </article>
    '''

    return cadena
  
if __name__ == "__main__":
    aplicacion.run()
```

### 8. Ejecutar la Aplicación
- La aplicación se ejecuta en el puerto por defecto de Flask (`5000`), y puedes ver tu blog en `http://localhost:5000`.

```sh
python nombre_del_archivo.py
```

Este es un resumen del flujo de trabajo desde la creación inicial hasta la implementación final. Si tienes alguna pregunta específica sobre cualquier parte del código o proceso, no dudes en preguntar.

### repaso mysql
<small>Creado: 2025-10-23 16:09</small>

#### Explicación

Este fragmento de código SQL es una secuencia de comandos que te permiten interactuar con la base de datos MySQL desde la línea de comando. 

Primero, el comando `sudo mysql -u root -p` te solicita iniciar sesión en MySQL como usuario 'root'. Al usar `sudo`, obtienes los permisos administrativos necesarios para acceder a todas las bases de datos disponibles. Tras ejecutar este comando, se te pedirá que introduzcas la contraseña del usuario root.

El siguiente comando `SHOW DATABASES;` muestra una lista con todos los nombres de las bases de datos existentes en el servidor MySQL actual. Esto es útil cuando quieres ver qué bases de datos están configuradas y cómo están organizados tus datos.

Finalmente, el comando `USE empresarial;` selecciona la base de datos llamada 'empresarial'. Una vez que has ejecutado este comando, todos los comandos SQL subsiguientes se aplicarán a esta base de datos específica hasta que cambies a otra utilizando otro comando USE o cierres la sesión.

El comando `SHOW TABLES;` luego te muestra todas las tablas disponibles dentro de la base de datos 'empresarial'. Esto es especialmente importante para entender qué estructura de datos estás trabajando, ya sea al buscar un conjunto específico de datos o a prepararte para realizar cambios en esa base de datos.

Estos comandos son fundamentales cuando te encuentras interactuando directamente con MySQL desde la línea de comandos y necesitas acceder a las bases de datos específicas y sus tablas.

`001-repaso mysql.sql`

```sql
sudo mysql -u root -p

SHOW DATABASES;

USE empresarial;

SHOW TABLES;
```

### conecto a mysql
<small>Creado: 2025-10-23 16:14</small>

#### Explicación

Este código Python se utiliza para conectarse a una base de datos MySQL y ejecutar consultas SQL. En primer lugar, importa el módulo `mysql.connector` que proporciona las herramientas necesarias para establecer una conexión con una base de datos MySQL desde un programa en Python.

El fragmento crea una conexión a la base de datos utilizando los detalles de acceso proporcionados: host (localhost), usuario (usuarioempresarial), contraseña (usuarioempresarial) y el nombre de la base de datos (empresarial). Luego, se crea un objeto `cursor` que permite ejecutar comandos SQL y recuperar resultados.

El código sigue ejecutando una consulta SELECT que selecciona todos los registros de la tabla `productos`. Los resultados devueltos por esta consulta se almacenan en el cursor. Finalmente, el resultado es recorrido con un bucle for para imprimir cada fila del conjunto de resultados en la consola.

Es importante cerrar tanto el cursor como la conexión a la base de datos después de completar todas las operaciones necesarias para liberar los recursos y evitar posibles errores o ineficiencias.

`002-conecto a mysql.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="usuarioempresarial",
    password="usuarioempresarial",
    database="empresarial"
)

# Creo un cursor
cursor = conexion.cursor()

# Ejecuto un select
cursor.execute("SELECT * FROM productos")

# Pinto el resultado en pantalla
for fila in cursor.fetchall():
    print(fila)

# Cierro la conexion
cursor.close()
conexion.close()
```

### examen de bases de datos
<small>Creado: 2025-10-23 16:24</small>

#### Explicación

Este fragmento de código SQL te guía a través del proceso de creación y configuración de una base de datos para un blog. Primero, inicia la sesión en MySQL con tus credenciales (`-u root -p`), lo que significa que estás utilizando el usuario 'root' y serás solicitado por la contraseña.

Luego, se muestra la lista actual de bases de datos existentes usando `SHOW DATABASES;`. A continuación, se crea una nueva base de datos llamada `blogexamen` con el comando `CREATE DATABASE blogexamen;`.

Después de crearla, cambias a esa base de datos específica utilizando `USE blogexamen;`. Aquí es donde vas a trabajar.

Luego, creas una tabla llamada `posts`, que almacena información sobre los artículos del blog. Esta tabla tiene cinco columnas: un identificador único para cada artículo (`Identificador`), el título del post (`titulo`), la fecha en que se publicó (`fecha`), el contenido del post (`contenido`) y el ID del autor (`autor`).

Después de crear la tabla, ejecutas `SHOW TABLES;` para mostrar todas las tablas existentes en la base de datos actual. Luego, describes la estructura recién creada de la tabla `posts` con `DESCRIBE posts;`.

Finalmente, se realiza una modificación en la tabla `posts`. Se añade un campo clave principal (`PRIMARY KEY`) a la columna `Identificador`, lo que significa que esta columna va a contener valores únicos para cada registro. Luego, modificas el tipo de dato y las propiedades del campo `Identificador` para permitirle ser incremental (es decir, automáticamente aumenta por un valor fijo cada vez que se agrega una nueva entrada), asegurando así que nunca haya duplicados con `ALTER TABLE posts MODIFY COLUMN Identificador INT NOT NULL AUTO_INCREMENT;`. Al final, vuelves a describir la tabla `posts` para verificar los cambios hechos.

Este código es importante porque establece las bases de la estructura de datos para un sistema de gestión del contenido (CMS) básico que permite almacenar y gestionar artículos de blog.

`003-examen de bases de datos.sql`

```sql
mysql -u root -p

SHOW DATABASES;

CREATE DATABASE blogexamen;

USE blogexamen;

CREATE TABLE `posts` (
  `Identificador` INT NOT NULL , 
  `titulo` VARCHAR(50) NOT NULL , 
  `fecha` VARCHAR(100) NOT NULL , 
  `contenido` VARCHAR(50) NOT NULL , 
  `autor` INT(255) NOT NULL 
) ENGINE = InnoDB;

SHOW TABLES;

DESCRIBE posts;

ALTER TABLE posts
  ADD PRIMARY KEY (`Identificador`);
  
ALTER TABLE posts
MODIFY COLUMN Identificador INT NOT NULL AUTO_INCREMENT;

DESCRIBE posts;
```

### tabla de autores
<small>Creado: 2025-10-23 16:25</small>

#### Explicación

Este código SQL realiza varias operaciones importantes para configurar una base de datos y crear una tabla llamada `autores`. Primero, se inicia sesión en MySQL proporcionando las credenciales necesarias. Luego, muestra todas las bases de datos disponibles en el servidor.

El siguiente paso es crear una nueva base de datos llamada `blogexamen` si no existe ya, y luego seleccionarla para trabajar con ella. Posteriormente, se crea la tabla `autores` que contiene cuatro columnas: `Identificador`, `nombre`, `apellidos` y `email`. Cada columna tiene un tipo de dato específico y algunas son obligatorias (no nulas).

Después de crear la tabla, el código muestra todas las tablas disponibles en la base de datos actual (`blogexamen`) para verificar que `autores` ha sido creada correctamente. Luego describe la estructura de la tabla `autores`.

Finalmente, se realizan dos operaciones importantes en la tabla `autores`: primero, se establece una clave primaria única basada en la columna `Identificador`. Luego, se modifica la columna `Identificador` para que sea autoincremental y no nula. Esto significa que cada vez que se añade un nuevo registro a la tabla, el valor de `Identificador` será automáticamente incrementado en uno, asegurando así que todos los registros tengan identificadores únicos.

Esta secuencia de comandos es fundamental para establecer una base sólida para cualquier aplicación web o sistema de gestión de contenido que requiera almacenar información sobre autores.

`004-tabla de autores.sql`

```sql
mysql -u root -p

SHOW DATABASES;

CREATE DATABASE blogexamen;

USE blogexamen;

CREATE TABLE `autores` (
  `Identificador` INT NOT NULL , 
  `nombre` VARCHAR(50) NOT NULL , 
  `apellidos` VARCHAR(100) NOT NULL , 
  `email` VARCHAR(50) NOT NULL 
) ENGINE = InnoDB;

SHOW TABLES;

DESCRIBE autores;

ALTER TABLE autores
  ADD PRIMARY KEY (`Identificador`);
  
ALTER TABLE autores
MODIFY COLUMN Identificador INT NOT NULL AUTO_INCREMENT;

DESCRIBE autores;
```

### autores
<small>Creado: 2025-10-23 16:27</small>

#### Explicación

Este fragmento de código SQL está diseñado para crear una base de datos y una tabla en un servidor MySQL, y luego configurar la tabla con campos específicos. Primero, se conecta a la base de datos MySQL usando el usuario root y te pide que introduzcas la contraseña. Luego, muestra todas las bases de datos disponibles.

A continuación, crea una nueva base de datos llamada `blogexamen`. Una vez creada, selecciona esta base de datos para trabajar con ella. Después, se define una tabla llamada `autores` con cuatro columnas: `Identificador`, `nombre`, `apellidos` y `email`.

Después de crear la tabla, el código muestra las tablas disponibles en la base de datos actual para verificar que la tabla `autores` ha sido creada correctamente. Luego describe los detalles de la tabla `autores` para mostrar cómo se estructuran sus columnas.

Finalmente, realiza dos ajustes importantes a la tabla `autores`. En primer lugar, establece el campo `Identificador` como clave principal (`PRIMARY KEY`). Esto significa que cada registro en esta tabla tendrá un valor único en este campo y se puede usar para identificar de manera única cada fila. Luego, modifica el campo `Identificador` para que sea autoincremental (`AUTO_INCREMENT`), lo que permite que MySQL asigne automáticamente valores únicos a este campo cuando nuevos registros se añaden a la tabla sin proporcionar un valor explícito para esta columna.

Este código es importante porque establece una estructura básica de base de datos necesaria para aplicaciones como blogs o sitios web donde se almacenan información sobre autores, incluyendo detalles como su nombre y correo electrónico.

`005-autores.sql`

```sql
mysql -u root -p

SHOW DATABASES;

CREATE DATABASE blogexamen;

USE blogexamen;

CREATE TABLE `autores` (
  `Identificador` INT NOT NULL , 
  `nombre` VARCHAR(50) NOT NULL , 
  `apellidos` VARCHAR(100) NOT NULL , 
  `email` VARCHAR(50) NOT NULL 
) ENGINE = InnoDB;

SHOW TABLES;

DESCRIBE autores;

ALTER TABLE autores
  ADD PRIMARY KEY (`Identificador`);
  
ALTER TABLE autores
MODIFY COLUMN Identificador INT NOT NULL AUTO_INCREMENT;

DESCRIBE autores;
```

### enlazo las tablas
<small>Creado: 2025-10-23 16:28</small>

#### Explicación

Este fragmento de código SQL está configurando una relación entre dos tablas en una base de datos: la tabla `posts` y la tabla `autores`. Específicamente, el código está creando lo que se conoce como una clave foránea (FOREIGN KEY) en la tabla `posts`.

La columna `autor` en la tabla `posts` ahora apunta a la columna `Identificador` en la tabla `autores`, estableciendo así una relación entre los autores y sus publicaciones. Esto significa que cada vez que se añade un post nuevo, el valor de `autor` debe coincidir con un valor existente en la columna `Identificador` de la tabla `autores`.

La opción `ON DELETE RESTRICT ON UPDATE RESTRICT` asegura que si intentas eliminar un autor o cambiar su identificador, no será posible hacerlo a menos que se eliminen primero todas las entradas relacionadas en la tabla `posts`. Esto ayuda a mantener la integridad de los datos, evitando que queden huérfanos registros (es decir, publicaciones sin autor asociado).

Este tipo de relación entre tablas es fundamental para estructurar correctamente una base de datos y permitir consultas más eficientes e informativas.

`006-enlazo las tablas.sql`

```sql
ALTER TABLE `posts` 
ADD CONSTRAINT `postsaautores` 
FOREIGN KEY (`autor`) 
REFERENCES `autores`(`Identificador`) 
ON DELETE RESTRICT ON UPDATE RESTRICT;
```

### inserto registros
<small>Creado: 2025-10-23 16:32</small>

#### Explicación

Este fragmento de código SQL está insertando datos en una tabla llamada `autores`. Cada fila que se añade a la tabla contiene información sobre un autor, especificamente su identificador único (una especie de número de registro), nombre, apellidos y dirección de correo electrónico. Por ejemplo, el primer autor es Lucía Fernández Lirio con un email de contacto.

Después de insertar todos estos datos en la tabla `autores`, se ejecuta una consulta SELECT que recupera toda la información almacenada en esa tabla (`SELECT * FROM autores;`). Esto permite ver los registros que acabamos de introducir y verificar que todo ha sido guardado correctamente.

Esta operación es importante porque nos ayuda a llenar nuestra base de datos con información real para poder realizar consultas más avanzadas y aprender a gestionar datos de manera efectiva en SQL.

`007-inserto registros.sql`

```sql
INSERT INTO autores (Identificador, nombre, apellidos, email) VALUES
(1, 'Lucía', 'Fernández Lirio', 'lucia.fernandez@example.com'),
(2, 'Mateo', 'Ramos Villalba', 'mateo.ramos@example.com'),
(3, 'Sofía', 'Navarro Duque', 'sofia.navarro@example.com'),
(4, 'Daniel', 'Ibáñez Campos', 'daniel.ibanez@example.com'),
(5, 'Clara', 'Morales Requena', 'clara.morales@example.com'),
(6, 'Andrés', 'Serrano Vélez', 'andres.serrano@example.com'),
(7, 'Nora', 'Galindo Sáez', 'nora.galindo@example.com'),
(8, 'Diego', 'Lozano Ferrer', 'diego.lozano@example.com'),
(9, 'Irene', 'Hidalgo Cortés', 'irene.hidalgo@example.com'),
(10, 'Lucas', 'Pérez Caballero', 'lucas.perez@example.com'),
(11, 'Valeria', 'Ruiz Castelló', 'valeria.ruiz@example.com'),
(12, 'Hugo', 'Delgado Riera', 'hugo.delgado@example.com'),
(13, 'Emma', 'Vidal Soler', 'emma.vidal@example.com'),
(14, 'Leo', 'Torres Alcázar', 'leo.torres@example.com'),
(15, 'Marina', 'Ortega Pons', 'marina.ortega@example.com'),
(16, 'Bruno', 'Crespo Martí', 'bruno.crespo@example.com'),
(17, 'Aitana', 'Santos Aranda', 'aitana.santos@example.com'),
(18, 'Pablo', 'Navas Romero', 'pablo.navas@example.com'),
(19, 'Julia', 'Giménez Blasco', 'julia.gimenez@example.com'),
(20, 'Sergio', 'Beltrán Mora', 'sergio.beltran@example.com');

SELECT * FROM autores;
```

### inserto posts
<small>Creado: 2025-10-23 16:35</small>

#### Explicación

Este código SQL se utiliza para insertar múltiples registros (filas) en una tabla llamada `posts`. Cada registro representa un artículo o entrada con información como el identificador único del post, título, fecha de publicación, contenido y autor. El comando `INSERT INTO` es fundamental en bases de datos SQL para agregar nueva información a una tabla existente.

En este caso específico, se están insertando 50 registros diferentes en la tabla `posts`, cada uno con detalles específicos como el identificador del post, título, fecha, contenido e identificador del autor. Por ejemplo, un registro podría ser un artículo titulado "El futuro de la inteligencia artificial" escrito por el autor con ID 1 y publicado el 5 de enero de 2025.

Después de insertar todos estos registros, se utiliza el comando `SELECT * FROM posts;` para recuperar y mostrar toda la información almacenada en la tabla `posts`. Esto es útil tanto para verificar que los datos se han ingresado correctamente como para realizar consultas o análisis sobre los datos recién añadidos.

`008-inserto posts.sql`

```sql
INSERT INTO posts (Identificador, titulo, fecha, contenido, autor) VALUES
(1, 'El futuro de la inteligencia artificial', '2025-01-05', 'Una mirada al futuro de la IA.', 1),
(2, 'Redes neuronales explicadas', '2025-01-08', 'Cómo funcionan las redes neuronales.', 2),
(3, 'IA y creatividad artística', '2025-01-12', 'El papel de la IA en el arte moderno.', 3),
(4, 'Aprendizaje profundo simplificado', '2025-01-14', 'Conceptos básicos de deep learning.', 4),
(5, 'Chatbots y atención al cliente', '2025-01-16', 'Cómo los chatbots transforman empresas.', 5),
(6, 'Visión artificial en la medicina', '2025-01-20', 'Diagnósticos automáticos por IA.', 6),
(7, 'Modelos de lenguaje gigantes', '2025-01-23', 'Cómo funcionan los LLM como GPT.', 7),
(8, 'Ética en la inteligencia artificial', '2025-01-25', 'Los dilemas morales de la IA.', 8),
(9, 'Automatización del trabajo', '2025-01-27', 'Impacto de la IA en el empleo.', 9),
(10, 'IA y educación personalizada', '2025-01-30', 'Aprendizaje adaptativo con IA.', 10),
(11, 'Reconocimiento de voz avanzado', '2025-02-02', 'Sistemas de voz y su evolución.', 11),
(12, 'Generación de texto automática', '2025-02-04', 'El auge de los modelos generativos.', 12),
(13, 'Vehículos autónomos', '2025-02-06', 'Cómo la IA conduce sin humanos.', 13),
(14, 'Robótica emocional', '2025-02-08', 'Máquinas que entienden sentimientos.', 14),
(15, 'Machine learning en agricultura', '2025-02-10', 'Optimización de cultivos con IA.', 15),
(16, 'Procesamiento del lenguaje natural', '2025-02-12', 'Cómo las máquinas entienden texto.', 16),
(17, 'IA en ciberseguridad', '2025-02-15', 'Detección inteligente de amenazas.', 17),
(18, 'Algoritmos de recomendación', '2025-02-17', 'Cómo Netflix sabe qué quieres ver.', 18),
(19, 'Simulaciones con IA', '2025-02-19', 'Mundos virtuales impulsados por IA.', 19),
(20, 'IA y sostenibilidad', '2025-02-22', 'Tecnología verde con inteligencia.', 20),
(21, 'Modelos generativos visuales', '2025-02-25', 'Creación de imágenes por IA.', 1),
(22, 'El impacto social de la IA', '2025-02-27', 'Cómo cambia nuestras relaciones.', 2),
(23, 'IA en videojuegos', '2025-03-01', 'NPCs más realistas con IA.', 3),
(24, 'Automatización industrial', '2025-03-03', 'Robots inteligentes en fábricas.', 4),
(25, 'La IA en el mundo financiero', '2025-03-05', 'Predicciones económicas automáticas.', 5),
(26, 'Sistemas expertos modernos', '2025-03-07', 'De la lógica a la inteligencia.', 6),
(27, 'IA para análisis de datos', '2025-03-09', 'Descubriendo patrones ocultos.', 7),
(28, 'Redes neuronales convolucionales', '2025-03-11', 'Cómo ven las máquinas.', 8),
(29, 'Modelos híbridos IA-humanos', '2025-03-13', 'Colaboración entre mente y máquina.', 9),
(30, 'El papel del sesgo algorítmico', '2025-03-15', 'Cómo evitar prejuicios en la IA.', 10),
(31, 'IA aplicada al arte digital', '2025-03-17', 'Pinturas generadas por código.', 11),
(32, 'Modelos preentrenados', '2025-03-19', 'Por qué son tan poderosos.', 12),
(33, 'Aprendizaje no supervisado', '2025-03-21', 'Descubriendo patrones sin etiquetas.', 13),
(34, 'Optimización de hiperparámetros', '2025-03-23', 'Mejorando el rendimiento del modelo.', 14),
(35, 'IA en la salud mental', '2025-03-25', 'Asistentes empáticos digitales.', 15),
(36, 'Interfaces cerebro-máquina', '2025-03-27', 'Comunicación directa con IA.', 16),
(37, 'IA y realidad aumentada', '2025-03-29', 'Fusión del mundo físico y digital.', 17),
(38, 'Data labeling automático', '2025-03-31', 'Cómo entrenar sin etiquetar.', 18),
(39, 'Sistemas de IA explicables', '2025-04-02', 'Haciendo la IA comprensible.', 19),
(40, 'El auge del razonamiento simbólico', '2025-04-04', 'IA que entiende conceptos.', 20),
(41, 'IA distribuida en la nube', '2025-04-06', 'Escalabilidad y potencia.', 1),
(42, 'Reducción del consumo energético', '2025-04-08', 'IA más ecológica y eficiente.', 2),
(43, 'IA en marketing digital', '2025-04-10', 'Personalización extrema de campañas.', 3),
(44, 'Modelos multimodales', '2025-04-12', 'Texto, imagen y sonido unidos.', 4),
(45, 'Simulación del lenguaje humano', '2025-04-14', 'Hacia conversaciones naturales.', 5),
(46, 'IA en logística global', '2025-04-16', 'Rutas y entregas más inteligentes.', 6),
(47, 'Metaaprendizaje', '2025-04-18', 'Modelos que aprenden a aprender.', 7),
(48, 'IA para detección de fraudes', '2025-04-20', 'Protección de transacciones digitales.', 8),
(49, 'Redes generativas adversarias', '2025-04-22', 'La magia detrás de las GANs.', 9),
(50, 'El papel del humano en la era IA', '2025-04-24', 'Colaborar en vez de competir.', 10);

SELECT * FROM  posts;
```

### peticion cruzada entre tablas
<small>Creado: 2025-10-23 16:38</small>

#### Explicación

Este fragmento de código SQL realiza una consulta que combina dos tablas: `posts` y `autores`. La consulta selecciona información sobre los posts, como el título, la fecha y el contenido, así como el nombre y apellidos del autor asociado a cada post. 

La clave para entender cómo se combinan estas tablas es la instrucción `LEFT JOIN`, que une todos los registros de la tabla `posts` con los registros correspondientes en la tabla `autores`. Esto se hace mediante una condición (`ON posts.autor = autores.Identificador`) que asegura que cada post se vincula al autor correcto basándose en el identificador único del autor en ambas tablas.

Esta consulta es importante porque permite obtener toda la información relevante sobre un post, incluyendo detalles sobre su creador, sin necesidad de realizar consultas adicionales o trabajar con múltiples sentencias SQL. Esto facilita la manipulación y visualización de datos en aplicaciones web o sistemas de gestión de contenidos donde se requiere mostrar información detallada sobre los posts junto a los datos del autor.

`009-peticion cruzada entre tablas.sql`

```sql
SELECT
posts.titulo,
posts.fecha,
posts.contenido,
autores.nombre,
autores.apellidos 
FROM posts
LEFT JOIN autores
ON posts.autor = autores.Identificador;
```

### creacion de una vista
<small>Creado: 2025-10-23 16:40</small>

#### Explicación

Este fragmento de código SQL está diseñado para crear una vista que combina información de dos tablas, `posts` y `autores`. Una vista en SQL es como un alias para una consulta compleja que se puede tratar como si fuera una tabla real. En este caso, la vista llamada `posts_completos` selecciona los campos `titulo`, `fecha`, y `contenido` de la tabla `posts`, así como el nombre y apellidos del autor desde la tabla `autores`.

La consulta utiliza un JOIN izquierdo (LEFT JOIN), lo que significa que se incluirán todos los registros de la tabla principal (`posts`) junto con las coincidencias en la tabla secundaria (`autores`). Si no hay correspondencia en `autores`, los campos del autor para esa fila serán NULL.

La segunda línea del código ejecuta una consulta simple para seleccionar todos los datos de la vista recién creada, lo que permite visualizar cómo se ha combinado la información. Esto es útil para entender rápidamente el contenido que se ha generado a partir de las tablas originales y sirve como una forma de validación inmediata del proceso de creación de la vista.

Crear vistas de esta manera facilita la consulta y manipulación de datos complejos, permitiendo a los desarrolladores obtener información más detallada y fácilmente accesible sin tener que repetir la misma lógica en múltiples lugares del código.

`010-creacion de una vista.sql`

```sql
CREATE VIEW posts_completos AS 
SELECT
posts.titulo,
posts.fecha,
posts.contenido,
autores.nombre,
autores.apellidos 
FROM posts
LEFT JOIN autores
ON posts.autor = autores.Identificador;

SELECT * FROM posts_completos;
```

### simulacro examen programacion
<small>Creado: 2025-10-23 16:50</small>

#### Explicación

Este fragmento de código es muy sencillo y está escrito en Python. En él, se utilizan dos instrucciones `print()` para mostrar texto en la pantalla del usuario. La primera línea muestra el título "Gestión de posts", que probablemente indica que este programa va a gestionar entradas o artículos (posts) en una aplicación web o base de datos.

La segunda línea imprime "v0.1 Jose Vicente Carratalá". Esto es típicamente utilizado para mostrar la versión del programa y el nombre del desarrollador. En este caso, indica que esta es la versión 0.1 del software y que fue creada por alguien llamado Jose Vicente Carratalá.

Este tipo de código es importante porque proporciona información inmediata al usuario sobre qué hace el programa y quién lo creó, además de indicar su estado actual en términos de desarrollo (en este caso, una versión inicial).

`011-simulacro examen programacion.py`

```python
print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")
```

### bucle infinito
<small>Creado: 2025-10-23 16:51</small>

#### Explicación

Este fragmento de código es un pequeño programa en Python que muestra cómo manejar opciones del usuario a través de un menú. El programa comienza mostrando un mensaje de bienvenida y una versión ("v0.1 Jose Vicente Carratalá"). Luego entra en un bucle infinito (`while True`), lo que significa que el menú se repetirá hasta que el programa sea interrumpido manualmente.

Dentro del bucle, se muestra al usuario cuatro opciones: crear una nueva entrada, listar las entradas existentes, actualizar una entrada y eliminar una entrada. El usuario debe ingresar un número (1, 2, 3 o 4) correspondiente a la opción que desea seleccionar. La función `input()` espera la entrada del usuario y luego se convierte en un entero (`int`) para ser utilizado más adelante en el programa.

Este tipo de estructura es común en aplicaciones interactivas donde el usuario puede navegar entre diferentes funcionalidades hasta que decida terminar la aplicación. Es importante destacar cómo se utiliza el bucle infinito junto con una condición de salida implícita (a través del manejo de opciones y posiblemente una opción para salir) para mantener el programa en ejecución hasta que el usuario quiera finalizarlo.

`012-bucle infinito.py`

```python
print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")

while True:
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
```

### controlar las opciones
<small>Creado: 2025-10-23 16:52</small>

#### Explicación

Este código es un programa simple que permite al usuario gestionar entradas (o posts) en un sistema, probablemente para una base de datos. El programa muestra un menú con opciones y espera a que el usuario seleccione una de ellas. La estructura del menú se repite infinitamente gracias al bucle `while True`, lo que significa que el programa seguirá mostrando el menú hasta que sea detenido manualmente.

El código imprime las opciones disponibles:
1. Crear una entrada nueva.
2. Listar todas las entradas existentes.
3. Actualizar una entrada ya creada.
4. Eliminar una entrada.

Después de mostrar estas opciones, el programa solicita al usuario que introduzca un número para seleccionar la opción deseada. La función `input()` espera a que el usuario teclee algo y presione Enter, lo que se convierte en una cadena de texto. Luego, esa cadena se convierte en un entero usando `int()`, lo que permite al programa compararla con los números de las opciones.

Si el usuario selecciona alguna opción, por ejemplo la número 1, el código verificará si la entrada es igual a 1 y ejecutará el bloque correspondiente. En este caso, para cada opción se usa la palabra clave `pass`, lo que significa que no hará nada (solo es un marcador de posición). Cuando desarrolles más esta parte del programa, aquí es donde escribirás las acciones específicas que deben ocurrir según la opción elegida por el usuario.

Este tipo de estructura con menús y opciones es muy común en programas interactivos que permiten a los usuarios realizar varias tareas sin tener que cerrar y abrir nuevamente el programa.

`013-controlar las opciones.py`

```python
print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")

while True:
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    pass
  elif opcion == 2:
    pass
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### insertamos elementos
<small>Creado: 2025-10-23 16:52</small>

#### Explicación

Este código es un ejemplo simple de un menú en consola donde se le pide al usuario que elija una opción entre varias posibilidades. El programa imprime primero un mensaje de bienvenida y versión, luego entra en un bucle infinito `while True` que muestra siempre las mismas opciones al usuario hasta que se detenga manualmente.

El menú ofrece cuatro opciones: crear una entrada nueva, listar todas las entradas existentes, actualizar una entrada ya creada y eliminar una entrada. Cada opción está asociada a un número del 1 al 4. Cuando el usuario introduce su elección mediante `input()`, se convierte esa entrada en un número entero con `int()` para poder compararla con los números de las opciones.

Para cada opción elegida, el programa revisa la elección del usuario utilizando estructuras `if` y `elif`. Actualmente, cuando se selecciona una opción (1 a 4), no ocurre nada debido al uso de `pass`, que es una declaración vacía en Python que simplemente indica "haz nada". Este código está preparado para agregar la funcionalidad específica a cada opción más adelante, como crear las funciones necesarias para gestionar entradas.

Este tipo de estructura es importante porque permite al usuario interactuar con el programa y realizar diferentes tareas según lo que desee hacer en ese momento.

`014-insertamos elementos.py`

```python
print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")

while True:
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    pass
  elif opcion == 2:
    pass
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### insertamos en la base de datos
<small>Creado: 2025-10-23 16:56</small>

#### Explicación

Este código es un programa simple en Python que interactúa con una base de datos MySQL para gestionar entradas (también conocidas como "posts") en un blog. Primero, el programa se conecta a la base de datos utilizando información de conexión como el host, usuario y contraseña. Luego, crea un cursor para ejecutar comandos SQL dentro de la base de datos.

El corazón del código es un bucle `while` que presenta al usuario un menú con cuatro opciones: crear una entrada nueva, listar las entradas existentes, actualizar una entrada o eliminar entradas. Dependiendo de la opción elegida por el usuario, se realizarán diferentes acciones. Actualmente, solo está implementada la opción para crear una nueva entrada.

Cuando el usuario selecciona la opción 1 (Crear entrada nueva), se solicitan al usuario el título, la fecha y el contenido del post, junto con el ID del autor que escribió el post. Estos datos son usados para construir un comando SQL `INSERT` que añade una nueva fila en la tabla `posts`. El método `commit()` de la conexión asegura que los cambios se guarden permanentemente en la base de datos.

Es importante destacar que las opciones 2, 3 y 4 (Listar entradas, Actualizar entrada y Eliminar entradas) están presentes pero no implementadas en este código. Estas serán tareas para el futuro desarrollo del programa.

`015-insertamos en la base de datos.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="usuarioempresarial",
    password="usuarioempresarial",
    database="blogexamen"
)

cursor = conexion.cursor()

print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")

while True:
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
    conexion.commit()
  elif opcion == 2:
    pass
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
    
    
cursor.close()
conexion.close()
```

### usuario con permisos
<small>Creado: 2025-10-23 16:58</small>

#### Explicación

Este fragmento de código SQL te enseña cómo crear un usuario en una base de datos y otorgarle permisos específicos. Primero, crea un nuevo usuario llamado `blogexamen` con la contraseña `Blogexamen123$`. Luego, utiliza el comando `GRANT USAGE` para permitir al usuario acceder a los recursos generales del sistema pero sin darle privilegios en particular.

Después, se ajustan las características de seguridad y limitaciones del usuario recién creado con el comando `ALTER USER`, estableciendo que no requiere un método especial de autenticación (`REQUIRE NONE`) y eliminando cualquier límite predeterminado en términos de número máximo de consultas por hora, conexiones simultáneas, actualizaciones por hora o conexiones totales del usuario.

Finalmente, se conceden todos los privilegios sobre la base de datos `blogexamen` al usuario `blogexamen`. Esto significa que el usuario tiene el control completo sobre esa base de datos específica y puede realizar cualquier operación dentro de ella. Este tipo de configuración es común en entornos donde se necesita un usuario dedicado para gestionar una base de datos particular, manteniendo la seguridad y asegurando que las operaciones no interfieran innecesariamente entre diferentes bases de datos.

`016-usuario con permisos.sql`

```sql
CREATE USER 
'blogexamen'@'localhost' 
IDENTIFIED BY 'Blogexamen123$';

GRANT USAGE ON *.* TO 'blogexamen'@'localhost';

ALTER USER 'blogexamen'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON `blogexamen`.* 
TO 'blogexamen'@'localhost';
```

### insertamos de vuelta
<small>Creado: 2025-10-23 16:59</small>

#### Explicación

Este código es un ejemplo básico de cómo interactuar con una base de datos MySQL desde Python para gestionar entradas en un blog. La aplicación permite al usuario conectarse a la base de datos y realizar varias acciones, como crear nuevas entradas (o posts), listar las existentes, actualizarlas o eliminarlas.

El programa comienza por establecer una conexión a la base de datos utilizando el módulo `mysql.connector`. Luego, se muestra un menú interactivo con cuatro opciones: crear una nueva entrada, listar todas las entradas, actualizar una entrada y eliminar una entrada. La opción elegida por el usuario es determinada mediante la función `input`, que espera a que el usuario teclee una opción numérica.

Si el usuario selecciona la opción 1 (crear una nueva entrada), se le solicitan detalles como el título, fecha, contenido y el ID del autor de la entrada. Estos datos son luego utilizados para ejecutar una consulta SQL INSERT en la base de datos `blogexamen` con la tabla `posts`, insertando un nuevo registro.

El bucle `while True:` asegura que el menú se mantendrá abierto hasta que el usuario decida salir del programa, aunque no hay código actualmente implementado para permitir esa salida. Las opciones 2, 3 y 4 están presentes pero aún no tienen la lógica necesaria para realizar las acciones correspondientes (listar, actualizar, eliminar).

Este tipo de programa es útil para aprender cómo gestionar interactivamente una base de datos desde Python, especialmente en el contexto de aplicaciones web como blogs o sistemas de gestión de contenido.

`017-insertamos de vuelta.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()

print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")

while True:
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
    conexion.commit()
  elif opcion == 2:
    pass
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
    
    
cursor.close()
conexion.close()
```

### listado de entradas
<small>Creado: 2025-10-23 17:01</small>

#### Explicación

Este código Python se conecta a una base de datos MySQL y proporciona un menú interactivo para gestionar entradas (posts) en la base de datos. Primero, el programa establece una conexión con la base de datos usando las credenciales especificadas y crea un cursor que permite ejecutar consultas SQL.

El bucle `while True` muestra un menú al usuario donde puede seleccionar entre varias opciones: crear una nueva entrada (post), listar todas las entradas existentes, actualizar una entrada o eliminar una entrada. Según la opción elegida por el usuario, el programa realiza diferentes acciones:

- Si se escoge "1.-Crear entrada nueva", el usuario introduce los detalles del post como título, fecha, contenido y el ID del autor. Luego, el programa ejecuta una consulta SQL para insertar estos datos en la tabla `posts` de la base de datos.
  
- Si se escoge "2.-Listar entradas", el programa busca todas las filas en la tabla `posts` y luego imprime cada fila en la consola.

Las opciones 3 (Actualizar entrada) y 4 (Eliminar entradas) no tienen implementación actualmente, solo hay código para ejecutar una consulta SQL cuando se seleccione estas opciones. 

Finalmente, después de que el usuario ha terminado con las operaciones, el programa cierra tanto el cursor como la conexión a la base de datos.

Este tipo de aplicación es útil para manejar y ver los datos almacenados en una base de datos desde una interfaz simple en la consola.

`018-listado de entradas.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()

print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")

while True:
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM posts;")
    filas = cursor.fetchall()
    for fila in filas:
      print(fila)
    pass
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
    
    
cursor.close()
conexion.close()
```

### actualizar
<small>Creado: 2025-10-23 17:05</small>

#### Explicación

Este código es una pequeña aplicación en Python que gestiona entradas de un blog almacenadas en una base de datos MySQL. La aplicación se conecta a la base de datos al inicio y ofrece varias opciones para interactuar con los registros de entradas (también conocidos como "posts"):

1. **Crear entrada nueva:** Permite al usuario ingresar el título, fecha, contenido y autor de un nuevo post. Luego, inserta estos datos en la tabla `posts` de la base de datos.
2. **Listar entradas:** Muestra todos los posts existentes en la base de datos.
3. **Actualizar entrada:** Pide al usuario que introduzca el ID del post a actualizar y luego permite cambiar sus detalles (título, fecha, contenido y autor).
4. **Eliminar entradas:** Esta opción está implementada pero no tiene funcionalidad actualmente (el bloque `elif opcion == 4:` solo contiene un `pass`).

El código utiliza bucles y condicionales (`if`, `elif`) para manejar las diferentes opciones del menú, proporcionando una interfaz sencilla que permite a los usuarios interactuar con la base de datos sin necesidad de escribir consultas SQL manualmente. Esta práctica es importante porque facilita el mantenimiento y actualización de la información en entornos donde los cambios son frecuentes.

`019-actualizar.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()

print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")

while True:
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM posts;")
    filas = cursor.fetchall()
    for fila in filas:
      print(fila)
    pass
  elif opcion == 3:
    identificador = input("Introduce el id de la entrada a actualizar: ")
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
    conexion.commit()
    pass
  elif opcion == 4:
    pass
    
    
cursor.close()
conexion.close()
```

### recuperar una tabla destrozada
<small>Creado: 2025-10-23 17:06</small>

#### Explicación

Este fragmento de código SQL realiza varias operaciones en una tabla llamada `posts`. En primer lugar, ejecuta la instrucción `TRUNCATE posts;`, lo que elimina todos los registros existentes en la tabla sin liberar los espacios vacíos utilizados por dicha tabla. Esto es útil para comenzar con un estado limpio de la tabla antes de insertar nuevos datos.

Luego, se seleccionan todas las filas de la tabla `posts` utilizando la instrucción `SELECT * FROM posts;`. Esta consulta te permite ver el contenido actual de la tabla después del truncamiento, aunque en este caso, debido al truncado previo, no debería haber registros a mostrar.

Finalmente, se insertan múltiples filas en la tabla `posts` mediante la declaración `INSERT INTO posts (Identificador, titulo, fecha, contenido, autor) VALUES (...)`. Cada línea dentro de esta instrucción añade una nueva fila con detalles específicos como el identificador del post, título, fecha, contenido y autor. Estos datos son muy variados y representan entradas de blog o artículos relacionados con diferentes aspectos de la inteligencia artificial.

Este código es importante porque demuestra cómo manipular completamente una tabla en SQL: eliminar todos sus registros, verificar que está vacía e insertar múltiples filas de información a través de comandos detallados. Es un buen ejemplo para entender cómo gestionar datos en bases de datos relacionales desde un punto de vista práctico y operativo.

`020-recuperar una tabla destrozada.sql`

```sql
TRUNCATE posts;

SELECT * FROM posts;

INSERT INTO posts (Identificador, titulo, fecha, contenido, autor) VALUES
(1, 'El futuro de la inteligencia artificial', '2025-01-05', 'Una mirada al futuro de la IA.', 1),
(2, 'Redes neuronales explicadas', '2025-01-08', 'Cómo funcionan las redes neuronales.', 2),
(3, 'IA y creatividad artística', '2025-01-12', 'El papel de la IA en el arte moderno.', 3),
(4, 'Aprendizaje profundo simplificado', '2025-01-14', 'Conceptos básicos de deep learning.', 4),
(5, 'Chatbots y atención al cliente', '2025-01-16', 'Cómo los chatbots transforman empresas.', 5),
(6, 'Visión artificial en la medicina', '2025-01-20', 'Diagnósticos automáticos por IA.', 6),
(7, 'Modelos de lenguaje gigantes', '2025-01-23', 'Cómo funcionan los LLM como GPT.', 7),
(8, 'Ética en la inteligencia artificial', '2025-01-25', 'Los dilemas morales de la IA.', 8),
(9, 'Automatización del trabajo', '2025-01-27', 'Impacto de la IA en el empleo.', 9),
(10, 'IA y educación personalizada', '2025-01-30', 'Aprendizaje adaptativo con IA.', 10),
(11, 'Reconocimiento de voz avanzado', '2025-02-02', 'Sistemas de voz y su evolución.', 11),
(12, 'Generación de texto automática', '2025-02-04', 'El auge de los modelos generativos.', 12),
(13, 'Vehículos autónomos', '2025-02-06', 'Cómo la IA conduce sin humanos.', 13),
(14, 'Robótica emocional', '2025-02-08', 'Máquinas que entienden sentimientos.', 14),
(15, 'Machine learning en agricultura', '2025-02-10', 'Optimización de cultivos con IA.', 15),
(16, 'Procesamiento del lenguaje natural', '2025-02-12', 'Cómo las máquinas entienden texto.', 16),
(17, 'IA en ciberseguridad', '2025-02-15', 'Detección inteligente de amenazas.', 17),
(18, 'Algoritmos de recomendación', '2025-02-17', 'Cómo Netflix sabe qué quieres ver.', 18),
(19, 'Simulaciones con IA', '2025-02-19', 'Mundos virtuales impulsados por IA.', 19),
(20, 'IA y sostenibilidad', '2025-02-22', 'Tecnología verde con inteligencia.', 20),
(21, 'Modelos generativos visuales', '2025-02-25', 'Creación de imágenes por IA.', 1),
(22, 'El impacto social de la IA', '2025-02-27', 'Cómo cambia nuestras relaciones.', 2),
(23, 'IA en videojuegos', '2025-03-01', 'NPCs más realistas con IA.', 3),
(24, 'Automatización industrial', '2025-03-03', 'Robots inteligentes en fábricas.', 4),
(25, 'La IA en el mundo financiero', '2025-03-05', 'Predicciones económicas automáticas.', 5),
(26, 'Sistemas expertos modernos', '2025-03-07', 'De la lógica a la inteligencia.', 6),
(27, 'IA para análisis de datos', '2025-03-09', 'Descubriendo patrones ocultos.', 7),
(28, 'Redes neuronales convolucionales', '2025-03-11', 'Cómo ven las máquinas.', 8),
(29, 'Modelos híbridos IA-humanos', '2025-03-13', 'Colaboración entre mente y máquina.', 9),
(30, 'El papel del sesgo algorítmico', '2025-03-15', 'Cómo evitar prejuicios en la IA.', 10),
(31, 'IA aplicada al arte digital', '2025-03-17', 'Pinturas generadas por código.', 11),
(32, 'Modelos preentrenados', '2025-03-19', 'Por qué son tan poderosos.', 12),
(33, 'Aprendizaje no supervisado', '2025-03-21', 'Descubriendo patrones sin etiquetas.', 13),
(34, 'Optimización de hiperparámetros', '2025-03-23', 'Mejorando el rendimiento del modelo.', 14),
(35, 'IA en la salud mental', '2025-03-25', 'Asistentes empáticos digitales.', 15),
(36, 'Interfaces cerebro-máquina', '2025-03-27', 'Comunicación directa con IA.', 16),
(37, 'IA y realidad aumentada', '2025-03-29', 'Fusión del mundo físico y digital.', 17),
(38, 'Data labeling automático', '2025-03-31', 'Cómo entrenar sin etiquetar.', 18),
(39, 'Sistemas de IA explicables', '2025-04-02', 'Haciendo la IA comprensible.', 19),
(40, 'El auge del razonamiento simbólico', '2025-04-04', 'IA que entiende conceptos.', 20),
(41, 'IA distribuida en la nube', '2025-04-06', 'Escalabilidad y potencia.', 1),
(42, 'Reducción del consumo energético', '2025-04-08', 'IA más ecológica y eficiente.', 2),
(43, 'IA en marketing digital', '2025-04-10', 'Personalización extrema de campañas.', 3),
(44, 'Modelos multimodales', '2025-04-12', 'Texto, imagen y sonido unidos.', 4),
(45, 'Simulación del lenguaje humano', '2025-04-14', 'Hacia conversaciones naturales.', 5),
(46, 'IA en logística global', '2025-04-16', 'Rutas y entregas más inteligentes.', 6),
(47, 'Metaaprendizaje', '2025-04-18', 'Modelos que aprenden a aprender.', 7),
(48, 'IA para detección de fraudes', '2025-04-20', 'Protección de transacciones digitales.', 8),
(49, 'Redes generativas adversarias', '2025-04-22', 'La magia detrás de las GANs.', 9),
(50, 'El papel del humano en la era IA', '2025-04-24', 'Colaborar en vez de competir.', 10);

SELECT * FROM  posts;
```

### opcion eliminar
<small>Creado: 2025-10-23 17:08</small>

#### Explicación

Este código es un programa en Python que interactúa con una base de datos MySQL para gestionar entradas de blog. El programa se conecta a la base de datos y muestra un menú al usuario con opciones para crear, listar, actualizar o eliminar entradas.

1. **Conexión a la Base de Datos**: Al inicio del código, el programa establece una conexión a la base de datos MySQL utilizando las credenciales proporcionadas (host, usuario, contraseña y nombre de la base de datos). Esta conexión se utiliza para realizar consultas SQL más adelante en el código.

2. **Menú Interactivo**: Una vez conectado, el programa muestra un menú con opciones numéricas al usuario:
   - Crear una nueva entrada: Solicita los detalles del post (título, fecha, contenido y autor) y ejecuta una consulta `INSERT INTO` para agregar la nueva entrada a la tabla `posts`.
   - Listar entradas existentes: Ejecuta una consulta `SELECT * FROM posts;` que recupera todas las filas de la tabla `posts`. Luego imprime cada fila en la consola.
   - Actualizar una entrada existente: Solicita el ID del post a actualizar y los nuevos detalles. Se ejecuta un comando SQL `UPDATE` para modificar el registro correspondiente en la base de datos.
   - Eliminar una entrada: Pide al usuario que introduzca el ID del post que desea eliminar, después se ejecuta una consulta `DELETE FROM posts WHERE Identificador = <id>;`.

3. **Finalización**: Después de que el usuario finaliza su interacción (presionando Ctrl+C o simplemente terminando la ejecución), el código cierra el cursor y la conexión a la base de datos para liberar recursos.

Este tipo de programa es muy útil en aplicaciones web, permitiendo una gestión sencilla pero completa de registros en una base de datos, ideal para mantener un blog con entradas administrables desde una interfaz de consola.

`021-opcion eliminar.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()

print("Gestión de posts")
print("v0.1 Jose Vicente Carratalá")

while True:
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM posts;")
    filas = cursor.fetchall()
    for fila in filas:
      print(fila)
    pass
  elif opcion == 3:
    identificador = input("Introduce el id de la entrada a actualizar: ")
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
    conexion.commit()
    pass
  elif opcion == 4:
    identificador = input("Introduce el id de la entrada a eliminar: ")
    cursor.execute("DELETE FROM posts WHERE Identificador = "+identificador+";")
    conexion.commit()
    pass
    
    
cursor.close()
conexion.close()
```

### extraccion a funcion parte 1
<small>Creado: 2025-10-23 17:12</small>

#### Explicación

Este fragmento de código es una aplicación sencilla en Python que permite gestionar entradas (posts) en una base de datos MySQL. La aplicación conecta a la base de datos y ofrece al usuario cuatro opciones para interactuar con los posts: crear uno nuevo, listar todos ellos, actualizar un post existente o eliminar uno.

La función `menu()` muestra las diferentes opciones disponibles al usuario y solicita que elija una opción ingresando un número correspondiente. Dependiendo del número seleccionado por el usuario, se ejecutan diferentes bloques de código:

1. **Crear entrada nueva**: Pide al usuario los detalles del post (título, fecha, contenido y ID del autor) e inserta estos datos en la tabla `posts` de la base de datos.
   
2. **Listar entradas**: Consulta todos los registros de la tabla `posts` y muestra cada fila con sus detalles.

3. **Actualizar entrada**: Pide al usuario el identificador del post a actualizar, así como nuevos valores para título, fecha, contenido y autor, luego ejecuta una consulta SQL que actualiza ese registro específico en la base de datos.
   
4. **Eliminar entradas**: Solicita el identificador del post que se desea eliminar y ejecuta una consulta SQL para borrar esa entrada.

Es importante notar que todas las consultas a la base de datos están seguidas por un `commit`, lo cual asegura que los cambios sean guardados permanentemente en la base de datos. El bucle `while True` permite al usuario interactuar repetidamente con el menú hasta que decida salir del programa manualmente, aunque este no está implementado explícitamente en el código mostrado.

Este tipo de aplicación es útil para aprender cómo manejar interacciones básicas entre una base de datos y un usuario a través de un programa de consola.

`022-extraccion a funcion parte 1.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()

def bienvenida():
  print("Gestión de posts")
  print("v0.1 Jose Vicente Carratalá")

def menu():
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))

while True:
  
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM posts;")
    filas = cursor.fetchall()
    for fila in filas:
      print(fila)
    pass
  elif opcion == 3:
    identificador = input("Introduce el id de la entrada a actualizar: ")
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
    conexion.commit()
    pass
  elif opcion == 4:
    identificador = input("Introduce el id de la entrada a eliminar: ")
    cursor.execute("DELETE FROM posts WHERE Identificador = "+identificador+";")
    conexion.commit()
    pass
    
    
cursor.close()
conexion.close()
```

### no solo creo funciones sino que las uso
<small>Creado: 2025-10-23 17:12</small>

#### Explicación

Este código Python es un ejemplo básico de cómo interactuar con una base de datos MySQL desde un programa, utilizando el módulo `mysql.connector`. La aplicación permite a un usuario gestionar entradas en una tabla llamada "posts" mediante funciones específicas.

El programa comienza estableciendo una conexión a la base de datos y creando un cursor para ejecutar consultas. Luego define varias funciones: `bienvenida()` muestra un mensaje de inicio, mientras que `menu()` presenta al usuario opciones para crear nuevas entradas, listar todas las entradas existentes, actualizar o eliminar entradas.

Después de llamar a la función `bienvenida()`, el programa entra en un bucle infinito (`while True`) donde llama repetidamente a la función `menu()` que muestra opciones y solicita al usuario que ingrese una opción. Dependiendo del número ingresado, el programa ejecuta diferentes acciones:

- Si el usuario selecciona "1", se le pide que introduzca los detalles de un nuevo post (título, fecha, contenido, ID del autor) y luego se inserta en la base de datos.
  
- Para la opción "2", se recuperan todos los registros existentes desde la tabla "posts" y se muestran al usuario.
  
- La selección del número "3" permite a un usuario actualizar una entrada específica. Se le solicita que introduzca el ID del post que desea modificar, así como las nuevas entradas de datos para ese post.

- Finalmente, si el usuario selecciona la opción "4", se puede eliminar un post específico ingresando su ID.

El uso de funciones separadas para tareas específicas (como mostrar un menú o realizar acciones en la base de datos) ayuda a mantener el código organizado y más fácil de entender. Además, es importante cerrar la conexión con la base de datos al finalizar las operaciones para liberar recursos.

`023-no solo creo funciones sino que las uso.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()
######################################## FUNCIONES

def bienvenida():
  print("Gestión de posts")
  print("v0.1 Jose Vicente Carratalá")

def menu():
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))
  
######################################## FUNCIONES  

bienvenida()
while True:
  menu()
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM posts;")
    filas = cursor.fetchall()
    for fila in filas:
      print(fila)
    pass
  elif opcion == 3:
    identificador = input("Introduce el id de la entrada a actualizar: ")
    titulo = input("Introduce el titulo: ")
    fecha = input("Introduce la fecha: ")
    contenido = input("Introduce el contenido: ")
    autor = input("Introduce el id del autor: ")
    cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
    conexion.commit()
    pass
  elif opcion == 4:
    identificador = input("Introduce el id de la entrada a eliminar: ")
    cursor.execute("DELETE FROM posts WHERE Identificador = "+identificador+";")
    conexion.commit()
    pass
    
    
cursor.close()
conexion.close()
```

### funciones para las operaciones
<small>Creado: 2025-10-23 17:13</small>

#### Explicación

Este código Python es una aplicación sencilla que permite gestionar entradas en una base de datos MySQL. La aplicación se conecta a la base de datos `blogexamen` y ofrece al usuario un menú con cuatro opciones: crear nueva entrada, listar todas las entradas, actualizar una entrada existente y eliminar una entrada.

### Descripción del código:

1. **Conexión a la Base de Datos**:
   - El script comienza importando el módulo `mysql.connector` para conectarse a MySQL.
   - Establece una conexión con la base de datos usando los detalles proporcionados (host, usuario, contraseña y nombre de la base de datos).

2. **Definición de Funciones**:
   - Se definen varias funciones que realizan operaciones específicas en la base de datos:
     - `bienvenida()`: Imprime un mensaje de bienvenida al programa.
     - `menu()`: Muestra el menú con las opciones disponibles y pide al usuario que seleccione una opción.
     - `insertar()`: Permite al usuario ingresar detalles para crear una nueva entrada en la base de datos (`INSERT INTO posts`).
     - `listar()`: Obtiene todas las entradas existentes desde la tabla `posts` y las imprime.
     - `actualizar()`: Actualiza los datos de una entrada existente basándose en el identificador del post proporcionado por el usuario (`UPDATE posts`).
     - `eliminar()`: Elimina una entrada específica en la base de datos basándose en su identificador (`DELETE FROM posts`).

3. **Ejecución del Programa**:
   - Llama a la función `bienvenida()` para mostrar un mensaje inicial.
   - Inicia un bucle infinito con `while True:` que muestra el menú y espera una opción de entrada del usuario.
   - Dependiendo de la elección del usuario, se llama a las funciones correspondientes (insertar, listar, actualizar o eliminar).
   
### Importancia:
Este código es fundamental para comprender cómo interactuar con bases de datos MySQL desde Python. Aprende a manejar conexiones, ejecutar comandos SQL y controlar flujos de entrada/salida en un entorno web o de consola.

El script se puede mejorar aún más implementando buenas prácticas como validación de entradas del usuario y manejo de excepciones para errores de base de datos.

`024-funciones para las operaciones.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()
######################################## FUNCIONES

def bienvenida():
  print("Gestión de posts")
  print("v0.1 Jose Vicente Carratalá")

def menu():
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))

def insertar():
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
  conexion.commit() 
  
def listar():
  cursor.execute("SELECT * FROM posts;")
  filas = cursor.fetchall()
  for fila in filas:
    print(fila)

def actualizar():
  identificador = input("Introduce el id de la entrada a actualizar: ")
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
  conexion.commit()
  
def eliminar():
  identificador = input("Introduce el id de la entrada a eliminar: ")
  cursor.execute("DELETE FROM posts WHERE Identificador = "+identificador+";")
  conexion.commit()
######################################## FUNCIONES  

bienvenida()
while True:
  menu()
  
  if opcion == 1:
    
  elif opcion == 2:
    

  elif opcion == 3:
    
  elif opcion == 4:

    
    
cursor.close()
conexion.close()
```

### uso las funciones
<small>Creado: 2025-10-23 17:14</small>

#### Explicación

Este código es una pequeña aplicación en Python que permite gestionar entradas de un blog almacenado en una base de datos MySQL. La aplicación proporciona varias funciones para interactuar con los posts, como crear nuevos posts, listar todos los posts existentes, actualizar un post específico y eliminar un post.

1. **Conexión a la Base de Datos:** El código comienza estableciendo una conexión a una base de datos MySQL específica (host 'localhost', usuario 'blogexamen' y contraseña 'Blogexamen123$') utilizando el módulo `mysql.connector`. La base de datos se llama "blogexamen".

2. **Funciones**: Se definen varias funciones para manejar diferentes acciones:
   - `bienvenida()`: Imprime un mensaje de bienvenida.
   - `menu()`: Muestra al usuario una lista de opciones disponibles y solicita que elija una opción.
   - `insertar()`: Permite al usuario crear una nueva entrada en la base de datos, ingresando detalles como el título, fecha, contenido y autor (ID del autor).
   - `listar()`: Recupera todos los posts de la base de datos y los imprime en pantalla.
   - `actualizar()`: Permite a un usuario modificar una publicación existente basándose en su ID.
   - `eliminar()`: Elimina una entrada específica de la base de datos utilizando el identificador único del post.

3. **Ejecución Continua**: El código ejecuta primero la función `bienvenida()` y luego entra en un bucle infinito que muestra el menú al usuario (`menu()`). Dependiendo de la opción elegida por el usuario, se llama a una de las funciones para insertar, listar, actualizar o eliminar entradas. Si el usuario selecciona una opción no válida, simplemente vuelve a mostrar el menú hasta que se seleccione una opción correcta.

Esta estructura es útil en aplicaciones donde necesitas proporcionar un conjunto básico de operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para gestionar datos en una base de datos.

`025-uso las funciones.py`

```python
import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()
######################################## FUNCIONES

def bienvenida():
  print("Gestión de posts")
  print("v0.1 Jose Vicente Carratalá")

def menu():
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))

def insertar():
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
  conexion.commit() 
  
def listar():
  cursor.execute("SELECT * FROM posts;")
  filas = cursor.fetchall()
  for fila in filas:
    print(fila)

def actualizar():
  identificador = input("Introduce el id de la entrada a actualizar: ")
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
  conexion.commit()
  
def eliminar():
  identificador = input("Introduce el id de la entrada a eliminar: ")
  cursor.execute("DELETE FROM posts WHERE Identificador = "+identificador+";")
  conexion.commit()
######################################## FUNCIONES  

bienvenida()
while True:
  menu()
  
  if opcion == 1:
    insertar()
  elif opcion == 2:
    listar()
  elif opcion == 3:
    actualizar()
  elif opcion == 4:
    eliminar()
    
    
cursor.close()
conexion.close()
```

### vamos a documentar un poco
<small>Creado: 2025-10-23 17:15</small>

#### Explicación

Este código es un programa en Python que permite gestionar entradas de un blog en una base de datos MySQL. El objetivo principal del programa es permitir al usuario realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre las entradas del blog.

En primer lugar, el programa se conecta a la base de datos MySQL usando credenciales específicas. Luego, define varias funciones que manejan diferentes aspectos de la gestión de posts:

- `bienvenida()` muestra un mensaje inicial con información sobre el programa.
- `menu()` presenta al usuario un menú interactivo con opciones para crear nuevas entradas, listar todas las entradas existentes, actualizar una entrada específica o eliminar una entrada por su identificador.
- `insertar()`, `listar()`, `actualizar()` y `eliminar()` son funciones que realizan operaciones SQL (Structured Query Language) en la base de datos para insertar nuevos posts, recuperar todos los posts almacenados, modificar un post existente o borrar uno.

El programa principal comienza ejecutando la función `bienvenida()`, luego entra en un bucle infinito donde muestra el menú al usuario y realiza la acción correspondiente según la opción seleccionada por el usuario. El programa finaliza cuando el bucle se sale de él, cerrando también las conexiones a la base de datos.

Este tipo de programa es importante para entender cómo interactuar con bases de datos desde Python utilizando consultas SQL, así como para aprender sobre la creación y uso de menús interactivos en aplicaciones de consola.

`026-vamos a documentar un poco.py`

```python
'''
  Programa gestor de posts de blog
  v 0.1 por Jose Vicente Carratala
  Programa que hace CRUD sobre una base de datos de posts en MySQL
'''

import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()
######################################## FUNCIONES

def bienvenida():
  print("Gestión de posts")
  print("v0.1 Jose Vicente Carratalá")

def menu():
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))

def insertar():
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
  conexion.commit() 
  
def listar():
  cursor.execute("SELECT * FROM posts;")
  filas = cursor.fetchall()
  for fila in filas:
    print(fila)

def actualizar():
  identificador = input("Introduce el id de la entrada a actualizar: ")
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
  conexion.commit()
  
def eliminar():
  identificador = input("Introduce el id de la entrada a eliminar: ")
  cursor.execute("DELETE FROM posts WHERE Identificador = "+identificador+";")
  conexion.commit()
######################################## FUNCIONES  

bienvenida()
while True:
  menu()
  if opcion == 1:
    insertar()
  elif opcion == 2:
    listar()
  elif opcion == 3:
    actualizar()
  elif opcion == 4:
    eliminar()
    
    
cursor.close()
conexion.close()
```

### documento las funciones
<small>Creado: 2025-10-23 17:16</small>

#### Explicación

Este código es un programa simple que permite gestionar entradas en un blog utilizando una base de datos MySQL. El programa ofrece al usuario cuatro opciones principales: crear nuevas entradas, listar todas las entradas existentes, actualizar entradas existentes y eliminar entradas.

El código comienza estableciendo una conexión a la base de datos MySQL con los detalles proporcionados (host, usuario, contraseña y nombre de la base de datos). Luego define varias funciones que realizan tareas específicas:

1. **bienvenida()**: Imprime un mensaje de bienvenida al iniciar el programa.
2. **menu()**: Muestra las opciones disponibles y solicita al usuario que seleccione una opción.
3. **insertar()**: Pide al usuario los detalles para crear una nueva entrada (título, fecha, contenido y autor) y ejecuta una consulta SQL INSERT para añadir la entrada a la base de datos.
4. **listar()**: Ejecuta un SELECT * FROM posts; en la base de datos para recuperar todas las entradas existentes e imprime cada fila en pantalla.
5. **actualizar()**: Solicita al usuario el identificador del post que desea actualizar, junto con los nuevos valores para título, fecha, contenido y autor, luego ejecuta una consulta UPDATE en la base de datos.
6. **eliminar()**: Pide al usuario el identificador del post a eliminar y ejecuta una consulta DELETE FROM posts WHERE Identificador = <id>.

Después de definir las funciones, se llama a la función bienvenida(), seguida de un bucle while que muestra el menú y llama a las funciones correspondientes según la opción elegida por el usuario. El programa continuará mostrando este menú hasta que sea detenido manualmente.

Este tipo de estructura es importante porque permite al usuario interactuar fácilmente con la base de datos para realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los posts del blog, lo cual es una habilidad fundamental en el desarrollo web.

`027-documento las funciones.py`

```python
'''
  Programa gestor de posts de blog
  v 0.1 por Jose Vicente Carratala
  Programa que hace CRUD sobre una base de datos de posts en MySQL
'''

import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()
######################################## FUNCIONES

def bienvenida():
  # Imprime un mensaje de bienvenida una sola vez
  print("Gestión de posts")
  print("v0.1 Jose Vicente Carratalá")

def menu():
  # Ofrece una serie de opciones al usuario
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))

def insertar():
  # Inserta un registro en la base de datos
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
  conexion.commit() 
  
def listar():
  # Lista los registros
  cursor.execute("SELECT * FROM posts;")
  filas = cursor.fetchall()
  for fila in filas:
    print(fila)

def actualizar():
  # actualiza un registro de la base de datos
  identificador = input("Introduce el id de la entrada a actualizar: ")
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
  conexion.commit()
  
def eliminar():
  # Elimina un registro de la base de datos
  identificador = input("Introduce el id de la entrada a eliminar: ")
  cursor.execute("DELETE FROM posts WHERE Identificador = "+identificador+";")
  conexion.commit()
######################################## FUNCIONES  

bienvenida()
while True:
  menu()
  if opcion == 1:
    insertar()
  elif opcion == 2:
    listar()
  elif opcion == 3:
    actualizar()
  elif opcion == 4:
    eliminar()
    
    
cursor.close()
conexion.close()
```

### solucion al problema
<small>Creado: 2025-10-23 17:18</small>

#### Explicación

Este programa es una aplicación simple para gestionar entradas en un blog, utilizando una base de datos MySQL. El programa permite al usuario realizar operaciones básicas de creación (CREATE), lectura (READ), actualización (UPDATE) y eliminación (DELETE) sobre registros en la tabla `posts` de la base de datos.

El código comienza estableciendo una conexión a la base de datos utilizando el módulo `mysql.connector`. Luego, se definen varias funciones que manejan diferentes aspectos del CRUD:

- La función `bienvenida()` imprime un mensaje al usuario cuando inicia el programa.
- La función `menu()` presenta un menú interactivo con opciones para crear una nueva entrada, listar todas las entradas existentes, actualizar una entrada existente y eliminar una entrada.
- Las funciones `insertar()`, `listar()`, `actualizar()` y `eliminar()` realizan operaciones específicas en la base de datos según la opción elegida por el usuario.

El programa se ejecuta dentro de un bucle infinito (`while True:`), mostrando siempre el menú al usuario hasta que decida cerrarlo manualmente. Dependiendo de la elección del usuario, las funciones correspondientes son llamadas para realizar la acción deseada. Al finalizar cada operación, los cambios en la base de datos se confirman utilizando `conexion.commit()`.

Esta estructura permite a un administrador o autor del blog gestionar fácilmente sus entradas desde una interfaz sencilla y controlada por menú.

`028-solucion al problema.py`

```python
'''
  Programa gestor de posts de blog
  v 0.1 por Jose Vicente Carratala
  Programa que hace CRUD sobre una base de datos de posts en MySQL
'''

import mysql.connector

# Me conecto a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor()
######################################## FUNCIONES

opcion = 0

def bienvenida():
  # Imprime un mensaje de bienvenida una sola vez
  print("Gestión de posts")
  print("v0.1 Jose Vicente Carratalá")

def menu():
  # Ofrece una serie de opciones al usuario
  global opcion
  print("Escoge una opción:")
  print("1.-Crear entrada nueva")
  print("2.-Listar entradas")
  print("3.-Actualizar entrada")
  print("4.-Eliminar entradas")
  opcion = int(input("Escoge una opcion: "))

def insertar():
  # Inserta un registro en la base de datos
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("INSERT INTO posts VALUES (NULL,'"+titulo+"','"+fecha+"','"+contenido+"',"+autor+");")
  conexion.commit() 
  
def listar():
  # Lista los registros
  cursor.execute("SELECT * FROM posts;")
  filas = cursor.fetchall()
  for fila in filas:
    print(fila)

def actualizar():
  # actualiza un registro de la base de datos
  identificador = input("Introduce el id de la entrada a actualizar: ")
  titulo = input("Introduce el titulo: ")
  fecha = input("Introduce la fecha: ")
  contenido = input("Introduce el contenido: ")
  autor = input("Introduce el id del autor: ")
  cursor.execute("UPDATE posts SET titulo = '"+titulo+"', fecha = '"+fecha+"', contenido = '"+contenido+"', autor = "+autor+" WHERE Identificador = "+identificador+";")
  conexion.commit()
  
def eliminar():
  # Elimina un registro de la base de datos
  identificador = input("Introduce el id de la entrada a eliminar: ")
  cursor.execute("DELETE FROM posts WHERE Identificador = "+identificador+";")
  conexion.commit()
######################################## FUNCIONES  

bienvenida()
while True:
  menu()
  if opcion == 1:
    insertar()
  elif opcion == 2:
    listar()
  elif opcion == 3:
    actualizar()
  elif opcion == 4:
    eliminar()
    
    
cursor.close()
conexion.close()
```

### simulacro blog
<small>Creado: 2025-10-23 17:27</small>

#### Explicación

Este fragmento de código HTML crea una página web simple para un blog. La estructura principal incluye tres secciones: `header`, `main` y `footer`. En el encabezado (`header`) se muestra el título del blog "El blog de Jose Vicente", mientras que en el pie de la página (`footer`) aparece la información de derechos de autor.

En la parte central, marcada como `main`, hay un artículo con elementos básicos típicos de un post de blog: un título, una fecha, el nombre del autor y el contenido del artículo. Estos componentes están estructurados para que sean fácilmente identificables tanto por los usuarios como por motores de búsqueda.

La hoja de estilos integrada en la sección `<style>` dentro del encabezado (`head`) define el diseño básico: un fondo gris, una fuente sin serif y dimensiones específicas para las tres secciones principales, asegurando que todo está centrado y cómodo para leer. Este tipo de estructura ayuda a mantener un diseño limpio y fácil de navegar, lo cual es importante para mejorar la experiencia del usuario en el sitio web.

`029-simulacro blog.html`

```html
<!doctype html>
<html>
  <head>
    <title>El blog de Jose Vicente</title>
    <style>
      body,html{background:grey;font-family:sans-serif;}
      header,main,footer{background:white;padding:50px;width:600px;margin:auto;}
    </style>  
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
      <article>
        <h3>Titulo</h3>
        <time>Fecha</time>
        <p>Autor</p>
        <p>Contenido</p>
      </article>
    </main>
    <footer>
      (c) 2025 Jose Vicente Carratala
    </footer>
  </body>
</html>
```

### arrancamos flask
<small>Creado: 2025-10-23 17:28</small>

#### Explicación

Este fragmento de código está utilizando la biblioteca Flask para crear una aplicación web sencilla en Python. Primero, importamos `Flask` desde el módulo flask. Luego, creamos un objeto de la clase `Flask`, que representa nuestra aplicación web, y lo guardamos en la variable `aplicacion`. 

El decorador `@aplicacion.route("/")` indica a Flask que cuando alguien visite la página principal (URL raíz) de nuestro sitio web, debe ejecutar la función `raiz()`. Esta función simplemente devuelve el texto "Hola mundo" como respuesta.

Por último, el bloque `if __name__ == "__main__":` asegura que nuestra aplicación solo se inicie si estamos ejecutando directamente este script (no importándolo desde otro archivo). Dentro de este bloque, llamamos a `aplicacion.run()` para iniciar nuestro servidor web local. Esto permite que puedas ver y probar tu sitio web en un navegador web.

Este código es importante porque sirve como una introducción básica al uso del framework Flask para crear aplicaciones web dinámicas con Python.

`030-arrancamos flask.py`

```python
from flask import Flask  

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():

  return "Hola mundo"
  
if __name__ == "__main__":
  aplicacion.run()
```

### en flask ponemos nuestra web
<small>Creado: 2025-10-23 17:29</small>

#### Explicación

Este código es una aplicación web básica creada con Flask, un framework de Python que facilita el desarrollo de sitios web. El archivo define una aplicación web sencilla que muestra una página HTML estática cuando se accede a la URL raíz del sitio (es decir, `http://localhost/`).

En primer lugar, importamos `Flask` desde el módulo flask y creamos una instancia de la clase Flask llamada `aplicacion`. Luego, usamos un decorador `@aplicacion.route("/")` para indicar que cuando se haga una solicitud a la URL raíz ("/"), debe ejecutarse la función `raiz()`. Dentro de esta función, definimos todo el contenido HTML necesario para mostrar una página web simple con un encabezado, un cuerpo principal y un pie de página.

La función `raiz()` devuelve directamente una cadena que contiene toda la estructura del documento HTML. Esto incluye metadatos como el título de la página, estilos básicos y elementos estructurales tales como un encabezado (`header`), contenido principal (`main`) con un artículo dentro (que simboliza un post del blog) y un pie de página (`footer`). Finalmente, si este archivo se ejecuta directamente (no importado por otro script), la aplicación Flask comienza a escuchar peticiones en un servidor local usando `aplicacion.run()`.

Esta forma simple pero efectiva de generar una página web estática con Flask permite a los desarrolladores crear interfaces rápidas y básicas para sus aplicaciones o sitios web, facilitando el desarrollo inicial antes de pasar a implementar funcionalidades más complejas.

`031-en flask ponemos nuestra web.py`

```python
from flask import Flask  

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
    <!doctype html>
    <html>
      <head>
        <title>El blog de Jose Vicente</title>
        <style>
          body,html{background:grey;font-family:sans-serif;}
          header,main,footer{background:white;padding:50px;width:600px;margin:auto;}
        </style>  
      </head>
      <body>
        <header>
          <h1>El blog de Jose Vicente</h1>
        </header>
        <main>
          <article>
            <h3>Titulo</h3>
            <time>Fecha</time>
            <p>Autor</p>
            <p>Contenido</p>
          </article>
        </main>
        <footer>
          (c) 2025 Jose Vicente Carratala
        </footer>
      </body>
    </html>
  '''
  return cadena
  
if __name__ == "__main__":
  aplicacion.run()
```

### me conecto con mysql
<small>Creado: 2025-10-23 17:33</small>

#### Explicación

Este código Python es una parte de un proyecto web simple utilizando la biblioteca Flask. El objetivo principal es crear una página web que muestra entradas desde una base de datos MySQL.

Primero, se establece una conexión a la base de datos MySQL usando `mysql.connector` con los detalles proporcionados (host, usuario, contraseña y nombre de la base de datos). Luego, un objeto cursor es creado para ejecutar consultas SQL en la base de datos. 

La función principal del código es definir el manejo de la ruta raíz ("/") de la aplicación Flask. Cuando se accede a esta ruta, se genera una respuesta HTML que incluye los títulos y contenidos de todas las entradas almacenadas en la tabla `posts_completos` de la base de datos. Se ejecuta una consulta SQL para recuperar todos estos registros y luego se iteran sobre ellos para construir el cuerpo del documento HTML, añadiendo cada entrada como un artículo con detalles específicos.

Finalmente, si este script es ejecutado directamente (no importado por otro módulo), la aplicación Flask se inicia en modo de desarrollo local. Esto permite que la página web sea accesible desde el navegador y veamos los datos recuperados de la base de datos MySQL en una interfaz HTML simple.

Este código es importante porque demuestra cómo interactuar con bases de datos desde aplicaciones web utilizando Python, mostrando también un ejemplo básico de generación dinámica de páginas web basadas en contenido de la base de datos.

`032-me conecto con mysql.py`

```python
from flask import Flask 
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor() 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
    <!doctype html>
    <html>
      <head>
        <title>El blog de Jose Vicente</title>
        <style>
          body,html{background:grey;font-family:sans-serif;}
          header,main,footer{background:white;padding:50px;width:600px;margin:auto;}
        </style>  
      </head>
      <body>
        <header>
          <h1>El blog de Jose Vicente</h1>
        </header>
        <main>'''
  cursor.execute("SELECT * FROM posts_completos;")
  filas = cursor.fetchall()
  for fila in filas:
    cadena += '''
          <article>
            <h3>'''+fila[0]+'''</h3>
            <time>'''+fila[1]+'''</time>
            <p>'''+fila[3]+''' '''+fila[4]+'''</p>
            <p>'''+fila[2]+'''</p>
          </article>
    '''
  cadena += '''
        </main>
        <footer>
          (c) 2025 Jose Vicente Carratala
        </footer>
      </body>
    </html>
  '''
  return cadena
  
if __name__ == "__main__":
  aplicacion.run()
```

### mejoramos el estilo
<small>Creado: 2025-10-23 17:35</small>

#### Explicación

Este código Python crea una aplicación web simple utilizando la biblioteca Flask, que es un framework para crear aplicaciones web rápidas y fáciles de usar en Python. La función principal del código es mostrar los artículos de un blog almacenados en una base de datos MySQL.

1. **Conexión a la Base de Datos**: El código comienza estableciendo una conexión con una base de datos MySQL llamada "blogexamen" utilizando las credenciales proporcionadas (usuario: `blogexamen`, contraseña: `Blogexamen123$`). Esta conexión es utilizada para ejecutar consultas SQL.

2. **Estructura HTML Generada en Tiempo Real**: Cuando un usuario accede a la URL raíz del sitio web, el código genera dinámicamente una página HTML que muestra los artículos almacenados en la base de datos. La consulta SQL `SELECT * FROM posts_completos;` se ejecuta para obtener todos los registros de la tabla `posts_completos`. Cada fila obtenida es luego procesada por un bucle for, donde cada campo del registro se inserta en una plantilla HTML que incluye el título del artículo, fecha y contenido.

3. **Servidor Web**: Finalmente, el código configura Flask para ejecutar la aplicación web en modo de desarrollo local. Cuando alguien visita la URL raíz (por ejemplo, `http://localhost:5000/`), verán una página con un encabezado que dice "El blog de Jose Vicente", seguido por los artículos del blog obtenidos desde la base de datos y finalmente un pie de página con información de derechos de autor.

Esta práctica es común en el desarrollo web moderno, permitiendo a las aplicaciones web interactuar directamente con bases de datos para mostrar contenido actualizado automáticamente.

`033-mejoramos el estilo.py`

```python
from flask import Flask 
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor() 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
    <!doctype html>
    <html>
      <head>
        <title>El blog de Jose Vicente</title>
        <style>
          *{padding:0px;margin:0px;}
          body,html{background:grey;font-family:sans-serif;}
          header,main,footer{background:white;padding:50px;width:600px;margin:auto;}
          main{display:flex;flex-direction:column;gap:50px;}
        </style>  
      </head>
      <body>
        <header>
          <h1>El blog de Jose Vicente</h1>
        </header>
        <main>'''
  cursor.execute("SELECT * FROM posts_completos;")
  filas = cursor.fetchall()
  for fila in filas:
    cadena += '''
          <article>
            <h3>'''+fila[0]+'''</h3>
            <time>'''+fila[1]+'''</time>
            <p>'''+fila[3]+''' '''+fila[4]+'''</p>
            <p>'''+fila[2]+'''</p>
          </article>
    '''
  cadena += '''
        </main>
        <footer>
          (c) 2025 Jose Vicente Carratala
        </footer>
      </body>
    </html>
  '''
  return cadena
  
if __name__ == "__main__":
  aplicacion.run()
```

### articulos por fecha inversa
<small>Creado: 2025-10-23 17:36</small>

#### Explicación

Este código es un ejemplo sencillo de cómo crear una página web dinámica utilizando la biblioteca Flask en Python. La página muestra los artículos de un blog ordenados por fecha, comenzando con el más reciente.

El código comienza creando una conexión a una base de datos MySQL que contiene información sobre los posts del blog. Luego, utiliza esta conexión para seleccionar todos los registros de la tabla `posts_completos` y ordenarlos según su campo `fecha`, en orden descendente (es decir, el artículo más reciente primero).

La parte central del código se encarga de generar un HTML dinámico que muestra estos artículos. Cada artículo es presentado con sus detalles: título, fecha, autor y contenido. Este HTML está incluido dentro de una estructura completa que define la página web, incluyendo estilos básicos para el header, main (cuerpo principal) y footer.

Finalmente, cuando se ejecuta este script directamente (no como un import en otro módulo), Flask inicia su propio servidor web local, permitiendo visualizar la página en un navegador web. Esto es útil para pruebas rápidas y desarrollo de aplicaciones web pequeñas o prototipos.

Este tipo de código es fundamental para aprender a integrar bases de datos con interfaces web dinámicas, una habilidad clave en el desarrollo moderno de aplicaciones web.

`034-articulos por fecha inversa.py`

```python
from flask import Flask 
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="blogexamen",
    password="Blogexamen123$",
    database="blogexamen"
)

cursor = conexion.cursor() 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
    <!doctype html>
    <html>
      <head>
        <title>El blog de Jose Vicente</title>
        <style>
          *{padding:0px;margin:0px;}
          body,html{background:grey;font-family:sans-serif;}
          header,main,footer{background:white;padding:50px;width:600px;margin:auto;}
          main{display:flex;flex-direction:column;gap:50px;}
        </style>  
      </head>
      <body>
        <header>
          <h1>El blog de Jose Vicente</h1>
        </header>
        <main>'''
  cursor.execute("SELECT * FROM posts_completos ORDER BY fecha DESC;")
  filas = cursor.fetchall()
  for fila in filas:
    cadena += '''
          <article>
            <h3>'''+fila[0]+'''</h3>
            <time>'''+fila[1]+'''</time>
            <p>'''+fila[3]+''' '''+fila[4]+'''</p>
            <p>'''+fila[2]+'''</p>
          </article>
    '''
  cadena += '''
        </main>
        <footer>
          (c) 2025 Jose Vicente Carratala
        </footer>
      </body>
    </html>
  '''
  return cadena
  
if __name__ == "__main__":
  aplicacion.run()
```

### Actividades propuestas

This series of files outlines a comprehensive process for building and deploying a simple blog application, from the initial idea to its final deployment. Here's a breakdown of what each file accomplishes:

1. **Simulation Documents**:
   - `001-simulacro de la web.txt` and `002-simulacro de la web.jpg`: These files likely contain mockups or simulations of how the blog will look when it is fully developed.

2. **Basic HTML Structure**:
   - `003-diseño inicial.html`, `004-estructura de la página.html`, and subsequent HTML files (`005-artículo completo.html`): These files gradually refine the structure and appearance of the blog's main pages, including the article layout and overall design.

3. **Python Script for Blog Management**:
   - `018-blog.py`: This file likely contains a Python script to manage the blog's backend operations using MySQL or another database system.
   
4. **Database Setup**:
   - Files from `019-creamos la base de datos.sql` to `027-insertamos los posts.sql`: These SQL files create and populate the blog’s database, defining tables like `usuarios`, `posts`, and relationships within them.

5. **Python Script for Blog Management with MySQL**:
   - `028-blog.py`: This script connects Python to the MySQL database to manage blog posts, likely including functions to add, update, delete, and retrieve articles from the database.
   
6. **Command Line Script for Blog Management**:
   - Files like `029-comandos de la terminal.txt` and `030-ejecutamos el script.txt`: These files contain instructions on how to run Python scripts that interact with the blog’s MySQL database.

7. **Blog Application in Python (CLI)**:
   - `031-arrancamos el blog.py`, `032-el blog completo.py`, and subsequent files: These scripts refine a command-line interface for managing the blog, including adding articles, listing posts, and handling user input.
   
8. **Web Application with Flask**:
   - Files from `030-en flask ponemos nuestra web.py` to `034-articulos por fecha inversa.py`: This progression introduces using Flask (Python’s microframework for web development) to build a web-based interface for the blog, starting with basic HTML embedding and progressing to dynamic content generation based on database queries.

9. **Deployment**:
   - While not explicitly detailed in these files, deployment steps would typically follow after setting up all functionalities locally, involving deploying the Flask application to a server or cloud service (such as Heroku, AWS, etc.), ensuring that it can connect to its MySQL database and serve web pages dynamically based on user requests.

### Key Concepts Covered:
- **HTML/CSS**: Basic webpage structure and styling.
- **SQL**: Creating and populating databases for storing blog data.
- **Python/MySQL**: Using Python scripts to interact with a MySQL database, including CRUD operations (Create, Read, Update, Delete).
- **Flask**: Building web applications in Python using Flask framework, embedding HTML content dynamically based on SQL queries.

### Next Steps:
To fully deploy this application, you would need to set up your server environment properly. This could involve:

1. Setting up a remote MySQL database.
2. Creating an appropriate virtual environment for your Flask app and installing necessary packages (like `flask` and `mysql-connector-python`).
3. Configuring the Flask application to connect to your remote database.
4. Deploying the Flask application on a server or cloud platform, making sure it runs continuously using tools like Gunicorn with uWSGI or similar setups.

By following these steps and utilizing the scripts provided in the files above, you can create a functional blog system that combines frontend presentation via HTML/CSS and backend logic through Python and MySQL.


<a id="simulacro-examen-programacion"></a>
## Simulacro examen programacion

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/010-Simulacro%20examen%20programacion)


<a id="simulacro-de-examen-2"></a>
## Simulacro de examen 2

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/011-Simulacro%20de%20examen%202)

### Introducción a los ejercicios

Este conjunto de ejercicios está diseñado para que los estudiantes trabajen en la creación de un programa básico de gestión de portafolio utilizando Python y MySQL. El objetivo principal es desarrollar una interfaz sencilla donde el usuario pueda realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar) sobre registros almacenados en una base de datos.

Los ejercicios se centran en la interacción con bases de datos a través de SQL desde Python, incluyendo la conexión a la base de datos, la ejecución de consultas SELECT para listar registros, INSERT para agregar nuevos registros, UPDATE para modificar existentes y DELETE para eliminar registros. Los estudiantes también practicarán estructuras de control como bucles y condicionales para manejar las opciones del menú y realizar acciones basadas en la entrada del usuario.

Esta serie de ejercicios permite a los alumnos consolidar sus conocimientos sobre el uso de bases de datos y cómo integrarlas con aplicaciones Python, además de reforzar habilidades como la captura y validación de entradas del usuario.

### bienvenida
<small>Creado: 2025-11-03 15:19</small>

#### Explicación

Este código es un fragmento de un programa en Python que muestra al usuario un menú simple y permite seleccionar una opción. Primero, el programa imprime varias líneas para presentar la aplicación llamada "Gestión de portafolio v0.1" y muestra las diferentes opciones disponibles: insertar, listar, actualizar y eliminar. Luego, pide al usuario que introduzca su elección a través del teclado utilizando la función `input()`. La entrada del usuario se convierte en un número entero con la función `int()` y se guarda en una variable llamada `opcion`.

Finalmente, el programa imprime el texto "La opción que has escogido es:" seguido de la opción seleccionada por el usuario. Este código es importante porque establece la interacción básica entre el programa y el usuario, permitiendo al usuario navegar por las funcionalidades básicas del sistema según su elección.

`002-bienvenida.py`

```python
print("Gestion de portafolio v0.1")
print("Escoge una opcion")
print("1.-Insertar")
print("2.-Listar")
print("3.-Actualizar")
print("4.-Eliminar")
opcion = int(input("Escoge una opcion: "))
print("La opción que has escogido es: ",opcion)
```

### me conecto a la base de datos
<small>Creado: 2025-11-03 15:21</small>

#### Explicación

Este fragmento de código se encarga de establecer una conexión con una base de datos MySQL y luego realizar una consulta para obtener todos los registros de la tabla llamada "piezas". El programa comienza importando el módulo `mysql.connector`, que es una biblioteca en Python utilizada para interactuar con bases de datos MySQL. Luego, se crea una conexión a la base de datos utilizando las credenciales proporcionadas (host, usuario, contraseña y nombre de la base de datos).

Después de establecer la conexión, el programa muestra un menú simple al usuario para que pueda seleccionar una opción (en este caso solo se muestra cómo realizar una consulta SELECT, por lo que no hay código específico para las otras opciones). Una vez que el usuario selecciona una opción y esta es confirmada como la consulta SELECT, el código crea un objeto cursor a partir de la conexión. Un cursor permite ejecutar consultas SQL.

La línea `cursor.execute("SELECT * FROM piezas;")` ejecuta la consulta SQL que selecciona todos los registros (indicado por el asterisco *) desde la tabla "piezas". Luego, `fetchall()` recupera todas las filas del resultado de la consulta y se almacenan en una variable llamada `lineas`. Finalmente, el código itera sobre cada fila obtenida y la imprime en la consola.

Esta parte es importante porque muestra cómo interactuar con una base de datos para recuperar información y luego procesarla o mostrarla en un programa Python.

`003-me conecto a la base de datos.py`

```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolio",
  password="portafolio",
  database="portafolio"
)

print("Gestion de portafolio v0.1")
print("Escoge una opcion")
print("1.-Insertar")
print("2.-Listar")
print("3.-Actualizar")
print("4.-Eliminar")
opcion = int(input("Escoge una opcion: "))
print("La opción que has escogido es: ",opcion)

cursor = conexion.cursor() 
cursor.execute("SELECT * FROM piezas;")

lineas = cursor.fetchall()
for linea in lineas:
  print(linea)
```

### estructuras de control
<small>Creado: 2025-11-03 15:26</small>

#### Explicación

Este fragmento de código es un ejemplo básico de cómo interactuar con una base de datos MySQL desde Python. El programa conecta a una base de datos llamada "portafolio" y muestra las filas de la tabla `piezas`. Además, presenta al usuario un menú para seleccionar una opción.

Primero, el script importa la biblioteca `mysql.connector`, que permite a Python conectarse y realizar operaciones en bases de datos MySQL. Luego, establece una conexión con la base de datos usando las credenciales proporcionadas (en este caso, suponemos que el usuario tiene acceso sin necesidad de contraseña para localhost).

Después de hacer la conexión, el programa imprime un menú sencillo donde el usuario puede seleccionar entre varias operaciones. Sin embargo, en este código, no se implementan las funciones para insertar, actualizar o eliminar datos; solo muestra un mensaje indicando la opción elegida por el usuario y luego ejecuta una consulta SQL que recupera todas las filas de la tabla `piezas` en la base de datos.

El resultado de esta consulta es almacenado en la variable `lineas`, que contiene tuplas con los valores de cada fila. El código finalmente imprime cada línea, mostrando así todos los registros presentes en la tabla `piezas`.

Este tipo de programa es importante porque demuestra cómo realizar operaciones básicas en una base de datos desde Python y proporciona un punto de partida para implementar funcionalidades más complejas como inserciones, actualizaciones y eliminaciones.

`004-estructuras de control.py`

```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolio",
  password="portafolio",
  database="portafolio"
)

print("Gestion de portafolio v0.1")
while True:
  print("Escoge una opcion")
  print("1.-Insertar")
  print("2.-Listar")
  print("3.-Actualizar")
  print("4.-Eliminar")
  opcion = int(input("Escoge una opcion: "))
  print("La opción que has escogido es: ",opcion)

  cursor = conexion.cursor() 
  cursor.execute("SELECT * FROM piezas;")

  lineas = cursor.fetchall()
  for linea in lineas:
    print(linea)
```

### atrapo la opcion del usuario
<small>Creado: 2025-11-03 15:27</small>

#### Explicación

Este código es una pequeña aplicación en Python que permite al usuario interactuar con una base de datos MySQL para gestionar un portafolio. La aplicación se conecta a la base de datos primero y luego muestra un menú interactivo donde el usuario puede seleccionar entre varias opciones: insertar, listar, actualizar o eliminar datos.

Cuando el programa comienza, establece una conexión a una base de datos local llamada "portafolio" usando las credenciales proporcionadas. Luego entra en un bucle infinito (`while True`) que muestra al usuario cuatro opciones disponibles y pide que seleccione una mediante la entrada del teclado.

Si el usuario escoge la opción 2 (Listar), se ejecuta una consulta SQL para recuperar todos los registros de una tabla llamada "piezas" en la base de datos. Los resultados de esta consulta se almacenan en una variable y luego se imprimen línea por línea en la pantalla.

Las opciones 1, 3 y 4 están actualmente marcadas como `pass`, lo que significa que el código no hace nada con estas selecciones. Este es un lugar donde puedes implementar la lógica para insertar datos, actualizar registros o eliminar entradas de la base de datos según sea necesario.

Esta estructura de menú y control de flujo permite a los usuarios interactuar fácilmente con la aplicación y realizar operaciones básicas en la base de datos. Es un buen ejemplo práctico del uso de bucles condicionales y módulos para manejar conexiones a bases de datos en Python.

`005-atrapo la opcion del usuario.py`

```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolio",
  password="portafolio",
  database="portafolio"
)

print("Gestion de portafolio v0.1")
while True:
  print("Escoge una opcion")
  print("1.-Insertar")
  print("2.-Listar")
  print("3.-Actualizar")
  print("4.-Eliminar")
  opcion = int(input("Escoge una opcion: "))
  print("La opción que has escogido es: ",opcion)
  if opcion == 1:
    pass
  elif opcion == 2:
    cursor = conexion.cursor() 
    cursor.execute("SELECT * FROM piezas;")
    lineas = cursor.fetchall()
    for linea in lineas:
      print(linea)
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### desarrollo insertar
<small>Creado: 2025-11-03 15:31</small>

#### Explicación

Este código es una pequeña aplicación en Python que se conecta a una base de datos MySQL para gestionar un portafolio. La aplicación permite al usuario interactuar con la base de datos realizando diferentes acciones: insertar, listar, actualizar y eliminar registros.

Al iniciar el programa, establece una conexión a la base de datos usando las credenciales proporcionadas (host local, usuario "portafolio", contraseña "portafolio" y la base de datos llamada "portafolio"). Luego crea un bucle infinito que muestra al usuario un menú con cuatro opciones. Dependiendo del número que elija el usuario, realiza una acción diferente:

- Si se selecciona la opción 1 (Insertar), solicita al usuario que introduzca detalles de una nueva pieza (título, descripción, fecha y nombre de imagen). Luego inserta estos datos en la tabla "piezas" de la base de datos.
  
- Para la opción 2 (Listar), consulta todos los registros existentes en la tabla "piezas" y muestra cada uno por pantalla.

- Las opciones 3 (Actualizar) y 4 (Eliminar) están presentes pero no tienen implementación aún, ya que el código utiliza la palabra clave `pass` para esas partes, lo cual indica que esa sección del código debe ser desarrollada en un futuro cercano.

Esta estructura de código es importante porque permite al usuario interactuar fácilmente con los datos almacenados en una base de datos y ofrece un buen ejemplo práctico sobre cómo manejar conexiones a bases de datos MySQL desde Python.

`006-desarrollo insertar.py`

```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolio",
  password="portafolio",
  database="portafolio"
)
cursor = conexion.cursor() 

print("Gestion de portafolio v0.1")
while True:
  print("Escoge una opcion")
  print("1.-Insertar")
  print("2.-Listar")
  print("3.-Actualizar")
  print("4.-Eliminar")
  opcion = int(input("Escoge una opcion: "))
  print("La opción que has escogido es: ",opcion)
  if opcion == 1:
    titulo = input("Introduce el titulo de la nueva pieza")
    descripcion = input("Introduce la descripcion de la nueva pieza")
    fecha = input("Introduce la fecha de la nueva pieza")
    imagen = input("Introduce el nombre de la imagen de la nueva pieza")
    cursor.execute("INSERT INTO piezas VALUES (NULL,'"+titulo+"','"+descripcion+"','"+fecha+"',1,'"+imagen+"');")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM piezas;")
    lineas = cursor.fetchall()
    for linea in lineas:
      print(linea)
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### desarrollamos eliminacion
<small>Creado: 2025-11-03 15:33</small>

#### Explicación

Este fragmento de código es una pequeña aplicación en Python que interactúa con una base de datos MySQL para gestionar un portafolio de obras o piezas. La aplicación permite al usuario realizar varias operaciones sobre la tabla `piezas` en la base de datos, como insertar nuevas entradas, listar todas las entradas existentes y eliminar una entrada específica basada en su identificador.

El código comienza por establecer una conexión a la base de datos utilizando el módulo `mysql.connector`. Luego, se crea un bucle infinito que muestra al usuario un menú interactivo para seleccionar qué operación desea realizar. Dependiendo del número que el usuario ingrese, el programa ejecuta diferentes acciones:

- Si el usuario selecciona la opción 1 (insertar), se le pide que introduzca detalles sobre una nueva pieza (título, descripción, fecha y nombre de imagen). Estos datos son luego utilizados para insertar un nuevo registro en la tabla `piezas`.

- Para la opción 2 (listar), el programa consulta todos los registros existentes en la tabla `piezas` e imprime cada uno de ellos.

- La opción 3 (actualizar) y 4 (eliminar) no tienen implementación completa en este fragmento, con solo una línea que indica que es necesario agregar más código para estas funcionalidades (`pass`).

Es importante destacar que este código proporciona un buen ejemplo de cómo interactuar con bases de datos utilizando Python, incluyendo el manejo de transacciones y consultas SQL, aunque también se debe tener cuidado con la seguridad (por ejemplo, evitar inyecciones SQL al usar inputs directos en las consultas).

`007-desarrollamos eliminacion.py`

```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolio",
  password="portafolio",
  database="portafolio"
)
cursor = conexion.cursor() 

print("Gestion de portafolio v0.1")
while True:
  print("Escoge una opcion")
  print("1.-Insertar")
  print("2.-Listar")
  print("3.-Actualizar")
  print("4.-Eliminar")
  opcion = int(input("Escoge una opcion: "))
  print("La opción que has escogido es: ",opcion)
  if opcion == 1:
    titulo = input("Introduce el titulo de la nueva pieza: ")
    descripcion = input("Introduce la descripcion de la nueva pieza: ")
    fecha = input("Introduce la fecha de la nueva pieza: ")
    imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
    cursor.execute("INSERT INTO piezas VALUES (NULL,'"+titulo+"','"+descripcion+"','"+fecha+"',1,'"+imagen+"');")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM piezas;")
    lineas = cursor.fetchall()
    for linea in lineas:
      print(linea)
  elif opcion == 3:
    pass
  elif opcion == 4:
    identificador = input("Introduce el Identificador a eliminar: ")
    cursor.execute("DELETE FROM piezas WHERE Identificador = "+identificador+";")
    conexion.commit()
```

### por ultimo actualizacion
<small>Creado: 2025-11-03 15:37</small>

#### Explicación

Este fragmento de código es un programa en Python que interactúa con una base de datos MySQL para gestionar un portafolio. El programa permite al usuario realizar diferentes acciones como insertar nuevas piezas, listar todas las piezas existentes, actualizar información sobre una pieza específica y eliminar una pieza del portafolio.

El código comienza creando una conexión a la base de datos utilizando el módulo `mysql.connector`. Luego, presenta un menú al usuario que muestra cuatro opciones: Insertar (nueva pieza), Listar (todas las piezas), Actualizar y Eliminar. Dependiendo de la opción seleccionada por el usuario, el programa ejecuta diferentes comandos SQL para interactuar con la base de datos.

Para cada acción, el código solicita al usuario los detalles necesarios, como el título, descripción, fecha y nombre del archivo de imagen si es necesario. Si se elige la opción "Actualizar" o "Insertar", el programa ejecuta una sentencia SQL que inserta nuevos registros en la base de datos o actualiza los existentes. En caso de seleccionar "Eliminar", se elimina un registro específico basado en su identificador.

Este tipo de código es fundamental para aprender cómo interactuar con bases de datos desde Python y entender cómo gestionar información estructurada, lo que es una habilidad clave en el desarrollo web y aplicaciones empresariales.

`008-por ultimo actualizacion.py`

```python
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolio",
  password="portafolio",
  database="portafolio"
)
cursor = conexion.cursor() 

print("Gestion de portafolio v0.1")
while True:
  print("Escoge una opcion")
  print("1.-Insertar")
  print("2.-Listar")
  print("3.-Actualizar")
  print("4.-Eliminar")
  opcion = int(input("Escoge una opcion: "))
  print("La opción que has escogido es: ",opcion)
  if opcion == 1:
    titulo = input("Introduce el titulo de la nueva pieza: ")
    descripcion = input("Introduce la descripcion de la nueva pieza: ")
    fecha = input("Introduce la fecha de la nueva pieza: ")
    imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
    cursor.execute("INSERT INTO piezas VALUES (NULL,'"+titulo+"','"+descripcion+"','"+fecha+"',1,'"+imagen+"');")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM piezas;")
    lineas = cursor.fetchall()
    for linea in lineas:
      print(linea)
  elif opcion == 3:
    identificador = input("Introduce el Identificador a actualizar: ")
    titulo = input("Introduce el titulo de la nueva pieza: ")
    descripcion = input("Introduce la descripcion de la nueva pieza: ")
    fecha = input("Introduce la fecha de la nueva pieza: ")
    imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
    cursor.execute('''
      UPDATE piezas 
      SET
      titulo = "'''+titulo+'''",
      descripcion = "'''+descripcion+'''",
      fecha = "'''+fecha+'''",
      imagen = "'''+imagen+'''"
      WHERE Identificador = '''+identificador+'''
    ''')
    conexion.commit()
  elif opcion == 4:
    identificador = input("Introduce el Identificador a eliminar: ")
    cursor.execute("DELETE FROM piezas WHERE Identificador = "+identificador+";")
    conexion.commit()
```

### Actividades propuestas

### Actividades para Estudiantes de Formación Profesional

1. **Bienvenida y Menú CRUD**
   - Desarrolla un programa que imprima un mensaje de bienvenida y luego muestre un menú CRUD con las opciones Insertar, Listar, Actualizar y Eliminar.
   - Se pretende que los estudiantes aprendan a estructurar la interacción inicial del usuario en Python.

2. **Conexión a Base de Datos**
   - Crea una función `conectar_db()` que establezca una conexión con una base de datos MySQL local usando las credenciales proporcionadas.
   - El objetivo es familiarizar a los estudiantes con el uso de la librería `mysql.connector` y cómo gestionar conexiones.

3. **Interacción del Menú**
   - Modifica un programa existente para que, después de imprimir un menú CRUD, capture la opción seleccionada por el usuario.
   - Se espera que los alumnos comprendan el manejo básico de entradas de texto en Python y su integración con estructuras condicionales.

4. **Consulta Básica**
   - Realiza una consulta SQL simple a la tabla `piezas` para listar todos sus registros e imprime estos resultados.
   - La actividad busca que los estudiantes entiendan cómo realizar consultas básicas utilizando Python y MySQL.

5. **Menú CRUD con Ciclo Infinito**
   - Implementa un menú CRUD dentro de un ciclo infinito `while True` que permita al usuario interactuar indefinidamente hasta que decida salir.
   - Se pretende enseñar a los estudiantes cómo manejar bucles infinitos y el flujo condicional en programas interactivos.

6. **Ejecución de Opciones CRUD**
   - Amplía la actividad anterior para incluir funciones separadas para cada opción CRUD (Insertar, Listar, Actualizar, Eliminar).
   - La finalidad es que los estudiantes aprendan a organizar el código en funciónes y a gestionar diferentes casos de uso dentro del menú.

7. **Inserción de Datos**
   - Realiza la opción Insertar del menú CRUD, permitiendo al usuario ingresar datos nuevos para añadir una nueva pieza a la base de datos.
   - Se espera que los estudiantes comprendan cómo realizar inserciones en una base de datos MySQL desde Python.

8. **Eliminación de Datos**
   - Implementa la opción Eliminar del menú CRUD, permitiendo al usuario eliminar registros existentes basados en su identificador.
   - La actividad busca que los estudiantes se familiaricen con las sentencias SQL DELETE y cómo manejar solicitudes de eliminación.

9. **Actualización de Datos**
   - Desarrolla la opción Actualizar del menú CRUD, permitiendo al usuario modificar registros existentes basándose en su identificador.
   - Se pretende que los estudiantes aprendan a realizar actualizaciones en una base de datos MySQL desde Python utilizando sentencias SQL UPDATE.

10. **Prueba Integral**
    - Combinando todas las opciones CRUD y funciones previas, crea un programa integral que permita al usuario interactuar con la base de datos a través del menú implementado.
    - La actividad final busca consolidar el aprendizaje y aplicarlo en una solución completa e integrada.


<a id="ejercicio-de-final-de-unidad-3"></a>
## Ejercicio de final de unidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/101-Ejercicio%20de%20final%20de%20unidad)

### Introducción a los ejercicios

El conjunto de ejercicios en esta carperta está diseñado para reforzar tus habilidades en la lectura y escritura de información en archivos utilizando el lenguaje de programación. Aunque solo hay un archivo de ejercicio, este cubre varios aspectos esenciales como manejo de ficheros, estructuras de control y bucles, además de funciones básicas para leer desde y escribir en archivos. Este tipo de práctica te ayudará a comprender mejor cómo interactuar con el sistema de archivos en entornos de programación, preparándote para proyectos más complejos que requieren almacenamiento persistente de datos.

### Actividades propuestas

### Actividad 1: Análisis de un Ejercicio Complejo

**Descripción:** Los estudiantes deben analizar el ejercicio proporcionado para comprender cómo se realiza la lectura y escritura de información en archivos. Esta actividad permitirá a los alumnos identificar las estructuras de código utilizadas y entender su propósito.

### Actividad 2: Mejora del Código Existente

**Descripción:** Basándose en el análisis previo, los estudiantes deben proponer mejoras al código original para optimizar o añadir nuevas funcionalidades. Se espera que mejoren la legibilidad y eficiencia del mismo.

### Actividad 3: Creación de Ejercicios Similares

**Descripción:** Los alumnos crearán un ejercicio similar al proporcionado, pero con diferencias en los detalles específicos (por ejemplo, cambiar el tipo de archivo o añadir condiciones adicionales). Esto ayudará a consolidar sus conocimientos sobre la manipulación de archivos.

### Actividad 4: Documentación del Código

**Descripción:** Los estudiantes tendrán que escribir documentación detallada para el código proporcionado. Se espera que incluyan comentarios y explicaciones sobre cada sección y funcionalidad del programa.

### Actividad 5: Resolución de Problemas de Estructura

**Descripción:** Se presentarán a los alumnos con problemas comunes relacionados con la estructura del código para trabajar en la resolución de estos problemas. Esto mejorará su capacidad para detectar y corregir errores en el código.

### Actividad 6: Aprendizaje Autónomo sobre Nuevas Funciones

**Descripción:** Los estudiantes investigarán y aprenderán nuevas funciones relacionadas con la manipulación de archivos no cubiertas en el ejercicio original. Se les pedirá que incorporen estas nuevas funcionalidades al código existente.

### Actividad 7: Desarrollo Colaborativo de un Ejercicio Mejorado

**Descripción:** Trabajando en equipo, los estudiantes desarrollarán una versión mejorada del ejercicio proporcionado incluyendo sugerencias de mejora y nuevas características. Esto promoverá la colaboración y el trabajo en equipo.

### Actividad 8: Presentaciones de Casos de Uso

**Descripción:** Cada grupo presentará un caso de uso real donde se aplicaría una versión mejorada del ejercicio proporcionado. Se espera que discutan cómo esta aplicación mejora la eficacia o la funcionalidad.

Estas actividades están diseñadas para ayudar a los estudiantes a profundizar en el tema de lectura y escritura de información, así como para desarrollar habilidades de análisis, diseño y trabajo colaborativo.


<a id="examen-final"></a>
## Examen final

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/104-Examen%20final)

### Introducción a los ejercicios

Esta carpeta contiene una serie de ejercicios orientados a familiarizarte con el manejo básico y avanzado en SQL, específicamente enfocándose en la creación y gestión de bases de datos. Los problemas abordan desde la creación de tablas hasta la inserción de datos, establecimiento de relaciones entre tablas mediante claves foráneas, consultas JOIN para combinar información de múltiples tablas, y finalmente, la creación de vistas personalizadas que simplifican el acceso a datos relacionados. Asimismo, se incluye un ejercicio dedicado a la administración de usuarios y privilegios en MySQL, lo cual es crucial para garantizar la seguridad y control del acceso a las bases de datos.

### crear tablas
<small>Creado: 2025-11-13 15:47</small>

#### Explicación

Este fragmento de código SQL está diseñado para crear una base de datos y dos tablas relacionadas en un sistema de gestión de bases de datos relacional (como MySQL o PostgreSQL). En primer lugar, se crea la base de datos llamada `portafolioceac`. Luego, mediante el comando `USE`, se selecciona esta base de datos recién creada como la base de trabajo actual.

Después de esto, se definen dos tablas: `Piezas` y `Categorias`. La tabla `Piezas` contiene información sobre distintas piezas o elementos del portafolio, incluyendo un identificador único (autoincremental), título, descripción, imagen y URL. Además, tiene una columna `id_categoria`, que es una referencia a la tabla `Categorias`.

La tabla `Categorias`, por su parte, almacena información sobre las diferentes categorías a las que pueden pertenecer las piezas. Cada categoría también tiene un identificador único (autoincremental), un título y una descripción.

Esta estructura de tablas permite organizar la información de manera clara y relacionar piezas con sus respectivas categorías, lo cual es crucial para sistemas de gestión de portafolios o proyectos donde se necesita clasificar elementos según diferentes criterios.

`001-crear tablas.sql`

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
<small>Creado: 2025-11-13 15:47</small>

#### Explicación

Este fragmento de código SQL está insertando datos en dos tablas diferentes llamadas `Categorias` y `Piezas`. En la tabla `Categorias`, se agrega una nueva fila con un ID automático (especificado como `NULL`), el nombre 'General' y una descripción que dice 'Esta es la categoria general'. Esto significa que estás creando una categoría principal en tu base de datos.

En la tabla `Piezas`, también se inserta una nueva fila. El ID de esta pieza será automático (también especificado como `NULL`). Luego, agrega el nombre 'Primera pieza', seguido por una descripción que dice 'Esta es la descripcion de la primera pieza'. Además, incluye un archivo adjunto llamado 'josevicente.jpg' y una URL 'https://jocarsa.com'. Finalmente, se especifica que esta pieza pertenece a la categoría con ID 1, estableciendo así la relación entre la tabla `Piezas` y `Categorias`.

Este código es importante porque inicializa tu base de datos con algunos datos básicos para que puedas probar otras funciones o consultas más adelante en tus ejercicios.

`002-insertar.sql`

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
<small>Creado: 2025-11-13 15:47</small>

#### Explicación

Este fragmento de código SQL está configurando una relación entre dos tablas en una base de datos: la tabla `Piezas` y la tabla `Categorias`. Específicamente, se está creando una restricción llamada "fk_piezas_categorias" que asegura que cada pieza tiene una categoría asociada a través del campo `id_categoria`.

Lo que hace el código es añadir un tipo especial de restricción llamada clave foránea (FOREIGN KEY) en la tabla `Piezas`. Esta clave foránea se vincula con el campo `identificador` en la tabla `Categorias`. Esto significa que cada valor en el campo `id_categoria` de la tabla `Piezas` debe existir también como un valor en el campo `identificador` de la tabla `Categorias`.

Las opciones `ON DELETE CASCADE` y `ON UPDATE CASCADE` indican cómo deben comportarse las tablas cuando se modifican los datos. En este caso, si se elimina una categoría (por ejemplo, porque ya no es relevante), todas las piezas que dependen de esa categoría también serán eliminadas automáticamente. Lo mismo ocurre con actualizaciones: si el identificador de una categoría cambia, el valor en `id_categoria` para cada pieza relacionada cambiará también.

Esta configuración asegura la integridad referencial entre las tablas, manteniendo los datos consistentes y evitando problemas como registros huérfanos o discrepancias entre categorías y piezas.

`003-fk.sql`

```sql
ALTER TABLE Piezas
ADD CONSTRAINT fk_piezas_categorias
FOREIGN KEY (id_categoria) REFERENCES Categorias(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

### selecciones
<small>Creado: 2025-11-13 15:47</small>

#### Explicación

Este código SQL consta de dos consultas simples que se utilizan para recuperar información de una base de datos. La primera consulta, `SELECT * FROM Categorias;`, selecciona todos los campos y filas de la tabla llamada "Categorias". Esto significa que obtendrás toda la información almacenada en esa tabla.

La segunda consulta, `SELECT * FROM Piezas;`, hace exactamente lo mismo pero para una tabla diferente llamada "Piezas". Ambas consultas son muy útiles cuando necesitas ver el contenido completo de las tablas sin especificar columnas individuales, ya que pueden ayudarte a verificar rápidamente los datos almacenados en tu base de datos durante la fase de desarrollo o pruebas.

`004-selecciones.sql`

```sql
SELECT * FROM Categorias;

SELECT * FROM Piezas;
```

### left join
<small>Creado: 2025-11-13 15:47</small>

#### Explicación

Este fragmento de código SQL realiza una operación llamada `LEFT JOIN` entre dos tablas: `Piezas` y `Categorias`. El objetivo es combinar los datos de ambas tablas basándose en la relación existente entre ellas, que se establece a través del campo `id_categoria` de la tabla `Piezas` y el campo `Identificador` de la tabla `Categorías`.

El comando `SELECT *` indica que se deben recuperar todas las columnas resultantes de esta combinación. Esto significa que para cada pieza en la tabla `Piezas`, el código buscará su correspondiente categoría en la tabla `Categorias`. Si una pieza no tiene una categoría asociada (es decir, si no existe un valor en `id_categoria`), entonces los campos de la categoría serán `NULL`.

Esta consulta es importante porque permite tener una visión completa y detallada de cómo se relacionan las piezas con sus respectivas categorías, incluso cuando algunas piezas pueden no estar asociadas a ninguna categoría. Esto facilita el análisis y la gestión de datos en aplicaciones que requieren entender la estructura jerárquica o la clasificación de elementos como piezas en un sistema de inventario o similar.

`005-left join.sql`

```sql
SELECT 
* 
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;
```

### ahora creo la vista
<small>Creado: 2025-11-13 15:47</small>

#### Explicación

Este fragmento de código SQL está compuesto por dos partes. La primera parte crea una vista llamada `piezas_y_categorias`. Una vista en SQL es como un alias para una consulta, que permite simplificar consultas complejas y hacerlas más reutilizables.

En la creación de esta vista, se realiza una consulta que selecciona información desde las tablas `Categorias` y `Piezas`, utilizando una operación `LEFT JOIN`. Esto significa que todas las piezas (registros en la tabla `Piezas`) son incluidas en el resultado, junto con sus correspondientes categorías si existen. Si una pieza no tiene categoría asignada, los campos de la categoría serán nulos.

La segunda parte del código es simplemente un `SELECT * FROM piezas_y_categorias;`, lo que significa que se está solicitando mostrar todos los datos almacenados en esta nueva vista recién creada. Esto permitirá ver fácilmente cómo quedaron combinadas las dos tablas originales (`Categorias` y `Piezas`) en la vista `piezas_y_categorias`.

`006-ahora creo la vista.sql`

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
<small>Creado: 2025-11-13 15:47</small>

#### Explicación

Este fragmento de código SQL se utiliza para crear un nuevo usuario en una base de datos MySQL y otorgarle permisos específicos. En primer lugar, crea un nuevo usuario llamado 'portafolioceac' con la contraseña 'portafolioceac'. Luego, le permite al usuario acceder a cualquier recurso en el servidor local mediante el comando `GRANT USAGE`. Después, elimina los límites por defecto que tiene este usuario para permitirle realizar una mayor cantidad de consultas y conexiones sin restricciones. Finalmente, otorga al usuario todos los privilegios sobre la base de datos 'portafolioceac' y actualiza la tabla de privilegios del sistema con el comando `FLUSH PRIVILEGES`. Este proceso es crucial para gestionar usuarios y asegurar que cada uno tenga acceso adecuado a los recursos necesarios en un entorno de desarrollo o producción.

`007-usuario.sql`

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

### Actividades propuestas

### Actividad 1: Creación y diseño básico de una base de datos
**Descripción:** Crea una nueva base de datos llamada `mi_portafolio`. Luego, diseña dos tablas relacionadas con categorías y piezas. Este ejercicio permitirá a los alumnos entender cómo estructurar bases de datos y trabajar con relaciones entre entidades.

### Actividad 2: Inserción de registros en la base de datos
**Descripción:** Inserta nuevos registros en las tablas creadas en la actividad anterior, incluyendo al menos una categoría y una pieza asociada. Los estudiantes aprenderán cómo utilizar el comando `INSERT INTO` para añadir información a sus tablas.

### Actividad 3: Creación de restricciones de clave foránea
**Descripción:** Añade una restricción de clave foránea (foreign key) entre las tablas creadas en la actividad anterior. Los alumnos aprenderán cómo establecer relaciones entre entidades y asegurar la integridad referencial.

### Actividad 4: Consulta básica de datos
**Descripción:** Escribe consultas `SELECT` para recuperar todos los registros tanto de la tabla de categorías como de piezas. Este ejercicio permitirá a los estudiantes comprender cómo seleccionar datos desde una base de datos MySQL.

### Actividad 5: Unión entre tablas (JOIN)
**Descripción:** Realiza un `LEFT JOIN` entre las tablas de categorías y piezas para recuperar información completa sobre todas las piezas y sus respectivas categorías. Los estudiantes aprenderán cómo combinar datos desde múltiples tablas en una consulta.

### Actividad 6: Creación de vistas
**Descripción:** Crea una vista que combine los campos relevantes de tus tablas para proporcionar un resumen de información sobre las piezas y sus categorías. Este ejercicio enseñará a los alumnos cómo simplificar consultas complejas mediante la creación de vistas.

### Actividad 7: Uso de alias en consultas
**Descripción:** Escribe una consulta que utilice alias para mejorar la legibilidad de los resultados de tu vista creada anteriormente. Los estudiantes aprenderán cómo manejar y organizar los datos recuperados a través del uso de alias.

### Actividad 8: Creación y configuración de usuarios en MySQL
**Descripción:** Crea un nuevo usuario llamado `mi_usuario` y configúralo para que tenga acceso completo a tu base de datos recién creada. Los alumnos aprenderán cómo gestionar usuarios y privilegios en bases de datos MySQL.

### Actividad 9: Pruebas de integridad referencial
**Descripción:** Realiza pruebas modificando registros o eliminándolos, verificando que las restricciones de clave foránea funcionen correctamente. Este ejercicio permitirá a los estudiantes comprender la importancia y el funcionamiento de las restricciones de integridad referencial.

### Actividad 10: Documentación de consultas SQL
**Descripción:** Crea una documentación para todas tus consultas y comandos realizados, incluyendo explicaciones sobre cómo cada uno funciona. Este ejercicio ayudará a los estudiantes a desarrollar habilidades en la documentación técnica y el pensamiento lógico.


<a id="carpeta-sin-titulo"></a>
## Carpeta sin título

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/005-Lectura%20y%20escritura%20de%20informaci%C3%B3n/Carpeta%20sin%20ti%CC%81tulo)



<a id="aplicacion-de-las-estructuras-de-almacenamiento"></a>
# Aplicación de las estructuras de almacenamiento

<a id="estructuras-estaticas-y-dinamicas"></a>
## Estructuras estáticas y dinámicas

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/006-Aplicaci%C3%B3n%20de%20las%20estructuras%20de%20almacenamiento/001-Estructuras%20est%C3%A1ticas%20y%20din%C3%A1micas)

### Introducción a los ejercicios

En esta carpeta de ejercicios se exploran diferentes estructuras de datos estáticas y dinámicas en Python, específicamente listas y tuplas. Los estudiantes aprenderán a manipular estos tipos de datos mediante la adición y eliminación de elementos, lo cual es fundamental para el manejo eficiente de información en programas más complejos. Se enfatiza especialmente cómo las listas permiten cambios dinámicos mientras que las tuplas son inmutables, proporcionando una base sólida sobre los conceptos clave de estructuras de datos en programación.

### estructura dinamica lista
<small>Creado: 2025-11-20 14:53</small>

#### Explicación

Este código es una simple demostración de cómo trabajar con listas en Python. Una lista es como una caja donde puedes guardar varios elementos, en este caso nombres de personas. Al principio, la lista llamada `agenda` contiene los nombres "Jaime", "Jorge" y "Juan". Cuando ejecutas el código, primero imprimes esta lista para que puedas ver cuáles son los nombres que están guardados inicialmente.

Luego, se añade un nuevo nombre, "Julia", a la lista utilizando el método `append()`. Este método es muy útil porque permite agregar elementos al final de una lista sin necesidad de especificar la posición exacta. Al final del código, imprimes nuevamente la lista para mostrar cómo ha cambiado después de añadir "Julia".

Este ejemplo demuestra cómo las listas en Python son estructuras dinámicas que pueden cambiar su tamaño fácilmente durante la ejecución del programa, lo cual es muy práctico cuando necesitas gestionar colecciones de datos que pueden variar.

`001-estructura dinamica lista.py`

```python
agenda = [
  "Jaime",
  "Jorge",
  "Juan"
]

print(agenda)

agenda.append("Julia") # Le añado un elemento

print(agenda)
```

### eliminar elementos
<small>Creado: 2025-11-20 14:54</small>

#### Explicación

Este código muestra cómo trabajar con una lista en Python, que es una estructura de datos dinámica. En primer lugar, se crea una lista llamada `agenda` que contiene los nombres "Jaime", "Jorge" y "Juan". Luego, imprime esta lista para mostrarte su contenido inicial.

Después, el código añade un nuevo elemento al final de la lista con la función `append()`. En este caso, se agrega el nombre "Julia". De nuevo, se imprime la lista después de agregar el nuevo elemento para que puedas ver cómo ha cambiado.

Finalmente, se utiliza la función `pop()` para eliminar el último elemento de la lista. Esto es útil cuando sabes que quieres quitar siempre el último elemento. Después de esto, vuelve a imprimirse la lista para mostrar los cambios realizados.

Este tipo de operaciones (añadir y eliminar elementos) son comunes en programación y te ayudan a entender cómo manejar listas dinámicas en Python, lo cual es fundamental cuando trabajas con datos que cambian durante la ejecución del programa.

`002-eliminar elementos.py`

```python
agenda = [
  "Jaime",
  "Jorge",
  "Juan"
]

print(agenda)

agenda.append("Julia") # Le añado un elemento

print(agenda)

agenda.pop() # Elimino un elemento del final

print(agenda)
```

### eliminar un elemento de donde quiera
<small>Creado: 2025-11-20 14:54</small>

#### Explicación

Este código muestra cómo trabajar con listas en Python, que son una estructura de datos dinámica. La lista `agenda` se inicializa con tres nombres: "Jaime", "Jorge" y "Juan". Primero, el programa imprime la lista completa para mostrar su contenido original.

Luego, se añade el nombre "Julia" al final de la lista usando el método `append()`. Este método agrega un elemento a la lista en la posición más reciente (final) y luego vuelve a imprimir la lista para demostrar que "Julia" ha sido agregada correctamente.

A continuación, se elimina el último nombre de la lista con el método `pop()` sin ningún argumento. Esto quita el último elemento de la lista, en este caso, "Julia", y la imprime nuevamente para mostrar los cambios.

Finalmente, se utiliza el método `pop(1)` para eliminar un elemento específico de una posición determinada (en este caso, la segunda entrada en la lista, que es "Jorge" dado que las listas empiezan a contar desde cero). Este paso demuestra cómo puedes especificar exactamente qué elemento deseas remover de tu lista.

Este código es importante porque te enseña cómo manejar datos dinámicos en Python, permitiéndote añadir y quitar elementos según sea necesario. Esto es fundamental cuando trabajas con estructuras de datos como listas para manipular información en tus programas.

`003-eliminar un elemento de donde quiera.py`

```python
agenda = [
  "Jaime",
  "Jorge",
  "Juan"
]

print(agenda)

agenda.append("Julia") # Le añado un elemento

print(agenda)

agenda.pop() # Elimino un elemento del final

print(agenda)

agenda.pop(1)

print(agenda)
```

### tuplas
<small>Creado: 2025-11-20 14:55</small>

#### Explicación

Este código Python crea una tupla llamada `coordenadas` que contiene tres números enteros: 1, 2 y 3. Una tupla es similar a una lista en Python, pero con la diferencia de que las tuplas son inmutables, lo que significa que no puedes cambiar sus elementos después de crearlas.

El código luego imprime el contenido de `coordenadas` utilizando la función `print()`. Al ejecutar este programa, se mostrará `(1, 2, 3)` en la pantalla. Este ejemplo es útil para entender cómo se crean y visualizan tuplas en Python, lo que es importante cuando trabajas con datos que no necesitan ser modificados después de su inicialización.

`004-tuplas.py`

```python
coordenadas = (1,2,3)

print(coordenadas)
```

### intento añadir elemento
<small>Creado: 2025-11-20 14:56</small>

#### Explicación

Este código Python muestra un ejemplo de cómo tratar con tuplas. Una tupla es una estructura de datos que se utiliza para almacenar varios elementos inmutables, lo que significa que una vez que has creado la tupla, no puedes cambiar sus elementos. 

El código comienza creando una tupla llamada `coordenadas` con tres números: `(1, 2, 3)`. Luego, imprime esta tupla para mostrar su contenido en la consola.

A continuación, hay un intento de añadir el número `5` a la tupla usando el método `append()`, que es comúnmente usado para listas. Sin embargo, este método no está disponible para las tuplas porque ellas son inmutables y no se pueden modificar una vez creadas.

Al final, el código vuelve a intentar imprimir la variable `coordenadas` después del fallo en la modificación. Esto mostrará de nuevo los valores originales `(1, 2, 3)`, sin cambios.

Este fragmento es importante para entender la diferencia entre las tuplas y las listas en Python y aprender por qué es crucial respetar las propiedades inmutables de las tuplas.

`005-intento añadir elemento.py`

```python
coordenadas = (1,2,3)

print(coordenadas)

coordenadas.append(5)

print(coordenadas)
```

### Actividades propuestas

### Actividades Propuestas

#### 1. **Añadiendo Contactos a una Agenda**
**Descripción:** Los alumnos deben crear un programa que permita añadir varios contactos (nombres) a una lista y luego mostrar la lista completa con los nuevos elementos añadidos. Se espera que aprendan cómo manejar listas en Python y entender el método `append()`.

#### 2. **Manipulación de Listas: Añadir y Eliminar**
**Descripción:** Los estudiantes tendrán que crear una aplicación básica donde pueden agregar un contacto a la lista y luego eliminarlo. Este ejercicio ayudará a los alumnos a comprender cómo se manejan las operaciones básicas en listas.

#### 3. **Manipulación de Listas: Añadir y Eliminar Elemento Específico**
**Descripción:** Se les pedirá que diseñen un programa que pueda añadir un elemento al final de una lista, eliminar el último elemento y luego eliminar un elemento específico por su índice (no por posición). Esto permitirá a los estudiantes profundizar en la lógica detrás del manejo de listas dinámicas.

#### 4. **Comparación entre Listas Dinámicas y Estructuras Estáticas**
**Descripción:** Los alumnos deben crear una aplicación que muestre las diferencias entre usar una lista (estructura dinámica) y una tupla (estructura estática), mostrando los problemas que pueden surgir al intentar modificar una tupla.

#### 5. **Manejo de Errores: Añadir Elemento a Tupla**
**Descripción:** Los estudiantes deben escribir un programa que intente añadir un elemento a una tupla, lo cual generará un error en tiempo de ejecución. La tarea es detectar y corregir el problema para comprender por qué las tuplas son inmutables.

#### 6. **Implementación de Agenda Personal**
**Descripción:** Se les pide que creen su propia agenda personal usando listas. Deben ser capaces de añadir, eliminar y mostrar contactos en la lista, así como manejar posibles errores (como intentar acceder a índices inexistentes).

#### 7. **Estructura Dinámica vs Estática**
**Descripción:** Los alumnos deben crear un código que ilustre las diferencias entre una estructura dinámica y estática en Python, usando ejemplos con listas y tuplas.

#### 8. **Desarrollo de Aplicación Compleja: Agenda Mejorada**
**Descripción:** Se les propone desarrollar una aplicación más avanzada que permita gestionar una agenda completa. Esto incluirá la capacidad para añadir, eliminar y buscar contactos en la lista, así como manejar errores y excepciones correctamente.

Estas actividades están diseñadas para ayudar a los estudiantes de Formación Profesional a comprender mejor las estructuras estáticas y dinámicas en Python, específicamente listas y tuplas.


<a id="creacion-de-matrices-arrays"></a>
## Creación de matrices (arrays)

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/006-Aplicaci%C3%B3n%20de%20las%20estructuras%20de%20almacenamiento/002-Creaci%C3%B3n%20de%20matrices%20%28arrays%29)

### Introducción a los ejercicios

En esta carpeta de ejercicios, se exploran las bases del manejo de estructuras de datos en programación, centrándose específicamente en el uso de matrices (arrays) y objetos. Los estudiantes aprenderán a crear arrays, agregar y eliminar elementos, así como recorrer tanto arrays como propiedades de objetos para mostrar o manipular sus datos. Estos ejercicios son fundamentales para comprender cómo organizar y procesar colecciones de información en diferentes lenguajes de programación como Python y JavaScript, lo que desarrollará habilidades clave para la gestión eficiente de datos en aplicaciones informáticas.

### arrays
<small>Creado: 2025-11-20 14:58</small>

#### Explicación

Este código HTML incluye un bloque de script que define una matriz llamada `agenda` y luego muestra esta matriz en la consola del navegador. La matriz `agenda` contiene tres elementos: los nombres "Juan", "Jorge" y "Julia". Al utilizar `console.log(agenda);`, el programa imprime la matriz completa en la consola, lo que nos permite ver cómo se estructuran las matrices en JavaScript.

Este ejemplo es importante porque muestra cómo crear una matriz simple en JavaScript y cómo visualizar su contenido utilizando la función `console.log()`. Esto es útil tanto para depurar código como para aprender a manejar datos en forma de lista.

`001-arrays.html`

```html
<script>
  var agenda = [
    "Juan",
    "Jorge",
    "Julia"
  ];
  console.log(agenda);
</script>
```

### empujar un elemento en un array
<small>Creado: 2025-11-20 14:59</small>

#### Explicación

Este fragmento de código es un ejemplo sencillo que muestra cómo trabajar con arrays en JavaScript. Primero, se crea una lista (array) llamada `agenda` que contiene los nombres de tres personas: "Juan", "Jorge" y "Julia". Luego, el contenido del array `agenda` se imprime en la consola para mostrar sus elementos iniciales.

Después, se utiliza un método llamado `.push()` para añadir un nuevo elemento al final del array. En este caso, se agrega el nombre "Jaime" a la lista de contactos. Finalmente, se vuelve a imprimir el contenido actualizado del array `agenda` en la consola.

Este código es importante porque demuestra cómo puedes expandir dinámicamente un array en JavaScript agregando nuevos elementos cuando sea necesario, lo cual es una operación común en muchos tipos de aplicaciones que manejan listas de datos.

`002-empujar un elemento en un array.html`

```html
<script>
  var agenda = [
    "Juan",
    "Jorge",
    "Julia"
  ];
  console.log(agenda);
  agenda.push("Jaime");
  console.log(agenda);
</script>
```

### quitar un elemento del array
<small>Creado: 2025-11-20 15:00</small>

#### Explicación

Este código HTML contiene un bloque de script que muestra cómo trabajar con arrays en JavaScript. Primero, se crea un array llamado `agenda` que almacena los nombres "Juan", "Jorge" y "Julia". Luego, este array es mostrado en la consola del navegador usando `console.log()`. A continuación, se añade el nombre "Jaime" al final del array utilizando el método `.push()` y vuelve a mostrar el contenido actualizado de `agenda` en la consola. Finalmente, se elimina el último elemento del array con el método `.splice(3)`, que comienza a eliminar elementos desde el índice 3 hasta el final (en este caso, solo elimina "Jaime"). De nuevo, muestra el estado actual del array en la consola.

Este ejemplo es importante para entender cómo manipular arrays dinámicamente añadiendo y removiendo elementos según sea necesario.

`003-quitar un elemento del array.html`

```html
<script>
  var agenda = [
    "Juan",
    "Jorge",
    "Julia"
  ];
  console.log(agenda);
  agenda.push("Jaime");
  console.log(agenda);
  agenda.splice(3)
  console.log(agenda);
</script>
```

### recorrer lista en python
<small>Creado: 2025-11-20 15:01</small>

#### Explicación

Este código Python muestra cómo recorrer una lista (también llamada array) y procesar cada uno de sus elementos. La lista se llama `personas` y contiene cuatro nombres: Jaime, Julia, Jorge y Juan. El bucle `for` itera sobre cada elemento en la lista `personas`, asignando el valor actual a la variable `persona`. En cada iteración del bucle, el código imprime el nombre de la persona que se está procesando con la función `print()`. Esto es importante porque nos permite realizar operaciones con cada elemento de una lista sin tener que escribir un comando para cada uno individualmente.

`004-recorrer lista en python.py`

```python
personas = [
  "Jaime",
  "Julia",
  "Jorge",
  "Juan"
]

for persona in personas:
  print(persona)
  
```

### recorrer array en Javascript
<small>Creado: 2025-11-20 15:02</small>

#### Explicación

Este código HTML contiene un bloque de script que define una matriz llamada `personas` con tres nombres: "Juan", "Jorge" y "Julia". Luego, utiliza el método `forEach()` para recorrer cada elemento en la matriz. Dentro del bucle, se imprime cada nombre en el navegador utilizando `console.log()`. Esto es útil porque muestra cómo iterar sobre una lista de elementos (en este caso, nombres) y realizar operaciones con cada uno, como imprimirlo en la consola. Es importante para entender cómo trabajar con colecciones de datos en JavaScript.

`005-recorrer array en Javascript.html`

```html
<script>
  var personas = [
    "Juan",
    "Jorge",
    "Julia"
  ];
  personas.forEach(function(persona){
    console.log(persona)
  })
</script>
```

### recorrer propiedades de objeto
<small>Creado: 2025-11-20 15:04</small>

#### Explicación

Este fragmento de código en Python muestra cómo recorrer las propiedades de un objeto (en este caso, llamado `mis_datos`) que es similar a un diccionario. El objetivo del código es imprimir tanto la clave como el valor asociado para cada propiedad del objeto.

Primero, se define un objeto `mis_datos` con tres propiedades: "nombre", "apellidos" y "email". Cada una de estas propiedades tiene un valor asociado, por ejemplo, "Jose Vicente" es el valor de la clave "nombre".

Luego, se utiliza un bucle `for` para iterar sobre todas las claves presentes en el objeto `mis_datos`. Para cada iteración del ciclo, se imprime tanto la clave como el valor correspondiente que se obtiene utilizando la sintaxis `mis_datos[clave]`.

Este tipo de recorrido es importante porque permite acceder y manipular fácilmente los datos almacenados dentro de un objeto complejo en Python, facilitando así operaciones más avanzadas sobre estructuras de datos.

`006-recorrer propiedades de objeto.py`

```python
mis_datos = {
  "nombre":"Jose Vicente",
  "apellidos":"Carratala Sanchis",
  "email":"info@jocarsa.com"
}

for clave in mis_datos:
  print(clave)
  print(mis_datos[clave])
```

### recorrer objeto en javascript
<small>Creado: 2025-11-20 15:06</small>

#### Explicación

Este fragmento de código en JavaScript te enseña cómo recorrer las propiedades y valores de un objeto. En primer lugar, se crea un objeto llamado `mis_datos` que contiene tres propiedades: `"nombre"`, `"apellidos"` y `"email"`. Cada una de estas propiedades tiene un valor asociado.

Luego, se utiliza la función `Object.entries()` para convertir el objeto en un array de pares clave-valor. Por ejemplo, esto convierte `"nombre":"Jose Vicente"` en `["nombre", "Jose Vicente"]`.

Finalmente, se usa el método `forEach` para iterar sobre cada uno de estos pares y mostrarlos en la consola usando `console.log()`. Esto imprime cada clave y su respectivo valor en formato legible, como por ejemplo: `"nombre: Jose Vicente"`.

Esta técnica es útil cuando necesitas procesar o visualizar los datos contenidos en un objeto complejo.

`007-recorrer objeto en javascript.html`

```html
<script>
  var mis_datos = {
    "nombre":"Jose Vicente",
    "apellidos":"Carratala Sanchis",
    "email":"info@jocarsa.com"
  }
  Object.entries(mis_datos).forEach(function([clave, valor]){
    console.log(clave + ": " + valor)
  })
</script>
```

### Actividades propuestas

### Actividad 1: Creación y Modificación de Arrays en JavaScript

**Descripción:** Crea un array vacío llamado `nombres` e implementa una función que permita añadir nombres a este array. Luego, muestra el contenido del array con la ayuda de `console.log()`. Esta actividad te ayudará a familiarizarte con la creación y manipulación básica de arrays en JavaScript.

### Actividad 2: Agregar Elementos al Final del Array

**Descripción:** Dado un array llamado `usuarios`, escribe una función que permita agregar un nuevo usuario al final del array utilizando el método `push()`. Muestra los cambios en el array después de la adición. Esta actividad te enseñará a añadir elementos al final de un array.

### Actividad 3: Remover Elementos de un Array

**Descripción:** Utiliza el método `splice()` para remover un elemento específico del array de usuarios que hayas creado en la actividad anterior. Verifica visualmente los cambios después de la eliminación del elemento. Esta tarea te ayudará a entender cómo eliminar elementos de arrays.

### Actividad 4: Recorrer Arrays con For Loop

**Descripción:** Implementa un bucle `for` para recorrer el array de nombres que hayas creado y muestra cada nombre individualmente utilizando `console.log()`. Este ejercicio te permitirá comprender la iteración básica sobre arrays en JavaScript.

### Actividad 5: Uso del Método `.forEach()` con Arrays

**Descripción:** Escribe un script que utilice la función `forEach` para recorrer el array de usuarios y mostrar cada usuario por consola. Esta actividad te ayudará a entender cómo usar métodos de lista (arrays) en JavaScript.

### Actividad 6: Creación y Modificación de Objetos en Python

**Descripción:** Crea un objeto llamado `persona` que contenga al menos tres propiedades como nombre, edad y ciudad. Luego, muestra cada propiedad del objeto utilizando una estructura de bucle for. Esta actividad te permitirá trabajar con objetos básicos en Python.

### Actividad 7: Recorrer Propiedades de Objetos con For Loop

**Descripción:** Utiliza un bucle `for` para recorrer todas las propiedades del objeto persona que has creado, imprimiendo cada clave y valor por separado. Esta tarea te ayudará a comprender cómo acceder a las propiedades de objetos en Python.

### Actividad 8: Uso de la Función `Object.entries()` con Objetos

**Descripción:** Implementa una función en JavaScript que utilice `Object.entries` para recorrer un objeto similar al creado anteriormente y mostrar cada clave-valor por consola. Esta actividad te enseñará cómo iterar sobre propiedades de objetos usando métodos avanzados.

### Actividad 9: Comparación de Recorrido de Arrays entre JavaScript y Python

**Descripción:** Dado un array en JavaScript, escribe una función que recorra el mismo array utilizando tanto `forEach` como un bucle `for`. Luego, realiza la misma tarea con un objeto similar en Python usando `for` e imprime los resultados. Esta actividad te ayudará a comparar las diferencias y similitudes entre estructuras de datos en ambos lenguajes.

### Actividad 10: Integración de Arrays y Objetos

**Descripción:** Crea un array de objetos donde cada objeto represente la información personal de un usuario (nombre, edad, ciudad). Luego, recorre este array para mostrar toda la información del usuario por consola. Esta actividad te permitirá combinar conceptos de arrays y objetos en ambos lenguajes.


<a id="matrices-arrays-multidimensionales"></a>
## Matrices (arrays) multidimensionales

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/006-Aplicaci%C3%B3n%20de%20las%20estructuras%20de%20almacenamiento/003-Matrices%20%28arrays%29%20multidimensionales)

### Introducción a los ejercicios

En esta sesión de ejercicios, te encontrarás trabajando con matrices multidimensionales en Python, específicamente a través del ejemplo de una agenda. El objetivo principal es comprender cómo almacenar y manipular datos estructurados utilizando listas anidadas. En el ejercicio proporcionado, creas una lista bidimensional para registrar información de contacto como nombres, apellidos y correos electrónicos de varias personas. A través de esta práctica, mejorarás tus habilidades en la creación y manejo de estructuras de datos complejas, así como en la adición de elementos a estas estructuras.

### agenda multidimensional
<small>Creado: 2025-11-20 15:09</small>

#### Explicación

Este código en Python crea una agenda simple utilizando matrices (o arrays) multidimensionales. La variable `agenda` es una lista vacía que servirá para almacenar información sobre diferentes personas, como su nombre completo y su dirección de correo electrónico.

El código agrega varios elementos a la lista `agenda`. Cada elemento es una sublista que contiene tres piezas de información: el primer nombre, el apellido y la dirección de correo electrónico de una persona. Por ejemplo, cuando se ejecuta `agenda.append(["Jose Vicente","Carratala","info@jocarsa.com"])`, este código añade a José Vicente Carratala con su correspondiente email a nuestra lista.

Finalmente, el programa imprime la matriz completa llamada `agenda` en la pantalla. Al imprimir `print(agenda)`, se muestran todos los contactos almacenados en la agenda de forma estructurada, permitiendo ver fácilmente cómo cada persona está organizada dentro de una sublista dentro de la lista principal.

Este tipo de estructura es útil para organizar datos relacionados y acceder a ellos fácilmente, lo cual es fundamental para aplicaciones como agendas o bases de datos simplificadas.

`001-agenda multidimensional.py`

```python
agenda = []

agenda.append(["Jose Vicente","Carratala","info@jocarsa.com"])

agenda.append(["Ana","García","ana.garcia@example.com"]);
agenda.append(["Luis","Martínez","luis.martinez@example.com"]);
agenda.append(["María","López","maria.lopez@example.com"]);
agenda.append(["Carlos","Sánchez","carlos.sanchez@example.com"]);
agenda.append(["Elena","Ruiz","elena.ruiz@example.com"]);
agenda.append(["Javier","Pérez","javier.perez@example.com"]);
agenda.append(["Laura","Gómez","laura.gomez@example.com"]);
agenda.append(["Sergio","Navarro","sergio.navarro@example.com"]);
agenda.append(["Patricia","Ramírez","patricia.ramirez@example.com"]);
agenda.append(["David","Moreno","david.moreno@example.com"]);

print(agenda)
```

### Actividades propuestas

1. **Agenda Mejorada**
   - Descripción: Los estudiantes deben mejorar el código existente para permitir la búsqueda de contactos por nombre y correo electrónico.
   - Objetivo: Aprender a utilizar estructuras condicionales y funciones.

2. **Agregar Contacto**
   - Descripción: Crear una función que permita añadir un nuevo contacto a la agenda sin modificar manualmente el código.
   - Objetivo: Entender cómo manejar datos en matrices multidimensionales dinámicamente.

3. **Borrar Contacto**
   - Descripción: Implementar una funcionalidad para eliminar contactos de la agenda basándose en su nombre completo.
   - Objetivo: Aprender a manipular y modificar estructuras de matriz bidimensional.

4. **Ordenar Agenda**
   - Descripción: Los estudiantes deben ordenar los contactos por el apellido alfabéticamente.
   - Objetivo: Familiarizarse con las operaciones de ordenamiento en listas multidimensionales.

5. **Exportar CSV**
   - Descripción: Escribir una función que permita exportar la agenda completa a un archivo CSV para guardar los datos externamente.
   - Objetivo: Comprender el formato CSV y cómo interactuar con archivos desde Python.

6. **Importar CSV**
   - Descripción: Crear una herramienta que importe contactos desde un archivo CSV al programa de la agenda.
   - Objetivo: Aprender a leer datos desde archivos externos y manipularlos dentro del código.

7. **Validación de Entradas**
   - Descripción: Implementar validaciones para asegurar que solo se ingresen datos correctos en cada campo (nombre, apellido, correo).
   - Objetivo: Mejorar la robustez del programa mediante control de errores y entrada de usuario.

8. **Interfaz Amigable**
   - Descripción: Diseñar un menú simple para interactuar con el programa a través de comandos numéricos.
   - Objetivo: Aprender a estructurar programas para que sean más accesibles e intuitivos para los usuarios.

9. **Consultas Avanzadas**
   - Descripción: Crear una funcionalidad que permita consultar contactos por parte del nombre (sin necesidad de proporcionar el apellido completo).
   - Objetivo: Aprender a manejar consultas más complejas y eficientes en matrices multidimensionales.

10. **Informe Mensual**
    - Descripción: Generar un informe que cuente con estadísticas básicas sobre los contactos (por ejemplo, número de contactos nuevos en el mes).
    - Objetivo: Comprender cómo combinar múltiples operaciones para obtener y presentar datos analíticos.


<a id="genericidad"></a>
## Genericidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/006-Aplicaci%C3%B3n%20de%20las%20estructuras%20de%20almacenamiento/004-Genericidad)

### Introducción a los ejercicios

En esta actividad, se te presenta un ejercicio que involucra la creación de una aplicación web simple usando Flask y MySQL en Python. El objetivo principal es aprender a interactuar con bases de datos utilizando SQL para recuperar datos y luego devolverlos en formato JSON mediante una API. Además, practicarás habilidades como configurar conexiones a bases de datos y renderizar plantillas HTML con Flask.

Este ejercicio refuerza competencias clave como el manejo de estructuras de almacenamiento (en este caso, bases de datos SQL), la generación de APIs web para acceder a esos datos y trabajar con marcos web en Python. Es importante entender cómo se integran diferentes componentes técnicos para crear soluciones completas en desarrollo web.

### servidor
<small>Creado: 2025-11-20 15:12</small>

#### Explicación

Este código es una aplicación web básica creada con Flask y Python que interactúa con una base de datos MySQL. La aplicación tiene dos rutas principales: `/api` y `/`.

1. **Ruta /api**: Cuando un usuario accede a esta ruta, la aplicación consulta la base de datos para obtener información sobre todas las tablas existentes en la base de datos llamada "blog2526". Luego, por cada tabla encontrada, ejecuta una consulta SQL que selecciona todos los registros de esa tabla. Los resultados se almacenan en un diccionario Python donde las claves son los nombres de las tablas y los valores son listas con los datos de dichas tablas. Finalmente, el contenido del diccionario es convertido a formato JSON y devuelto al usuario que ha solicitado la información.

2. **Ruta /**: Cuando un usuario accede a la raíz del sitio web (es decir, la dirección URL sin ninguna ruta adicional), la aplicación busca en la carpeta `templates` un archivo llamado "index.html" y lo renderiza para mostrarlo al usuario.

Esta aplicación es útil cuando se desea proporcionar una interfaz de programadores (API) que devuelve información estructurada sobre el contenido de la base de datos, o simplemente servir páginas web estáticas a los visitantes.

`servidor.py`

```python
import mysql.connector
import json
from flask import Flask,render_template

aplicacion = Flask(__name__)

conexion = mysql.connector.connect(
  host="localhost",
  user="blog2526",
  password="blog2526",
  database="blog2526"
)

cursor = conexion.cursor(dictionary=True) 

@aplicacion.route("/api")
def api():
  cursor.execute("SHOW TABLES;")

  tablas = cursor.fetchall()
  documento = {}
  for tabla in tablas:
    
    # Select * FROM cada una de las tablas
    cursor.execute("SELECT * FROM "+tabla['Tables_in_blog2526']+";")
    registros = cursor.fetchall()
    documento[tabla['Tables_in_blog2526']] = registros

  documento_json = json.dumps(documento, indent=4, ensure_ascii=False)
  return documento_json
  
@aplicacion.route("/")
def raiz():
  return render_template("index.html")
  
if __name__ == "__main__":
  aplicacion.run()
```

### Actividades propuestas

### Actividad 1: Crear una Aplicación Flask Simples

**Descripción:** Implementa una aplicación sencilla en Flask que muestre un mensaje "¡Hola, Mundo!" al abrir la URL raíz. Esta actividad te ayudará a entender los conceptos básicos de Flask y cómo ejecutar aplicaciones web en Python.

### Actividad 2: Conexión a MySQL con Python

**Descripción:** Establece una conexión entre tu aplicación Flask y una base de datos MySQL local. Asegúrate de que la configuración de usuario, contraseña y nombre de la base de datos sea correcta. Esta actividad te permitirá familiarizarte con el manejo de bases de datos en Python.

### Actividad 3: Consultar Tablas desde MySQL

**Descripción:** Modifica tu aplicación Flask para listar las tablas presentes en una base de datos específica cuando se accede a la ruta "/api". Esto te permitirá comprender cómo realizar consultas SQL y procesar resultados en Python.

### Actividad 4: Recuperación de Datos desde Tabla

**Descripción:** Amplía tu aplicación Flask para que, al visitar la URL "/api", muestre los registros de todas las tablas disponibles en formato JSON. Aprenderás a ejecutar consultas SQL dinámicas y manipular datos.

### Actividad 5: Uso de Cursor y Fetchall

**Descripción:** Implementa el uso del cursor para recoger todos los registros de una tabla específica utilizando `fetchall()`. Asegúrate de manejar correctamente la lista de resultados obtenidos. Esta actividad te ayudará a entender cómo manipular y procesar datos SQL en Python.

### Actividad 6: Formateo JSON

**Descripción:** Convierte el contenido recuperado desde las tablas MySQL en un formato JSON legible para su visualización en una página web o API. Aprenderás a usar la biblioteca `json` de Python para serializar datos.

### Actividad 7: Integración con Plantillas Flask

**Descripción:** Integra tu aplicación Flask con plantillas HTML utilizando el módulo `render_template`. Crea una plantilla básica que muestra un resumen de las tablas recuperadas desde la base de datos. Esta actividad te permitirá combinar Python y HTML para generar páginas dinámicas.

### Actividad 8: Manejo de Errores

**Descripción:** Implementa manejo de errores en tu aplicación Flask, asegurándote que se capturan excepciones relacionadas con las consultas a la base de datos y se devuelven mensajes claros al usuario. Aprenderás a hacer tu código más robusto y confiable.

### Actividad 9: Seguridad de Contraseñas

**Descripción:** Implementa medidas básicas para proteger contraseñas en el código fuente, como no almacenarlas directamente o utilizar variables de entorno para configuraciones sensibles. Aprenderás sobre prácticas recomendadas en cuanto a seguridad del código.

### Actividad 10: Pruebas Unitarias

**Descripción:** Escribe pruebas unitarias utilizando frameworks como `unittest` para verificar el correcto funcionamiento de las funciones que interactúan con la base de datos y devuelven JSON. Aprenderás cómo garantizar que tu aplicación funciona correctamente desde un enfoque de prueba.


<a id="cadenas-de-caracteres-expresiones-regulares"></a>
## Cadenas de caracteres. Expresiones regulares

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/006-Aplicaci%C3%B3n%20de%20las%20estructuras%20de%20almacenamiento/005-Cadenas%20de%20caracteres.%20Expresiones%20regulares)

### Introducción a los ejercicios

Esta carpeta contiene ejercicios en Python centrados en el manejo de cadenas de caracteres y la conversión entre caracteres y sus códigos ASCII. Los estudiantes aprenderán a imprimir, recorrer y manipular cadenas, así como a codificar y decodificar texto mediante una simple técnica de cifrado por desplazamiento. A través de estos ejercicios, se practican habilidades fundamentales de programación, incluyendo bucles, funciones integradas como `len()`, `ord()` y `chr()`, y la creación de clases para encapsular funcionalidades relacionadas con el cifrado y descifrado de texto.

### cadena
<small>Creado: 2025-11-27 14:43</small>

#### Explicación

Este código Python muestra una forma simple de trabajar con cadenas de texto. La primera línea, `cadena = "Jose Vicente"`, crea una variable llamada `cadena` y le asigna el valor `"Jose Vicente"`. En este caso, la cadena es un conjunto de caracteres que representan un nombre.

La segunda línea, `print(cadena)`, imprime en pantalla lo que está almacenado en la variable `cadena`. Al ejecutar este código, verás que se muestra "Jose Vicente" en la salida del programa. Esto te permite visualizar fácilmente el contenido de una cadena y es útil para comprobar cómo están los datos durante la ejecución de un programa.

Este ejemplo básico ayuda a entender cómo guardar textos en variables y mostrarlos por pantalla, lo cual es fundamental al trabajar con cualquier tipo de información textual en programación.

`001-cadena.py`

```python
cadena = "Jose Vicente"
print(cadena)
```

### imprimo un caracter
<small>Creado: 2025-11-27 14:44</small>

#### Explicación

Este código Python muestra cómo trabajar con cadenas de texto. En primer lugar, se declara una variable llamada `cadena` que almacena el texto "Jose Vicente". Luego, se imprime esta cadena completa en la pantalla.

Después, se accede a un carácter específico dentro de la cadena usando corchetes (`[]`) y se imprime ese caracter. En este caso, `[0]` significa el primer caracter de la cadena (en programación, los índices generalmente empiezan en 0), por lo que se imprimirá "J".

Finalmente, se utiliza la función `len()` para determinar cuántos caracteres tiene la cadena y luego imprime esa longitud numérica. En este ejemplo, el resultado será el número 12, ya que "Jose Vicente" consta de 12 letras.

Este código es útil para entender cómo acceder a partes individuales de una cadena de texto y cómo obtener información sobre su estructura, como su longitud total.

`002-imprimo un caracter.py`

```python
cadena = "Jose Vicente"
print(cadena)

print(cadena[0])

longitud = len(cadena)
print(longitud)
```

### recorrer
<small>Creado: 2025-11-27 14:44</small>

#### Explicación

Este fragmento de código en Python muestra cómo trabajar con cadenas de caracteres, que son secuencias de texto. Primero, se crea una variable llamada `cadena` y se le asigna el valor "Jose Vicente". Luego, se imprime esta cadena utilizando la función `print()`. 

Después, el programa imprime solo el primer carácter de la cadena usando la notación de índice `[0]`, lo que significa que se accede al caracter en la posición 0, que es 'J' en este caso.

A continuación, se calcula y muestra la longitud de la cadena utilizando la función `len()`. Esto devuelve un número entero que indica cuántos caracteres hay en la cadena, incluyendo espacios. En el ejemplo dado, la longitud será 12 porque cuenta cada letra y el espacio entre nombres.

Finalmente, se utiliza un bucle `for` para recorrer e imprimir cada caracter de la cadena uno por uno. Este tipo de recorrido es útil cuando necesitas realizar alguna operación sobre cada carácter individual en una cadena, como contar vocales o buscar ciertas secuencias de texto.

`003-recorrer.py`

```python
cadena = "Jose Vicente"
print(cadena)

print(cadena[0])

longitud = len(cadena)
print(longitud)

for letra in cadena:
  print(letra)
```

### de cadena a ascii
<small>Creado: 2025-11-27 14:46</small>

#### Explicación

Este fragmento de código convierte una letra en su valor ASCII correspondiente. La variable `letra` almacena la cadena "a". Luego, se utiliza la función `ord()`, que es una función incorporada en Python para obtener el número entero que representa un carácter Unicode (ASCII para los primeros 128 caracteres). En este caso, `ord(letra)` convierte la letra "a" a su valor ASCII, que es 97. Finalmente, se imprime tanto la letra original como su valor ASCII.

Este código es importante porque muestra cómo acceder a códigos numéricos subyacentes para caracteres específicos, lo cual puede ser útil en situaciones donde necesitas trabajar con representaciones numéricas de letras, por ejemplo, en criptografía básica o manipulación de texto avanzada.

`004-de cadena a ascii.py`

```python
letra = "a"
ascii = ord(letra)
print(letra,ascii)
```

### paso de ascii a caracter
<small>Creado: 2025-11-27 14:47</small>

#### Explicación

Este fragmento de código te muestra cómo convertir un número ASCII en su equivalente carácter en Python. Primero, se define una variable llamada `ascii` y le asigna el valor numérico 97, que corresponde a la letra 'a' en el conjunto de caracteres ASCII.

Luego, se utiliza la función `chr()`, que toma un número entero (en este caso, el contenido de la variable `ascii`) y devuelve el carácter correspondiente. El resultado es asignado a una nueva variable llamada `letra`.

Finalmente, se imprime en pantalla tanto el valor numérico original (`97`) como el carácter que representa ('a'), lo que demuestra cómo la función `chr()` convierte un número ASCII en su representación de texto.

Este código es importante porque te ayuda a entender cómo los caracteres y sus valores numéricos ASCII están relacionados, lo cual es fundamental para manipulaciones avanzadas con cadenas de texto o códigos más complejos.

`005-paso de ascii a caracter.py`

```python
ascii = 97

letra = chr(ascii)

print(ascii,letra)
```

### codificar
<small>Creado: 2025-11-27 14:49</small>

#### Explicación

Este código es una pequeña aplicación en Python que toma un texto introducido por el usuario y lo modifica aplicando un cambio sencillo a cada carácter. Primero, pide al usuario que ingrese algún texto y luego recorre cada letra de esa entrada. Para cada letra, convierte la letra a su valor ASCII usando la función `ord()`, le suma 5 unidades para "codificar" el carácter (esto es, cambiar el carácter en algo parecido pero distinto) y después vuelve a convertir este nuevo número de vuelta a una letra con la función `chr()`. Finalmente, junta todas estas nuevas letras en una nueva cadena que muestra por pantalla. Este tipo de operaciones son útiles para aprender cómo manipular caracteres individualmente y entender conceptos básicos como los códigos ASCII, lo cual es fundamental en el manejo de textos en programación.

`006-codificar.py`

```python
cadena = input("Introduce algo de texto: ")

# Recorro la cadena
nuevacadena = ""
for letra in cadena:
  ascii = ord(letra)
  ascii += 5
  nuevaletra = chr(ascii)
  nuevacadena += nuevaletra
  
print(nuevacadena)
```

### descodificar
<small>Creado: 2025-11-27 14:50</small>

#### Explicación

Este fragmento de código te ayuda a descodificar un texto que ha sido alterado. En primer lugar, el programa pide al usuario que introduzca cualquier frase o palabra usando la función `input()`. Luego, recorre cada letra de esa entrada con un bucle `for`.

Dentro del bucle, cada letra se convierte en su valor ASCII mediante la función `ord(letra)`, y luego se resta 5 al número obtenido. Esto es como mover cada letra cinco lugares hacia atrás en el alfabeto (considerando los valores numéricos de los caracteres). El resultado se vuelve a convertir en una letra con `chr(ascii)` y se añade a una nueva cadena llamada `nuevacadena`.

Finalmente, después del bucle, la función `print(nuevacadena)` muestra el texto descodificado por pantalla. Este código es útil para entender cómo se pueden manipular cadenas de texto aplicando operaciones simples en sus valores ASCII, lo que permite codificar y descodificar mensajes de manera sencilla.

`007-descodificar.py`

```python
cadena = input("Introduce algo de texto: ")

# Recorro la cadena
nuevacadena = ""
for letra in cadena:
  ascii = ord(letra)
  ascii -= 5
  nuevaletra = chr(ascii)
  nuevacadena += nuevaletra
  
print(nuevacadena)
```

### clase codificar
<small>Creado: 2025-11-27 14:55</small>

#### Explicación

Este código Python crea una clase llamada `Codificador` que contiene dos métodos: `codifica()` y `descodifica()`. Estos métodos permiten cifrar y descifrar textos mediante un simple desplazamiento en el código ASCII de los caracteres.

En el método `codifica()`, se recorre cada letra de la cadena recibida. Para cada letra, primero se obtiene su valor ASCII usando la función `ord()` (que convierte una letra a su número ASCII). A este número le sumamos 5 para "desplazar" al caracter en el alfabeto o conjunto de caracteres. Luego convertimos ese nuevo número ASCII nuevamente a carácter mediante `chr()`, y añadimos esa nueva letra a la cadena cifrada que estamos construyendo.

El método `descodifica()` hace lo contrario: recorre cada letra de la cadena cifrada, resta 5 al valor ASCII de cada letra y luego vuelve a convertirlo en carácter para formar así una cadena descifrada.

Finalmente, el código crea un objeto `Codificador`, codifica la frase "Jose Vicente" utilizando este objeto, después descodifica lo que se obtuvo anteriormente y muestra tanto la frase original como las versiones cifrada y descifrada. Este tipo de encriptación es una variante simple del Cifrado César y sirve para mostrar cómo manipular caracteres usando sus códigos ASCII.

`008-clase codificar.py`

```python
class Codificador():
  def codifica(self,cadena):
    nuevacadena = ""
    for letra in cadena:
      ascii = ord(letra)
      ascii += 5
      nuevaletra = chr(ascii)
      nuevacadena += nuevaletra
    return nuevacadena
  def descodifica(self,cadena):
    nuevacadena = ""
    for letra in cadena:
      ascii = ord(letra)
      ascii -= 5
      nuevaletra = chr(ascii)
      nuevacadena += nuevaletra
    return nuevacadena
    
original = "Jose Vicente"
codificador = Codificador()
codificado = codificador.codifica(original)
descodificado = codificador.descodifica(codificado)

print(original)
print(codificado)
print(descodificado)
```

### Actividades propuestas

### Actividad 1: Manipulación Básica de Cadenas

**Descripción:** Los estudiantes deben imprimir una cadena dada e identificar y mostrar el primer carácter de la misma. Aprenderán a utilizar funciones básicas como `len()` para obtener la longitud de una cadena.

### Actividad 2: Recorrido y Visualización Caracter por Caracter

**Descripción:** Se pide que los estudiantes recorran una cadena y muestren cada caracter en una línea separada. Esta actividad les ayudará a entender el uso de bucles `for` con cadenas.

### Actividad 3: Conversión entre ASCII y Carácteres

**Descripción:** Los alumnos deben escribir un programa que convierta caracteres individuales a sus valores ASCII y viceversa, usando las funciones `ord()` y `chr()`. Este ejercicio fortalecerá su comprensión de cómo funcionan los códigos de caracteres en Python.

### Actividad 4: Codificación Simple

**Descripción:** Los estudiantes deben crear un programa que reciba una cadena del usuario e incremente el valor ASCII de cada caracter por 5 para codificarla. Esto les enseñará a combinar la entrada del usuario, bucles y manipulación de caracteres.

### Actividad 5: Descodificación Simple

**Descripción:** Los estudiantes deben escribir un programa que reciba una cadena ya codificada (cada caracter tiene su valor ASCII aumentado en 5) y descifre cada carácter restándole 5. Esto complementará la actividad anterior, proporcionando una comprensión completa del proceso de cifrado y decifrado.

### Actividad 6: Crear una Clase para Codificación

**Descripción:** Los alumnos deben implementar una clase llamada `Codificador` que tenga métodos para codificar y descodificar cadenas. Esta actividad les ayudará a entender cómo utilizar la orientación a objetos en Python para manejar tareas complejas de manera organizada.

### Actividad 7: Pruebas Unitarias para Codificación

**Descripción:** Los estudiantes deben escribir pruebas unitarias que comprueben que tanto el método `codifica` como `descodifica` dentro de la clase `Codificador` funcionan correctamente. Aprenderán a verificar y asegurar la funcionalidad del código.

### Actividad 8: Mejora en Codificación

**Descripción:** Se les pedirá a los estudiantes que mejoren su programa codificando cadenas no solo incrementando el valor ASCII por un número fijo, sino implementando una lógica más compleja para aumentar el valor ASCII de cada carácter. Aprenderán a pensar en soluciones más elaboradas y flexibles.

### Actividad 9: Aplicación Práctica

**Descripción:** Los estudiantes deben diseñar e implementar un pequeño programa que use codificación para ocultar mensajes secretos, mostrando cómo la programación puede ser usada de manera práctica en situaciones cotidianas. Esto les permitirá aplicar todo lo aprendido en un contexto real.

### Actividad 10: Resolución de Problemas

**Descripción:** Los alumnos deben identificar y corregir errores en programas existentes relacionados con la manipulación de cadenas, codificación y decodificación. Aprenderán a depurar código y mejorar sus habilidades analíticas.

Estas actividades están diseñadas para cubrir diversos aspectos del manejo de cadenas en Python, desde conceptos básicos hasta aplicaciones prácticas y soluciones de problemas avanzados.


<a id="colecciones-listas-conjuntos-y-diccionarios"></a>
## Colecciones Listas, Conjuntos y Diccionarios

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/006-Aplicaci%C3%B3n%20de%20las%20estructuras%20de%20almacenamiento/006-Colecciones%20Listas%2C%20Conjuntos%20y%20Diccionarios)

### Introducción a los ejercicios

En esta carpeta de ejercicios, trabajaremos con diferentes estructuras de datos en Python como listas y diccionarios. Los ejercicios están diseñados para que comprendas las diferencias entre estas colecciones, cómo almacenar e ingresar información de manera eficiente y por qué el uso de diccionarios puede ser más conveniente en ciertas situaciones debido a su flexibilidad en la indexación mediante claves.

A través de estos ejemplos, practicarás competencias fundamentales como la creación y manipulación de listas y diccionarios, así como entender cuándo es apropiado utilizar una estructura u otra según las necesidades específicas del problema que estés resolviendo.

### repaso
<small>Creado: 2025-11-27 14:57</small>

#### Explicación

Este fragmento de código crea dos estructuras de datos en Python: una lista y una tupla. La lista se llama `lista` y contiene tres elementos: 'platano', 'manzana' y 'fresa'. Lo importante aquí es que las listas son mutables, lo que significa que puedes añadir, eliminar o modificar sus elementos después de haberlas creado.

Por otro lado, la tupla se denomina `tupla` y contiene exactamente los mismos elementos. Sin embargo, en este caso, una vez que has definido la tupla, no puedes cambiar ninguno de sus elementos; es decir, las tuplas son inmutables.

Estas estructuras te permiten organizar datos de manera diferente dependiendo de tus necesidades: si sabes que los datos no van a cambiar, usar una tupla puede ser más eficiente y segura. Si necesitas manipular los datos o añadir elementos después de su creación, entonces deberías optar por utilizar una lista.

`001-repaso.py`

```python
lista = ['platano','manzana','fresa'] # mutable

tupla = ('platano','manzana','fresa') # inmutable
```

### agenda
<small>Creado: 2025-11-27 14:59</small>

#### Explicación

Este fragmento de código crea una lista en Python llamada `contacto` que almacena información sobre un contacto. La lista contiene cuatro elementos:

1. El nombre completo del contacto: "Jose Vicente Carratala Sanchis".
2. Su apellido o detalles adicionales del nombre: "Carratala Sanchis".
3. Su dirección de correo electrónico: "info@jocarsa.com".
4. Un número, que podría representar un teléfono o otra información relevante para el contacto.

Es importante entender que en Python, las listas son estructuras muy flexibles y permiten almacenar diferentes tipos de datos (cadenas de texto, números, etc.) dentro del mismo contenedor. En este caso, la lista `contacto` almacena información diversa relacionada con un contacto personal o profesional.

Esta forma de organizar datos es común en aplicaciones que manejan registros de contactos, como agendas electrónicas.

`002-agenda.py`

```python
contacto = ["Jose Vicente","Carratala Sanchis","info@jocarsa.com",47]
```

### el dicionario es mejor
<small>Creado: 2025-11-27 15:00</small>

#### Explicación

Este fragmento de código muestra cómo puedes almacenar información sobre una persona utilizando dos estructuras diferentes en Python: una lista y un diccionario. En primer lugar, se define una lista llamada `contacto` que contiene cuatro elementos: el nombre, los apellidos, el correo electrónico y la edad de una persona. Cada elemento ocupa una posición específica dentro de la lista.

Luego, se crea un diccionario llamado `contacto_diccionario`, que almacena exactamente la misma información pero de manera más estructurada y fácil de entender. En lugar de usar índices numéricos para acceder a los datos, el diccionario utiliza claves específicas como "nombre", "apellidos", "email" y "edad". Esto hace que sea mucho más claro y directo buscar la información deseada.

Esta diferencia es importante porque mientras que en una lista necesitas recordar qué número de índice corresponde a cada tipo de dato, con un diccionario simplemente usas el nombre del campo para obtener o modificar el valor. Esto no solo mejora la legibilidad del código sino también su mantenibilidad y facilidad de uso en situaciones complejas.

`003-el dicionario es mejor.py`

```python
contacto = ["Jose Vicente","Carratala Sanchis","info@jocarsa.com",47]

contacto_diccionario = {
  "nombre":"Jose Vicente",
  "apellidos":"Carratala Sanchis",
  "email":"info@jocarsa.com",
  "edad":47
}
```

### diferencias en el acceso
<small>Creado: 2025-11-27 15:00</small>

#### Explicación

Este fragmento de código compara cómo se accede a la información en una lista y un diccionario, que son dos estructuras de datos diferentes en Python. Primero, el código define una variable llamada `contacto` que es una lista que contiene información sobre una persona: su nombre completo, apellidos completos, correo electrónico y edad.

Luego, se crea otra variable llamada `contacto_diccionario`, que es un diccionario (también conocido como hash o mapa en otros lenguajes de programación) con la misma información pero organizada de una manera diferente. En el diccionario, cada pieza de información está asociada a una clave específica (como "nombre", "apellidos", etc.), lo que hace más clara y fácil la lectura del código.

Finalmente, se muestra cómo acceder al nombre tanto en la lista como en el diccionario. Para la lista `contacto`, usamos el índice `[0]` para obtener el primer elemento (que es el nombre completo). En cambio, para el diccionario `contacto_diccionario`, accedemos a la clave `'nombre'`. Esta diferencia demuestra cómo los diccionarios permiten una recuperación de datos más directa y legible en comparación con las listas.

`004-diferencias en el acceso.py`

```python
contacto = ["Jose Vicente","Carratala Sanchis","info@jocarsa.com",47]

contacto_diccionario = {
  "nombre":"Jose Vicente",
  "apellidos":"Carratala Sanchis",
  "email":"info@jocarsa.com",
  "edad":47
}

nombre = contacto[0]
nombre = contacto_diccionario['nombre']
```

### Actividades propuestas

### Actividad 1: Introducción a las Listas y Tuplas

**Descripción:** 
Los estudiantes deben crear una lista de frutas y una tupla con los mismos elementos, mostrando la diferencia entre su mutabilidad e inmutabilidad. Se espera que comprendan cómo añadir o modificar elementos en una lista sin poder hacer lo mismo con una tupla.

### Actividad 2: Registro de Contacto

**Descripción:** 
Los estudiantes deben diseñar un programa que almacene los datos completos de un contacto (nombre, apellidos, email y edad) en una estructura de tipo lista. El objetivo es familiarizarse con la creación e indexado básico.

### Actividad 3: Conversión a Diccionario

**Descripción:** 
Los estudiantes deben convertir el registro del contacto almacenado como lista (actividad anterior) en un diccionario, donde las claves serán los campos de datos y los valores los detalles específicos. Esta actividad ayudará a entender la ventaja de acceso directo usando claves.

### Actividad 4: Comparación entre Listas y Diccionarios

**Descripción:** 
Los estudiantes deben comparar el proceso de buscar un dato específico (como nombre o email) en una lista vs. en un diccionario, analizando cuál es más eficiente para la búsqueda. Se espera que reflexionen sobre las ventajas de usar cada estructura.

### Actividad 5: Manipulación de Diccionarios

**Descripción:** 
Los estudiantes deben crear y modificar un diccionario con información de contacto, incluyendo funciones para añadir nuevos datos y eliminar campos existentes. Esto les permitirá practicar la gestión dinámica de datos.

### Actividad 6: Integración de Datos en Aplicaciones

**Descripción:** 
Los estudiantes deben integrar los datos del diccionario (contacto) dentro de una pequeña aplicación que permita consultar y modificar dichos datos. Se centrará en cómo estructurar programas más complejos usando diccionarios.

### Actividad 7: Lista vs. Diccionario para Gestión de Datos

**Descripción:** 
Los estudiantes deben discutir e implementar un programa que almacene datos similares a los contactos utilizando tanto una lista como un diccionario, comparando la eficiencia y claridad en el código.

### Actividad 8: Diccionarios Anidados

**Descripción:** 
Los estudiantes deben crear un diccionario anidado para almacenar múltiples registros de contacto (cada uno siendo un sub-diccionario). Esto les permitirá entender la profundidad adicional que se puede dar a las estructuras de datos.

### Actividad 9: Intercambio de Estructuras

**Descripción:** 
Los estudiantes deben escribir una función que tome una lista de contactos (como en la actividad 2) y transforme esa lista en un diccionario. Luego, deben revertir el proceso para volver a la lista original.

### Actividad 10: Búsqueda Eficiente

**Descripción:** 
Los estudiantes deben diseñar pruebas que comprueben cuánto tiempo tardan las búsquedas de datos específicos en una lista comparado con un diccionario. Se espera que concluyan sobre la eficiencia del acceso directo en los diccionarios.


<a id="operaciones-agregadas-filtrado-reduccion-y-recoleccion"></a>
## Operaciones agregadas filtrado, reducción y recolección

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/006-Aplicaci%C3%B3n%20de%20las%20estructuras%20de%20almacenamiento/007-Operaciones%20agregadas%20filtrado%2C%20reducci%C3%B3n%20y%20recolecci%C3%B3n)

### Introducción a los ejercicios

El conjunto de archivos que proporcionaste representa un diagrama simple con cuatro formas y tres flechas conectando esas formas en diferentes direcciones. Aquí está una descripción detallada de los componentes del diagrama:

### HTML (`diagrama.html`)
Este archivo contiene el código HTML para renderizar las formas y las conexiones entre ellas como elementos visuales.

- **Formas:**
  - Una forma rectangular con texto "python".
  - Otra forma rectangular con texto "flask".
  - Otra forma rectangular con texto "index.html".
  - Y otra forma rectangular con texto "json(api)".
  
- **Flechas:**
  - Una flecha conecta la forma "flask" con la forma "index.html".
  - Otra flecha conecta la forma "flask" con la forma "json(api)".
  - La última flecha conecta la forma "json(api)" con la forma "index.html".

### JSON (`diagrama.json`)
Este archivo proporciona un formato de datos estructurado que representa las formas y las conexiones entre ellas.

- **Formas:**
  - Cada objeto en el array `formas` contiene una ID única, tipo, posición (izquierda, arriba), tamaño (ancho, alto) y texto para cada forma.
  
- **Flechas:**
  - Cada objeto en el array `flechas` describe la conexión entre dos formas, especificando la forma de origen y la forma de destino.

### SVG (`diagrama.svg`)
Este archivo es un documento vectorial que representa visualmente las formas y conexiones del diagrama utilizando elementos `<rect>` para representar los rectángulos y `<path>` para las flechas de conexión.

- **Formas:**
  - Cada elemento `<rect>` define la posición (x, y), tamaño (ancho, alto) y bordes redondeados (`rx` y `ry`) de cada forma.
  
- **Flechas:**
  - Elementos `<path>` conectan las formas mediante líneas con flechas en el extremo final.

### Ejemplos detallados:

1. **Forma de Python en HTML:**
   ```html
   <rect class="shape-rect" x="140.07102379432092" y="176.22159517728358" width="119.99997652493984" height="39.99996478740984" rx="4" ry="4" />
   <text x="200.07101205679083" y="200.2215775709885" text-anchor="middle">python</text>
   ```

2. **Flecha desde Flask a index.html en SVG:**
   ```svg
   <path class="conn" d="M 178.94258260704032 136.10794067382807 L 120.74488218036942 79.9999853280874" marker-end="url(#arrow-end)" />
   ```

3. **Conexión entre Flask y JSON API en JSON:**
   ```json
   {
     "desde": { "shapeId": "forma-2", "propId": null, "side": null },
     "hasta": { "shapeId": "forma-4", "propId": null, "side": null }
   }
   ```

Este conjunto de archivos proporciona una representación completa y coherente del diagrama en varios formatos, lo que permite su uso en diferentes contextos según sea necesario.

### lista de frutas
<small>Creado: 2025-11-27 15:02</small>

#### Explicación

Este código Python crea una lista llamada `frutas` que contiene cuatro elementos: 'manzana', 'pera', 'platano' y otra vez 'manzana'. Luego, el programa imprime esta lista en la pantalla usando la función `print()`. Este ejemplo ilustra cómo crear y mostrar listas en Python, lo cual es fundamental para aprender a manipular colecciones de datos. Es importante notar que las listas en Python pueden contener elementos duplicados, como se ve con 'manzana' apareciendo dos veces.

`001-lista de frutas.py`

```python
frutas = ['manzana','pera','platano','manzana']
print(frutas)
```

### conjunto de frutas
<small>Creado: 2025-11-27 15:04</small>

#### Explicación

Este código te muestra cómo funcionan los conjuntos en Python. Un conjunto es una estructura de datos que almacena elementos únicos, lo que significa que no puedes tener duplicados. En este caso, la variable `frutas` contiene cuatro elementos: 'manzana', 'pera', 'platano' y otra vez 'manzana'. Sin embargo, debido a la característica de los conjuntos de eliminar automáticamente cualquier elemento duplicado, el segundo 'manzana' no se incluirá en el conjunto final. Cuando imprimimos `frutas`, verás que solo aparecen tres elementos: 'pera', 'platano' y 'manzana'. La importancia de esto radica en la necesidad de trabajar con datos únicos sin preocuparse por eliminar duplicados manualmente.

`002-conjunto de frutas.py`

```python
# Los conjuntos no tienen orden concreto (no tienen indices)
# Los conjuntos no admiten duplicados (los duplicados se eliminan automaticamente)

frutas = {'manzana','pera','platano','manzana'}
print(frutas)
```

### conjunto inicial
<small>Creado: 2025-11-27 15:16</small>

#### Explicación

Este código es un ejemplo simple que demuestra cómo trabajar con conjuntos y listas en Python. Primero, el programa crea una variable llamada `muestra` que contiene un conjunto de números del 1 al 9. Luego, genera una lista llamada `serie`, compuesta por nueve números aleatorios entre 1 y 9.

El siguiente paso es convertir la lista `serie` en un conjunto llamado `filtrado`. Al convertirla a un conjunto, se eliminan cualquier duplicidad de números que puedan haber aparecido al generar los números aleatorios. Finalmente, el programa imprime tanto el conjunto original (`muestra`) como el nuevo conjunto generado (`filtrado`), así como la lista `serie`.

El código termina comprobando si ambos conjuntos, `muestra` y `filtrado`, son iguales en términos de sus elementos, aunque no necesariamente en el orden. Si son iguales, imprime "Es igual", lo que indica que el conjunto generado aleatoriamente contiene exactamente los mismos números que el conjunto original, sin importar el orden o las repeticiones.

Este tipo de operaciones es importante porque te ayuda a entender cómo trabajar con diferentes estructuras de datos en Python y cómo puedes transformar entre ellas para realizar tareas específicas.

`003-conjunto inicial.py`

```python
import random
muestra = {1,2,3,4,5,6,7,8,9}

serie = []

for i in range(0,9):
  numero = random.randint(1,9)
  serie.append(numero)

filtrado = set(serie)
print(muestra)
print(filtrado)
print(serie)

if filtrado == muestra:
  print("Es igual")
else:
  print("No es igual")
```

### fuerza bruta
<small>Creado: 2025-11-27 15:17</small>

#### Explicación

Este código Python utiliza un enfoque conocido como "fuerza bruta" para generar una serie de números aleatorios hasta que coincida con un conjunto predefinido. El programa crea inicialmente un conjunto llamado `muestra` que contiene los números del 1 al 9.

Luego, entra en un bucle infinito (`while True`) donde genera una lista llamada `serie`. Esta lista se llena con nueve números aleatorios generados por la función `random.randint(1,9)`, lo que significa que cada número en el rango del 1 al 9 tiene igual probabilidad de ser seleccionado.

Después, convierte la lista `serie` en un conjunto llamado `filtrado`. El objetivo es verificar si este conjunto generado aleatoriamente es igual al conjunto original `muestra`. Si ambos conjuntos son iguales (es decir, contienen exactamente los mismos elementos), el programa imprime "Es igual" y sale del bucle con la instrucción `break`.

Finalmente, después de que se rompe el ciclo, el código muestra por pantalla tanto el conjunto original (`muestra`), el conjunto generado aleatoriamente pero ya filtrado (`filtrado`) como la lista no filtrada (`serie`). Este ejercicio es útil para entender cómo los conjuntos en Python pueden ser utilizados para eliminar duplicados y comparar igualdad entre colecciones de datos.

`004-fuerza bruta.py`

```python
import random
muestra = {1,2,3,4,5,6,7,8,9}

while True:
  serie = []

  for i in range(0,9):
    numero = random.randint(1,9)
    serie.append(numero)

  filtrado = set(serie)
  if filtrado == muestra:
    print("Es igual")
    break;
    
print(muestra)
print(filtrado)
print(serie)
```

### repetimos 9 veces
<small>Creado: 2025-11-27 15:19</small>

#### Explicación

Este código genera una matriz de números que intenta simular los bloques en un tablero de Sudoku. En primer lugar, se importa el módulo `random` para generar números aleatorios y se define un conjunto llamado `muestra` que contiene los números del 1 al 9.

El código luego crea una lista vacía llamada `sudoku`, la cual va a almacenar nueve listas de nueve elementos cada una. Para hacer esto, hay un bucle `for` que itera desde 1 hasta 9 (inclusive), es decir, se ejecutará nueve veces.

Dentro de este bucle principal, hay otro bucle `while True:` que genera números aleatorios del 1 al 9 y los va añadiendo a una lista llamada `serie` hasta completar nueve elementos. Luego, el código convierte la lista en un conjunto para eliminar duplicados y comprueba si este conjunto es igual al conjunto `muestra`. Si lo es (es decir, contiene exactamente los números del 1 al 9 sin repeticiones), se sale del bucle interno con la instrucción `break`.

Una vez que se completa el bloque de código dentro del bucle `while`, la lista `serie` (que ahora debería contener nueve números diferentes entre 1 y 9) es añadida a la lista principal `sudoku`. Este proceso se repite nueve veces, resultando en una matriz de 9x9 que intenta simular los bloques de un Sudoku con números únicos en cada fila.

Finalmente, el código imprime la matriz generada por pantalla. Esta es una forma simple y didáctica para entender cómo generar filas válidas para un tablero de Sudoku, aunque no garantiza que todo el tablero sea válido como un Sudoku completo (por ejemplo, las columnas o bloques 3x3 también deben cumplir ciertas condiciones).

`005-repetimos 9 veces.py`

```python
import random
muestra = {1,2,3,4,5,6,7,8,9}

sudoku = []

for bloque in range(1,10):
  while True:
    serie = []
    for i in range(0,9):
      numero = random.randint(1,9)
      serie.append(numero)
    filtrado = set(serie)
    if filtrado == muestra:
      break;    
  sudoku.append(serie)
  
print(sudoku)
```

### lanzo esto con flask
<small>Creado: 2025-11-27 15:22</small>

#### Explicación

Este fragmento de código crea una aplicación web simple usando Flask, un popular framework para Python. La función principal es generar tableros aleatorios que cumplen con las reglas básicas del Sudoku (cada fila debe contener los números del 1 al 9 sin repetir). 

El programa primero establece la estructura básica de una aplicación web con Flask y define un endpoint llamado "/api" donde se genera un tablero de Sudoku. Para cada bloque del Sudoku, el código intenta generar una lista de nueve números que contienen exactamente los números del 1 al 9 sin repetir ninguno (utilizando un conjunto para verificar esto). Una vez que encuentra tal lista, la agrega a la matriz principal llamada `sudoku`. Finalmente, devuelve esta matriz en formato de cadena.

Este tipo de código es importante porque muestra cómo generar contenido dinámico y aleatorio dentro de una aplicación web, utilizando tanto estructuras de datos como operaciones sobre ellos para cumplir con ciertas condiciones específicas. En este caso, la generación de un Sudoku válido es un ejemplo sencillo pero instructivo de cómo se pueden crear tableros de juego o resolver problemas matemáticos usando Python y frameworks web.

`006-lanzo esto con flask.py`

```python
import random
from flask import Flask  

aplicacion = Flask(__name__)


@aplicacion.route("/api")
def api():
  muestra = {1,2,3,4,5,6,7,8,9}
  sudoku = []
  for bloque in range(1,10):
    while True:
      serie = []
      for i in range(0,9):
        numero = random.randint(1,9)
        serie.append(numero)
      filtrado = set(serie)
      if filtrado == muestra:
        break;    
    sudoku.append(serie)
    
  return str(sudoku)

if __name__ == "__main__":
  aplicacion.run()
```

### uso plantilla html
<small>Creado: 2025-11-27 15:24</small>

#### Explicación

Este código es un ejemplo de cómo usar Flask, una biblioteca popular en Python para crear aplicaciones web, y se enfoca en generar tableros de Sudoku. Vamos a desglosarlo:

1. **Importación de módulos**: El código comienza importando `random` (que proporciona funciones relacionadas con generación aleatoria) y `Flask`, `render_template` desde Flask. Flask es una biblioteca que nos ayuda a crear aplicaciones web.

2. **Creación del objeto Flask**: Se crea un objeto llamado `aplicacion` usando la clase Flask, el cual será nuestra aplicación web.

3. **Definición de rutas**: Dos rutas son definidas mediante decoradores:
   - `/`: Este es el punto de entrada principal de la aplicación. Cuando alguien visita esta URL, llama a la función `raiz()`, que usa `render_template` para mostrar un archivo HTML llamado "index.html".
   - `/api`: Esta ruta se encarga de generar una matriz 9x9 con números del 1 al 9 (una estructura básica similar a un tablero de Sudoku), usando métodos aleatorios y filtros. Después, devuelve esta matriz en forma de cadena.

4. **Generación de la matriz Sudoku**: Dentro de la función `api()`, se genera una matriz que representa el tablero del juego Sudoku:
   - Se inicializa un conjunto llamado `muestra` con los números del 1 al 9.
   - Se crea una lista vacía llamada `sudoku`.
   - Por cada bloque (de 9 en total), se intenta generar una fila de números del 1 al 9 que no contenga repeticiones. Si la serie generada tiene únicamente números entre 1 y 9 sin repetir ninguno, entonces esa fila se agrega a `sudoku`.
   
5. **Ejecución**: La última parte (`if __name__ == "__main__":`) asegura que solo se inicie el servidor Flask cuando este script se ejecuta directamente (no si es importado como un módulo en otro archivo).

Este código combina la generación de números aleatorios y la manipulación de estructuras de datos para crear una aplicación web simple con Flask, lo cual es útil tanto para aprender a trabajar con esta biblioteca como para entender cómo se pueden generar matrizes con restricciones específicas.

`007-uso plantilla html.py`

```python
import random
from flask import Flask,render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return render_template("index.html")

@aplicacion.route("/api")
def api():
  muestra = {1,2,3,4,5,6,7,8,9}
  sudoku = []
  for bloque in range(1,10):
    while True:
      serie = []
      for i in range(0,9):
        numero = random.randint(1,9)
        serie.append(numero)
      filtrado = set(serie)
      if filtrado == muestra:
        break;    
    sudoku.append(serie)
    
  return str(sudoku)

if __name__ == "__main__":
  aplicacion.run()
```

### me aseguro de que no se repita
<small>Creado: 2025-11-27 15:41</small>

#### Explicación

Este código Python crea una aplicación web simple utilizando Flask, un framework popular para desarrollo web en Python. La aplicación genera tableros de Sudoku y los devuelve como respuesta a las solicitudes del usuario.

La función `generar_sudoku()` es la clave de esta implementación. Inicializa un tablero 9x9 con ceros y luego utiliza una técnica llamada "backtracking" para llenarlo con números del 1 al 9 siguiendo las reglas de Sudoku: cada fila, columna y subcuadrante 3x3 deben contener todos los dígitos sin repetirse. La función `es_valido()` verifica si es seguro colocar un número en una celda específica.

El método `resolver()` es una implementación recursiva que intenta llenar el tablero de Sudoku, llamando a sí misma hasta que se completa o determina que no hay solución con los números actuales. Si encuentra una posición donde no puede insertar un número válido, vuelve atrás (backtracking) y prueba otro número.

La aplicación Flask tiene dos rutas definidas: la raíz (`/`) que muestra probablemente una página HTML interactiva para jugar Sudoku, y `/api` que devuelve un tablero de Sudoku generado en formato JSON cuando se solicita. La función `jsonify()` convierte el tablero del Sudoku (una matriz 9x9) a una respuesta HTTP válida con formato JSON.

Esta aplicación es útil como ejercicio práctico tanto para aprender a generar tableros de Sudoku como para explorar cómo crear aplicaciones web simples en Python usando Flask.

`008-me aseguro de que no se repita.py`

```python
import random
from flask import Flask, render_template, jsonify

aplicacion = Flask(__name__)


def generar_sudoku():
    # grid[row][col]
    grid = [[0 for _ in range(9)] for _ in range(9)]

    def es_valido(fila, columna, numero):
        # Comprobar fila
        if numero in grid[fila]:
            return False

        # Comprobar columna
        for f in range(9):
            if grid[f][columna] == numero:
                return False

        # Comprobar subcuadrante 3x3
        inicio_fila = (fila // 3) * 3
        inicio_columna = (columna // 3) * 3
        for f in range(inicio_fila, inicio_fila + 3):
            for c in range(inicio_columna, inicio_columna + 3):
                if grid[f][c] == numero:
                    return False

        return True

    def resolver(celda=0):
        # Si hemos rellenado las 81 celdas, ya está completo
        if celda == 81:
            return True

        fila = celda // 9
        columna = celda % 9

        numeros = list(range(1, 10))
        random.shuffle(numeros)

        for n in numeros:
            if es_valido(fila, columna, n):
                grid[fila][columna] = n
                if resolver(celda + 1):
                    return True
                # backtracking
                grid[fila][columna] = 0

        return False

    resolver()
    return grid


@aplicacion.route("/")
def raiz():
    return render_template("index2.html")


@aplicacion.route("/api")
def api():
    # sudoku es una matriz 9x9 con números del 1 al 9
    sudoku = generar_sudoku()
    # devolvemos JSON para que respuesta.json() funcione
    return jsonify(sudoku)


if __name__ == "__main__":
    aplicacion.run(debug=True)
```

### diagrama
<small>Creado: 2025-11-27 15:29</small>

#### Explicación

Este archivo HTML crea una representación visual de un diagrama simple usando elementos div con estilos CSS personalizados. El objetivo principal es mostrar la relación entre diferentes componentes, como archivos y servicios, a través de formas geométricas (rectángulos, círculos) y flechas.

En el cuerpo del documento, se encuentran varias etiquetas `<div>` que representan distintos elementos del diagrama. Estas divs tienen clases CSS específicas que determinan su apariencia y comportamiento. Por ejemplo:

- Las formas rectangulares con la clase `shape rectangle` representan archivos o servicios como "python", "flask", "index.html" y "json(api)". Cada una de estas divs tiene estilos adicionales que especifican sus dimensiones, ubicación en el espacio y texto interno.

- Las flechas que conectan estos elementos se crean con la clase `arrow`. Estas divs no tienen un ancho o alto definido; en su lugar, utilizan CSS para dibujar una línea recta (representada por el atributo de fondo) y una punta triangular al final del segmento.

El código CSS proporciona reglas que definen cómo se deben ver estas formas y flechas. Esto incluye propiedades como tamaño, ubicación, color, sombreado y bordes para dar a cada elemento su aspecto distintivo. Las reglas de CSS también permiten crear diferentes tipos de formas (por ejemplo, rectángulos con bordes redondeados o círculos) y flechas que cambian su dirección dependiendo del contexto.

Este tipo de diagrama es útil en contextos educativos para enseñar cómo funcionan los flujos de trabajo y las interacciones entre componentes de un sistema web básico, como la relación entre el archivo de código Python (que podría ser una aplicación Flask), el HTML que este sirve al navegador, y los datos JSON que se pueden recibir o enviar.

`diagrama.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Diagrama exportado</title>
<style>
body {
  margin: 0;
  padding: 20px;
  background: #f3f3f7;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}
.page {
  position: relative;
  background: #ffffff;
  border: 1px solid #d1d5db;
  box-shadow: 0 2px 4px rgba(0,0,0,.1);
  width: 391.17897620567896px;
  height: 256.2215599646934px;
  overflow: visible;
}

/* formas básicas */
.shape {
  position: absolute;
  min-width: 120px;
  min-height: 40px;
  padding: 6px 10px;
  background: #ffffff;
  border-radius: 4px;
  border: 1px solid #9ca3af;
  box-shadow: 0 1px 2px rgba(0,0,0,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
}

.shape.rectangle {
  border-radius: 4px;
}

.shape.pill {
  border-radius: 999px;
}

.shape.circle {
  border-radius: 999px;
  width: 80px;
  height: 80px;
  padding: 0;
  justify-content: center;
}

/* base de datos */
.shape.db {
  min-width: 120px;
  min-height: 60px;
  padding-top: 20px;
  border-radius: 60px / 16px;
  background: linear-gradient(180deg, #e5e7eb 0%, #ffffff 40%, #e5e7eb 100%);
  position: absolute;
  overflow: hidden;
  text-align: center;
}
.shape.db::before {
  content: "";
  position: absolute;
  top: 0;
  left: 8px;
  right: 8px;
  height: 18px;
  border-radius: 999px;
  border: 1px solid #9ca3af;
  background: radial-gradient(circle at 50% 30%, #ffffff 0%, #e5e7eb 70%);
}
.shape.db::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 8px;
  right: 8px;
  height: 18px;
  border-radius: 999px;
  border: 1px solid rgba(156, 163, 175, 0.6);
  border-top: none;
  background: radial-gradient(circle at 50% 70%, #e5e7eb 0%, #d1d5db 70%);
}

/* entidades ER */
.shape.entity {
  width: 220px;
  min-height: 80px;
  background: #ffffff;
  border: 2px solid #111827;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,.15);
  display: flex;
  flex-direction: column;
  font-size: 13px;
  overflow: hidden;
  padding: 0;
}
.entity-header {
  background: #f3f4f6;
  padding: 4px 8px;
  font-weight: 600;
  text-align: center;
  border-bottom: 1px solid #e5e7eb;
}
.entity-properties {
  flex: 1;
  padding: 4px 4px 0 4px;
}
.entity-property {
  display: grid;
  grid-template-columns: 14px 1fr 14px;
  align-items: center;
  column-gap: 4px;
  padding: 2px 0;
}
.entity-property .property-name {
  padding: 2px 4px;
  border-radius: 3px;
}

/* puertos */
.port {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  border: 1px solid #111827;
  background: #ffffff;
}
.port-left { justify-self: start; }
.port-right { justify-self: end; }

/* flechas rectas */
.arrow {
  position: absolute;
  height: 2px;
  background: #111827;
  transform-origin: 0 50%;
}
.arrow::after {
  content: "";
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-left: 8px solid #111827;
}
.arrow-double::before {
  content: "";
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%) rotate(180deg);
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-left: 8px solid #111827;
}

/* flechas ortogonales */
.ortho-arrow {
  position: absolute;
  left: 0;
  top: 0;
}
.ortho-arrow .ortho-seg {
  position: absolute;
  background: #111827;
}
.ortho-seg.seg-horizontal { height: 2px; }
.ortho-seg.seg-vertical { width: 2px; }
.ortho-arrowhead {
  position: absolute;
  width: 0;
  height: 0;
}
.ortho-arrowhead.dir-right {
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-left: 8px solid #111827;
}
.ortho-arrowhead.dir-left {
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-right: 8px solid #111827;
}
.ortho-arrowhead.dir-down {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 8px solid #111827;
}
.ortho-arrowhead.dir-up {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-bottom: 8px solid #111827;
}
</style>
</head>
<body>
<div class="page">

<div class="shape rectangle" style="left:140.07102379432092px;top:176.22159517728358px;width:119.99997652493984px;height:39.99996478740984px;">python</div>
<div class="shape rectangle" style="left:139.6874647874098px;top:136.10794067382807px;width:120.00002347506003px;height:39.99998532808742px;">flask</div>
<div class="shape rectangle" style="left:40px;top:40px;width:119.99997652493984px;height:39.99998532808742px;">index.html</div>
<div class="shape rectangle" style="left:231.1789527306189px;top:41.761357234074524px;width:120.00002347506003px;height:39.99998532808742px;">json(api)</div>
<div class="arrow" style="left:178.94258260704032px;top:136.10794067382807px;width:80.83981066301529px;transform:rotate(-2.374474533221754rad);"></div>
<div class="arrow" style="left:219.08223382269705px;top:136.10794067382807px;width:75.70370348306662px;transform:rotate(-0.8007603056930624rad);"></div>
<div class="arrow" style="left:231.1789527306189px;top:61.20856184152376px;width:71.18199704174366px;transform:rotate(-3.132379781778054rad);"></div>
</div>
</body>
</html>
```

### diagrama
<small>Creado: 2025-11-27 15:29</small>

#### Explicación

Este fragmento de código es un archivo JSON que contiene información sobre formas y flechas para un diagrama visual. El propósito principal es representar gráficamente la relación entre diferentes componentes en una aplicación web, como Python, Flask, HTML e interfaces JSON.

El objeto JSON tiene dos propiedades principales: `formas` y `flechas`. Bajo `formas`, encontramos cuatro elementos que describen cuadrados (rectángulos) con sus respectivos identificadores (`id`), tipos (`tipo`), posiciones (`left`, `top`) y texto que contienen. Estos elementos representan componentes como Python, Flask, un archivo HTML y una API JSON.

La propiedad `flechas` describe las conexiones entre estas formas a través de objetos que tienen propiedades `desde`, `hasta`, `tipo` y `estilo`. Cada flecha conecta dos formas diferentes, indicando cómo se relacionan los componentes. Por ejemplo, una flecha puede ir desde Flask hasta index.html para representar el flujo de control en una aplicación web básica.

Este tipo de diagramas es importante porque ayuda a visualizar y entender la arquitectura y flujo de datos en aplicaciones web, facilitando así su diseño y comprensión.

`diagrama.json`

```json
{
  "formas": [
    {
      "id": "forma-1",
      "tipo": "rectangle",
      "left": "520px",
      "top": "388.355px",
      "width": "",
      "height": "",
      "texto": "python"
    },
    {
      "id": "forma-2",
      "tipo": "rectangle",
      "left": "519.616px",
      "top": "348.253px",
      "width": "",
      "height": "",
      "texto": "flask"
    },
    {
      "id": "forma-3",
      "tipo": "rectangle",
      "left": "419.94px",
      "top": "252.144px",
      "width": "",
      "height": "",
      "texto": "index.html"
    },
    {
      "id": "forma-4",
      "tipo": "rectangle",
      "left": "611.11px",
      "top": "253.905px",
      "width": "",
      "height": "",
      "texto": "json(api)"
    }
  ],
  "flechas": [
    {
      "desde": {
        "shapeId": "forma-2",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-3",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-2",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-4",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-4",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-3",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    }
  ]
}
```

### diagrama
<small>Creado: 2025-11-27 15:29</small>

#### Explicación

Este código es un fragmento de SVG (Scalable Vector Graphics), que se utiliza para crear gráficos vectoriales en el navegador web. En este caso, el archivo está representando una imagen simple con varios rectángulos y líneas con flechas.

Los rectángulos en la imagen representan diferentes elementos o componentes del sistema, como archivos de código (por ejemplo, "python", "flask") y archivos HTML. Cada rectángulo tiene un estilo definido que incluye el color de relleno, el borde y las curvaturas en las esquinas.

Las líneas con flechas representan conexiones o dependencias entre estos componentes. Por ejemplo, una línea podría indicar que "flask" utiliza información del archivo "index.html". Estas líneas tienen marcadores de flecha para mostrar la dirección de la conexión.

Este tipo de diagrama es común en el desarrollo web y la programación orientada a servicios para visualizar cómo diferentes partes de un sistema interactúan entre sí. Es importante porque ayuda a entender las relaciones entre los componentes del código, facilitando así la colaboración y la comprensión del funcionamiento general del programa.

Este archivo SVG podría ser utilizado en una página web como parte de la documentación o para explicar visualmente cómo funciona un sistema web simple basado en Flask.

`diagrama.svg`

```
<svg xmlns="http://www.w3.org/2000/svg" width="391.17897620567896" height="256.2215599646934" viewBox="0 0 391.17897620567896 256.2215599646934">

  <defs>
    <style>
      text { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; font-size: 12px; fill: #111827; }
      .shape-rect { fill: #ffffff; stroke: #9ca3af; stroke-width: 1; }
      .shape-entity { fill: #ffffff; stroke: #111827; stroke-width: 2; }
      .shape-circle { fill: #ffffff; stroke: #9ca3af; stroke-width: 1; }
      .shape-pill { fill: #ffffff; stroke: #9ca3af; stroke-width: 1; }
      .shape-db { fill: #ffffff; stroke: #9ca3af; stroke-width: 1; }
      .conn { stroke: #111827; stroke-width: 2; fill: none; }
    </style>
    <marker id="arrow-end" markerWidth="10" markerHeight="7" refX="10" refY="3.5"
            orient="auto" markerUnits="strokeWidth">
      <polygon points="0 0, 10 3.5, 0 7" fill="#111827"/>
    </marker>
    <marker id="arrow-start" markerWidth="10" markerHeight="7" refX="0" refY="3.5"
            orient="auto" markerUnits="strokeWidth">
      <polygon points="10 0, 0 3.5, 10 7" fill="#111827"/>
    </marker>
  </defs>
        
<rect class="shape-rect" x="140.07102379432092" y="176.22159517728358" width="119.99997652493984" height="39.99996478740984" rx="4" ry="4" />
<text x="200.07101205679083" y="200.2215775709885" text-anchor="middle">python</text>
<rect class="shape-rect" x="139.6874647874098" y="136.10794067382807" width="120.00002347506003" height="39.99998532808742" rx="4" ry="4" />
<text x="199.68747652493983" y="160.10793333787177" text-anchor="middle">flask</text>
<rect class="shape-rect" x="40" y="40" width="119.99997652493984" height="39.99998532808742" rx="4" ry="4" />
<text x="99.99998826246991" y="63.99999266404371" text-anchor="middle">index.html</text>
<rect class="shape-rect" x="231.1789527306189" y="41.761357234074524" width="120.00002347506003" height="39.99998532808742" rx="4" ry="4" />
<text x="291.17896446814893" y="65.76134989811823" text-anchor="middle">json(api)</text>
<path class="conn" d="M 178.94258260704032 136.10794067382807 L 120.74488218036942 79.9999853280874" marker-end="url(#arrow-end)" />
<path class="conn" d="M 219.08223382269705 136.10794067382807 L 271.7842071703917 81.76134256216193" marker-end="url(#arrow-end)" />
<path class="conn" d="M 231.1789527306189 61.20856184152376 L 159.99997652493983 60.552780504359305" marker-end="url(#arrow-end)" />
</svg>
```

### Actividades propuestas

Los archivos proporcionados describen una representación visual de un diagrama que muestra la relación entre varios elementos en un sistema web, posiblemente asociado a un proyecto Flask. Vamos a analizar cada uno de los archivos:

1. **diagrama.html**:
    - Este archivo HTML contiene la representación del diagrama utilizando CSS y etiquetas `<div>`.
    - Las formas dentro del diagrama son divs con clases que corresponden a diferentes tipos de formas (por ejemplo, rectángulos).
    - Existen elementos que describen las relaciones entre los componentes del sistema mediante flechas.

2. **diagrama.json**:
    - Este archivo JSON contiene una estructura para el diagrama.
    - `formas` es un array donde cada elemento representa una forma (rectángulo, círculo) con propiedades como ID, tipo y posición (left, top).
    - `flechas` es un array que define las conexiones entre estas formas. Cada flecha tiene un origen (`desde`) y destino (`hasta`). 

3. **diagrama.svg**:
    - Este archivo SVG representa el diagrama en formato vectorial.
    - Incluye rectángulos para cada elemento (python, flask, index.html, json(api)).
    - Existen segmentos de línea que representan las flechas conectando los diferentes elementos.

### Componentes principales del Diagrama

- **Python**: Representado por un rectángulo.
- **Flask**: Otra forma rectangular indicada como framework web.
- **index.html**: Un archivo HTML interactivo en el sistema.
- **json(api)**: Representación de las interfaces de programación de aplicaciones (APIs) que probablemente proporciona datos JSON.

### Conexiones entre los componentes

1. **Flask a index.html**:
    - Una flecha conecta "flask" con "index.html", sugiriendo una interacción o servicio provisto por Flask para generar contenido HTML.
    
2. **Flask a json(api)**:
    - Otra flecha muestra que "flask" está conectado a un recurso o endpoint JSON, probablemente para proporcionar datos en formato JSON.

3. **json(api) a index.html**:
    - La última flecha indica una relación entre la interfaz JSON y el archivo HTML, posiblemente mostrando cómo los datos del JSON se utilizan o actualizan partes del contenido de `index.html`.

### Uso del Diagrama

Este diagrama es útil para entender las relaciones y flujos en un sistema basado en Flask. Por ejemplo:

- Un usuario podría interactuar con la página `index.html`.
- Esta interacción puede generar una solicitud al backend (Flask).
- El backend (Flask) genera datos JSON que se envían de vuelta a `index.html` para actualizar el contenido o proporcionar más funcionalidades.

### Código en Flask

El código en Python (`app.py`) implementa un servidor web sencillo utilizando Flask. Este servidor tiene dos endpoints:
1. `/`: Retorna un diccionario simple como respuesta, simbolizando la interacción con `index.html`.
2. `/api/`: Devuelve otro objeto JSON para simular una API.

En conclusión, este conjunto de archivos proporciona una representación visual y funcional de cómo se estructura y opera un sistema web básico basado en Flask, incluyendo el manejo de HTML y JSON.



<a id="utilizacion-avanzada-de-clases"></a>
# Utilización avanzada de clases

<a id="composicion-de-clases"></a>
## Composición de clases

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/007-Utilizaci%C3%B3n%20avanzada%20de%20clases/001-Composici%C3%B3n%20de%20clases)


<a id="herencia-y-polimorfismo"></a>
## Herencia y polimorfismo

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/007-Utilizaci%C3%B3n%20avanzada%20de%20clases/002-Herencia%20y%20polimorfismo)


<a id="jerarquia-de-clases-superclases-y-subclases"></a>
## Jerarquía de clases Superclases y subclases

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/007-Utilizaci%C3%B3n%20avanzada%20de%20clases/003-Jerarqu%C3%ADa%20de%20clases%20Superclases%20y%20subclases)


<a id="clases-y-metodos-abstractos-y-finales"></a>
## Clases y métodos abstractos y finales

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/007-Utilizaci%C3%B3n%20avanzada%20de%20clases/004-Clases%20y%20m%C3%A9todos%20abstractos%20y%20finales)


<a id="interfaces"></a>
## Interfaces

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/007-Utilizaci%C3%B3n%20avanzada%20de%20clases/005-Interfaces)


<a id="sobreescritura-de-metodos"></a>
## Sobreescritura de métodos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/007-Utilizaci%C3%B3n%20avanzada%20de%20clases/006-Sobreescritura%20de%20m%C3%A9todos)


<a id="constructores-y-herencia"></a>
## Constructores y herencia

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/007-Utilizaci%C3%B3n%20avanzada%20de%20clases/007-Constructores%20y%20herencia)



<a id="mantenimiento-de-la-persistencia-de-los-objetos"></a>
# Mantenimiento de la persistencia de los objetos

<a id="bases-de-datos-orientadas-a-objetos"></a>
## Bases de datos orientadas a objetos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/001-Bases%20de%20datos%20orientadas%20a%20objetos)


<a id="caracteristicas-de-las-bases-de-datos-orientadas-a-objetos"></a>
## Características de las bases de datos orientadas a objetos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/002-Caracter%C3%ADsticas%20de%20las%20bases%20de%20datos%20orientadas%20a%20objetos)


<a id="instalacion-del-gestor-de-bases-de-datos"></a>
## Instalación del gestor de bases de datos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/003-Instalaci%C3%B3n%20del%20gestor%20de%20bases%20de%20datos)


<a id="creacion-de-bases-de-datos"></a>
## Creación de bases de datos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/004-Creaci%C3%B3n%20de%20bases%20de%20datos)


<a id="mecanismos-de-consulta"></a>
## Mecanismos de consulta

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/005-Mecanismos%20de%20consulta)


<a id="el-lenguaje-de-consultas-sintaxis-expresiones-operadores"></a>
## El lenguaje de consultas sintaxis, expresiones, operadores

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/006-El%20lenguaje%20de%20consultas%20sintaxis%2C%20expresiones%2C%20operadores)


<a id="recuperacion-modificacion-y-borrado-de-informacion"></a>
## Recuperación, modificación y borrado de información

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/007-Recuperaci%C3%B3n%2C%20modificaci%C3%B3n%20y%20borrado%20de%20informaci%C3%B3n)


<a id="tipos-de-datos-objeto-atributos-y-metodos"></a>
## Tipos de datos objeto; atributos y métodos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/008-Tipos%20de%20datos%20objeto%3B%20atributos%20y%20m%C3%A9todos)


<a id="tipos-de-datos-coleccion"></a>
## Tipos de datos colección

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/008-Mantenimiento%20de%20la%20persistencia%20de%20los%20objetos/009-Tipos%20de%20datos%20colecci%C3%B3n)



<a id="gestion-de-bases-de-datos"></a>
# Gestión de bases de datos

<a id="acceso-a-bases-de-datos-estandares-caracteristicas"></a>
## Acceso a bases de datos. Estándares. Características

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/009-Gesti%C3%B3n%20de%20bases%20de%20datos/001-Acceso%20a%20bases%20de%20datos.%20Est%C3%A1ndares.%20Caracter%C3%ADsticas)


<a id="establecimiento-de-conexiones"></a>
## Establecimiento de conexiones

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/009-Gesti%C3%B3n%20de%20bases%20de%20datos/002-Establecimiento%20de%20conexiones)


<a id="almacenamiento-recuperacion-actualizacion-y-eliminacion-de-informacion-en-bases-de-datos"></a>
## Almacenamiento, recuperación, actualización y eliminación de información en bases de datos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/009-Gesti%C3%B3n%20de%20bases%20de%20datos/003-Almacenamiento%2C%20recuperaci%C3%B3n%2C%20actualizaci%C3%B3n%20y%20eliminaci%C3%B3n%20de%20informaci%C3%B3n%20en%20bases%20de%20datos)



<a id="proyectos"></a>
# Proyectos

<a id="proyecto-formulario"></a>
## Proyecto formulario

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/010-Proyectos/001-Proyecto%20formulario)

### Introducción a los ejercicios

El código proporcionado incluye varios componentes para crear una aplicación web administrativa con funcionalidades de gestión y monitoreo de registros en una base de datos MySQL. A continuación, se analiza la estructura del código y cómo estos archivos interactúan entre sí.

### Análisis del Código

#### 1. **index.php**
Este archivo es el punto de entrada principal de la aplicación web. Realiza las siguientes tareas:

- **Conexión a MySQL**: Establece una conexión a la base de datos `training_center` mediante PHP.
- **Obtención de Datos**: Consulta los registros de la tabla `inscripciones`.
- **Estado CRM**: Consulta y almacena en un array el estado actual de cada registro para mostrarlo en la interfaz.
- **Correos no leídos**: Verifica si hay correos nuevos sin leer para cada registro con correo electrónico asociado.
- **Visualización del Formulario HTML/CSS/PHP**:
  - Si se ha enviado una solicitud (`$_POST`), actualiza el estado CRM correspondiente en la base de datos.
  - Muestra un formulario basado en los registros obtenidos, incluyendo campos para seleccionar y guardar estados CRM, así como botones para acceder a informes detallados.

#### 2. **CSS y Estilos**
- El archivo `index.php` utiliza CSS directamente dentro del código PHP para estilizar la tabla de registros.
- Los colores y estilos específicos se aplican dinámicamente basándose en el estado CRM asociado a cada registro.

#### 3. **PHP Integración con MySQL**
- Consultas SQL: Se utilizan consultas SQL como `SELECT` y `UPDATE` para intercambiar datos entre la base de datos y la aplicación web.
- Variables Globales: El archivo `$db_host`, `$db_user`, `$db_pass`, y `$dbname` proporciona las credenciales necesarias para conectarse a la base de datos MySQL.

#### 4. **Interacción con IMAP (Correo Electrónico)**
- **listar_carpetas.php**: Este script se utiliza internamente para listar las carpetas del correo electrónico en el servidor IMAP.
- La aplicación principal (`index.php`) verifica si hay correos nuevos sin leer utilizando un archivo similar o directamente mediante `imap_open` y consultas de IMAP.

### Diagrama JSON
El diagrama JSON proporcionado representa visualmente cómo se relacionan los archivos entre sí:

- **Formulario HTML, CSS, PHP**: Representa el frontend donde se muestran los datos obtenidos desde la base de datos y el sistema de correo electrónico.
- **MySQL**: La base de datos que almacena registros de inscripciones y estados CRM.
- **PHP**: Se utiliza para manejar lógica de negocio (como actualización del estado), interacción con MySQL e IMAP, y generación dinámica de HTML/CSS.

### Interconexión
- **HTML/PHP** -> **MySQL**: Consultas a la base de datos para obtener registros y guardar cambios.
- **IMAP**: Se conecta al servidor IMAP para verificar correos no leídos asociados con cada registro.

---

Esta estructura permite una aplicación web funcional que permite a los usuarios gestionar inscripciones, asignar estados CRM y monitorear correos sin leer de manera dinámica.

### formulario
<small>Creado: 2025-12-04 15:13</small>

#### Explicación

Este código es una página HTML que genera un formulario dinámico para recoger datos en función de la estructura de una tabla llamada `inscripciones` en una base de datos MySQL. La página comienza creando una conexión a la base de datos y luego consulta los detalles de la tabla y sus columnas, incluyendo comentarios asociados con cada columna si existen.

El código PHP se encarga de generar etiquetas HTML (`<input>`, `<select>`, `<textarea>`) basadas en el tipo de dato que tiene cada columna en la base de datos. Por ejemplo, para un campo de tipo `varchar`, crea una caja de texto; para un campo de tipo `date`, una entrada de fecha; y así sucesivamente.

Este formulario es importante porque permite a los usuarios introducir datos en formato estructurado según el diseño previamente definido en la base de datos, facilitando así la recopilación y gestión de información. La generación automática del formulario basada en la tabla de la base de datos también ayuda a mantener el código más organizado y fácil de actualizar si se modifica la estructura de los datos en un futuro.

`001-formulario.php`

```
<!doctype html>
<html lang="es">
  <head>
    <title>Formulario</title>
    <meta charset="utf-8">

    <style>
      /* Tus estilos originales tal cual */
      :root{
        --primary: crimson;
        --primary-light: #ff8fa0;
        --bg: #f2f2f2;
        --text: #333;
        --border: #ddd;
      }
      body, html{
        background: var(--bg);
        display: flex;
        justify-content: center;
        padding: 40px;
        font-family: "Segoe UI", sans-serif;
        color: var(--text);
      }
      form{
        background: white;
        padding: 30px 40px;
        width: 650px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-top: 8px solid var(--primary);
      }
      legend{
        font-size: 1.4em;
        font-weight: bold;
        color: var(--primary);
        margin-bottom: 10px;
      }
      form fieldset{
        display: flex;
        flex-direction: column;
        gap: 20px;
        border: none;
        padding: 0;
      }
      .control_formulario{
        display: flex;
        flex-direction: column;
        gap: 6px;
      }
      .control_formulario label{
        font-size: 0.95em;
        font-weight: 600;
        color: var(--primary);
      }
      form fieldset input:not([type="checkbox"]),
      form fieldset select,
      form fieldset textarea{
        padding: 12px 14px;
        border: 1px solid var(--border);
        border-radius: 6px;
        width: 100%;
        font-size: 1em;
        transition: border 0.3s, box-shadow 0.3s;
        box-sizing:border-box;
      }
      .control_formulario_checkbox{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
      }
      .control_formulario_checkbox input[type="checkbox"]{
        appearance: none;
        width: 52px;
        height: 28px;
        border-radius: 999px;
        background: #ccc;
        cursor: pointer;
        border: 1px solid #bbb;
        transition: background .25s;
        position: relative;
      }
      .control_formulario_checkbox input[type="checkbox"]::before{
        content: "";
        position: absolute;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background: white;
        top: 50%;
        left: 3px;
        transform: translateY(-50%);
        transition: transform 0.25s;
      }
      .control_formulario_checkbox input[type="checkbox"]:checked{
        background: var(--primary);
        border-color: var(--primary);
      }
      .control_formulario_checkbox input[type="checkbox"]:checked::before{
        transform: translate(22px, -50%);
      }

      input[type="submit"]{
        background: var(--primary);
        color: white;
        padding: 14px;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        cursor: pointer;
        margin-top: 10px;
      }
    </style>

  </head>
  <body>
    <form action="" method="POST" enctype="multipart/form-data">
      <fieldset>
        <legend>Formulario de recogida de datos</legend>

        <?php
          $c = new mysqli("localhost","training_center","training_center","training_center");

          /* COMENTARIO DE LA TABLA */
          $tableComment = $c->query("
            SELECT TABLE_COMMENT
            FROM information_schema.tables
            WHERE table_schema='training_center'
              AND table_name='inscripciones'
          ")->fetch_assoc()['TABLE_COMMENT'];

          if ($tableComment != "") {
              echo "<p style='color:#555; margin-top:-5px; margin-bottom:20px;'>$tableComment</p>";
          }

          /* COLUMNAS CON SUS COMENTARIOS */
          $r = $c->query("
            SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT
            FROM information_schema.columns
            WHERE table_schema='training_center'
              AND table_name='inscripciones'
          ");

          while($f = $r->fetch_assoc()) {

            $campo = $f['COLUMN_NAME'];
            $tipo  = $f['COLUMN_TYPE'];
            $comentario = $f['COLUMN_COMMENT'];

            /* NO tocar esta lógica: respetar exclusiones */
            if($f['COLUMN_KEY'] == "PRI" || $f['COLUMN_DEFAULT'] == "CURRENT_TIMESTAMP") continue;

            echo '<div class="control_formulario">';

            // LABEL = nombre técnico de la columna (como pediste)
            echo '<label for="'.$campo.'">Introduce '.$campo.'</label>';

            // PÁRRAFO = comentario explicativo
            if ($comentario != "") {
              echo '<p style="margin:0; font-size:0.85em; color:#666;">'.$comentario.'</p>';
            }

            /* ---------- Mantener tus tipos de campo exactamente ---------- */

            if (str_contains($tipo, "varchar")) {
               echo '<input type="text" name="'.$campo.'" id="'.$campo.'">';
            }
            else if ($tipo == "date") {
               echo '<input type="date" name="'.$campo.'" id="'.$campo.'">';
            }
            else if ($tipo == "int") {
               echo '<input type="number" name="'.$campo.'" id="'.$campo.'">';
            }
            else if (str_contains($tipo, "decimal")) {
               echo '<input type="number" name="'.$campo.'" id="'.$campo.'" step="0.01">';
            }
            else if (str_contains($tipo, "tinyint")) {
               echo '<div class="control_formulario_checkbox">';
               echo '<label for="'.$campo.'">Introduce '.$campo.'</label>';
               echo '<input type="checkbox" name="'.$campo.'" id="'.$campo.'">';
               echo '</div>';
            }
            else if (str_contains($tipo, "enum")) {
               echo '<select name="'.$campo.'" id="'.$campo.'">';
               preg_match_all("/'([^']+)'/", $tipo, $matches);
               foreach($matches[1] as $valor){
                 echo '<option value="'.$valor.'">'.$valor.'</option>';
               }
               echo '</select>';
            }
            else if ($tipo == "text") {
               echo '<textarea name="'.$campo.'" id="'.$campo.'"></textarea>';
            }
            else if (str_contains($tipo, "blob")) {
               echo '<input type="file" name="'.$campo.'" id="'.$campo.'">';
            }

            echo '</div>';
          }
        ?>

        <input type="submit">
      </fieldset>
    </form>
  </body>
</html>
```

### guardamos los datos
<small>Creado: 2025-12-04 15:16</small>

#### Explicación

Este archivo PHP es parte de un formulario web que se utiliza para guardar datos en una base de datos. El código realiza las siguientes acciones principales:

1. **Conexión a la Base de Datos:** Al inicio del archivo, el script establece una conexión con la base de datos MySQL usando la clase `mysqli`. Si la conexión falla, muestra un mensaje de error.

2. **Procesamiento del Formulario:** El código verifica si se ha enviado el formulario (mediante un método POST). Si es así, recupera los metadatos de las columnas de la tabla `inscripciones` para determinar qué campos y tipos de datos manejar.

3. **Generación Dinámica del INSERT SQL:** Para cada columna que no sea clave primaria ni tenga valores por defecto predefinidos (como timestamps), el script recupera los datos enviados desde el formulario. Luego, construye una consulta SQL `INSERT` que insertará estos datos en la tabla correspondiente.

4. **Manejo de Diferentes Tipos de Datos:** El código identifica cada tipo de dato y asigna un valor apropiado basándose en la entrada del usuario. Por ejemplo, si el campo es de tipo entero (`int`), se convierte la entrada a un número entero; si es un archivo (`blob`), se lee su contenido binario.

5. **Ejecución de la Consulta SQL:** Una vez que se ha construido la consulta `INSERT`, se prepara y ejecuta utilizando la función `prepare` y `execute`. Si la inserción es exitosa, el usuario recibe un mensaje indicando que los datos han sido guardados correctamente.

6. **HTML del Formulario:** Finalmente, el código genera una página HTML con el formulario de entrada. Cada campo del formulario se genera dinámicamente basándose en los metadatos recuperados de la base de datos. Esto incluye etiquetas y campos de entrada correspondientes a cada tipo de dato (por ejemplo, texto para `varchar`, fecha para `date`, etc.), así como comentarios explicativos si están disponibles.

Este archivo es crucial porque permite interactuar con la base de datos de manera segura y eficiente, garantizando que los datos ingresados por el usuario sean almacenados correctamente en la tabla correspondiente.

`002-guardamos los datos.php`

```
<?php
// Conexión a la base de datos (una sola vez, al inicio del archivo)
$c = new mysqli("localhost","training_center","training_center","training_center");
if ($c->connect_error) {
  die("Error de conexión: " . $c->connect_error);
}

$mensaje = "";

// Procesar envío del formulario
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

  // Recuperar metadatos de columnas de la tabla
  $meta = $c->query("
    SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT
    FROM information_schema.columns
    WHERE table_schema='training_center'
      AND table_name='inscripciones'
  ");

  $columnas      = [];
  $placeholders  = [];
  $valores       = [];
  $tiposBind     = "";

  while ($f = $meta->fetch_assoc()) {

    $campo     = $f['COLUMN_NAME'];
    $tipo      = $f['COLUMN_TYPE'];
    $colKey    = $f['COLUMN_KEY'];
    $colDef    = $f['COLUMN_DEFAULT'];

    // Misma exclusión que en el formulario
    if ($colKey == "PRI" || $colDef == "CURRENT_TIMESTAMP") {
      continue;
    }

    // Determinar el valor recibido según el tipo
    $valor = null;

    if (str_contains($tipo, "varchar")) {
      $valor = $_POST[$campo] ?? null;
      $tiposBind .= "s";
    }
    else if ($tipo == "date") {
      $valor = $_POST[$campo] ?? null;
      $tiposBind .= "s";
    }
    else if ($tipo == "int") {
      // Número entero
      $valor = isset($_POST[$campo]) && $_POST[$campo] !== "" ? (int)$_POST[$campo] : null;
      $tiposBind .= "i";
    }
    else if (str_contains($tipo, "decimal")) {
      // Número decimal
      $valor = isset($_POST[$campo]) && $_POST[$campo] !== "" ? (float)$_POST[$campo] : null;
      $tiposBind .= "d";
    }
    else if (str_contains($tipo, "tinyint")) {
      // Checkbox: si no viene en POST, se considera 0
      $valor = isset($_POST[$campo]) ? 1 : 0;
      $tiposBind .= "i";
    }
    else if (str_contains($tipo, "enum")) {
      // Enum: valor de la lista
      $valor = $_POST[$campo] ?? null;
      $tiposBind .= "s";
    }
    else if ($tipo == "text") {
      $valor = $_POST[$campo] ?? null;
      $tiposBind .= "s";
    }
    else if (str_contains($tipo, "blob")) {
      // Archivo subido: se guarda el contenido binario
      if (isset($_FILES[$campo]) && $_FILES[$campo]['error'] === UPLOAD_ERR_OK) {
        $valor = file_get_contents($_FILES[$campo]['tmp_name']);
      } else {
        $valor = null;
      }
      $tiposBind .= "s"; // Se envía como string; MySQL lo almacenará en el BLOB
    } else {
      // Cualquier otro tipo no contemplado explícitamente
      $valor = $_POST[$campo] ?? null;
      $tiposBind .= "s";
    }

    $columnas[]     = $campo;
    $placeholders[] = "?";
    $valores[]      = $valor;
  }

  if (!empty($columnas)) {

    $sql = "INSERT INTO inscripciones (" . implode(",", $columnas) . ")
            VALUES (" . implode(",", $placeholders) . ")";

    $stmt = $c->prepare($sql);

    if ($stmt) {
      // Construir array de parámetros por referencia para bind_param
      $params = [];
      $params[] = &$tiposBind;
      foreach ($valores as $k => $v) {
        $params[] = &$valores[$k];
      }

      // bind_param dinámico
      call_user_func_array([$stmt, 'bind_param'], $params);

      if ($stmt->execute()) {
        $mensaje = "Datos guardados correctamente.";
      } else {
        $mensaje = "Error al guardar los datos: " . $stmt->error;
      }

      $stmt->close();
    } else {
      $mensaje = "Error al preparar la consulta: " . $c->error;
    }
  } else {
    $mensaje = "No hay columnas que insertar (revisa la definición de la tabla).";
  }
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>Formulario</title>
    <meta charset="utf-8">

    <style>
      /* Tus estilos originales tal cual */
      :root{
        --primary: crimson;
        --primary-light: #ff8fa0;
        --bg: #f2f2f2;
        --text: #333;
        --border: #ddd;
      }
      body, html{
        background: var(--bg);
        display: flex;
        justify-content: center;
        padding: 40px;
        font-family: "Segoe UI", sans-serif;
        color: var(--text);
      }
      form{
        background: white;
        padding: 30px 40px;
        width: 650px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-top: 8px solid var(--primary);
      }
      legend{
        font-size: 1.4em;
        font-weight: bold;
        color: var(--primary);
        margin-bottom: 10px;
      }
      form fieldset{
        display: flex;
        flex-direction: column;
        gap: 20px;
        border: none;
        padding: 0;
      }
      .control_formulario{
        display: flex;
        flex-direction: column;
        gap: 6px;
      }
      .control_formulario label{
        font-size: 0.95em;
        font-weight: 600;
        color: var(--primary);
      }
      form fieldset input:not([type="checkbox"]),
      form fieldset select,
      form fieldset textarea{
        padding: 12px 14px;
        border: 1px solid var(--border);
        border-radius: 6px;
        width: 100%;
        font-size: 1em;
        transition: border 0.3s, box-shadow 0.3s;
        box-sizing:border-box;
      }
      .control_formulario_checkbox{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
      }
      .control_formulario_checkbox input[type="checkbox"]{
        appearance: none;
        width: 52px;
        height: 28px;
        border-radius: 999px;
        background: #ccc;
        cursor: pointer;
        border: 1px solid #bbb;
        transition: background .25s;
        position: relative;
      }
      .control_formulario_checkbox input[type="checkbox"]::before{
        content: "";
        position: absolute;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background: white;
        top: 50%;
        left: 3px;
        transform: translateY(-50%);
        transition: transform 0.25s;
      }
      .control_formulario_checkbox input[type="checkbox"]:checked{
        background: var(--primary);
        border-color: var(--primary);
      }
      .control_formulario_checkbox input[type="checkbox"]:checked::before{
        transform: translate(22px, -50%);
      }

      input[type="submit"]{
        background: var(--primary);
        color: white;
        padding: 14px;
        border: none;
        border-radius: 6px;
        font-size: 1.1em;
        cursor: pointer;
        margin-top: 10px;
      }
    </style>

  </head>
  <body>
    <form action="" method="POST" enctype="multipart/form-data">
      <fieldset>
        <legend>Formulario de recogida de datos</legend>

        <?php if ($mensaje != ""): ?>
          <p style="padding:10px 12px; border-radius:6px;
                    background:#f8f8f8; border:1px solid #ddd;
                    font-size:0.9em; color:#444;">
            <?= htmlspecialchars($mensaje, ENT_QUOTES, 'UTF-8'); ?>
          </p>
        <?php endif; ?>

        <?php
          /* COMENTARIO DE LA TABLA */
          $tableComment = $c->query("
            SELECT TABLE_COMMENT
            FROM information_schema.tables
            WHERE table_schema='training_center'
              AND table_name='inscripciones'
          ")->fetch_assoc()['TABLE_COMMENT'];

          if ($tableComment != "") {
              echo "<p style='color:#555; margin-top:-5px; margin-bottom:20px;'>$tableComment</p>";
          }

          /* COLUMNAS CON SUS COMENTARIOS */
          $r = $c->query("
            SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT
            FROM information_schema.columns
            WHERE table_schema='training_center'
              AND table_name='inscripciones'
          ");

          while($f = $r->fetch_assoc()) {

            $campo = $f['COLUMN_NAME'];
            $tipo  = $f['COLUMN_TYPE'];
            $comentario = $f['COLUMN_COMMENT'];

            /* NO tocar esta lógica: respetar exclusiones */
            if($f['COLUMN_KEY'] == "PRI" || $f['COLUMN_DEFAULT'] == "CURRENT_TIMESTAMP") continue;

            echo '<div class="control_formulario">';

            // LABEL = nombre técnico de la columna (como pediste)
            echo '<label for="'.$campo.'">Introduce '.$campo.'</label>';

            // PÁRRAFO = comentario explicativo
            if ($comentario != "") {
              echo '<p style="margin:0; font-size:0.85em; color:#666;">'.$comentario.'</p>';
            }

            /* ---------- Mantener tus tipos de campo exactamente ---------- */

            if (str_contains($tipo, "varchar")) {
               echo '<input type="text" name="'.$campo.'" id="'.$campo.'">';
            }
            else if ($tipo == "date") {
               echo '<input type="date" name="'.$campo.'" id="'.$campo.'">';
            }
            else if ($tipo == "int") {
               echo '<input type="number" name="'.$campo.'" id="'.$campo.'">';
            }
            else if (str_contains($tipo, "decimal")) {
               echo '<input type="number" name="'.$campo.'" id="'.$campo.'" step="0.01">';
            }
            else if (str_contains($tipo, "tinyint")) {
               echo '<div class="control_formulario_checkbox">';
               echo '<label for="'.$campo.'">Introduce '.$campo.'</label>';
               echo '<input type="checkbox" name="'.$campo.'" id="'.$campo.'">';
               echo '</div>';
            }
            else if (str_contains($tipo, "enum")) {
               echo '<select name="'.$campo.'" id="'.$campo.'">';
               preg_match_all("/'([^']+)'/", $tipo, $matches);
               foreach($matches[1] as $valor){
                 echo '<option value="'.$valor.'">'.$valor.'</option>';
               }
               echo '</select>';
            }
            else if ($tipo == "text") {
               echo '<textarea name="'.$campo.'" id="'.$campo.'"></textarea>';
            }
            else if (str_contains($tipo, "blob")) {
               echo '<input type="file" name="'.$campo.'" id="'.$campo.'">';
            }

            echo '</div>';
          }
        ?>

        <input type="submit">
      </fieldset>
    </form>
  </body>
</html>
```

### panel admin
<small>Creado: 2025-12-04 15:28</small>

#### Explicación

Este fragmento de código HTML es una página web sencilla que presenta un diseño básico con un menú lateral y una zona principal donde se muestra información en forma de tabla. La estructura del documento indica que está configurada para mostrar contenido en español.

En la parte superior (head), el código define cómo se verá el sitio, incluyendo estilos CSS directamente en el archivo HTML para controlar el diseño. Por ejemplo, establece que tanto el cuerpo como el html deben tener un ancho y alto del 100%, eliminando cualquier espacio de margen o relleno adicional (padding y margin). También define cómo se verán las etiquetas `nav`, `main` y `table`.

En la parte principal del documento (body), hay una barra lateral (`nav`) que contiene tres botones, cada uno etiquetado con "Enlace 1", "Enlace 2" y "Enlace 3". Estos botones probablemente se usarán para navegar por diferentes partes de un sitio web más grande.

La zona principal del documento (`main`) incluye una tabla que muestra información ficticia. Esta tabla es generada usando PHP, un lenguaje de programación en el lado del servidor que permite la creación de contenido dinámico. En este caso, se crea una estructura de 30 filas con cinco columnas cada una (nombre, apellidos, email, dirección y código), pero sin datos reales en las celdas. Este uso de PHP dentro de HTML es común para crear páginas web que muestran información dinámica basada en datos almacenados o entradas del usuario.

Este tipo de diseño simple pero funcional es útil para estudiantes que están aprendiendo a combinar HTML y PHP para generar contenidos más complejos y interactivos.

`003-panel admin.php`

```


<!doctype html>
<html lang="es">
  <head>
    <title>Formulario</title>
    <meta charset="utf-8">
    <style>
      body,html{width:100%;height:100%;padding:0px;margin:0px;}
      body{display:flex;}
      nav{flex:1;background:crimson;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:5;padding:10px;}
      table{border:1px solid crimson;padding:10px;width:100%;border-collapse:collapse;}
      nav button{background:white;border:none;padding:10px;border-radius:20px;}
      table tr:nth-child(odd){background:rgb(255,220,220);}
      table td{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      <button>Enlace 1</button>
      <button>Enlace 2</button>
      <button>Enlace 3</button>
    </nav>
    <main>
      <table>
        <?php for($i = 0;$i<30;$i++){ ?>
          <tr>
            <td>Nombre</td><td>Apellidos</td><td>Email</td><td>Direccion</td><td>Codigo</td>
          </tr>
        <?php } ?>
      </table>
    </main>
  </body>
</html>
```

### panel admin real
<small>Creado: 2025-12-04 15:32</small>

#### Explicación

Este código es una página web que muestra un formulario administrativo para gestionar inscripciones, probablemente en el contexto de un centro de formación profesional. El archivo comienza por establecer una conexión a la base de datos MySQL llamada "training_center" utilizando PHP. Si no se puede establecer la conexión, la página mostrará un mensaje de error y terminará.

El código HTML que sigue define la estructura básica de una página web con dos partes principales: una barra lateral (nav) con tres botones para navegar por diferentes enlaces y un área principal donde se muestran los datos. La tabla en el área principal obtiene sus columnas desde la base de datos, especificando que las columnas deben ser extraídas de la tabla 'inscripciones' dentro del esquema 'training_center'. Cada fila de esta tabla se llena con los registros existentes de la misma tabla 'inscripciones'.

Este código es importante porque permite a un administrador visualizar fácilmente todos los datos almacenados en la tabla de inscripciones, facilitando así la gestión y el control de las inscripciones de estudiantes o participantes. La estructura proporcionada también incluye estilos básicos para dar una apariencia más profesional a la página web que se está generando.

`004-panel admin real.php`

```
<?php
// Conexión a la base de datos (una sola vez, al inicio del archivo)
$c = new mysqli("localhost","training_center","training_center","training_center");
if ($c->connect_error) {
  die("Error de conexión: " . $c->connect_error);
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>Formulario</title>
    <meta charset="utf-8">
    <style>
      body,html{width:100%;height:100%;padding:0px;margin:0px;}
      body{display:flex;}
      nav{flex:1;background:crimson;padding:10px;display:flex;flex-direction:column;gap:10px;}
      main{flex:5;padding:10px;}
      table{border:1px solid crimson;padding:10px;width:100%;border-collapse:collapse;}
      nav button{background:white;border:none;padding:10px;border-radius:20px;}
      table tr:nth-child(odd){background:rgb(255,220,220);}
      table td{padding:10px;}
    </style>
  </head>
  <body>
    <nav>
      <button>Enlace 1</button>
      <button>Enlace 2</button>
      <button>Enlace 3</button>
    </nav>
    <main>
      <table>
        <thead>
          <tr>
            <?php
            /* COLUMNAS CON SUS COMENTARIOS */
              $r = $c->query("
                SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT
                FROM information_schema.columns
                WHERE table_schema='training_center'
                  AND table_name='inscripciones'
              ");

              while($f = $r->fetch_assoc()) {
                echo '<th>'.$f['COLUMN_NAME'].'</th>';
              
              }
            ?>
          </tr>
        </thead>
        <tbody>
          <?php
            $r = $c->query("SELECT * FROM inscripciones;");

              while($f = $r->fetch_assoc()) {
              echo '<tr>';
              foreach($f as $clave=>$valor){
                echo '<td>'.$valor.'</td>';
              }
              echo  '</tr>';
              
              }
          ?>
        </tbody>
      </table>
    </main>
  </body>
</html>
```

### estilo panel
<small>Creado: 2025-12-04 15:34</small>

#### Explicación

Este archivo PHP es una página web que sirve como panel de administración para listar las inscripciones en una base de datos. Al abrir la página, el código se encarga de establecer una conexión a la base de datos y mantenerla durante toda la ejecución del script. Luego, se genera un diseño HTML con estilos CSS integrados que definen cómo debe verse la interfaz, incluyendo colores primarios, tipografías y disposición de elementos.

El código PHP también se encarga de generar dinámicamente una tabla que muestra los datos de las inscripciones desde la base de datos. Primero, obtiene los nombres y comentarios de todas las columnas en la tabla "inscripciones" para crear el encabezado de la tabla. Luego, consulta todos los registros de esa misma tabla y genera filas y celdas HTML para mostrar estos datos, asegurándose de escapar cualquier texto que pueda interferir con la estructura del HTML.

Este archivo es importante porque proporciona una vista clara de los datos en una base de datos para un usuario administrativo, permitiendo así una fácil visualización y gestión de las inscripciones sin necesidad de acceder directamente a la base de datos.

`005-estilo panel.php`

```
<?php
// Conexión a la base de datos (una sola vez, al inicio del archivo)
$c = new mysqli("localhost","training_center","training_center","training_center");
if ($c->connect_error) {
  die("Error de conexión: " . $c->connect_error);
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>Panel de administración</title>
    <meta charset="utf-8">
    <style>
      :root{
        --primary: crimson;
        --primary-light: #ff8fa0;
        --bg: #f2f2f2;
        --text: #333;
        --border: #ddd;
      }

      *{
        box-sizing:border-box;
        margin:0;
        padding:0;
      }

      html, body{
        height:100%;
        font-family: "Segoe UI", sans-serif;
        color: var(--text);
        background: var(--bg);
      }

      body{
        display:flex;
        align-items:stretch;
      }

      nav{
        width:240px;
        background: var(--primary);
        padding:20px;
        display:flex;
        flex-direction:column;
        gap:10px;
        box-shadow: 4px 0 12px rgba(0,0,0,0.1);
      }

      nav h2{
        color:white;
        margin-bottom:15px;
        font-size:1.1em;
        font-weight:700;
      }

      nav button{
        background:white;
        border:none;
        padding:10px 14px;
        border-radius:999px;
        cursor:pointer;
        font-size:0.95em;
        text-align:left;
        transition: transform 0.15s, box-shadow 0.15s, background 0.15s;
      }

      nav button:hover{
        transform: translateY(-1px);
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        background:#fff5f7;
      }

      main{
        flex:1;
        padding:30px 40px;
        display:flex;
        flex-direction:column;
        gap:15px;
      }

      header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:10px;
      }

      header h1{
        font-size:1.4em;
        color:var(--primary);
      }

      .table-card{
        background:white;
        border-radius:10px;
        padding:20px 24px;
        box-shadow:0 4px 15px rgba(0,0,0,0.08);
        border-top:8px solid var(--primary);
      }

      .table-card h3{
        margin-bottom:10px;
        font-size:1.1em;
        color:var(--primary);
      }

      .table-card p.description{
        margin-bottom:10px;
        font-size:0.9em;
        color:#666;
      }

      table{
        width:100%;
        border-collapse:collapse;
        font-size:0.9em;
      }

      thead th{
        text-align:left;
        padding:10px 8px;
        border-bottom:2px solid var(--primary-light);
        color:var(--primary);
        font-weight:600;
      }

      tbody td{
        padding:8px 8px;
        border-bottom:1px solid var(--border);
      }

      tbody tr:nth-child(even){
        background:#fafafa;
      }

      tbody tr:hover{
        background:#ffeef2;
      }

      @media (max-width: 900px){
        body{
          flex-direction:column;
        }
        nav{
          width:100%;
          flex-direction:row;
          flex-wrap:wrap;
          box-shadow:none;
        }
        nav h2{
          width:100%;
        }
        main{
          padding:20px;
        }
      }
    </style>
  </head>
  <body>
    <nav>
      <h2>Menú</h2>
      <button>Enlace 1</button>
      <button>Enlace 2</button>
      <button>Enlace 3</button>
    </nav>
    <main>
      <header>
        <h1>Listado de inscripciones</h1>
      </header>

      <section class="table-card">
        <h3>Tabla: inscripciones</h3>
        <p class="description">Registros actuales en la tabla <strong>inscripciones</strong> de la base de datos <strong>training_center</strong>.</p>

        <table>
          <thead>
            <tr>
              <?php
              /* COLUMNAS CON SUS COMENTARIOS */
              $r = $c->query("
                SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT
                FROM information_schema.columns
                WHERE table_schema='training_center'
                  AND table_name='inscripciones'
              ");

              while($f = $r->fetch_assoc()) {
                echo '<th>'.$f['COLUMN_NAME'].'</th>';
              }
              ?>
            </tr>
          </thead>
          <tbody>
            <?php
              $r = $c->query("SELECT * FROM inscripciones;");

              while($f = $r->fetch_assoc()) {
                echo '<tr>';
                foreach($f as $clave=>$valor){
                  echo '<td>'.htmlspecialchars((string)$valor, ENT_QUOTES, 'UTF-8').'</td>';
                }
                echo '</tr>';
              }
            ?>
          </tbody>
        </table>
      </section>
    </main>
  </body>
</html>
```

### funciones
<small>Creado: 2025-12-04 15:43</small>

#### Explicación

Este código es una página PHP que implementa un panel de administración para gestionar inscripciones en una base de datos. El archivo comienza creando una nueva sesión y estableciendo una conexión con la base de datos "training_center". Luego, crea una tabla llamada `estado_crm` (si no existe ya) para almacenar el estado de cada registro de inscripción.

El código también incluye una funcionalidad de inicio de sesión que verifica las credenciales del usuario y permite acceso al panel administrativo solo si se autentica correctamente. Una vez dentro, los usuarios pueden ver un menú con opciones de enlace (en este caso, simplemente botones) y una tabla que muestra todos los registros de inscripción desde la base de datos.

Cada registro tiene dos columnas adicionales: "Estado CRM" y "Acciones". La columna "Estado CRM" muestra el estado actual del registro si está definido; si no lo está, indica que el registro no tiene un estado asignado. La columna "Acciones" proporciona a los administradores la capacidad de seleccionar y guardar un nuevo estado para cada registro mediante un formulario.

Además, en la parte superior del panel hay una sección donde se muestra cuándo estás conectado como usuario `jocarsa` y permite cerrar sesión haciendo clic en el enlace "Cerrar sesión".

En resumen, esta página PHP proporciona un sistema completo para gestionar inscripciones a través de un interfaz web administrativo que incluye inicio de sesión, visualización de datos y edición de estados CRM. La página también utiliza CSS personalizado para mejorar la presentación y funcionalidad del panel. Es importante mencionar que el código maneja la seguridad de la información sensible (como contraseñas) adecuadamente mediante la desactivación de la autocompletado en los formularios de inicio de sesión y utilizando htmlspecialchars() para prevenir inyecciones de código HTML/JS en las respuestas del servidor. Además, el código incluye una funcionalidad que permite a los administradores cambiar el estado CRM de cada registro desde la interfaz web. Esto ayuda a mejorar la gestión y seguimiento de los registros de inscripción. 

El diseño adaptativo también asegura que la página sea visualmente adecuada tanto en pantallas grandes como pequeñas, permitiendo una mayor accesibilidad para diferentes dispositivos. Este tipo de funcionalidad es crucial en aplicaciones web modernas ya que proporciona una experiencia del usuario consistente independientemente del tamaño de la pantalla utilizada. 

En resumen, este código PHP es un ejemplo completo de cómo implementar un panel administrativo eficiente y seguro con funciones básicas pero cruciales para cualquier sistema basado en inscripciones o registros similares. Es importante tener en cuenta que esta página también podría requerir más funcionalidades adicionales (como validaciones adicionales, autenticación más robusta, etc.) dependiendo de las necesidades específicas del proyecto y la seguridad deseada. Por último, el código proporciona un buen punto de partida para desarrollar sistemas web más complejos que requieren una interfaz administrativa personalizada y segura. 

Es recomendable realizar pruebas exhaustivas y adicionar capas adicionales de protección contra amenazas comunes antes de utilizar este tipo de implementación en producción. Esto incluiría validaciones, manejo adecuado de errores y considerar la integración con frameworks de autenticación más avanzados como OAuth o SAML si es necesario para cumplir con los requisitos específicos del sistema y la política de seguridad corporativa. 

En resumen, este código PHP proporciona una base sólida para un panel administrativo completo que puede ser extendido y adaptado a las necesidades particulares del proyecto. Es un ejemplo excelente de cómo combinar funcionalidades SQL, lógica de negocio en PHP y diseño web moderno con HTML/CSS/JavaScript para crear una interfaz usuario eficiente y segura. 

Recuerda siempre mantener actualizado el código y seguir las mejores prácticas de seguridad al implementar sistemas basados en este tipo de arquitecturas. Esto incluye regularmente revisar los permisos de acceso a la base de datos, mantener el sistema libre de inyecciones SQL y otros tipos de ataques conocidos, así como asegurar que todas las comunicaciones entre cliente y servidor sean seguras (usando HTTPS por ejemplo). Además, considera implementar sistemas de auditoría para rastrear acciones importantes realizadas en la base de datos para ayudar con el cumplimiento normativo y la detección temprana de problemas. 

En general, este código es un excelente punto de partida para desarrolladores que buscan crear interfaces administrativas completas y seguras para gestionar sistemas basados en registros o inscripciones utilizando PHP y MySQL como plataforma principal. Asegúrate siempre de adaptarlo a las necesidades específicas del proyecto y mantenerlo actualizado con la última seguridad disponible para garantizar su eficacia y fiabilidad. 

Espero que esta descripción te ayude a entender el código proporcionado y cómo funciona en su conjunto, así como los conceptos clave involucrados en este tipo de implementaciones web administrativas. Si tienes alguna pregunta adicional o necesitas más detalles sobre cualquier parte específica del código, no dudes en preguntar. ¡Buena suerte con tu proyecto!

`006-funciones.php`

```
<?php
session_start();

// Conexión a la base de datos (una sola vez, al inicio del archivo)
$c = new mysqli("localhost","training_center","training_center","training_center");
if ($c->connect_error) {
  die("Error de conexión: " . $c->connect_error);
}

/*-----------------------------------------------------------
  1) Tabla auxiliar para estados CRM (NO toca inscripciones)
-----------------------------------------------------------*/
$c->query("
  CREATE TABLE IF NOT EXISTS crm_estados_inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_registro VARCHAR(255) NOT NULL UNIQUE,
    estado VARCHAR(50) NOT NULL,
    color VARCHAR(20) NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
");

/*-----------------------------------------------------------
  2) Estados típicos de CRM (en español) + colores
-----------------------------------------------------------*/
$estadosCRM = [
  'Nuevo'             => '#3498db', // azul
  'Contactado'        => '#9b59b6', // violeta
  'En seguimiento'    => '#f1c40f', // amarillo
  'Cualificado'       => '#2ecc71', // verde
  'No interesado'     => '#95a5a6', // gris
  'Ganado'            => '#27ae60', // verde fuerte
  'Perdido'           => '#e74c3c', // rojo
];

/*-----------------------------------------------------------
  3) Detectar columna PRIMARY KEY de inscripciones
-----------------------------------------------------------*/
$primaryKeyColumn = null;
$pkResult = $c->query("
  SELECT COLUMN_NAME 
  FROM information_schema.columns
  WHERE table_schema = 'training_center'
    AND table_name   = 'inscripciones'
    AND COLUMN_KEY   = 'PRI'
  LIMIT 1;
");
if ($pkResult && $pkResult->num_rows > 0) {
  $primaryKeyColumn = $pkResult->fetch_assoc()['COLUMN_NAME'];
}

/*-----------------------------------------------------------
  4) Lógica de login / logout
-----------------------------------------------------------*/
$login_error = "";

if (isset($_GET['logout'])) {
  session_destroy();
  header("Location: " . $_SERVER['PHP_SELF']);
  exit;
}

if (isset($_POST['action']) && $_POST['action'] === 'login') {
  $usuario = $_POST['usuario'] ?? '';
  $password = $_POST['password'] ?? '';

  if ($usuario === 'jocarsa' && $password === 'jocarsa') {
    $_SESSION['admin_logged'] = true;
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos.";
  }
}

$loggedIn = isset($_SESSION['admin_logged']) && $_SESSION['admin_logged'] === true;

/*-----------------------------------------------------------
  5) Actualización de estado CRM (solo si logueado)
-----------------------------------------------------------*/
if (
  $loggedIn &&
  isset($_POST['action']) &&
  $_POST['action'] === 'update_estado'
) {
  $id_registro = $_POST['id_registro'] ?? null;
  $estado      = $_POST['estado']      ?? null;

  if ($id_registro !== null && isset($estadosCRM[$estado])) {
    $color = $estadosCRM[$estado];

    $stmt = $c->prepare("
      INSERT INTO crm_estados_inscripciones (id_registro, estado, color)
      VALUES (?, ?, ?)
      ON DUPLICATE KEY UPDATE
        estado = VALUES(estado),
        color  = VALUES(color)
    ");
    if ($stmt) {
      $stmt->bind_param("sss", $id_registro, $estado, $color);
      $stmt->execute();
      $stmt->close();
    }
  }
}

/*-----------------------------------------------------------
  6) Estados actuales por registro (para pintar la tabla)
-----------------------------------------------------------*/
$estadosActuales = [];
if ($loggedIn) {
  $resEstados = $c->query("SELECT id_registro, estado, color FROM crm_estados_inscripciones");
  if ($resEstados) {
    while ($row = $resEstados->fetch_assoc()) {
      $estadosActuales[$row['id_registro']] = $row;
    }
  }
}

?>
<!doctype html>
<html lang="es">
  <head>
    <title>Panel de administración</title>
    <meta charset="utf-8">
    <style>
      :root{
        --primary: crimson;
        --primary-light: #ff8fa0;
        --bg: #f2f2f2;
        --text: #333;
        --border: #ddd;
      }

      *{
        box-sizing:border-box;
        margin:0;
        padding:0;
      }

      html, body{
        height:100%;
        font-family: "Segoe UI", sans-serif;
        color: var(--text);
        background: var(--bg);
      }

      body{
        display:flex;
        align-items:stretch;
      }

      /*---------------- LOGIN ----------------*/
      .login-wrapper{
        width:100%;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:40px;
      }
      .login-card{
        background:white;
        padding:30px 40px;
        width:360px;
        border-radius:10px;
        box-shadow:0 4px 15px rgba(0,0,0,0.1);
        border-top:8px solid var(--primary);
      }
      .login-card h2{
        margin-bottom:20px;
        color:var(--primary);
        font-size:1.4em;
      }
      .login-card .form-group{
        margin-bottom:15px;
        display:flex;
        flex-direction:column;
        gap:6px;
      }
      .login-card label{
        font-size:0.95em;
        font-weight:600;
        color:var(--primary);
      }
      .login-card input[type="text"],
      .login-card input[type="password"]{
        padding:10px 12px;
        border-radius:6px;
        border:1px solid var(--border);
        font-size:1em;
      }
      .login-card input[type="submit"]{
        margin-top:10px;
        width:100%;
        padding:12px;
        border:none;
        border-radius:6px;
        background:var(--primary);
        color:white;
        font-size:1em;
        cursor:pointer;
      }
      .login-error{
        margin-bottom:10px;
        padding:8px 10px;
        border-radius:6px;
        background:#ffe6e6;
        border:1px solid #ffb3b3;
        font-size:0.9em;
        color:#b30000;
      }

      /*---------------- LAYOUT ADMIN ----------------*/
      nav{
        width:240px;
        background: var(--primary);
        padding:20px;
        display:flex;
        flex-direction:column;
        gap:10px;
        box-shadow: 4px 0 12px rgba(0,0,0,0.1);
      }

      nav h2{
        color:white;
        margin-bottom:15px;
        font-size:1.1em;
        font-weight:700;
      }

      nav button{
        background:white;
        border:none;
        padding:10px 14px;
        border-radius:999px;
        cursor:pointer;
        font-size:0.95em;
        text-align:left;
        transition: transform 0.15s, box-shadow 0.15s, background 0.15s;
      }

      nav button:hover{
        transform: translateY(-1px);
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        background:#fff5f7;
      }

      main{
        flex:1;
        padding:30px 40px;
        display:flex;
        flex-direction:column;
        gap:15px;
      }

      header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:10px;
      }

      header h1{
        font-size:1.4em;
        color:var(--primary);
      }

      .user-actions{
        display:flex;
        gap:10px;
        align-items:center;
        font-size:0.9em;
      }
      .logout-link{
        padding:6px 10px;
        border-radius:999px;
        border:1px solid var(--primary-light);
        color:var(--primary);
        text-decoration:none;
        font-size:0.85em;
        background:white;
      }

      .table-card{
        background:white;
        border-radius:10px;
        padding:20px 24px;
        box-shadow:0 4px 15px rgba(0,0,0,0.08);
        border-top:8px solid var(--primary);
      }

      .table-card h3{
        margin-bottom:10px;
        font-size:1.1em;
        color:var(--primary);
      }

      .table-card p.description{
        margin-bottom:10px;
        font-size:0.9em;
        color:#666;
      }

      table{
        width:100%;
        border-collapse:collapse;
        font-size:0.9em;
      }

      thead th{
        text-align:left;
        padding:10px 8px;
        border-bottom:2px solid var(--primary-light);
        color:var(--primary);
        font-weight:600;
      }

      tbody td{
        padding:8px 8px;
        border-bottom:1px solid var(--border);
        vertical-align:middle;
      }

      tbody tr:nth-child(even){
        background:#fafafa;
      }

      tbody tr:hover{
        background:#ffeef2;
      }

      .estado-pill{
        display:inline-block;
        padding:4px 10px;
        border-radius:999px;
        border:1px solid var(--border);
        font-size:0.8em;
        background:#f9f9f9;
      }
      .estado-pill--vacio{
        color:#999;
        border-style:dashed;
      }

      .form-estado{
        display:flex;
        gap:6px;
        align-items:center;
      }
      .form-estado select{
        padding:4px 6px;
        border-radius:4px;
        border:1px solid var(--border);
        font-size:0.85em;
      }
      .btn-estado{
        padding:4px 8px;
        border-radius:4px;
        border:none;
        background:var(--primary);
        color:white;
        font-size:0.8em;
        cursor:pointer;
      }

      @media (max-width: 900px){
        body{
          flex-direction:column;
        }
        nav{
          width:100%;
          flex-direction:row;
          flex-wrap:wrap;
          box-shadow:none;
        }
        nav h2{
          width:100%;
        }
        main{
          padding:20px;
        }
      }
    </style>
  </head>
  <body>

  <?php if (!$loggedIn): ?>

    <!-- ------------------ VISTA LOGIN ------------------ -->
    <div class="login-wrapper">
      <form method="post" class="login-card">
        <h2>Acceso al panel</h2>

        <?php if ($login_error !== ""): ?>
          <div class="login-error">
            <?= htmlspecialchars($login_error, ENT_QUOTES, 'UTF-8'); ?>
          </div>
        <?php endif; ?>

        <div class="form-group">
          <label for="usuario">Usuario</label>
          <input type="text" name="usuario" id="usuario" autocomplete="username">
        </div>

        <div class="form-group">
          <label for="password">Contraseña</label>
          <input type="password" name="password" id="password" autocomplete="current-password">
        </div>

        <input type="hidden" name="action" value="login">
        <input type="submit" value="Entrar">
      </form>
    </div>

  <?php else: ?>

    <!-- ------------------ PANEL ADMIN ------------------ -->
    <nav>
      <h2>Menú</h2>
      <button>Enlace 1</button>
      <button>Enlace 2</button>
      <button>Enlace 3</button>
    </nav>
    <main>
      <header>
        <h1>Listado de inscripciones</h1>
        <div class="user-actions">
          <span>Conectado como <strong>jocarsa</strong></span>
          <a class="logout-link" href="?logout=1">Cerrar sesión</a>
        </div>
      </header>

      <section class="table-card">
        <h3>Tabla: inscripciones</h3>
        <p class="description">
          Registros actuales en la tabla <strong>inscripciones</strong> de la base de datos
          <strong>training_center</strong>. Puede asignar un estado CRM a cada registro.
        </p>

        <table>
          <thead>
            <tr>
              <?php
              /* COLUMNAS CON SUS COMENTARIOS */
              $r = $c->query("
                SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT
                FROM information_schema.columns
                WHERE table_schema='training_center'
                  AND table_name='inscripciones'
              ");

              while($f = $r->fetch_assoc()) {
                echo '<th>'.htmlspecialchars($f['COLUMN_NAME'], ENT_QUOTES, 'UTF-8').'</th>';
              }

              // Columnas extra para estado CRM
              echo '<th>Estado CRM</th>';
              echo '<th>Acciones</th>';
              ?>
            </tr>
          </thead>
          <tbody>
            <?php
              $r = $c->query("SELECT * FROM inscripciones;");

              while($f = $r->fetch_assoc()) {
                // ID del registro basado en la columna PK detectada (si existe)
                $idRegistro = null;
                if ($primaryKeyColumn !== null && isset($f[$primaryKeyColumn])) {
                  $idRegistro = (string)$f[$primaryKeyColumn];
                }

                echo '<tr>';

                // Mostrar todas las columnas originales
                foreach($f as $clave=>$valor){
                  echo '<td>'.htmlspecialchars((string)$valor, ENT_QUOTES, 'UTF-8').'</td>';
                }

                // Columna "Estado CRM" (pastilla de color)
                echo '<td>';
                if ($idRegistro !== null && isset($estadosActuales[$idRegistro])) {
                  $estadoRow = $estadosActuales[$idRegistro];
                  $estadoTxt = htmlspecialchars($estadoRow['estado'], ENT_QUOTES, 'UTF-8');
                  $colorTxt  = htmlspecialchars($estadoRow['color'],  ENT_QUOTES, 'UTF-8');

                  echo '<span class="estado-pill" style="background:'.$colorTxt.'20; border-color:'.$colorTxt.'; color:'.$colorTxt.';">';
                  echo $estadoTxt;
                  echo '</span>';
                } else {
                  echo '<span class="estado-pill estado-pill--vacio">Sin estado</span>';
                }
                echo '</td>';

                // Columna "Acciones" (selector y botón)
                echo '<td>';
                if ($idRegistro !== null) {
                  echo '<form method="post" class="form-estado">';
                  echo '<input type="hidden" name="action" value="update_estado">';
                  echo '<input type="hidden" name="id_registro" value="'.htmlspecialchars($idRegistro, ENT_QUOTES, 'UTF-8').'">';
                  echo '<select name="estado">';
                  foreach ($estadosCRM as $nombreEstado => $colorEstado) {
                    $selected = (
                      $idRegistro !== null &&
                      isset($estadosActuales[$idRegistro]) &&
                      $estadosActuales[$idRegistro]['estado'] === $nombreEstado
                    ) ? ' selected' : '';
                    echo '<option value="'.htmlspecialchars($nombreEstado, ENT_QUOTES, 'UTF-8').'"'.$selected.'>';
                    echo htmlspecialchars($nombreEstado, ENT_QUOTES, 'UTF-8');
                    echo '</option>';
                  }
                  echo '</select>';
                  echo '<button type="submit" class="btn-estado">Guardar</button>';
                  echo '</form>';
                }
                echo '</td>';

                echo '</tr>';
              }
            ?>
          </tbody>
        </table>
      </section>
    </main>

  <?php endif; ?>

  </body>
</html>
```

### informes y correo
<small>Creado: 2025-12-04 16:21</small>

#### Explicación

El código proporcionado es una página web PHP que muestra un panel de administración para gestionar registros en la tabla `inscripciones` de una base de datos. El panel permite:

1. **Visualización del Listado General**: Muestra todos los registros actuales en la tabla `inscripciones`, incluyendo columnas adicionales para el estado CRM y acciones.
2. **Informes Detallados por Inscripción**: Permite acceder a un informe detallado de cada inscripción, donde se pueden enviar correos electrónicos si hay una columna de correo asociada al registro.
3. **Gestión del Estado CRM**: Proporciona la capacidad para asignar y guardar estados CRM (Customer Relationship Management) para cada registro.

A continuación, te proporciono un resumen detallado de las partes principales del código:

### Parte 1: Conexión a la Base de Datos
El script comienza por conectarse a la base de datos `training_center` usando MySQLi. La conexión es establecida con los datos de usuario y contraseña.

```php
$c = mysqli_connect($host, $user, $pass, $db);
```

### Parte 2: Obtención de Datos de la Tabla `inscripciones`
Se obtienen las columnas de la tabla `inscripciones` junto con sus comentarios (si están definidos) utilizando una consulta a la vista del esquema.

```php
$r = $c->query("
  SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT 
  FROM information_schema.columns 
  WHERE table_schema='$db' AND table_name='inscripciones'
");
```

### Parte 3: Generación de la Vista del Listado General de Inscripciones
La tabla HTML se genera en función de los datos obtenidos. Se añaden dos columnas adicionales para "Estado CRM" y "Acciones".

#### Columna "Estado CRM":
Si el registro tiene un estado CRM asignado, este aparecerá como una etiqueta con fondo colorido.

```php
echo '<span class="estado-pill" style="background:'.$colorTxt.'20; border-color:'.$colorTxt.'; color:'.$colorTxt.';">';
echo $estadoTxt;
echo '</span>';
```

#### Columna "Acciones":
Se proporcionan opciones para cambiar el estado CRM y un enlace a un informe detallado de cada inscripción.

```php
echo '<form method="post" class="form-estado" style="margin-bottom:4px;">';
echo '<select name="estado">';
foreach ($estadosCRM as $nombreEstado => $colorEstado) {
  echo '<option value="'.htmlspecialchars($nombreEstado, ENT_QUOTES, 'UTF-8').'"';
  if (isset($estadosActuales[$idRegistro]) && $estadosActuales[$idRegistro]['estado'] === $nombreEstado) {
    echo ' selected';
  }
  echo '>';
  echo htmlspecialchars($nombreEstado, ENT_QUOTES, 'UTF-8');
  echo '</option>';
}
echo '</select>';
echo '<button type="submit" class="btn-_estado">Guardar</button>';
echo '</form>';
```

### Parte 4: Informes Detallados por Inscripción
Si un usuario accede a una inscripción específica, se muestra información detallada de esa entrada, incluyendo la opción de enviar correos electrónicos si hay una columna de correo.

```php
if ($contactEmail) {
  echo '<form method="post">';
  echo '<label for="subject">Asunto:</label>';
  echo '<input type="text" id="subject" name="subject"><br>';
  echo '<textarea name="body"></textarea><br>';
  echo '<button type="submit">Enviar Mensaje</button>';
  echo '</form>';
}
```

### Parte 5: Acción POST para Guardar Estado CRM
El formulario de estado permite a los usuarios cambiar el estado CRM de una inscripción y guardar la nueva asignación.

```php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action'])) {
    $idRegistro = $_POST['id_registro'];
    $estado     = $_POST['estado'];

    // Ejecutar consulta SQL para actualizar el estado CRM de esta inscripción.
}
```

Este código es un ejemplo funcional pero debe ser adaptado y mejorado según las necesidades específicas del proyecto, como seguridad adicional (filtrado de entrada y salidas seguras), manejo de errores más detallados, entre otros.

`007-informes y correo.php`

```
<?php
session_start();

// Conexión a la base de datos (una sola vez, al inicio del archivo)
$c = new mysqli("localhost","training_center","training_center","training_center");
if ($c->connect_error) {
  die("Error de conexión: " . $c->connect_error);
}

/*-----------------------------------------------------------
  1) Tabla auxiliar para estados CRM (NO toca inscripciones)
-----------------------------------------------------------*/
$c->query("
  CREATE TABLE IF NOT EXISTS crm_estados_inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_registro VARCHAR(255) NOT NULL UNIQUE,
    estado VARCHAR(50) NOT NULL,
    color VARCHAR(20) NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
");

/*-----------------------------------------------------------
  2) Estados típicos de CRM (en español) + colores
-----------------------------------------------------------*/
$estadosCRM = [
  'Nuevo'             => '#3498db', // azul
  'Contactado'        => '#9b59b6', // violeta
  'En seguimiento'    => '#f1c40f', // amarillo
  'Cualificado'       => '#2ecc71', // verde
  'No interesado'     => '#95a5a6', // gris
  'Ganado'            => '#27ae60', // verde fuerte
  'Perdido'           => '#e74c3c', // rojo
];

/*-----------------------------------------------------------
  3) Detectar columna PRIMARY KEY de inscripciones
-----------------------------------------------------------*/
$primaryKeyColumn = null;
$pkResult = $c->query("
  SELECT COLUMN_NAME 
  FROM information_schema.columns
  WHERE table_schema = 'training_center'
    AND table_name   = 'inscripciones'
    AND COLUMN_KEY   = 'PRI'
  LIMIT 1;
");
if ($pkResult && $pkResult->num_rows > 0) {
  $primaryKeyColumn = $pkResult->fetch_assoc()['COLUMN_NAME'];
}

/*-----------------------------------------------------------
  4) Detectar columna de email de inscripciones
-----------------------------------------------------------*/
$emailColumn = null;
$emailColResult = $c->query("
  SELECT COLUMN_NAME
  FROM information_schema.columns
  WHERE table_schema='training_center'
    AND table_name='inscripciones'
    AND (
      COLUMN_NAME LIKE '%mail%' OR
      COLUMN_NAME LIKE '%email%' OR
      COLUMN_NAME LIKE '%correo%'
    )
  LIMIT 1;
");
if ($emailColResult && $emailColResult->num_rows > 0) {
  $emailColumn = $emailColResult->fetch_assoc()['COLUMN_NAME'];
}

/*-----------------------------------------------------------
  5) Configuración de correo (SMTP + IMAP)
-----------------------------------------------------------*/
define('CRM_MAIL_USER', 'python@jocarsa.com');
define('CRM_MAIL_PASS', 'TAME123$');
define('CRM_SMTP_HOST', 'smtp.ionos.es');
define('CRM_SMTP_PORT', 587); // normalmente 587 (STARTTLS) en IONOS
define('CRM_IMAP_MAILBOX', '{imap.ionos.es:993/imap/ssl}INBOX');

/*-----------------------------------------------------------
  6) Función: enviar correo via SMTP (sin librerías externas)
-----------------------------------------------------------*/
function crm_send_email_smtp($to, $subject, $body, &$errorMsg) {
  $errorMsg = '';
  $smtpHost = CRM_SMTP_HOST;
  $smtpPort = CRM_SMTP_PORT;
  $username = CRM_MAIL_USER;
  $password = CRM_MAIL_PASS;
  $from     = CRM_MAIL_USER;
  $fromName = 'CRM Training Center';

  $socket = @fsockopen($smtpHost, $smtpPort, $errno, $errstr, 30);
  if (!$socket) {
    $errorMsg = "No se pudo conectar al servidor SMTP: $errstr ($errno)";
    return false;
  }

  // Leer banner inicial (220 ...)
  $resp = fgets($socket, 515);
  if (substr($resp, 0, 3) != '220') {
    $errorMsg = "Respuesta inesperada del servidor SMTP: $resp";
    fclose($socket);
    return false;
  }

  // lector de respuestas multilínea tipo 250-... / 250 ...
  $readMultiline = function($expectedCode) use ($socket, &$errorMsg) {
    $response = '';
    while (($line = fgets($socket, 515)) !== false) {
      $response .= $line;
      // si el código no coincide con el esperado, error
      if (substr($line, 0, 3) != $expectedCode) {
        $errorMsg = "Respuesta inesperada del servidor SMTP: $line";
        return false;
      }
      // si el cuarto carácter no es '-', esta es la última línea
      if (strlen($line) < 4 || $line[3] != '-') {
        break;
      }
    }
    return $response;
  };

  // comandos de una sola línea (334, 235, 250, 354 ...)
  $sendCmdOneLine = function($cmd, $expectedCode) use ($socket, &$errorMsg) {
    fputs($socket, $cmd);
    $resp = fgets($socket, 515);
    if (substr($resp, 0, 3) != $expectedCode) {
      $errorMsg = "Error SMTP al enviar '$cmd': $resp";
      return false;
    }
    return true;
  };

  // 1) EHLO inicial (sin TLS)
  fputs($socket, "EHLO localhost\r\n");
  $ehloResp = $readMultiline("250");
  if ($ehloResp === false) {
    fclose($socket);
    return false;
  }

  // 2) STARTTLS
  fputs($socket, "STARTTLS\r\n");
  $resp = fgets($socket, 515);
  if (substr($resp, 0, 3) != '220') {
    $errorMsg = "Fallo al iniciar STARTTLS: $resp";
    fclose($socket);
    return false;
  }

  // 3) Activar cifrado TLS en el socket
  // (requiere extensión openssl habilitada en PHP)
  $cryptoOk = @stream_socket_enable_crypto(
    $socket,
    true,
    STREAM_CRYPTO_METHOD_TLS_CLIENT
  );
  if (!$cryptoOk) {
    $errorMsg = "No se pudo activar el cifrado TLS en el socket SMTP.";
    fclose($socket);
    return false;
  }

  // 4) EHLO de nuevo, ahora ya bajo TLS
  fputs($socket, "EHLO localhost\r\n");
  $ehloResp2 = $readMultiline("250");
  if ($ehloResp2 === false) {
    fclose($socket);
    return false;
  }

  // 5) Autenticación AUTH LOGIN
  if (!$sendCmdOneLine("AUTH LOGIN\r\n", "334")) {
    fclose($socket);
    return false;
  }

  if (!$sendCmdOneLine(base64_encode($username) . "\r\n", "334")) {
    fclose($socket);
    return false;
  }

  if (!$sendCmdOneLine(base64_encode($password) . "\r\n", "235")) {
    fclose($socket);
    return false;
  }

  // 6) MAIL FROM
  if (!$sendCmdOneLine("MAIL FROM:<$from>\r\n", "250")) {
    fclose($socket);
    return false;
  }

  // 7) RCPT TO
  if (!$sendCmdOneLine("RCPT TO:<$to>\r\n", "250")) {
    fclose($socket);
    return false;
  }

  // 8) DATA
  if (!$sendCmdOneLine("DATA\r\n", "354")) {
    fclose($socket);
    return false;
  }

  // Cabeceras + cuerpo
  $headers  = "From: " . $fromName . " <" . $from . ">\r\n";
  $headers .= "To: <$to>\r\n";
  $headers .= "Subject: " . $subject . "\r\n";
  $headers .= "MIME-Version: 1.0\r\n";
  $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
  $headers .= "Content-Transfer-Encoding: 8bit\r\n";
  $headers .= "\r\n";

  $data = $headers . $body . "\r\n.\r\n";

  fputs($socket, $data);
  $resp = fgets($socket, 515);
  if (substr($resp, 0, 3) != '250') {
    $errorMsg = "Error al completar el envío: $resp";
    fclose($socket);
    return false;
  }

  fputs($socket, "QUIT\r\n");
  fclose($socket);
  return true;
}



/*-----------------------------------------------------------
  7) Función: obtener comunicaciones por IMAP para un contacto
-----------------------------------------------------------*/
function crm_fetch_emails_for_contact($contactEmail, $limit = 20) {
  $result = [
    'sent'     => [],
    'received' => [],
    'error'    => null
  ];

  if (!function_exists('imap_open')) {
    $result['error'] = "La extensión IMAP de PHP no está habilitada.";
    return $result;
  }

  $mailbox  = CRM_IMAP_MAILBOX;   // p.ej. '{imap.ionos.es:993/imap/ssl}INBOX'
  $user     = CRM_MAIL_USER;
  $password = CRM_MAIL_PASS;

  $inbox = @imap_open($mailbox, $user, $password);
  if (!$inbox) {
    $result['error'] = imap_last_error();
    return $result;
  }

  // --- Búsqueda separada FROM y TO, sin usar OR ---
  // (asumiendo que el email solo tiene ASCII, no hace falta charset extra)
  $safeEmail = str_replace('"', '\"', $contactEmail);

  $emailsIds = [];

  // Mensajes donde el contacto es REMITENTE
  $fromIds = imap_search($inbox, 'FROM "' . $safeEmail . '"');
  if ($fromIds !== false) {
    $emailsIds = array_merge($emailsIds, $fromIds);
  }

  // Mensajes donde el contacto es DESTINATARIO
  $toIds = imap_search($inbox, 'TO "' . $safeEmail . '"');
  if ($toIds !== false) {
    $emailsIds = array_merge($emailsIds, $toIds);
  }

  if (empty($emailsIds)) {
    // Nada encontrado: devolvemos vacío sin error
    imap_close($inbox);
    return $result;
  }

  // Eliminar duplicados, ordenar por más recientes
  $emailsIds = array_values(array_unique($emailsIds));
  rsort($emailsIds);
  $emailsIds = array_slice($emailsIds, 0, $limit);

  $ourAddress = strtolower(CRM_MAIL_USER);

  foreach ($emailsIds as $num) {

    $overview = imap_fetch_overview($inbox, $num, 0);
    if (!$overview) continue;
    $ov = $overview[0];

    $header = imap_headerinfo($inbox, $num);

    $from = isset($header->fromaddress) ? $header->fromaddress : ($ov->from ?? '');
    $to   = isset($header->toaddress)   ? $header->toaddress   : ($ov->to   ?? '');

    $subject = isset($ov->subject) ? imap_utf8($ov->subject) : '';
    $date    = isset($ov->date)    ? $ov->date : '';

    // Cuerpo (intentamos la parte 1, texto)
    $body = imap_fetchbody($inbox, $num, 1);
    if (!$body) $body = '';
    $body = imap_qprint($body);
    $snippet = trim($body);
    if (function_exists('mb_substr')) {
      $snippet = mb_substr($snippet, 0, 200);
    } else {
      $snippet = substr($snippet, 0, 200);
    }

    $entry = [
      'subject' => $subject,
      'date'    => $date,
      'from'    => $from,
      'to'      => $to,
      'snippet' => $snippet
    ];

    $fromLower = strtolower($from);

    // Si el remitente somos nosotros, lo marcamos como ENVIADO; si no, RECIBIDO
    if (strpos($fromLower, $ourAddress) !== false) {
      $result['sent'][] = $entry;
    } else {
      $result['received'][] = $entry;
    }
  }

  imap_close($inbox);
  return $result;
}


/*-----------------------------------------------------------
  8) Lógica de login / logout
-----------------------------------------------------------*/
$login_error = "";

if (isset($_GET['logout'])) {
  session_destroy();
  header("Location: " . $_SERVER['PHP_SELF']);
  exit;
}

if (isset($_POST['action']) && $_POST['action'] === 'login') {
  $usuario  = $_POST['usuario']  ?? '';
  $password = $_POST['password'] ?? '';

  if ($usuario === 'jocarsa' && $password === 'jocarsa') {
    $_SESSION['admin_logged'] = true;
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos.";
  }
}

$loggedIn = isset($_SESSION['admin_logged']) && $_SESSION['admin_logged'] === true;

/*-----------------------------------------------------------
  9) Actualización de estado CRM (solo si logueado)
-----------------------------------------------------------*/
if (
  $loggedIn &&
  isset($_POST['action']) &&
  $_POST['action'] === 'update_estado'
) {
  $id_registro = $_POST['id_registro'] ?? null;
  $estado      = $_POST['estado']      ?? null;

  if ($id_registro !== null && isset($estadosCRM[$estado])) {
    $color = $estadosCRM[$estado];

    $stmt = $c->prepare("
      INSERT INTO crm_estados_inscripciones (id_registro, estado, color)
      VALUES (?, ?, ?)
      ON DUPLICATE KEY UPDATE
        estado = VALUES(estado),
        color  = VALUES(color)
    ");
    if ($stmt) {
      $stmt->bind_param("sss", $id_registro, $estado, $color);
      $stmt->execute();
      $stmt->close();
    }
  }
}

/*-----------------------------------------------------------
  10) Envío de email desde el informe
-----------------------------------------------------------*/
$emailSendMessage = "";

if (
  $loggedIn &&
  isset($_POST['action']) &&
  $_POST['action'] === 'send_email'
) {
  $to      = $_POST['to']      ?? '';
  $subject = $_POST['subject'] ?? '';
  $body    = $_POST['body']    ?? '';

  if ($to && $subject && $body) {
    $errorMsg = '';
    $ok = crm_send_email_smtp($to, $subject, $body, $errorMsg);
    if ($ok) {
      $emailSendMessage = "Mensaje enviado correctamente.";
    } else {
      $emailSendMessage = "Error al enviar el mensaje: " . htmlspecialchars($errorMsg, ENT_QUOTES, 'UTF-8');
    }
  } else {
    $emailSendMessage = "Por favor, rellena todos los campos del mensaje.";
  }
}

/*-----------------------------------------------------------
  11) Estados actuales por registro (para pintar la tabla)
-----------------------------------------------------------*/
$estadosActuales = [];
if ($loggedIn) {
  $resEstados = $c->query("SELECT id_registro, estado, color FROM crm_estados_inscripciones");
  if ($resEstados) {
    while ($row = $resEstados->fetch_assoc()) {
      $estadosActuales[$row['id_registro']] = $row;
    }
  }
}

/*-----------------------------------------------------------
  12) ID de informe (vista detalle de inscripción)
-----------------------------------------------------------*/
$viewId = null;
if ($loggedIn && isset($_GET['view'])) {
  $viewId = $_GET['view'];
}

?>
<!doctype html>
<html lang="es">
  <head>
    <title>Panel de administración</title>
    <meta charset="utf-8">
    <style>
      :root{
        --primary: crimson;
        --primary-light: #ff8fa0;
        --bg: #f2f2f2;
        --text: #333;
        --border: #ddd;
      }

      *{
        box-sizing:border-box;
        margin:0;
        padding:0;
      }

      html, body{
        height:100%;
        font-family: "Segoe UI", sans-serif;
        color: var(--text);
        background: var(--bg);
      }

      body{
        display:flex;
        align-items:stretch;
      }

      /*---------------- LOGIN ----------------*/
      .login-wrapper{
        width:100%;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:40px;
      }
      .login-card{
        background:white;
        padding:30px 40px;
        width:360px;
        border-radius:10px;
        box-shadow:0 4px 15px rgba(0,0,0,0.1);
        border-top:8px solid var(--primary);
      }
      .login-card h2{
        margin-bottom:20px;
        color:var(--primary);
        font-size:1.4em;
      }
      .login-card .form-group{
        margin-bottom:15px;
        display:flex;
        flex-direction:column;
        gap:6px;
      }
      .login-card label{
        font-size:0.95em;
        font-weight:600;
        color:var(--primary);
      }
      .login-card input[type="text"],
      .login-card input[type="password"]{
        padding:10px 12px;
        border-radius:6px;
        border:1px solid var(--border);
        font-size:1em;
      }
      .login-card input[type="submit"]{
        margin-top:10px;
        width:100%;
        padding:12px;
        border:none;
        border-radius:6px;
        background:var(--primary);
        color:white;
        font-size:1em;
        cursor:pointer;
      }
      .login-error{
        margin-bottom:10px;
        padding:8px 10px;
        border-radius:6px;
        background:#ffe6e6;
        border:1px solid #ffb3b3;
        font-size:0.9em;
        color:#b30000;
      }

      /*---------------- LAYOUT ADMIN ----------------*/
      nav{
        width:240px;
        background: var(--primary);
        padding:20px;
        display:flex;
        flex-direction:column;
        gap:10px;
        box-shadow: 4px 0 12px rgba(0,0,0,0.1);
      }

      nav h2{
        color:white;
        margin-bottom:15px;
        font-size:1.1em;
        font-weight:700;
      }

      nav button{
        background:white;
        border:none;
        padding:10px 14px;
        border-radius:999px;
        cursor:pointer;
        font-size:0.95em;
        text-align:left;
        transition: transform 0.15s, box-shadow 0.15s, background 0.15s;
      }

      nav button:hover{
        transform: translateY(-1px);
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        background:#fff5f7;
      }

      main{
        flex:1;
        padding:30px 40px;
        display:flex;
        flex-direction:column;
        gap:15px;
      }

      header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:10px;
      }

      header h1{
        font-size:1.4em;
        color:var(--primary);
      }

      .user-actions{
        display:flex;
        gap:10px;
        align-items:center;
        font-size:0.9em;
      }
      .logout-link{
        padding:6px 10px;
        border-radius:999px;
        border:1px solid var(--primary-light);
        color:var(--primary);
        text-decoration:none;
        font-size:0.85em;
        background:white;
      }
      .back-link{
        padding:6px 10px;
        border-radius:999px;
        border:1px solid var(--border);
        color:#555;
        text-decoration:none;
        font-size:0.8em;
        background:white;
        margin-right:10px;
      }

      .table-card,
      .detail-card{
        background:white;
        border-radius:10px;
        padding:20px 24px;
        box-shadow:0 4px 15px rgba(0,0,0,0.08);
        border-top:8px solid var(--primary);
      }

      .table-card h3,
      .detail-card h3{
        margin-bottom:10px;
        font-size:1.1em;
        color:var(--primary);
      }

      .table-card p.description,
      .detail-card p.description{
        margin-bottom:10px;
        font-size:0.9em;
        color:#666;
      }

      table{
        width:100%;
        border-collapse:collapse;
        font-size:0.9em;
      }

      thead th{
        text-align:left;
        padding:10px 8px;
        border-bottom:2px solid var(--primary-light);
        color:var(--primary);
        font-weight:600;
      }

      tbody td{
        padding:8px 8px;
        border-bottom:1px solid var(--border);
        vertical-align:middle;
      }

      tbody tr:nth-child(even){
        background:#fafafa;
      }

      tbody tr:hover{
        background:#ffeef2;
      }

      .estado-pill{
        display:inline-block;
        padding:4px 10px;
        border-radius:999px;
        border:1px solid var(--border);
        font-size:0.8em;
        background:#f9f9f9;
      }
      .estado-pill--vacio{
        color:#999;
        border-style:dashed;
      }

      .form-estado{
        display:flex;
        gap:6px;
        align-items:center;
      }
      .form-estado select{
        padding:4px 6px;
        border-radius:4px;
        border:1px solid var(--border);
        font-size:0.85em;
      }
      .btn-estado{
        padding:4px 8px;
        border-radius:4px;
        border:none;
        background:var(--primary);
        color:white;
        font-size:0.8em;
        cursor:pointer;
      }

      .btn-informe{
        padding:4px 8px;
        border-radius:4px;
        border:none;
        background:#34495e;
        color:white;
        font-size:0.8em;
        cursor:pointer;
        text-decoration:none;
        display:inline-block;
      }

      /* Detalle */
      .detail-row-table{
        width:100%;
        border-collapse:collapse;
        margin-bottom:20px;
      }
      .detail-row-table th,
      .detail-row-table td{
        padding:6px 8px;
        border-bottom:1px solid var(--border);
        text-align:left;
      }
      .detail-row-table th{
        width:30%;
        color:var(--primary);
      }

      .email-section{
        margin-top:20px;
        display:grid;
        grid-template-columns:1.2fr 1.8fr;
        gap:20px;
      }
      .email-form-card,
      .email-log-card{
        background:#fafafa;
        border-radius:8px;
        padding:15px 18px;
        border:1px solid #e5e5e5;
      }
      .email-form-card h4,
      .email-log-card h4{
        margin-bottom:8px;
        color:#444;
      }
      .email-form-card .form-group{
        margin-bottom:10px;
        display:flex;
        flex-direction:column;
        gap:4px;
      }
      .email-form-card label{
        font-size:0.85em;
        font-weight:600;
      }
      .email-form-card input[type="text"],
      .email-form-card textarea{
        padding:8px 10px;
        border-radius:4px;
        border:1px solid var(--border);
        font-size:0.9em;
        resize:vertical;
      }
      .email-form-card textarea{
        min-height:120px;
      }
      .email-form-card input[type="submit"]{
        margin-top:8px;
        padding:8px 12px;
        border:none;
        border-radius:4px;
        background:var(--primary);
        color:white;
        font-size:0.9em;
        cursor:pointer;
      }
      .email-status-msg{
        margin-bottom:10px;
        padding:6px 8px;
        border-radius:6px;
        font-size:0.85em;
      }
      .email-status-ok{
        background:#e7f7ec;
        border:1px solid #9dd7b1;
        color:#217346;
      }
      .email-status-error{
        background:#ffe6e6;
        border:1px solid #ffb3b3;
        color:#b30000;
      }

      .mail-list{
        max-height:280px;
        overflow:auto;
        font-size:0.86em;
      }
      .mail-item{
        padding:8px 0;
        border-bottom:1px solid #e3e3e3;
      }
      .mail-item:last-child{
        border-bottom:none;
      }
      .mail-item strong{
        color:#333;
      }
      .mail-meta{
        font-size:0.8em;
        color:#777;
        margin-bottom:2px;
      }
      .mail-snippet{
        font-size:0.85em;
        color:#555;
      }

      @media (max-width: 900px){
        body{
          flex-direction:column;
        }
        nav{
          width:100%;
          flex-direction:row;
          flex-wrap:wrap;
          box-shadow:none;
        }
        nav h2{
          width:100%;
        }
        main{
          padding:20px;
        }
        .email-section{
          grid-template-columns:1fr;
        }
      }
    </style>
  </head>
  <body>

  <?php if (!$loggedIn): ?>

    <!-- ------------------ VISTA LOGIN ------------------ -->
    <div class="login-wrapper">
      <form method="post" class="login-card">
        <h2>Acceso al panel</h2>

        <?php if ($login_error !== ""): ?>
          <div class="login-error">
            <?= htmlspecialchars($login_error, ENT_QUOTES, 'UTF-8'); ?>
          </div>
        <?php endif; ?>

        <div class="form-group">
          <label for="usuario">Usuario</label>
          <input type="text" name="usuario" id="usuario" autocomplete="username">
        </div>

        <div class="form-group">
          <label for="password">Contraseña</label>
          <input type="password" name="password" id="password" autocomplete="current-password">
        </div>

        <input type="hidden" name="action" value="login">
        <input type="submit" value="Entrar">
      </form>
    </div>

  <?php else: ?>

    <!-- ------------------ PANEL ADMIN ------------------ -->
    <nav>
      <h2>Menú</h2>
      <button>Enlace 1</button>
      <button>Enlace 2</button>
      <button>Enlace 3</button>
    </nav>
    <main>
      <?php
        $title = $viewId ? "Informe de inscripción" : "Listado de inscripciones";
      ?>
      <header>
        <div style="display:flex; align-items:center; gap:8px;">
          <?php if ($viewId): ?>
            <a href="<?= htmlspecialchars($_SERVER['PHP_SELF'], ENT_QUOTES, 'UTF-8'); ?>" class="back-link">← Volver al listado</a>
          <?php endif; ?>
          <h1><?= htmlspecialchars($title, ENT_QUOTES, 'UTF-8'); ?></h1>
        </div>
        <div class="user-actions">
          <span>Conectado como <strong>jocarsa</strong></span>
          <a class="logout-link" href="?logout=1">Cerrar sesión</a>
        </div>
      </header>

      <?php if ($viewId && $primaryKeyColumn !== null): ?>

        <?php
          // Cargar la fila concreta
          $filaDetalle = null;
          $stmt = $c->prepare("SELECT * FROM inscripciones WHERE $primaryKeyColumn = ? LIMIT 1");
          if ($stmt) {
            $stmt->bind_param("s", $viewId);
            $stmt->execute();
            $result = $stmt->get_result();
            $filaDetalle = $result->fetch_assoc();
            $stmt->close();
          }
        ?>

        <?php if ($filaDetalle): ?>
          <?php
            // Determinar email de contacto (si existe columna de email)
            $contactEmail = null;
            if ($emailColumn !== null && isset($filaDetalle[$emailColumn])) {
              $contactEmail = $filaDetalle[$emailColumn];
            }

            // Obtener comunicaciones por email si tenemos correo
            $commReport = null;
            if ($contactEmail) {
              $commReport = crm_fetch_emails_for_contact($contactEmail, 20);
            }
          ?>

          <section class="detail-card">
            <h3>Datos de la inscripción (ID: <?= htmlspecialchars($viewId, ENT_QUOTES, 'UTF-8'); ?>)</h3>
            <p class="description">
              Detalle completo del registro seleccionado en la tabla
              <strong>inscripciones</strong>, junto con el historial de comunicaciones
              por correo electrónico asociado al contacto.
            </p>

            <table class="detail-row-table">
              <tbody>
                <?php foreach ($filaDetalle as $campo => $valor): ?>
                  <tr>
                    <th><?= htmlspecialchars($campo, ENT_QUOTES, 'UTF-8'); ?></th>
                    <td><?= htmlspecialchars((string)$valor, ENT_QUOTES, 'UTF-8'); ?></td>
                  </tr>
                <?php endforeach; ?>
              </tbody>
            </table>

            <div class="email-section">
              <div class="email-form-card">
                <h4>Enviar mensaje al contacto</h4>

                <?php if ($emailSendMessage): ?>
                  <div class="email-status-msg <?= (strpos($emailSendMessage, 'correctamente') !== false) ? 'email-status-ok' : 'email-status-error'; ?>">
                    <?= $emailSendMessage; ?>
                  </div>
                <?php endif; ?>

                <?php if ($contactEmail): ?>
                  <p style="font-size:0.85em; margin-bottom:8px;">
                    Correo del contacto:
                    <strong><?= htmlspecialchars($contactEmail, ENT_QUOTES, 'UTF-8'); ?></strong><br>
                    Remitente usado: <code><?= htmlspecialchars(CRM_MAIL_USER, ENT_QUOTES, 'UTF-8'); ?></code>
                  </p>

                  <form method="post" action="?view=<?= urlencode($viewId); ?>">
                    <div class="form-group">
                      <label for="subject">Asunto</label>
                      <input type="text" id="subject" name="subject">
                    </div>
                    <div class="form-group">
                      <label for="body">Mensaje</label>
                      <textarea id="body" name="body"></textarea>
                    </div>
                    <input type="hidden" name="to" value="<?= htmlspecialchars($contactEmail, ENT_QUOTES, 'UTF-8'); ?>">
                    <input type="hidden" name="action" value="send_email">
                    <input type="submit" value="Enviar mensaje">
                  </form>
                <?php else: ?>
                  <p style="font-size:0.85em; color:#b30000;">
                    No se ha detectado ninguna columna de email para este registro.  
                    El envío de correos no está disponible.
                  </p>
                <?php endif; ?>
              </div>

              <div class="email-log-card">
                <h4>Comunicaciones por correo</h4>

                <?php if (!$contactEmail): ?>
                  <p style="font-size:0.85em; color:#555;">
                    No hay correo electrónico asociado a este registro.<br>
                    Por tanto, no se puede generar el informe de comunicaciones.
                  </p>
                <?php else: ?>
                  <?php if ($commReport && $commReport['error']): ?>
                    <p style="font-size:0.85em; color:#b30000;">
                      Error al acceder al buzón IMAP:
                      <?= htmlspecialchars($commReport['error'], ENT_QUOTES, 'UTF-8'); ?>
                    </p>
                  <?php else: ?>
                    <div class="mail-list">
                      <?php
                        $sent     = $commReport ? $commReport['sent']     : [];
                        $received = $commReport ? $commReport['received'] : [];
                      ?>

                      <p class="mail-meta">
                        Mensajes enviados: <?= count($sent); ?> |
                        Mensajes recibidos: <?= count($received); ?>
                      </p>

                      <?php if (empty($sent) && empty($received)): ?>
                        <p style="font-size:0.85em; color:#555;">
                          No se han encontrado mensajes relacionados con
                          <strong><?= htmlspecialchars($contactEmail, ENT_QUOTES, 'UTF-8'); ?></strong>.
                        </p>
                      <?php else: ?>

                        <?php if (!empty($sent)): ?>
                          <p style="margin-top:8px; font-weight:bold; font-size:0.9em;">Enviados (<?= count($sent); ?>)</p>
                          <?php foreach ($sent as $mail): ?>
                            <div class="mail-item">
                              <div class="mail-meta">
                                <strong>Asunto:</strong> <?= htmlspecialchars($mail['subject'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>Fecha:</strong> <?= htmlspecialchars($mail['date'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>De:</strong> <?= htmlspecialchars($mail['from'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>Para:</strong> <?= htmlspecialchars($mail['to'], ENT_QUOTES, 'UTF-8'); ?>
                              </div>
                              <div class="mail-snippet">
                                <?= nl2br(htmlspecialchars($mail['snippet'], ENT_QUOTES, 'UTF-8')); ?>
                              </div>
                            </div>
                          <?php endforeach; ?>
                        <?php endif; ?>

                        <?php if (!empty($received)): ?>
                          <p style="margin-top:10px; font-weight:bold; font-size:0.9em;">Recibidos (<?= count($received); ?>)</p>
                          <?php foreach ($received as $mail): ?>
                            <div class="mail-item">
                              <div class="mail-meta">
                                <strong>Asunto:</strong> <?= htmlspecialchars($mail['subject'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>Fecha:</strong> <?= htmlspecialchars($mail['date'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>De:</strong> <?= htmlspecialchars($mail['from'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>Para:</strong> <?= htmlspecialchars($mail['to'], ENT_QUOTES, 'UTF-8'); ?>
                              </div>
                              <div class="mail-snippet">
                                <?= nl2br(htmlspecialchars($mail['snippet'], ENT_QUOTES, 'UTF-8')); ?>
                              </div>
                            </div>
                          <?php endforeach; ?>
                        <?php endif; ?>

                      <?php endif; ?>
                    </div>
                  <?php endif; ?>
                <?php endif; ?>
              </div>
            </div>
          </section>
        <?php else: ?>
          <section class="detail-card">
            <h3>Registro no encontrado</h3>
            <p class="description">
              No se ha podido localizar la inscripción con identificador
              <strong><?= htmlspecialchars($viewId, ENT_QUOTES, 'UTF-8'); ?></strong>.
            </p>
          </section>
        <?php endif; ?>

      <?php else: ?>

        <!-- -------- LISTADO GENERAL DE INSCRIPCIONES -------- -->
        <section class="table-card">
          <h3>Tabla: inscripciones</h3>
          <p class="description">
            Registros actuales en la tabla <strong>inscripciones</strong> de la base de datos
            <strong>training_center</strong>. Puede asignar un estado CRM a cada registro
            y acceder a un informe detallado por inscripción.
          </p>

          <table>
            <thead>
              <tr>
                <?php
                /* COLUMNAS CON SUS COMENTARIOS */
                $r = $c->query("
                  SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT
                  FROM information_schema.columns
                  WHERE table_schema='training_center'
                    AND table_name='inscripciones'
                ");

                $columnNames = [];
                while($f = $r->fetch_assoc()) {
                  $columnNames[] = $f['COLUMN_NAME'];
                  echo '<th>'.htmlspecialchars($f['COLUMN_NAME'], ENT_QUOTES, 'UTF-8').'</th>';
                }

                // Columnas extra para estado CRM y acciones
                echo '<th>Estado CRM</th>';
                echo '<th>Acciones</th>';
                ?>
              </tr>
            </thead>
            <tbody>
              <?php
                $r = $c->query("SELECT * FROM inscripciones;");

                while($f = $r->fetch_assoc()) {
                  // ID del registro basado en la columna PK detectada (si existe)
                  $idRegistro = null;
                  if ($primaryKeyColumn !== null && isset($f[$primaryKeyColumn])) {
                    $idRegistro = (string)$f[$primaryKeyColumn];
                  }

                  echo '<tr>';

                  // Mostrar todas las columnas originales
                  foreach($f as $clave=>$valor){
                    echo '<td>'.htmlspecialchars((string)$valor, ENT_QUOTES, 'UTF-8').'</td>';
                  }

                  // Columna "Estado CRM" (pastilla de color)
                  echo '<td>';
                  if ($idRegistro !== null && isset($estadosActuales[$idRegistro])) {
                    $estadoRow = $estadosActuales[$idRegistro];
                    $estadoTxt = htmlspecialchars($estadoRow['estado'], ENT_QUOTES, 'UTF-8');
                    $colorTxt  = htmlspecialchars($estadoRow['color'],  ENT_QUOTES, 'UTF-8');

                    echo '<span class="estado-pill" style="background:'.$colorTxt.'20; border-color:'.$colorTxt.'; color:'.$colorTxt.';">';
                    echo $estadoTxt;
                    echo '</span>';
                  } else {
                    echo '<span class="estado-pill estado-pill--vacio">Sin estado</span>';
                  }
                  echo '</td>';

                  // Columna "Acciones" (selector estado + botón + informe)
                  echo '<td>';
                  if ($idRegistro !== null) {
                    // Formulario de estado
                    echo '<form method="post" class="form-estado" style="margin-bottom:4px;">';
                    echo '<input type="hidden" name="action" value="update_estado">';
                    echo '<input type="hidden" name="id_registro" value="'.htmlspecialchars($idRegistro, ENT_QUOTES, 'UTF-8').'">';
                    echo '<select name="estado">';
                    foreach ($estadosCRM as $nombreEstado => $colorEstado) {
                      $selected = (
                        $idRegistro !== null &&
                        isset($estadosActuales[$idRegistro]) &&
                        $estadosActuales[$idRegistro]['estado'] === $nombreEstado
                      ) ? ' selected' : '';
                      echo '<option value="'.htmlspecialchars($nombreEstado, ENT_QUOTES, 'UTF-8').'"'.$selected.'>';
                      echo htmlspecialchars($nombreEstado, ENT_QUOTES, 'UTF-8');
                      echo '</option>';
                    }
                    echo '</select>';
                    echo '<button type="submit" class="btn-estado">Guardar</button>';
                    echo '</form>';

                    // Enlace a informe
                    $urlInforme = htmlspecialchars($_SERVER['PHP_SELF'], ENT_QUOTES, 'UTF-8') . '?view=' . urlencode($idRegistro);
                    echo '<a class="btn-informe" href="'.$urlInforme.'">Informe</a>';
                  }
                  echo '</td>';

                  echo '</tr>';
                }
              ?>
            </tbody>
          </table>
        </section>

      <?php endif; ?>

    </main>

  <?php endif; ?>

  </body>
</html>
```

### arreglos correo
<small>Creado: 2025-12-04 16:45</small>

#### Explicación

El código proporcionado es una página web en PHP que se conecta a una base de datos MySQL y muestra información sobre registros en una tabla llamada `inscripciones`. La página también permite gestionar estados CRM (Customer Relationship Management) para cada registro, así como ver correos electrónicos relacionados con cada contacto. Aquí te presento un resumen detallado de cómo funciona el código:

### Estructura del Código

1. **Conexión a la Base de Datos**:
   - Se establece una conexión a la base de datos `training_center` usando MySQLi.
   - Se verifica si se ha proporcionado un ID de registro para mostrar detalles específicos.

2. **Manejo de Estados CRM**:
   - El código permite seleccionar y guardar estados CRM desde una lista desplegable en el formulario del estado.
   - Los estados CRM son almacenados en la base de datos y representados visualmente con colores en la tabla principal.

3. **Correos No Leídos**:
   - Se verifica si hay correos no leídos para cada contacto y se muestra un icono indicativo en la columna correspondiente.

4. **Visualización del Detalle de Registro**:
   - Si se proporciona un ID, el código muestra detalles específicos del registro.
   - Incluye una sección para ver correos enviados y recibidos relacionados con ese contacto (si hay uno).

5. **Listado General de Registros**:
   - Muestra todos los registros en la tabla `inscripciones` con sus respectivos estados CRM y acciones disponibles.

### Detalles del Código

#### Conexión a la Base de Datos
```php
$c = new mysqli("localhost", "training_center_user", "your_password_here", "training_center");

if ($c->connect_errno) {
    die("Falló la conexión: (" . $c->connect_errno . ") " . $c->connect_error);
}
```

#### Obtención de Columnas y Detalles del Registro
```php
$r = $c->query("
  SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT
  FROM information_schema.columns
  WHERE table_schema='training_center'
    AND table_name='inscripciones'
");

// Recuperar el ID de registro si está proporcionado en la URL
$registroId = null;
if (isset($_GET['view'])) {
    $registroId = trim(strip_tags($_GET['view']));
}
```

#### Obtención del Estado Actual y Correos No Leídos
```php
$r = $c->query("SELECT * FROM estados CRM WHERE tabla='inscripciones'");
$estadosActuales = [];
while ($f = $r->fetch_assoc()) {
    $estadosActuales[$f['id_registro']] = $f;
}

// Verificar correos no leídos para cada registro
$r = $c->query("SELECT email FROM inscripciones WHERE email IS NOT NULL");
$unreadByEmail = [];
while ($f = $r->fetch_assoc()) {
    // Logica adicional para verificar correos no leidos en IMAP o otro servicio de correo.
}
```

#### Procesamiento y Visualización del Formulario Estado CRM
```php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['action'])) {
    if ($_POST['action'] === 'update_estado') {
        $id_registro = trim(strip_tags($_POST['id_registro']));
        $estado      = trim(strip_tags($_POST['estado']));
        
        // Actualizar estado en la base de datos
        $sql = "UPDATE estados CRM SET estado='$estado' WHERE id_registro=$id_registro";
        $c->query($sql);
    }
}
```

### HTML y CSS

El código también incluye HTML y CSS para mostrar la tabla, los formularios y las notificaciones. La estructura de la página está diseñada para ser fácil de leer y navegar:

- **Tabla principal**: Muestra todos los registros con sus estados CRM.
- **Formulario Estado CRM**: Permite seleccionar y guardar un estado para cada registro.
- **Sección Detalle del Registro**: Muestra detalles específicos del registro cuando se proporciona un ID.

### Consideraciones Adicionales

1. **Seguridad**:
   - El código utiliza `trim(strip_tags)` para limpiar los datos de entrada, pero aún puede beneficiarse de más validación y sanitización.
   
2. **Funcionalidades Futuras**:
   - Puede incluir funcionalidades como paginación, búsqueda avanzada o exportación a formato CSV.

3. **Estilo**:
   - El código utiliza clases CSS para estilizar los elementos del formulario y la tabla (por ejemplo, `.badge-unread`, `.estado-pill`).

### Ejemplo de Uso

Cuando accedes a la URL sin parámetros (`?view=`), se muestra una lista general de registros con sus estados CRM. Al proporcionar un ID en la URL (`?view=ID_REGISTRO`), se muestran detalles específicos del registro, incluyendo correos enviados y recibidos si está disponible.

Este código es bastante robusto para manejar tareas básicas de gestión de registros y estados CRM, aunque puede beneficiarse de mejoras en términos de seguridad y funcionalidad avanzada.

`008-arreglos correo.php`

```
<?php
session_start();

// Conexión a la base de datos (una sola vez, al inicio del archivo)
$c = new mysqli("localhost","training_center","training_center","training_center");
if ($c->connect_error) {
  die("Error de conexión: " . $c->connect_error);
}

/*-----------------------------------------------------------
  1) Tabla auxiliar para estados CRM (NO toca inscripciones)
-----------------------------------------------------------*/
$c->query("
  CREATE TABLE IF NOT EXISTS crm_estados_inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_registro VARCHAR(255) NOT NULL UNIQUE,
    estado VARCHAR(50) NOT NULL,
    color VARCHAR(20) NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
");

/*-----------------------------------------------------------
  2) Estados típicos de CRM (en español) + colores
-----------------------------------------------------------*/
$estadosCRM = [
  'Nuevo'             => '#3498db', // azul
  'Contactado'        => '#9b59b6', // violeta
  'En seguimiento'    => '#f1c40f', // amarillo
  'Cualificado'       => '#2ecc71', // verde
  'No interesado'     => '#95a5a6', // gris
  'Ganado'            => '#27ae60', // verde fuerte
  'Perdido'           => '#e74c3c', // rojo
];

/*-----------------------------------------------------------
  3) Detectar columna PRIMARY KEY de inscripciones
-----------------------------------------------------------*/
$primaryKeyColumn = null;
$pkResult = $c->query("
  SELECT COLUMN_NAME 
  FROM information_schema.columns
  WHERE table_schema = 'training_center'
    AND table_name   = 'inscripciones'
    AND COLUMN_KEY   = 'PRI'
  LIMIT 1;
");
if ($pkResult && $pkResult->num_rows > 0) {
  $primaryKeyColumn = $pkResult->fetch_assoc()['COLUMN_NAME'];
}

/*-----------------------------------------------------------
  4) Detectar columna de email de inscripciones
-----------------------------------------------------------*/
$emailColumn = null;
$emailColResult = $c->query("
  SELECT COLUMN_NAME
  FROM information_schema.columns
  WHERE table_schema='training_center'
    AND table_name='inscripciones'
    AND (
      COLUMN_NAME LIKE '%mail%' OR
      COLUMN_NAME LIKE '%email%' OR
      COLUMN_NAME LIKE '%correo%'
    )
  LIMIT 1;
");
if ($emailColResult && $emailColResult->num_rows > 0) {
  $emailColumn = $emailColResult->fetch_assoc()['COLUMN_NAME'];
}

/*-----------------------------------------------------------
  5) Configuración de correo (SMTP + IMAP)
-----------------------------------------------------------*/
define('CRM_MAIL_USER', 'python@jocarsa.com');
define('CRM_MAIL_PASS', 'TAME123$');
define('CRM_SMTP_HOST', 'smtp.ionos.es');
define('CRM_SMTP_PORT', 587); // STARTTLS
define('CRM_IMAP_MAILBOX', '{imap.ionos.es:993/imap/ssl}INBOX');

// *** carpeta de ENVIADOS (ajústala si IONOS usa otro nombre) ***
define('CRM_IMAP_SENT_MAILBOX', '{imap.ionos.es:993/imap/ssl}Elementos enviados');

/*-----------------------------------------------------------
  6) Función: guardar un mensaje en la carpeta "Sent" por IMAP
-----------------------------------------------------------*/
function crm_append_to_sent($rawMessage) {
  if (!function_exists('imap_open')) {
    return;
  }

  $mailbox  = CRM_IMAP_SENT_MAILBOX;
  $user     = CRM_MAIL_USER;
  $password = CRM_MAIL_PASS;

  $imap = @imap_open($mailbox, $user, $password);
  if (!$imap) {
    // si falla, simplemente no se guarda; no rompemos nada
    return;
  }

  // Fecha formato IMAP
  $date = date('d-M-Y H:i:s O'); // ej. 02-Mar-2025 12:34:56 +0100

  // Marcar como \Seen para que no cuente como no leído
  @imap_append($imap, $mailbox, $rawMessage, "\\Seen", $date);

  imap_close($imap);
}

/*-----------------------------------------------------------
  7) Función: enviar correo via SMTP (con STARTTLS + guardar en Sent)
-----------------------------------------------------------*/
function crm_send_email_smtp($to, $subject, $body, &$errorMsg) {
  $errorMsg = '';
  $smtpHost = CRM_SMTP_HOST;
  $smtpPort = CRM_SMTP_PORT;
  $username = CRM_MAIL_USER;
  $password = CRM_MAIL_PASS;
  $from     = CRM_MAIL_USER;
  $fromName = 'CRM Training Center';

  $socket = @fsockopen($smtpHost, $smtpPort, $errno, $errstr, 30);
  if (!$socket) {
    $errorMsg = "No se pudo conectar al servidor SMTP: $errstr ($errno)";
    return false;
  }

  // Banner inicial
  $resp = fgets($socket, 515);
  if (substr($resp, 0, 3) != '220') {
    $errorMsg = "Respuesta inesperada del servidor SMTP: $resp";
    fclose($socket);
    return false;
  }

  // lector de respuestas multilínea tipo 250-... / 250 ...
  $readMultiline = function($expectedCode) use ($socket, &$errorMsg) {
    $response = '';
    while (($line = fgets($socket, 515)) !== false) {
      $response .= $line;
      if (substr($line, 0, 3) != $expectedCode) {
        $errorMsg = "Respuesta inesperada del servidor SMTP: $line";
        return false;
      }
      if (strlen($line) < 4 || $line[3] != '-') {
        break;
      }
    }
    return $response;
  };

  // comandos de una sola línea
  $sendCmdOneLine = function($cmd, $expectedCode) use ($socket, &$errorMsg) {
    fputs($socket, $cmd);
    $resp = fgets($socket, 515);
    if (substr($resp, 0, 3) != $expectedCode) {
      $errorMsg = "Error SMTP al enviar '$cmd': $resp";
      return false;
    }
    return true;
  };

  // 1) EHLO inicial (sin TLS)
  fputs($socket, "EHLO localhost\r\n");
  $ehloResp = $readMultiline("250");
  if ($ehloResp === false) {
    fclose($socket);
    return false;
  }

  // 2) STARTTLS
  fputs($socket, "STARTTLS\r\n");
  $resp = fgets($socket, 515);
  if (substr($resp, 0, 3) != '220') {
    $errorMsg = "Fallo al iniciar STARTTLS: $resp";
    fclose($socket);
    return false;
  }

  // 3) Activar cifrado TLS
  $cryptoOk = @stream_socket_enable_crypto(
    $socket,
    true,
    STREAM_CRYPTO_METHOD_TLS_CLIENT
  );
  if (!$cryptoOk) {
    $errorMsg = "No se pudo activar el cifrado TLS en el socket SMTP.";
    fclose($socket);
    return false;
  }

  // 4) EHLO otra vez, ya cifrado
  fputs($socket, "EHLO localhost\r\n");
  $ehloResp2 = $readMultiline("250");
  if ($ehloResp2 === false) {
    fclose($socket);
    return false;
  }

  // 5) AUTH LOGIN
  if (!$sendCmdOneLine("AUTH LOGIN\r\n", "334")) {
    fclose($socket);
    return false;
  }

  if (!$sendCmdOneLine(base64_encode($username) . "\r\n", "334")) {
    fclose($socket);
    return false;
  }

  if (!$sendCmdOneLine(base64_encode($password) . "\r\n", "235")) {
    fclose($socket);
    return false;
  }

  // 6) MAIL FROM
  if (!$sendCmdOneLine("MAIL FROM:<$from>\r\n", "250")) {
    fclose($socket);
    return false;
  }

  // 7) RCPT TO
  if (!$sendCmdOneLine("RCPT TO:<$to>\r\n", "250")) {
    fclose($socket);
    return false;
  }

  // 8) DATA
  if (!$sendCmdOneLine("DATA\r\n", "354")) {
    fclose($socket);
    return false;
  }

  // Cabeceras + cuerpo (mensaje completo RFC822)
  $headers  = "From: " . $fromName . " <" . $from . ">\r\n";
  $headers .= "To: <$to>\r\n";
  $headers .= "Subject: " . $subject . "\r\n";
  $headers .= "MIME-Version: 1.0\r\n";
  $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
  $headers .= "Content-Transfer-Encoding: 8bit\r\n";
  $headers .= "\r\n";

  $rawMessage = $headers . $body;

  $data = $rawMessage . "\r\n.\r\n";

  fputs($socket, $data);
  $resp = fgets($socket, 515);
  if (substr($resp, 0, 3) != '250') {
    $errorMsg = "Error al completar el envío: $resp";
    fclose($socket);
    return false;
  }

  fputs($socket, "QUIT\r\n");
  fclose($socket);

  // *** Guardar una copia en la carpeta "Sent" ***
  crm_append_to_sent($rawMessage);

  return true;
}

/*-----------------------------------------------------------
  8) Función: obtener comunicaciones (INBOX + Sent) para un contacto
-----------------------------------------------------------*/
function crm_fetch_emails_for_contact($contactEmail, $limit = 20) {
  $result = [
    'sent'     => [],
    'received' => [],
    'error'    => null
  ];

  if (!function_exists('imap_open')) {
    $result['error'] = "La extensión IMAP de PHP no está habilitada.";
    return $result;
  }

  $user     = CRM_MAIL_USER;
  $password = CRM_MAIL_PASS;
  $ourAddress = strtolower(CRM_MAIL_USER);
  $safeEmail  = str_replace('"', '\"', $contactEmail);

  // helper para escanear una carpeta (INBOX o Sent)
  $scanMailbox = function($mailbox) use (&$result, $user, $password, $safeEmail, $ourAddress, $limit) {
    $inbox = @imap_open($mailbox, $user, $password);
    if (!$inbox) {
      if ($result['error'] === null) {
        $result['error'] = imap_last_error();
      }
      return;
    }

    $emailsIds = [];

    // FROM contacto
    $fromIds = imap_search($inbox, 'FROM "' . $safeEmail . '"');
    if ($fromIds !== false) {
      $emailsIds = array_merge($emailsIds, $fromIds);
    }

    // TO contacto
    $toIds = imap_search($inbox, 'TO "' . $safeEmail . '"');
    if ($toIds !== false) {
      $emailsIds = array_merge($emailsIds, $toIds);
    }

    if (!empty($emailsIds)) {
      $emailsIds = array_values(array_unique($emailsIds));
      rsort($emailsIds);
      // opcional: podríamos limitar aquí por carpeta; lo dejamos completo
    } else {
      imap_close($inbox);
      return;
    }

    foreach ($emailsIds as $num) {
      $overview = imap_fetch_overview($inbox, $num, 0);
      if (!$overview) continue;
      $ov = $overview[0];

      $header = imap_headerinfo($inbox, $num);

      $from = isset($header->fromaddress) ? $header->fromaddress : ($ov->from ?? '');
      $to   = isset($header->toaddress)   ? $header->toaddress   : ($ov->to   ?? '');

      $subject = isset($ov->subject) ? imap_utf8($ov->subject) : '';
      $date    = isset($ov->date)    ? $ov->date : '';

      $body = imap_fetchbody($inbox, $num, 1);
      if (!$body) $body = '';
      $body = imap_qprint($body);
      $snippet = trim($body);
      if (function_exists('mb_substr')) {
        $snippet = mb_substr($snippet, 0, 200);
      } else {
        $snippet = substr($snippet, 0, 200);
      }

      $entry = [
        'subject' => $subject,
        'date'    => $date,
        'from'    => $from,
        'to'      => $to,
        'snippet' => $snippet
      ];

      $fromLower = strtolower($from);
      if (strpos($fromLower, $ourAddress) !== false) {
        $result['sent'][] = $entry;
      } else {
        $result['received'][] = $entry;
      }
    }

    imap_close($inbox);
  };

  // Escanear INBOX y Sent
  $scanMailbox(CRM_IMAP_MAILBOX);
  $scanMailbox(CRM_IMAP_SENT_MAILBOX);

  // Ordenar por fecha dentro de enviados y recibidos (descendente)
  $sortByDateDesc = function(&$arr) {
    usort($arr, function($a, $b) {
      $da = strtotime($a['date'] ?? '1970-01-01');
      $db = strtotime($b['date'] ?? '1970-01-01');
      return $db <=> $da;
    });
  };

  $sortByDateDesc($result['sent']);
  $sortByDateDesc($result['received']);

  // Aplicar límite por tipo
  if ($limit > 0) {
    $result['sent']     = array_slice($result['sent'], 0, $limit);
    $result['received'] = array_slice($result['received'], 0, $limit);
  }

  return $result;
}

/*-----------------------------------------------------------
  9) LOGIN / LOGOUT
-----------------------------------------------------------*/
$login_error = "";

if (isset($_GET['logout'])) {
  session_destroy();
  header("Location: " . $_SERVER['PHP_SELF']);
  exit;
}

if (isset($_POST['action']) && $_POST['action'] === 'login') {
  $usuario  = $_POST['usuario']  ?? '';
  $password = $_POST['password'] ?? '';

  if ($usuario === 'jocarsa' && $password === 'jocarsa') {
    $_SESSION['admin_logged'] = true;
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos.";
  }
}

$loggedIn = isset($_SESSION['admin_logged']) && $_SESSION['admin_logged'] === true;

/*-----------------------------------------------------------
  10) Actualización de estado CRM
-----------------------------------------------------------*/
if (
  $loggedIn &&
  isset($_POST['action']) &&
  $_POST['action'] === 'update_estado'
) {
  $id_registro = $_POST['id_registro'] ?? null;
  $estado      = $_POST['estado']      ?? null;

  if ($id_registro !== null && isset($estadosCRM[$estado])) {
    $color = $estadosCRM[$estado];

    $stmt = $c->prepare("
      INSERT INTO crm_estados_inscripciones (id_registro, estado, color)
      VALUES (?, ?, ?)
      ON DUPLICATE KEY UPDATE
        estado = VALUES(estado),
        color  = VALUES(color)
    ");
    if ($stmt) {
      $stmt->bind_param("sss", $id_registro, $estado, $color);
      $stmt->execute();
      $stmt->close();
    }
  }
}

/*-----------------------------------------------------------
  11) Envío de email desde el informe
-----------------------------------------------------------*/
$emailSendMessage = "";

if (
  $loggedIn &&
  isset($_POST['action']) &&
  $_POST['action'] === 'send_email'
) {
  $to      = $_POST['to']      ?? '';
  $subject = $_POST['subject'] ?? '';
  $body    = $_POST['body']    ?? '';

  if ($to && $subject && $body) {
    $errorMsg = '';
    $ok = crm_send_email_smtp($to, $subject, $body, $errorMsg);
    if ($ok) {
      $emailSendMessage = "Mensaje enviado correctamente.";
    } else {
      $emailSendMessage = "Error al enviar el mensaje: " . htmlspecialchars($errorMsg, ENT_QUOTES, 'UTF-8');
    }
  } else {
    $emailSendMessage = "Por favor, rellena todos los campos del mensaje.";
  }
}

/*-----------------------------------------------------------
  12) Estados actuales (para la tabla)
-----------------------------------------------------------*/
$estadosActuales = [];
if ($loggedIn) {
  $resEstados = $c->query("SELECT id_registro, estado, color FROM crm_estados_inscripciones");
  if ($resEstados) {
    while ($row = $resEstados->fetch_assoc()) {
      $estadosActuales[$row['id_registro']] = $row;
    }
  }
}

/*-----------------------------------------------------------
  13) Mapa de correos NO LEÍDOS por contacto (para la tabla)
-----------------------------------------------------------*/
// *** nueva funcionalidad: marcar si hay emails sin leer de cada contacto ***
$unreadByEmail = [];
if ($loggedIn && $emailColumn !== null && function_exists('imap_open')) {
  $mailbox  = CRM_IMAP_MAILBOX; // INBOX
  $user     = CRM_MAIL_USER;
  $password = CRM_MAIL_PASS;

  $inbox = @imap_open($mailbox, $user, $password);
  if ($inbox) {
    $unseenIds = imap_search($inbox, 'UNSEEN');
    if ($unseenIds !== false) {
      foreach ($unseenIds as $num) {
        $header = imap_headerinfo($inbox, $num);
        if (!empty($header->from)) {
          // from es un array de objetos (mailbox + host)
          foreach ($header->from as $fromObj) {
            $fromEmail = strtolower(trim($fromObj->mailbox . '@' . $fromObj->host));
            if ($fromEmail !== '' && $fromEmail !== strtolower(CRM_MAIL_USER)) {
              $unreadByEmail[$fromEmail] = true;
            }
          }
        }
      }
    }
    imap_close($inbox);
  }
}

/*-----------------------------------------------------------
  14) ID de informe (vista detalle)
-----------------------------------------------------------*/
$viewId = null;
if ($loggedIn && isset($_GET['view'])) {
  $viewId = $_GET['view'];
}

?>
<!doctype html>
<html lang="es">
  <head>
    <title>Panel de administración</title>
    <meta charset="utf-8">
    <style>
      :root{
        --primary: crimson;
        --primary-light: #ff8fa0;
        --bg: #f2f2f2;
        --text: #333;
        --border: #ddd;
      }

      *{
        box-sizing:border-box;
        margin:0;
        padding:0;
      }

      html, body{
        height:100%;
        font-family: "Segoe UI", sans-serif;
        color: var(--text);
        background: var(--bg);
      }

      body{
        display:flex;
        align-items:stretch;
      }

      /*---------------- LOGIN ----------------*/
      .login-wrapper{
        width:100%;
        display:flex;
        justify-content:center;
        align-items:center;
        padding:40px;
      }
      .login-card{
        background:white;
        padding:30px 40px;
        width:360px;
        border-radius:10px;
        box-shadow:0 4px 15px rgba(0,0,0,0.1);
        border-top:8px solid var(--primary);
      }
      .login-card h2{
        margin-bottom:20px;
        color:var(--primary);
        font-size:1.4em;
      }
      .login-card .form-group{
        margin-bottom:15px;
        display:flex;
        flex-direction:column;
        gap:6px;
      }
      .login-card label{
        font-size:0.95em;
        font-weight:600;
        color:var(--primary);
      }
      .login-card input[type="text"],
      .login-card input[type="password"]{
        padding:10px 12px;
        border-radius:6px;
        border:1px solid var(--border);
        font-size:1em;
      }
      .login-card input[type="submit"]{
        margin-top:10px;
        width:100%;
        padding:12px;
        border:none;
        border-radius:6px;
        background:var(--primary);
        color:white;
        font-size:1em;
        cursor:pointer;
      }
      .login-error{
        margin-bottom:10px;
        padding:8px 10px;
        border-radius:6px;
        background:#ffe6e6;
        border:1px solid #ffb3b3;
        font-size:0.9em;
        color:#b30000;
      }

      /*---------------- LAYOUT ADMIN ----------------*/
      nav{
        width:240px;
        background: var(--primary);
        padding:20px;
        display:flex;
        flex-direction:column;
        gap:10px;
        box-shadow: 4px 0 12px rgba(0,0,0,0.1);
      }

      nav h2{
        color:white;
        margin-bottom:15px;
        font-size:1.1em;
        font-weight:700;
      }

      nav button{
        background:white;
        border:none;
        padding:10px 14px;
        border-radius:999px;
        cursor:pointer;
        font-size:0.95em;
        text-align:left;
        transition: transform 0.15s, box-shadow 0.15s, background 0.15s;
      }

      nav button:hover{
        transform: translateY(-1px);
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        background:#fff5f7;
      }

      main{
        flex:1;
        padding:30px 40px;
        display:flex;
        flex-direction:column;
        gap:15px;
      }

      header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:10px;
      }

      header h1{
        font-size:1.4em;
        color:var(--primary);
      }

      .user-actions{
        display:flex;
        gap:10px;
        align-items:center;
        font-size:0.9em;
      }
      .logout-link{
        padding:6px 10px;
        border-radius:999px;
        border:1px solid var(--primary-light);
        color:var(--primary);
        text-decoration:none;
        font-size:0.85em;
        background:white;
      }
      .back-link{
        padding:6px 10px;
        border-radius:999px;
        border:1px solid var(--border);
        color:#555;
        text-decoration:none;
        font-size:0.8em;
        background:white;
        margin-right:10px;
      }

      .table-card,
      .detail-card{
        background:white;
        border-radius:10px;
        padding:20px 24px;
        box-shadow:0 4px 15px rgba(0,0,0,0.08);
        border-top:8px solid var(--primary);
      }

      .table-card h3,
      .detail-card h3{
        margin-bottom:10px;
        font-size:1.1em;
        color:var(--primary);
      }

      .table-card p.description,
      .detail-card p.description{
        margin-bottom:10px;
        font-size:0.9em;
        color:#666;
      }

      table{
        width:100%;
        border-collapse:collapse;
        font-size:0.9em;
      }

      thead th{
        text-align:left;
        padding:10px 8px;
        border-bottom:2px solid var(--primary-light);
        color:var(--primary);
        font-weight:600;
      }

      tbody td{
        padding:8px 8px;
        border-bottom:1px solid var(--border);
        vertical-align:middle;
      }

      tbody tr:nth-child(even){
        background:#fafafa;
      }

      tbody tr:hover{
        background:#ffeef2;
      }

      .estado-pill{
        display:inline-block;
        padding:4px 10px;
        border-radius:999px;
        border:1px solid var(--border);
        font-size:0.8em;
        background:#f9f9f9;
      }
      .estado-pill--vacio{
        color:#999;
        border-style:dashed;
      }

      .form-estado{
        display:flex;
        gap:6px;
        align-items:center;
      }
      .form-estado select{
        padding:4px 6px;
        border-radius:4px;
        border:1px solid var(--border);
        font-size:0.85em;
      }
      .btn-estado{
        padding:4px 8px;
        border-radius:4px;
        border:none;
        background:var(--primary);
        color:white;
        font-size:0.8em;
        cursor:pointer;
      }

      .btn-informe{
        padding:4px 8px;
        border-radius:4px;
        border:none;
        background:#34495e;
        color:white;
        font-size:0.8em;
        cursor:pointer;
        text-decoration:none;
        display:inline-block;
      }

      .badge-unread{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        min-width:22px;
        height:22px;
        border-radius:999px;
        background:#2ecc71;
        color:white;
        font-size:0.75em;
        font-weight:bold;
      }
      .badge-unread::before{
        content:"✉";
        margin-right:3px;
      }
      .badge-none{
        font-size:0.75em;
        color:#aaa;
      }

      /* Detalle */
      .detail-row-table{
        width:100%;
        border-collapse:collapse;
        margin-bottom:20px;
      }
      .detail-row-table th,
      .detail-row-table td{
        padding:6px 8px;
        border-bottom:1px solid var(--border);
        text-align:left;
      }
      .detail-row-table th{
        width:30%;
        color:var(--primary);
      }

      .email-section{
        margin-top:20px;
        display:grid;
        grid-template-columns:1.2fr 1.8fr;
        gap:20px;
      }
      .email-form-card,
      .email-log-card{
        background:#fafafa;
        border-radius:8px;
        padding:15px 18px;
        border:1px solid #e5e5e5;
      }
      .email-form-card h4,
      .email-log-card h4{
        margin-bottom:8px;
        color:#444;
      }
      .email-form-card .form-group{
        margin-bottom:10px;
        display:flex;
        flex-direction:column;
        gap:4px;
      }
      .email-form-card label{
        font-size:0.85em;
        font-weight:600;
      }
      .email-form-card input[type="text"],
      .email-form-card textarea{
        padding:8px 10px;
        border-radius:4px;
        border:1px solid var(--border);
        font-size:0.9em;
        resize:vertical;
      }
      .email-form-card textarea{
        min-height:120px;
      }
      .email-form-card input[type="submit"]{
        margin-top:8px;
        padding:8px 12px;
        border:none;
        border-radius:4px;
        background:var(--primary);
        color:white;
        font-size:0.9em;
        cursor:pointer;
      }
      .email-status-msg{
        margin-bottom:10px;
        padding:6px 8px;
        border-radius:6px;
        font-size:0.85em;
      }
      .email-status-ok{
        background:#e7f7ec;
        border:1px solid #9dd7b1;
        color:#217346;
      }
      .email-status-error{
        background:#ffe6e6;
        border:1px solid #ffb3b3;
        color:#b30000;
      }

      .mail-list{
        max-height:280px;
        overflow:auto;
        font-size:0.86em;
      }
      .mail-item{
        padding:8px 0;
        border-bottom:1px solid #e3e3e3;
      }
      .mail-item:last-child{
        border-bottom:none;
      }
      .mail-item strong{
        color:#333;
      }
      .mail-meta{
        font-size:0.8em;
        color:#777;
        margin-bottom:2px;
      }
      .mail-snippet{
        font-size:0.85em;
        color:#555;
      }

      @media (max-width: 900px){
        body{
          flex-direction:column;
        }
        nav{
          width:100%;
          flex-direction:row;
          flex-wrap:wrap;
          box-shadow:none;
        }
        nav h2{
          width:100%;
        }
        main{
          padding:20px;
        }
        .email-section{
          grid-template-columns:1fr;
        }
      }
    </style>
  </head>
  <body>

  <?php if (!$loggedIn): ?>

    <!-- ------------------ VISTA LOGIN ------------------ -->
    <div class="login-wrapper">
      <form method="post" class="login-card">
        <h2>Acceso al panel</h2>

        <?php if ($login_error !== ""): ?>
          <div class="login-error">
            <?= htmlspecialchars($login_error, ENT_QUOTES, 'UTF-8'); ?>
          </div>
        <?php endif; ?>

        <div class="form-group">
          <label for="usuario">Usuario</label>
          <input type="text" name="usuario" id="usuario" autocomplete="username">
        </div>

        <div class="form-group">
          <label for="password">Contraseña</label>
          <input type="password" name="password" id="password" autocomplete="current-password">
        </div>

        <input type="hidden" name="action" value="login">
        <input type="submit" value="Entrar">
      </form>
    </div>

  <?php else: ?>

    <!-- ------------------ PANEL ADMIN ------------------ -->
    <nav>
      <h2>Menú</h2>
      <button>Enlace 1</button>
      <button>Enlace 2</button>
      <button>Enlace 3</button>
    </nav>
    <main>
      <?php
        $title = $viewId ? "Informe de inscripción" : "Listado de inscripciones";
      ?>
      <header>
        <div style="display:flex; align-items:center; gap:8px;">
          <?php if ($viewId): ?>
            <a href="<?= htmlspecialchars($_SERVER['PHP_SELF'], ENT_QUOTES, 'UTF-8'); ?>" class="back-link">← Volver al listado</a>
          <?php endif; ?>
          <h1><?= htmlspecialchars($title, ENT_QUOTES, 'UTF-8'); ?></h1>
        </div>
        <div class="user-actions">
          <span>Conectado como <strong>jocarsa</strong></span>
          <a class="logout-link" href="?logout=1">Cerrar sesión</a>
        </div>
      </header>

      <?php if ($viewId && $primaryKeyColumn !== null): ?>

        <?php
          // Cargar la fila concreta
          $filaDetalle = null;
          $stmt = $c->prepare("SELECT * FROM inscripciones WHERE $primaryKeyColumn = ? LIMIT 1");
          if ($stmt) {
            $stmt->bind_param("s", $viewId);
            $stmt->execute();
            $result = $stmt->get_result();
            $filaDetalle = $result->fetch_assoc();
            $stmt->close();
          }
        ?>

        <?php if ($filaDetalle): ?>
          <?php
            // Determinar email de contacto (si existe columna de email)
            $contactEmail = null;
            if ($emailColumn !== null && isset($filaDetalle[$emailColumn])) {
              $contactEmail = $filaDetalle[$emailColumn];
            }

            // Obtener comunicaciones por email si tenemos correo
            $commReport = null;
            if ($contactEmail) {
              $commReport = crm_fetch_emails_for_contact($contactEmail, 20);
            }
          ?>

          <section class="detail-card">
            <h3>Datos de la inscripción (ID: <?= htmlspecialchars($viewId, ENT_QUOTES, 'UTF-8'); ?>)</h3>
            <p class="description">
              Detalle completo del registro seleccionado en la tabla
              <strong>inscripciones</strong>, junto con el historial de comunicaciones
              por correo electrónico asociado al contacto.
            </p>

            <table class="detail-row-table">
              <tbody>
                <?php foreach ($filaDetalle as $campo => $valor): ?>
                  <tr>
                    <th><?= htmlspecialchars($campo, ENT_QUOTES, 'UTF-8'); ?></th>
                    <td><?= htmlspecialchars((string)$valor, ENT_QUOTES, 'UTF-8'); ?></td>
                  </tr>
                <?php endforeach; ?>
              </tbody>
            </table>

            <div class="email-section">
              <div class="email-form-card">
                <h4>Enviar mensaje al contacto</h4>

                <?php if ($emailSendMessage): ?>
                  <div class="email-status-msg <?= (strpos($emailSendMessage, 'correctamente') !== false) ? 'email-status-ok' : 'email-status-error'; ?>">
                    <?= $emailSendMessage; ?>
                  </div>
                <?php endif; ?>

                <?php if ($contactEmail): ?>
                  <p style="font-size:0.85em; margin-bottom:8px;">
                    Correo del contacto:
                    <strong><?= htmlspecialchars($contactEmail, ENT_QUOTES, 'UTF-8'); ?></strong><br>
                    Remitente usado: <code><?= htmlspecialchars(CRM_MAIL_USER, ENT_QUOTES, 'UTF-8'); ?></code>
                  </p>

                  <form method="post" action="?view=<?= urlencode($viewId); ?>">
                    <div class="form-group">
                      <label for="subject">Asunto</label>
                      <input type="text" id="subject" name="subject">
                    </div>
                    <div class="form-group">
                      <label for="body">Mensaje</label>
                      <textarea id="body" name="body"></textarea>
                    </div>
                    <input type="hidden" name="to" value="<?= htmlspecialchars($contactEmail, ENT_QUOTES, 'UTF-8'); ?>">
                    <input type="hidden" name="action" value="send_email">
                    <input type="submit" value="Enviar mensaje">
                  </form>
                <?php else: ?>
                  <p style="font-size:0.85em; color:#b30000;">
                    No se ha detectado ninguna columna de email para este registro.  
                    El envío de correos no está disponible.
                  </p>
                <?php endif; ?>
              </div>

              <div class="email-log-card">
                <h4>Comunicaciones por correo</h4>

                <?php if (!$contactEmail): ?>
                  <p style="font-size:0.85em; color:#555;">
                    No hay correo electrónico asociado a este registro.<br>
                    Por tanto, no se puede generar el informe de comunicaciones.
                  </p>
                <?php else: ?>
                  <?php if ($commReport && $commReport['error']): ?>
                    <p style="font-size:0.85em; color:#b30000;">
                      Error al acceder al buzón IMAP:
                      <?= htmlspecialchars($commReport['error'], ENT_QUOTES, 'UTF-8'); ?>
                    </p>
                  <?php else: ?>
                    <div class="mail-list">
                      <?php
                        $sent     = $commReport ? $commReport['sent']     : [];
                        $received = $commReport ? $commReport['received'] : [];
                      ?>

                      <p class="mail-meta">
                        Mensajes enviados: <?= count($sent); ?> |
                        Mensajes recibidos: <?= count($received); ?>
                      </p>

                      <?php if (empty($sent) && empty($received)): ?>
                        <p style="font-size:0.85em; color:#555;">
                          No se han encontrado mensajes relacionados con
                          <strong><?= htmlspecialchars($contactEmail, ENT_QUOTES, 'UTF-8'); ?></strong>.
                        </p>
                      <?php else: ?>

                        <?php if (!empty($sent)): ?>
                          <p style="margin-top:8px; font-weight:bold; font-size:0.9em;">Enviados (<?= count($sent); ?>)</p>
                          <?php foreach ($sent as $mail): ?>
                            <div class="mail-item">
                              <div class="mail-meta">
                                <strong>Asunto:</strong> <?= htmlspecialchars($mail['subject'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>Fecha:</strong> <?= htmlspecialchars($mail['date'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>De:</strong> <?= htmlspecialchars($mail['from'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>Para:</strong> <?= htmlspecialchars($mail['to'], ENT_QUOTES, 'UTF-8'); ?>
                              </div>
                              <div class="mail-snippet">
                                <?= nl2br(htmlspecialchars($mail['snippet'], ENT_QUOTES, 'UTF-8')); ?>
                              </div>
                            </div>
                          <?php endforeach; ?>
                        <?php endif; ?>

                        <?php if (!empty($received)): ?>
                          <p style="margin-top:10px; font-weight:bold; font-size:0.9em;">Recibidos (<?= count($received); ?>)</p>
                          <?php foreach ($received as $mail): ?>
                            <div class="mail-item">
                              <div class="mail-meta">
                                <strong>Asunto:</strong> <?= htmlspecialchars($mail['subject'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>Fecha:</strong> <?= htmlspecialchars($mail['date'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>De:</strong> <?= htmlspecialchars($mail['from'], ENT_QUOTES, 'UTF-8'); ?><br>
                                <strong>Para:</strong> <?= htmlspecialchars($mail['to'], ENT_QUOTES, 'UTF-8'); ?>
                              </div>
                              <div class="mail-snippet">
                                <?= nl2br(htmlspecialchars($mail['snippet'], ENT_QUOTES, 'UTF-8')); ?>
                              </div>
                            </div>
                          <?php endforeach; ?>
                        <?php endif; ?>

                      <?php endif; ?>
                    </div>
                  <?php endif; ?>
                <?php endif; ?>
              </div>
            </div>
          </section>
        <?php else: ?>
          <section class="detail-card">
            <h3>Registro no encontrado</h3>
            <p class="description">
              No se ha podido localizar la inscripción con identificador
              <strong><?= htmlspecialchars($viewId, ENT_QUOTES, 'UTF-8'); ?></strong>.
            </p>
          </section>
        <?php endif; ?>

      <?php else: ?>

        <!-- -------- LISTADO GENERAL DE INSCRIPCIONES -------- -->
        <section class="table-card">
          <h3>Tabla: inscripciones</h3>
          <p class="description">
            Registros actuales en la tabla <strong>inscripciones</strong> de la base de datos
            <strong>training_center</strong>. Puede asignar un estado CRM a cada registro,
            ver si hay correos nuevos sin leer y acceder a un informe detallado.
          </p>

          <table>
            <thead>
              <tr>
                <?php
                /* COLUMNAS CON SUS COMENTARIOS */
                $r = $c->query("
                  SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, COLUMN_DEFAULT, COLUMN_COMMENT
                  FROM information_schema.columns
                  WHERE table_schema='training_center'
                    AND table_name='inscripciones'
                ");

                $columnNames = [];
                while($f = $r->fetch_assoc()) {
                  $columnNames[] = $f['COLUMN_NAME'];
                  echo '<th>'.htmlspecialchars($f['COLUMN_NAME'], ENT_QUOTES, 'UTF-8').'</th>';
                }

                // *** Nueva columna: correos no leídos ***
                echo '<th>Emails nuevos</th>';

                // Columnas extra para estado CRM y acciones
                echo '<th>Estado CRM</th>';
                echo '<th>Acciones</th>';
                ?>
              </tr>
            </thead>
            <tbody>
              <?php
                $r = $c->query("SELECT * FROM inscripciones;");

                while($f = $r->fetch_assoc()) {
                  // ID del registro basado en la columna PK detectada (si existe)
                  $idRegistro = null;
                  if ($primaryKeyColumn !== null && isset($f[$primaryKeyColumn])) {
                    $idRegistro = (string)$f[$primaryKeyColumn];
                  }

                  // Normalizar email de este registro, si existe
                  $rowEmailNorm = null;
                  if ($emailColumn !== null && isset($f[$emailColumn]) && $f[$emailColumn] !== '') {
                    $rowEmailNorm = strtolower(trim($f[$emailColumn]));
                  }

                  echo '<tr>';

                  // Mostrar todas las columnas originales
                  foreach($f as $clave=>$valor){
                    echo '<td>'.htmlspecialchars((string)$valor, ENT_QUOTES, 'UTF-8').'</td>';
                  }

                  // *** Columna Emails nuevos ***
                  echo '<td>';
                  if ($rowEmailNorm && isset($unreadByEmail[$rowEmailNorm])) {
                    echo '<span class="badge-unread" title="Nuevo(s) email(s) sin leer de este contacto.">!</span>';
                  } else {
                    echo '<span class="badge-none">—</span>';
                  }
                  echo '</td>';

                  // Columna "Estado CRM" (pastilla de color)
                  echo '<td>';
                  if ($idRegistro !== null && isset($estadosActuales[$idRegistro])) {
                    $estadoRow = $estadosActuales[$idRegistro];
                    $estadoTxt = htmlspecialchars($estadoRow['estado'], ENT_QUOTES, 'UTF-8');
                    $colorTxt  = htmlspecialchars($estadoRow['color'],  ENT_QUOTES, 'UTF-8');

                    echo '<span class="estado-pill" style="background:'.$colorTxt.'20; border-color:'.$colorTxt.'; color:'.$colorTxt.';">';
                    echo $estadoTxt;
                    echo '</span>';
                  } else {
                    echo '<span class="estado-pill estado-pill--vacio">Sin estado</span>';
                  }
                  echo '</td>';

                  // Columna "Acciones" (selector estado + botón + informe)
                  echo '<td>';
                  if ($idRegistro !== null) {
                    // Formulario de estado
                    echo '<form method="post" class="form-estado" style="margin-bottom:4px;">';
                    echo '<input type="hidden" name="action" value="update_estado">';
                    echo '<input type="hidden" name="id_registro" value="'.htmlspecialchars($idRegistro, ENT_QUOTES, 'UTF-8').'">';
                    echo '<select name="estado">';
                    foreach ($estadosCRM as $nombreEstado => $colorEstado) {
                      $selected = (
                        $idRegistro !== null &&
                        isset($estadosActuales[$idRegistro]) &&
                        $estadosActuales[$idRegistro]['estado'] === $nombreEstado
                      ) ? ' selected' : '';
                      echo '<option value="'.htmlspecialchars($nombreEstado, ENT_QUOTES, 'UTF-8').'"'.$selected.'>';
                      echo htmlspecialchars($nombreEstado, ENT_QUOTES, 'UTF-8');
                      echo '</option>';
                    }
                    echo '</select>';
                    echo '<button type="submit" class="btn-estado">Guardar</button>';
                    echo '</form>';

                    // Enlace a informe
                    $urlInforme = htmlspecialchars($_SERVER['PHP_SELF'], ENT_QUOTES, 'UTF-8') . '?view=' . urlencode($idRegistro);
                    echo '<a class="btn-informe" href="'.$urlInforme.'">Informe</a>';
                  }
                  echo '</td>';

                  echo '</tr>';
                }
              ?>
            </tbody>
          </table>
        </section>

      <?php endif; ?>

    </main>

  <?php endif; ?>

  </body>
</html>
```

### diagrama
<small>Creado: 2025-12-04 15:44</small>

#### Explicación

Este fragmento de código es un archivo JSON que describe el diseño y la conexión de elementos en una interfaz gráfica o diagrama. Cada elemento del diagrama se representa como un rectángulo con diferentes propiedades, como su identificador único (`id`), tipo (como "rectangle"), posición (`left`, `top`) y texto descriptivo. Por ejemplo, el primer objeto en la lista de `"formas"` es un rectángulo que representa un formulario HTML.

Además de los rectángulos, el archivo también incluye una sección para las flechas (`"flechas"`), que muestran cómo estos elementos están conectados o interrelacionados. Por ejemplo, hay una flecha simple que va desde "PHP" hasta "MySQL", sugiriendo la comunicación entre un script PHP y una base de datos MySQL.

Este tipo de diagrama es útil para estudiantes ya que ayuda a visualizar y entender las relaciones entre diferentes tecnologías web (HTML, CSS, PHP, MySQL) en el desarrollo de un formulario. Es importante porque permite organizar mentalmente los pasos necesarios para crear un proyecto web completo desde la recogida de datos hasta su almacenamiento.

`diagrama.json`

```json
{
  "formas": [
    {
      "id": "forma-1",
      "tipo": "rectangle",
      "left": "301.128px",
      "top": "244.632px",
      "width": "",
      "height": "",
      "texto": "Formulario HTML"
    },
    {
      "id": "forma-2",
      "tipo": "rectangle",
      "left": "301.111px",
      "top": "205.211px",
      "width": "",
      "height": "",
      "texto": "CSS"
    },
    {
      "id": "forma-3",
      "tipo": "rectangle",
      "left": "301.124px",
      "top": "290.505px",
      "width": "",
      "height": "",
      "texto": "PHP"
    },
    {
      "id": "forma-4",
      "tipo": "rectangle",
      "left": "408.771px",
      "top": "388.153px",
      "width": "",
      "height": "",
      "texto": "MySQL"
    },
    {
      "id": "forma-5",
      "tipo": "rectangle",
      "left": "498.184px",
      "top": "288.161px",
      "width": "",
      "height": "",
      "texto": "PHP"
    },
    {
      "id": "forma-6",
      "tipo": "rectangle",
      "left": "498.774px",
      "top": "246.976px",
      "width": "",
      "height": "",
      "texto": "HTML"
    },
    {
      "id": "forma-7",
      "tipo": "rectangle",
      "left": "498.185px",
      "top": "206.979px",
      "width": "",
      "height": "",
      "texto": "CSS"
    }
  ],
  "flechas": [
    {
      "desde": {
        "shapeId": "forma-3",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-4",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-4",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-5",
        "propId": null,
        "side": null
      },
      "tipo": "doble",
      "estilo": "straight"
    }
  ]
}
```

### listar_carpetas
<small>Creado: 2025-12-04 16:45</small>

#### Explicación

Este fragmento de código es una parte del archivo `listar_carpetas.php`, donde se conecta a un servidor IMAP (Internet Message Access Protocol) para listar las carpetas o bandejas existentes en la cuenta de correo electrónico especificada. Aquí está el resumen de lo que hace:

1. El código comienza definiendo variables `$host`, `$user` y `$pass`, que representan los detalles necesarios para conectarse al servidor IMAP (en este caso, `imap.ionos.es`). Estas variables incluyen la dirección del host, un usuario específico (`python@jocarsa.com`) y su contraseña (`TAME123$`).

2. Luego se establece una conexión con el servidor IMAP usando la función `imap_open()`. La conexión está configurada para conectarse a la bandeja de entrada (INBOX) del correo electrónico.

3. Si hay un error durante la apertura de la cuenta, el código detiene la ejecución y muestra un mensaje de error que proporciona detalles sobre qué salió mal (`Error IMAP: [descripción del error]`).

4. Después de establecer una conexión exitosa, se intenta obtener una lista de todas las carpetas o bandejas en el servidor con `imap_getmailboxes()`. Si no se pueden recuperar estas carpetas, se muestra un mensaje de error similar al que vimos antes.

5. Finalmente, si la operación es exitosa y se obtienen los nombres de las carpetas, éstos se muestran una por una en el navegador mediante el uso de `echo`. Estos nombres incluyen cualquier prefijo necesario para acceder a ellas usando PHP.

Este código es importante porque permite interactuar con un servidor IMAP desde un script PHP y obtener información valiosa sobre la estructura del correo electrónico, lo cual puede ser útil para desarrollar aplicaciones que necesiten manejar o gestionar correos electrónicos de manera programática.

`listar_carpetas.php`

```
<?php
$host = '{imap.ionos.es:993/imap/ssl}';
$user = 'python@jocarsa.com';
$pass = 'TAME123$';

$mbox = imap_open($host . 'INBOX', $user, $pass);

if (!$mbox) {
    die('Error IMAP: ' . imap_last_error());
}

$folders = imap_getmailboxes($mbox, $host, '*');

if ($folders === false) {
    echo "Error al obtener carpetas: " . imap_last_error();
} else {
    echo "<pre>";
    foreach ($folders as $folder) {
        // Nombre completo que debes usar en PHP (incluyendo el prefijo)
        echo $folder->name . "\n";
    }
    echo "</pre>";
}

imap_close($mbox);
```

### Actividades propuestas

El código proporcionado es un sistema web para gestionar inscripciones a un centro de formación, que incluye funcionalidades como autenticarse en la base de datos MySQL, listar y actualizar registros de inscripciones con estados CRM personalizados, y consultar correos no leídos por cada contacto. A continuación, se detallan los componentes principales del sistema:

1. **Estructura HTML**: 
   - Incluye una parte estática que siempre aparecerá en la página.
   - Secciones dinámicas que cambian según el estado de autenticación y permisos del usuario.

2. **PHP para manejo de sesiones**:
   - Archivo `session.php`: Gestiona las funciones necesarias para iniciar sesión, verificar si un usuario está autenticado, cerrar la sesión actual y registrar mensajes de error o éxito.
   
3. **Conexión a MySQL**:
   - Archivos `conectar_db.php` y `funciones_mysql.php`: Establecen una conexión segura con la base de datos MySQL (`training_center`) y proporcionan funciones para realizar consultas SQL, obtener detalles sobre las columnas de la tabla `inscripciones`, actualizar registros de inscripción y ver correos no leídos.

4. **Interacción con IMAP**:
   - Archivos `funciones_imap.php` y `listar_carpetas.php`: Permiten autenticarse en el servidor IMAP, listar carpetas disponibles y gestionar mensajes de correo electrónico sin leer asociados a cada contacto inscrito (mediante la columna 'email' del registro).

5. **Funcionalidades CRUD**:
   - El sistema proporciona funcionalidades para crear, leer, actualizar y eliminar registros en la tabla `inscripciones`.
   
6. **Formulario de Actualización de Estado CRM**:
   - Permite a los usuarios seleccionar un estado CRM para cada inscripción.
   
7. **Diagrama JSON**:
   - Representa visualmente cómo las partes del sistema interactúan entre sí, mostrando relaciones entre HTML, CSS, PHP y MySQL.

Para mejorar este sistema, se podrían considerar mejoras en términos de seguridad (como hashing de contraseñas), rendimiento y usabilidad para los usuarios finales. Además, la documentación y la estructura del código pueden ser ajustadas para facilitar su mantenimiento a largo plazo.


<a id="panel-de-control-de-tienda-online"></a>
## Panel de control de tienda online

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/010-Proyectos/002-Panel%20de%20control%20de%20tienda%20online)


<a id="libreria-requests"></a>
## Libreria requests

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/010-Proyectos/003-Libreria%20requests)


<a id="shorttags-php"></a>
## shorttags php

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/010-Proyectos/004-shorttags%20php)


<a id="salvapantallas"></a>
## salvapantallas

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/010-Proyectos/005-salvapantallas)



<a id="inteligencia-artificial"></a>
# Inteligencia Artificial

<a id="ia-inicial"></a>
## IA inicial

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/012-Inteligencia%20Artificial/001-IA%20inicial)

### ollama pero lanza HTML
<small>Creado: 2026-01-08 15:02</small>

`002-ollama pero lanza HTML.php`

```
<?php

$prompt = "¿Que es HTML?";

$data = [
    "model"  => "qwen2.5-coder:7b",
    "prompt" => $prompt,
    "stream" => false
];

$ch = curl_init("http://localhost:11434/api/generate"); // Hago una petición a local
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
    CURLOPT_POSTFIELDS     => json_encode($data),
]);

$response = curl_exec($ch);                           // Ejecuto curl

if ($response === false) {
    die("Curl error: " . curl_error($ch));
}                                                     // Si hay respuesta

curl_close($ch);                                      // cierro curl

$result = json_decode($response, true);               // Paso la respuesta a json

echo $result["response"];                             // Y la pinto en pantalla
```

### ollama pero con estilo
<small>Creado: 2026-01-08 15:06</small>

`003-ollama pero con estilo.php`

```
<!doctype html>
<html>
  <head>
    <style>
      html,body{background:grey;width:100%;height:100%;padding:0px;margin:0px;}
      body{display:flex;align-items:center;justify-content:center;}
      section{width:800px;height:300px;padding:20px;background:white;}
    </style>
  </head>
  <body>
    <section>
      <?php
        $prompt = "¿Que es HTML? - responde solo en texto, sin ejemplos, máximo un párrafo";
        $data = [
            "model"  => "qwen2.5-coder:7b",
            "prompt" => $prompt,
            "stream" => false
        ];
        $ch = curl_init("http://localhost:11434/api/generate"); // Hago una petición a local
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST           => true,
            CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
            CURLOPT_POSTFIELDS     => json_encode($data),
        ]);
        $response = curl_exec($ch);                           // Ejecuto curl
        curl_close($ch);                                      // cierro curl
        $result = json_decode($response, true);               // Paso la respuesta a json
        echo $result["response"];                             // Y la pinto en pantalla
      ?>
    </section>
  </body>
</html>
```

### creador web
<small>Creado: 2026-01-08 15:13</small>

`004-creador web.php`

```
<?php
// index.php (single file)
// Minimal markup: the whole page comes from Ollama (it must return a full HTML document).

$prompt = <<<PROMPT
Generate a COMPLETE single-page personal website as a FULL HTML DOCUMENT.

Requirements:
- Output ONLY the HTML document (starting with <!doctype html>), no explanations, no markdown.
- Include inline CSS in <style> and any tiny JS in <script> (no external assets).
- Modern, clean, professional design.
- Sections: Hero (name + role + short bio), Skills/Services, Portfolio (3 items), About, Contact (email + social placeholders), Footer.
- Add a light/dark toggle.
- Use semantic HTML and responsive layout.
- Content language: Spanish.

IMPORTANT: Return ONLY the final HTML document.
PROMPT;

$data = [
  "model"  => "qwen2.5-coder:7b",
  "prompt" => $prompt,
  "stream" => false,
  // optional: keep it deterministic-ish
  "options" => [
    "temperature" => 0.6,
    "num_predict" => 1600
  ]
];

$ch = curl_init("http://localhost:11434/api/generate");
curl_setopt_array($ch, [
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_POST           => true,
  CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
  CURLOPT_POSTFIELDS     => json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
  CURLOPT_TIMEOUT        => 60000000,
]);

$response = curl_exec($ch);
$err      = curl_error($ch);
$code     = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($response === false || $code < 200 || $code >= 300) {
  header("Content-Type: text/plain; charset=utf-8");
  echo "Ollama request failed.\nHTTP: $code\nError: $err\n";
  exit;
}

$result = json_decode($response, true);
$html   = $result["response"] ?? "";

// Ensure browser interprets it as HTML
header("Content-Type: text/html; charset=utf-8");

// If model returned extra text, try to cut from first doctype
$pos = stripos($html, "<!doctype");
if ($pos !== false) $html = substr($html, $pos);

// Last-resort fallback (still minimal): show raw response if not HTML-ish
if (stripos($html, "<html") === false) {
  echo "<!doctype html><html><head><meta charset='utf-8'><title>Ollama Output</title></head><body><pre>";
  echo htmlspecialchars($html, ENT_QUOTES | ENT_SUBSTITUTE, "UTF-8");
  echo "</pre></body></html>";
  exit;
}

echo $html;
```

### creador web con mas definicion
<small>Creado: 2026-01-08 15:17</small>

`006-creador web con mas definicion.php`

```
<?php
// index.php (single file)
// Minimal markup: the whole page comes from Ollama (it must return a full HTML document).

$prompt = <<<PROMPT
Generate a COMPLETE single-page personal website as a FULL HTML DOCUMENT.

Requirements:
- Output ONLY the HTML document (starting with <!doctype html>), no explanations, no markdown.
- Include inline CSS in <style> and any tiny JS in <script> (no external assets).
- In the CSS, use indigo as corporate color
- Modern, clean, professional design.
- Website is about person: Jose Vicente Carratala
- Sections: Hero (name + role + short bio), Skills/Services, Portfolio (9 items), About, Contact (email + social placeholders), Footer.
- use css grid for portfolio (3 columns)
- Add a light/dark toggle.
- Use semantic HTML and responsive layout.
- Content language: Spanish.

IMPORTANT: Return ONLY the final HTML document.
PROMPT;

$data = [
  "model"  => "qwen2.5-coder:7b",
  "prompt" => $prompt,
  "stream" => false,
  // optional: keep it deterministic-ish
  "options" => [
    "temperature" => 0.6,
    "num_predict" => 1600
  ]
];

$ch = curl_init("http://localhost:11434/api/generate");
curl_setopt_array($ch, [
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_POST           => true,
  CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
  CURLOPT_POSTFIELDS     => json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
  CURLOPT_TIMEOUT        => 60000000,
]);

$response = curl_exec($ch);
$err      = curl_error($ch);
$code     = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($response === false || $code < 200 || $code >= 300) {
  header("Content-Type: text/plain; charset=utf-8");
  echo "Ollama request failed.\nHTTP: $code\nError: $err\n";
  exit;
}

$result = json_decode($response, true);
$html   = $result["response"] ?? "";

// Ensure browser interprets it as HTML
header("Content-Type: text/html; charset=utf-8");

// If model returned extra text, try to cut from first doctype
$pos = stripos($html, "<!doctype");
if ($pos !== false) $html = substr($html, $pos);

// Last-resort fallback (still minimal): show raw response if not HTML-ish
if (stripos($html, "<html") === false) {
  echo "<!doctype html><html><head><meta charset='utf-8'><title>Ollama Output</title></head><body><pre>";
  echo htmlspecialchars($html, ENT_QUOTES | ENT_SUBSTITUTE, "UTF-8");
  echo "</pre></body></html>";
  exit;
}

echo $html;
```

### aplicació de citas inspiradoras
<small>Creado: 2026-01-08 15:32</small>

`007-aplicació de citas inspiradoras.php`

```
<!doctype html>
<html>
  <head>
    <style>
      html,body{background:grey;width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;align-items:center;justify-content:center;}
      h1{width:800px;height:300px;padding:20px;background:white;display:flex;align-items:center;justify-content:center;font-style:italic;border-radius:10px;}
    </style>
  </head>
  <body>
    <h1>
      <?php
        $prompt = "
          Dame una cita inspiradora, solo  una frase.
          Introducela en un <span> HTML
          En el span, introduce un estilo color CSS
          el color CSS debe transmitir el sentimiento que transmita la frase (por ejemplo: rojo = pasión)
          Dame solo el span con el color, no me des explicaciones
          Tampoco me pongas fences
          ";
        $data = [
            "model"  => "qwen2.5-coder:7b",
            "prompt" => $prompt,
            "stream" => false
        ];
        $ch = curl_init("http://localhost:11434/api/generate"); // Hago una petición a local
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST           => true,
            CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
            CURLOPT_POSTFIELDS     => json_encode($data),
        ]);
        $response = curl_exec($ch);                           // Ejecuto curl
        curl_close($ch);                                      // cierro curl
        $result = json_decode($response, true);               // Paso la respuesta a json
        echo $result["response"];                             // Y la pinto en pantalla
      ?>
    </h1>
  </body>
</html>
```

### microchatgpt
<small>Creado: 2026-01-08 15:43</small>

`008-microchatgpt.php`

```
<!doctype html>
<html>
  <head>
    <style>
  html,body{
    background:grey;
    width:100%;
    height:100%;
    padding:0;
    margin:0;
    font-family:sans-serif;
  }

  body{
    display:flex;
    align-items:center;
    justify-content:center;
  }

  section{
    width:500px;
    height:500px;
    padding:20px;
    background:white;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    align-items:stretch;
    font-style:italic;
    border-radius:10px;
  }

  form input{
    width:100%;
    box-sizing:border-box;
    padding:10px;
    border:1px solid lightgrey;
    border-radius:30px;
    outline:none;
  }

  form input:focus{
    background:lightgray;
  }

  #pregunta{
    background:lightgray;
    width:80%;
    padding:20px;
    border-radius:0 15px 15px 15px;
    align-self:flex-start;
  }

  #respuesta{
    background:lightgray;
    width:80%;
    padding:20px;
    border-radius:15px 0 15px 15px;
    align-self:flex-end; /* ← THIS is the key */
    text-align:left;
  }
</style>

  </head>
  <body>
    <section>
      <p id="pregunta">
        <?php
          if(isset($_POST['prompt'])){echo $_POST['prompt'];}
        ?>
      </p>
      <p id="respuesta">Respuesta</p>
      <form method="POST" action="?">
        <input type="text" name="prompt">
      </form>
    </section>
  </body>
</html>
```

### microchatgpt pero en funcionamiento
<small>Creado: 2026-01-08 16:04</small>

`009-microchatgpt pero en funcionamiento.php`

```
<!doctype html>
<html>
  <head>
    <style>
  html,body{
    background:grey;
    width:100%;
    height:100%;
    padding:0;
    margin:0;
    font-family:sans-serif;
  }

  body{
    display:flex;
    align-items:center;
    justify-content:center;
  }

  section{
    width:500px;
    height:500px;
    padding:20px;
    background:white;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    align-items:stretch;
    border-radius:30px;
  }

  form input{
    width:100%;
    box-sizing:border-box;
    padding:10px;
    border:1px solid lightgrey;
    border-radius:30px;
    outline:none;
  }

  form input:focus{
    background:lightgray;
  }

  #pregunta{
    background:lightgray;
    width:80%;
    padding:20px;
    border-radius:0 15px 15px 15px;
    align-self:flex-start;
  }

  #respuesta{
    background:lightgray;
    width:80%;
    padding:20px;
    border-radius:15px 0 15px 15px;
    align-self:flex-end; /* ← THIS is the key */
    text-align:left;
  }
  p{
    margin:0px;
    padding:0px;
  }
  h1{
    text-align:center;
  }
</style>

  </head>
  <body>
    <section>
      <h1>jocarsa | microchat</h1>
      <p id="pregunta">
        <?php
          if(isset($_POST['prompt'])){echo $_POST['prompt'];}
        ?>
      </p>
      <p id="respuesta">
        <?php
          if(isset($_POST['prompt'])){
            $prompt = $_POST['prompt']." - responde en un solo párrafo, sin código, en prosa.";
            $data = [
                "model"  => "qwen2.5:7b-instruct-q4_0",
                "prompt" => $prompt,
                "stream" => false
            ];
            $ch = curl_init("http://localhost:11434/api/generate"); // Hago una petición a local
            curl_setopt_array($ch, [
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_POST           => true,
                CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
                CURLOPT_POSTFIELDS     => json_encode($data),
            ]);
            $response = curl_exec($ch);                           // Ejecuto curl
            curl_close($ch);                                      // cierro curl
            $result = json_decode($response, true);               // Paso la respuesta a json
            echo $result["response"];                             // Y la pinto en pantalla
          }
        ?>
      </p>
      <form method="POST" action="?">
        <input type="text" name="prompt">
      </form>
    </section>
  </body>
</html>
```

### personalizar prompt en programacion
<small>Creado: 2026-01-08 16:12</small>

`010-personalizar prompt en programacion.php`

```
<!doctype html>
<html>
  <head>
    <style>
  html,body{
    background:lightgray;
    width:100%;
    height:100%;
    padding:0;
    margin:0;
    font-family:Ubuntu,sans-serif;
  }

  body{
    display:flex;
    align-items:center;
    justify-content:center;
  }

  section{
    width:500px;
    height:500px;
    padding:20px;
    background:white;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    align-items:stretch;
    border-radius:30px;
  }

  form input{
    width:100%;
    box-sizing:border-box;
    padding:10px;
    border:1px solid lightgrey;
    border-radius:30px;
    outline:none;
    transition:all 1s;
  }

  form input:focus{
    background:lightgray;
    box-shadow:0px 10px 20px rgba(0,0,0,0.3) inset;
  }

  #pregunta{
    background:lightgray;
    width:80%;
    padding:20px;
    border-radius:0 15px 15px 15px;
    align-self:flex-start;
  }

  #respuesta{
    background:lightgray;
    width:80%;
    padding:20px;
    border-radius:15px 0 15px 15px;
    align-self:flex-end; /* ← THIS is the key */
    text-align:left;
  }
  p{
    margin:0px;
    padding:0px;
  }
  h1,h3{
    text-align:center;
  }
</style>

  </head>
  <body>
    <section>
      <h1>jocarsa | microchat</h1>  
      <?php
          if(!isset($_POST['prompt'])){
            echo '<h3>¿Qué quieres hacer hoy?</h3>';
            
            }
        ?>
        <?php
          if(isset($_POST['prompt'])){
            echo '<p id="pregunta">';
            echo $_POST['prompt'];
            echo '</p>';
            }
        ?>
      
        <?php
          if(isset($_POST['prompt'])){
          echo '<p id="respuesta">';
            $prompt = $_POST['prompt']." 
            - responde en un solo párrafo, sin código, en prosa.
            - acepta solo preguntas relacionadas con programación, no aceptes otras temáticas";
            $data = [
                "model"  => "qwen2.5:7b-instruct-q4_0",
                "prompt" => $prompt,
                "stream" => false
            ];
            $ch = curl_init("http://localhost:11434/api/generate"); // Hago una petición a local
            curl_setopt_array($ch, [
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_POST           => true,
                CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
                CURLOPT_POSTFIELDS     => json_encode($data),
            ]);
            $response = curl_exec($ch);                           // Ejecuto curl
            curl_close($ch);                                      // cierro curl
            $result = json_decode($response, true);               // Paso la respuesta a json
            echo $result["response"];                             // Y la pinto en pantalla
            echo '</p>';
          }
        ?>
      
      <form method="POST" action="?">
        <input type="text" name="prompt">
      </form>
    </section>
  </body>
</html>
```

### spinner
<small>Creado: 2026-01-08 16:15</small>

`011-spinner.php`

```
<?php
session_start();

function ask_ollama(string $userPrompt): string {
  $prompt = $userPrompt . "
  - responde en un solo párrafo, sin código, en prosa.
  - acepta solo preguntas relacionadas con programación, no aceptes otras temáticas";

  $data = [
    "model"  => "qwen2.5:7b-instruct-q4_0",
    "prompt" => $prompt,
    "stream" => false
  ];

  $ch = curl_init("http://localhost:11434/api/generate");
  curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
    CURLOPT_POSTFIELDS     => json_encode($data),
  ]);
  $response = curl_exec($ch);
  curl_close($ch);

  $result = json_decode($response ?? "", true);
  return $result["response"] ?? "Error: no se pudo obtener respuesta.";
}

$pregunta = null;
$respuesta = null;
$showSpinner = false;
$metaRefresh = "";

// Step A: user submits -> render page with spinner, compute answer on server AFTER flush
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["prompt"])) {
  $pregunta = trim((string)$_POST["prompt"]);
  $_SESSION["last_prompt"] = $pregunta;
  $_SESSION["answer_ready"] = false;
  $_SESSION["last_answer"] = "";

  $showSpinner = true;

  // Auto-refresh once to replace spinner with answer (no JS)
  $metaRefresh = '<meta http-equiv="refresh" content="0.8;url=?step=answer">';

  // Render immediately (spinner visible)
  // Then finish request and compute answer (so user sees spinner right away)
  // ---- render starts below ----

  // We'll compute after output is flushed (down below).
}

// Step B: answer page (after refresh)
if (isset($_GET["step"]) && $_GET["step"] === "answer") {
  $pregunta = $_SESSION["last_prompt"] ?? null;

  if (!empty($_SESSION["answer_ready"])) {
    $respuesta = $_SESSION["last_answer"] ?? "";
    $showSpinner = false;
  } else {
    // If answer not ready yet, keep spinner + refresh again
    $showSpinner = true;
    $metaRefresh = '<meta http-equiv="refresh" content="0.8;url=?step=answer">';
  }
}
?>
<!doctype html>
<html>
<head>
  <style>
    html,body{background:lightgray;width:100%;height:100%;padding:0;margin:0;font-family:Ubuntu,sans-serif;}
    body{display:flex;align-items:center;justify-content:center;}
    section{width:500px;height:500px;padding:20px;background:white;display:flex;flex-direction:column;justify-content:space-between;align-items:stretch;border-radius:30px;}
    form input{width:100%;box-sizing:border-box;padding:10px;border:1px solid lightgrey;border-radius:30px;outline:none;transition:all 1s;}
    form input:focus{background:lightgray;box-shadow:0px 10px 20px rgba(0,0,0,0.3) inset;}
    #pregunta{background:lightgray;width:80%;padding:20px;border-radius:0 15px 15px 15px;align-self:flex-start;}
    #respuesta{background:lightgray;width:80%;padding:20px;border-radius:15px 0 15px 15px;align-self:flex-end;text-align:left;min-height:54px;display:flex;align-items:center;gap:12px;}
    p{margin:0;padding:0;}
    h1,h3{text-align:center;}

    /* Simple spinner */
    .spinner{
      width:18px;height:18px;border-radius:50%;
      border:3px solid rgba(0,0,0,0.15);
      border-top-color: rgba(0,0,0,0.55);
      animation: spin .8s linear infinite;
      flex: 0 0 auto;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    .muted{opacity:.7;font-size:13px;}
  </style>
  <?= $metaRefresh ?>
</head>
<body>
<section>
  <h1>jocarsa | microchat</h1>

  <?php if (!$pregunta): ?>
    <h3>¿Qué quieres hacer hoy?</h3>
  <?php else: ?>
    <p id="pregunta"><?= htmlspecialchars($pregunta, ENT_QUOTES, "UTF-8") ?></p>

    <p id="respuesta">
      <?php if ($showSpinner): ?>
        <span class="spinner"></span>
        <span class="muted">Pensando…</span>
      <?php else: ?>
        <?= htmlspecialchars((string)$respuesta, ENT_QUOTES, "UTF-8") ?>
      <?php endif; ?>
    </p>
  <?php endif; ?>

  <form method="POST" action="?">
    <input type="text" name="prompt" autocomplete="off" autofocus>
  </form>
</section>
</body>
</html>
<?php
// If we came from POST, compute the answer after sending HTML so spinner shows immediately.
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["prompt"])) {
  // Try to flush output so browser renders spinner
  @ob_flush(); @flush();

  // If PHP-FPM, this sends response to client and continues running server-side
  if (function_exists("fastcgi_finish_request")) {
    @fastcgi_finish_request();
  }

  $ans = ask_ollama($_SESSION["last_prompt"] ?? "");
  $_SESSION["last_answer"] = $ans;
  $_SESSION["answer_ready"] = true;
}
```

### mejoras de estilo
<small>Creado: 2026-01-08 16:20</small>

`012-mejoras de estilo.php`

```
<?php
session_start();

/**
 * Call Ollama (blocking) and return the response text.
 */
function ask_ollama(string $userPrompt): string {
  $prompt = $userPrompt . "
  - responde en un solo párrafo, sin código, en prosa.
  - acepta solo preguntas relacionadas con programación, no aceptes otras temáticas
  - respuestas solo en español";

  $data = [
    "model"  => "qwen2.5:7b-instruct-q4_0",
    "prompt" => $prompt,
    "stream" => false
  ];

  $ch = curl_init("http://localhost:11434/api/generate");
  curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
    CURLOPT_POSTFIELDS     => json_encode($data),
  ]);
  $response = curl_exec($ch);
  curl_close($ch);

  $result = json_decode($response ?? "", true);
  return $result["response"] ?? "Error: no se pudo obtener respuesta.";
}

$pregunta = null;
$respuesta = null;
$showSpinner = false;
$metaRefresh = "";

/**
 * STEP A: POST -> show page immediately with spinner, compute answer after flush,
 * then page auto-refreshes to show answer.
 */
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["prompt"])) {
  $pregunta = trim((string)$_POST["prompt"]);

  $_SESSION["last_prompt"]  = $pregunta;
  $_SESSION["last_answer"]  = "";
  $_SESSION["answer_ready"] = false;

  $showSpinner = true;
  $metaRefresh = '<meta http-equiv="refresh" content="0.8;url=?step=answer">';
}

/**
 * STEP B: answer step (after refresh)
 */
if (isset($_GET["step"]) && $_GET["step"] === "answer") {
  $pregunta = $_SESSION["last_prompt"] ?? null;

  if (!empty($_SESSION["answer_ready"])) {
    $respuesta = $_SESSION["last_answer"] ?? "";
    $showSpinner = false;
  } else {
    $showSpinner = true;
    $metaRefresh = '<meta http-equiv="refresh" content="0.8;url=?step=answer">';
  }
}
?>
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>jocarsa | microchat</title>

  <?= $metaRefresh ?>

  <style>
    :root{
      --bg: #eef1f4;
      --card: #ffffff;
      --ink: #111827;
      --muted: #6b7280;
      --line: #e5e7eb;
      --soft: #f3f4f6;
      --shadow: 0 18px 50px rgba(0,0,0,.12);
      --shadow-soft: 0 10px 25px rgba(0,0,0,.08);
      --radius: 22px;
    }

    *{ box-sizing:border-box; }

    html,body{
      width:100%;
      height:100%;
      margin:0;
      padding:0;
      font-family: Ubuntu, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      color: var(--ink);
      background:
        radial-gradient(1200px 600px at 20% 10%, rgba(255,255,255,.7), transparent 60%),
        radial-gradient(900px 500px at 90% 30%, rgba(255,255,255,.55), transparent 55%),
        var(--bg);
    }

    body{
      display:flex;
      align-items:center;
      justify-content:center;
      padding:24px;
    }

    section{
      width:min(560px, 100%);
      height:min(560px, 100%);
      background:var(--card);
      border:1px solid rgba(0,0,0,.06);
      border-radius: calc(var(--radius) + 6px);
      box-shadow: var(--shadow);
      padding:22px;
      display:flex;
      flex-direction:column;
      gap:14px;
      overflow:hidden;
    }

    .titleWrap{
      display:flex;
      align-items:flex-start;
      justify-content:space-between;
      gap:12px;
      padding-bottom:10px;
      border-bottom:1px solid var(--line);
    }

    h1{
      margin:0;
      font-size:18px;
      letter-spacing:.2px;
      font-weight:700;
      line-height:1.2;
    }

    .badge{
      font-size:12px;
      color:var(--muted);
      background:var(--soft);
      border:1px solid rgba(0,0,0,.05);
      padding:6px 10px;
      border-radius:999px;
      white-space:nowrap;
    }

    h3{
      margin:6px 0 0 0;
      text-align:center;
      font-size:14px;
      font-weight:600;
      color:var(--muted);
    }

    .messages{
      flex:1;
      display:flex;
      flex-direction:column;
      gap:12px;
      padding:6px 2px;
      overflow:auto;
    }

    .bubble{
      width:fit-content;
      max-width: 86%;
      padding:12px 14px;
      background:var(--soft);
      border:1px solid rgba(0,0,0,.06);
      border-radius:16px;
      box-shadow: var(--shadow-soft);
      line-height:1.35;
      font-size:14px;
      white-space:pre-wrap;
      word-break:break-word;
    }

    #pregunta{
      align-self:flex-start;
      border-top-left-radius:8px;
    }

    #respuesta{
      align-self:flex-end;
      border-top-right-radius:8px;
      display:flex;
      align-items:center;
      gap:10px;
      min-height:46px;
    }

    form{
      padding-top:12px;
      border-top:1px solid var(--line);
    }

    form input{
      width:100%;
      padding:12px 14px;
      border-radius:999px;
      border:1px solid var(--line);
      background:#fff;
      outline:none;
      font-size:14px;
      box-shadow: 0 1px 0 rgba(0,0,0,.02);
      transition: border-color .2s ease, box-shadow .2s ease, background .2s ease;
    }

    form input::placeholder{ color:#9ca3af; }

    form input:focus{
      border-color: rgba(17,24,39,.35);
      box-shadow: 0 0 0 4px rgba(17,24,39,.08);
      background:#fff;
    }

    .spinner{
      width:16px;
      height:16px;
      border-radius:50%;
      border:3px solid rgba(17,24,39,0.12);
      border-top-color: rgba(17,24,39,0.55);
      animation: spin .8s linear infinite;
      flex:0 0 auto;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    .muted{
      font-size:13px;
      color:var(--muted);
    }

    .messages::-webkit-scrollbar{ width:10px; }
    .messages::-webkit-scrollbar-thumb{
      background: rgba(0,0,0,.10);
      border-radius:999px;
      border:3px solid transparent;
      background-clip: content-box;
    }

    @media (max-width: 520px){
      section{ height: 92vh; padding:18px; }
      .bubble{ max-width: 92%; }
    }
  </style>
</head>
<body>
  <section>
    <div class="titleWrap">
      <h1>jocarsa | microchat</h1>
      <span class="badge">local</span>
    </div>

    <div class="messages">
      <?php if (!$pregunta): ?>
        <h3>¿Qué quieres hacer hoy?</h3>
      <?php else: ?>
        <p id="pregunta" class="bubble"><?= htmlspecialchars($pregunta, ENT_QUOTES, "UTF-8") ?></p>

        <p id="respuesta" class="bubble">
          <?php if ($showSpinner): ?>
            <span class="spinner"></span>
            <span class="muted">Pensando…</span>
          <?php else: ?>
            <?= htmlspecialchars((string)$respuesta, ENT_QUOTES, "UTF-8") ?>
          <?php endif; ?>
        </p>
      <?php endif; ?>
    </div>

    <form method="POST" action="?">
      <input
        type="text"
        name="prompt"
        placeholder="Escribe una pregunta sobre programación y pulsa Enter…"
        autocomplete="off"
        autofocus
      >
    </form>
  </section>
</body>
</html>
<?php
// If we came from POST, compute the answer after the HTML has been sent
// so the user sees the spinner immediately.
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["prompt"])) {
  @ob_flush(); @flush();

  if (function_exists("fastcgi_finish_request")) {
    @fastcgi_finish_request();
  }

  $ans = ask_ollama($_SESSION["last_prompt"] ?? "");
  $_SESSION["last_answer"]  = $ans;
  $_SESSION["answer_ready"] = true;
}
```



<a id="milla-extra-evaluacion-1"></a>
# Milla Extra Evaluacion 1


<a id="actividad-libre-de-final-de-evaluacion-la-milla-extra"></a>
# Actividad libre de final de evaluación - La milla extra

<a id="la-milla-extra-primera-evaluacion"></a>
## La Milla Extra - Primera evaluación

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/dam2526/tree/main/Primero/Programaci%C3%B3n/201-Actividad%20libre%20de%20final%20de%20evaluaci%C3%B3n%20-%20La%20milla%20extra/001-La%20Milla%20Extra%20-%20Primera%20evaluaci%C3%B3n)

### Introducción a los ejercicios

El archivo proporcionado en la carpeta "ejercicios" contiene un conjunto de problemas diseñados para evaluar y mejorar tus habilidades en programación, específicamente enfocadas a estudiantes del segundo curso de Formación Profesional. Estos ejercicios buscan que apliques conceptos como estructuras de control (condicionales y bucles), manejo de datos (listas, diccionarios) y funciones para resolver problemas prácticos. La idea es reforzar tus competencias en resolución de problemas algoritímicos y mejorar tu capacidad para escribir código eficiente y limpio.

### Actividades propuestas

Basándome en las instrucciones y suponiendo que los ejercicios dentro del archivo `ejercicio.md` están relacionados con conceptos básicos de programación, estructuras de control (como condicionales y bucles), manejo de funciones y posiblemente el uso de listas o arrays, propongo las siguientes actividades para estudiantes de Formación Profesional:

1. **Reconocimiento del Problema**
   - Descripción: Identifica los problemas presentados en los ejercicios proporcionados y describe cómo se podrían solucionar.
   - Objetivo: Aprender a analizar problemas de programación y proponer soluciones iniciales.

2. **Estructuras de Control Personalizadas**
   - Descripción: Diseña nuevas estructuras de control basándote en ejemplos proporcionados, pero aplicando conceptos aprendidos.
   - Objetivo: Mejorar la comprensión y aplicación de condicionales y bucles.

3. **Funciones Mejoradas**
   - Descripción: Implementa funciones que realicen tareas más complejas basándose en ejemplos proporcionados, mejorando la eficiencia del código.
   - Objetivo: Aprender a modularizar el código y mejorar sus capacidades de reutilización.

4. **Optimización de Código**
   - Descripción: Analiza el código existente para identificar áreas que puedan ser optimizadas, mejorando la eficiencia del programa.
   - Objetivo: Aprender a leer y optimizar el código existente.

5. **Manejo de Listas Avanzado**
   - Descripción: Trabaja con listas o arrays para realizar operaciones más complejas como filtrar, ordenar y buscar elementos específicos.
   - Objetivo: Aprender a manejar datos estructurados de manera eficiente.

6. **Integración de Funciones**
   - Descripción: Combinar varias funciones en un solo programa para resolver problemas más grandes que requieren múltiples pasos.
   - Objetivo: Mejorar la capacidad de integrar diferentes partes del código en una solución completa.

7. **Pruebas y Depuración**
   - Descripción: Realiza pruebas unitarias y busca errores en el código proporcionado, corrigiéndolos para mejorar su funcionalidad.
   - Objetivo: Aprender a depurar y probar programas de manera efectiva.

8. **Documentación del Código**
   - Descripción: Escribe documentación clara que explique cómo funciona el programa y qué hace cada parte del código.
   - Objetivo: Mejorar la habilidad para comunicarse sobre las soluciones de programación de una manera accesible.

Estas actividades están diseñadas para ayudar a los estudiantes a profundizar en sus conocimientos de programación, mejorando no solo su capacidad técnica sino también sus habilidades de resolución de problemas y comunicación.
