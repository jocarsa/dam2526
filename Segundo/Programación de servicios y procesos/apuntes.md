# Programación de servicios y procesos

**Author:** Jose Vicente Carratala Sanchis

## Table of contents

- [Programación multiproceso](#programacion-multiproceso)
  - [Ejecutables. Procesos. Servicios](#ejecutables-procesos-servicios)
  - [Estados de un proceso. Planificación de procesos](#estados-de-un-proceso-planificacion-de-procesos)
  - [Hilos](#hilos)
  - [Programación concurrente](#programacion-concurrente)
  - [Programación paralela y distribuida](#programacion-paralela-y-distribuida)
  - [Comunicación entre procesos](#comunicacion-entre-procesos)
  - [Gestión de procesos. Herramientas de monitorización](#gestion-de-procesos-herramientas-de-monitorizacion)
  - [Sincronización entre procesos](#sincronizacion-entre-procesos)
  - [Programación de aplicaciones multiproceso](#programacion-de-aplicaciones-multiproceso)
  - [Ollama](#ollama)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad)
  - [Examen final](#examen-final)
- [Programación multihilo](#programacion-multihilo)
  - [Contexto de ejecución de los hilos](#contexto-de-ejecucion-de-los-hilos)
  - [Estados de un hilo. Cambios de estado](#estados-de-un-hilo-cambios-de-estado)
  - [Librerías y clases](#librerias-y-clases)
  - [Gestión de hilos. Prioridades](#gestion-de-hilos-prioridades)
  - [Sincronización de hilos](#sincronizacion-de-hilos)
  - [Compartición de información entre hilos](#comparticion-de-informacion-entre-hilos)
  - [Programación de aplicaciones multihilo](#programacion-de-aplicaciones-multihilo)
- [Programación de comunicaciones en red](#programacion-de-comunicaciones-en-red)
  - [Comunicación entre aplicaciones](#comunicacion-entre-aplicaciones)
  - [Roles cliente y servidor](#roles-cliente-y-servidor)
  - [Librerías y clases](#librerias-y-clases-1)
  - [Sockets. Tipos. Características](#sockets-tipos-caracteristicas)
  - [Creación de sockets](#creacion-de-sockets)
  - [Enlazado y establecimiento de conexiones](#enlazado-y-establecimiento-de-conexiones)
  - [Utilización de sockets para la transmisión y recepción de información](#utilizacion-de-sockets-para-la-transmision-y-recepcion-de-informacion)
  - [Programación de aplicaciones cliente y servidor](#programacion-de-aplicaciones-cliente-y-servidor)
  - [Utilización de hilos para la implementación de comunicaciones simultáneas con el servidor](#utilizacion-de-hilos-para-la-implementacion-de-comunicaciones-simultaneas-con-el-servidor)
- [Generación de servicios en red](#generacion-de-servicios-en-red)
  - [Protocolos estándar de comunicación en red a nivel de aplicación](#protocolos-estandar-de-comunicacion-en-red-a-nivel-de-aplicacion)
  - [Servicios web](#servicios-web)
  - [Librerías de clases y componentes](#librerias-de-clases-y-componentes)
  - [Programación de servidores](#programacion-de-servidores)
  - [Establecimiento y finalización de conexiones](#establecimiento-y-finalizacion-de-conexiones)
  - [Transmisión de información](#transmision-de-informacion)
  - [Implementación de comunicaciones simultáneas](#implementacion-de-comunicaciones-simultaneas)
  - [Utilización de aplicaciones clientes](#utilizacion-de-aplicaciones-clientes)
  - [Monitorización del servicio. Herramientas](#monitorizacion-del-servicio-herramientas)
- [Utilización de técnicas de programación segura](#utilizacion-de-tecnicas-de-programacion-segura)
  - [Prácticas de programación segura](#practicas-de-programacion-segura)
  - [Criptografía de clave pública y clave privada](#criptografia-de-clave-publica-y-clave-privada)
  - [Principales aplicaciones de la criptografía](#principales-aplicaciones-de-la-criptografia)
  - [Protocolos criptográficos](#protocolos-criptograficos)
  - [Política de seguridad. Roles](#politica-de-seguridad-roles)
  - [Programación de mecanismos de control de acceso](#programacion-de-mecanismos-de-control-de-acceso)
  - [Encriptación de información](#encriptacion-de-informacion)
  - [Protocolos seguros de comunicaciones](#protocolos-seguros-de-comunicaciones)
  - [Programación de aplicaciones con comunicaciones seguras](#programacion-de-aplicaciones-con-comunicaciones-seguras)
- [Actividad libre de final de evaluación - La milla extra](#actividad-libre-de-final-de-evaluacion-la-milla-extra)
  - [La Milla Extra - Primera evaluación](#la-milla-extra-primera-evaluacion)

---

<a id="programacion-multiproceso"></a>
# Programación multiproceso

<a id="ejecutables-procesos-servicios"></a>
## Ejecutables. Procesos. Servicios

En un mundo digital cada vez más complejo, la programación multiproceso es una habilidad fundamental para desarrolladores que desean crear aplicaciones eficientes y escalables. Los ejecutables son los programas binarios que se pueden ejecutar directamente por el sistema operativo, mientras que los procesos son instancias de ejecutables en ejecución. Cada proceso tiene su propio espacio de memoria y recursos, lo que permite la paralelización de tareas.

Los servicios, por otro lado, son una forma especial de proceso que se ejecutan en segundo plano y están diseñados para proporcionar funcionalidades a otros programas o sistemas. Pueden ser iniciados automáticamente al arrancar el sistema operativo y pueden funcionar incluso cuando no hay ninguna interfaz gráfica de usuario activa.

La programación multiproceso implica la creación, gestión y sincronización de múltiples procesos simultáneamente. Esto requiere un buen entendimiento del ciclo de vida de los procesos, desde su creación hasta su finalización, incluyendo el manejo de recursos compartidos y la comunicación entre procesos.

Para implementar programación multiproceso en aplicaciones modernas, se utilizan bibliotecas y frameworks específicos que facilitan la creación y gestión de procesos. Estas herramientas proporcionan funciones para crear nuevos procesos, compartir datos entre ellos y coordinar su ejecución.

La sincronización entre procesos es un desafío importante en programación multiproceso. Se requiere un mecanismo eficiente para garantizar que los procesos accedan a recursos compartidos de manera segura y coherente. Esto puede implicar la utilización de semáforos, barreras o variables de condición.

Además de la sincronización, la programación multiproceso también implica el manejo de errores y excepciones. Es crucial tener en cuenta que cualquier error en un proceso puede afectar a otros procesos compartiendo recursos. Por lo tanto, es importante implementar mecanismos robustos para capturar y gestionar excepciones.

La programación multiproceso no solo mejora la eficiencia de las aplicaciones, sino que también facilita el desarrollo de sistemas distribuidos y escalables. Al permitir la paralelización de tareas, los procesos pueden ejecutarse en diferentes núcleos del procesador o incluso en diferentes máquinas, lo que aumenta significativamente su capacidad para manejar cargas de trabajo intensivas.

En conclusión, la programación multiproceso es una técnica poderosa y fundamental para el desarrollo moderno de aplicaciones. Permite crear sistemas eficientes, escalables y robustos que pueden manejar complejas tareas en paralelo. A través del uso adecuado de ejecutables, procesos y servicios, los desarrolladores pueden aprovechar al máximo las capacidades del hardware y optimizar el rendimiento de sus aplicaciones.

### proceso

```python
numero = 1.0000000098
print("empiezo")
for i in range(0,1000000000):
    numero *= 1.0000000000654
print("acabo")




    
```

<a id="estados-de-un-proceso-planificacion-de-procesos"></a>
## Estados de un proceso. Planificación de procesos

En el mundo de la programación multiproceso, los procesos son unidades fundamentales que realizan tareas específicas dentro de un sistema operativo. Cada proceso tiene un estado que describe su situación actual, y estos estados cambian constantemente a lo largo del tiempo. Comprender los diferentes estados de un proceso es crucial para el diseño y la optimización de aplicaciones multiproceso.

El primer estado que experimenta un proceso es el **estado de creación**. Aquí, el sistema operativo asigna recursos necesarios al proceso, como memoria y procesador, y prepara todo lo necesario para que comience su ejecución. Durante este tiempo, el proceso no está listo para interactuar con otros procesos.

Después de la creación, el proceso entra en el **estado listo**. En este estado, el sistema operativo ha asignado todos los recursos necesarios y el proceso está listo para ser ejecutado por el planificador del sistema. El planificador decide cuándo es el momento adecuado para ejecutar el proceso basándose en criterios como la prioridad y el tiempo de espera.

El **estado ejecución** es el siguiente en la secuencia. Una vez que el planificador selecciona un proceso para su ejecución, este entra en el estado ejecución. Durante este período, el procesador se centra completamente en la tarea del proceso, realizando operaciones y manipulando datos hasta que llega al final de su ciclo o a una llamada de sistema.

El **estado bloqueado** es un estado crucial cuando un proceso necesita esperar por algún recurso. Esto puede ser debido a la espera de entrada/salida (como lectura/escritura en disco), la espera de un evento específico, o simplemente porque ha terminado su tiempo de ejecución asignado y debe esperar su turno nuevamente.

El **estado finalizado** es el último estado que experimenta un proceso. Aquí, el sistema operativo libera todos los recursos asociados al proceso, incluyendo la memoria y el procesador, para que puedan ser utilizados por otros procesos. El proceso se marca como terminado y su espacio de memoria se limpia.

Además de estos estados básicos, hay un estado intermedio conocido como **estado listo** o **estado listo para ejecución**, donde el sistema operativo ha asignado todos los recursos necesarios pero aún no ha seleccionado el proceso para su ejecución. Este estado es crucial porque permite que el planificador decida cuándo y cómo ejecutar los procesos.

La planificación de procesos es un aspecto fundamental del sistema operativo, ya que determina la eficiencia y la respuesta de las aplicaciones multiproceso. El planificador debe considerar factores como la prioridad del proceso, el tiempo de espera, la cantidad de recursos disponibles y las necesidades específicas de cada proceso para decidir cuándo ejecutarlos.

Además de los estados mencionados anteriormente, hay otros estados que pueden experimentar los procesos durante su ciclo de vida. Por ejemplo, el **estado suspendido** ocurre cuando un proceso ha sido interrumpido por otro proceso con mayor prioridad o por una llamada de sistema. El proceso puede ser reanudado en cualquier momento.

La gestión eficiente de estos estados y la planificación adecuada son esenciales para crear sistemas operativos y aplicaciones multiproceso que sean rápidos, confiables y eficientes. Comprender los estados de un proceso y cómo el sistema operativo los maneja permite a los desarrolladores optimizar su código y mejorar la experiencia del usuario.

En resumen, los procesos en programación multiproceso pasan por varios estados a lo largo de su ciclo de vida, desde la creación hasta la finalización. Cada estado tiene sus propias características y el sistema operativo utiliza una planificación inteligente para determinar cuándo y cómo ejecutar estos procesos, asegurando así un rendimiento óptimo del sistema.

<a id="hilos"></a>
## Hilos

En este capítulo, exploramos los conceptos fundamentales del programación multiproceso y multihilo, dos técnicas esenciales para mejorar la eficiencia y escalabilidad de las aplicaciones. Comenzamos con una introducción a los procesos y hilos, sus estados y cómo interactúan entre sí.

A continuación, profundizamos en las librerías y clases disponibles para el manejo de hilos en diferentes lenguajes de programación, aprendiendo cómo crear, iniciar y gestionar hilos de manera efectiva. Descubrimos también los métodos de comunicación entre hilos, esenciales para la sincronización y coordinación de tareas concurrentes.

A medida que avanzamos, nos centramos en la gestión de las preferencias de la aplicación, una tarea crucial en el desarrollo de interfaces de usuario. Aprenderemos cómo persistir datos entre ejecuciones del programa y cómo utilizar servicios en segundo plano para realizar tareas asincrónicas sin bloquear la interfaz principal.

Finalmente, exploramos los aspectos de seguridad y permisos en aplicaciones multiproceso y multihilo, aprendiendo a proteger los recursos compartidos y garantizar que solo las partes autorizadas puedan acceder a ellos. Con estos conocimientos, podrás desarrollar aplicaciones robustas y seguras que aprovechen al máximo la potencia de los procesos y hilos para mejorar el rendimiento y la experiencia del usuario.

Este capítulo te proporciona una sólida base en programación multiproceso y multihilo, preparándote para abordar proyectos más complejos y optimizar el rendimiento de tus aplicaciones.

<a id="programacion-concurrente"></a>
## Programación concurrente

La programación concurrente es un campo fundamental en la informática que permite la ejecución simultánea de múltiples procesos o hilos dentro de una misma aplicación. Este concepto es crucial para aprovechar los recursos del sistema operativo y mejorar el rendimiento de las aplicaciones, ya que permite realizar varias tareas a la vez.

En la programación concurrente, se utilizan diferentes técnicas para gestionar la concurrencia, como la creación y sincronización de hilos. Los hilos son unidades de ejecución dentro de un proceso, lo que significa que pueden compartir los mismos recursos del sistema operativo, como memoria y archivos abiertos, pero también tienen su propio contexto de ejecución.

La programación concurrente puede ser implementada en diferentes niveles de abstracción, desde el uso directo de APIs del sistema operativo hasta la creación de bibliotecas o frameworks específicos para aplicaciones multihilo. Cada nivel ofrece diferentes ventajas y desventajas en términos de eficiencia y facilidad de uso.

Una de las principales ventajas de la programación concurrente es el aumento del rendimiento, ya que permite realizar múltiples tareas simultáneamente. Esto es especialmente relevante en aplicaciones que requieren procesamiento intensivo o acceso a recursos compartidos, como servidores web, bases de datos y sistemas operativos.

Sin embargo, la programación concurrente también presenta desafíos significativos. La sincronización entre hilos puede llevar a problemas como el interbloqueo y la condición de carrera, lo que requiere un enfoque cuidadoso para evitar errores inesperados.

Además, la gestión de la concurrencia implica consideraciones adicionales sobre la seguridad y la confiabilidad. Es importante garantizar que los hilos no accedan simultáneamente a recursos compartidos sin control adecuado, lo que puede llevar a inconsistencias o comportamientos inesperados.

La programación concurrente también tiene implicaciones en términos de diseño de aplicaciones. Los desarrolladores deben considerar cómo distribuir las tareas entre hilos y qué tipo de sincronización es necesaria para evitar problemas de concurrencia.

En resumen, la programación concurrente es un poderoso mecanismo que permite mejorar el rendimiento y la eficiencia de las aplicaciones mediante la ejecución simultánea de múltiples procesos o hilos. Aunque presenta desafíos significativos en términos de sincronización y gestión de recursos, su uso adecuado puede llevar a soluciones más robustas y escalables para una amplia gama de aplicaciones.

### no paralelo

```
#include <iostream>
#include <iomanip> // for std::setprecision

int main() {
    long long iterations = 1000000000; // 1 billion iterations
    double numero = 1.000000000043;

    for (long long i = 0; i < iterations; ++i) {
        numero *= 1.00000000000534;
    }

    std::cout << std::setprecision(15);
    std::cout << "Resultado después de " << iterations << " iteraciones: " << numero << std::endl;

    return 0;
}
```

### medimos tiempo

```
#include <iostream>
#include <iomanip>
#include <chrono> // for timing

int main() {
    long long iterations = 10000000000; // 1 billion iterations
    double numero = 1.000000000043;

    // Record start time
    auto start = std::chrono::high_resolution_clock::now();

    for (long long i = 0; i < iterations; ++i) {
        numero *= 1.00000000000534;
    }

    // Record end time
    auto end = std::chrono::high_resolution_clock::now();

    // Compute duration in seconds
    std::chrono::duration<double> duration = end - start;

    std::cout << std::setprecision(15);
    std::cout << "Resultado después de " << iterations << " iteraciones: " << numero << std::endl;
    std::cout << "Tiempo transcurrido: " << duration.count() << " segundos" << std::endl;

    return 0;
}
```

### openmp

```
#include <iostream>
#include <iomanip>
#include <chrono>
#include <cmath>
#include <omp.h>

int main() {
    // ⚠️ This is 10 billion (not 1 billion)
    long long iterations = 10000000000000000LL; 
    const double factor  = 1.00000000000534;
    const double initial = 1.000000000043;

    // Time start
    auto start = std::chrono::high_resolution_clock::now();

    // Parallel: split the exponent across threads and multiply partial powers.
    double combined_power = 1.0;

    #pragma omp parallel
    {
        int T = omp_get_num_threads();
        int tid = omp_get_thread_num();

        // Divide iterations as evenly as possible across threads
        long long base_chunk = iterations / T;
        long long remainder  = iterations % T;
        long long my_count   = base_chunk + (tid < remainder ? 1 : 0);

        // Each thread computes factor^my_count (use pow for speed)
        double local_power = std::pow(factor, static_cast<double>(my_count));

        // Multiplicative reduction
        #pragma omp atomic
        combined_power *= local_power;
    }

    double numero = initial * combined_power;

    // Time end
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    std::cout << std::setprecision(15);
    std::cout << "Resultado después de " << iterations << " iteraciones: " << numero << "\n";
    std::cout << "Tiempo transcurrido: " << duration.count() << " segundos\n";

    return 0;
}
// g++ 003-openmp.cpp -fopenmp -O3 -o 003-openmp
```

### estocastico

```
#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <omp.h>

struct Emitter {
    float x, y;
    float radius;
    float intensity;
    cv::Vec3f color;  // RGB en [0,1]
};

static cv::Vec3f random_color(std::mt19937 &rng) {
    std::uniform_real_distribution<float> dist(0.2f, 1.0f);
    float r = dist(rng), g = dist(rng), b = dist(rng);
    float m = std::max({r,g,b});
    return cv::Vec3f(r/m, g/m, b/m);
}

// “Splat” 3x3 para que cada sample deje más huella visual
inline void splat3x3(cv::Mat &img, int x, int y, const cv::Vec3f &val) {
    static const float k[3][3] = {
        {0.0625f, 0.125f, 0.0625f},
        {0.1250f, 0.250f, 0.1250f},
        {0.0625f, 0.125f, 0.0625f}
    };
    const int W = img.cols, H = img.rows;
    for (int dy=-1; dy<=1; ++dy) {
        int py = y + dy;
        if (py < 0 || py >= H) continue;
        for (int dx=-1; dx<=1; ++dx) {
            int px = x + dx;
            if (px < 0 || px >= W) continue;
            img.at<cv::Vec3f>(py, px) += val * k[dy+1][dx+1];
        }
    }
}

int main() {
    // ---------- parámetros hardcoded ----------
    const int W = 960;
    const int H = 540;

    // Usa el máximo de hilos disponibles (si quieres forzar, pon un número fijo)
    int NUM_THREADS = 32;
    omp_set_num_threads(NUM_THREADS);

    const int   NUM_EMITTERS       = 1200;     // menos de 2000 para reducir dispersión
    long long   SAMPLES_PER_FRAME  = 1'000'000; // más muestras: más señal visible
    const bool  USE_SPLAT_3x3      = true;     // true => “pincel” más visible
    const float DECAY              = 0.96f;    // persistencia
    const float GAMMA              = 2.2f;     // mapea a perceptual
    const float CLAMP_LUMA         = 5.0f;     // clamp antes de gamma (en lineal)

    // ---------- escena ----------
    cv::Mat accum = cv::Mat::zeros(H, W, CV_32FC3);

    std::mt19937 rng_scene{std::random_device{}()};
    std::uniform_real_distribution<float> ux(30.f, W - 30.f);
    std::uniform_real_distribution<float> uy(30.f, H - 30.f);
    std::uniform_real_distribution<float> ur(8.f, 50.f);
    std::uniform_real_distribution<float> uinten(0.7f, 2.0f);

    std::vector<Emitter> emitters;
    emitters.reserve(NUM_EMITTERS);
    for (int i = 0; i < NUM_EMITTERS; ++i) {
        Emitter e;
        e.x = ux(rng_scene);
        e.y = uy(rng_scene);
        e.radius = ur(rng_scene);
        e.intensity = uinten(rng_scene);
        e.color = random_color(rng_scene);
        emitters.push_back(e);
    }

    // Acumuladores por hilo
    std::vector<cv::Mat> thread_accums(NUM_THREADS);
    for (int t = 0; t < NUM_THREADS; ++t) {
        thread_accums[t] = cv::Mat::zeros(H, W, CV_32FC3);
    }

    cv::namedWindow("Stochastic Rendering", cv::WINDOW_AUTOSIZE);

    double fps = 0.0;
    uint64_t frame_idx = 0;

    while (true) {
        for (int t = 0; t < NUM_THREADS; ++t)
            thread_accums[t].setTo(cv::Scalar(0,0,0));

        auto t0 = std::chrono::high_resolution_clock::now();

        // ---------- muestreo paralelo ----------
        #pragma omp parallel
        {
            int tid = omp_get_thread_num();
            // Semilla por hilo + por frame (evita streams iguales)
            std::seed_seq seed{
                (unsigned)tid,
                (unsigned)frame_idx,
                (unsigned)std::chrono::high_resolution_clock::now().time_since_epoch().count()
            };
            std::mt19937 rng(seed);
            std::uniform_int_distribution<int> pick(0, (int)emitters.size() - 1);
            std::normal_distribution<float> gauss(0.f, 1.f);

            cv::Mat &acc_local = thread_accums[tid];

            #pragma omp for schedule(static)
            for (long long i = 0; i < SAMPLES_PER_FRAME; ++i) {
                const Emitter &e = emitters[pick(rng)];
                float sx = e.x + gauss(rng) * e.radius;
                float sy = e.y + gauss(rng) * e.radius;

                int px = (int)std::lround(sx);
                int py = (int)std::lround(sy);
                if ((unsigned)px >= (unsigned)W || (unsigned)py >= (unsigned)H) continue;

                cv::Vec3f contrib = e.color * e.intensity;
                if (USE_SPLAT_3x3)
                    splat3x3(acc_local, px, py, contrib);
                else
                    acc_local.at<cv::Vec3f>(py, px) += contrib;
            }
        }

        // Reducir al acumulador global
        for (int t = 0; t < NUM_THREADS; ++t)
            accum += thread_accums[t];

        auto t1 = std::chrono::high_resolution_clock::now();
        fps = 1.0 / std::chrono::duration<double>(t1 - t0).count();

        // ---------- tonemapping con auto-exposición ----------
        // 1) calcula luminancia y busca el máximo (evita valores atípicos grandes con clamp)
        cv::Mat luma;
        // Rec.709: 0.2126 R + 0.7152 G + 0.0722 B
        std::vector<cv::Mat> ch; cv::split(accum, ch);
        luma = 0.2126f*ch[2] + 0.7152f*ch[1] + 0.0722f*ch[0]; // si tuviste BGR, ajusta aquí
        double maxL;
        cv::minMaxLoc(luma, nullptr, &maxL);
        float exposure = (float)(1.0 / std::max(1e-6, std::min(maxL, (double)CLAMP_LUMA)));

        cv::Mat mapped = accum * exposure; // normaliza por el “brillo” del frame
        cv::threshold(mapped, mapped, 1.0f, 1.0f, cv::THRESH_TRUNC); // clamp post-exposure
        cv::pow(mapped, 1.0f / GAMMA, mapped);

        cv::Mat display;
        mapped.convertTo(display, CV_8UC3, 255.0);

        // HUD
        cv::putText(display, "Threads: " + std::to_string(NUM_THREADS),
                    {10, 22}, cv::FONT_HERSHEY_SIMPLEX, 0.6, {255,255,255}, 1, cv::LINE_AA);
        cv::putText(display, "Emitters: " + std::to_string(NUM_EMITTERS),
                    {10, 44}, cv::FONT_HERSHEY_SIMPLEX, 0.6, {255,255,255}, 1, cv::LINE_AA);
        cv::putText(display, "Samples/frame: " + std::to_string(SAMPLES_PER_FRAME),
                    {10, 66}, cv::FONT_HERSHEY_SIMPLEX, 0.6, {255,255,255}, 1, cv::LINE_AA);
        cv::putText(display, cv::format("FPS: %.2f", fps),
                    {10, 88}, cv::FONT_HERSHEY_SIMPLEX, 0.6, {255,255,255}, 1, cv::LINE_AA);
        cv::putText(display, "q/ESC exit | +/- samples | s: toggle splat",
                    {10, H - 12}, cv::FONT_HERSHEY_SIMPLEX, 0.5, {255,255,255}, 1, cv::LINE_AA);

        cv::imshow("Stochastic Rendering", display);

        int key = cv::waitKey(1);
        if (key == 27 || key == 'q' || key == 'Q') break;
        if (key == '+' || key == '=') SAMPLES_PER_FRAME = std::min<long long>(SAMPLES_PER_FRAME * 11 / 10, 20'000'000LL);
        if (key == '-' || key == '_') SAMPLES_PER_FRAME = std::max<long long>(SAMPLES_PER_FRAME * 9 / 10, 10'000LL);
        if (key == 's' || key == 'S') {/* toggle splat? dejaría una variable global si quieres */}

        // Decaimiento para que no crezca sin límite y dé “trail”
        accum *= DECAY;

        ++frame_idx;
    }

    return 0;
}
```

<a id="programacion-paralela-y-distribuida"></a>
## Programación paralela y distribuida

La programación paralela y distribuida es una rama avanzada del desarrollo de software que permite aprovechar los recursos computacionales múltiples para mejorar el rendimiento y la eficiencia. En este contexto, la programación multiproceso se centra en la ejecución simultánea de varias tareas o procesos dentro de un mismo sistema operativo.

La paralelización puede ser implementada a nivel de instrucciones, donde cada instrucción se ejecuta en paralelo, o a nivel de procesos, donde múltiples procesos son iniciados y ejecutados simultáneamente. Cada proceso tiene su propio espacio de memoria y contexto de ejecución, lo que permite una comunicación eficiente entre ellos.

La distribución del trabajo se refiere a la división de un problema en subproblemas más pequeños y su ejecución en diferentes computadoras o nodos. Este enfoque es especialmente útil cuando se trata de problemas de gran escala que requieren mucho tiempo de procesamiento.

Las principales ventajas de la programación paralela y distribuida incluyen el aumento del rendimiento, la escalabilidad para manejar cargas de trabajo crecientes y la capacidad de resolver problemas complejos en tiempos más cortos. Sin embargo, también presentan desafíos significativos, como la coordinación entre procesos o nodos, la gestión de recursos compartidos y la mitigación de errores.

Para implementar programas paralelos y distribuidos, se utilizan diferentes paradigmas y herramientas. En el ámbito de la programación multiproceso, los lenguajes como C++ y Java ofrecen bibliotecas y frameworks que facilitan la creación de aplicaciones concurrentes. Para la programación distribuida, existen plataformas como Apache Hadoop y Spark que permiten procesar grandes conjuntos de datos en paralelo.

La coordinación entre procesos o nodos es crucial para garantizar la integridad del sistema y el correcto funcionamiento de las aplicaciones paralelas. Se utilizan mecanismos como semáforos, barreras y colas para sincronizar los procesos y asegurar que se acceda a recursos compartidos de manera segura.

En resumen, la programación paralela y distribuida es una disciplina que permite aprovechar los recursos computacionales múltiples para mejorar el rendimiento y la eficiencia en aplicaciones complejas. A través del uso de procesos y nodos, se puede dividir un problema en subproblemas más pequeños y ejecutarlos simultáneamente, lo que resulta en tiempos de respuesta significativamente reducidos.

<a id="comunicacion-entre-procesos"></a>
## Comunicación entre procesos

La comunicación entre procesos es un aspecto crucial en la programación multiproceso, permitiendo que diferentes partes de una aplicación interactúen eficientemente. En este contexto, los procesos pueden compartir información, sincronizarse o coordinarse para realizar tareas complejas. Una de las principales formas de comunicarse entre procesos son mediante pipes, que son canales unidireccionales que permiten la transferencia de datos.

Los pipes se crean utilizando las funciones `pipe()` en sistemas Unix-like y proporcionan una forma sencilla de enviar datos desde un proceso al otro. El primer extremo del pipe es el extremo de escritura, mientras que el segundo extremo es el extremo de lectura. Cuando un proceso intenta leer desde un pipe vacío, se bloqueará hasta que otro proceso escriba en él.

Además de los pipes, existen otros métodos para la comunicación entre procesos, como los sockets y las colas de mensajes. Los sockets son una forma más generalizada de comunicación entre procesos, permitiendo la conexión bidireccional y el intercambio de datos estructurados. Las colas de mensajes son útiles cuando se necesita enviar mensajes a un proceso específico sin necesidad de establecer una conexión previa.

La sincronización entre procesos es otro aspecto importante en programación multiproceso. Cuando varios procesos acceden simultáneamente a los mismos recursos, puede producirse la concurrencia y, por lo tanto, problemas como la incoherencia de datos o el bloqueo. Para resolver estos problemas, se utilizan mecanismos de sincronización como las barreras, semáforos y variables de condición.

Las barreras son un tipo de sincronización que permite a varios procesos esperar mutuamente hasta que todos lleguen a un punto específico en el programa. Las semáforos son una forma más generalizada de control de acceso a recursos compartidos, permitiendo especificar cuántos procesos pueden acceder al recurso simultáneamente. Las variables de condición son útiles cuando se necesita notificar a uno o varios procesos que un evento ha ocurrido.

La comunicación entre procesos es una habilidad fundamental en la programación multiproceso y distribuida, permitiendo la creación de aplicaciones escalables y eficientes. A través de pipes, sockets, colas de mensajes y mecanismos de sincronización, los desarrolladores pueden diseñar sistemas que puedan manejar tareas complejas y coordinarse entre diferentes procesos para lograr resultados coherentes y precisos.

En resumen, la comunicación entre procesos es un aspecto clave en la programación multiproceso, permitiendo la interacción eficiente de diferentes partes de una aplicación. A través de pipes, sockets, colas de mensajes y mecanismos de sincronización, los desarrolladores pueden crear sistemas escalables y eficientes que puedan manejar tareas complejas y coordinarse entre diferentes procesos para lograr resultados coherentes y precisos.

### websockets cliente

```html
<!doctype html>
<html>
  <head><meta charset="utf-8"></head>
  <body>
    <script>
      const ws = new WebSocket("wss://jocarsa.com/socket");
      ws.onopen    = () => ws.send("hello");
      ws.onmessage = e => console.log("he recibido un mensaje:", e.data);
      ws.onclose   = () => console.log("closed");
      ws.onerror   = e => console.error("ws error:", e);
    </script>
  </body>
</html>
```

### servidor

```python
# servidor.py
import asyncio, websockets

async def handler(ws):
    async for msg in ws:
        await ws.send(f"echo: {msg}")

async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
```

### nuevo cliente

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>WebSocket Test</title>
</head>
<body>
  <script>
    let ws;
    let reconnectTimer;
    const url = "wss://jocarsa.com/socket";

    function connect() {
      ws = new WebSocket(url);

      ws.onopen = () => {
        console.log("✅ Connected to server");
        ws.send("hello from client");
      };

      ws.onmessage = e => {
        console.log("📩 Message:", e.data);
      };

      ws.onclose = e => {
        console.warn("❌ Connection closed:", e.code, e.reason);
        scheduleReconnect();
      };

      ws.onerror = e => {
        console.error("⚠️ WebSocket error:", e);
        ws.close();
      };
    }

    function scheduleReconnect() {
      if (reconnectTimer) return;
      reconnectTimer = setTimeout(() => {
        console.log("🔄 Reconnecting…");
        reconnectTimer = null;
        connect();
      }, 3000); // 3s before retry
    }

    // optional: send heartbeat every 25s
    setInterval(() => {
      if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send("ping");
      }
    }, 25000);

    // Start
    connect();
  </script>
</body>
</html>
```

### nuevo servidor

```python
# servidor.py (compatible con websockets >= 11)
import asyncio
import itertools
import websockets
from websockets.exceptions import ConnectionClosed

CONNECTED = {}                 # {client_id: websocket}
ID_SEQ = itertools.count(1)

def print_connected(prefix=""):
    if not CONNECTED:
        print(f"{prefix}No hay clientes conectados.")
        return
    print(f"{prefix}Clientes conectados ({len(CONNECTED)}):")
    for cid, ws in CONNECTED.items():
        peer = getattr(ws, "remote_address", None)
        print(f"  - #{cid} {peer}")

async def keepalive(ws, cid, interval=30, timeout=10):
    while True:
        await asyncio.sleep(interval)
        try:
            pong_waiter = await ws.ping()
            await asyncio.wait_for(pong_waiter, timeout=timeout)
        except Exception as e:
            print(f"[#{cid}] ping falló ({e}). Cerrando conexión…")
            try:
                await ws.close(code=1002, reason="Ping timeout")
            finally:
                break

async def register(ws):
    cid = next(ID_SEQ)
    CONNECTED[cid] = ws
    peer = getattr(ws, "remote_address", None)
    path = getattr(ws, "path", None)  # websockets >=11
    print(f"Conectado #{cid} desde {peer} path={path}")
    print_connected(prefix="> ")
    return cid

async def unregister(cid):
    CONNECTED.pop(cid, None)
    print(f"Desconectado #{cid}")
    print_connected(prefix="> ")

# *** IMPORTANT: single-arg handler for websockets >= 11 ***
async def handler(ws):
    cid = await register(ws)
    ka_task = asyncio.create_task(keepalive(ws, cid))
    try:
        async for msg in ws:
            await ws.send(f"echo: {msg}")
    except ConnectionClosed as e:
        print(f"[#{cid}] conexión cerrada: {e.code} {e.reason}")
    finally:
        ka_task.cancel()
        await unregister(cid)

async def main():
    # ping_interval=None para usar nuestro keepalive explícito
    async with websockets.serve(
        handler,
        host="127.0.0.1",
        port=8765,
        ping_interval=None,
        max_queue=32,
    ):
        print("Servidor WebSocket en ws://127.0.0.1:8765 listo.")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSaliendo…")
```

### calculo

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>WS Compute Client</title>
</head>
<body>
  <script>
    const url = "wss://jocarsa.com/socket";
    let ws, reconnectTimer;

    function connect() {
      ws = new WebSocket(url);

      ws.onopen = () => {
        console.log("✅ Connected");
      };

      ws.onmessage = (e) => {
        try {
          const msg = JSON.parse(e.data);
          if (msg.type === "task" && msg.op === "repeat_multiply") {
            const { task_id, initial, factor, times } = msg;
            console.log("🧮 Task received:", msg);

            const t0 = performance.now();
            // Compute: initial * (factor ** times)
            // (Exponentiation is equivalent to repeated multiplication and far faster.)
            const result = initial * Math.pow(factor, times);
            const duration_ms = Math.round(performance.now() - t0);

            const reply = {
              type: "result",
              task_id,
              result,
              duration_ms,
              agent: navigator.userAgent
            };
            ws.send(JSON.stringify(reply));
            console.log("📤 Result sent:", reply);
          } else {
            console.log("📩 Message:", msg);
          }
        } catch (err) {
          console.log("📩 Raw message:", e.data);
        }
      };

      ws.onclose = (e) => {
        console.warn("❌ Closed:", e.code, e.reason);
        scheduleReconnect();
      };

      ws.onerror = (e) => {
        console.error("⚠️ Error:", e);
        // Let onclose handle reconnect
      };
    }

    function scheduleReconnect() {
      if (reconnectTimer) return;
      reconnectTimer = setTimeout(() => {
        reconnectTimer = null;
        console.log("🔄 Reconnecting…");
        connect();
      }, 3000);
    }

    connect();
  </script>
</body>
</html>
```

### servidorcalculo

```python
# servidor.py
import asyncio
import itertools
import json
import websockets
from websockets.exceptions import ConnectionClosed

TASK_SEQ = itertools.count(1)
CLIENTS = {}  # {cid: ws}
ID_SEQ = itertools.count(1)

async def send_task(ws, *, initial: float, factor: float, times: int):
    task_id = next(TASK_SEQ)
    payload = {
        "type": "task",
        "op": "repeat_multiply",
        "task_id": task_id,
        "initial": initial,
        "factor": factor,
        "times": times,
    }
    await ws.send(json.dumps(payload))
    return task_id

def list_clients():
    if not CLIENTS:
        print("No hay clientes conectados.")
        return
    print(f"Clientes conectados ({len(CLIENTS)}):")
    for cid, ws in CLIENTS.items():
        print(f"  - #{cid} {getattr(ws,'remote_address',None)}")

async def handler(ws):
    cid = next(ID_SEQ)
    CLIENTS[cid] = ws
    print(f"Conectado #{cid} desde {getattr(ws,'remote_address',None)} path={getattr(ws,'path',None)}")
    list_clients()

    # Send the computation task immediately on connect:
    task_id = await send_task(
        ws,
        initial=1.0000054,
        factor=1.00000043,
        times=1_000_000
    )
    print(f"[#{cid}] Tarea enviada task_id={task_id}")

    try:
        async for raw in ws:
            try:
                msg = json.loads(raw)
            except Exception:
                print(f"[#{cid}] Mensaje no-JSON: {raw!r}")
                continue

            if msg.get("type") == "result" and msg.get("task_id") == task_id:
                result = msg.get("result")
                duration = msg.get("duration_ms")
                ua = msg.get("agent")
                print(f"[#{cid}] ✅ Resultado task_id={task_id}")
                print(f"          result={result}")
                if duration is not None:
                    print(f"          duration_ms={duration}")
                if ua:
                    print(f"          agent={ua}")
            else:
                # Echo other messages or handle more ops
                pass

    except ConnectionClosed as e:
        print(f"[#{cid}] conexión cerrada: {e.code} {e.reason}")
    finally:
        CLIENTS.pop(cid, None)
        print(f"Desconectado #{cid}")
        list_clients()

async def main():
    async with websockets.serve(
        handler,
        host="127.0.0.1",
        port=8765,
        ping_interval=None,   # we'll keep it simple; rely on TCP (add your own keepalive if you want)
    ):
        print("Servidor WebSocket en ws://127.0.0.1:8765 listo.")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSaliendo…")
```

<a id="gestion-de-procesos-herramientas-de-monitorizacion"></a>
## Gestión de procesos. Herramientas de monitorización

La gestión de procesos es un aspecto fundamental del desarrollo de software multiproceso, permitiendo la creación de aplicaciones que pueden realizar múltiples tareas simultáneamente. En esta subunidad, exploraremos las herramientas disponibles para monitorizar y administrar eficazmente los procesos en sistemas operativos modernos.

El primer paso para gestionar procesos es entender su estado actual. Los procesos pueden estar en varios estados como ejecutando, listo, bloqueado o terminado. Herramientas como `top` en Linux proporcionan una visión general rápida de todos los procesos en ejecución y sus estados actuales.

Además de monitorizar el estado de los procesos, es crucial medir su rendimiento. Herramientas como `htop`, que es una versión mejorada de `top`, no solo muestra la CPU y la memoria utilizadas por cada proceso, sino también proporciona información sobre la tasa de cambio de uso de recursos.

La gestión de procesos también implica la creación y terminación de procesos. En sistemas operativos basados en Unix, se pueden crear nuevos procesos utilizando la función `fork()`, que duplica el proceso actual, mientras que para terminar un proceso se utiliza la llamada a `exit()`.

Para sincronizar los procesos, es necesario garantizar que ciertas partes del código se ejecuten en orden específico. Herramientas como semáforos y variables de condición proporcionan mecanismos para controlar el acceso a recursos compartidos entre múltiples procesos.

La comunicación entre procesos es otro aspecto crucial de la gestión multiproceso. Protocolos como POSIX Message Queues o Sockets permiten que los procesos intercambien datos y sincronizarse de manera eficiente. Estas herramientas son fundamentales para el desarrollo de aplicaciones distribuidas.

Además de las herramientas de monitorización y comunicación, es importante considerar la gestión de memoria en un entorno multiproceso. Herramientas como `valgrind` pueden ayudar a detectar errores comunes relacionados con la asignación y liberación de memoria, lo que es crucial para mantener la estabilidad y el rendimiento de las aplicaciones.

La gestión de procesos también implica la planificación y priorización. Algunos sistemas operativos utilizan algoritmos como Round Robin o Prioridad Dinámica para determinar cuándo se ejecutan los procesos. Comprender estos algoritmos es clave para optimizar el uso de recursos en aplicaciones multiproceso.

La monitorización continua de los procesos es esencial para identificar problemas y mejorar la eficiencia del sistema. Herramientas como `dstat` proporcionan una visión detallada de la carga del sistema, el uso de CPU, memoria y red, lo que permite a los desarrolladores tomar decisiones informadas sobre la optimización.

En conclusión, la gestión de procesos es un componente integral del desarrollo multiproceso. Herramientas como `top`, `htop`, semáforos, variables de condición, POSIX Message Queues, Sockets y herramientas de monitorización avanzada son fundamentales para crear aplicaciones que puedan ejecutar múltiples tareas simultáneamente de manera eficiente y segura. Comprender estos conceptos es crucial para cualquier desarrollador de software que trabaje en entornos multiproceso.

<a id="sincronizacion-entre-procesos"></a>
## Sincronización entre procesos

La sincronización entre procesos es un aspecto crucial en la programación multiproceso, ya que permite a múltiples procesos compartir recursos de manera segura y coordinada. En este contexto, los procesos pueden necesitar acceder simultáneamente a datos comunes o realizar operaciones que deben ejecutarse en orden específico. Para lograr esto, se utilizan mecanismos como semáforos, barreras y variables de condición.

Un semáforo es un recurso compartido que puede tener un valor entero no negativo. Los procesos pueden solicitar el acceso al recurso incrementando el valor del semáforo (wait) o liberarlo decrementándolo (signal). Si el valor del semáforo es cero, los procesos se bloquean hasta que otro proceso libere el recurso.

Las barreras son mecanismos que permiten a un grupo de procesos esperar mutuamente en un punto específico antes de continuar. Cada proceso debe alcanzar la barrera antes de que todos puedan avanzar. Las barreras son útiles para sincronizar eventos importantes, como el inicio o final de una operación.

Las variables de condición son mecanismos que permiten a los procesos esperar por ciertas condiciones antes de continuar su ejecución. Estas variables se utilizan junto con semáforos y permiten un control más preciso sobre la sincronización entre procesos. Por ejemplo, un proceso puede esperar hasta que otro proceso cambie el valor de una variable.

Además de estos mecanismos básicos, existen otras técnicas para la sincronización entre procesos como los monitores y las colas. Los monitores son bloques de código que encapsulan datos y métodos relacionados, proporcionando un control más estricto sobre el acceso a los recursos compartidos. Las colas son estructuras de datos que permiten a los procesos comunicarse entre sí en orden.

La sincronización entre procesos requiere cuidado para evitar problemas como la condición de carrera y el bloqueo muerto. La condición de carrera ocurre cuando dos o más procesos intentan modificar un recurso compartido al mismo tiempo, lo que puede resultar en datos inconsistentes. El bloqueo muerto ocurre cuando dos o más procesos se bloquean entre sí esperando a que el otro libere un recurso.

Para evitar estos problemas, es importante diseñar correctamente los mecanismos de sincronización y utilizar técnicas como la exclusión mutua para proteger los recursos compartidos. Además, es crucial realizar pruebas exhaustivas para identificar y corregir posibles problemas de sincronización.

En resumen, la sincronización entre procesos es un tema fundamental en la programación multiproceso que permite a múltiples procesos compartir recursos de manera segura y coordinada. A través de mecanismos como semáforos, barreras y variables de condición, se pueden controlar el acceso a los recursos compartidos y garantizar la consistencia de los datos. Es importante diseñar correctamente estos mecanismos y realizar pruebas exhaustivas para evitar problemas de sincronización y asegurar el correcto funcionamiento del sistema.

### path tracing basico

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Minimal JS BDPT — Cornell Box</title>
  <style>
    html, body { height: 100%; margin: 0; background:#0b0d10; color:#e8edf2; font:14px/1.4 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell; }
    .wrap { display:flex; gap:16px; padding:16px; align-items:flex-start; }
    canvas { image-rendering: pixelated; border-radius:14px; box-shadow: 0 10px 30px rgba(0,0,0,.35); background:#000; }
    .panel { max-width: 380px; }
    .panel h1 { font-size:18px; margin:0 0 8px; }
    .row { display:flex; gap:8px; align-items:center; margin:6px 0; }
    input[type=range] { width: 180px; }
    button { background:#1f2937; color:#e8edf2; border:1px solid #2b3646; border-radius:10px; padding:8px 10px; cursor:pointer; }
    .pill { display:inline-block; padding:2px 8px; border:1px solid #2b3646; border-radius:999px; font-size:12px; }
    a { color:#9bd; }
  </style>
</head>
<body>
  <div class="wrap">
    <canvas id="view" width="320" height="240"></canvas>
    <div class="panel">
      <h1>Minimal JS Bidirectional Path Tracer</h1>
      <div class="row"><span class="pill">Scene</span><span>Cornell Box (diffuse walls + ceiling light)</span></div>
      <div class="row"><label>Resolution</label>
        <button id="half">½x</button>
        <button id="one">1x</button>
        <button id="double">2x</button>
      </div>
      <div class="row"><label>Samples / frame</label><input id="spp" type="range" min="1" max="16" value="1"><span id="sppv">1</span></div>
      <div class="row"><label>Max depth</label><input id="depth" type="range" min="2" max="8" value="5"><span id="depthv">5</span></div>
      <div class="row"><label>Pause</label><button id="toggle">⏸️</button><button id="reset">Reset</button></div>
      <div class="row"><span id="stats">0 spp</span></div>
      <p><em>Note:</em> This is a tiny educational BDPT. It connects camera and light subpaths with a very simple weight (no full MIS), so it's not production-accurate but great to learn from.</p>
      <p>Controls: drag to look, scroll to dolly.</p>
      <p>Source: single-file, vanilla JS. No WebGL/WebGPU; pure CPU.</p>
    </div>
  </div>
<script>
(() => {
  // ===== Linear algebra helpers =====
  const V = {
    add:(a,b)=>[a[0]+b[0],a[1]+b[1],a[2]+b[2]],
    sub:(a,b)=>[a[0]-b[0],a[1]-b[1],a[2]-b[2]],
    mul:(a,s)=>[a[0]*s,a[1]*s,a[2]*s],
    had:(a,b)=>[a[0]*b[0],a[1]*b[1],a[2]*b[2]],
    dot:(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],
    cross:(a,b)=>[a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]],
    len:(a)=>Math.hypot(a[0],a[1],a[2]),
    norm:(a)=>{const l=V.len(a)||1e-16; return [a[0]/l,a[1]/l,a[2]/l];},
    clamp01:(a)=>[Math.min(1,Math.max(0,a[0])),Math.min(1,Math.max(0,a[1])),Math.min(1,Math.max(0,a[2]))],
  };

  function rng() { return Math.random(); }

  // ===== Ray / Triangle intersection (Möller–Trumbore) =====
  function rayTri(ro, rd, v0, v1, v2) {
    const eps=1e-6;
    const e1=V.sub(v1,v0), e2=V.sub(v2,v0);
    const p = V.cross(rd,e2);
    const det = V.dot(e1,p);
    if (Math.abs(det) < eps) return null;
    const inv = 1/det;
    const tvec = V.sub(ro,v0);
    const u = V.dot(tvec,p) * inv; if (u<0||u>1) return null;
    const q = V.cross(tvec,e1);
    const v = V.dot(rd,q) * inv; if (v<0||u+v>1) return null;
    const t = V.dot(e2,q) * inv; if (t<eps) return null;
    const n = V.norm(V.cross(e1,e2));
    return { t, n };
  }

  // ===== Scene setup: Cornell Box (units ~ meters) =====
  // Materials: purely diffuse (Lambert), with optional emission
  const materials = [];
  function makeMat(albedo, emit=[0,0,0]) { return { albedo, emit }; }
  const MAT_WHITE = materials.push(makeMat([0.8,0.8,0.8]))-1;
  const MAT_RED   = materials.push(makeMat([0.75,0.15,0.15]))-1;
  const MAT_GREEN = materials.push(makeMat([0.15,0.75,0.2]))-1;
  // Strong small area light for fast convergence
  const MAT_LIGHT = materials.push(makeMat([0,0,0],[18,18,18]))-1;

  // Triangle list with per-triangle material ids
  const tris = []; const triMat = [];
  function addQuad(a,b,c,d, mat) { // two tris
    tris.push(a,b,c,  a,c,d); triMat.push(mat,mat);
  }

  // Box dimensions
  // Room: x in [-1,1], y in [0,2], z in [-1,1]
  const y0=0, y1=2, x0=-1, x1=1, z0=-1, z1=1;
  // Floor
  addQuad([x0,y0,z1],[x1,y0,z1],[x1,y0,z0],[x0,y0,z0], MAT_WHITE);
  // Ceiling (with light hole we will overlay a light patch)
  addQuad([x0,y1,z0],[x1,y1,z0],[x1,y1,z1],[x0,y1,z1], MAT_WHITE);
  // Back wall (z1)
  addQuad([x0,y0,z1],[x1,y0,z1],[x1,y1,z1],[x0,y1,z1], MAT_WHITE);
  // Left wall (x0) — red
  addQuad([x0,y0,z0],[x0,y0,z1],[x0,y1,z1],[x0,y1,z0], MAT_RED);
  // Right wall (x1) — green
  addQuad([x1,y0,z1],[x1,y0,z0],[x1,y1,z0],[x1,y1,z1], MAT_GREEN);

  // Light: small square patch on ceiling
  const Ls = 0.4; // size of light square
  const ly = y1 - 1e-4; // slight offset to avoid z-fighting
  const light = {
    p0:[-Ls, ly, -Ls], p1:[ Ls, ly, -Ls], p2:[ Ls, ly,  Ls], p3:[-Ls, ly,  Ls],
    normal: [0,-1,0], area: (2*Ls)*(2*Ls), mat: MAT_LIGHT,
  };
  addQuad(light.p0, light.p1, light.p2, light.p3, MAT_LIGHT);

  // Intersection over all triangles
  function intersect(ro, rd) {
    let hitT = 1e20, hitN = null, hitIdx = -1;
    for (let i=0;i<tris.length;i+=3) {
      const v0=tris[i], v1=tris[i+1], v2=tris[i+2];
      const h = rayTri(ro, rd, v0, v1, v2);
      if (h && h.t < hitT) { hitT = h.t; hitN = h.n; hitIdx = i/3; }
    }
    if (hitIdx<0) return null;
    const mat = triMat[hitIdx];
    const pos = [ro[0]+rd[0]*hitT, ro[1]+rd[1]*hitT, ro[2]+rd[2]*hitT];
    return { t: hitT, n: hitN, pos, mat };
  }

  // Visibility check between two points
  function visible(a, b) {
    const dir = V.sub(b,a); const dist = V.len(dir); const rd = V.mul(dir, 1/(dist));
    const eps = 1e-4; const ro = V.add(a, V.mul(rd, eps));
    const h = intersect(ro, rd);
    if (!h) return true;
    return h.t + 1e-4 >= dist; // unobstructed if first hit beyond target
  }

  // Cosine-weighted hemisphere sample around normal n
  function cosineHemisphere(n) {
    const r1 = 2*Math.PI*rng();
    const r2 = rng(), r2s = Math.sqrt(r2);
    const u = Math.cos(r1)*r2s, v = Math.sin(r1)*r2s, w = Math.sqrt(1-r2);
    // Build ONB from n
    const t = Math.abs(n[1])<0.999 ? V.norm(V.cross([0,1,0], n)) : V.norm(V.cross([1,0,0], n));
    const b = V.cross(n, t);
    const d = [ t[0]*u + b[0]*v + n[0]*w,
                t[1]*u + b[1]*v + n[1]*w,
                t[2]*u + b[2]*v + n[2]*w ];
    return V.norm(d);
  }

  // Sample a point and direction from the light (uniform on area, cosine dir)
  function sampleLight() {
    const ux = rng(), uz = rng();
    const x = (ux*2-1)*0.4; const z = (uz*2-1)*0.4; // within light square of side 0.8
    const p = [x, light.p0[1], z];
    const n = light.normal;
    const d = cosineHemisphere(V.mul(n,-1)); // emit downward (since normal is down)
    // pdf: area uniform * cosine hemisphere
    const pdfA = 1 / light.area;
    const pdfW = Math.max(0, V.dot(V.mul(n,-1), d)) / Math.PI;
    const emit = materials[MAT_LIGHT].emit; // radiance
    let throughput = [emit[0], emit[1], emit[2]]; // start with light radiance; scalars below
    // Scale to account for sampling densities (rough, educational)
    throughput = V.mul(throughput, 1/(pdfA*pdfW + 1e-8));
    return { p, n, d, throughput, pdfA, pdfW };
  }

  // Trace one diffuse bounce; returns next hit or null (escaped)
  function bounce(ro, rd) {
    const h = intersect(ro, rd);
    if (!h) return null;
    const m = materials[h.mat];
    return { pos: h.pos, n: h.n, matId: h.mat, mat: m };
  }

  // ===== BDPT sample for one pixel =====
  function bdptSample(px, py, cam, maxDepth) {
    // Camera ray through pixel jitter
    const u = (px + rng())/cam.w * 2 - 1;
    const v = (py + rng())/cam.h * 2 - 1;
    // Screen is at z = -1 in camera space
    const dirCam = V.norm([u*cam.fovScale, v*cam.fovScale, -1]);
    // Transform by camera basis
    const dir = V.norm([
      cam.right[0]*dirCam[0] + cam.up[0]*dirCam[1] + cam.forward[0]*dirCam[2],
      cam.right[1]*dirCam[0] + cam.up[1]*dirCam[1] + cam.forward[1]*dirCam[2],
      cam.right[2]*dirCam[0] + cam.up[2]*dirCam[1] + cam.forward[2]*dirCam[2]
    ]);
    const eyeVerts = [];
    let ro = cam.pos.slice(), rd = dir.slice();
    let throughput = [1,1,1];
    for (let d=0; d<maxDepth; d++) {
      const hit = bounce(ro, rd); if (!hit) break;
      const nl = V.dot(hit.n, V.mul(rd,-1))>0 ? hit.n : V.mul(hit.n,-1);
      eyeVerts.push({ pos: hit.pos, n: nl, through: throughput.slice(), matId: hit.matId });
      const m = hit.mat;
      if (V.len(m.emit) > 0) { // if we hit light, add emission (eye path endpoint at light)
        // Simple NEE-like add
        throughput = V.had(throughput, m.emit);
        break;
      }
      // Diffuse bounce
      const newDir = cosineHemisphere(nl);
      const cos = Math.max(0, V.dot(nl, newDir));
      throughput = V.had(throughput, V.mul(m.albedo, cos/Math.PI));
      // RR
      if (d>2) {
        const q = Math.max(0.05, Math.min(0.95, Math.max(throughput[0], throughput[1], throughput[2])));
        if (rng()>q) break; else throughput = V.mul(throughput, 1/q);
      }
      const eps=1e-4; ro = V.add(hit.pos, V.mul(newDir, eps)); rd = newDir;
    }

    // Build a short light subpath
    const lightVerts = [];
    let Lsamp = sampleLight();
    let lro = V.add(Lsamp.p, V.mul(Lsamp.d, 1e-4));
    let lrd = Lsamp.d.slice();
    let lthrough = Lsamp.throughput.slice();
    for (let d=0; d<maxDepth; d++) {
      const hit = bounce(lro, lrd); if (!hit) break;
      const nl = V.dot(hit.n, V.mul(lrd,-1))>0 ? hit.n : V.mul(hit.n,-1);
      lightVerts.push({ pos: hit.pos, n: nl, through: lthrough.slice(), matId: hit.matId });
      const m = hit.mat;
      if (V.len(m.emit) > 0 && d>0) { // hitting light again; stop
        break;
      }
      // Diffuse bounce
      const newDir = cosineHemisphere(nl);
      const cos = Math.max(0, V.dot(nl, newDir));
      lthrough = V.had(lthrough, V.mul(m.albedo, cos/Math.PI));
      if (d>2) {
        const q = Math.max(0.05, Math.min(0.95, Math.max(lthrough[0], lthrough[1], lthrough[2])));
        if (rng()>q) break; else lthrough = V.mul(lthrough, 1/q);
      }
      const eps=1e-4; lro = V.add(hit.pos, V.mul(newDir, eps)); lrd = newDir;
    }

    // Connect all pairs (eye i) — (light j)
    let C = [0,0,0];
    for (let i=0; i<eyeVerts.length; i++) {
      for (let j=0; j<lightVerts.length; j++) {
        const a = eyeVerts[i], b = lightVerts[j];
        if (materials[a.matId]===materials[MAT_LIGHT]) continue; // avoid trivial
        const dir = V.sub(b.pos, a.pos);
        const dist2 = Math.max(1e-8, V.dot(dir,dir));
        const dirN = V.mul(dir, 1/Math.sqrt(dist2));
        const cos1 = Math.max(0, V.dot(a.n, dirN));
        const cos2 = Math.max(0, V.dot(b.n, V.mul(dirN,-1)));
        if (cos1<=0 || cos2<=0) continue;
        if (!visible(a.pos, b.pos)) continue;
        const G = (cos1 * cos2) / dist2;
        const contrib = V.mul(V.had(a.through, V.had(b.through, [G,G,G])), 1 /* no MIS, simple */);
        C = V.add(C, contrib);
      }
    }

    // Also add direct hit to light from last eye vertex (simple NEE)
    if (eyeVerts.length>0) {
      const a = eyeVerts[eyeVerts.length-1];
      // sample one point on light and connect
      const ux=rng(), uz=rng();
      const p = [ (ux*2-1)*0.4, light.p0[1], (uz*2-1)*0.4 ];
      const dir = V.sub(p, a.pos);
      const dist2 = Math.max(1e-8, V.dot(dir,dir));
      const dirN = V.mul(dir, 1/Math.sqrt(dist2));
      const cos1 = Math.max(0, V.dot(a.n, dirN));
      const cosL = Math.max(0, V.dot(light.normal, V.mul(dirN,-1)));
      if (cos1>0 && cosL>0 && visible(a.pos, p)) {
        const G = (cos1 * cosL) / dist2;
        const Le = materials[MAT_LIGHT].emit;
        const pdfA = 1/light.area;
        const contrib = V.mul(V.had(a.through, Le), (G / pdfA));
        C = V.add(C, contrib);
      }
    }

    return C;
  }

  // ===== Camera / render loop =====
  const canvas = document.getElementById('view');
  const ctx = canvas.getContext('2d');
  let W = canvas.width, H = canvas.height;
  let accumulation = new Float32Array(W*H*3);
  let spp = 0;

  const cam = {
    pos: [0, 1, 3.2],
    target: [0, 1, 0],
    upWorld: [0,1,0],
    fov: 45 * Math.PI/180,
    w: W, h: H,
    fovScale: 1,
    forward:[0,0,-1], right:[1,0,0], up:[0,1,0],
  };
  function updateCam() {
    cam.w=W; cam.h=H;
    cam.fovScale = Math.tan(cam.fov*0.5);
    const f = V.norm(V.sub(cam.target, cam.pos));
    const r = V.norm(V.cross(f, cam.upWorld));
    const u = V.cross(r, f);
    cam.forward=f; cam.right=r; cam.up=u;
  }
  updateCam();

  // Simple mouse controls
  let isDown=false, lastX=0, lastY=0; let yaw=0, pitch=0; let dist=3.2;
  function recalcCamFromAngles() {
    const cy = Math.cos(yaw), sy = Math.sin(yaw);
    const cp = Math.cos(pitch), sp = Math.sin(pitch);
    const dir = [sy*cp, sp, -cy*cp];
    cam.pos = V.add(cam.target, V.mul(dir, dist));
    updateCam(); resetAccum();
  }
  canvas.addEventListener('mousedown', e=>{isDown=true; lastX=e.clientX; lastY=e.clientY;});
  window.addEventListener('mouseup', ()=>isDown=false);
  window.addEventListener('mousemove', e=>{
    if(!isDown) return; const dx=(e.clientX-lastX)/200, dy=(e.clientY-lastY)/200; lastX=e.clientX; lastY=e.clientY;
    yaw -= dx; pitch = Math.max(-1.2, Math.min(1.2, pitch - dy)); recalcCamFromAngles();
  });
  window.addEventListener('wheel', e=>{ dist = Math.max(1.2, Math.min(6, dist + (e.deltaY>0?0.2:-0.2))); recalcCamFromAngles();});

  function resetAccum() { accumulation.fill(0); spp=0; }

  // UI controls
  const sppSlider = document.getElementById('spp'); const sppVal = document.getElementById('sppv');
  const depthSlider = document.getElementById('depth'); const depthVal = document.getElementById('depthv');
  const stats = document.getElementById('stats');
  sppSlider.oninput = ()=>{ sppVal.textContent = sppSlider.value; };
  depthSlider.oninput = ()=>{ depthVal.textContent = depthSlider.value; resetAccum(); };
  document.getElementById('reset').onclick = ()=> resetAccum();
  document.getElementById('toggle').onclick = ()=> running=!running;
  document.getElementById('half').onclick = ()=> resizeCanvas(0.5);
  document.getElementById('one').onclick = ()=> resizeCanvas(1);
  document.getElementById('double').onclick = ()=> resizeCanvas(2);

  function resizeCanvas(scale) {
    canvas.width = Math.round(320*scale); canvas.height = Math.round(240*scale);
    W=canvas.width; H=canvas.height; accumulation = new Float32Array(W*H*3); resetAccum(); updateCam();
  }

  let running = true;

  function renderFrame() {
    if (!running) { requestAnimationFrame(renderFrame); return; }
    const S = parseInt(sppSlider.value,10);
    const maxDepth = parseInt(depthSlider.value,10);
    for (let s=0;s<S;s++) {
      for (let y=0;y<H;y++) {
        for (let x=0;x<W;x++) {
          const c = bdptSample(x,y,cam,maxDepth);
          const idx = (y*W+x)*3;
          accumulation[idx  ] += c[0];
          accumulation[idx+1] += c[1];
          accumulation[idx+2] += c[2];
        }
      }
      spp++;
    }
    // tonemap + display
    const img = ctx.getImageData(0,0,W,H); const d = img.data;
    const inv = 1/Math.max(1,spp);
    for (let i=0, p=0; i<accumulation.length; i+=3) {
      // Simple Reinhard tonemap
      const r = accumulation[i  ]*inv, g = accumulation[i+1]*inv, b = accumulation[i+2]*inv;
      const t = (x)=> x/(1+x);
      d[p++] = Math.pow(t(r), 1/2.2)*255|0;
      d[p++] = Math.pow(t(g), 1/2.2)*255|0;
      d[p++] = Math.pow(t(b), 1/2.2)*255|0;
      d[p++] = 255;
    }
    ctx.putImageData(img,0,0);
    stats.textContent = `${spp} spp — ${W}×${H}`;
    requestAnimationFrame(renderFrame);
  }
  renderFrame();
})();
</script>
</body>
</html>
```

### mejoras

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Minimal JS BDPT — Cornell Box</title>
  <style>
    html, body { height: 100%; margin: 0; background:#0b0d10; color:#e8edf2; font:14px/1.4 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell; }
    .wrap { display:flex; gap:16px; padding:16px; align-items:flex-start; }
    canvas { image-rendering: pixelated; border-radius:14px; box-shadow: 0 10px 30px rgba(0,0,0,.35); background:#000; }
    .panel { max-width: 380px; }
    .panel h1 { font-size:18px; margin:0 0 8px; }
    .row { display:flex; gap:8px; align-items:center; margin:6px 0; }
    input[type=range] { width: 180px; }
    button { background:#1f2937; color:#e8edf2; border:1px solid #2b3646; border-radius:10px; padding:8px 10px; cursor:pointer; }
    .pill { display:inline-block; padding:2px 8px; border:1px solid #2b3646; border-radius:999px; font-size:12px; }
    a { color:#9bd; }
  </style>
</head>
<body>
  <div class="wrap">
    <canvas id="view" width="320" height="240"></canvas>
    <div class="panel">
      <h1>Minimal JS Bidirectional Path Tracer</h1>
      <div class="row"><span class="pill">Scene</span><span>Cornell Box (diffuse walls + ceiling light)</span></div>
      <div class="row"><label>Resolution</label>
        <button id="half">½x</button>
        <button id="one">1x</button>
        <button id="double">2x</button>
      </div>
      <div class="row"><label>Samples / frame</label><input id="spp" type="range" min="1" max="16" value="1"><span id="sppv">1</span></div>
      <div class="row"><label>Max depth</label><input id="depth" type="range" min="2" max="8" value="5"><span id="depthv">5</span></div>
      <div class="row"><label>Pause</label><button id="toggle">⏸️</button><button id="reset">Reset</button></div>
      <div class="row"><span id="stats">0 spp</span></div>
      <p><em>Note:</em> This is a tiny educational BDPT. It connects camera and light subpaths with a very simple weight (no full MIS), so it's not production-accurate but great to learn from.</p>
      <p>Controls: drag to look, scroll to dolly.</p>
      <p>Source: single-file, vanilla JS. No WebGL/WebGPU; pure CPU.</p>
    </div>
  </div>
<script>
(() => {
  // ===== Linear algebra helpers =====
  const V = {
    add:(a,b)=>[a[0]+b[0],a[1]+b[1],a[2]+b[2]],
    sub:(a,b)=>[a[0]-b[0],a[1]-b[1],a[2]-b[2]],
    mul:(a,s)=>[a[0]*s,a[1]*s,a[2]*s],
    had:(a,b)=>[a[0]*b[0],a[1]*b[1],a[2]*b[2]],
    dot:(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],
    cross:(a,b)=>[a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]],
    len:(a)=>Math.hypot(a[0],a[1],a[2]),
    norm:(a)=>{const l=V.len(a)||1e-16; return [a[0]/l,a[1]/l,a[2]/l];},
    clamp01:(a)=>[Math.min(1,Math.max(0,a[0])),Math.min(1,Math.max(0,a[1])),Math.min(1,Math.max(0,a[2]))],
  };

  function rng() { return Math.random(); }

  // ===== Ray / Triangle intersection (Möller–Trumbore) =====
  function rayTri(ro, rd, v0, v1, v2) {
    const eps=1e-6;
    const e1=V.sub(v1,v0), e2=V.sub(v2,v0);
    const p = V.cross(rd,e2);
    const det = V.dot(e1,p);
    if (Math.abs(det) < eps) return null;
    const inv = 1/det;
    const tvec = V.sub(ro,v0);
    const u = V.dot(tvec,p) * inv; if (u<0||u>1) return null;
    const q = V.cross(tvec,e1);
    const v = V.dot(rd,q) * inv; if (v<0||u+v>1) return null;
    const t = V.dot(e2,q) * inv; if (t<eps) return null;
    const n = V.norm(V.cross(e1,e2));
    return { t, n };
  }

  // ===== Scene setup: Cornell Box (units ~ meters) =====
  // Materials: purely diffuse (Lambert), with optional emission
  const materials = [];
  function makeMat(albedo, emit=[0,0,0]) { return { albedo, emit }; }
  const MAT_WHITE = materials.push(makeMat([0.8,0.8,0.8]))-1;
  const MAT_RED   = materials.push(makeMat([0.75,0.15,0.15]))-1;
  const MAT_GREEN = materials.push(makeMat([0.15,0.75,0.2]))-1;
  // Strong small area light for fast convergence
  const MAT_LIGHT = materials.push(makeMat([0,0,0],[18,18,18]))-1;

  // Triangle list with per-triangle material ids
  const tris = []; const triMat = [];
  function addQuad(a,b,c,d, mat) { // two tris
    tris.push(a,b,c,  a,c,d); triMat.push(mat,mat);
  }

  // Box dimensions
  // Room: x in [-1,1], y in [0,2], z in [-1,1]
  const y0=0, y1=2, x0=-1, x1=1, z0=-1, z1=1;
  // Floor
  addQuad([x0,y0,z1],[x1,y0,z1],[x1,y0,z0],[x0,y0,z0], MAT_WHITE);
  // Ceiling (with light hole we will overlay a light patch)
  addQuad([x0,y1,z0],[x1,y1,z0],[x1,y1,z1],[x0,y1,z1], MAT_WHITE);
  // Back wall (z1)
  addQuad([x0,y0,z1],[x1,y0,z1],[x1,y1,z1],[x0,y1,z1], MAT_WHITE);
  // Left wall (x0) — red
  addQuad([x0,y0,z0],[x0,y0,z1],[x0,y1,z1],[x0,y1,z0], MAT_RED);
  // Right wall (x1) — green
  addQuad([x1,y0,z1],[x1,y0,z0],[x1,y1,z0],[x1,y1,z1], MAT_GREEN);

  // Light: small square patch on ceiling
  const Ls = 0.4; // size of light square
  const ly = y1 - 1e-4; // slight offset to avoid z-fighting
  const light = {
    p0:[-Ls, ly, -Ls], p1:[ Ls, ly, -Ls], p2:[ Ls, ly,  Ls], p3:[-Ls, ly,  Ls],
    normal: [0,-1,0], area: (2*Ls)*(2*Ls), mat: MAT_LIGHT,
  };
  addQuad(light.p0, light.p1, light.p2, light.p3, MAT_LIGHT);

  // Intersection over all triangles
  function intersect(ro, rd) {
    let hitT = 1e20, hitN = null, hitIdx = -1;
    for (let i=0;i<tris.length;i+=3) {
      const v0=tris[i], v1=tris[i+1], v2=tris[i+2];
      const h = rayTri(ro, rd, v0, v1, v2);
      if (h && h.t < hitT) { hitT = h.t; hitN = h.n; hitIdx = i/3; }
    }
    if (hitIdx<0) return null;
    const mat = triMat[hitIdx];
    const pos = [ro[0]+rd[0]*hitT, ro[1]+rd[1]*hitT, ro[2]+rd[2]*hitT];
    return { t: hitT, n: hitN, pos, mat };
  }

  // Visibility check between two points
  function visible(a, b) {
    const dir = V.sub(b,a); const dist = V.len(dir); const rd = V.mul(dir, 1/(dist));
    const eps = 1e-4; const ro = V.add(a, V.mul(rd, eps));
    const h = intersect(ro, rd);
    if (!h) return true;
    return h.t + 1e-4 >= dist; // unobstructed if first hit beyond target
  }

  // Cosine-weighted hemisphere sample around normal n
  function cosineHemisphere(n) {
    const r1 = 2*Math.PI*rng();
    const r2 = rng(), r2s = Math.sqrt(r2);
    const u = Math.cos(r1)*r2s, v = Math.sin(r1)*r2s, w = Math.sqrt(1-r2);
    // Build ONB from n
    const t = Math.abs(n[1])<0.999 ? V.norm(V.cross([0,1,0], n)) : V.norm(V.cross([1,0,0], n));
    const b = V.cross(n, t);
    const d = [ t[0]*u + b[0]*v + n[0]*w,
                t[1]*u + b[1]*v + n[1]*w,
                t[2]*u + b[2]*v + n[2]*w ];
    return V.norm(d);
  }

  // Sample a point and direction from the light (uniform on area, cosine dir)
  function sampleLight() {
    const ux = rng(), uz = rng();
    const x = (ux*2-1)*0.4; const z = (uz*2-1)*0.4; // within light square of side 0.8
    const p = [x, light.p0[1], z];
    const n = light.normal;
    const d = cosineHemisphere(n); // emit downward along the light's normal (normal already points down)
    // pdf: area uniform * cosine hemisphere
    const pdfA = 1 / light.area;
    const pdfW = Math.max(0, V.dot(n, d)) / Math.PI;
    const emit = materials[MAT_LIGHT].emit; // radiance
    let throughput = [emit[0], emit[1], emit[2]]; // start with light radiance; scalars below
    // Scale to account for sampling densities (rough, educational)
    throughput = V.mul(throughput, 1/(pdfA*pdfW + 1e-8));
    return { p, n, d, throughput, pdfA, pdfW };
  }

  // Trace one diffuse bounce; returns next hit or null (escaped)
  function bounce(ro, rd) {
    const h = intersect(ro, rd);
    if (!h) return null;
    const m = materials[h.mat];
    return { pos: h.pos, n: h.n, matId: h.mat, mat: m };
  }

  // ===== BDPT sample for one pixel =====
  function bdptSample(px, py, cam, maxDepth) {
    // Camera ray through pixel jitter
    const u = (px + rng())/cam.w * 2 - 1;
    const v = (py + rng())/cam.h * 2 - 1;
    // Screen is at z = -1 in camera space
    const dirCam = V.norm([u*cam.fovScale, v*cam.fovScale, -1]);
    // Transform by camera basis
    const dir = V.norm([
      cam.right[0]*dirCam[0] + cam.up[0]*dirCam[1] + cam.forward[0]*dirCam[2],
      cam.right[1]*dirCam[0] + cam.up[1]*dirCam[1] + cam.forward[1]*dirCam[2],
      cam.right[2]*dirCam[0] + cam.up[2]*dirCam[1] + cam.forward[2]*dirCam[2]
    ]);
    const eyeVerts = [];
    let ro = cam.pos.slice(), rd = dir.slice();
    let throughput = [1,1,1];
    for (let d=0; d<maxDepth; d++) {
      const hit = bounce(ro, rd); if (!hit) break;
      const nl = V.dot(hit.n, V.mul(rd,-1))>0 ? hit.n : V.mul(hit.n,-1);
      eyeVerts.push({ pos: hit.pos, n: nl, through: throughput.slice(), matId: hit.matId });
      const m = hit.mat;
      if (V.len(m.emit) > 0) { // if we hit light, add emission (eye path endpoint at light)
        // Simple NEE-like add
        throughput = V.had(throughput, m.emit);
        break;
      }
      // Diffuse bounce
      const newDir = cosineHemisphere(nl);
      const cos = Math.max(0, V.dot(nl, newDir));
      throughput = V.had(throughput, V.mul(m.albedo, cos/Math.PI));
      // RR
      if (d>2) {
        const q = Math.max(0.05, Math.min(0.95, Math.max(throughput[0], throughput[1], throughput[2])));
        if (rng()>q) break; else throughput = V.mul(throughput, 1/q);
      }
      const eps=1e-4; ro = V.add(hit.pos, V.mul(newDir, eps)); rd = newDir;
    }

    // Build a short light subpath
    const lightVerts = [];
    let Lsamp = sampleLight();
    let lro = V.add(Lsamp.p, V.mul(Lsamp.d, 1e-4));
    let lrd = Lsamp.d.slice();
    let lthrough = Lsamp.throughput.slice();
    for (let d=0; d<maxDepth; d++) {
      const hit = bounce(lro, lrd); if (!hit) break;
      const nl = V.dot(hit.n, V.mul(lrd,-1))>0 ? hit.n : V.mul(hit.n,-1);
      lightVerts.push({ pos: hit.pos, n: nl, through: lthrough.slice(), matId: hit.matId });
      const m = hit.mat;
      if (V.len(m.emit) > 0 && d>0) { // hitting light again; stop
        break;
      }
      // Diffuse bounce
      const newDir = cosineHemisphere(nl);
      const cos = Math.max(0, V.dot(nl, newDir));
      lthrough = V.had(lthrough, V.mul(m.albedo, cos/Math.PI));
      if (d>2) {
        const q = Math.max(0.05, Math.min(0.95, Math.max(lthrough[0], lthrough[1], lthrough[2])));
        if (rng()>q) break; else lthrough = V.mul(lthrough, 1/q);
      }
      const eps=1e-4; lro = V.add(hit.pos, V.mul(newDir, eps)); lrd = newDir;
    }

    // Connect all pairs (eye i) — (light j)
    let C = [0,0,0];
    for (let i=0; i<eyeVerts.length; i++) {
      for (let j=0; j<lightVerts.length; j++) {
        const a = eyeVerts[i], b = lightVerts[j];
        if (materials[a.matId]===materials[MAT_LIGHT]) continue; // avoid trivial
        const dir = V.sub(b.pos, a.pos);
        const dist2 = Math.max(1e-8, V.dot(dir,dir));
        const dirN = V.mul(dir, 1/Math.sqrt(dist2));
        const cos1 = Math.max(0, V.dot(a.n, dirN));
        const cos2 = Math.max(0, V.dot(b.n, V.mul(dirN,-1)));
        if (cos1<=0 || cos2<=0) continue;
        if (!visible(a.pos, b.pos)) continue;
        const G = (cos1 * cos2) / dist2;
        // Include BRDF at both connection points
        const brdfA = V.mul(materials[a.matId].albedo, 1/Math.PI);
        const brdfB = V.mul(materials[b.matId].albedo, 1/Math.PI);
        const contrib = V.had(V.had(V.had(a.through, b.through), brdfA), V.mul(V.had(brdfB, [G,G,G]), 1));
        C = V.add(C, contrib);
      }
    }

    // Also add direct hit to light from last eye vertex (simple NEE)
    if (eyeVerts.length>0) {
      const a = eyeVerts[eyeVerts.length-1];
      // sample one point on light and connect
      const ux=rng(), uz=rng();
      const p = [ (ux*2-1)*0.4, light.p0[1], (uz*2-1)*0.4 ];
      const dir = V.sub(p, a.pos);
      const dist2 = Math.max(1e-8, V.dot(dir,dir));
      const dirN = V.mul(dir, 1/Math.sqrt(dist2));
      const cos1 = Math.max(0, V.dot(a.n, dirN));
      const cosL = Math.max(0, V.dot(light.normal, V.mul(dirN,-1)));
      if (cos1>0 && cosL>0 && visible(a.pos, p)) {
        const G = (cos1 * cosL) / dist2;
        const Le = materials[MAT_LIGHT].emit;
        const pdfA = 1/light.area;
        const contrib = V.mul(V.had(a.through, Le), (G / pdfA));
        C = V.add(C, contrib);
      }
    }

    return C;
  }

  // ===== Camera / render loop =====
  const canvas = document.getElementById('view');
  const ctx = canvas.getContext('2d');
  let W = canvas.width, H = canvas.height;
  let accumulation = new Float32Array(W*H*3);
  let spp = 0;

  const cam = {
    pos: [0, 1, 3.2],
    target: [0, 1, 0],
    upWorld: [0,1,0],
    fov: 45 * Math.PI/180,
    w: W, h: H,
    fovScale: 1,
    forward:[0,0,-1], right:[1,0,0], up:[0,1,0],
  };
  function updateCam() {
    cam.w=W; cam.h=H;
    cam.fovScale = Math.tan(cam.fov*0.5);
    const f = V.norm(V.sub(cam.target, cam.pos));
    const r = V.norm(V.cross(f, cam.upWorld));
    const u = V.cross(r, f);
    cam.forward=f; cam.right=r; cam.up=u;
  }
  updateCam();

  // Simple mouse controls
  let isDown=false, lastX=0, lastY=0; let yaw=0, pitch=0; let dist=3.2;
  function recalcCamFromAngles() {
    const cy = Math.cos(yaw), sy = Math.sin(yaw);
    const cp = Math.cos(pitch), sp = Math.sin(pitch);
    const dir = [sy*cp, sp, -cy*cp];
    cam.pos = V.add(cam.target, V.mul(dir, dist));
    updateCam(); resetAccum();
  }
  canvas.addEventListener('mousedown', e=>{isDown=true; lastX=e.clientX; lastY=e.clientY;});
  window.addEventListener('mouseup', ()=>isDown=false);
  window.addEventListener('mousemove', e=>{
    if(!isDown) return; const dx=(e.clientX-lastX)/200, dy=(e.clientY-lastY)/200; lastX=e.clientX; lastY=e.clientY;
    yaw -= dx; pitch = Math.max(-1.2, Math.min(1.2, pitch - dy)); recalcCamFromAngles();
  });
  window.addEventListener('wheel', e=>{ dist = Math.max(1.2, Math.min(6, dist + (e.deltaY>0?0.2:-0.2))); recalcCamFromAngles();});

  function resetAccum() { accumulation.fill(0); spp=0; }

  // UI controls
  const sppSlider = document.getElementById('spp'); const sppVal = document.getElementById('sppv');
  const depthSlider = document.getElementById('depth'); const depthVal = document.getElementById('depthv');
  const stats = document.getElementById('stats');
  sppSlider.oninput = ()=>{ sppVal.textContent = sppSlider.value; };
  depthSlider.oninput = ()=>{ depthVal.textContent = depthSlider.value; resetAccum(); };
  document.getElementById('reset').onclick = ()=> resetAccum();
  document.getElementById('toggle').onclick = ()=> running=!running;
  document.getElementById('half').onclick = ()=> resizeCanvas(0.5);
  document.getElementById('one').onclick = ()=> resizeCanvas(1);
  document.getElementById('double').onclick = ()=> resizeCanvas(2);

  function resizeCanvas(scale) {
    canvas.width = Math.round(320*scale); canvas.height = Math.round(240*scale);
    W=canvas.width; H=canvas.height; accumulation = new Float32Array(W*H*3); resetAccum(); updateCam();
  }

  let running = true;

  function renderFrame() {
    if (!running) { requestAnimationFrame(renderFrame); return; }
    const S = parseInt(sppSlider.value,10);
    const maxDepth = parseInt(depthSlider.value,10);
    for (let s=0;s<S;s++) {
      for (let y=0;y<H;y++) {
        for (let x=0;x<W;x++) {
          const c = bdptSample(x,y,cam,maxDepth);
          const idx = (y*W+x)*3;
          accumulation[idx  ] += c[0];
          accumulation[idx+1] += c[1];
          accumulation[idx+2] += c[2];
        }
      }
      spp++;
    }
    // tonemap + display
    const img = ctx.getImageData(0,0,W,H); const d = img.data;
    const inv = 1/Math.max(1,spp);
    for (let i=0, p=0; i<accumulation.length; i+=3) {
      // Simple Reinhard tonemap
      const r = accumulation[i  ]*inv, g = accumulation[i+1]*inv, b = accumulation[i+2]*inv;
      const t = (x)=> x/(1+x);
      d[p++] = Math.pow(t(r), 1/2.2)*255|0;
      d[p++] = Math.pow(t(g), 1/2.2)*255|0;
      d[p++] = Math.pow(t(b), 1/2.2)*255|0;
      d[p++] = 255;
    }
    ctx.putImageData(img,0,0);
    stats.textContent = `${spp} spp — ${W}×${H}`;
    requestAnimationFrame(renderFrame);
  }
  renderFrame();
})();
</script>
</body>
</html>
```

### mistral

```html
<!DOCTYPE html>
<html>
<head>
    <title>Bidirectional Path Tracer - Cornell Box</title>
    <style>body { margin: 0; overflow: hidden; }</style>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    <script>
        // =============================================
        // Scene Setup
        // =============================================
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Add orbit controls for navigation
        const controls = new THREE.OrbitControls(camera, renderer.domElement);

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const wallMaterial = new THREE.MeshLambertMaterial({ color: 0xffffff });

        // Walls
        const leftWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, boxSize, boxSize), wallMaterial);
        const rightWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, boxSize, boxSize), wallMaterial);
        const backWall = new THREE.Mesh(new THREE.BoxGeometry(boxSize, boxSize, 0.5), wallMaterial);
        const floor = new THREE.Mesh(new THREE.BoxGeometry(boxSize, 0.5, boxSize), wallMaterial);
        const ceiling = new THREE.Mesh(new THREE.BoxGeometry(boxSize, 0.5, boxSize), wallMaterial);

        leftWall.position.set(-boxSize/2, 0, 0);
        rightWall.position.set(boxSize/2, 0, 0);
        backWall.position.set(0, 0, -boxSize/2);
        floor.position.set(0, -boxSize/2, 0);
        ceiling.position.set(0, boxSize/2, 0);

        scene.add(leftWall, rightWall, backWall, floor, ceiling);

        // Light (emissive rectangle)
        const lightMaterial = new THREE.MeshBasicMaterial({
            color: 0xffffff,
            emissive: 0xffffff,
            emissiveIntensity: 5
        });
        const light = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 0.01), lightMaterial);
        light.position.set(0, boxSize/2 - 0.5, boxSize/2 - 0.5);
        scene.add(light);

        // Spheres (diffuse and reflective)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.5, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xff0000 })
        );
        sphere1.position.set(-1, -1, 0);
        scene.add(sphere1);

        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.5, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0x00ff00, shininess: 30 })
        );
        sphere2.position.set(1, -1, 0);
        scene.add(sphere2);

        // =============================================
        // Camera Position
        // =============================================
        camera.position.set(0, 2, 10);
        controls.update();

        // =============================================
        // Bidirectional Path Tracer (Simplified)
        // =============================================
        // This is a conceptual implementation.
        // In practice, you'd use WebGL shaders or a custom renderer.
        class PathTracer {
            constructor(scene, camera, width, height) {
                this.scene = scene;
                this.camera = camera;
                this.width = width;
                this.height = height;
                this.maxDepth = 5;
                this.samples = 0;
                this.renderTarget = new THREE.WebGLRenderTarget(width, height);
            }

            // Generate a random direction in a hemisphere
            sampleHemisphere(normal) {
                const u = Math.random();
                const v = Math.random();
                const theta = 2 * Math.PI * u;
                const phi = Math.acos(2 * v - 1);
                const x = Math.sin(phi) * Math.cos(theta);
                const y = Math.sin(phi) * Math.sin(theta);
                const z = Math.cos(phi);
                const dir = new THREE.Vector3(x, y, z);
                if (dir.dot(normal) < 0) dir.negate();
                return dir;
            }

            // Trace a path from a point and direction
            tracePath(origin, direction, depth) {
                if (depth > this.maxDepth) return new THREE.Color(0, 0, 0);

                const raycaster = new THREE.Raycaster(origin, direction);
                const intersects = raycaster.intersectObjects(this.scene.children, true);
                if (intersects.length === 0) return new THREE.Color(0, 0, 0);

                const hit = intersects[0];
                const hitObj = hit.object;
                const hitPoint = hit.point;
                const hitNormal = hit.normal;

                // If hit a light, return its emission
                if (hitObj.material.emissive) {
                    return hitObj.material.emissive.clone().multiplyScalar(hitObj.material.emissiveIntensity || 1);
                }

                // Sample new direction (diffuse reflection)
                const newDir = this.sampleHemisphere(hitNormal);
                const brdf = 1 / Math.PI; // Lambertian BRDF

                // Recursively trace
                const incoming = this.tracePath(hitPoint, newDir, depth + 1);
                return incoming.multiplyScalar(brdf);
            }

            // Connect light and eye paths (simplified)
            connectPaths(lightPath, eyePath) {
                // In a full implementation, you'd connect the last vertex of lightPath
                // to the first vertex of eyePath and compute the contribution.
                // This is a placeholder for the concept.
                return new THREE.Color(0.5, 0.5, 0.5);
            }

            // Render a pixel
            renderPixel(x, y) {
                const px = (x / this.width) * 2 - 1;
                const py = -(y / this.height) * 2 + 1;
                const direction = new THREE.Vector3(px, py, -1).unproject(this.camera).sub(this.camera.position).normalize();
                const color = this.tracePath(this.camera.position, direction, 0);
                return color;
            }

            // Render the scene (simplified)
            render() {
                const data = new Uint8Array(this.width * this.height * 4);
                for (let y = 0; y < this.height; y++) {
                    for (let x = 0; x < this.width; x++) {
                        const color = this.renderPixel(x, y);
                        const idx = (y * this.width + x) * 4;
                        data[idx] = Math.floor(color.r * 255);
                        data[idx + 1] = Math.floor(color.g * 255);
                        data[idx + 2] = Math.floor(color.b * 255);
                        data[idx + 3] = 255;
                    }
                }
                const texture = new THREE.DataTexture(data, this.width, this.height, THREE.RGBAFormat);
                texture.needsUpdate = true;
                this.renderTarget.texture = texture;
                return this.renderTarget.texture;
            }
        }

        // =============================================
        // Initialize Path Tracer
        // =============================================
        const pathTracer = new PathTracer(scene, camera, 256, 256);
        const resultTexture = pathTracer.render();

        // Display result (simplified)
        const resultMaterial = new THREE.MeshBasicMaterial({ map: resultTexture });
        const resultQuad = new THREE.Mesh(new THREE.PlaneGeometry(5, 5), resultMaterial);
        resultQuad.position.z = -5;
        scene.add(resultQuad);

        // =============================================
        // Animation Loop
        // =============================================
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>
```

### mistral

```html
<!DOCTYPE html>
<html>
<head>
    <title>Bidirectional Path Tracer - Cornell Box</title>
    <style>body { margin: 0; overflow: hidden; }</style>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    <script>
        // =============================================
        // Scene Setup
        // =============================================
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Add orbit controls for navigation
        const controls = new THREE.OrbitControls(camera, renderer.domElement);

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const wallMaterial = new THREE.MeshLambertMaterial({ color: 0xffffff });

        // Walls
        const leftWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, boxSize, boxSize), wallMaterial);
        const rightWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, boxSize, boxSize), wallMaterial);
        const backWall = new THREE.Mesh(new THREE.BoxGeometry(boxSize, boxSize, 0.5), wallMaterial);
        const floor = new THREE.Mesh(new THREE.BoxGeometry(boxSize, 0.5, boxSize), wallMaterial);
        const ceiling = new THREE.Mesh(new THREE.BoxGeometry(boxSize, 0.5, boxSize), wallMaterial);

        leftWall.position.set(-boxSize/2, 0, 0);
        rightWall.position.set(boxSize/2, 0, 0);
        backWall.position.set(0, 0, -boxSize/2);
        floor.position.set(0, -boxSize/2, 0);
        ceiling.position.set(0, boxSize/2, 0);

        scene.add(leftWall, rightWall, backWall, floor, ceiling);

        // Light (emissive rectangle)
        const lightMaterial = new THREE.MeshBasicMaterial({
            color: 0xffffff,
            emissive: 0xffffff,
            emissiveIntensity: 5
        });
        const light = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 0.01), lightMaterial);
        light.position.set(0, boxSize/2 - 0.5, boxSize/2 - 0.5);
        scene.add(light);

        // Spheres (diffuse and reflective)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.5, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xff0000 })
        );
        sphere1.position.set(-1, -1, 0);
        scene.add(sphere1);

        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.5, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0x00ff00, shininess: 30 })
        );
        sphere2.position.set(1, -1, 0);
        scene.add(sphere2);

        // =============================================
        // Camera Position
        // =============================================
        camera.position.set(0, 2, 10);
        controls.update();

        // =============================================
        // Path Tracer (Simplified)
        // =============================================
        class PathTracer {
            constructor(scene, camera, width, height) {
                this.scene = scene;
                this.camera = camera;
                this.width = width;
                this.height = height;
                this.maxDepth = 3;
                this.samplesPerPixel = 1;
            }

            // Generate a random direction in a hemisphere
            sampleHemisphere(normal) {
                const u = Math.random();
                const v = Math.random();
                const theta = 2 * Math.PI * u;
                const phi = Math.acos(2 * v - 1);
                const x = Math.sin(phi) * Math.cos(theta);
                const y = Math.sin(phi) * Math.sin(theta);
                const z = Math.cos(phi);
                const dir = new THREE.Vector3(x, y, z);
                if (dir.dot(normal) < 0) dir.negate();
                return dir;
            }

            // Trace a path from a point and direction
            tracePath(origin, direction, depth) {
                if (depth > this.maxDepth) return new THREE.Color(0, 0, 0);

                const raycaster = new THREE.Raycaster(origin, direction);
                const intersects = raycaster.intersectObjects(this.scene.children, true);
                if (intersects.length === 0) return new THREE.Color(0, 0, 0);

                const hit = intersects[0];
                const hitObj = hit.object;
                const hitPoint = hit.point;
                const hitNormal = hit.normal;

                // If hit a light, return its emission
                if (hitObj.material.emissive) {
                    return hitObj.material.emissive.clone().multiplyScalar(hitObj.material.emissiveIntensity || 1);
                }

                // Sample new direction (diffuse reflection)
                const newDir = this.sampleHemisphere(hitNormal);
                const brdf = 1 / Math.PI; // Lambertian BRDF

                // Recursively trace
                const incoming = this.tracePath(hitPoint, newDir, depth + 1);
                return incoming.multiplyScalar(brdf);
            }

            // Render a pixel
            renderPixel(x, y) {
                const px = (x / this.width) * 2 - 1;
                const py = -(y / this.height) * 2 + 1;
                const direction = new THREE.Vector3(px, py, -1).unproject(this.camera).sub(this.camera.position).normalize();
                let color = new THREE.Color(0, 0, 0);
                for (let s = 0; s < this.samplesPerPixel; s++) {
                    color.add(this.tracePath(this.camera.position, direction, 0));
                }
                color.divideScalar(this.samplesPerPixel);
                return color;
            }

            // Render the scene
            render() {
                const data = new Uint8Array(this.width * this.height * 4);
                for (let y = 0; y < this.height; y++) {
                    for (let x = 0; x < this.width; x++) {
                        const color = this.renderPixel(x, y);
                        const idx = (y * this.width + x) * 4;
                        data[idx] = Math.floor(color.r * 255);
                        data[idx + 1] = Math.floor(color.g * 255);
                        data[idx + 2] = Math.floor(color.b * 255);
                        data[idx + 3] = 255;
                    }
                }
                const texture = new THREE.DataTexture(data, this.width, this.height, THREE.RGBAFormat);
                texture.needsUpdate = true;
                return texture;
            }
        }

        // =============================================
        // Initialize Path Tracer
        // =============================================
        const pathTracer = new PathTracer(scene, camera, 256, 256);
        const resultTexture = pathTracer.render();

        // Display result
        const resultMaterial = new THREE.MeshBasicMaterial({ map: resultTexture });
        const resultQuad = new THREE.Mesh(new THREE.PlaneGeometry(5, 5), resultMaterial);
        resultQuad.position.z = -5;
        scene.add(resultQuad);

        // =============================================
        // Animation Loop
        // =============================================
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>
```

### claude

```html
<!DOCTYPE html>
<html>
<head>
    <title>Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="controls">
        <div>Samples: <span id="samples">0</span></div>
        <div>Progress: <span id="progress">0%</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <div style="margin-top: 10px;">
            <label>Samples/Frame: <input type="number" id="spp" value="1" min="1" max="10"></label>
        </div>
        <div>
            <label>Max Bounces: <input type="number" id="bounces" value="4" min="1" max="8"></label>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const objects = [];

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        scene.add(leftWall);
        objects.push({ mesh: leftWall, type: 'diffuse', color: [1, 0, 0] });

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        scene.add(rightWall);
        objects.push({ mesh: rightWall, type: 'diffuse', color: [0, 1, 0] });

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xcccccc, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        scene.add(backWall);
        objects.push({ mesh: backWall, type: 'diffuse', color: [0.8, 0.8, 0.8] });

        // Floor (white)
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xcccccc, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = Math.PI / 2;
        scene.add(floor);
        objects.push({ mesh: floor, type: 'diffuse', color: [0.8, 0.8, 0.8] });

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xcccccc, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        scene.add(ceiling);
        objects.push({ mesh: ceiling, type: 'diffuse', color: [0.8, 0.8, 0.8] });

        // Light (area light)
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        scene.add(light);
        objects.push({ mesh: light, type: 'emissive', color: [1, 1, 1], emission: [15, 15, 15] });

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        scene.add(sphere1);
        objects.push({ mesh: sphere1, type: 'diffuse', color: [0.9, 0.9, 0.9] });

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        scene.add(sphere2);
        objects.push({ mesh: sphere2, type: 'reflective', color: [0.95, 0.95, 0.95] });

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        controls.update();

        // =============================================
        // Path Tracer
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        let imageData = ctx.createImageData(width, height);
        let accumBuffer = new Float32Array(width * height * 3);
        let sampleCount = 0;
        let isTracing = false;
        let currentPixel = 0;

        const raycaster = new THREE.Raycaster();

        function random() {
            return Math.random();
        }

        function randomInUnitSphere() {
            while (true) {
                const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
            }
        }

        function randomInHemisphere(normal) {
            const v = randomInUnitSphere();
            const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
            if (dot > 0) return v;
            return [-v[0], -v[1], -v[2]];
        }

        function reflect(v, n) {
            const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
            return [
                v[0] - 2*dot*n[0],
                v[1] - 2*dot*n[1],
                v[2] - 2*dot*n[2]
            ];
        }

        function normalize(v) {
            const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
            return [v[0]/len, v[1]/len, v[2]/len];
        }

        function trace(origin, direction, depth, maxDepth) {
            if (depth >= maxDepth) return [0, 0, 0];

            raycaster.set(
                new THREE.Vector3(origin[0], origin[1], origin[2]),
                new THREE.Vector3(direction[0], direction[1], direction[2])
            );

            const intersects = raycaster.intersectObjects(objects.map(o => o.mesh));
            if (intersects.length === 0) return [0.1, 0.1, 0.15]; // Sky color

            const hit = intersects[0];
            const obj = objects.find(o => o.mesh === hit.object);
            
            const hitPoint = [hit.point.x, hit.point.y, hit.point.z];
            const hitNormal = [hit.face.normal.x, hit.face.normal.y, hit.face.normal.z];
            
            // Transform normal to world space
            const normalMatrix = new THREE.Matrix3().getNormalMatrix(hit.object.matrixWorld);
            const worldNormal = new THREE.Vector3(hitNormal[0], hitNormal[1], hitNormal[2])
                .applyMatrix3(normalMatrix).normalize();
            const normal = [worldNormal.x, worldNormal.y, worldNormal.z];

            // Offset hit point slightly along normal to avoid self-intersection
            const offset = 0.001;
            hitPoint[0] += normal[0] * offset;
            hitPoint[1] += normal[1] * offset;
            hitPoint[2] += normal[2] * offset;

            // If hit emissive surface, return emission
            if (obj.type === 'emissive') {
                return obj.emission;
            }

            // Sample new direction based on material
            let newDir;
            let attenuation = obj.color;

            if (obj.type === 'reflective') {
                newDir = reflect(direction, normal);
                newDir = normalize(newDir);
            } else {
                newDir = randomInHemisphere(normal);
                newDir = normalize(newDir);
            }

            // Recursive trace
            const incoming = trace(hitPoint, newDir, depth + 1, maxDepth);
            return [
                attenuation[0] * incoming[0],
                attenuation[1] * incoming[1],
                attenuation[2] * incoming[2]
            ];
        }

        function getRay(x, y) {
            // Add random offset for anti-aliasing
            const u = (x + random()) / width;
            const v = (y + random()) / height;
            
            const px = (u * 2 - 1) * Math.tan(camera.fov * Math.PI / 360) * camera.aspect;
            const py = -(v * 2 - 1) * Math.tan(camera.fov * Math.PI / 360);
            
            const dir = new THREE.Vector3(px, py, -1);
            dir.applyQuaternion(camera.quaternion);
            dir.normalize();
            
            return {
                origin: [camera.position.x, camera.position.y, camera.position.z],
                direction: [dir.x, dir.y, dir.z]
            };
        }

        function pathTraceFrame() {
            if (!isTracing) return;

            const samplesPerFrame = parseInt(document.getElementById('spp').value);
            const maxBounces = parseInt(document.getElementById('bounces').value);
            const pixelsPerFrame = Math.min(width * height, 1000);

            for (let i = 0; i < pixelsPerFrame; i++) {
                const pixelIndex = currentPixel;
                const x = pixelIndex % width;
                const y = Math.floor(pixelIndex / width);

                for (let s = 0; s < samplesPerFrame; s++) {
                    const ray = getRay(x, y);
                    const color = trace(ray.origin, ray.direction, 0, maxBounces);
                    
                    const idx = (y * width + x) * 3;
                    accumBuffer[idx] += color[0];
                    accumBuffer[idx + 1] += color[1];
                    accumBuffer[idx + 2] += color[2];
                }

                currentPixel++;
                if (currentPixel >= width * height) {
                    currentPixel = 0;
                    sampleCount += samplesPerFrame;
                }
            }

            // Update display
            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    const idx = (y * width + x) * 3;
                    const imgIdx = (y * width + x) * 4;
                    
                    const scale = 1.0 / (sampleCount || 1);
                    let r = accumBuffer[idx] * scale;
                    let g = accumBuffer[idx + 1] * scale;
                    let b = accumBuffer[idx + 2] * scale;
                    
                    // Gamma correction
                    r = Math.pow(r, 1/2.2);
                    g = Math.pow(g, 1/2.2);
                    b = Math.pow(b, 1/2.2);
                    
                    imageData.data[imgIdx] = Math.min(255, r * 255);
                    imageData.data[imgIdx + 1] = Math.min(255, g * 255);
                    imageData.data[imgIdx + 2] = Math.min(255, b * 255);
                    imageData.data[imgIdx + 3] = 255;
                }
            }
            
            ctx.putImageData(imageData, 0, 0);
            
            document.getElementById('samples').textContent = sampleCount;
            document.getElementById('progress').textContent = 
                Math.floor((currentPixel / (width * height)) * 100) + '%';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            isTracing = !isTracing;
            document.getElementById('togglePT').textContent = 
                isTracing ? 'Pause Path Tracing' : 'Resume Path Tracing';
        });

        document.getElementById('reset').addEventListener('click', () => {
            accumBuffer.fill(0);
            sampleCount = 0;
            currentPixel = 0;
            ctx.clearRect(0, 0, width, height);
        });

        // =============================================
        // Animation Loop
        // =============================================
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
            
            if (isTracing) {
                pathTraceFrame();
            }
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            imageData = ctx.createImageData(width, height);
            accumBuffer = new Float32Array(width * height * 3);
            sampleCount = 0;
            currentPixel = 0;
        });
    </script>
</body>
</html>
```

### buckets

```html
<!DOCTYPE html>
<html>
<head>
    <title>Multi-Core Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 250px;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
        .bucket { 
            position: absolute; 
            border: 1px solid rgba(255,255,0,0.5); 
            pointer-events: none;
        }
        #bucketViz { position: absolute; top: 0; left: 0; pointer-events: none; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="bucketViz"></div>
    <div id="controls">
        <div><strong>Multi-Core Path Tracer</strong></div>
        <div>Cores: <span id="cores">0</span></div>
        <div>Samples: <span id="samples">0</span></div>
        <div>Buckets Completed: <span id="bucketsCompleted">0</span>/<span id="bucketsTotal">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <div style="margin-top: 10px;">
            <label>Samples/Bucket: <input type="number" id="spp" value="16" min="1" max="100"></label>
        </div>
        <div>
            <label>Max Bounces: <input type="number" id="bounces" value="4" min="1" max="8"></label>
        </div>
        <div>
            <label><input type="checkbox" id="showBuckets" checked> Show Buckets</label>
        </div>
        <div style="margin-top: 5px; font-size: 11px; color: #aaa;">
            Bucket size: <span id="bucketSize">64x64</span>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];

        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ 
                mesh, 
                type, 
                color, 
                emission,
                // Pre-compute world matrix
                worldMatrix: mesh.matrixWorld.clone()
            });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xcccccc, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.8, 0.8, 0.8]);

        // Floor (white)
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xcccccc, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = Math.PI / 2;
        addObject(floor, 'diffuse', [0.8, 0.8, 0.8]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xcccccc, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.8, 0.8, 0.8]);

        // Light (area light)
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [15, 15, 15]);

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        controls.update();

        // Update world matrices
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(obj => {
            obj.worldMatrix = obj.mesh.matrixWorld.clone();
        });

        // =============================================
        // Multi-Core Bucket Rendering System
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const BUCKET_SIZE = 64;
        const numCores = navigator.hardwareConcurrency || 4;
        document.getElementById('cores').textContent = numCores;

        let workers = [];
        let buckets = [];
        let bucketsCompleted = 0;
        let isTracing = false;
        let sampleCount = 0;
        let imageData = ctx.createImageData(width, height);

        // Create bucket list
        function createBuckets() {
            buckets = [];
            const cols = Math.ceil(width / BUCKET_SIZE);
            const rows = Math.ceil(height / BUCKET_SIZE);
            
            for (let y = 0; y < rows; y++) {
                for (let x = 0; x < cols; x++) {
                    buckets.push({
                        x: x * BUCKET_SIZE,
                        y: y * BUCKET_SIZE,
                        width: Math.min(BUCKET_SIZE, width - x * BUCKET_SIZE),
                        height: Math.min(BUCKET_SIZE, height - y * BUCKET_SIZE),
                        completed: false
                    });
                }
            }
            
            // Shuffle buckets for better visual feedback
            for (let i = buckets.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [buckets[i], buckets[j]] = [buckets[j], buckets[i]];
            }
            
            document.getElementById('bucketsTotal').textContent = buckets.length;
            document.getElementById('bucketSize').textContent = `${BUCKET_SIZE}x${BUCKET_SIZE}`;
        }

        // Worker code as a blob
        const workerCode = `
            const raycaster = {};
            
            function intersectRay(origin, direction, objects) {
                let closest = null;
                let minDist = Infinity;
                
                for (const obj of objects) {
                    const result = intersectObject(origin, direction, obj);
                    if (result && result.distance < minDist) {
                        minDist = result.distance;
                        closest = result;
                        closest.object = obj;
                    }
                }
                
                return closest;
            }
            
            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') {
                    return intersectSphere(origin, direction, obj);
                } else if (obj.geometry === 'plane') {
                    return intersectPlane(origin, direction, obj);
                }
                return null;
            }
            
            function intersectSphere(origin, direction, obj) {
                const center = obj.position;
                const radius = obj.radius;
                const oc = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - radius*radius;
                const discriminant = b*b - 4*a*c;
                
                if (discriminant < 0) return null;
                
                const t = (-b - Math.sqrt(discriminant)) / (2*a);
                if (t < 0.001) return null;
                
                const point = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const normal = [
                    (point[0] - center[0]) / radius,
                    (point[1] - center[1]) / radius,
                    (point[2] - center[2]) / radius
                ];
                
                return { distance: t, point, normal };
            }
            
            function intersectPlane(origin, direction, obj) {
                const normal = obj.normal;
                const point = obj.position;
                
                const denom = normal[0]*direction[0] + normal[1]*direction[1] + normal[2]*direction[2];
                if (Math.abs(denom) < 0.0001) return null;
                
                const diff = [point[0] - origin[0], point[1] - origin[1], point[2] - origin[2]];
                const t = (diff[0]*normal[0] + diff[1]*normal[1] + diff[2]*normal[2]) / denom;
                
                if (t < 0.001) return null;
                
                const hitPoint = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                // Check if hit point is within plane bounds
                const localPoint = [
                    hitPoint[0] - point[0],
                    hitPoint[1] - point[1],
                    hitPoint[2] - point[2]
                ];
                
                const size = obj.size;
                const u = obj.uAxis;
                const v = obj.vAxis;
                
                const uCoord = localPoint[0]*u[0] + localPoint[1]*u[1] + localPoint[2]*u[2];
                const vCoord = localPoint[0]*v[0] + localPoint[1]*v[1] + localPoint[2]*v[2];
                
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;
                
                return { distance: t, point: hitPoint, normal };
            }
            
            function random() {
                return Math.random();
            }
            
            function randomInUnitSphere() {
                while (true) {
                    const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                    if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
                }
            }
            
            function randomInHemisphere(normal) {
                const v = randomInUnitSphere();
                const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
                if (dot > 0) return v;
                return [-v[0], -v[1], -v[2]];
            }
            
            function reflect(v, n) {
                const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
                return [v[0] - 2*dot*n[0], v[1] - 2*dot*n[1], v[2] - 2*dot*n[2]];
            }
            
            function normalize(v) {
                const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
                return len > 0 ? [v[0]/len, v[1]/len, v[2]/len] : v;
            }
            
            function trace(origin, direction, depth, maxDepth, objects) {
                if (depth >= maxDepth) return [0, 0, 0];
                
                const hit = intersectRay(origin, direction, objects);
                if (!hit) return [0.1, 0.1, 0.15];
                
                const obj = hit.object;
                const hitPoint = hit.point;
                const normal = hit.normal;
                
                const offset = 0.001;
                const offsetPoint = [
                    hitPoint[0] + normal[0] * offset,
                    hitPoint[1] + normal[1] * offset,
                    hitPoint[2] + normal[2] * offset
                ];
                
                if (obj.type === 'emissive') {
                    return obj.emission;
                }
                
                let newDir;
                const attenuation = obj.color;
                
                if (obj.type === 'reflective') {
                    newDir = reflect(direction, normal);
                    newDir = normalize(newDir);
                } else {
                    newDir = randomInHemisphere(normal);
                    newDir = normalize(newDir);
                }
                
                const incoming = trace(offsetPoint, newDir, depth + 1, maxDepth, objects);
                return [
                    attenuation[0] * incoming[0],
                    attenuation[1] * incoming[1],
                    attenuation[2] * incoming[2]
                ];
            }
            
            self.onmessage = function(e) {
                const { bucket, camera, objects, samplesPerPixel, maxBounces, width, height } = e.data;
                
                const data = new Float32Array(bucket.width * bucket.height * 3);
                
                for (let y = 0; y < bucket.height; y++) {
                    for (let x = 0; x < bucket.width; x++) {
                        const screenX = bucket.x + x;
                        const screenY = bucket.y + y;
                        
                        let color = [0, 0, 0];
                        
                        for (let s = 0; s < samplesPerPixel; s++) {
                            const u = (screenX + random()) / width;
                            const v = (screenY + random()) / height;
                            
                            const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                            const py = -(v * 2 - 1) * camera.tanFov;
                            
                            let dir = [px, py, -1];
                            const len = Math.sqrt(dir[0]*dir[0] + dir[1]*dir[1] + dir[2]*dir[2]);
                            dir = [dir[0]/len, dir[1]/len, dir[2]/len];
                            
                            // Apply camera rotation
                            const q = camera.quaternion;
                            const rotated = rotateByQuaternion(dir, q);
                            
                            const sample = trace(camera.position, rotated, 0, maxBounces, objects);
                            color[0] += sample[0];
                            color[1] += sample[1];
                            color[2] += sample[2];
                        }
                        
                        const idx = (y * bucket.width + x) * 3;
                        data[idx] = color[0] / samplesPerPixel;
                        data[idx + 1] = color[1] / samplesPerPixel;
                        data[idx + 2] = color[2] / samplesPerPixel;
                    }
                }
                
                self.postMessage({ bucket, data });
            };
            
            function rotateByQuaternion(v, q) {
                const qx = q[0], qy = q[1], qz = q[2], qw = q[3];
                const x = v[0], y = v[1], z = v[2];
                
                const ix = qw * x + qy * z - qz * y;
                const iy = qw * y + qz * x - qx * z;
                const iz = qw * z + qx * y - qy * x;
                const iw = -qx * x - qy * y - qz * z;
                
                return [
                    ix * qw + iw * -qx + iy * -qz - iz * -qy,
                    iy * qw + iw * -qy + iz * -qx - ix * -qz,
                    iz * qw + iw * -qz + ix * -qy - iy * -qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        // Create workers
        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            
            for (let i = 0; i < numCores; i++) {
                const worker = new Worker(workerUrl);
                worker.onmessage = handleWorkerResult;
                worker.idle = true;
                workers.push(worker);
            }
        }

        // Convert Three.js objects to worker-compatible format
        function serializeObjects() {
            const serialized = [];
            
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1);
                    normal.applyQuaternion(mesh.quaternion).normalize();
                    
                    const uAxis = new THREE.Vector3(1, 0, 0);
                    uAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    const vAxis = new THREE.Vector3(0, 1, 0);
                    vAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            
            return serialized;
        }

        // Handle worker results
        function handleWorkerResult(e) {
            const { bucket, data } = e.data;
            
            // Update image data
            for (let y = 0; y < bucket.height; y++) {
                for (let x = 0; x < bucket.width; x++) {
                    const srcIdx = (y * bucket.width + x) * 3;
                    const dstIdx = ((bucket.y + y) * width + (bucket.x + x)) * 4;
                    
                    let r = data[srcIdx];
                    let g = data[srcIdx + 1];
                    let b = data[srcIdx + 2];
                    
                    // Gamma correction
                    r = Math.pow(r, 1/2.2);
                    g = Math.pow(g, 1/2.2);
                    b = Math.pow(b, 1/2.2);
                    
                    imageData.data[dstIdx] = Math.min(255, r * 255);
                    imageData.data[dstIdx + 1] = Math.min(255, g * 255);
                    imageData.data[dstIdx + 2] = Math.min(255, b * 255);
                    imageData.data[dstIdx + 3] = 255;
                }
            }
            
            ctx.putImageData(imageData, 0, 0);
            
            // Mark bucket as completed
            const bucketIndex = buckets.findIndex(b => 
                b.x === bucket.x && b.y === bucket.y && !b.completed
            );
            if (bucketIndex !== -1) {
                buckets[bucketIndex].completed = true;
                bucketsCompleted++;
                document.getElementById('bucketsCompleted').textContent = bucketsCompleted;
                
                // Visualize completed bucket
                if (document.getElementById('showBuckets').checked) {
                    visualizeBucket(bucket);
                }
            }
            
            // Mark worker as idle and assign next bucket
            e.target.idle = true;
            assignNextBucket(e.target);
        }

        // Visualize bucket being rendered
        function visualizeBucket(bucket) {
            const div = document.createElement('div');
            div.className = 'bucket';
            div.style.left = bucket.x + 'px';
            div.style.top = bucket.y + 'px';
            div.style.width = bucket.width + 'px';
            div.style.height = bucket.height + 'px';
            document.getElementById('bucketViz').appendChild(div);
            
            setTimeout(() => div.remove(), 500);
        }

        // Assign next bucket to worker
        function assignNextBucket(worker) {
            if (!isTracing) return;
            
            const nextBucket = buckets.find(b => !b.completed);
            if (!nextBucket) {
                // All buckets completed, start next pass
                if (isTracing) {
                    sampleCount += parseInt(document.getElementById('spp').value);
                    document.getElementById('samples').textContent = sampleCount;
                    startNewPass();
                }
                return;
            }
            
            worker.idle = false;
            
            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };
            
            worker.postMessage({
                bucket: nextBucket,
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerPixel: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width: width,
                height: height
            });
        }

        // Start new rendering pass
        function startNewPass() {
            bucketsCompleted = 0;
            document.getElementById('bucketsCompleted').textContent = '0';
            
            buckets.forEach(b => b.completed = false);
            
            // Shuffle buckets again for variety
            for (let i = buckets.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [buckets[i], buckets[j]] = [buckets[j], buckets[i]];
            }
            
            // Assign buckets to all idle workers
            workers.filter(w => w.idle).forEach(w => assignNextBucket(w));
        }

        // Start rendering
        function startRendering() {
            isTracing = true;
            createBuckets();
            initWorkers();
            
            // Start all workers
            workers.forEach(w => assignNextBucket(w));
        }

        // Stop rendering
        function stopRendering() {
            isTracing = false;
        }

        // Reset
        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);
            sampleCount = 0;
            bucketsCompleted = 0;
            document.getElementById('samples').textContent = '0';
            document.getElementById('bucketsCompleted').textContent = '0';
            document.getElementById('bucketViz').innerHTML = '';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (bucketsCompleted === 0) {
                    startRendering();
                } else {
                    isTracing = true;
                    startNewPass();
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });

        document.getElementById('reset').addEventListener('click', resetRendering);

        // =============================================
        // Animation Loop
        // =============================================
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### espiral

```html
<!DOCTYPE html>
<html>
<head>
    <title>Multi-Core Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 250px;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
        .bucket { 
            position: absolute; 
            border: 1px solid rgba(255,255,0,0.5); 
            pointer-events: none;
        }
        #bucketViz { position: absolute; top: 0; left: 0; pointer-events: none; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="bucketViz"></div>
    <div id="controls">
        <div><strong>Multi-Core Path Tracer</strong></div>
        <div>Cores: <span id="cores">0</span></div>
        <div>Samples: <span id="samples">0</span></div>
        <div>Buckets Completed: <span id="bucketsCompleted">0</span>/<span id="bucketsTotal">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <div style="margin-top: 10px;">
            <label>Samples/Bucket: <input type="number" id="spp" value="16" min="1" max="100"></label>
        </div>
        <div>
            <label>Max Bounces: <input type="number" id="bounces" value="4" min="1" max="8"></label>
        </div>
        <div>
            <label><input type="checkbox" id="showBuckets" checked> Show Buckets</label>
        </div>
        <div style="margin-top: 5px; font-size: 11px; color: #aaa;">
            Bucket size: <span id="bucketSize">64x64</span>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];

        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ 
                mesh, 
                type, 
                color, 
                emission,
                // Pre-compute world matrix
                worldMatrix: mesh.matrixWorld.clone()
            });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xcccccc, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.8, 0.8, 0.8]);

        // Floor (white)
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = Math.PI / 2;
        addObject(floor, 'diffuse', [0.8, 0.8, 0.8]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xcccccc, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.8, 0.8, 0.8]);

        // Light (area light) - much brighter
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        controls.update();

        // Update world matrices
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(obj => {
            obj.worldMatrix = obj.mesh.matrixWorld.clone();
        });

        // =============================================
        // Multi-Core Bucket Rendering System
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const BUCKET_SIZE = 64;
        const numCores = navigator.hardwareConcurrency || 4;
        document.getElementById('cores').textContent = numCores;

        let workers = [];
        let buckets = [];
        let bucketsCompleted = 0;
        let isTracing = false;
        let sampleCount = 0;
        let imageData = ctx.createImageData(width, height);

        // Create bucket list in spiral order from center
        function createBuckets() {
            buckets = [];
            const cols = Math.ceil(width / BUCKET_SIZE);
            const rows = Math.ceil(height / BUCKET_SIZE);
            
            const allBuckets = [];
            for (let y = 0; y < rows; y++) {
                for (let x = 0; x < cols; x++) {
                    allBuckets.push({
                        x: x * BUCKET_SIZE,
                        y: y * BUCKET_SIZE,
                        width: Math.min(BUCKET_SIZE, width - x * BUCKET_SIZE),
                        height: Math.min(BUCKET_SIZE, height - y * BUCKET_SIZE),
                        completed: false,
                        gridX: x,
                        gridY: y
                    });
                }
            }
            
            // Sort buckets in spiral order from center
            const centerX = cols / 2;
            const centerY = rows / 2;
            
            allBuckets.sort((a, b) => {
                const distA = Math.sqrt(Math.pow(a.gridX - centerX, 2) + Math.pow(a.gridY - centerY, 2));
                const distB = Math.sqrt(Math.pow(b.gridX - centerX, 2) + Math.pow(b.gridY - centerY, 2));
                
                if (Math.abs(distA - distB) < 0.5) {
                    // Same distance ring, sort by angle for spiral effect
                    const angleA = Math.atan2(a.gridY - centerY, a.gridX - centerX);
                    const angleB = Math.atan2(b.gridY - centerY, b.gridX - centerX);
                    return angleA - angleB;
                }
                
                return distA - distB;
            });
            
            buckets = allBuckets;
            
            document.getElementById('bucketsTotal').textContent = buckets.length;
            document.getElementById('bucketSize').textContent = `${BUCKET_SIZE}x${BUCKET_SIZE}`;
        }

        // Worker code as a blob
        const workerCode = `
            const raycaster = {};
            
            function intersectRay(origin, direction, objects) {
                let closest = null;
                let minDist = Infinity;
                
                for (const obj of objects) {
                    const result = intersectObject(origin, direction, obj);
                    if (result && result.distance < minDist) {
                        minDist = result.distance;
                        closest = result;
                        closest.object = obj;
                    }
                }
                
                return closest;
            }
            
            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') {
                    return intersectSphere(origin, direction, obj);
                } else if (obj.geometry === 'plane') {
                    return intersectPlane(origin, direction, obj);
                }
                return null;
            }
            
            function intersectSphere(origin, direction, obj) {
                const center = obj.position;
                const radius = obj.radius;
                const oc = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - radius*radius;
                const discriminant = b*b - 4*a*c;
                
                if (discriminant < 0) return null;
                
                const t = (-b - Math.sqrt(discriminant)) / (2*a);
                if (t < 0.001) return null;
                
                const point = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const normal = [
                    (point[0] - center[0]) / radius,
                    (point[1] - center[1]) / radius,
                    (point[2] - center[2]) / radius
                ];
                
                return { distance: t, point, normal };
            }
            
            function intersectPlane(origin, direction, obj) {
                const normal = obj.normal;
                const point = obj.position;
                
                const denom = normal[0]*direction[0] + normal[1]*direction[1] + normal[2]*direction[2];
                if (Math.abs(denom) < 0.0001) return null;
                
                const diff = [point[0] - origin[0], point[1] - origin[1], point[2] - origin[2]];
                const t = (diff[0]*normal[0] + diff[1]*normal[1] + diff[2]*normal[2]) / denom;
                
                if (t < 0.001) return null;
                
                const hitPoint = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                // Check if hit point is within plane bounds
                const localPoint = [
                    hitPoint[0] - point[0],
                    hitPoint[1] - point[1],
                    hitPoint[2] - point[2]
                ];
                
                const size = obj.size;
                const u = obj.uAxis;
                const v = obj.vAxis;
                
                const uCoord = localPoint[0]*u[0] + localPoint[1]*u[1] + localPoint[2]*u[2];
                const vCoord = localPoint[0]*v[0] + localPoint[1]*v[1] + localPoint[2]*v[2];
                
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;
                
                return { distance: t, point: hitPoint, normal };
            }
            
            function random() {
                return Math.random();
            }
            
            function randomInUnitSphere() {
                while (true) {
                    const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                    if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
                }
            }
            
            function randomInHemisphere(normal) {
                const v = randomInUnitSphere();
                const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
                if (dot > 0) return v;
                return [-v[0], -v[1], -v[2]];
            }
            
            function reflect(v, n) {
                const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
                return [v[0] - 2*dot*n[0], v[1] - 2*dot*n[1], v[2] - 2*dot*n[2]];
            }
            
            function normalize(v) {
                const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
                return len > 0 ? [v[0]/len, v[1]/len, v[2]/len] : v;
            }
            
            function trace(origin, direction, depth, maxDepth, objects) {
                if (depth >= maxDepth) return [0, 0, 0];
                
                const hit = intersectRay(origin, direction, objects);
                if (!hit) return [0, 0, 0]; // Black background, no ambient light
                
                const obj = hit.object;
                const hitPoint = hit.point;
                const normal = hit.normal;
                
                const offset = 0.001;
                const offsetPoint = [
                    hitPoint[0] + normal[0] * offset,
                    hitPoint[1] + normal[1] * offset,
                    hitPoint[2] + normal[2] * offset
                ];
                
                // If we hit a light source, return its emission
                if (obj.type === 'emissive') {
                    return obj.emission;
                }
                
                // For diffuse surfaces, use proper BRDF with cosine weighting
                const attenuation = obj.color;
                
                if (obj.type === 'reflective') {
                    // Perfect specular reflection
                    const newDir = reflect(direction, normal);
                    const normalized = normalize(newDir);
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    return [
                        attenuation[0] * incoming[0],
                        attenuation[1] * incoming[1],
                        attenuation[2] * incoming[2]
                    ];
                } else {
                    // Diffuse reflection with proper importance sampling
                    const newDir = randomInHemisphere(normal);
                    const normalized = normalize(newDir);
                    
                    // Cosine term (Lambert's law)
                    const cosTheta = Math.max(0, 
                        normalized[0] * normal[0] + 
                        normalized[1] * normal[1] + 
                        normalized[2] * normal[2]
                    );
                    
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    
                    // BRDF = albedo / PI, PDF = 1 / (2*PI) for uniform hemisphere sampling
                    // Combined with cosine term: (albedo / PI) * incoming * cosTheta / (1 / (2*PI))
                    // Simplifies to: albedo * incoming * cosTheta * 2
                    const scale = 2.0 * cosTheta;
                    
                    return [
                        attenuation[0] * incoming[0] * scale,
                        attenuation[1] * incoming[1] * scale,
                        attenuation[2] * incoming[2] * scale
                    ];
                }
            }
            
            self.onmessage = function(e) {
                const { bucket, camera, objects, samplesPerPixel, maxBounces, width, height } = e.data;
                
                const data = new Float32Array(bucket.width * bucket.height * 3);
                
                for (let y = 0; y < bucket.height; y++) {
                    for (let x = 0; x < bucket.width; x++) {
                        const screenX = bucket.x + x;
                        const screenY = bucket.y + y;
                        
                        let color = [0, 0, 0];
                        
                        for (let s = 0; s < samplesPerPixel; s++) {
                            const u = (screenX + random()) / width;
                            const v = (screenY + random()) / height;
                            
                            const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                            const py = -(v * 2 - 1) * camera.tanFov;
                            
                            let dir = [px, py, -1];
                            const len = Math.sqrt(dir[0]*dir[0] + dir[1]*dir[1] + dir[2]*dir[2]);
                            dir = [dir[0]/len, dir[1]/len, dir[2]/len];
                            
                            // Apply camera rotation
                            const q = camera.quaternion;
                            const rotated = rotateByQuaternion(dir, q);
                            
                            const sample = trace(camera.position, rotated, 0, maxBounces, objects);
                            color[0] += sample[0];
                            color[1] += sample[1];
                            color[2] += sample[2];
                        }
                        
                        const idx = (y * bucket.width + x) * 3;
                        data[idx] = color[0] / samplesPerPixel;
                        data[idx + 1] = color[1] / samplesPerPixel;
                        data[idx + 2] = color[2] / samplesPerPixel;
                    }
                }
                
                self.postMessage({ bucket, data });
            };
            
            function rotateByQuaternion(v, q) {
                const qx = q[0], qy = q[1], qz = q[2], qw = q[3];
                const x = v[0], y = v[1], z = v[2];
                
                const ix = qw * x + qy * z - qz * y;
                const iy = qw * y + qz * x - qx * z;
                const iz = qw * z + qx * y - qy * x;
                const iw = -qx * x - qy * y - qz * z;
                
                return [
                    ix * qw + iw * -qx + iy * -qz - iz * -qy,
                    iy * qw + iw * -qy + iz * -qx - ix * -qz,
                    iz * qw + iw * -qz + ix * -qy - iy * -qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        // Create workers
        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            
            for (let i = 0; i < numCores; i++) {
                const worker = new Worker(workerUrl);
                worker.onmessage = handleWorkerResult;
                worker.idle = true;
                workers.push(worker);
            }
        }

        // Convert Three.js objects to worker-compatible format
        function serializeObjects() {
            const serialized = [];
            
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1);
                    normal.applyQuaternion(mesh.quaternion).normalize();
                    
                    const uAxis = new THREE.Vector3(1, 0, 0);
                    uAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    const vAxis = new THREE.Vector3(0, 1, 0);
                    vAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            
            return serialized;
        }

        // Handle worker results
        function handleWorkerResult(e) {
            const { bucket, data } = e.data;
            
            // Update image data
            for (let y = 0; y < bucket.height; y++) {
                for (let x = 0; x < bucket.width; x++) {
                    const srcIdx = (y * bucket.width + x) * 3;
                    const dstIdx = ((bucket.y + y) * width + (bucket.x + x)) * 4;
                    
                    let r = data[srcIdx];
                    let g = data[srcIdx + 1];
                    let b = data[srcIdx + 2];
                    
                    // Gamma correction
                    r = Math.pow(r, 1/2.2);
                    g = Math.pow(g, 1/2.2);
                    b = Math.pow(b, 1/2.2);
                    
                    imageData.data[dstIdx] = Math.min(255, r * 255);
                    imageData.data[dstIdx + 1] = Math.min(255, g * 255);
                    imageData.data[dstIdx + 2] = Math.min(255, b * 255);
                    imageData.data[dstIdx + 3] = 255;
                }
            }
            
            ctx.putImageData(imageData, 0, 0);
            
            // Mark bucket as completed
            const bucketIndex = buckets.findIndex(b => 
                b.x === bucket.x && b.y === bucket.y && !b.completed
            );
            if (bucketIndex !== -1) {
                buckets[bucketIndex].completed = true;
                bucketsCompleted++;
                document.getElementById('bucketsCompleted').textContent = bucketsCompleted;
                
                // Visualize completed bucket
                if (document.getElementById('showBuckets').checked) {
                    visualizeBucket(bucket);
                }
            }
            
            // Mark worker as idle and assign next bucket
            e.target.idle = true;
            assignNextBucket(e.target);
        }

        // Visualize bucket being rendered
        function visualizeBucket(bucket) {
            const div = document.createElement('div');
            div.className = 'bucket';
            div.style.left = bucket.x + 'px';
            div.style.top = bucket.y + 'px';
            div.style.width = bucket.width + 'px';
            div.style.height = bucket.height + 'px';
            document.getElementById('bucketViz').appendChild(div);
            
            setTimeout(() => div.remove(), 500);
        }

        // Assign next bucket to worker
        function assignNextBucket(worker) {
            if (!isTracing) return;
            
            const nextBucket = buckets.find(b => !b.completed);
            if (!nextBucket) {
                // All buckets completed, start next pass
                if (isTracing) {
                    sampleCount += parseInt(document.getElementById('spp').value);
                    document.getElementById('samples').textContent = sampleCount;
                    startNewPass();
                }
                return;
            }
            
            worker.idle = false;
            
            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };
            
            worker.postMessage({
                bucket: nextBucket,
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerPixel: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width: width,
                height: height
            });
        }

        // Start new rendering pass
        function startNewPass() {
            bucketsCompleted = 0;
            document.getElementById('bucketsCompleted').textContent = '0';
            
            buckets.forEach(b => b.completed = false);
            
            // Keep spiral order, don't shuffle
            
            // Assign buckets to all idle workers
            workers.filter(w => w.idle).forEach(w => assignNextBucket(w));
        }

        // Start rendering
        function startRendering() {
            isTracing = true;
            createBuckets();
            initWorkers();
            
            // Start all workers
            workers.forEach(w => assignNextBucket(w));
        }

        // Stop rendering
        function stopRendering() {
            isTracing = false;
        }

        // Reset
        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);
            sampleCount = 0;
            bucketsCompleted = 0;
            document.getElementById('samples').textContent = '0';
            document.getElementById('bucketsCompleted').textContent = '0';
            document.getElementById('bucketViz').innerHTML = '';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (bucketsCompleted === 0) {
                    startRendering();
                } else {
                    isTracing = true;
                    startNewPass();
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });

        document.getElementById('reset').addEventListener('click', resetRendering);

        // =============================================
        // Animation Loop
        // =============================================
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### suelo

```html
<!DOCTYPE html>
<html>
<head>
    <title>Multi-Core Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 250px;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
        .bucket { 
            position: absolute; 
            border: 1px solid rgba(255,255,0,0.5); 
            pointer-events: none;
        }
        #bucketViz { position: absolute; top: 0; left: 0; pointer-events: none; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="bucketViz"></div>
    <div id="controls">
        <div><strong>Multi-Core Path Tracer</strong></div>
        <div>Cores: <span id="cores">0</span></div>
        <div>Samples: <span id="samples">0</span></div>
        <div>Buckets Completed: <span id="bucketsCompleted">0</span>/<span id="bucketsTotal">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <div style="margin-top: 10px;">
            <label>Samples/Bucket: <input type="number" id="spp" value="16" min="1" max="100"></label>
        </div>
        <div>
            <label>Max Bounces: <input type="number" id="bounces" value="4" min="1" max="8"></label>
        </div>
        <div>
            <label><input type="checkbox" id="showBuckets" checked> Show Buckets</label>
        </div>
        <div style="margin-top: 5px; font-size: 11px; color: #aaa;">
            Bucket size: <span id="bucketSize">64x64</span>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];

        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ 
                mesh, 
                type, 
                color, 
                emission,
                // Pre-compute world matrix
                worldMatrix: mesh.matrixWorld.clone()
            });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.95, 0.95, 0.95]);

        // Floor (white)
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = Math.PI / 2;
        addObject(floor, 'diffuse', [0.95, 0.95, 0.95]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.95, 0.95, 0.95]);

        // Light (area light) - much brighter
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        controls.update();

        // Update world matrices
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(obj => {
            obj.worldMatrix = obj.mesh.matrixWorld.clone();
        });

        // =============================================
        // Multi-Core Bucket Rendering System
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const BUCKET_SIZE = 64;
        const numCores = navigator.hardwareConcurrency || 4;
        document.getElementById('cores').textContent = numCores;

        let workers = [];
        let buckets = [];
        let bucketsCompleted = 0;
        let isTracing = false;
        let sampleCount = 0;
        let imageData = ctx.createImageData(width, height);

        // Create bucket list in spiral order from center
        function createBuckets() {
            buckets = [];
            const cols = Math.ceil(width / BUCKET_SIZE);
            const rows = Math.ceil(height / BUCKET_SIZE);
            
            const allBuckets = [];
            for (let y = 0; y < rows; y++) {
                for (let x = 0; x < cols; x++) {
                    allBuckets.push({
                        x: x * BUCKET_SIZE,
                        y: y * BUCKET_SIZE,
                        width: Math.min(BUCKET_SIZE, width - x * BUCKET_SIZE),
                        height: Math.min(BUCKET_SIZE, height - y * BUCKET_SIZE),
                        completed: false,
                        gridX: x,
                        gridY: y
                    });
                }
            }
            
            // Sort buckets in spiral order from center
            const centerX = cols / 2;
            const centerY = rows / 2;
            
            allBuckets.sort((a, b) => {
                const distA = Math.sqrt(Math.pow(a.gridX - centerX, 2) + Math.pow(a.gridY - centerY, 2));
                const distB = Math.sqrt(Math.pow(b.gridX - centerX, 2) + Math.pow(b.gridY - centerY, 2));
                
                if (Math.abs(distA - distB) < 0.5) {
                    // Same distance ring, sort by angle for spiral effect
                    const angleA = Math.atan2(a.gridY - centerY, a.gridX - centerX);
                    const angleB = Math.atan2(b.gridY - centerY, b.gridX - centerX);
                    return angleA - angleB;
                }
                
                return distA - distB;
            });
            
            buckets = allBuckets;
            
            document.getElementById('bucketsTotal').textContent = buckets.length;
            document.getElementById('bucketSize').textContent = `${BUCKET_SIZE}x${BUCKET_SIZE}`;
        }

        // Worker code as a blob
        const workerCode = `
            const raycaster = {};
            
            function intersectRay(origin, direction, objects) {
                let closest = null;
                let minDist = Infinity;
                
                for (const obj of objects) {
                    const result = intersectObject(origin, direction, obj);
                    if (result && result.distance < minDist) {
                        minDist = result.distance;
                        closest = result;
                        closest.object = obj;
                    }
                }
                
                return closest;
            }
            
            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') {
                    return intersectSphere(origin, direction, obj);
                } else if (obj.geometry === 'plane') {
                    return intersectPlane(origin, direction, obj);
                }
                return null;
            }
            
            function intersectSphere(origin, direction, obj) {
                const center = obj.position;
                const radius = obj.radius;
                const oc = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - radius*radius;
                const discriminant = b*b - 4*a*c;
                
                if (discriminant < 0) return null;
                
                const t = (-b - Math.sqrt(discriminant)) / (2*a);
                if (t < 0.001) return null;
                
                const point = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const normal = [
                    (point[0] - center[0]) / radius,
                    (point[1] - center[1]) / radius,
                    (point[2] - center[2]) / radius
                ];
                
                return { distance: t, point, normal };
            }
            
            function intersectPlane(origin, direction, obj) {
                const normal = obj.normal;
                const point = obj.position;
                
                const denom = normal[0]*direction[0] + normal[1]*direction[1] + normal[2]*direction[2];
                if (Math.abs(denom) < 0.0001) return null;
                
                const diff = [point[0] - origin[0], point[1] - origin[1], point[2] - origin[2]];
                const t = (diff[0]*normal[0] + diff[1]*normal[1] + diff[2]*normal[2]) / denom;
                
                if (t < 0.001) return null;
                
                const hitPoint = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                // Check if hit point is within plane bounds
                const localPoint = [
                    hitPoint[0] - point[0],
                    hitPoint[1] - point[1],
                    hitPoint[2] - point[2]
                ];
                
                const size = obj.size;
                const u = obj.uAxis;
                const v = obj.vAxis;
                
                const uCoord = localPoint[0]*u[0] + localPoint[1]*u[1] + localPoint[2]*u[2];
                const vCoord = localPoint[0]*v[0] + localPoint[1]*v[1] + localPoint[2]*v[2];
                
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;
                
                return { distance: t, point: hitPoint, normal };
            }
            
            function random() {
                return Math.random();
            }
            
            function randomInUnitSphere() {
                while (true) {
                    const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                    if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
                }
            }
            
            function randomInHemisphere(normal) {
                const v = randomInUnitSphere();
                const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
                if (dot > 0) return v;
                return [-v[0], -v[1], -v[2]];
            }
            
            function reflect(v, n) {
                const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
                return [v[0] - 2*dot*n[0], v[1] - 2*dot*n[1], v[2] - 2*dot*n[2]];
            }
            
            function normalize(v) {
                const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
                return len > 0 ? [v[0]/len, v[1]/len, v[2]/len] : v;
            }
            
            function trace(origin, direction, depth, maxDepth, objects) {
                if (depth >= maxDepth) return [0, 0, 0];
                
                const hit = intersectRay(origin, direction, objects);
                if (!hit) return [0, 0, 0]; // Black background, no ambient light
                
                const obj = hit.object;
                const hitPoint = hit.point;
                const normal = hit.normal;
                
                const offset = 0.001;
                const offsetPoint = [
                    hitPoint[0] + normal[0] * offset,
                    hitPoint[1] + normal[1] * offset,
                    hitPoint[2] + normal[2] * offset
                ];
                
                // If we hit a light source, return its emission
                if (obj.type === 'emissive') {
                    return obj.emission;
                }
                
                // For diffuse surfaces, use proper BRDF with cosine weighting
                const attenuation = obj.color;
                
                if (obj.type === 'reflective') {
                    // Perfect specular reflection
                    const newDir = reflect(direction, normal);
                    const normalized = normalize(newDir);
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    return [
                        attenuation[0] * incoming[0],
                        attenuation[1] * incoming[1],
                        attenuation[2] * incoming[2]
                    ];
                } else {
                    // Diffuse reflection with proper importance sampling
                    const newDir = randomInHemisphere(normal);
                    const normalized = normalize(newDir);
                    
                    // Cosine term (Lambert's law)
                    const cosTheta = Math.max(0, 
                        normalized[0] * normal[0] + 
                        normalized[1] * normal[1] + 
                        normalized[2] * normal[2]
                    );
                    
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    
                    // BRDF = albedo / PI, PDF = 1 / (2*PI) for uniform hemisphere sampling
                    // Combined with cosine term: (albedo / PI) * incoming * cosTheta / (1 / (2*PI))
                    // Simplifies to: albedo * incoming * cosTheta * 2
                    const scale = 2.0 * cosTheta;
                    
                    return [
                        attenuation[0] * incoming[0] * scale,
                        attenuation[1] * incoming[1] * scale,
                        attenuation[2] * incoming[2] * scale
                    ];
                }
            }
            
            self.onmessage = function(e) {
                const { bucket, camera, objects, samplesPerPixel, maxBounces, width, height } = e.data;
                
                const data = new Float32Array(bucket.width * bucket.height * 3);
                
                for (let y = 0; y < bucket.height; y++) {
                    for (let x = 0; x < bucket.width; x++) {
                        const screenX = bucket.x + x;
                        const screenY = bucket.y + y;
                        
                        let color = [0, 0, 0];
                        
                        for (let s = 0; s < samplesPerPixel; s++) {
                            const u = (screenX + random()) / width;
                            const v = (screenY + random()) / height;
                            
                            const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                            const py = -(v * 2 - 1) * camera.tanFov;
                            
                            let dir = [px, py, -1];
                            const len = Math.sqrt(dir[0]*dir[0] + dir[1]*dir[1] + dir[2]*dir[2]);
                            dir = [dir[0]/len, dir[1]/len, dir[2]/len];
                            
                            // Apply camera rotation
                            const q = camera.quaternion;
                            const rotated = rotateByQuaternion(dir, q);
                            
                            const sample = trace(camera.position, rotated, 0, maxBounces, objects);
                            color[0] += sample[0];
                            color[1] += sample[1];
                            color[2] += sample[2];
                        }
                        
                        const idx = (y * bucket.width + x) * 3;
                        data[idx] = color[0] / samplesPerPixel;
                        data[idx + 1] = color[1] / samplesPerPixel;
                        data[idx + 2] = color[2] / samplesPerPixel;
                    }
                }
                
                self.postMessage({ bucket, data });
            };
            
            function rotateByQuaternion(v, q) {
                const qx = q[0], qy = q[1], qz = q[2], qw = q[3];
                const x = v[0], y = v[1], z = v[2];
                
                const ix = qw * x + qy * z - qz * y;
                const iy = qw * y + qz * x - qx * z;
                const iz = qw * z + qx * y - qy * x;
                const iw = -qx * x - qy * y - qz * z;
                
                return [
                    ix * qw + iw * -qx + iy * -qz - iz * -qy,
                    iy * qw + iw * -qy + iz * -qx - ix * -qz,
                    iz * qw + iw * -qz + ix * -qy - iy * -qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        // Create workers
        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            
            for (let i = 0; i < numCores; i++) {
                const worker = new Worker(workerUrl);
                worker.onmessage = handleWorkerResult;
                worker.idle = true;
                workers.push(worker);
            }
        }

        // Convert Three.js objects to worker-compatible format
        function serializeObjects() {
            const serialized = [];
            
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1);
                    normal.applyQuaternion(mesh.quaternion).normalize();
                    
                    const uAxis = new THREE.Vector3(1, 0, 0);
                    uAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    const vAxis = new THREE.Vector3(0, 1, 0);
                    vAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            
            return serialized;
        }

        // Handle worker results
        function handleWorkerResult(e) {
            const { bucket, data } = e.data;
            
            // Update image data
            for (let y = 0; y < bucket.height; y++) {
                for (let x = 0; x < bucket.width; x++) {
                    const srcIdx = (y * bucket.width + x) * 3;
                    const dstIdx = ((bucket.y + y) * width + (bucket.x + x)) * 4;
                    
                    let r = data[srcIdx];
                    let g = data[srcIdx + 1];
                    let b = data[srcIdx + 2];
                    
                    // Gamma correction
                    r = Math.pow(r, 1/2.2);
                    g = Math.pow(g, 1/2.2);
                    b = Math.pow(b, 1/2.2);
                    
                    imageData.data[dstIdx] = Math.min(255, r * 255);
                    imageData.data[dstIdx + 1] = Math.min(255, g * 255);
                    imageData.data[dstIdx + 2] = Math.min(255, b * 255);
                    imageData.data[dstIdx + 3] = 255;
                }
            }
            
            ctx.putImageData(imageData, 0, 0);
            
            // Mark bucket as completed
            const bucketIndex = buckets.findIndex(b => 
                b.x === bucket.x && b.y === bucket.y && !b.completed
            );
            if (bucketIndex !== -1) {
                buckets[bucketIndex].completed = true;
                bucketsCompleted++;
                document.getElementById('bucketsCompleted').textContent = bucketsCompleted;
                
                // Visualize completed bucket
                if (document.getElementById('showBuckets').checked) {
                    visualizeBucket(bucket);
                }
            }
            
            // Mark worker as idle and assign next bucket
            e.target.idle = true;
            assignNextBucket(e.target);
        }

        // Visualize bucket being rendered
        function visualizeBucket(bucket) {
            const div = document.createElement('div');
            div.className = 'bucket';
            div.style.left = bucket.x + 'px';
            div.style.top = bucket.y + 'px';
            div.style.width = bucket.width + 'px';
            div.style.height = bucket.height + 'px';
            document.getElementById('bucketViz').appendChild(div);
            
            setTimeout(() => div.remove(), 500);
        }

        // Assign next bucket to worker
        function assignNextBucket(worker) {
            if (!isTracing) return;
            
            const nextBucket = buckets.find(b => !b.completed);
            if (!nextBucket) {
                // All buckets completed, start next pass
                if (isTracing) {
                    sampleCount += parseInt(document.getElementById('spp').value);
                    document.getElementById('samples').textContent = sampleCount;
                    startNewPass();
                }
                return;
            }
            
            worker.idle = false;
            
            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };
            
            worker.postMessage({
                bucket: nextBucket,
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerPixel: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width: width,
                height: height
            });
        }

        // Start new rendering pass
        function startNewPass() {
            bucketsCompleted = 0;
            document.getElementById('bucketsCompleted').textContent = '0';
            
            buckets.forEach(b => b.completed = false);
            
            // Keep spiral order, don't shuffle
            
            // Assign buckets to all idle workers
            workers.filter(w => w.idle).forEach(w => assignNextBucket(w));
        }

        // Start rendering
        function startRendering() {
            isTracing = true;
            createBuckets();
            initWorkers();
            
            // Start all workers
            workers.forEach(w => assignNextBucket(w));
        }

        // Stop rendering
        function stopRendering() {
            isTracing = false;
        }

        // Reset
        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);
            sampleCount = 0;
            bucketsCompleted = 0;
            document.getElementById('samples').textContent = '0';
            document.getElementById('bucketsCompleted').textContent = '0';
            document.getElementById('bucketViz').innerHTML = '';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (bucketsCompleted === 0) {
                    startRendering();
                } else {
                    isTracing = true;
                    startNewPass();
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });

        document.getElementById('reset').addEventListener('click', resetRendering);

        // =============================================
        // Animation Loop
        // =============================================
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### suelo2

```html
<!DOCTYPE html>
<html>
<head>
    <title>Multi-Core Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 250px;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
        .bucket { 
            position: absolute; 
            border: 1px solid rgba(255,255,0,0.5); 
            pointer-events: none;
        }
        #bucketViz { position: absolute; top: 0; left: 0; pointer-events: none; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="bucketViz"></div>
    <div id="controls">
        <div><strong>Multi-Core Path Tracer</strong></div>
        <div>Cores: <span id="cores">0</span></div>
        <div>Samples: <span id="samples">0</span></div>
        <div>Buckets Completed: <span id="bucketsCompleted">0</span>/<span id="bucketsTotal">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <div style="margin-top: 10px;">
            <label>Samples/Bucket: <input type="number" id="spp" value="16" min="1" max="100"></label>
        </div>
        <div>
            <label>Max Bounces: <input type="number" id="bounces" value="4" min="1" max="8"></label>
        </div>
        <div>
            <label><input type="checkbox" id="showBuckets" checked> Show Buckets</label>
        </div>
        <div style="margin-top: 5px; font-size: 11px; color: #aaa;">
            Bucket size: <span id="bucketSize">64x64</span>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];

        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ 
                mesh, 
                type, 
                color, 
                emission,
                // Pre-compute world matrix
                worldMatrix: mesh.matrixWorld.clone()
            });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.95, 0.95, 0.95]);

        // Floor (white) - facing up
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = -Math.PI / 2; // Changed to face upward
        addObject(floor, 'diffuse', [0.95, 0.95, 0.95]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.95, 0.95, 0.95]);

        // Light (area light) - much brighter
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        controls.update();

        // Update world matrices
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(obj => {
            obj.worldMatrix = obj.mesh.matrixWorld.clone();
        });

        // =============================================
        // Multi-Core Bucket Rendering System
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const BUCKET_SIZE = 64;
        const numCores = navigator.hardwareConcurrency || 4;
        document.getElementById('cores').textContent = numCores;

        let workers = [];
        let buckets = [];
        let bucketsCompleted = 0;
        let isTracing = false;
        let sampleCount = 0;
        let imageData = ctx.createImageData(width, height);

        // Create bucket list in spiral order from center
        function createBuckets() {
            buckets = [];
            const cols = Math.ceil(width / BUCKET_SIZE);
            const rows = Math.ceil(height / BUCKET_SIZE);
            
            const allBuckets = [];
            for (let y = 0; y < rows; y++) {
                for (let x = 0; x < cols; x++) {
                    allBuckets.push({
                        x: x * BUCKET_SIZE,
                        y: y * BUCKET_SIZE,
                        width: Math.min(BUCKET_SIZE, width - x * BUCKET_SIZE),
                        height: Math.min(BUCKET_SIZE, height - y * BUCKET_SIZE),
                        completed: false,
                        gridX: x,
                        gridY: y
                    });
                }
            }
            
            // Sort buckets in spiral order from center
            const centerX = cols / 2;
            const centerY = rows / 2;
            
            allBuckets.sort((a, b) => {
                const distA = Math.sqrt(Math.pow(a.gridX - centerX, 2) + Math.pow(a.gridY - centerY, 2));
                const distB = Math.sqrt(Math.pow(b.gridX - centerX, 2) + Math.pow(b.gridY - centerY, 2));
                
                if (Math.abs(distA - distB) < 0.5) {
                    // Same distance ring, sort by angle for spiral effect
                    const angleA = Math.atan2(a.gridY - centerY, a.gridX - centerX);
                    const angleB = Math.atan2(b.gridY - centerY, b.gridX - centerX);
                    return angleA - angleB;
                }
                
                return distA - distB;
            });
            
            buckets = allBuckets;
            
            document.getElementById('bucketsTotal').textContent = buckets.length;
            document.getElementById('bucketSize').textContent = `${BUCKET_SIZE}x${BUCKET_SIZE}`;
        }

        // Worker code as a blob
        const workerCode = `
            const raycaster = {};
            
            function intersectRay(origin, direction, objects) {
                let closest = null;
                let minDist = Infinity;
                
                for (const obj of objects) {
                    const result = intersectObject(origin, direction, obj);
                    if (result && result.distance < minDist) {
                        minDist = result.distance;
                        closest = result;
                        closest.object = obj;
                    }
                }
                
                return closest;
            }
            
            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') {
                    return intersectSphere(origin, direction, obj);
                } else if (obj.geometry === 'plane') {
                    return intersectPlane(origin, direction, obj);
                }
                return null;
            }
            
            function intersectSphere(origin, direction, obj) {
                const center = obj.position;
                const radius = obj.radius;
                const oc = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - radius*radius;
                const discriminant = b*b - 4*a*c;
                
                if (discriminant < 0) return null;
                
                const t = (-b - Math.sqrt(discriminant)) / (2*a);
                if (t < 0.001) return null;
                
                const point = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const normal = [
                    (point[0] - center[0]) / radius,
                    (point[1] - center[1]) / radius,
                    (point[2] - center[2]) / radius
                ];
                
                return { distance: t, point, normal };
            }
            
            function intersectPlane(origin, direction, obj) {
                const normal = obj.normal;
                const point = obj.position;
                
                const denom = normal[0]*direction[0] + normal[1]*direction[1] + normal[2]*direction[2];
                if (Math.abs(denom) < 0.0001) return null;
                
                const diff = [point[0] - origin[0], point[1] - origin[1], point[2] - origin[2]];
                const t = (diff[0]*normal[0] + diff[1]*normal[1] + diff[2]*normal[2]) / denom;
                
                if (t < 0.001) return null;
                
                const hitPoint = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                // Check if hit point is within plane bounds
                const localPoint = [
                    hitPoint[0] - point[0],
                    hitPoint[1] - point[1],
                    hitPoint[2] - point[2]
                ];
                
                const size = obj.size;
                const u = obj.uAxis;
                const v = obj.vAxis;
                
                const uCoord = localPoint[0]*u[0] + localPoint[1]*u[1] + localPoint[2]*u[2];
                const vCoord = localPoint[0]*v[0] + localPoint[1]*v[1] + localPoint[2]*v[2];
                
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;
                
                // Make sure normal faces the ray (double-sided behavior)
                let finalNormal = normal;
                if (denom > 0) {
                    finalNormal = [-normal[0], -normal[1], -normal[2]];
                }
                
                return { distance: t, point: hitPoint, normal: finalNormal };
            }
            
            function random() {
                return Math.random();
            }
            
            function randomInUnitSphere() {
                while (true) {
                    const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                    if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
                }
            }
            
            function randomInHemisphere(normal) {
                const v = randomInUnitSphere();
                const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
                if (dot > 0) return v;
                return [-v[0], -v[1], -v[2]];
            }
            
            function reflect(v, n) {
                const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
                return [v[0] - 2*dot*n[0], v[1] - 2*dot*n[1], v[2] - 2*dot*n[2]];
            }
            
            function normalize(v) {
                const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
                return len > 0 ? [v[0]/len, v[1]/len, v[2]/len] : v;
            }
            
            function trace(origin, direction, depth, maxDepth, objects) {
                if (depth >= maxDepth) return [0, 0, 0];
                
                const hit = intersectRay(origin, direction, objects);
                if (!hit) return [0, 0, 0]; // Black background, no ambient light
                
                const obj = hit.object;
                const hitPoint = hit.point;
                const normal = hit.normal;
                
                const offset = 0.001;
                const offsetPoint = [
                    hitPoint[0] + normal[0] * offset,
                    hitPoint[1] + normal[1] * offset,
                    hitPoint[2] + normal[2] * offset
                ];
                
                // If we hit a light source, return its emission
                if (obj.type === 'emissive') {
                    return obj.emission;
                }
                
                // For diffuse surfaces, use proper BRDF with cosine weighting
                const attenuation = obj.color;
                
                if (obj.type === 'reflective') {
                    // Perfect specular reflection
                    const newDir = reflect(direction, normal);
                    const normalized = normalize(newDir);
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    return [
                        attenuation[0] * incoming[0],
                        attenuation[1] * incoming[1],
                        attenuation[2] * incoming[2]
                    ];
                } else {
                    // Diffuse reflection with proper importance sampling
                    const newDir = randomInHemisphere(normal);
                    const normalized = normalize(newDir);
                    
                    // Cosine term (Lambert's law)
                    const cosTheta = Math.max(0, 
                        normalized[0] * normal[0] + 
                        normalized[1] * normal[1] + 
                        normalized[2] * normal[2]
                    );
                    
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    
                    // BRDF = albedo / PI, PDF = 1 / (2*PI) for uniform hemisphere sampling
                    // Combined with cosine term: (albedo / PI) * incoming * cosTheta / (1 / (2*PI))
                    // Simplifies to: albedo * incoming * cosTheta * 2
                    const scale = 2.0 * cosTheta;
                    
                    return [
                        attenuation[0] * incoming[0] * scale,
                        attenuation[1] * incoming[1] * scale,
                        attenuation[2] * incoming[2] * scale
                    ];
                }
            }
            
            self.onmessage = function(e) {
                const { bucket, camera, objects, samplesPerPixel, maxBounces, width, height } = e.data;
                
                const data = new Float32Array(bucket.width * bucket.height * 3);
                
                for (let y = 0; y < bucket.height; y++) {
                    for (let x = 0; x < bucket.width; x++) {
                        const screenX = bucket.x + x;
                        const screenY = bucket.y + y;
                        
                        let color = [0, 0, 0];
                        
                        for (let s = 0; s < samplesPerPixel; s++) {
                            const u = (screenX + random()) / width;
                            const v = (screenY + random()) / height;
                            
                            const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                            const py = -(v * 2 - 1) * camera.tanFov;
                            
                            let dir = [px, py, -1];
                            const len = Math.sqrt(dir[0]*dir[0] + dir[1]*dir[1] + dir[2]*dir[2]);
                            dir = [dir[0]/len, dir[1]/len, dir[2]/len];
                            
                            // Apply camera rotation
                            const q = camera.quaternion;
                            const rotated = rotateByQuaternion(dir, q);
                            
                            const sample = trace(camera.position, rotated, 0, maxBounces, objects);
                            color[0] += sample[0];
                            color[1] += sample[1];
                            color[2] += sample[2];
                        }
                        
                        const idx = (y * bucket.width + x) * 3;
                        data[idx] = color[0] / samplesPerPixel;
                        data[idx + 1] = color[1] / samplesPerPixel;
                        data[idx + 2] = color[2] / samplesPerPixel;
                    }
                }
                
                self.postMessage({ bucket, data });
            };
            
            function rotateByQuaternion(v, q) {
                const qx = q[0], qy = q[1], qz = q[2], qw = q[3];
                const x = v[0], y = v[1], z = v[2];
                
                const ix = qw * x + qy * z - qz * y;
                const iy = qw * y + qz * x - qx * z;
                const iz = qw * z + qx * y - qy * x;
                const iw = -qx * x - qy * y - qz * z;
                
                return [
                    ix * qw + iw * -qx + iy * -qz - iz * -qy,
                    iy * qw + iw * -qy + iz * -qx - ix * -qz,
                    iz * qw + iw * -qz + ix * -qy - iy * -qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        // Create workers
        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            
            for (let i = 0; i < numCores; i++) {
                const worker = new Worker(workerUrl);
                worker.onmessage = handleWorkerResult;
                worker.idle = true;
                workers.push(worker);
            }
        }

        // Convert Three.js objects to worker-compatible format
        function serializeObjects() {
            const serialized = [];
            
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1);
                    normal.applyQuaternion(mesh.quaternion).normalize();
                    
                    const uAxis = new THREE.Vector3(1, 0, 0);
                    uAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    const vAxis = new THREE.Vector3(0, 1, 0);
                    vAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            
            return serialized;
        }

        // Handle worker results
        function handleWorkerResult(e) {
            const { bucket, data } = e.data;
            
            // Update image data
            for (let y = 0; y < bucket.height; y++) {
                for (let x = 0; x < bucket.width; x++) {
                    const srcIdx = (y * bucket.width + x) * 3;
                    const dstIdx = ((bucket.y + y) * width + (bucket.x + x)) * 4;
                    
                    let r = data[srcIdx];
                    let g = data[srcIdx + 1];
                    let b = data[srcIdx + 2];
                    
                    // Gamma correction
                    r = Math.pow(r, 1/2.2);
                    g = Math.pow(g, 1/2.2);
                    b = Math.pow(b, 1/2.2);
                    
                    imageData.data[dstIdx] = Math.min(255, r * 255);
                    imageData.data[dstIdx + 1] = Math.min(255, g * 255);
                    imageData.data[dstIdx + 2] = Math.min(255, b * 255);
                    imageData.data[dstIdx + 3] = 255;
                }
            }
            
            ctx.putImageData(imageData, 0, 0);
            
            // Mark bucket as completed
            const bucketIndex = buckets.findIndex(b => 
                b.x === bucket.x && b.y === bucket.y && !b.completed
            );
            if (bucketIndex !== -1) {
                buckets[bucketIndex].completed = true;
                bucketsCompleted++;
                document.getElementById('bucketsCompleted').textContent = bucketsCompleted;
                
                // Visualize completed bucket
                if (document.getElementById('showBuckets').checked) {
                    visualizeBucket(bucket);
                }
            }
            
            // Mark worker as idle and assign next bucket
            e.target.idle = true;
            assignNextBucket(e.target);
        }

        // Visualize bucket being rendered
        function visualizeBucket(bucket) {
            const div = document.createElement('div');
            div.className = 'bucket';
            div.style.left = bucket.x + 'px';
            div.style.top = bucket.y + 'px';
            div.style.width = bucket.width + 'px';
            div.style.height = bucket.height + 'px';
            document.getElementById('bucketViz').appendChild(div);
            
            setTimeout(() => div.remove(), 500);
        }

        // Assign next bucket to worker
        function assignNextBucket(worker) {
            if (!isTracing) return;
            
            const nextBucket = buckets.find(b => !b.completed);
            if (!nextBucket) {
                // All buckets completed, start next pass
                if (isTracing) {
                    sampleCount += parseInt(document.getElementById('spp').value);
                    document.getElementById('samples').textContent = sampleCount;
                    startNewPass();
                }
                return;
            }
            
            worker.idle = false;
            
            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };
            
            worker.postMessage({
                bucket: nextBucket,
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerPixel: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width: width,
                height: height
            });
        }

        // Start new rendering pass
        function startNewPass() {
            bucketsCompleted = 0;
            document.getElementById('bucketsCompleted').textContent = '0';
            
            buckets.forEach(b => b.completed = false);
            
            // Keep spiral order, don't shuffle
            
            // Assign buckets to all idle workers
            workers.filter(w => w.idle).forEach(w => assignNextBucket(w));
        }

        // Start rendering
        function startRendering() {
            isTracing = true;
            createBuckets();
            initWorkers();
            
            // Start all workers
            workers.forEach(w => assignNextBucket(w));
        }

        // Stop rendering
        function stopRendering() {
            isTracing = false;
        }

        // Reset
        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);
            sampleCount = 0;
            bucketsCompleted = 0;
            document.getElementById('samples').textContent = '0';
            document.getElementById('bucketsCompleted').textContent = '0';
            document.getElementById('bucketViz').innerHTML = '';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (bucketsCompleted === 0) {
                    startRendering();
                } else {
                    isTracing = true;
                    startNewPass();
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });

        document.getElementById('reset').addEventListener('click', resetRendering);

        // =============================================
        // Animation Loop
        // =============================================
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### montecarlo

```html
<!DOCTYPE html>
<html>
<head>
    <title>Monte Carlo Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 250px;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="controls">
        <div><strong>Monte Carlo Path Tracer</strong></div>
        <div>Cores Used: <span id="cores">0</span> / <span id="totalCores">0</span></div>
        <div>Total Samples: <span id="samples">0</span></div>
        <div>Samples/sec: <span id="sps">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <div style="margin-top: 10px;">
            <label>Samples/Frame: <input type="number" id="spp" value="1000" min="100" max="10000"></label>
        </div>
        <div>
            <label>Max Bounces: <input type="number" id="bounces" value="5" min="1" max="10"></label>
        </div>
        <div style="margin-top: 5px; font-size: 11px; color: #aaa;">
            Monte Carlo progressive refinement
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];

        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ 
                mesh, 
                type, 
                color, 
                emission,
                worldMatrix: mesh.matrixWorld.clone()
            });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.95, 0.95, 0.95]);

        // Floor (white) - facing up
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = -Math.PI / 2;
        addObject(floor, 'diffuse', [0.95, 0.95, 0.95]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.95, 0.95, 0.95]);

        // Light (area light) - much brighter
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        controls.update();

        // Update world matrices
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(obj => {
            obj.worldMatrix = obj.mesh.matrixWorld.clone();
        });

        // =============================================
        // Monte Carlo Progressive Path Tracer
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const totalCores = navigator.hardwareConcurrency || 4;
        const numCores = Math.max(1, Math.floor(totalCores / 2));
        document.getElementById('cores').textContent = numCores;
        document.getElementById('totalCores').textContent = totalCores;

        let workers = [];
        let isTracing = false;
        let totalSamples = 0;
        let accumBuffer = new Float32Array(width * height * 3);
        let imageData = ctx.createImageData(width, height);
        let lastSampleCount = 0;
        let lastTime = Date.now();

        // Worker code for Monte Carlo sampling
        const workerCode = `
            const raycaster = {};
            
            function intersectRay(origin, direction, objects) {
                let closest = null;
                let minDist = Infinity;
                
                for (const obj of objects) {
                    const result = intersectObject(origin, direction, obj);
                    if (result && result.distance < minDist) {
                        minDist = result.distance;
                        closest = result;
                        closest.object = obj;
                    }
                }
                
                return closest;
            }
            
            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') {
                    return intersectSphere(origin, direction, obj);
                } else if (obj.geometry === 'plane') {
                    return intersectPlane(origin, direction, obj);
                }
                return null;
            }
            
            function intersectSphere(origin, direction, obj) {
                const center = obj.position;
                const radius = obj.radius;
                const oc = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - radius*radius;
                const discriminant = b*b - 4*a*c;
                
                if (discriminant < 0) return null;
                
                const t = (-b - Math.sqrt(discriminant)) / (2*a);
                if (t < 0.001) return null;
                
                const point = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const normal = [
                    (point[0] - center[0]) / radius,
                    (point[1] - center[1]) / radius,
                    (point[2] - center[2]) / radius
                ];
                
                return { distance: t, point, normal };
            }
            
            function intersectPlane(origin, direction, obj) {
                const normal = obj.normal;
                const point = obj.position;
                
                const denom = normal[0]*direction[0] + normal[1]*direction[1] + normal[2]*direction[2];
                if (Math.abs(denom) < 0.0001) return null;
                
                const diff = [point[0] - origin[0], point[1] - origin[1], point[2] - origin[2]];
                const t = (diff[0]*normal[0] + diff[1]*normal[1] + diff[2]*normal[2]) / denom;
                
                if (t < 0.001) return null;
                
                const hitPoint = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const localPoint = [
                    hitPoint[0] - point[0],
                    hitPoint[1] - point[1],
                    hitPoint[2] - point[2]
                ];
                
                const size = obj.size;
                const u = obj.uAxis;
                const v = obj.vAxis;
                
                const uCoord = localPoint[0]*u[0] + localPoint[1]*u[1] + localPoint[2]*u[2];
                const vCoord = localPoint[0]*v[0] + localPoint[1]*v[1] + localPoint[2]*v[2];
                
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;
                
                let finalNormal = normal;
                if (denom > 0) {
                    finalNormal = [-normal[0], -normal[1], -normal[2]];
                }
                
                return { distance: t, point: hitPoint, normal: finalNormal };
            }
            
            function random() {
                return Math.random();
            }
            
            function randomInUnitSphere() {
                while (true) {
                    const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                    if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
                }
            }
            
            function randomInHemisphere(normal) {
                const v = randomInUnitSphere();
                const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
                if (dot > 0) return v;
                return [-v[0], -v[1], -v[2]];
            }
            
            function reflect(v, n) {
                const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
                return [v[0] - 2*dot*n[0], v[1] - 2*dot*n[1], v[2] - 2*dot*n[2]];
            }
            
            function normalize(v) {
                const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
                return len > 0 ? [v[0]/len, v[1]/len, v[2]/len] : v;
            }
            
            function trace(origin, direction, depth, maxDepth, objects) {
                if (depth >= maxDepth) return [0, 0, 0];
                
                const hit = intersectRay(origin, direction, objects);
                if (!hit) return [0, 0, 0];
                
                const obj = hit.object;
                const hitPoint = hit.point;
                const normal = hit.normal;
                
                const offset = 0.001;
                const offsetPoint = [
                    hitPoint[0] + normal[0] * offset,
                    hitPoint[1] + normal[1] * offset,
                    hitPoint[2] + normal[2] * offset
                ];
                
                if (obj.type === 'emissive') {
                    return obj.emission;
                }
                
                const attenuation = obj.color;
                
                if (obj.type === 'reflective') {
                    const newDir = reflect(direction, normal);
                    const normalized = normalize(newDir);
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    return [
                        attenuation[0] * incoming[0],
                        attenuation[1] * incoming[1],
                        attenuation[2] * incoming[2]
                    ];
                } else {
                    const newDir = randomInHemisphere(normal);
                    const normalized = normalize(newDir);
                    
                    const cosTheta = Math.max(0, 
                        normalized[0] * normal[0] + 
                        normalized[1] * normal[1] + 
                        normalized[2] * normal[2]
                    );
                    
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    const scale = 2.0 * cosTheta;
                    
                    return [
                        attenuation[0] * incoming[0] * scale,
                        attenuation[1] * incoming[1] * scale,
                        attenuation[2] * incoming[2] * scale
                    ];
                }
            }
            
            self.onmessage = function(e) {
                const { camera, objects, samplesPerBatch, maxBounces, width, height } = e.data;
                
                const sampleData = [];
                
                // Monte Carlo: randomly sample pixels across entire image
                for (let s = 0; s < samplesPerBatch; s++) {
                    const x = Math.floor(random() * width);
                    const y = Math.floor(random() * height);
                    
                    const u = (x + random()) / width;
                    const v = (y + random()) / height;
                    
                    const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                    const py = -(v * 2 - 1) * camera.tanFov;
                    
                    let dir = [px, py, -1];
                    const len = Math.sqrt(dir[0]*dir[0] + dir[1]*dir[1] + dir[2]*dir[2]);
                    dir = [dir[0]/len, dir[1]/len, dir[2]/len];
                    
                    const q = camera.quaternion;
                    const rotated = rotateByQuaternion(dir, q);
                    
                    const color = trace(camera.position, rotated, 0, maxBounces, objects);
                    
                    // Store as individual samples
                    sampleData.push({
                        x: x,
                        y: y,
                        color: color
                    });
                }
                
                self.postMessage({ sampleData });
            };
            
            function rotateByQuaternion(v, q) {
                const qx = q[0], qy = q[1], qz = q[2], qw = q[3];
                const x = v[0], y = v[1], z = v[2];
                
                const ix = qw * x + qy * z - qz * y;
                const iy = qw * y + qz * x - qx * z;
                const iz = qw * z + qx * y - qy * x;
                const iw = -qx * x - qy * y - qz * z;
                
                return [
                    ix * qw + iw * -qx + iy * -qz - iz * -qy,
                    iy * qw + iw * -qy + iz * -qx - ix * -qz,
                    iz * qw + iw * -qz + ix * -qy - iy * -qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        // Create workers
        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            
            for (let i = 0; i < numCores; i++) {
                const worker = new Worker(workerUrl);
                worker.onmessage = handleWorkerResult;
                worker.idle = true;
                workers.push(worker);
            }
        }

        // Convert Three.js objects to worker-compatible format
        function serializeObjects() {
            const serialized = [];
            
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1);
                    normal.applyQuaternion(mesh.quaternion).normalize();
                    
                    const uAxis = new THREE.Vector3(1, 0, 0);
                    uAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    const vAxis = new THREE.Vector3(0, 1, 0);
                    vAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            
            return serialized;
        }

        // Sample count per pixel buffer for proper averaging
        let sampleCountPerPixel = new Uint32Array(width * height);

        // Handle worker results
        function handleWorkerResult(e) {
            const { sampleData } = e.data;
            
            // Accumulate samples into buffer
            for (const sample of sampleData) {
                const pixelIdx = sample.y * width + sample.x;
                const idx = pixelIdx * 3;
                accumBuffer[idx] += sample.color[0];
                accumBuffer[idx + 1] += sample.color[1];
                accumBuffer[idx + 2] += sample.color[2];
                sampleCountPerPixel[pixelIdx]++;
            }
            
            totalSamples += sampleData.length;
            
            // Mark worker as idle and continue
            e.target.idle = true;
            if (isTracing) {
                assignWork(e.target);
            }
        }

        // Update display (called periodically)
        function updateDisplay() {
            if (totalSamples === 0) return;
            
            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    const pixelIdx = y * width + x;
                    const idx = pixelIdx * 3;
                    const imgIdx = pixelIdx * 4;
                    
                    const count = sampleCountPerPixel[pixelIdx];
                    if (count === 0) {
                        // No samples yet for this pixel, keep it black
                        imageData.data[imgIdx] = 0;
                        imageData.data[imgIdx + 1] = 0;
                        imageData.data[imgIdx + 2] = 0;
                        imageData.data[imgIdx + 3] = 255;
                        continue;
                    }
                    
                    const scale = 1.0 / count;
                    
                    let r = accumBuffer[idx] * scale;
                    let g = accumBuffer[idx + 1] * scale;
                    let b = accumBuffer[idx + 2] * scale;
                    
                    // Gamma correction
                    r = Math.pow(r, 1/2.2);
                    g = Math.pow(g, 1/2.2);
                    b = Math.pow(b, 1/2.2);
                    
                    imageData.data[imgIdx] = Math.min(255, r * 255);
                    imageData.data[imgIdx + 1] = Math.min(255, g * 255);
                    imageData.data[imgIdx + 2] = Math.min(255, b * 255);
                    imageData.data[imgIdx + 3] = 255;
                }
            }
            
            ctx.putImageData(imageData, 0, 0);
            document.getElementById('samples').textContent = totalSamples;
            
            // Calculate samples per second
            const now = Date.now();
            const elapsed = (now - lastTime) / 1000;
            if (elapsed > 1.0) {
                const sps = Math.floor((totalSamples - lastSampleCount) / elapsed);
                document.getElementById('sps').textContent = sps.toLocaleString();
                lastSampleCount = totalSamples;
                lastTime = now;
            }
        }

        // Assign work to a worker
        function assignWork(worker) {
            if (!isTracing) return;
            
            worker.idle = false;
            
            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };
            
            worker.postMessage({
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerBatch: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width: width,
                height: height
            });
        }

        // Start rendering
        function startRendering() {
            isTracing = true;
            initWorkers();
            lastTime = Date.now();
            lastSampleCount = 0;
            
            // Start all workers
            workers.forEach(w => assignWork(w));
        }

        // Stop rendering
        function stopRendering() {
            isTracing = false;
        }

        // Reset
        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);
            accumBuffer = new Float32Array(width * height * 3);
            sampleCountPerPixel = new Uint32Array(width * height);
            totalSamples = 0;
            lastSampleCount = 0;
            document.getElementById('samples').textContent = '0';
            document.getElementById('sps').textContent = '0';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (totalSamples === 0) {
                    startRendering();
                } else {
                    isTracing = true;
                    workers.filter(w => w.idle).forEach(w => assignWork(w));
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });

        document.getElementById('reset').addEventListener('click', resetRendering);

        // =============================================
        // Animation Loop
        // =============================================
        let frameCount = 0;
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
            
            // Update display every few frames
            if (isTracing && frameCount++ % 2 === 0) {
                updateDisplay();
            }
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### fps

```html
<!DOCTYPE html>
<html>
<head>
    <title>Monte Carlo Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 250px;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="controls">
        <div><strong>Monte Carlo Path Tracer</strong></div>
        <div>Cores Used: <span id="cores">0</span> / <span id="totalCores">0</span></div>
        <div>Total Samples: <span id="samples">0</span></div>
        <div>Samples/sec: <span id="sps">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <div style="margin-top: 10px;">
            <label>Samples/Frame: <input type="number" id="spp" value="1000" min="100" max="10000"></label>
        </div>
        <div>
            <label>Max Bounces: <input type="number" id="bounces" value="5" min="1" max="10"></label>
        </div>
        <div style="margin-top: 5px; font-size: 11px; color: #aaa;">
            Click to enable FPS controls<br>
            WASD: Move | Mouse: Look<br>
            Space: Up | Shift: Down/Sprint<br>
            Motion blur effect enabled
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;
        controls.enabled = false; // Disable orbit controls, we'll use FPS controls

        // =============================================
        // FPS Controls
        // =============================================
        const moveSpeed = 0.05;
        const mouseSensitivity = 0.002;
        const keys = { w: false, a: false, s: false, d: false, shift: false, space: false };
        let pitch = 0;
        let yaw = 0;
        let isPointerLocked = false;

        // Pointer lock
        document.body.addEventListener('click', () => {
            if (!isPointerLocked) {
                document.body.requestPointerLock();
            }
        });

        document.addEventListener('pointerlockchange', () => {
            isPointerLocked = document.pointerLockElement === document.body;
            if (isPointerLocked) {
                console.log('Pointer locked - use WASD to move, mouse to look');
            } else {
                console.log('Pointer unlocked - click to lock again');
            }
        });

        // Mouse movement
        document.addEventListener('mousemove', (e) => {
            if (!isPointerLocked) return;

            yaw -= e.movementX * mouseSensitivity;
            pitch -= e.movementY * mouseSensitivity;
            pitch = Math.max(-Math.PI / 2 + 0.01, Math.min(Math.PI / 2 - 0.01, pitch));

            const euler = new THREE.Euler(pitch, yaw, 0, 'YXZ');
            camera.quaternion.setFromEuler(euler);
        });

        // Keyboard input
        document.addEventListener('keydown', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) {
                keys[key] = true;
                e.preventDefault();
            }
        });

        document.addEventListener('keyup', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) {
                keys[key] = false;
                e.preventDefault();
            }
        });

        // Update camera position
        function updateMovement() {
            const forward = new THREE.Vector3(0, 0, -1);
            forward.applyQuaternion(camera.quaternion);
            forward.y = 0;
            forward.normalize();

            const right = new THREE.Vector3(1, 0, 0);
            right.applyQuaternion(camera.quaternion);
            right.y = 0;
            right.normalize();

            const speed = keys.shift && (keys.w || keys.s || keys.a || keys.d) ? moveSpeed * 2 : moveSpeed;

            if (keys.w) {
                camera.position.addScaledVector(forward, speed);
            }
            if (keys.s) {
                camera.position.addScaledVector(forward, -speed);
            }
            if (keys.d) {
                camera.position.addScaledVector(right, speed);
            }
            if (keys.a) {
                camera.position.addScaledVector(right, -speed);
            }
            if (keys.space) {
                camera.position.y += speed;
            }
            if (keys.shift && !keys.w && !keys.s && !keys.a && !keys.d) {
                camera.position.y -= speed;
            }
        }

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];

        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ 
                mesh, 
                type, 
                color, 
                emission,
                worldMatrix: mesh.matrixWorld.clone()
            });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.95, 0.95, 0.95]);

        // Floor (white) - facing up
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = -Math.PI / 2;
        addObject(floor, 'diffuse', [0.95, 0.95, 0.95]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.95, 0.95, 0.95]);

        // Light (area light) - much brighter
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        pitch = 0;
        yaw = 0;
        camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));

        // Update world matrices
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(obj => {
            obj.worldMatrix = obj.mesh.matrixWorld.clone();
        });

        // =============================================
        // Monte Carlo Progressive Path Tracer
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const totalCores = navigator.hardwareConcurrency || 4;
        const numCores = Math.max(1, Math.floor(totalCores / 2));
        document.getElementById('cores').textContent = numCores;
        document.getElementById('totalCores').textContent = totalCores;

        let workers = [];
        let isTracing = false;
        let totalSamples = 0;
        let accumBuffer = new Float32Array(width * height * 3);
        let imageData = ctx.createImageData(width, height);
        let lastSampleCount = 0;
        let lastTime = Date.now();

        // Worker code for Monte Carlo sampling
        const workerCode = `
            const raycaster = {};
            
            function intersectRay(origin, direction, objects) {
                let closest = null;
                let minDist = Infinity;
                
                for (const obj of objects) {
                    const result = intersectObject(origin, direction, obj);
                    if (result && result.distance < minDist) {
                        minDist = result.distance;
                        closest = result;
                        closest.object = obj;
                    }
                }
                
                return closest;
            }
            
            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') {
                    return intersectSphere(origin, direction, obj);
                } else if (obj.geometry === 'plane') {
                    return intersectPlane(origin, direction, obj);
                }
                return null;
            }
            
            function intersectSphere(origin, direction, obj) {
                const center = obj.position;
                const radius = obj.radius;
                const oc = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - radius*radius;
                const discriminant = b*b - 4*a*c;
                
                if (discriminant < 0) return null;
                
                const t = (-b - Math.sqrt(discriminant)) / (2*a);
                if (t < 0.001) return null;
                
                const point = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const normal = [
                    (point[0] - center[0]) / radius,
                    (point[1] - center[1]) / radius,
                    (point[2] - center[2]) / radius
                ];
                
                return { distance: t, point, normal };
            }
            
            function intersectPlane(origin, direction, obj) {
                const normal = obj.normal;
                const point = obj.position;
                
                const denom = normal[0]*direction[0] + normal[1]*direction[1] + normal[2]*direction[2];
                if (Math.abs(denom) < 0.0001) return null;
                
                const diff = [point[0] - origin[0], point[1] - origin[1], point[2] - origin[2]];
                const t = (diff[0]*normal[0] + diff[1]*normal[1] + diff[2]*normal[2]) / denom;
                
                if (t < 0.001) return null;
                
                const hitPoint = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const localPoint = [
                    hitPoint[0] - point[0],
                    hitPoint[1] - point[1],
                    hitPoint[2] - point[2]
                ];
                
                const size = obj.size;
                const u = obj.uAxis;
                const v = obj.vAxis;
                
                const uCoord = localPoint[0]*u[0] + localPoint[1]*u[1] + localPoint[2]*u[2];
                const vCoord = localPoint[0]*v[0] + localPoint[1]*v[1] + localPoint[2]*v[2];
                
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;
                
                let finalNormal = normal;
                if (denom > 0) {
                    finalNormal = [-normal[0], -normal[1], -normal[2]];
                }
                
                return { distance: t, point: hitPoint, normal: finalNormal };
            }
            
            function random() {
                return Math.random();
            }
            
            function randomInUnitSphere() {
                while (true) {
                    const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                    if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
                }
            }
            
            function randomInHemisphere(normal) {
                const v = randomInUnitSphere();
                const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
                if (dot > 0) return v;
                return [-v[0], -v[1], -v[2]];
            }
            
            function reflect(v, n) {
                const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
                return [v[0] - 2*dot*n[0], v[1] - 2*dot*n[1], v[2] - 2*dot*n[2]];
            }
            
            function normalize(v) {
                const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
                return len > 0 ? [v[0]/len, v[1]/len, v[2]/len] : v;
            }
            
            function trace(origin, direction, depth, maxDepth, objects) {
                if (depth >= maxDepth) return [0, 0, 0];
                
                const hit = intersectRay(origin, direction, objects);
                if (!hit) return [0, 0, 0];
                
                const obj = hit.object;
                const hitPoint = hit.point;
                const normal = hit.normal;
                
                const offset = 0.001;
                const offsetPoint = [
                    hitPoint[0] + normal[0] * offset,
                    hitPoint[1] + normal[1] * offset,
                    hitPoint[2] + normal[2] * offset
                ];
                
                if (obj.type === 'emissive') {
                    return obj.emission;
                }
                
                const attenuation = obj.color;
                
                if (obj.type === 'reflective') {
                    const newDir = reflect(direction, normal);
                    const normalized = normalize(newDir);
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    return [
                        attenuation[0] * incoming[0],
                        attenuation[1] * incoming[1],
                        attenuation[2] * incoming[2]
                    ];
                } else {
                    const newDir = randomInHemisphere(normal);
                    const normalized = normalize(newDir);
                    
                    const cosTheta = Math.max(0, 
                        normalized[0] * normal[0] + 
                        normalized[1] * normal[1] + 
                        normalized[2] * normal[2]
                    );
                    
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    const scale = 2.0 * cosTheta;
                    
                    return [
                        attenuation[0] * incoming[0] * scale,
                        attenuation[1] * incoming[1] * scale,
                        attenuation[2] * incoming[2] * scale
                    ];
                }
            }
            
            self.onmessage = function(e) {
                const { camera, objects, samplesPerBatch, maxBounces, width, height } = e.data;
                
                const sampleData = [];
                
                // Monte Carlo: randomly sample pixels across entire image
                for (let s = 0; s < samplesPerBatch; s++) {
                    const x = Math.floor(random() * width);
                    const y = Math.floor(random() * height);
                    
                    const u = (x + random()) / width;
                    const v = (y + random()) / height;
                    
                    const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                    const py = -(v * 2 - 1) * camera.tanFov;
                    
                    let dir = [px, py, -1];
                    const len = Math.sqrt(dir[0]*dir[0] + dir[1]*dir[1] + dir[2]*dir[2]);
                    dir = [dir[0]/len, dir[1]/len, dir[2]/len];
                    
                    const q = camera.quaternion;
                    const rotated = rotateByQuaternion(dir, q);
                    
                    const color = trace(camera.position, rotated, 0, maxBounces, objects);
                    
                    // Store as individual samples
                    sampleData.push({
                        x: x,
                        y: y,
                        color: color
                    });
                }
                
                self.postMessage({ sampleData });
            };
            
            function rotateByQuaternion(v, q) {
                const qx = q[0], qy = q[1], qz = q[2], qw = q[3];
                const x = v[0], y = v[1], z = v[2];
                
                const ix = qw * x + qy * z - qz * y;
                const iy = qw * y + qz * x - qx * z;
                const iz = qw * z + qx * y - qy * x;
                const iw = -qx * x - qy * y - qz * z;
                
                return [
                    ix * qw + iw * -qx + iy * -qz - iz * -qy,
                    iy * qw + iw * -qy + iz * -qx - ix * -qz,
                    iz * qw + iw * -qz + ix * -qy - iy * -qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        // Create workers
        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            
            for (let i = 0; i < numCores; i++) {
                const worker = new Worker(workerUrl);
                worker.onmessage = handleWorkerResult;
                worker.idle = true;
                workers.push(worker);
            }
        }

        // Convert Three.js objects to worker-compatible format
        function serializeObjects() {
            const serialized = [];
            
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1);
                    normal.applyQuaternion(mesh.quaternion).normalize();
                    
                    const uAxis = new THREE.Vector3(1, 0, 0);
                    uAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    const vAxis = new THREE.Vector3(0, 1, 0);
                    vAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            
            return serialized;
        }

        // Sample count per pixel buffer for proper averaging
        let sampleCountPerPixel = new Uint32Array(width * height);

        // Handle worker results
        function handleWorkerResult(e) {
            const { sampleData } = e.data;
            
            // Accumulate samples into buffer
            for (const sample of sampleData) {
                const pixelIdx = sample.y * width + sample.x;
                const idx = pixelIdx * 3;
                accumBuffer[idx] += sample.color[0];
                accumBuffer[idx + 1] += sample.color[1];
                accumBuffer[idx + 2] += sample.color[2];
                sampleCountPerPixel[pixelIdx]++;
            }
            
            totalSamples += sampleData.length;
            
            // Mark worker as idle and continue
            e.target.idle = true;
            if (isTracing) {
                assignWork(e.target);
            }
        }

        // Update display (called periodically)
        function updateDisplay() {
            if (totalSamples === 0) return;
            
            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    const pixelIdx = y * width + x;
                    const idx = pixelIdx * 3;
                    const imgIdx = pixelIdx * 4;
                    
                    const count = sampleCountPerPixel[pixelIdx];
                    if (count === 0) {
                        // No samples yet for this pixel, keep it black
                        imageData.data[imgIdx] = 0;
                        imageData.data[imgIdx + 1] = 0;
                        imageData.data[imgIdx + 2] = 0;
                        imageData.data[imgIdx + 3] = 255;
                        continue;
                    }
                    
                    const scale = 1.0 / count;
                    
                    let r = accumBuffer[idx] * scale;
                    let g = accumBuffer[idx + 1] * scale;
                    let b = accumBuffer[idx + 2] * scale;
                    
                    // Gamma correction
                    r = Math.pow(r, 1/2.2);
                    g = Math.pow(g, 1/2.2);
                    b = Math.pow(b, 1/2.2);
                    
                    imageData.data[imgIdx] = Math.min(255, r * 255);
                    imageData.data[imgIdx + 1] = Math.min(255, g * 255);
                    imageData.data[imgIdx + 2] = Math.min(255, b * 255);
                    imageData.data[imgIdx + 3] = 255;
                }
            }
            
            ctx.putImageData(imageData, 0, 0);
            document.getElementById('samples').textContent = totalSamples;
            
            // Calculate samples per second
            const now = Date.now();
            const elapsed = (now - lastTime) / 1000;
            if (elapsed > 1.0) {
                const sps = Math.floor((totalSamples - lastSampleCount) / elapsed);
                document.getElementById('sps').textContent = sps.toLocaleString();
                lastSampleCount = totalSamples;
                lastTime = now;
            }
        }

        // Assign work to a worker
        function assignWork(worker) {
            if (!isTracing) return;
            
            worker.idle = false;
            
            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };
            
            worker.postMessage({
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerBatch: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width: width,
                height: height
            });
        }

        // Start rendering
        function startRendering() {
            isTracing = true;
            initWorkers();
            lastTime = Date.now();
            lastSampleCount = 0;
            
            // Start all workers
            workers.forEach(w => assignWork(w));
        }

        // Stop rendering
        function stopRendering() {
            isTracing = false;
        }

        // Reset
        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);
            accumBuffer = new Float32Array(width * height * 3);
            sampleCountPerPixel = new Uint32Array(width * height);
            totalSamples = 0;
            lastSampleCount = 0;
            document.getElementById('samples').textContent = '0';
            document.getElementById('sps').textContent = '0';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (totalSamples === 0) {
                    startRendering();
                } else {
                    isTracing = true;
                    workers.filter(w => w.idle).forEach(w => assignWork(w));
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });

        document.getElementById('reset').addEventListener('click', resetRendering);

        // =============================================
        // Animation Loop
        // =============================================
        let frameCount = 0;
        function animate() {
            requestAnimationFrame(animate);
            
            updateMovement();
            
            renderer.render(scene, camera);
            
            // Update display every few frames
            if (isTracing && frameCount++ % 2 === 0) {
                updateDisplay();
            }
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### bajar calidad

```html
<!DOCTYPE html>
<html>
<head>
    <title>Monte Carlo Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 250px;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="controls">
        <div><strong>Monte Carlo Path Tracer</strong></div>
        <div>Cores Used: <span id="cores">0</span> / <span id="totalCores">0</span></div>
        <div>Total Samples: <span id="samples">0</span></div>
        <div>Samples/sec: <span id="sps">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <div style="margin-top: 10px;">
            <label>Pixel Size: <input type="number" id="pixelSize" value="1" min="1" max="16"></label>
            <span style="font-size: 10px; color: #aaa;">(1=full quality, 4=4x faster)</span>
        </div>
        <div>
            <label>Samples/Frame: <input type="number" id="spp" value="1000" min="100" max="10000"></label>
        </div>
        <div>
            <label>Max Bounces: <input type="number" id="bounces" value="5" min="1" max="10"></label>
        </div>
        <div style="margin-top: 5px; font-size: 11px; color: #aaa;">
            Click to enable FPS controls<br>
            WASD: Move | Mouse: Look<br>
            Space: Up | Shift: Down/Sprint<br>
            Motion blur effect enabled
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;
        controls.enabled = false; // Disable orbit controls, we'll use FPS controls

        // =============================================
        // FPS Controls
        // =============================================
        const moveSpeed = 0.05;
        const mouseSensitivity = 0.002;
        const keys = { w: false, a: false, s: false, d: false, shift: false, space: false };
        let pitch = 0;
        let yaw = 0;
        let isPointerLocked = false;

        // Pointer lock
        document.body.addEventListener('click', () => {
            if (!isPointerLocked) {
                document.body.requestPointerLock();
            }
        });

        document.addEventListener('pointerlockchange', () => {
            isPointerLocked = document.pointerLockElement === document.body;
            if (isPointerLocked) {
                console.log('Pointer locked - use WASD to move, mouse to look');
            } else {
                console.log('Pointer unlocked - click to lock again');
            }
        });

        // Mouse movement
        document.addEventListener('mousemove', (e) => {
            if (!isPointerLocked) return;

            yaw -= e.movementX * mouseSensitivity;
            pitch -= e.movementY * mouseSensitivity;
            pitch = Math.max(-Math.PI / 2 + 0.01, Math.min(Math.PI / 2 - 0.01, pitch));

            const euler = new THREE.Euler(pitch, yaw, 0, 'YXZ');
            camera.quaternion.setFromEuler(euler);
        });

        // Keyboard input
        document.addEventListener('keydown', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) {
                keys[key] = true;
                e.preventDefault();
            }
        });

        document.addEventListener('keyup', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) {
                keys[key] = false;
                e.preventDefault();
            }
        });

        // Update camera position
        function updateMovement() {
            const forward = new THREE.Vector3(0, 0, -1);
            forward.applyQuaternion(camera.quaternion);
            forward.y = 0;
            forward.normalize();

            const right = new THREE.Vector3(1, 0, 0);
            right.applyQuaternion(camera.quaternion);
            right.y = 0;
            right.normalize();

            const speed = keys.shift && (keys.w || keys.s || keys.a || keys.d) ? moveSpeed * 2 : moveSpeed;

            if (keys.w) {
                camera.position.addScaledVector(forward, speed);
            }
            if (keys.s) {
                camera.position.addScaledVector(forward, -speed);
            }
            if (keys.d) {
                camera.position.addScaledVector(right, speed);
            }
            if (keys.a) {
                camera.position.addScaledVector(right, -speed);
            }
            if (keys.space) {
                camera.position.y += speed;
            }
            if (keys.shift && !keys.w && !keys.s && !keys.a && !keys.d) {
                camera.position.y -= speed;
            }
        }

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];

        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ 
                mesh, 
                type, 
                color, 
                emission,
                worldMatrix: mesh.matrixWorld.clone()
            });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.95, 0.95, 0.95]);

        // Floor (white) - facing up
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = -Math.PI / 2;
        addObject(floor, 'diffuse', [0.95, 0.95, 0.95]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.95, 0.95, 0.95]);

        // Light (area light) - much brighter
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        pitch = 0;
        yaw = 0;
        camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));

        // Update world matrices
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(obj => {
            obj.worldMatrix = obj.mesh.matrixWorld.clone();
        });

        // =============================================
        // Monte Carlo Progressive Path Tracer
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const totalCores = navigator.hardwareConcurrency || 4;
        const numCores = Math.max(1, Math.floor(totalCores / 1));
        document.getElementById('cores').textContent = numCores;
        document.getElementById('totalCores').textContent = totalCores;

        let workers = [];
        let isTracing = false;
        let totalSamples = 0;
        let accumBuffer = new Float32Array(width * height * 3);
        let imageData = ctx.createImageData(width, height);
        let lastSampleCount = 0;
        let lastTime = Date.now();

        // Worker code for Monte Carlo sampling
        const workerCode = `
            const raycaster = {};
            
            function intersectRay(origin, direction, objects) {
                let closest = null;
                let minDist = Infinity;
                
                for (const obj of objects) {
                    const result = intersectObject(origin, direction, obj);
                    if (result && result.distance < minDist) {
                        minDist = result.distance;
                        closest = result;
                        closest.object = obj;
                    }
                }
                
                return closest;
            }
            
            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') {
                    return intersectSphere(origin, direction, obj);
                } else if (obj.geometry === 'plane') {
                    return intersectPlane(origin, direction, obj);
                }
                return null;
            }
            
            function intersectSphere(origin, direction, obj) {
                const center = obj.position;
                const radius = obj.radius;
                const oc = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - radius*radius;
                const discriminant = b*b - 4*a*c;
                
                if (discriminant < 0) return null;
                
                const t = (-b - Math.sqrt(discriminant)) / (2*a);
                if (t < 0.001) return null;
                
                const point = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const normal = [
                    (point[0] - center[0]) / radius,
                    (point[1] - center[1]) / radius,
                    (point[2] - center[2]) / radius
                ];
                
                return { distance: t, point, normal };
            }
            
            function intersectPlane(origin, direction, obj) {
                const normal = obj.normal;
                const point = obj.position;
                
                const denom = normal[0]*direction[0] + normal[1]*direction[1] + normal[2]*direction[2];
                if (Math.abs(denom) < 0.0001) return null;
                
                const diff = [point[0] - origin[0], point[1] - origin[1], point[2] - origin[2]];
                const t = (diff[0]*normal[0] + diff[1]*normal[1] + diff[2]*normal[2]) / denom;
                
                if (t < 0.001) return null;
                
                const hitPoint = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const localPoint = [
                    hitPoint[0] - point[0],
                    hitPoint[1] - point[1],
                    hitPoint[2] - point[2]
                ];
                
                const size = obj.size;
                const u = obj.uAxis;
                const v = obj.vAxis;
                
                const uCoord = localPoint[0]*u[0] + localPoint[1]*u[1] + localPoint[2]*u[2];
                const vCoord = localPoint[0]*v[0] + localPoint[1]*v[1] + localPoint[2]*v[2];
                
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;
                
                let finalNormal = normal;
                if (denom > 0) {
                    finalNormal = [-normal[0], -normal[1], -normal[2]];
                }
                
                return { distance: t, point: hitPoint, normal: finalNormal };
            }
            
            function random() {
                return Math.random();
            }
            
            function randomInUnitSphere() {
                while (true) {
                    const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                    if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
                }
            }
            
            function randomInHemisphere(normal) {
                const v = randomInUnitSphere();
                const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
                if (dot > 0) return v;
                return [-v[0], -v[1], -v[2]];
            }
            
            function reflect(v, n) {
                const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
                return [v[0] - 2*dot*n[0], v[1] - 2*dot*n[1], v[2] - 2*dot*n[2]];
            }
            
            function normalize(v) {
                const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
                return len > 0 ? [v[0]/len, v[1]/len, v[2]/len] : v;
            }
            
            function trace(origin, direction, depth, maxDepth, objects) {
                if (depth >= maxDepth) return [0, 0, 0];
                
                const hit = intersectRay(origin, direction, objects);
                if (!hit) return [0, 0, 0];
                
                const obj = hit.object;
                const hitPoint = hit.point;
                const normal = hit.normal;
                
                const offset = 0.001;
                const offsetPoint = [
                    hitPoint[0] + normal[0] * offset,
                    hitPoint[1] + normal[1] * offset,
                    hitPoint[2] + normal[2] * offset
                ];
                
                if (obj.type === 'emissive') {
                    return obj.emission;
                }
                
                const attenuation = obj.color;
                
                if (obj.type === 'reflective') {
                    const newDir = reflect(direction, normal);
                    const normalized = normalize(newDir);
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    return [
                        attenuation[0] * incoming[0],
                        attenuation[1] * incoming[1],
                        attenuation[2] * incoming[2]
                    ];
                } else {
                    const newDir = randomInHemisphere(normal);
                    const normalized = normalize(newDir);
                    
                    const cosTheta = Math.max(0, 
                        normalized[0] * normal[0] + 
                        normalized[1] * normal[1] + 
                        normalized[2] * normal[2]
                    );
                    
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    const scale = 2.0 * cosTheta;
                    
                    return [
                        attenuation[0] * incoming[0] * scale,
                        attenuation[1] * incoming[1] * scale,
                        attenuation[2] * incoming[2] * scale
                    ];
                }
            }
            
            self.onmessage = function(e) {
                const { camera, objects, samplesPerBatch, maxBounces, width, height, pixelSize } = e.data;
                
                const sampleData = [];
                
                // Monte Carlo: randomly sample pixels across entire image
                for (let s = 0; s < samplesPerBatch; s++) {
                    // Sample at pixelSize intervals
                    const gridWidth = Math.ceil(width / pixelSize);
                    const gridHeight = Math.ceil(height / pixelSize);
                    
                    const gridX = Math.floor(random() * gridWidth);
                    const gridY = Math.floor(random() * gridHeight);
                    
                    const x = gridX * pixelSize;
                    const y = gridY * pixelSize;
                    
                    // Sample from center of pixel block
                    const u = (x + pixelSize / 2 + random() * pixelSize - pixelSize / 2) / width;
                    const v = (y + pixelSize / 2 + random() * pixelSize - pixelSize / 2) / height;
                    
                    const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                    const py = -(v * 2 - 1) * camera.tanFov;
                    
                    let dir = [px, py, -1];
                    const len = Math.sqrt(dir[0]*dir[0] + dir[1]*dir[1] + dir[2]*dir[2]);
                    dir = [dir[0]/len, dir[1]/len, dir[2]/len];
                    
                    const q = camera.quaternion;
                    const rotated = rotateByQuaternion(dir, q);
                    
                    const color = trace(camera.position, rotated, 0, maxBounces, objects);
                    
                    // Store as individual samples with pixel block coordinates
                    sampleData.push({
                        x: x,
                        y: y,
                        pixelSize: pixelSize,
                        color: color
                    });
                }
                
                self.postMessage({ sampleData });
            };
            
            function rotateByQuaternion(v, q) {
                const qx = q[0], qy = q[1], qz = q[2], qw = q[3];
                const x = v[0], y = v[1], z = v[2];
                
                const ix = qw * x + qy * z - qz * y;
                const iy = qw * y + qz * x - qx * z;
                const iz = qw * z + qx * y - qy * x;
                const iw = -qx * x - qy * y - qz * z;
                
                return [
                    ix * qw + iw * -qx + iy * -qz - iz * -qy,
                    iy * qw + iw * -qy + iz * -qx - ix * -qz,
                    iz * qw + iw * -qz + ix * -qy - iy * -qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        // Create workers
        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            
            for (let i = 0; i < numCores; i++) {
                const worker = new Worker(workerUrl);
                worker.onmessage = handleWorkerResult;
                worker.idle = true;
                workers.push(worker);
            }
        }

        // Convert Three.js objects to worker-compatible format
        function serializeObjects() {
            const serialized = [];
            
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1);
                    normal.applyQuaternion(mesh.quaternion).normalize();
                    
                    const uAxis = new THREE.Vector3(1, 0, 0);
                    uAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    const vAxis = new THREE.Vector3(0, 1, 0);
                    vAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            
            return serialized;
        }

        // Sample count per pixel buffer for proper averaging
        let sampleCountPerPixel = new Uint32Array(width * height);

        // Handle worker results
        function handleWorkerResult(e) {
            const { sampleData } = e.data;
            
            // Accumulate samples into buffer
            for (const sample of sampleData) {
                const pixelSize = sample.pixelSize;
                
                // Fill all pixels in the block
                for (let dy = 0; dy < pixelSize && sample.y + dy < height; dy++) {
                    for (let dx = 0; dx < pixelSize && sample.x + dx < width; dx++) {
                        const px = sample.x + dx;
                        const py = sample.y + dy;
                        const pixelIdx = py * width + px;
                        const idx = pixelIdx * 3;
                        
                        accumBuffer[idx] += sample.color[0];
                        accumBuffer[idx + 1] += sample.color[1];
                        accumBuffer[idx + 2] += sample.color[2];
                        sampleCountPerPixel[pixelIdx]++;
                    }
                }
            }
            
            totalSamples += sampleData.length;
            
            // Mark worker as idle and continue
            e.target.idle = true;
            if (isTracing) {
                assignWork(e.target);
            }
        }

        // Update display (called periodically)
        function updateDisplay() {
            if (totalSamples === 0) return;
            
            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    const pixelIdx = y * width + x;
                    const idx = pixelIdx * 3;
                    const imgIdx = pixelIdx * 4;
                    
                    const count = sampleCountPerPixel[pixelIdx];
                    if (count === 0) {
                        // No samples yet for this pixel, keep it black
                        imageData.data[imgIdx] = 0;
                        imageData.data[imgIdx + 1] = 0;
                        imageData.data[imgIdx + 2] = 0;
                        imageData.data[imgIdx + 3] = 255;
                        continue;
                    }
                    
                    const scale = 1.0 / count;
                    
                    let r = accumBuffer[idx] * scale;
                    let g = accumBuffer[idx + 1] * scale;
                    let b = accumBuffer[idx + 2] * scale;
                    
                    // Gamma correction
                    r = Math.pow(r, 1/2.2);
                    g = Math.pow(g, 1/2.2);
                    b = Math.pow(b, 1/2.2);
                    
                    imageData.data[imgIdx] = Math.min(255, r * 255);
                    imageData.data[imgIdx + 1] = Math.min(255, g * 255);
                    imageData.data[imgIdx + 2] = Math.min(255, b * 255);
                    imageData.data[imgIdx + 3] = 255;
                }
            }
            
            ctx.putImageData(imageData, 0, 0);
            document.getElementById('samples').textContent = totalSamples;
            
            // Calculate samples per second
            const now = Date.now();
            const elapsed = (now - lastTime) / 1000;
            if (elapsed > 1.0) {
                const sps = Math.floor((totalSamples - lastSampleCount) / elapsed);
                document.getElementById('sps').textContent = sps.toLocaleString();
                lastSampleCount = totalSamples;
                lastTime = now;
            }
        }

        // Assign work to a worker
        function assignWork(worker) {
            if (!isTracing) return;
            
            worker.idle = false;
            
            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };
            
            const pixelSize = parseInt(document.getElementById('pixelSize').value);
            
            worker.postMessage({
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerBatch: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width: width,
                height: height,
                pixelSize: pixelSize
            });
        }

        // Start rendering
        function startRendering() {
            isTracing = true;
            initWorkers();
            lastTime = Date.now();
            lastSampleCount = 0;
            
            // Start all workers
            workers.forEach(w => assignWork(w));
        }

        // Stop rendering
        function stopRendering() {
            isTracing = false;
        }

        // Reset
        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);
            accumBuffer = new Float32Array(width * height * 3);
            sampleCountPerPixel = new Uint32Array(width * height);
            totalSamples = 0;
            lastSampleCount = 0;
            document.getElementById('samples').textContent = '0';
            document.getElementById('sps').textContent = '0';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (totalSamples === 0) {
                    startRendering();
                } else {
                    isTracing = true;
                    workers.filter(w => w.idle).forEach(w => assignWork(w));
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });

        document.getElementById('reset').addEventListener('click', resetRendering);

        // =============================================
        // Animation Loop
        // =============================================
        let frameCount = 0;
        function animate() {
            requestAnimationFrame(animate);
            
            updateMovement();
            
            renderer.render(scene, camera);
            
            // Update display every few frames
            if (isTracing && frameCount++ % 2 === 0) {
                updateDisplay();
            }
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### decaida

```html
<!DOCTYPE html>
<html>
<head>
    <title>Monte Carlo Path Tracer - Cornell Box</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 260px;
            line-height: 1.4;
            user-select: none;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
        label { display: block; margin-top: 6px; }
        input[type="number"] { width: 90px; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="controls">
        <div><strong>Monte Carlo Path Tracer</strong></div>
        <div>Cores Used: <span id="cores">0</span> / <span id="totalCores">0</span></div>
        <div>Total Samples: <span id="samples">0</span></div>
        <div>Samples/sec: <span id="sps">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <label>
            Pixel Size:
            <input type="number" id="pixelSize" value="1" min="1" max="16">
            <span style="font-size: 10px; color: #aaa;">(1=full quality, 4=4x faster)</span>
        </label>
        <label>
            Samples/Frame:
            <input type="number" id="spp" value="1000" min="100" max="10000">
        </label>
        <label>
            Max Bounces:
            <input type="number" id="bounces" value="5" min="1" max="10">
        </label>
        <label>
            Fade Half-Life (s):
            <input type="number" id="fadeHalfLife" value="0.75" step="0.05" min="0.05" max="10">
        </label>
        <div style="margin-top: 6px; font-size: 11px; color: #aaa;">
            Click to enable FPS controls<br>
            WASD: Move | Mouse: Look<br>
            Space: Up | Shift: Down/Sprint<br>
            Motion blur + POV fade enabled
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;
        controls.enabled = false; // Disable orbit controls, we'll use FPS controls

        // =============================================
        // FPS Controls
        // =============================================
        const moveSpeed = 0.05;
        const mouseSensitivity = 0.002;
        const keys = { w: false, a: false, s: false, d: false, shift: false, space: false };
        let pitch = 0;
        let yaw = 0;
        let isPointerLocked = false;

        // Pointer lock
        document.body.addEventListener('click', () => {
            if (!isPointerLocked) {
                document.body.requestPointerLock();
            }
        });

        document.addEventListener('pointerlockchange', () => {
            isPointerLocked = document.pointerLockElement === document.body;
            if (isPointerLocked) {
                console.log('Pointer locked - use WASD to move, mouse to look');
            } else {
                console.log('Pointer unlocked - click to lock again');
            }
        });

        // Mouse movement
        document.addEventListener('mousemove', (e) => {
            if (!isPointerLocked) return;

            yaw -= e.movementX * mouseSensitivity;
            pitch -= e.movementY * mouseSensitivity;
            pitch = Math.max(-Math.PI / 2 + 0.01, Math.min(Math.PI / 2 - 0.01, pitch));

            const euler = new THREE.Euler(pitch, yaw, 0, 'YXZ');
            camera.quaternion.setFromEuler(euler);
        });

        // Keyboard input
        document.addEventListener('keydown', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) {
                keys[key] = true;
                e.preventDefault();
            }
        });

        document.addEventListener('keyup', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) {
                keys[key] = false;
                e.preventDefault();
            }
        });

        // Update camera position
        function updateMovement() {
            const forward = new THREE.Vector3(0, 0, -1);
            forward.applyQuaternion(camera.quaternion);
            forward.y = 0;
            forward.normalize();

            const right = new THREE.Vector3(1, 0, 0);
            right.applyQuaternion(camera.quaternion);
            right.y = 0;
            right.normalize();

            const speed = keys.shift && (keys.w || keys.s || keys.a || keys.d) ? moveSpeed * 2 : moveSpeed;

            if (keys.w) {
                camera.position.addScaledVector(forward, speed);
            }
            if (keys.s) {
                camera.position.addScaledVector(forward, -speed);
            }
            if (keys.d) {
                camera.position.addScaledVector(right, speed);
            }
            if (keys.a) {
                camera.position.addScaledVector(right, -speed);
            }
            if (keys.space) {
                camera.position.y += speed;
            }
            if (keys.shift && !keys.w && !keys.s && !keys.a && !keys.d) {
                camera.position.y -= speed;
            }
        }

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];

        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ 
                mesh, 
                type, 
                color, 
                emission,
                worldMatrix: mesh.matrixWorld.clone()
            });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.95, 0.95, 0.95]);

        // Floor (white) - facing up
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = -Math.PI / 2;
        addObject(floor, 'diffuse', [0.95, 0.95, 0.95]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.95, 0.95, 0.95]);

        // Light (area light) - much brighter
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse white)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Add some lighting for Three.js preview
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        pitch = 0;
        yaw = 0;
        camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));

        // Update world matrices
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(obj => {
            obj.worldMatrix = obj.mesh.matrixWorld.clone();
        });

        // =============================================
        // Monte Carlo Progressive Path Tracer
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const totalCores = navigator.hardwareConcurrency || 4;
        const numCores = Math.max(1, Math.floor(totalCores / 2));
        document.getElementById('cores').textContent = numCores;
        document.getElementById('totalCores').textContent = totalCores;

        let workers = [];
        let isTracing = false;
        let totalSamples = 0;
        let accumBuffer = new Float32Array(width * height * 3);
        let imageData = ctx.createImageData(width, height);
        let lastSampleCount = 0;
        let lastTime = Date.now();

        // --- Persistence-of-vision display buffer ---
        let displayBuffer = new Float32Array(width * height * 3); // stores faded, linearly-averaged display color
        let lastDisplayTS = performance.now();

        // Worker code for Monte Carlo sampling
        const workerCode = `
            const raycaster = {};
            
            function intersectRay(origin, direction, objects) {
                let closest = null;
                let minDist = Infinity;
                
                for (const obj of objects) {
                    const result = intersectObject(origin, direction, obj);
                    if (result && result.distance < minDist) {
                        minDist = result.distance;
                        closest = result;
                        closest.object = obj;
                    }
                }
                
                return closest;
            }
            
            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') {
                    return intersectSphere(origin, direction, obj);
                } else if (obj.geometry === 'plane') {
                    return intersectPlane(origin, direction, obj);
                }
                return null;
            }
            
            function intersectSphere(origin, direction, obj) {
                const center = obj.position;
                const radius = obj.radius;
                const oc = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - radius*radius;
                const discriminant = b*b - 4*a*c;
                
                if (discriminant < 0) return null;
                
                const t = (-b - Math.sqrt(discriminant)) / (2*a);
                if (t < 0.001) return null;
                
                const point = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const normal = [
                    (point[0] - center[0]) / radius,
                    (point[1] - center[1]) / radius,
                    (point[2] - center[2]) / radius
                ];
                
                return { distance: t, point, normal };
            }
            
            function intersectPlane(origin, direction, obj) {
                const normal = obj.normal;
                const point = obj.position;
                
                const denom = normal[0]*direction[0] + normal[1]*direction[1] + normal[2]*direction[2];
                if (Math.abs(denom) < 0.0001) return null;
                
                const diff = [point[0] - origin[0], point[1] - origin[1], point[2] - origin[2]];
                const t = (diff[0]*normal[0] + diff[1]*normal[1] + diff[2]*normal[2]) / denom;
                
                if (t < 0.001) return null;
                
                const hitPoint = [
                    origin[0] + direction[0] * t,
                    origin[1] + direction[1] * t,
                    origin[2] + direction[2] * t
                ];
                
                const localPoint = [
                    hitPoint[0] - point[0],
                    hitPoint[1] - point[1],
                    hitPoint[2] - point[2]
                ];
                
                const size = obj.size;
                const u = obj.uAxis;
                const v = obj.vAxis;
                
                const uCoord = localPoint[0]*u[0] + localPoint[1]*u[1] + localPoint[2]*u[2];
                const vCoord = localPoint[0]*v[0] + localPoint[1]*v[1] + localPoint[2]*v[2];
                
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;
                
                let finalNormal = normal;
                if (denom > 0) {
                    finalNormal = [-normal[0], -normal[1], -normal[2]];
                }
                
                return { distance: t, point: hitPoint, normal: finalNormal };
            }
            
            function random() {
                return Math.random();
            }
            
            function randomInUnitSphere() {
                while (true) {
                    const v = [random() * 2 - 1, random() * 2 - 1, random() * 2 - 1];
                    if (v[0]*v[0] + v[1]*v[1] + v[2]*v[2] < 1) return v;
                }
            }
            
            function randomInHemisphere(normal) {
                const v = randomInUnitSphere();
                const dot = v[0]*normal[0] + v[1]*normal[1] + v[2]*normal[2];
                if (dot > 0) return v;
                return [-v[0], -v[1], -v[2]];
            }
            
            function reflect(v, n) {
                const dot = v[0]*n[0] + v[1]*n[1] + v[2]*n[2];
                return [v[0] - 2*dot*n[0], v[1] - 2*dot*n[1], v[2] - 2*dot*n[2]];
            }
            
            function normalize(v) {
                const len = Math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
                return len > 0 ? [v[0]/len, v[1]/len, v[2]/len] : v;
            }
            
            function trace(origin, direction, depth, maxDepth, objects) {
                if (depth >= maxDepth) return [0, 0, 0];
                
                const hit = intersectRay(origin, direction, objects);
                if (!hit) return [0, 0, 0];
                
                const obj = hit.object;
                const hitPoint = hit.point;
                const normal = hit.normal;
                
                const offset = 0.001;
                const offsetPoint = [
                    hitPoint[0] + normal[0] * offset,
                    hitPoint[1] + normal[1] * offset,
                    hitPoint[2] + normal[2] * offset
                ];
                
                if (obj.type === 'emissive') {
                    return obj.emission;
                }
                
                const attenuation = obj.color;
                
                if (obj.type === 'reflective') {
                    const newDir = reflect(direction, normal);
                    const normalized = normalize(newDir);
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    return [
                        attenuation[0] * incoming[0],
                        attenuation[1] * incoming[1],
                        attenuation[2] * incoming[2]
                    ];
                } else {
                    const newDir = randomInHemisphere(normal);
                    const normalized = normalize(newDir);
                    
                    const cosTheta = Math.max(0, 
                        normalized[0] * normal[0] + 
                        normalized[1] * normal[1] + 
                        normalized[2] * normal[2]
                    );
                    
                    const incoming = trace(offsetPoint, normalized, depth + 1, maxDepth, objects);
                    const scale = 2.0 * cosTheta;
                    
                    return [
                        attenuation[0] * incoming[0] * scale,
                        attenuation[1] * incoming[1] * scale,
                        attenuation[2] * incoming[2] * scale
                    ];
                }
            }
            
            self.onmessage = function(e) {
                const { camera, objects, samplesPerBatch, maxBounces, width, height, pixelSize } = e.data;
                
                const sampleData = [];
                
                // Monte Carlo: randomly sample pixels across entire image
                for (let s = 0; s < samplesPerBatch; s++) {
                    // Sample at pixelSize intervals
                    const gridWidth = Math.ceil(width / pixelSize);
                    const gridHeight = Math.ceil(height / pixelSize);
                    
                    const gridX = Math.floor(random() * gridWidth);
                    const gridY = Math.floor(random() * gridHeight);
                    
                    const x = gridX * pixelSize;
                    const y = gridY * pixelSize;
                    
                    // Sample from center of pixel block
                    const u = (x + pixelSize / 2 + random() * pixelSize - pixelSize / 2) / width;
                    const v = (y + pixelSize / 2 + random() * pixelSize - pixelSize / 2) / height;
                    
                    const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                    const py = -(v * 2 - 1) * camera.tanFov;
                    
                    let dir = [px, py, -1];
                    const len = Math.sqrt(dir[0]*dir[0] + dir[1]*dir[1] + dir[2]*dir[2]);
                    dir = [dir[0]/len, dir[1]/len, dir[2]/len];
                    
                    const q = camera.quaternion;
                    const rotated = rotateByQuaternion(dir, q);
                    
                    const color = trace(camera.position, rotated, 0, maxBounces, objects);
                    
                    // Store as individual samples with pixel block coordinates
                    sampleData.push({
                        x: x,
                        y: y,
                        pixelSize: pixelSize,
                        color: color
                    });
                }
                
                self.postMessage({ sampleData });
            };
            
            function rotateByQuaternion(v, q) {
                const qx = q[0], qy = q[1], qz = q[2], qw = q[3];
                const x = v[0], y = v[1], z = v[2];
                
                const ix = qw * x + qy * z - qz * y;
                const iy = qw * y + qz * x - qx * z;
                const iz = qw * z + qx * y - qy * x;
                const iw = -qx * x - qy * y - qz * z;
                
                return [
                    ix * qw + iw * -qx + iy * -qz - iz * -qy,
                    iy * qw + iw * -qy + iz * -qx - ix * -qz,
                    iz * qw + iw * -qz + ix * -qy - iy * -qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        // Create workers
        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            
            for (let i = 0; i < numCores; i++) {
                const worker = new Worker(workerUrl);
                worker.onmessage = handleWorkerResult;
                worker.idle = true;
                workers.push(worker);
            }
        }

        // Convert Three.js objects to worker-compatible format
        function serializeObjects() {
            const serialized = [];
            
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1);
                    normal.applyQuaternion(mesh.quaternion).normalize();
                    
                    const uAxis = new THREE.Vector3(1, 0, 0);
                    uAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    const vAxis = new THREE.Vector3(0, 1, 0);
                    vAxis.applyQuaternion(mesh.quaternion).normalize();
                    
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            
            return serialized;
        }

        // Sample count per pixel buffer for proper averaging
        let sampleCountPerPixel = new Uint32Array(width * height);

        // Handle worker results
        function handleWorkerResult(e) {
            const { sampleData } = e.data;
            
            // Accumulate samples into buffer
            for (const sample of sampleData) {
                const pixelSize = sample.pixelSize;
                
                // Fill all pixels in the block
                for (let dy = 0; dy < pixelSize && sample.y + dy < height; dy++) {
                    for (let dx = 0; dx < pixelSize && sample.x + dx < width; dx++) {
                        const px = sample.x + dx;
                        const py = sample.y + dy;
                        const pixelIdx = py * width + px;
                        const idx = pixelIdx * 3;
                        
                        accumBuffer[idx] += sample.color[0];
                        accumBuffer[idx + 1] += sample.color[1];
                        accumBuffer[idx + 2] += sample.color[2];
                        sampleCountPerPixel[pixelIdx]++;
                    }
                }
            }
            
            totalSamples += sampleData.length;
            
            // Mark worker as idle and continue
            e.target.idle = true;
            if (isTracing) {
                assignWork(e.target);
            }
        }

        // Update display (with persistence-of-vision fading)
        function updateDisplay() {
            // allow fade even with few samples; if none at all, nothing to show
            if (totalSamples === 0) return;
            
            const nowPerf = performance.now();
            const dt = Math.max(0.0, (nowPerf - lastDisplayTS) / 1000.0);
            lastDisplayTS = nowPerf;

            // Half-life in seconds: decay = 0.5^(dt/halfLife)
            const halfLifeInput = document.getElementById('fadeHalfLife');
            const halfLife = Math.max(0.05, parseFloat(halfLifeInput.value) || 0.75);
            const decay = Math.pow(0.5, dt / halfLife);
            const oneMinus = 1.0 - decay;

            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    const pixelIdx = y * width + x;
                    const idx3 = pixelIdx * 3;
                    const imgIdx = pixelIdx * 4;

                    // New average (linear)
                    const count = sampleCountPerPixel[pixelIdx];
                    let nr = 0, ng = 0, nb = 0;
                    if (count > 0) {
                        const inv = 1.0 / count;
                        nr = accumBuffer[idx3    ] * inv;
                        ng = accumBuffer[idx3 + 1] * inv;
                        nb = accumBuffer[idx3 + 2] * inv;
                    }

                    // Persistence: display = display*decay + new*(1-decay)
                    const dr = displayBuffer[idx3    ] * decay + nr * oneMinus;
                    const dg = displayBuffer[idx3 + 1] * decay + ng * oneMinus;
                    const db = displayBuffer[idx3 + 2] * decay + nb * oneMinus;

                    displayBuffer[idx3    ] = dr;
                    displayBuffer[idx3 + 1] = dg;
                    displayBuffer[idx3 + 2] = db;

                    // Gamma correction (sRGB approx)
                    const gr = Math.pow(Math.max(0, dr), 1/2.2);
                    const gg = Math.pow(Math.max(0, dg), 1/2.2);
                    const gb = Math.pow(Math.max(0, db), 1/2.2);

                    imageData.data[imgIdx    ] = Math.min(255, gr * 255);
                    imageData.data[imgIdx + 1] = Math.min(255, gg * 255);
                    imageData.data[imgIdx + 2] = Math.min(255, gb * 255);
                    imageData.data[imgIdx + 3] = 255;
                }
            }

            ctx.putImageData(imageData, 0, 0);

            // Stats (samples / sps)
            document.getElementById('samples').textContent = totalSamples;
            const nowMs = Date.now();
            const elapsed = (nowMs - lastTime) / 1000;
            if (elapsed > 1.0) {
                const sps = Math.floor((totalSamples - lastSampleCount) / elapsed);
                document.getElementById('sps').textContent = sps.toLocaleString();
                lastSampleCount = totalSamples;
                lastTime = nowMs;
            }
        }

        // Assign work to a worker
        function assignWork(worker) {
            if (!isTracing) return;
            
            worker.idle = false;
            
            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };
            
            const pixelSize = parseInt(document.getElementById('pixelSize').value);
            
            worker.postMessage({
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerBatch: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width: width,
                height: height,
                pixelSize: pixelSize
            });
        }

        // Start rendering
        function startRendering() {
            isTracing = true;
            initWorkers();
            lastTime = Date.now();
            lastSampleCount = 0;
            lastDisplayTS = performance.now();
            
            // Start all workers
            workers.forEach(w => assignWork(w));
        }

        // Stop rendering
        function stopRendering() {
            isTracing = false;
        }

        // Reset
        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);
            accumBuffer = new Float32Array(width * height * 3);
            sampleCountPerPixel = new Uint32Array(width * height);
            displayBuffer = new Float32Array(width * height * 3); // clear persistence buffer
            totalSamples = 0;
            lastSampleCount = 0;
            lastTime = Date.now();
            lastDisplayTS = performance.now();
            document.getElementById('samples').textContent = '0';
            document.getElementById('sps').textContent = '0';
        }

        // =============================================
        // Controls
        // =============================================
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (totalSamples === 0) {
                    startRendering();
                } else {
                    isTracing = true;
                    lastDisplayTS = performance.now(); // resume timing continuity
                    workers.filter(w => w.idle).forEach(w => assignWork(w));
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });

        document.getElementById('reset').addEventListener('click', resetRendering);

        // =============================================
        // Animation Loop
        // =============================================
        let frameCount = 0;
        function animate() {
            requestAnimationFrame(animate);
            
            updateMovement();
            renderer.render(scene, camera);
            
            // Update display every few frames
            if (isTracing && frameCount++ % 2 === 0) {
                updateDisplay();
            }
        }
        animate();

        // Handle resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### caida 2

```html
<!DOCTYPE html>
<html>
<head>
    <title>Monte Carlo Path Tracer - Cornell Box (POV Fade)</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 260px;
            line-height: 1.4;
            user-select: none;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
        label { display: block; margin-top: 6px; }
        input[type="number"] { width: 90px; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="controls">
        <div><strong>Monte Carlo Path Tracer</strong></div>
        <div>Cores Used: <span id="cores">0</span> / <span id="totalCores">0</span></div>
        <div>Total Samples: <span id="samples">0</span></div>
        <div>Samples/sec: <span id="sps">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <label>
            Pixel Size:
            <input type="number" id="pixelSize" value="2" min="1" max="16">
            <span style="font-size: 10px; color: #aaa;">(1=full quality, 4=4x faster)</span>
        </label>
        <label>
            Samples/Frame:
            <input type="number" id="spp" value="1000" min="100" max="10000">
        </label>
        <label>
            Max Bounces:
            <input type="number" id="bounces" value="5" min="1" max="10">
        </label>
        <label>
            Fade Half-Life (s):
            <input type="number" id="fadeHalfLife" value="20" step="0.05" min="0.05" max="20">
        </label>
        <div style="margin-top: 6px; font-size: 11px; color: #aaa;">
            Click to enable FPS controls<br>
            WASD: Move | Mouse: Look<br>
            Space: Up | Shift: Down/Sprint<br>
            POV fading is time-based (exponential)
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;
        controls.enabled = false; // FPS controls instead

        // =============================================
        // FPS Controls
        // =============================================
        const moveSpeed = 0.05;
        const mouseSensitivity = 0.002;
        const keys = { w: false, a: false, s: false, d: false, shift: false, space: false };
        let pitch = 0;
        let yaw = 0;
        let isPointerLocked = false;

        // Pointer lock
        document.body.addEventListener('click', () => {
            if (!isPointerLocked) document.body.requestPointerLock();
        });
        document.addEventListener('pointerlockchange', () => {
            isPointerLocked = document.pointerLockElement === document.body;
        });

        // Mouse movement
        document.addEventListener('mousemove', (e) => {
            if (!isPointerLocked) return;
            yaw -= e.movementX * mouseSensitivity;
            pitch -= e.movementY * mouseSensitivity;
            pitch = Math.max(-Math.PI / 2 + 0.01, Math.min(Math.PI / 2 - 0.01, pitch));
            const euler = new THREE.Euler(pitch, yaw, 0, 'YXZ');
            camera.quaternion.setFromEuler(euler);
        });

        // Keyboard input
        document.addEventListener('keydown', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) { keys[key] = true; e.preventDefault(); }
        });
        document.addEventListener('keyup', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) { keys[key] = false; e.preventDefault(); }
        });

        function updateMovement() {
            const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(camera.quaternion);
            forward.y = 0; forward.normalize();
            const right = new THREE.Vector3(1, 0, 0).applyQuaternion(camera.quaternion);
            right.y = 0; right.normalize();
            const speed = keys.shift && (keys.w || keys.s || keys.a || keys.d) ? moveSpeed * 2 : moveSpeed;

            if (keys.w) camera.position.addScaledVector(forward, speed);
            if (keys.s) camera.position.addScaledVector(forward, -speed);
            if (keys.d) camera.position.addScaledVector(right, speed);
            if (keys.a) camera.position.addScaledVector(right, -speed);
            if (keys.space) camera.position.y += speed;
            if (keys.shift && !keys.w && !keys.s && !keys.a && !keys.d) camera.position.y -= speed;
        }

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];
        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ mesh, type, color, emission, worldMatrix: mesh.matrixWorld.clone() });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.95, 0.95, 0.95]);

        // Floor (white)
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = -Math.PI / 2;
        addObject(floor, 'diffuse', [0.95, 0.95, 0.95]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.95, 0.95, 0.95]);

        // Area light
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Preview lights
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        pitch = 0; yaw = 0;
        camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(o => o.worldMatrix = o.mesh.matrixWorld.clone());

        // =============================================
        // Monte Carlo Progressive Path Tracer
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

        const totalCores = navigator.hardwareConcurrency || 4;
        //const numCores = Math.max(1, Math.floor(totalCores / 1));
        const numCores = navigator.hardwareConcurrency;
        document.getElementById('cores').textContent = numCores;
        document.getElementById('totalCores').textContent = totalCores;

        let workers = [];
        let isTracing = false;
        let totalSamples = 0;

        // Running accumulators (for stats / quality if needed)
        let accumBuffer = new Float32Array(width * height * 3);
        let sampleCountPerPixel = new Uint32Array(width * height);

        // Per-frame deltas (for display injection)
        let deltaAccumBuffer = new Float32Array(width * height * 3);
        let deltaCountPerPixel = new Uint32Array(width * height);

        // Display buffer with persistence (linear space)
        let displayBuffer = new Float32Array(width * height * 3);
        let imageData = ctx.createImageData(width, height);

        let lastSampleCount = 0;
        let lastTime = Date.now();
        let lastDisplayTS = performance.now();

        // Worker code
        const workerCode = `
            function intersectRay(origin, direction, objects) {
                let closest = null, minDist = Infinity;
                for (const obj of objects) {
                    const hit = intersectObject(origin, direction, obj);
                    if (hit && hit.distance < minDist) {
                        minDist = hit.distance;
                        closest = hit; closest.object = obj;
                    }
                }
                return closest;
            }

            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') return intersectSphere(origin, direction, obj);
                if (obj.geometry === 'plane')  return intersectPlane(origin, direction, obj);
                return null;
            }

            function intersectSphere(origin, direction, obj) {
                const c = obj.position, r = obj.radius;
                const oc = [origin[0]-c[0], origin[1]-c[1], origin[2]-c[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c2 = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - r*r;
                const disc = b*b - 4*a*c2;
                if (disc < 0) return null;
                const t = (-b - Math.sqrt(disc)) / (2*a);
                if (t < 0.001) return null;
                const p = [origin[0]+direction[0]*t, origin[1]+direction[1]*t, origin[2]+direction[2]*t];
                const n = [(p[0]-c[0])/r, (p[1]-c[1])/r, (p[2]-c[2])/r];
                return { distance: t, point: p, normal: n };
            }

            function intersectPlane(origin, direction, obj) {
                const n = obj.normal, p0 = obj.position;
                const denom = n[0]*direction[0] + n[1]*direction[1] + n[2]*direction[2];
                if (Math.abs(denom) < 1e-4) return null;
                const diff = [p0[0]-origin[0], p0[1]-origin[1], p0[2]-origin[2]];
                const t = (diff[0]*n[0] + diff[1]*n[1] + diff[2]*n[2]) / denom;
                if (t < 0.001) return null;

                const hp = [origin[0]+direction[0]*t, origin[1]+direction[1]*t, origin[2]+direction[2]*t];
                const lp = [hp[0]-p0[0], hp[1]-p0[1], hp[2]-p0[2]];
                const size = obj.size, u = obj.uAxis, v = obj.vAxis;

                const uCoord = lp[0]*u[0] + lp[1]*u[1] + lp[2]*u[2];
                const vCoord = lp[0]*v[0] + lp[1]*v[1] + lp[2]*v[2];
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;

                let finalN = n;
                if (denom > 0) finalN = [-n[0], -n[1], -n[2]];
                return { distance: t, point: hp, normal: finalN };
            }

            function rand() { return Math.random(); }
            function randomInUnitSphere() {
                while (true) {
                    const v = [rand()*2-1, rand()*2-1, rand()*2-1];
                    if (v[0]*v[0]+v[1]*v[1]+v[2]*v[2] < 1) return v;
                }
            }
            function randomInHemisphere(n) {
                const v = randomInUnitSphere();
                const d = v[0]*n[0]+v[1]*n[1]+v[2]*n[2];
                return (d > 0) ? v : [-v[0], -v[1], -v[2]];
            }
            function reflect(v, n) {
                const d = v[0]*n[0]+v[1]*n[1]+v[2]*n[2];
                return [v[0]-2*d*n[0], v[1]-2*d*n[1], v[2]-2*d*n[2]];
            }
            function norm(v){ const L=Math.hypot(v[0],v[1],v[2]); return L>0?[v[0]/L,v[1]/L,v[2]/L]:v; }

            function trace(o, d, depth, maxDepth, objs) {
                if (depth >= maxDepth) return [0,0,0];
                const hit = intersectRay(o, d, objs);
                if (!hit) return [0,0,0];

                const obj = hit.object, p = hit.point, n = hit.normal;
                const offs = 0.001;
                const po = [p[0]+n[0]*offs, p[1]+n[1]*offs, p[2]+n[2]*offs];

                if (obj.type === 'emissive') return obj.emission;

                const albedo = obj.color;
                if (obj.type === 'reflective') {
                    const nd = norm( reflect(d, n) );
                    const inc = trace(po, nd, depth+1, maxDepth, objs);
                    return [albedo[0]*inc[0], albedo[1]*inc[1], albedo[2]*inc[2]];
                } else {
                    const nd = norm( randomInHemisphere(n) );
                    const cosT = Math.max(0, nd[0]*n[0]+nd[1]*n[1]+nd[2]*n[2]);
                    const inc = trace(po, nd, depth+1, maxDepth, objs);
                    const scale = 2.0 * cosT;
                    return [albedo[0]*inc[0]*scale, albedo[1]*inc[1]*scale, albedo[2]*inc[2]*scale];
                }
            }

            self.onmessage = function(e) {
                const { camera, objects, samplesPerBatch, maxBounces, width, height, pixelSize } = e.data;
                const out = [];
                const gridW = Math.ceil(width / pixelSize);
                const gridH = Math.ceil(height / pixelSize);

                for (let s = 0; s < samplesPerBatch; s++) {
                    const gx = Math.floor(Math.random() * gridW);
                    const gy = Math.floor(Math.random() * gridH);
                    const x = gx * pixelSize;
                    const y = gy * pixelSize;

                    const u = (x + Math.random() * pixelSize) / width;
                    const v = (y + Math.random() * pixelSize) / height;

                    const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                    const py = -(v * 2 - 1) * camera.tanFov;

                    let dir = [px, py, -1];
                    const L = Math.hypot(dir[0], dir[1], dir[2]);
                    dir = [dir[0]/L, dir[1]/L, dir[2]/L];

                    const q = camera.quaternion;
                    const r = rotateByQuaternion(dir, q);

                    const col = trace(camera.position, r, 0, maxBounces, objects);
                    out.push({ x, y, pixelSize, color: col });
                }
                self.postMessage({ sampleData: out });
            };

            function rotateByQuaternion(v, q) {
                const qx=q[0], qy=q[1], qz=q[2], qw=q[3];
                const x=v[0], y=v[1], z=v[2];
                const ix = qw*x + qy*z - qz*y;
                const iy = qw*y + qz*x - qx*z;
                const iz = qw*z + qx*y - qy*x;
                const iw = -qx*x - qy*y - qz*z;
                return [
                    ix*qw + iw*-qx + iy*-qz - iz*-qy,
                    iy*qw + iw*-qy + iz*-qx - ix*-qz,
                    iz*qw + iw*-qz + ix*-qy - iy*-qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            for (let i = 0; i < numCores; i++) {
                const w = new Worker(workerUrl);
                w.onmessage = handleWorkerResult;
                w.idle = true;
                workers.push(w);
            }
        }

        function serializeObjects() {
            const serialized = [];
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1).applyQuaternion(mesh.quaternion).normalize();
                    const uAxis  = new THREE.Vector3(1, 0, 0).applyQuaternion(mesh.quaternion).normalize();
                    const vAxis  = new THREE.Vector3(0, 1, 0).applyQuaternion(mesh.quaternion).normalize();
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            return serialized;
        }

        // Handle worker results: update both global accumulators AND per-frame deltas
        function handleWorkerResult(e) {
            const { sampleData } = e.data;

            for (const sample of sampleData) {
                const ps = sample.pixelSize;
                for (let dy = 0; dy < ps && sample.y + dy < height; dy++) {
                    for (let dx = 0; dx < ps && sample.x + dx < width; dx++) {
                        const px = sample.x + dx;
                        const py = sample.y + dy;
                        const pIdx = py * width + px;
                        const i3 = pIdx * 3;

                        // Global running accumulation
                        accumBuffer[i3    ] += sample.color[0];
                        accumBuffer[i3 + 1] += sample.color[1];
                        accumBuffer[i3 + 2] += sample.color[2];
                        sampleCountPerPixel[pIdx]++;

                        // Per-frame deltas (only what arrived since last display)
                        deltaAccumBuffer[i3    ] += sample.color[0];
                        deltaAccumBuffer[i3 + 1] += sample.color[1];
                        deltaAccumBuffer[i3 + 2] += sample.color[2];
                        deltaCountPerPixel[pIdx]++;
                    }
                }
            }

            totalSamples += sampleData.length;

            e.target.idle = true;
            if (isTracing) assignWork(e.target);
        }

        // Persistence-of-vision display update:
        // decay old display by time; inject only NEW contributions; clear deltas.
        function updateDisplay() {
            const nowPerf = performance.now();
            const dt = Math.max(0.0, (nowPerf - lastDisplayTS) / 1000.0);
            lastDisplayTS = nowPerf;

            const halfLife = Math.max(0.05, parseFloat(document.getElementById('fadeHalfLife').value) || 0.75);
            const decay = Math.pow(0.5, dt / halfLife);
            const oneMinus = 1.0 - decay;

            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    const pIdx = y * width + x;
                    const i3 = pIdx * 3;
                    const img = pIdx * 4;

                    // 1) Decay previous display state
                    let dr = displayBuffer[i3    ] * decay;
                    let dg = displayBuffer[i3 + 1] * decay;
                    let db = displayBuffer[i3 + 2] * decay;

                    // 2) Add only new samples since last frame (average of deltas)
                    const dcnt = deltaCountPerPixel[pIdx];
                    if (dcnt > 0) {
                        const inv = 1.0 / dcnt;
                        const nr = deltaAccumBuffer[i3    ] * inv;
                        const ng = deltaAccumBuffer[i3 + 1] * inv;
                        const nb = deltaAccumBuffer[i3 + 2] * inv;

                        dr += nr * oneMinus;
                        dg += ng * oneMinus;
                        db += nb * oneMinus;

                        // Clear consumed deltas
                        deltaAccumBuffer[i3    ] = 0;
                        deltaAccumBuffer[i3 + 1] = 0;
                        deltaAccumBuffer[i3 + 2] = 0;
                        deltaCountPerPixel[pIdx] = 0;
                    }

                    displayBuffer[i3    ] = dr;
                    displayBuffer[i3 + 1] = dg;
                    displayBuffer[i3 + 2] = db;

                    // Gamma → sRGB-ish
                    const gr = Math.pow(Math.max(0, dr), 1/2.2);
                    const gg = Math.pow(Math.max(0, dg), 1/2.2);
                    const gb = Math.pow(Math.max(0, db), 1/2.2);

                    imageData.data[img    ] = Math.min(255, gr * 255);
                    imageData.data[img + 1] = Math.min(255, gg * 255);
                    imageData.data[img + 2] = Math.min(255, gb * 255);
                    imageData.data[img + 3] = 255;
                }
            }

            ctx.putImageData(imageData, 0, 0);

            // Stats UI
            const nowMs = Date.now();
            const elapsed = (nowMs - lastTime) / 1000;
            if (elapsed > 1.0) {
                const sps = Math.floor((totalSamples - lastSampleCount) / elapsed);
                document.getElementById('sps').textContent = sps.toLocaleString();
                lastSampleCount = totalSamples;
                lastTime = nowMs;
            }
            document.getElementById('samples').textContent = totalSamples;
        }

        function assignWork(worker) {
            if (!isTracing) return;
            worker.idle = false;

            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };

            const pixelSize = parseInt(document.getElementById('pixelSize').value);
            worker.postMessage({
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerBatch: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width, height, pixelSize
            });
        }

        function startRendering() {
            isTracing = true;
            initWorkers();
            lastTime = Date.now();
            lastSampleCount = 0;
            lastDisplayTS = performance.now();
            workers.forEach(w => assignWork(w));
        }
        function stopRendering() { isTracing = false; }

        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);

            accumBuffer = new Float32Array(width * height * 3);
            sampleCountPerPixel = new Uint32Array(width * height);

            deltaAccumBuffer = new Float32Array(width * height * 3);
            deltaCountPerPixel = new Uint32Array(width * height);

            displayBuffer = new Float32Array(width * height * 3);

            totalSamples = 0;
            lastSampleCount = 0;
            lastTime = Date.now();
            lastDisplayTS = performance.now();
            document.getElementById('samples').textContent = '0';
            document.getElementById('sps').textContent = '0';
        }

        // Controls
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (totalSamples === 0) startRendering();
                else {
                    isTracing = true;
                    lastDisplayTS = performance.now();
                    workers.filter(w => w.idle).forEach(w => assignWork(w));
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });
        document.getElementById('reset').addEventListener('click', resetRendering);

        // Animation Loop
        let frameCount = 0;
        function animate() {
            requestAnimationFrame(animate);
            updateMovement();
            renderer.render(scene, camera);

            // Update display regularly EVEN IF paused (so it fades out)
            if (frameCount++ % 2 === 0) updateDisplay();
        }
        animate();

        // Resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### multinucleo

```html
<!DOCTYPE html>
<html>
<head>
    <title>Monte Carlo Path Tracer - Cornell Box (POV Fade)</title>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; }
        #canvas3d { position: absolute; top: 0; left: 0; }
        #canvasPT { position: absolute; top: 0; left: 0; }
        #controls { 
            position: absolute; 
            top: 10px; 
            left: 10px; 
            background: rgba(0,0,0,0.7); 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 12px;
            max-width: 260px;
            line-height: 1.4;
            user-select: none;
        }
        button { margin: 5px 0; padding: 5px 10px; cursor: pointer; }
        label { display: block; margin-top: 6px; }
        input[type="number"] { width: 90px; }
    </style>
</head>
<body>
    <canvas id="canvas3d"></canvas>
    <canvas id="canvasPT"></canvas>
    <div id="controls">
        <div><strong>Monte Carlo Path Tracer</strong></div>
        <div>Cores Used: <span id="cores">0</span> / <span id="totalCores">0</span></div>
        <div>Total Samples: <span id="samples">0</span></div>
        <div>Samples/sec: <span id="sps">0</span></div>
        <button id="togglePT">Start Path Tracing</button>
        <button id="reset">Reset</button>
        <label>
            Pixel Size:
            <input type="number" id="pixelSize" value="2" min="1" max="16">
            <span style="font-size: 10px; color: #aaa;">(1=full quality, 4=4x faster)</span>
        </label>
        <label>
            Samples/Frame:
            <input type="number" id="spp" value="1000" min="100" max="10000">
        </label>
        <label>
            Max Bounces:
            <input type="number" id="bounces" value="5" min="1" max="10">
        </label>
        <label>
            Fade Half-Life (s):
            <input type="number" id="fadeHalfLife" value="20" step="0.05" min="0.05" max="20">
        </label>
        <div style="margin-top: 6px; font-size: 11px; color: #aaa;">
            Click to enable FPS controls<br>
            WASD: Move | Mouse: Look<br>
            Space: Up | Shift: Down/Sprint<br>
            POV fading is time-based (exponential)
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
    <script>
        // =============================================
        // Three.js Scene Setup
        // =============================================
        const canvas3d = document.getElementById('canvas3d');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: canvas3d, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const controls = new THREE.OrbitControls(camera, canvas3d);
        controls.enableDamping = true;
        controls.enabled = false; // FPS controls instead

        // =============================================
        // FPS Controls
        // =============================================
        const moveSpeed = 0.05;
        const mouseSensitivity = 0.002;
        const keys = { w: false, a: false, s: false, d: false, shift: false, space: false };
        let pitch = 0;
        let yaw = 0;
        let isPointerLocked = false;

        // Pointer lock
        document.body.addEventListener('click', () => {
            if (!isPointerLocked) document.body.requestPointerLock();
        });
        document.addEventListener('pointerlockchange', () => {
            isPointerLocked = document.pointerLockElement === document.body;
        });

        // Mouse movement
        document.addEventListener('mousemove', (e) => {
            if (!isPointerLocked) return;
            yaw -= e.movementX * mouseSensitivity;
            pitch -= e.movementY * mouseSensitivity;
            pitch = Math.max(-Math.PI / 2 + 0.01, Math.min(Math.PI / 2 - 0.01, pitch));
            const euler = new THREE.Euler(pitch, yaw, 0, 'YXZ');
            camera.quaternion.setFromEuler(euler);
        });

        // Keyboard input
        document.addEventListener('keydown', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) { keys[key] = true; e.preventDefault(); }
        });
        document.addEventListener('keyup', (e) => {
            const key = e.key.toLowerCase();
            if (keys.hasOwnProperty(key)) { keys[key] = false; e.preventDefault(); }
        });

        function updateMovement() {
            const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(camera.quaternion);
            forward.y = 0; forward.normalize();
            const right = new THREE.Vector3(1, 0, 0).applyQuaternion(camera.quaternion);
            right.y = 0; right.normalize();
            const speed = keys.shift && (keys.w || keys.s || keys.a || keys.d) ? moveSpeed * 2 : moveSpeed;

            if (keys.w) camera.position.addScaledVector(forward, speed);
            if (keys.s) camera.position.addScaledVector(forward, -speed);
            if (keys.d) camera.position.addScaledVector(right, speed);
            if (keys.a) camera.position.addScaledVector(right, -speed);
            if (keys.space) camera.position.y += speed;
            if (keys.shift && !keys.w && !keys.s && !keys.a && !keys.d) camera.position.y -= speed;
        }

        // =============================================
        // Cornell Box Geometry
        // =============================================
        const boxSize = 5;
        const sceneObjects = [];
        function addObject(mesh, type, color, emission = null) {
            scene.add(mesh);
            sceneObjects.push({ mesh, type, color, emission, worldMatrix: mesh.matrixWorld.clone() });
        }

        // Left wall (red)
        const leftWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xff0000, side: THREE.DoubleSide })
        );
        leftWall.position.set(-boxSize/2, 0, 0);
        leftWall.rotation.y = Math.PI / 2;
        addObject(leftWall, 'diffuse', [1, 0, 0]);

        // Right wall (green)
        const rightWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide })
        );
        rightWall.position.set(boxSize/2, 0, 0);
        rightWall.rotation.y = -Math.PI / 2;
        addObject(rightWall, 'diffuse', [0, 1, 0]);

        // Back wall (white)
        const backWall = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        backWall.position.set(0, 0, -boxSize/2);
        addObject(backWall, 'diffuse', [0.95, 0.95, 0.95]);

        // Floor (white)
        const floor = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        floor.position.set(0, -boxSize/2, 0);
        floor.rotation.x = -Math.PI / 2;
        addObject(floor, 'diffuse', [0.95, 0.95, 0.95]);

        // Ceiling (white)
        const ceiling = new THREE.Mesh(
            new THREE.PlaneGeometry(boxSize, boxSize),
            new THREE.MeshLambertMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        ceiling.position.set(0, boxSize/2, 0);
        ceiling.rotation.x = -Math.PI / 2;
        addObject(ceiling, 'diffuse', [0.95, 0.95, 0.95]);

        // Area light
        const lightSize = 1.5;
        const light = new THREE.Mesh(
            new THREE.PlaneGeometry(lightSize, lightSize),
            new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide })
        );
        light.position.set(0, boxSize/2 - 0.05, 0);
        light.rotation.x = -Math.PI / 2;
        addObject(light, 'emissive', [1, 1, 1], [20, 20, 20]);

        // Sphere 1 (diffuse)
        const sphere1 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshLambertMaterial({ color: 0xffffff })
        );
        sphere1.position.set(-1.2, -boxSize/2 + 0.7, 0.5);
        addObject(sphere1, 'diffuse', [0.9, 0.9, 0.9]);

        // Sphere 2 (reflective)
        const sphere2 = new THREE.Mesh(
            new THREE.SphereGeometry(0.7, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xffffff, shininess: 100 })
        );
        sphere2.position.set(1.2, -boxSize/2 + 0.7, -0.5);
        addObject(sphere2, 'reflective', [0.95, 0.95, 0.95]);

        // Preview lights
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(0, boxSize/2 - 0.5, 0);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.set(0, 0, 8);
        pitch = 0; yaw = 0;
        camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));
        scene.updateMatrixWorld(true);
        sceneObjects.forEach(o => o.worldMatrix = o.mesh.matrixWorld.clone());

        // =============================================
        // Monte Carlo Progressive Path Tracer
        // =============================================
        const canvasPT = document.getElementById('canvasPT');
        const ctx = canvasPT.getContext('2d');
        let width = window.innerWidth;
        let height = window.innerHeight;
        canvasPT.width = width;
        canvasPT.height = height;

         const totalCores = navigator.hardwareConcurrency || 4;
        const numCores = totalCores;
        document.getElementById('cores').textContent = numCores;
        document.getElementById('totalCores').textContent = totalCores;

        let workers = [];
        let isTracing = false;
        let totalSamples = 0;

        // Running accumulators (for stats / quality if needed)
        let accumBuffer = new Float32Array(width * height * 3);
        let sampleCountPerPixel = new Uint32Array(width * height);

        // Per-frame deltas (for display injection)
        let deltaAccumBuffer = new Float32Array(width * height * 3);
        let deltaCountPerPixel = new Uint32Array(width * height);

        // Display buffer with persistence (linear space)
        let displayBuffer = new Float32Array(width * height * 3);
        let imageData = ctx.createImageData(width, height);

        let lastSampleCount = 0;
        let lastTime = Date.now();
        let lastDisplayTS = performance.now();

        // Worker code
        const workerCode = `
            function intersectRay(origin, direction, objects) {
                let closest = null, minDist = Infinity;
                for (const obj of objects) {
                    const hit = intersectObject(origin, direction, obj);
                    if (hit && hit.distance < minDist) {
                        minDist = hit.distance;
                        closest = hit; closest.object = obj;
                    }
                }
                return closest;
            }

            function intersectObject(origin, direction, obj) {
                if (obj.geometry === 'sphere') return intersectSphere(origin, direction, obj);
                if (obj.geometry === 'plane')  return intersectPlane(origin, direction, obj);
                return null;
            }

            function intersectSphere(origin, direction, obj) {
                const c = obj.position, r = obj.radius;
                const oc = [origin[0]-c[0], origin[1]-c[1], origin[2]-c[2]];
                const a = direction[0]*direction[0] + direction[1]*direction[1] + direction[2]*direction[2];
                const b = 2.0 * (oc[0]*direction[0] + oc[1]*direction[1] + oc[2]*direction[2]);
                const c2 = oc[0]*oc[0] + oc[1]*oc[1] + oc[2]*oc[2] - r*r;
                const disc = b*b - 4*a*c2;
                if (disc < 0) return null;
                const t = (-b - Math.sqrt(disc)) / (2*a);
                if (t < 0.001) return null;
                const p = [origin[0]+direction[0]*t, origin[1]+direction[1]*t, origin[2]+direction[2]*t];
                const n = [(p[0]-c[0])/r, (p[1]-c[1])/r, (p[2]-c[2])/r];
                return { distance: t, point: p, normal: n };
            }

            function intersectPlane(origin, direction, obj) {
                const n = obj.normal, p0 = obj.position;
                const denom = n[0]*direction[0] + n[1]*direction[1] + n[2]*direction[2];
                if (Math.abs(denom) < 1e-4) return null;
                const diff = [p0[0]-origin[0], p0[1]-origin[1], p0[2]-origin[2]];
                const t = (diff[0]*n[0] + diff[1]*n[1] + diff[2]*n[2]) / denom;
                if (t < 0.001) return null;

                const hp = [origin[0]+direction[0]*t, origin[1]+direction[1]*t, origin[2]+direction[2]*t];
                const lp = [hp[0]-p0[0], hp[1]-p0[1], hp[2]-p0[2]];
                const size = obj.size, u = obj.uAxis, v = obj.vAxis;

                const uCoord = lp[0]*u[0] + lp[1]*u[1] + lp[2]*u[2];
                const vCoord = lp[0]*v[0] + lp[1]*v[1] + lp[2]*v[2];
                if (Math.abs(uCoord) > size/2 || Math.abs(vCoord) > size/2) return null;

                let finalN = n;
                if (denom > 0) finalN = [-n[0], -n[1], -n[2]];
                return { distance: t, point: hp, normal: finalN };
            }

            function rand() { return Math.random(); }
            function randomInUnitSphere() {
                while (true) {
                    const v = [rand()*2-1, rand()*2-1, rand()*2-1];
                    if (v[0]*v[0]+v[1]*v[1]+v[2]*v[2] < 1) return v;
                }
            }
            function randomInHemisphere(n) {
                const v = randomInUnitSphere();
                const d = v[0]*n[0]+v[1]*n[1]+v[2]*n[2];
                return (d > 0) ? v : [-v[0], -v[1], -v[2]];
            }
            function reflect(v, n) {
                const d = v[0]*n[0]+v[1]*n[1]+v[2]*n[2];
                return [v[0]-2*d*n[0], v[1]-2*d*n[1], v[2]-2*d*n[2]];
            }
            function norm(v){ const L=Math.hypot(v[0],v[1],v[2]); return L>0?[v[0]/L,v[1]/L,v[2]/L]:v; }

            function trace(o, d, depth, maxDepth, objs) {
                if (depth >= maxDepth) return [0,0,0];
                const hit = intersectRay(o, d, objs);
                if (!hit) return [0,0,0];

                const obj = hit.object, p = hit.point, n = hit.normal;
                const offs = 0.001;
                const po = [p[0]+n[0]*offs, p[1]+n[1]*offs, p[2]+n[2]*offs];

                if (obj.type === 'emissive') return obj.emission;

                const albedo = obj.color;
                if (obj.type === 'reflective') {
                    const nd = norm( reflect(d, n) );
                    const inc = trace(po, nd, depth+1, maxDepth, objs);
                    return [albedo[0]*inc[0], albedo[1]*inc[1], albedo[2]*inc[2]];
                } else {
                    const nd = norm( randomInHemisphere(n) );
                    const cosT = Math.max(0, nd[0]*n[0]+nd[1]*n[1]+nd[2]*n[2]);
                    const inc = trace(po, nd, depth+1, maxDepth, objs);
                    const scale = 2.0 * cosT;
                    return [albedo[0]*inc[0]*scale, albedo[1]*inc[1]*scale, albedo[2]*inc[2]*scale];
                }
            }

            self.onmessage = function(e) {
                const { camera, objects, samplesPerBatch, maxBounces, width, height, pixelSize } = e.data;
                const out = [];
                const gridW = Math.ceil(width / pixelSize);
                const gridH = Math.ceil(height / pixelSize);

                for (let s = 0; s < samplesPerBatch; s++) {
                    const gx = Math.floor(Math.random() * gridW);
                    const gy = Math.floor(Math.random() * gridH);
                    const x = gx * pixelSize;
                    const y = gy * pixelSize;

                    const u = (x + Math.random() * pixelSize) / width;
                    const v = (y + Math.random() * pixelSize) / height;

                    const px = (u * 2 - 1) * camera.tanFov * camera.aspect;
                    const py = -(v * 2 - 1) * camera.tanFov;

                    let dir = [px, py, -1];
                    const L = Math.hypot(dir[0], dir[1], dir[2]);
                    dir = [dir[0]/L, dir[1]/L, dir[2]/L];

                    const q = camera.quaternion;
                    const r = rotateByQuaternion(dir, q);

                    const col = trace(camera.position, r, 0, maxBounces, objects);
                    out.push({ x, y, pixelSize, color: col });
                }
                self.postMessage({ sampleData: out });
            };

            function rotateByQuaternion(v, q) {
                const qx=q[0], qy=q[1], qz=q[2], qw=q[3];
                const x=v[0], y=v[1], z=v[2];
                const ix = qw*x + qy*z - qz*y;
                const iy = qw*y + qz*x - qx*z;
                const iz = qw*z + qx*y - qy*x;
                const iw = -qx*x - qy*y - qz*z;
                return [
                    ix*qw + iw*-qx + iy*-qz - iz*-qy,
                    iy*qw + iw*-qy + iz*-qx - ix*-qz,
                    iz*qw + iw*-qz + ix*-qy - iy*-qx
                ];
            }
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        const workerUrl = URL.createObjectURL(blob);

        function initWorkers() {
            workers.forEach(w => w.terminate());
            workers = [];
            for (let i = 0; i < numCores; i++) {
                const w = new Worker(workerUrl);
                w.onmessage = handleWorkerResult;
                w.idle = true;
                workers.push(w);
            }
        }

        function serializeObjects() {
            const serialized = [];
            for (const obj of sceneObjects) {
                const mesh = obj.mesh;
                if (mesh.geometry.type === 'SphereGeometry') {
                    serialized.push({
                        geometry: 'sphere',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        radius: mesh.geometry.parameters.radius,
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                } else if (mesh.geometry.type === 'PlaneGeometry') {
                    const normal = new THREE.Vector3(0, 0, 1).applyQuaternion(mesh.quaternion).normalize();
                    const uAxis  = new THREE.Vector3(1, 0, 0).applyQuaternion(mesh.quaternion).normalize();
                    const vAxis  = new THREE.Vector3(0, 1, 0).applyQuaternion(mesh.quaternion).normalize();
                    serialized.push({
                        geometry: 'plane',
                        position: [mesh.position.x, mesh.position.y, mesh.position.z],
                        normal: [normal.x, normal.y, normal.z],
                        uAxis: [uAxis.x, uAxis.y, uAxis.z],
                        vAxis: [vAxis.x, vAxis.y, vAxis.z],
                        size: Math.max(mesh.geometry.parameters.width, mesh.geometry.parameters.height),
                        type: obj.type,
                        color: obj.color,
                        emission: obj.emission
                    });
                }
            }
            return serialized;
        }

        // Handle worker results: update both global accumulators AND per-frame deltas
        function handleWorkerResult(e) {
            const { sampleData } = e.data;

            for (const sample of sampleData) {
                const ps = sample.pixelSize;
                for (let dy = 0; dy < ps && sample.y + dy < height; dy++) {
                    for (let dx = 0; dx < ps && sample.x + dx < width; dx++) {
                        const px = sample.x + dx;
                        const py = sample.y + dy;
                        const pIdx = py * width + px;
                        const i3 = pIdx * 3;

                        // Global running accumulation
                        accumBuffer[i3    ] += sample.color[0];
                        accumBuffer[i3 + 1] += sample.color[1];
                        accumBuffer[i3 + 2] += sample.color[2];
                        sampleCountPerPixel[pIdx]++;

                        // Per-frame deltas (only what arrived since last display)
                        deltaAccumBuffer[i3    ] += sample.color[0];
                        deltaAccumBuffer[i3 + 1] += sample.color[1];
                        deltaAccumBuffer[i3 + 2] += sample.color[2];
                        deltaCountPerPixel[pIdx]++;
                    }
                }
            }

            totalSamples += sampleData.length;

            // IMMEDIATELY assign new work to keep worker busy
            if (isTracing) assignWork(e.target);
        }

        // Persistence-of-vision display update:
        // decay old display by time; inject only NEW contributions; clear deltas.
        function updateDisplay() {
            const nowPerf = performance.now();
            const dt = Math.max(0.0, (nowPerf - lastDisplayTS) / 1000.0);
            lastDisplayTS = nowPerf;

            const halfLife = Math.max(0.05, parseFloat(document.getElementById('fadeHalfLife').value) || 0.75);
            const decay = Math.pow(0.5, dt / halfLife);
            const oneMinus = 1.0 - decay;

            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    const pIdx = y * width + x;
                    const i3 = pIdx * 3;
                    const img = pIdx * 4;

                    // 1) Decay previous display state
                    let dr = displayBuffer[i3    ] * decay;
                    let dg = displayBuffer[i3 + 1] * decay;
                    let db = displayBuffer[i3 + 2] * decay;

                    // 2) Add only new samples since last frame (average of deltas)
                    const dcnt = deltaCountPerPixel[pIdx];
                    if (dcnt > 0) {
                        const inv = 1.0 / dcnt;
                        const nr = deltaAccumBuffer[i3    ] * inv;
                        const ng = deltaAccumBuffer[i3 + 1] * inv;
                        const nb = deltaAccumBuffer[i3 + 2] * inv;

                        dr += nr * oneMinus;
                        dg += ng * oneMinus;
                        db += nb * oneMinus;

                        // Clear consumed deltas
                        deltaAccumBuffer[i3    ] = 0;
                        deltaAccumBuffer[i3 + 1] = 0;
                        deltaAccumBuffer[i3 + 2] = 0;
                        deltaCountPerPixel[pIdx] = 0;
                    }

                    displayBuffer[i3    ] = dr;
                    displayBuffer[i3 + 1] = dg;
                    displayBuffer[i3 + 2] = db;

                    // Gamma → sRGB-ish
                    const gr = Math.pow(Math.max(0, dr), 1/2.2);
                    const gg = Math.pow(Math.max(0, dg), 1/2.2);
                    const gb = Math.pow(Math.max(0, db), 1/2.2);

                    imageData.data[img    ] = Math.min(255, gr * 255);
                    imageData.data[img + 1] = Math.min(255, gg * 255);
                    imageData.data[img + 2] = Math.min(255, gb * 255);
                    imageData.data[img + 3] = 255;
                }
            }

            ctx.putImageData(imageData, 0, 0);

            // Stats UI
            const nowMs = Date.now();
            const elapsed = (nowMs - lastTime) / 1000;
            if (elapsed > 1.0) {
                const sps = Math.floor((totalSamples - lastSampleCount) / elapsed);
                document.getElementById('sps').textContent = sps.toLocaleString();
                lastSampleCount = totalSamples;
                lastTime = nowMs;
            }
            document.getElementById('samples').textContent = totalSamples;
        }

        function assignWork(worker) {
            if (!isTracing) return;
            worker.idle = false;

            const cameraData = {
                position: [camera.position.x, camera.position.y, camera.position.z],
                quaternion: [camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
                tanFov: Math.tan(camera.fov * Math.PI / 360),
                aspect: camera.aspect
            };

            const pixelSize = parseInt(document.getElementById('pixelSize').value);
            worker.postMessage({
                camera: cameraData,
                objects: serializeObjects(),
                samplesPerBatch: parseInt(document.getElementById('spp').value),
                maxBounces: parseInt(document.getElementById('bounces').value),
                width, height, pixelSize
            });
        }

        function startRendering() {
            isTracing = true;
            initWorkers();
            lastTime = Date.now();
            lastSampleCount = 0;
            lastDisplayTS = performance.now();
            workers.forEach(w => assignWork(w));
        }
        function stopRendering() { isTracing = false; }

        function resetRendering() {
            stopRendering();
            ctx.clearRect(0, 0, width, height);
            imageData = ctx.createImageData(width, height);

            accumBuffer = new Float32Array(width * height * 3);
            sampleCountPerPixel = new Uint32Array(width * height);

            deltaAccumBuffer = new Float32Array(width * height * 3);
            deltaCountPerPixel = new Uint32Array(width * height);

            displayBuffer = new Float32Array(width * height * 3);

            totalSamples = 0;
            lastSampleCount = 0;
            lastTime = Date.now();
            lastDisplayTS = performance.now();
            document.getElementById('samples').textContent = '0';
            document.getElementById('sps').textContent = '0';
        }

        // Controls
        document.getElementById('togglePT').addEventListener('click', () => {
            if (isTracing) {
                stopRendering();
                document.getElementById('togglePT').textContent = 'Resume Path Tracing';
            } else {
                if (totalSamples === 0) startRendering();
                else {
                    isTracing = true;
                    lastDisplayTS = performance.now();
                    workers.filter(w => w.idle).forEach(w => assignWork(w));
                }
                document.getElementById('togglePT').textContent = 'Pause Path Tracing';
            }
        });
        document.getElementById('reset').addEventListener('click', resetRendering);

        // Animation Loop
        let frameCount = 0;
        function animate() {
            requestAnimationFrame(animate);
            updateMovement();
            renderer.render(scene, camera);

            // Update display regularly EVEN IF paused (so it fades out)
            if (frameCount++ % 2 === 0) updateDisplay();
        }
        animate();

        // Resize
        window.addEventListener('resize', () => {
            width = window.innerWidth;
            height = window.innerHeight;
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
            canvasPT.width = width;
            canvasPT.height = height;
            resetRendering();
        });
    </script>
</body>
</html>
```

### superbuckets

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Path Tracer — 4×4 Tiles, Multicore, Low-RAM + Direct Light Sampling</title>
  <style>
    body { margin:0; overflow:hidden; font-family:Arial, sans-serif; }
    #canvas3d, #canvasPT { position:absolute; top:0; left:0; }
    #controls{
      position:absolute; top:10px; left:10px;
      background:rgba(0,0,0,.7); color:#fff; padding:10px; border-radius:6px;
      font-size:12px; max-width:360px; line-height:1.4; user-select:none;
    }
    label{display:block; margin-top:6px}
    input[type="number"]{width:90px}
    button{margin:6px 0; padding:6px 10px; cursor:pointer}
  </style>
</head>
<body>
  <canvas id="canvas3d"></canvas>
  <canvas id="canvasPT"></canvas>

  <div id="controls">
    <div><strong>Monte Carlo Path Tracer (NEE)</strong></div>
    <div>Cores (Workers): <input type="number" id="workers" value="16" min="1" max="64"> <span style="opacity:.7">/ tiles: 16</span></div>
    <div>OS hints (hardwareConcurrency): <span id="hwc">?</span></div>
    <div>Total Patches: <span id="samples">0</span></div>
    <div>Patches/sec: <span id="sps">0</span></div>

    <button id="togglePT">Start Path Tracing</button>
    <button id="reset">Reset</button>

    <label>Pixel Size:
      <input type="number" id="pixelSize" value="2" min="1" max="16">
      <span style="font-size:10px; color:#aaa">(1 = full quality)</span>
    </label>
    <label>Samples/Batch (per worker tick):
      <input type="number" id="spp" value="2000" min="50" max="50000">
    </label>
    <label>Max Bounces:
      <input type="number" id="bounces" value="6" min="1" max="10">
    </label>
    <label>Fade Half-Life (s):
      <input type="number" id="fadeHalfLife" value="20" step="0.05" min="0.05" max="60">
    </label>

    <div style="margin-top:6px; font-size:11px; color:#aaa">
      Click to enable FPS controls. <b>W</b>=forward, <b>S</b>=backward, <b>A</b>=left, <b>D</b>=right. Space=up, Shift=sprint (or down if no move).
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
  <script>
    // ---------- Basic scene ----------
    const canvas3d = document.getElementById('canvas3d');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(50, innerWidth/innerHeight, 0.01, 1000);
    const renderer = new THREE.WebGLRenderer({canvas: canvas3d, antialias:true});
    renderer.setSize(innerWidth, innerHeight);
    const orbit = new THREE.OrbitControls(camera, canvas3d); orbit.enabled = false;

    // FPS controls (WASD)
    const keys = { w:false, a:false, s:false, d:false, shift:false, space:false };
    let pitch=0, yaw=0, locked=false;
    const mouseSensitivity=0.002, moveSpeed=0.04;

    document.body.addEventListener('click', ()=>{ if(!locked) document.body.requestPointerLock(); });
    document.addEventListener('pointerlockchange', ()=> locked = document.pointerLockElement===document.body);
    window.addEventListener('keydown', e=>{ const k=e.key.toLowerCase(); if(k in keys){keys[k]=true; e.preventDefault();}});
    window.addEventListener('keyup',   e=>{ const k=e.key.toLowerCase(); if(k in keys){keys[k]=false; e.preventDefault();}});
    window.addEventListener('mousemove', e=>{
      if(!locked) return;
      yaw   -= e.movementX * mouseSensitivity;
      pitch -= e.movementY * mouseSensitivity;
      pitch = Math.max(-Math.PI/2+0.01, Math.min(Math.PI/2-0.01, pitch));
      camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));
    });

    function updateMovement(){
      const forward = new THREE.Vector3(0,0,-1).applyQuaternion(camera.quaternion).normalize();
      const right   = new THREE.Vector3(1,0,0).applyQuaternion(camera.quaternion).normalize();
      const speed = keys.shift && (keys.w||keys.a||keys.s||keys.d) ? moveSpeed*2 : moveSpeed;

      if (keys.w) camera.position.addScaledVector(forward,  speed);
      if (keys.s) camera.position.addScaledVector(forward, -speed);
      if (keys.d) camera.position.addScaledVector(right,    speed);
      if (keys.a) camera.position.addScaledVector(right,   -speed);
      if (keys.space) camera.position.y += speed;
      if (keys.shift && !(keys.w||keys.a||keys.s||keys.d)) camera.position.y -= speed; // "down" only when not moving
    }

    // ---------- Cornell Box geometry ----------
    const boxSize=5, half=boxSize/2, objs=[];
    function add(mesh, type, color, emission=null){ scene.add(mesh); objs.push({mesh, type, color, emission}); }
    const mkPlane=(w,h,color)=> new THREE.Mesh(new THREE.PlaneGeometry(w,h), new THREE.MeshLambertMaterial({color, side:THREE.DoubleSide}));
    const mkSphere=(r,mat)=> new THREE.Mesh(new THREE.SphereGeometry(r,32,32), mat);

    // Left, Right, Back, Floor, Ceiling. Front is open.
    const left = mkPlane(boxSize,boxSize,0xff0000); left.position.set(-half,0,0); left.rotation.y=Math.PI/2; add(left,'diffuse',[1,0,0]);
    const right= mkPlane(boxSize,boxSize,0x00ff00); right.position.set( half,0,0); right.rotation.y=-Math.PI/2; add(right,'diffuse',[0,1,0]);
    const back = mkPlane(boxSize,boxSize,0xffffff); back.position.set(0,0,-half); add(back,'diffuse',[0.95,0.95,0.95]);
    const floor= mkPlane(boxSize,boxSize,0xffffff); floor.position.set(0,-half,0); floor.rotation.x=-Math.PI/2; add(floor,'diffuse',[0.95,0.95,0.95]);
    const ceil = mkPlane(boxSize,boxSize,0xffffff); ceil.position.set(0, half,0); ceil.rotation.x=-Math.PI/2; add(ceil,'diffuse',[0.95,0.95,0.95]);

    // Area light
    const lightSize=1.6;
    const lamp = new THREE.Mesh(new THREE.PlaneGeometry(lightSize, lightSize), new THREE.MeshBasicMaterial({color:0xffffff, side:THREE.DoubleSide}));
    lamp.position.set(0, half-0.05, 0); lamp.rotation.x=-Math.PI/2;
    add(lamp,'emissive',[1,1,1],[40,40,40]); // strong emission to converge faster

    // Spheres
    const s1 = mkSphere(0.7, new THREE.MeshLambertMaterial({color:0xffffff})); s1.position.set(-1.1,-half+0.7,0.5); add(s1,'diffuse',[0.9,0.9,0.9]);
    const s2 = mkSphere(0.7, new THREE.MeshPhongMaterial({color:0xffffff, shininess:100})); s2.position.set(1.1,-half+0.7,-0.5); add(s2,'reflective',[0.95,0.95,0.95]);

    // Three.js preview lights only
    const pl = new THREE.PointLight(0xffffff,1,100); pl.position.set(0, half-0.5, 0); scene.add(pl);
    scene.add(new THREE.AmbientLight(0x404040));

    // Classic Cornell camera: outside, looking inward
    camera.position.set(0, 1.2, 7.5);
    pitch = 0; yaw = 0;
    camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));
    scene.updateMatrixWorld(true);

    // ---------- Path-tracer canvas ----------
    const canvasPT = document.getElementById('canvasPT');
    const ctx = canvasPT.getContext('2d');
    let width=innerWidth, height=innerHeight;
    canvasPT.width=width; canvasPT.height=height;

    // 4×4 tiles
    const TILES_PER_SIDE = 4;
    let tiles=[];
    function rebuildTiles(){
      tiles=[];
      const tw=Math.ceil(width/TILES_PER_SIDE), th=Math.ceil(height/TILES_PER_SIDE);
      for(let ty=0; ty<TILES_PER_SIDE; ty++){
        for(let tx=0; tx<TILES_PER_SIDE; tx++){
          const x=tx*tw, y=ty*th;
          tiles.push({ id:ty*TILES_PER_SIDE+tx, x, y, width:Math.min(tw, width-x), height:Math.min(th, height-y) });
        }
      }
    }
    rebuildTiles();

    // ---------- Worker code (per-tile display; RGBA patches; with NEE) ----------
    const workerCode = `
      let objects=null, running=false, cfg=null, cam=null, tile=null, width=0, height=0;
      let disp=null; // Float32 display buffer (tileW*tileH*3)
      let rgba=null, imageW=0, imageH=0;
      let lastTS=performance.now();

      function ensureBuffers(){
        if(!tile) return;
        const w=tile.width, h=tile.height;
        if(!disp || imageW!==w || imageH!==h){
          disp = new Float32Array(w*h*3);
          rgba = new Uint8ClampedArray(w*h*4);
          imageW=w; imageH=h;
        }
      }

      // --- Geometry & math ---
      function dot(a,b){return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]}
      function sub(a,b){return [a[0]-b[0],a[1]-b[1],a[2]-b[2]]}
      function len(v){return Math.hypot(v[0],v[1],v[2])}
      function norm(v){const L=len(v); return L>0?[v[0]/L,v[1]/L,v[2]/L]:[0,0,0]}
      function muls(v,s){return [v[0]*s,v[1]*s,v[2]*s]}
      function add(a,b){return [a[0]+b[0],a[1]+b[1],a[2]+b[2]]}

      function intersectRay(o,d,objs){let c=null,m=1/0;
        for(const ob of objs){const h=ob.geometry==='sphere'?isSphere(o,d,ob):ob.geometry==='plane'?isPlane(o,d,ob):null;
          if(h&&h.distance<m){m=h.distance;c=h;c.object=ob}}
        return c}
      function isSphere(o,d,ob){
        const c=ob.position,r=ob.radius; const oc=[o[0]-c[0],o[1]-c[1],o[2]-c[2]];
        const a=dot(d,d); const b=2*dot(oc,d); const c2=dot(oc,oc)-r*r; const disc=b*b-4*a*c2;
        if(disc<0) return null; const t=(-b-Math.sqrt(disc))/(2*a); if(t<0.001) return null;
        const p=add(o,muls(d,t)); const n=muls(sub(p,c),1/r); return {distance:t, point:p, normal:n};}
      function isPlane(o,d,ob){
        const n=ob.normal, p0=ob.position; const denom=dot(n,d); if(Math.abs(denom)<1e-4) return null;
        const t=dot(sub(p0,o),n)/denom; if(t<0.001) return null;
        const hp=add(o,muls(d,t)); const lp=sub(hp,p0);
        const uC=dot(lp,ob.uAxis), vC=dot(lp,ob.vAxis); const half=ob.size*0.5;
        if(Math.abs(uC)>half || Math.abs(vC)>half) return null;
        const fn = denom>0?[-n[0],-n[1],-n[2]]:n;
        return {distance:t, point:hp, normal:fn, uv:[uC,vC]};}
      function rUnit(){for(;;){const v=[Math.random()*2-1,Math.random()*2-1,Math.random()*2-1]; if(dot(v,v)<1) return v;}}
      function rHemi(n){const v=rUnit(); return dot(v,n)>0?v:[-v[0],-v[1],-v[2]];}
      function reflect(v,n){const d=dot(v,n); return [v[0]-2*d*n[0], v[1]-2*d*n[1], v[2]-2*d*n[2]];}
      function rotQ(v,q){const [qx,qy,qz,qw]=q; const [x,y,z]=v;
        const ix=qw*x+qy*z-qz*y, iy=qw*y+qz*x-qx*z, iz=qw*z+qx*y-qy*x, iw=-qx*x-qy*y-qz*z;
        return [ix*qw+iw*-qx+iy*-qz-iz*-qy, iy*qw+iw*-qy+iz*-qx-ix*-qz, iz*qw+iw*-qz+ix*-qy-iy*-qx];}

      // --- Next-Event Estimation (sample emissive planes directly) ---
      function sampleAreaLight(point, normal, objs){
        let Ld=[0,0,0];
        for(const ob of objs){
          if(ob.type!=='emissive' || ob.geometry!=='plane') continue;
          const half=ob.size*0.5;
          // uniform on area
          const su = (Math.random()*2-1)*half;
          const sv = (Math.random()*2-1)*half;
          const xL = add(ob.position, add(muls(ob.uAxis, su), muls(ob.vAxis, sv)));

          const toL = sub(xL, point);
          const dist2 = Math.max(1e-6, dot(toL,toL));
          const dist = Math.sqrt(dist2);
          const wi = muls(toL, 1/dist);

          const cosSurf = Math.max(0, dot(normal, wi));
          const cosLight = Math.max(0, dot(ob.normal, muls(wi,-1))); // angle at light
          if(cosSurf<=0 || cosLight<=0) continue;

          // Visibility (shadow ray)
          const eps=0.001;
          const shadowOrig = add(point, muls(normal, eps));
          const hit = intersectRay(shadowOrig, wi, objs);
          if(!hit) continue;
          // Consider it visible only if we hit the light itself (within small epsilon of xL)
          if(hit.object!==ob) continue;

          const area = ob.size * ob.size;
          const G = (cosSurf * cosLight) / dist2;
          const pdf = 1/area; // uniform area sampling
          const scale = G / pdf; // = G * area

          Ld = add(Ld, muls(ob.emission, scale));
        }
        return Ld;
      }

      function trace(o,d,depth,maxDepth,objs){
        if(depth>=maxDepth) return [0,0,0];
        const hit=intersectRay(o,d,objs); if(!hit) return [0,0,0];
        const ob=hit.object, p=hit.point, n=hit.normal; const eps=0.001; const po=add(p, muls(n, eps));

        if(ob.type==='emissive') return ob.emission;

        const al=ob.color;

        // Direct lighting for diffuse surfaces
        let Lo = [0,0,0];
        if(ob.type!=='reflective'){
          const Ld = sampleAreaLight(p, n, objs); // radiance arriving from light
          // BRDF = albedo / PI
          Lo = add(Lo, muls(Ld, 1/Math.PI));
        }

        if(ob.type==='reflective'){
          const nd=norm(reflect(d,n));
          const inc=trace(po,nd,depth+1,maxDepth,objs);
          return [al[0]*inc[0]+Lo[0], al[1]*inc[1]+Lo[1], al[2]*inc[2]+Lo[2]];
        }else{
          // Diffuse bounce (indirect)
          const nd=norm(rHemi(n));
          const cosT=Math.max(0, dot(nd,n));
          const inc=trace(po,nd,depth+1,maxDepth,objs);
          // MIS-less: cosine hemisphere with BRDF=albedo/PI, pdf=cos/PI -> cancels to albedo
          const indir = [al[0]*inc[0], al[1]*inc[1], al[2]*inc[2]];
          return [Lo[0] + indir[0], Lo[1] + indir[1], Lo[2] + indir[2]];
        }
      }

      function batch(samples){
        const ps=cfg.pixelSize|0, maxB=cfg.maxBounces|0;
        const w=tile.width, h=tile.height, x0=tile.x, y0=tile.y;
        const gxMax=Math.max(1,(w/ps)|0), gyMax=Math.max(1,(h/ps)|0);

        const acc = new Float32Array(w*h*3);
        const cnt = new Uint16Array(w*h);

        for(let s=0;s<samples;s++){
          const gx=(Math.random()*gxMax)|0, gy=(Math.random()*gyMax)|0;
          const px=x0 + gx*ps, py=y0 + gy*ps;
          const u=(px + Math.random()*ps) / width;
          const v=(py + Math.random()*ps) / height;
          const dx=(u*2-1)*cam.tanFov*cam.aspect, dy=-(v*2-1)*cam.tanFov;
          let dir=[dx,dy,-1]; dir=norm(dir);
          dir=rotQ(dir, cam.quaternion);
          const c = trace(cam.position, dir, 0, maxB, objects);

          for(let oy=0; oy<ps && (gy*ps+oy)<h; oy++){
            for(let ox=0; ox<ps && (gx*ps+ox)<w; ox++){
              const ix = (gy*ps+oy)*w + (gx*ps+ox);
              const i3 = ix*3;
              acc[i3  ]+=c[0]; acc[i3+1]+=c[1]; acc[i3+2]+=c[2]; cnt[ix]++;
            }
          }
        }

        const now=performance.now();
        const dt=Math.max(0,(now-lastTS)/1000); lastTS=now;
        const half=Math.max(0.05, cfg.fadeHalfLife||0.75);
        const decay=Math.pow(0.5, dt/half), oneMinus=1-decay;

        for(let i=0;i<w*h;i++){
          const i3=i*3;
          const n = cnt[i] ? 1.0/cnt[i] : 0.0;
          const nr = acc[i3]*n, ng=acc[i3+1]*n, nb=acc[i3+2]*n;
          let dr=disp[i3]*decay + nr*oneMinus;
          let dg=disp[i3+1]*decay + ng*oneMinus;
          let db=disp[i3+2]*decay + nb*oneMinus;
          disp[i3]=dr; disp[i3+1]=dg; disp[i3+2]=db;

          // gamma -> sRGB-ish
          dr = Math.pow(Math.max(0,dr), 1/2.2);
          dg = Math.pow(Math.max(0,dg), 1/2.2);
          db = Math.pow(Math.max(0,db), 1/2.2);
          const j=i*4;
          rgba[j  ] = dr*255;
          rgba[j+1] = dg*255;
          rgba[j+2] = db*255;
          rgba[j+3] = 255;
        }
      }

      function loop(){
        if(!running) return;
        ensureBuffers();
        batch(cfg.spp|0);
        postMessage({type:'PATCH', x:tile.x, y:tile.y, w:imageW, h:imageH, buf:rgba}, [rgba.buffer]);
        rgba = new Uint8ClampedArray(imageW*imageH*4);
        setTimeout(loop, 0);
      }

      onmessage=(e)=>{
        const {type}=e.data;
        if(type==='INIT'){
          objects=e.data.objects; width=e.data.width; height=e.data.height;
          tile=e.data.tile; cfg=e.data.cfg; cam=e.data.camera; ensureBuffers();
        }else if(type==='CONFIG'){
          cfg=e.data.cfg; width=e.data.width; height=e.data.height; tile=e.data.tile; ensureBuffers();
        }else if(type==='CAM'){ cam=e.data.camera;
        }else if(type==='START'){ running=true; loop();
        }else if(type==='STOP'){ running=false;
        }else if(type==='RESET'){ running=false; disp=null; rgba=null; }
      };
    `;

    const blobURL = URL.createObjectURL(new Blob([workerCode], {type:'application/javascript'}));

    // ---------- Worker management ----------
    let workers=[];
    let isTracing=false;
    let totalSamples=0, lastSamples=0, lastT=Date.now();

    function serializeObjects(){
      const out=[];
      for(const o of objs){
        const m=o.mesh;
        if(m.geometry.type==='SphereGeometry'){
          out.push({
            geometry:'sphere',
            position:[m.position.x, m.position.y, m.position.z],
            radius:m.geometry.parameters.radius,
            type:o.type, color:o.color, emission:o.emission
          });
        }else if(m.geometry.type==='PlaneGeometry'){
          const normal = new THREE.Vector3(0,0,1).applyQuaternion(m.quaternion).normalize();
          const uAxis  = new THREE.Vector3(1,0,0).applyQuaternion(m.quaternion).normalize();
          const vAxis  = new THREE.Vector3(0,1,0).applyQuaternion(m.quaternion).normalize();
          out.push({
            geometry:'plane',
            position:[m.position.x, m.position.y, m.position.z],
            normal:[normal.x,normal.y,normal.z],
            uAxis:[uAxis.x,uAxis.y,uAxis.z],
            vAxis:[vAxis.x,vAxis.y,vAxis.z],
            size:Math.max(m.geometry.parameters.width, m.geometry.parameters.height),
            type:o.type, color:o.color, emission:o.emission
          });
        }
      }
      return out;
    }
    function currentCamera(){
      return {
        position:[camera.position.x, camera.position.y, camera.position.z],
        quaternion:[camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
        tanFov: Math.tan(camera.fov * Math.PI / 360),
        aspect: camera.aspect
      };
    }
    function cfgFromUI(){
      return {
        spp: parseInt(document.getElementById('spp').value,10),
        pixelSize: parseInt(document.getElementById('pixelSize').value,10),
        maxBounces: parseInt(document.getElementById('bounces').value,10),
        fadeHalfLife: parseFloat(document.getElementById('fadeHalfLife').value)
      };
    }

    function initWorkers(){
      for(const w of workers){ try{ w.postMessage({type:'STOP'}); w.terminate(); }catch{} }
      workers=[];

      const want = Math.max(1, Math.min(parseInt(document.getElementById('workers').value,10)||16, tiles.length));
      document.getElementById('workers').value = want;

      const objects = serializeObjects();
      const cfg = cfgFromUI();
      const cam = currentCamera();

      for(let i=0;i<want;i++){
        const w = new Worker(blobURL);
        w.onmessage = onWorkerMessage;
        const tile = tiles[i];
        w.postMessage({type:'INIT', objects, width, height, tile, cfg, camera:cam});
        workers.push(w);
      }
      document.getElementById('hwc').textContent = (navigator.hardwareConcurrency||'?') + " (hint)";
    }
    function startWorkers(){
      const cfg = cfgFromUI();
      const cam = currentCamera();
      for(let i=0;i<workers.length;i++){
        workers[i].postMessage({type:'CONFIG', cfg, width, height, tile: tiles[i]});
        workers[i].postMessage({type:'CAM', camera:cam});
        workers[i].postMessage({type:'START'});
      }
    }
    function stopWorkers(){ for(const w of workers) w.postMessage({type:'STOP'}); }
    function resetWorkers(){
      for(const w of workers) w.postMessage({type:'RESET'});
      ctx.clearRect(0,0,width,height);
      totalSamples=0; lastSamples=0; lastT=Date.now();
      document.getElementById('samples').textContent = '0';
      document.getElementById('sps').textContent = '0';
    }

    function onWorkerMessage(e){
      if(e.data.type==='PATCH'){
        const {x,y,w,h,buf} = e.data;
        const img = new ImageData(buf, w, h);
        ctx.putImageData(img, x, y);
        totalSamples += 1;
      }
    }

    // ---------- UI / lifecycle ----------
    const btnToggle = document.getElementById('togglePT');
    document.getElementById('reset').addEventListener('click', ()=>{ resetWorkers(); });

    btnToggle.addEventListener('click', ()=>{
      if(isTracing){
        isTracing=false; btnToggle.textContent='Resume Path Tracing'; stopWorkers();
      }else{
        if(workers.length===0) initWorkers();
        isTracing=true; btnToggle.textContent='Pause Path Tracing'; startWorkers();
      }
    });

    // keep camera/renderer fresh
    let frame=0;
    function animate(){
      requestAnimationFrame(animate);
      updateMovement();
      renderer.setSize(innerWidth, innerHeight, false);
      renderer.render(scene, camera);

      // stream camera occasionally to workers (to follow motion)
      if(isTracing && (frame % 8 === 0)){
        const cam = currentCamera();
        for(const w of workers) w.postMessage({type:'CAM', camera:cam});
      }

      // stats
      const t=Date.now(), el=(t-lastT)/1000;
      if(el>1){
        document.getElementById('sps').textContent = Math.floor((totalSamples-lastSamples)/el).toLocaleString();
        lastSamples = totalSamples; lastT=t;
      }
      document.getElementById('samples').textContent = totalSamples.toLocaleString();
      frame++;
    }
    animate();

    // resize
    window.addEventListener('resize', ()=>{
      width=innerWidth; height=innerHeight;
      camera.aspect=width/height; camera.updateProjectionMatrix();
      renderer.setSize(width, height);
      canvasPT.width=width; canvasPT.height=height;
      rebuildTiles();
      resetWorkers();
      if(workers.length){ initWorkers(); if(isTracing) startWorkers(); }
    });

    // show hardwareConcurrency hint
    document.getElementById('hwc').textContent = (navigator.hardwareConcurrency || '?') + " (hint)";
  </script>
</body>
</html>
```

### luz mas fuerte

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Path Tracer — 4×4 Tiles, Multicore, Low-RAM + Direct Light Sampling</title>
  <style>
    body { margin:0; overflow:hidden; font-family:Arial, sans-serif; }
    #canvas3d, #canvasPT { position:absolute; top:0; left:0; }
    #controls{
      position:absolute; top:10px; left:10px;
      background:rgba(0,0,0,.7); color:#fff; padding:10px; border-radius:6px;
      font-size:12px; max-width:360px; line-height:1.4; user-select:none;
    }
    label{display:block; margin-top:6px}
    input[type="number"]{width:90px}
    button{margin:6px 0; padding:6px 10px; cursor:pointer}
  </style>
</head>
<body>
  <canvas id="canvas3d"></canvas>
  <canvas id="canvasPT"></canvas>

  <div id="controls">
    <div><strong>Monte Carlo Path Tracer (NEE)</strong></div>
    <div>Cores (Workers): <input type="number" id="workers" value="16" min="1" max="64"> <span style="opacity:.7">/ tiles: 16</span></div>
    <div>OS hints (hardwareConcurrency): <span id="hwc">?</span></div>
    <div>Total Patches: <span id="samples">0</span></div>
    <div>Patches/sec: <span id="sps">0</span></div>

    <button id="togglePT">Start Path Tracing</button>
    <button id="reset">Reset</button>

    <label>Pixel Size:
      <input type="number" id="pixelSize" value="2" min="1" max="16">
      <span style="font-size:10px; color:#aaa">(1 = full quality)</span>
    </label>
    <label>Samples/Batch (per worker tick):
      <input type="number" id="spp" value="2000" min="50" max="50000">
    </label>
    <label>Max Bounces:
      <input type="number" id="bounces" value="6" min="1" max="10">
    </label>
    <label>Fade Half-Life (s):
      <input type="number" id="fadeHalfLife" value="20" step="0.05" min="0.05" max="60">
    </label>

    <div style="margin-top:6px; font-size:11px; color:#aaa">
      Click to enable FPS controls. <b>W</b>=forward, <b>S</b>=backward, <b>A</b>=left, <b>D</b>=right. Space=up, Shift=sprint (or down if no move).
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
  <script>
    // ---------- Basic scene ----------
    const canvas3d = document.getElementById('canvas3d');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(50, innerWidth/innerHeight, 0.01, 1000);
    const renderer = new THREE.WebGLRenderer({canvas: canvas3d, antialias:true});
    renderer.setSize(innerWidth, innerHeight);
    const orbit = new THREE.OrbitControls(camera, canvas3d); orbit.enabled = false;

    // FPS controls (WASD)
    const keys = { w:false, a:false, s:false, d:false, shift:false, space:false };
    let pitch=0, yaw=0, locked=false;
    const mouseSensitivity=0.002, moveSpeed=0.04;

    document.body.addEventListener('click', ()=>{ if(!locked) document.body.requestPointerLock(); });
    document.addEventListener('pointerlockchange', ()=> locked = document.pointerLockElement===document.body);
    window.addEventListener('keydown', e=>{ const k=e.key.toLowerCase(); if(k in keys){keys[k]=true; e.preventDefault();}});
    window.addEventListener('keyup',   e=>{ const k=e.key.toLowerCase(); if(k in keys){keys[k]=false; e.preventDefault();}});
    window.addEventListener('mousemove', e=>{
      if(!locked) return;
      yaw   -= e.movementX * mouseSensitivity;
      pitch -= e.movementY * mouseSensitivity;
      pitch = Math.max(-Math.PI/2+0.01, Math.min(Math.PI/2-0.01, pitch));
      camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));
    });

    function updateMovement(){
      const forward = new THREE.Vector3(0,0,-1).applyQuaternion(camera.quaternion).normalize();
      const right   = new THREE.Vector3(1,0,0).applyQuaternion(camera.quaternion).normalize();
      const speed = keys.shift && (keys.w||keys.a||keys.s||keys.d) ? moveSpeed*2 : moveSpeed;

      if (keys.w) camera.position.addScaledVector(forward,  speed);
      if (keys.s) camera.position.addScaledVector(forward, -speed);
      if (keys.d) camera.position.addScaledVector(right,    speed);
      if (keys.a) camera.position.addScaledVector(right,   -speed);
      if (keys.space) camera.position.y += speed;
      if (keys.shift && !(keys.w||keys.a||keys.s||keys.d)) camera.position.y -= speed; // "down" only when not moving
    }

    // ---------- Cornell Box geometry ----------
    const boxSize=5, half=boxSize/2, objs=[];
    function add(mesh, type, color, emission=null){ scene.add(mesh); objs.push({mesh, type, color, emission}); }
    const mkPlane=(w,h,color)=> new THREE.Mesh(new THREE.PlaneGeometry(w,h), new THREE.MeshLambertMaterial({color, side:THREE.DoubleSide}));
    const mkSphere=(r,mat)=> new THREE.Mesh(new THREE.SphereGeometry(r,32,32), mat);

    // Left, Right, Back, Floor, Ceiling. Front is open.
    const left = mkPlane(boxSize,boxSize,0xff0000); left.position.set(-half,0,0); left.rotation.y=Math.PI/2; add(left,'diffuse',[1,0,0]);
    const right= mkPlane(boxSize,boxSize,0x00ff00); right.position.set( half,0,0); right.rotation.y=-Math.PI/2; add(right,'diffuse',[0,1,0]);
    const back = mkPlane(boxSize,boxSize,0xffffff); back.position.set(0,0,-half); add(back,'diffuse',[0.95,0.95,0.95]);
    const floor= mkPlane(boxSize,boxSize,0xffffff); floor.position.set(0,-half,0); floor.rotation.x=-Math.PI/2; add(floor,'diffuse',[0.95,0.95,0.95]);
    const ceil = mkPlane(boxSize,boxSize,0xffffff); ceil.position.set(0, half,0); ceil.rotation.x=-Math.PI/2; add(ceil,'diffuse',[0.95,0.95,0.95]);

    // Area light
    const lightSize=1.6;
    const lamp = new THREE.Mesh(new THREE.PlaneGeometry(lightSize, lightSize), new THREE.MeshBasicMaterial({color:0xffffff, side:THREE.DoubleSide}));
    lamp.position.set(0, half-0.05, 0); lamp.rotation.x=-Math.PI/2;
    add(lamp,'emissive',[1,1,1],[40,40,40]); // strong emission to converge faster

    // Spheres
    const s1 = mkSphere(0.7, new THREE.MeshLambertMaterial({color:0xffffff})); s1.position.set(-1.1,-half+0.7,0.5); add(s1,'diffuse',[0.9,0.9,0.9]);
    const s2 = mkSphere(0.7, new THREE.MeshPhongMaterial({color:0xffffff, shininess:100})); s2.position.set(1.1,-half+0.7,-0.5); add(s2,'reflective',[0.95,0.95,0.95]);

    // Three.js preview lights only
    const pl = new THREE.PointLight(0xffffff,1,100); pl.position.set(0, half-0.5, 0); scene.add(pl);
    scene.add(new THREE.AmbientLight(0x404040));

    // Classic Cornell camera: outside, looking inward
    camera.position.set(0, 1.2, 7.5);
    pitch = 0; yaw = 0;
    camera.quaternion.setFromEuler(new THREE.Euler(pitch, yaw, 0, 'YXZ'));
    scene.updateMatrixWorld(true);

    // ---------- Path-tracer canvas ----------
    const canvasPT = document.getElementById('canvasPT');
    const ctx = canvasPT.getContext('2d');
    let width=innerWidth, height=innerHeight;
    canvasPT.width=width; canvasPT.height=height;

    // 4×4 tiles
    const TILES_PER_SIDE = 4;
    let tiles=[];
    function rebuildTiles(){
      tiles=[];
      const tw=Math.ceil(width/TILES_PER_SIDE), th=Math.ceil(height/TILES_PER_SIDE);
      for(let ty=0; ty<TILES_PER_SIDE; ty++){
        for(let tx=0; tx<TILES_PER_SIDE; tx++){
          const x=tx*tw, y=ty*th;
          tiles.push({ id:ty*TILES_PER_SIDE+tx, x, y, width:Math.min(tw, width-x), height:Math.min(th, height-y) });
        }
      }
    }
    rebuildTiles();

    // ---------- Worker code (per-tile display; RGBA patches; with NEE) ----------
    const workerCode = `
      let objects=null, running=false, cfg=null, cam=null, tile=null, width=0, height=0;
      let disp=null; // Float32 display buffer (tileW*tileH*3)
      let rgba=null, imageW=0, imageH=0;
      let lastTS=performance.now();

      function ensureBuffers(){
        if(!tile) return;
        const w=tile.width, h=tile.height;
        if(!disp || imageW!==w || imageH!==h){
          disp = new Float32Array(w*h*3);
          rgba = new Uint8ClampedArray(w*h*4);
          imageW=w; imageH=h;
        }
      }

      // --- Geometry & math ---
      function dot(a,b){return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]}
      function sub(a,b){return [a[0]-b[0],a[1]-b[1],a[2]-b[2]]}
      function len(v){return Math.hypot(v[0],v[1],v[2])}
      function norm(v){const L=len(v); return L>0?[v[0]/L,v[1]/L,v[2]/L]:[0,0,0]}
      function muls(v,s){return [v[0]*s,v[1]*s,v[2]*s]}
      function add(a,b){return [a[0]+b[0],a[1]+b[1],a[2]+b[2]]}

      function intersectRay(o,d,objs){let c=null,m=1/0;
        for(const ob of objs){const h=ob.geometry==='sphere'?isSphere(o,d,ob):ob.geometry==='plane'?isPlane(o,d,ob):null;
          if(h&&h.distance<m){m=h.distance;c=h;c.object=ob}}
        return c}
      function isSphere(o,d,ob){
        const c=ob.position,r=ob.radius; const oc=[o[0]-c[0],o[1]-c[1],o[2]-c[2]];
        const a=dot(d,d); const b=2*dot(oc,d); const c2=dot(oc,oc)-r*r; const disc=b*b-4*a*c2;
        if(disc<0) return null; const t=(-b-Math.sqrt(disc))/(2*a); if(t<0.001) return null;
        const p=add(o,muls(d,t)); const n=muls(sub(p,c),1/r); return {distance:t, point:p, normal:n};}
      function isPlane(o,d,ob){
        const n=ob.normal, p0=ob.position; const denom=dot(n,d); if(Math.abs(denom)<1e-4) return null;
        const t=dot(sub(p0,o),n)/denom; if(t<0.001) return null;
        const hp=add(o,muls(d,t)); const lp=sub(hp,p0);
        const uC=dot(lp,ob.uAxis), vC=dot(lp,ob.vAxis); const half=ob.size*0.5;
        if(Math.abs(uC)>half || Math.abs(vC)>half) return null;
        const fn = denom>0?[-n[0],-n[1],-n[2]]:n;
        return {distance:t, point:hp, normal:fn, uv:[uC,vC]};}
      function rUnit(){for(;;){const v=[Math.random()*2-1,Math.random()*2-1,Math.random()*2-1]; if(dot(v,v)<1) return v;}}
      function rHemi(n){const v=rUnit(); return dot(v,n)>0?v:[-v[0],-v[1],-v[2]];}
      function reflect(v,n){const d=dot(v,n); return [v[0]-2*d*n[0], v[1]-2*d*n[1], v[2]-2*d*n[2]];}
      function rotQ(v,q){const [qx,qy,qz,qw]=q; const [x,y,z]=v;
        const ix=qw*x+qy*z-qz*y, iy=qw*y+qz*x-qx*z, iz=qw*z+qx*y-qy*x, iw=-qx*x-qy*y-qz*z;
        return [ix*qw+iw*-qx+iy*-qz-iz*-qy, iy*qw+iw*-qy+iz*-qx-ix*-qz, iz*qw+iw*-qz+ix*-qy-iy*-qx];}

      // --- Next-Event Estimation (sample emissive planes directly) ---
      function sampleAreaLight(point, normal, objs){
        let Ld=[0,0,0];
        for(const ob of objs){
          if(ob.type!=='emissive' || ob.geometry!=='plane') continue;
          const half=ob.size*0.5;
          // uniform on area
          const su = (Math.random()*2-1)*half;
          const sv = (Math.random()*2-1)*half;
          const xL = add(ob.position, add(muls(ob.uAxis, su), muls(ob.vAxis, sv)));

          const toL = sub(xL, point);
          const dist2 = Math.max(1e-6, dot(toL,toL));
          const dist = Math.sqrt(dist2);
          const wi = muls(toL, 1/dist);

          const cosSurf = Math.max(0, dot(normal, wi));
          const cosLight = Math.max(0, dot(ob.normal, muls(wi,-1))); // angle at light
          if(cosSurf<=0 || cosLight<=0) continue;

          // Visibility (shadow ray)
          const eps=0.001;
          const shadowOrig = add(point, muls(normal, eps));
          const hit = intersectRay(shadowOrig, wi, objs);
          if(!hit) continue;
          // Consider it visible only if we hit the light itself (within small epsilon of xL)
          if(hit.object!==ob) continue;

          const area = ob.size * ob.size;
          const G = (cosSurf * cosLight) / dist2;
          const pdf = 1/area; // uniform area sampling
          const scale = G / pdf; // = G * area

          Ld = add(Ld, muls(ob.emission, scale));
        }
        return Ld;
      }

      function trace(o,d,depth,maxDepth,objs){
        if(depth>=maxDepth) return [0,0,0];
        const hit=intersectRay(o,d,objs); if(!hit) return [0,0,0];
        const ob=hit.object, p=hit.point, n=hit.normal; const eps=0.001; const po=add(p, muls(n, eps));

        if(ob.type==='emissive') return ob.emission;

        const al=ob.color;

        // Direct lighting for diffuse surfaces
        let Lo = [0,0,0];
        if(ob.type!=='reflective'){
          const Ld = sampleAreaLight(p, n, objs); // radiance arriving from light
          // BRDF = albedo / PI
          Lo = add(Lo, muls(Ld, 1/Math.PI));
        }

        if(ob.type==='reflective'){
          const nd=norm(reflect(d,n));
          const inc=trace(po,nd,depth+1,maxDepth,objs);
          return [al[0]*inc[0]+Lo[0], al[1]*inc[1]+Lo[1], al[2]*inc[2]+Lo[2]];
        }else{
          // Diffuse bounce (indirect)
          const nd=norm(rHemi(n));
          const cosT=Math.max(0, dot(nd,n));
          const inc=trace(po,nd,depth+1,maxDepth,objs);
          // MIS-less: cosine hemisphere with BRDF=albedo/PI, pdf=cos/PI -> cancels to albedo
          const indir = [al[0]*inc[0], al[1]*inc[1], al[2]*inc[2]];
          return [Lo[0] + indir[0], Lo[1] + indir[1], Lo[2] + indir[2]];
        }
      }

      function batch(samples){
        const ps=cfg.pixelSize|0, maxB=cfg.maxBounces|0;
        const w=tile.width, h=tile.height, x0=tile.x, y0=tile.y;
        const gxMax=Math.max(1,(w/ps)|0), gyMax=Math.max(1,(h/ps)|0);

        const acc = new Float32Array(w*h*3);
        const cnt = new Uint16Array(w*h);

        for(let s=0;s<samples;s++){
          const gx=(Math.random()*gxMax)|0, gy=(Math.random()*gyMax)|0;
          const px=x0 + gx*ps, py=y0 + gy*ps;
          const u=(px + Math.random()*ps) / width;
          const v=(py + Math.random()*ps) / height;
          const dx=(u*2-1)*cam.tanFov*cam.aspect, dy=-(v*2-1)*cam.tanFov;
          let dir=[dx,dy,-1]; dir=norm(dir);
          dir=rotQ(dir, cam.quaternion);
          const c = trace(cam.position, dir, 0, maxB, objects);

          for(let oy=0; oy<ps && (gy*ps+oy)<h; oy++){
            for(let ox=0; ox<ps && (gx*ps+ox)<w; ox++){
              const ix = (gy*ps+oy)*w + (gx*ps+ox);
              const i3 = ix*3;
              acc[i3  ]+=c[0]; acc[i3+1]+=c[1]; acc[i3+2]+=c[2]; cnt[ix]++;
            }
          }
        }

        const now=performance.now();
        const dt=Math.max(0,(now-lastTS)/1000); lastTS=now;
        const half=Math.max(0.05, cfg.fadeHalfLife||0.75);
        const decay=Math.pow(0.5, dt/half), oneMinus=1-decay;

        for(let i=0;i<w*h;i++){
          const i3=i*3;
          const n = cnt[i] ? 1.0/cnt[i] : 0.0;
          const nr = acc[i3]*n, ng=acc[i3+1]*n, nb=acc[i3+2]*n;
          let dr=disp[i3]*decay + nr*oneMinus;
          let dg=disp[i3+1]*decay + ng*oneMinus;
          let db=disp[i3+2]*decay + nb*oneMinus;
          disp[i3]=dr; disp[i3+1]=dg; disp[i3+2]=db;

          // gamma -> sRGB-ish
          dr = Math.pow(Math.max(0,dr), 1/2.2);
          dg = Math.pow(Math.max(0,dg), 1/2.2);
          db = Math.pow(Math.max(0,db), 1/2.2);
          const j=i*4;
          rgba[j  ] = dr*255;
          rgba[j+1] = dg*255;
          rgba[j+2] = db*255;
          rgba[j+3] = 255;
        }
      }

      function loop(){
        if(!running) return;
        ensureBuffers();
        batch(cfg.spp|0);
        postMessage({type:'PATCH', x:tile.x, y:tile.y, w:imageW, h:imageH, buf:rgba}, [rgba.buffer]);
        rgba = new Uint8ClampedArray(imageW*imageH*4);
        setTimeout(loop, 0);
      }

      onmessage=(e)=>{
        const {type}=e.data;
        if(type==='INIT'){
          objects=e.data.objects; width=e.data.width; height=e.data.height;
          tile=e.data.tile; cfg=e.data.cfg; cam=e.data.camera; ensureBuffers();
        }else if(type==='CONFIG'){
          cfg=e.data.cfg; width=e.data.width; height=e.data.height; tile=e.data.tile; ensureBuffers();
        }else if(type==='CAM'){ cam=e.data.camera;
        }else if(type==='START'){ running=true; loop();
        }else if(type==='STOP'){ running=false;
        }else if(type==='RESET'){ running=false; disp=null; rgba=null; }
      };
    `;

    const blobURL = URL.createObjectURL(new Blob([workerCode], {type:'application/javascript'}));

    // ---------- Worker management ----------
    let workers=[];
    let isTracing=false;
    let totalSamples=0, lastSamples=0, lastT=Date.now();

    function serializeObjects(){
      const out=[];
      for(const o of objs){
        const m=o.mesh;
        if(m.geometry.type==='SphereGeometry'){
          out.push({
            geometry:'sphere',
            position:[m.position.x, m.position.y, m.position.z],
            radius:m.geometry.parameters.radius,
            type:o.type, color:o.color, emission:o.emission
          });
        }else if(m.geometry.type==='PlaneGeometry'){
          const normal = new THREE.Vector3(0,0,1).applyQuaternion(m.quaternion).normalize();
          const uAxis  = new THREE.Vector3(1,0,0).applyQuaternion(m.quaternion).normalize();
          const vAxis  = new THREE.Vector3(0,1,0).applyQuaternion(m.quaternion).normalize();
          out.push({
            geometry:'plane',
            position:[m.position.x, m.position.y, m.position.z],
            normal:[normal.x,normal.y,normal.z],
            uAxis:[uAxis.x,uAxis.y,uAxis.z],
            vAxis:[vAxis.x,vAxis.y,vAxis.z],
            size:Math.max(m.geometry.parameters.width, m.geometry.parameters.height),
            type:o.type, color:o.color, emission:o.emission
          });
        }
      }
      return out;
    }
    function currentCamera(){
      return {
        position:[camera.position.x, camera.position.y, camera.position.z],
        quaternion:[camera.quaternion.x, camera.quaternion.y, camera.quaternion.z, camera.quaternion.w],
        tanFov: Math.tan(camera.fov * Math.PI / 360),
        aspect: camera.aspect
      };
    }
    function cfgFromUI(){
      return {
        spp: parseInt(document.getElementById('spp').value,10),
        pixelSize: parseInt(document.getElementById('pixelSize').value,10),
        maxBounces: parseInt(document.getElementById('bounces').value,10),
        fadeHalfLife: parseFloat(document.getElementById('fadeHalfLife').value)
      };
    }

    function initWorkers(){
      for(const w of workers){ try{ w.postMessage({type:'STOP'}); w.terminate(); }catch{} }
      workers=[];

      const want = Math.max(1, Math.min(parseInt(document.getElementById('workers').value,10)||16, tiles.length));
      document.getElementById('workers').value = want;

      const objects = serializeObjects();
      const cfg = cfgFromUI();
      const cam = currentCamera();

      for(let i=0;i<want;i++){
        const w = new Worker(blobURL);
        w.onmessage = onWorkerMessage;
        const tile = tiles[i];
        w.postMessage({type:'INIT', objects, width, height, tile, cfg, camera:cam});
        workers.push(w);
      }
      document.getElementById('hwc').textContent = (navigator.hardwareConcurrency||'?') + " (hint)";
    }
    function startWorkers(){
      const cfg = cfgFromUI();
      const cam = currentCamera();
      for(let i=0;i<workers.length;i++){
        workers[i].postMessage({type:'CONFIG', cfg, width, height, tile: tiles[i]});
        workers[i].postMessage({type:'CAM', camera:cam});
        workers[i].postMessage({type:'START'});
      }
    }
    function stopWorkers(){ for(const w of workers) w.postMessage({type:'STOP'}); }
    function resetWorkers(){
      for(const w of workers) w.postMessage({type:'RESET'});
      ctx.clearRect(0,0,width,height);
      totalSamples=0; lastSamples=0; lastT=Date.now();
      document.getElementById('samples').textContent = '0';
      document.getElementById('sps').textContent = '0';
    }

    function onWorkerMessage(e){
      if(e.data.type==='PATCH'){
        const {x,y,w,h,buf} = e.data;
        const img = new ImageData(buf, w, h);
        ctx.putImageData(img, x, y);
        totalSamples += 1;
      }
    }

    // ---------- UI / lifecycle ----------
    const btnToggle = document.getElementById('togglePT');
    document.getElementById('reset').addEventListener('click', ()=>{ resetWorkers(); });

    btnToggle.addEventListener('click', ()=>{
      if(isTracing){
        isTracing=false; btnToggle.textContent='Resume Path Tracing'; stopWorkers();
      }else{
        if(workers.length===0) initWorkers();
        isTracing=true; btnToggle.textContent='Pause Path Tracing'; startWorkers();
      }
    });

    // keep camera/renderer fresh
    let frame=0;
    function animate(){
      requestAnimationFrame(animate);
      updateMovement();
      renderer.setSize(innerWidth, innerHeight, false);
      renderer.render(scene, camera);

      // stream camera occasionally to workers (to follow motion)
      if(isTracing && (frame % 8 === 0)){
        const cam = currentCamera();
        for(const w of workers) w.postMessage({type:'CAM', camera:cam});
      }

      // stats
      const t=Date.now(), el=(t-lastT)/1000;
      if(el>1){
        document.getElementById('sps').textContent = Math.floor((totalSamples-lastSamples)/el).toLocaleString();
        lastSamples = totalSamples; lastT=t;
      }
      document.getElementById('samples').textContent = totalSamples.toLocaleString();
      frame++;
    }
    animate();

    // resize
    window.addEventListener('resize', ()=>{
      width=innerWidth; height=innerHeight;
      camera.aspect=width/height; camera.updateProjectionMatrix();
      renderer.setSize(width, height);
      canvasPT.width=width; canvasPT.height=height;
      rebuildTiles();
      resetWorkers();
      if(workers.length){ initWorkers(); if(isTracing) startWorkers(); }
    });

    // show hardwareConcurrency hint
    document.getElementById('hwc').textContent = (navigator.hardwareConcurrency || '?') + " (hint)";
  </script>
</body>
</html>
```

<a id="programacion-de-aplicaciones-multiproceso"></a>
## Programación de aplicaciones multiproceso

La programación multiproceso es un concepto fundamental en la informática que permite a una computadora ejecutar varias tareas simultáneamente. Cada proceso se considera como una unidad de trabajo independiente con su propio conjunto de recursos y memoria. En esta subunidad, exploraremos cómo diseñar y implementar aplicaciones multiproceso utilizando diferentes técnicas y herramientas disponibles en la programación.

La primera etapa del desarrollo de aplicaciones multiproceso implica identificar las tareas que pueden ejecutarse concurrentemente para optimizar el rendimiento del sistema. Cada tarea debe ser independiente y no depender de los estados o resultados de otras tareas, lo que facilita su paralelización.

Una vez identificadas las tareas, se necesita establecer la comunicación entre ellas. Los procesos pueden compartir recursos como archivos, bases de datos o variables globales, pero es crucial manejar adecuadamente el acceso concurrente para evitar problemas de concurrencia y garantizar la integridad de los datos.

La sincronización entre procesos es otro aspecto crucial en la programación multiproceso. Se requiere coordinar las acciones de los procesos para asegurar que se ejecuten en el orden correcto o para evitar situaciones como el interbloqueo, donde dos o más procesos esperan indefinidamente por recursos que no están disponibles.

Además de la sincronización, es importante gestionar la memoria compartida entre los procesos. La memoria virtual proporciona una forma de compartir datos entre procesos, pero requiere cuidados adicionales para evitar problemas como el acceso a memoria inválida o la corrupción de datos.

La programación multiproceso también implica considerar aspectos de seguridad y privacidad. Los procesos deben estar diseñados para minimizar sus riesgos de ataque y asegurar que solo acceden a los recursos necesarios, evitando así posibles vulnerabilidades.

En el mundo real, la programación multiproceso se utiliza en una amplia variedad de aplicaciones, desde servidores web hasta sistemas operativos y bases de datos. Cada uno de estos sistemas beneficia del paralelismo para mejorar su eficiencia y capacidad de respuesta.

Para implementar aplicaciones multiproceso, existen varias bibliotecas y frameworks disponibles en diferentes lenguajes de programación. Estas herramientas facilitan la creación y gestión de procesos, proporcionando funciones para crear, ejecutar y comunicarse entre ellos.

En conclusión, la programación multiproceso es una técnica poderosa que permite a las computadoras realizar tareas complejas de manera eficiente. Al entender los conceptos básicos de paralelismo, comunicación, sincronización y gestión de memoria, se puede desarrollar software robusto y escalable para satisfacer las necesidades modernas del mundo digital.

<a id="ollama"></a>
## Ollama

### Llamada

```bash
ollama list
```

### llamada limpia

```bash
curl -s http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:7b-instruct-q4_0",
  "prompt": "Dime una frase inspiradora sobre la programación."
}' | jq -r 'select(.response != null) | .response' | tr -d '\n'; echo
```

### mas limpio todavia

```bash
curl -s http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:7b-instruct-q4_0",
  "prompt": "Resume qué es el aprendizaje automático en una sola frase."
}' | jq -r 'select(.response != null) | .response' | tr -d '\n'; echo

sudo snap restart ollama
```

### generador

```python
import subprocess
import json

# Ask for the prompt dynamically (or replace this with a variable)
prompt = input("Introduce el prompt: ")

# Build the payload
payload = {
    "model": "qwen2.5:7b-instruct-q4_0",
    "prompt": prompt
}

# Execute the curl command
result = subprocess.run(
    [
        "curl", "-s", "http://localhost:11434/api/generate",
        "-d", json.dumps(payload)
    ],
    capture_output=True,
    text=True
)

# Filter and print response like your jq + tr pipeline
try:
    lines = result.stdout.splitlines()
    response = ""
    for line in lines:
        obj = json.loads(line)
        if "response" in obj and obj["response"] is not None:
            response += obj["response"]
    print(response.strip())
except Exception as e:
    print("Error parsing output:", e)
    print(result.stdout)
```

### cargo blog

```python
import subprocess
import json
import os

SCHEMA_PATH = "blog.sql"
MAX_SCHEMA_CHARS = 200_000  # por si el .sql es enorme, evita pasarte de contexto

def cargar_schema_sql(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        schema = f.read()
    if len(schema) > MAX_SCHEMA_CHARS:
        schema = schema[:MAX_SCHEMA_CHARS] + "\n-- [Truncado para no exceder el contexto]\n"
    return schema

# Pide el prompt dinámicamente (o reemplázalo por una variable)
prompt_usuario = input("Introduce el prompt: ").strip()

# Carga el esquema de blog.sql
schema_sql = cargar_schema_sql(SCHEMA_PATH)

# Construye el contexto a inyectar en el prompt
contexto_sql = ""
if schema_sql:
    contexto_sql = (
        "Eres un asistente experto en SQL. A continuación tienes el esquema de base de datos "
        "extraído del archivo 'blog.sql'. Usa **exclusivamente** esta estructura para responder "
        "preguntas y proponer consultas SQL (estándar ANSI cuando sea posible). "
        "Responde siempre con:\n"
        "1) Breve explicación\n"
        "2) La consulta SQL dentro de un bloque ```sql```.\n\n"
        "=== ESQUEMA (blog.sql) ===\n"
        f"{schema_sql}\n"
        "=== FIN DEL ESQUEMA ===\n\n"
    )
else:
    contexto_sql = (
        "Eres un asistente experto en SQL. (Aviso: no se encontró 'blog.sql', responde de forma "
        "general sin validar contra un esquema cargado.)\n\n"
    )

# Prompt final que se envía al modelo
prompt_final = (
    f"{contexto_sql}"
    f"Pregunta del usuario:\n{prompt_usuario}\n"
)

# Construye el payload para Ollama
payload = {
    "model": "qwen2.5:7b-instruct-q4_0",
    "prompt": prompt_final,
    # Opcionalmente puedes fijar 'stream': True/False; por defecto es True y devolvemos JSONL
    # "stream": True
    # También puedes añadir un 'system' si prefieres separar instrucciones:
    # "system": "Sigue estrictamente el esquema proporcionado y el formato de salida indicado."
}

# Ejecuta la llamada curl
result = subprocess.run(
    [
        "curl", "-s", "http://localhost:11434/api/generate",
        "-d", json.dumps(payload)
    ],
    capture_output=True,
    text=True
)

# Parseo estilo jq + tr
try:
    lines = result.stdout.splitlines()
    response = ""
    for line in lines:
        if not line.strip():
            continue
        obj = json.loads(line)
        if "response" in obj and obj["response"] is not None:
            response += obj["response"]
    print(response.strip())
except Exception as e:
    print("Error parsing output:", e)
    print(result.stdout)
```

### blog

```sql
-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 23-10-2025 a las 19:05:19
-- Versión del servidor: 8.0.43-0ubuntu0.24.04.1
-- Versión de PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `blog`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entradas`
--

CREATE TABLE `entradas` (
  `Identificador` int NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `fecha` date NOT NULL,
  `contenido` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `Identificador` int NOT NULL,
  `usuario` varchar(255) NOT NULL,
  `contrasena` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `entradas`
--
ALTER TABLE `entradas`
  ADD PRIMARY KEY (`Identificador`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Identificador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `entradas`
--
ALTER TABLE `entradas`
  MODIFY `Identificador` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `Identificador` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
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


<a id="programacion-multihilo"></a>
# Programación multihilo

<a id="contexto-de-ejecucion-de-los-hilos"></a>
## Contexto de ejecución de los hilos

<a id="estados-de-un-hilo-cambios-de-estado"></a>
## Estados de un hilo. Cambios de estado

En el mundo de la programación multihilo, cada hilo es un flujo independiente dentro del mismo proceso. Cada uno tiene su propio contexto de ejecución, incluyendo variables locales y pilas de llamadas. Sin embargo, estos hilos no se ejecutan en paralelo; en lugar de eso, el sistema operativo asigna rápidamente el control entre los hilos para simular la concurrencia.

El estado de un hilo puede cambiar constantemente a lo largo del tiempo. Algunos de los estados más comunes incluyen "NEW" (nuevo), "RUNNABLE" (ejecutable), "BLOCKED" (bloqueado), "WAITING" (esperando) y "TERMINATED" (terminado). Cada estado representa una situación diferente en la vida del hilo.

Cuando un hilo se encuentra en el estado "NEW", significa que ha sido creado pero aún no ha comenzado a ejecutarse. El sistema operativo lo coloca en el estado "RUNNABLE" cuando está listo para ser ejecutado, pero es posible que no esté en la CPU debido a la planificación del procesador.

El estado "BLOCKED" ocurre cuando un hilo se encuentra esperando una condición específica. Esto puede ser el acceso a un recurso compartido o la finalización de otra operación. Mientras está bloqueado, el hilo no consume CPU y el sistema operativo lo coloca en este estado para evitar que consuma recursos innecesarios.

El estado "WAITING" es similar al bloqueo, pero se utiliza cuando un hilo espera a que otro hilo o componente del sistema realice una acción. Por ejemplo, un hilo puede esperar a que un recurso esté disponible antes de continuar su ejecución.

Finalmente, el estado "TERMINATED" indica que el hilo ha finalizado su ejecución y no puede volver a comenzar. El sistema operativo libera todos los recursos asociados al hilo para que puedan ser utilizados por otros procesos o hilos.

La transición entre estos estados ocurre de manera automática, controlada por el sistema operativo. Los programadores pueden interactuar con estos estados mediante métodos proporcionados por las bibliotecas de multihilo, como `start()`, `join()`, `sleep()` y `wait()`. Estos métodos permiten iniciar la ejecución de un hilo, esperar a que otro hilo termine su ejecución, pausar el hilo actual o hacer que el hilo actual espere a que se cumpla una condición.

La comprensión de los estados de un hilo y cómo cambiar entre ellos es fundamental para la programación multihilo. Permite al programador controlar el flujo de ejecución, evitar condiciones de carrera y optimizar el uso de recursos del sistema. A través de la planificación cuidadosa de los hilos y su estado, se pueden crear aplicaciones más eficientes y escalables.

En resumen, los estados de un hilo en programación multihilo representan diferentes fases de su vida. Desde su creación hasta su finalización, cada hilo pasa por varios estados, controlados automáticamente por el sistema operativo. Comprender estos estados y cómo interactuar con ellos es esencial para desarrollar aplicaciones concurrentes y eficientes.

<a id="librerias-y-clases"></a>
## Librerías y clases

La programación multihilo es una técnica fundamental para crear aplicaciones que pueden realizar múltiples tareas simultáneamente, mejorando así la eficiencia y el rendimiento. En esta subunidad, exploraremos las librerías y clases disponibles en diferentes entornos de desarrollo para facilitar la implementación de programación multihilo.

En Java, por ejemplo, la clase `Thread` proporciona una forma directa de crear e iniciar hilos. Cada hilo puede ejecutar un método `run()` que contiene el código a ser ejecutado en paralelo con los demás hilos. Además, Java ofrece la clase `ExecutorService`, que permite gestionar y administrar un grupo de hilos de manera más eficiente.

En Python, la biblioteca estándar `threading` proporciona una interfaz para trabajar con hilos. Permite crear objetos `Thread` que encapsulan el código a ejecutar en paralelo. La clase `Lock` es útil para sincronizar acceso a recursos compartidos entre hilos, evitando problemas como la condición de carrera.

C# ofrece la clase `Thread` y también proporciona la interfaz `IAsyncResult` para trabajar con operaciones asíncronas. Además, el espacio de nombres `System.Threading.Tasks` introduce la clase `Task`, que representa una unidad de trabajo asincrónica y puede ser más fácil de usar y manejar que los hilos tradicionales.

En C++, a pesar de no tener clases nativas para hilos como en Java o Python, se puede utilizar la biblioteca estándar `<thread>` introducida en C++11. Esta biblioteca proporciona una interfaz moderna y segura para trabajar con hilos, incluyendo funciones para crear, unir y gestionar hilos.

Las librerías y clases disponibles varían según el lenguaje de programación y la plataforma, pero generalmente ofrecen funcionalidades comunes como la creación y gestión de hilos, sincronización de acceso a recursos compartidos, y manejo de excepciones. Utilizar estas herramientas adecuadamente es crucial para desarrollar aplicaciones multihilo eficientes y seguras.

Es importante recordar que aunque la programación multihilo puede mejorar el rendimiento, también introduce complejidades adicionales en términos de gestión de recursos y control de concurrencia. Por lo tanto, es fundamental entender los conceptos básicos de sincronización y coordinación entre hilos para evitar problemas como la condición de carrera y la incoherencia de datos.

Además, al trabajar con múltiples hilos, es crucial considerar el uso adecuado de memoria compartida. Las variables globales o estáticas pueden ser accedidas por múltiples hilos simultáneamente, lo que requiere cuidados adicionales para evitar problemas como la sobrecarga y la corrupción de datos.

En resumen, las librerías y clases disponibles en diferentes entornos de desarrollo facilitan la implementación de programación multihilo, pero su uso adecuado requiere una comprensión profunda de los conceptos básicos de concurrencia. Al aprender a utilizar estas herramientas eficazmente, se puede crear software más potente y escalable que pueda aprovechar al máximo las capacidades modernas de procesadores y sistemas operativos multiprocesador.

<a id="gestion-de-hilos-prioridades"></a>
## Gestión de hilos. Prioridades

En el mundo de la programación, los hilos son un concepto fundamental que permite la ejecución simultánea de varias partes de un programa. Cada hilo opera dentro del mismo espacio de memoria principal, lo que significa que comparten variables globales y pueden interactuar entre sí sin necesidad de mecanismos adicionales complejos.

La gestión de hilos es una habilidad crucial para desarrolladores que desean optimizar el rendimiento de sus aplicaciones. Al asignar tareas a diferentes hilos, se puede aprovechar mejor la capacidad de procesamiento paralela del sistema operativo, lo que resulta en tiempos de respuesta más rápidos y mayor eficiencia.

La prioridad de un hilo es un valor numérico que indica su urgencia o importancia dentro del sistema. Los hilos con una alta prioridad son ejecutados antes que los hilos con una prioridad baja, a menos que se produzca algún tipo de bloqueo o espera por parte de los hilos de mayor prioridad.

La gestión de la prioridad de los hilos es un aspecto delicado y requiere cuidado. Un hilo con una prioridad demasiado alta puede bloquear otros hilos necesarios, lo que puede llevar a problemas como el colapso del sistema o la inactividad de ciertas partes de la aplicación. Por lo tanto, es crucial equilibrar las prioridades adecuadamente para evitar estos problemas.

Además de la gestión de prioridades, los desarrolladores también deben considerar otros aspectos importantes al trabajar con hilos. Esto incluye la sincronización entre hilos, que implica asegurarse de que los hilos no accedan simultáneamente a recursos compartidos de manera insegura, y el manejo de excepciones, que es crucial para evitar la propagación de errores y mantener la estabilidad del sistema.

La programación multihilo también requiere una buena comprensión de las características del lenguaje de programación utilizado. Algunos lenguajes tienen soporte nativo para hilos, mientras que otros pueden requerir el uso de bibliotecas o frameworks adicionales para implementar la funcionalidad.

En resumen, la gestión de hilos y sus prioridades es un aspecto crucial de la programación moderna. A través del manejo adecuado de los hilos, los desarrolladores pueden crear aplicaciones más eficientes y responsivas, lo que resulta en una mejor experiencia para los usuarios finales.

<a id="sincronizacion-de-hilos"></a>
## Sincronización de hilos

La sincronización de hilos es un aspecto crucial en la programación multihilo, ya que permite controlar el acceso a recursos compartidos entre múltiples hilos. En Java, esta sincronización se realiza mediante bloques `synchronized` o métodos marcados como `synchronized`. Estos elementos aseguran que solo un hilo pueda acceder al bloque de código o método en cualquier momento, evitando así condiciones de carrera y garantizando la consistencia de los datos.

Un bloque `synchronized` se define utilizando una expresión que evalúa a un objeto. Cualquier otro hilo intentará adquirir el mismo bloque solo si no lo posee el hilo actualmente ejecutándose en ese bloque. Si el bloque está ocupado, el hilo esperará hasta que la propiedad del bloque sea liberada.

Además de los bloques `synchronized`, Java ofrece la clase `ReentrantLock` como una alternativa más flexible y poderosa para la sincronización. Esta clase permite adquirir y liberar explícitamente un bloque de código, lo que puede ser útil en situaciones donde se requiere mayor control sobre el flujo del programa.

La sincronización no solo es importante para evitar problemas de concurrencia, sino también para mejorar el rendimiento del programa. Al asegurar que los hilos accedan a recursos compartidos de manera ordenada y secuencial, se reduce la posibilidad de errores y aumenta la eficiencia en la utilización de los recursos.

Es importante recordar que, aunque la sincronización es una herramienta poderosa, también puede llevar a problemas como el bloqueo o la ineficiencia. Por lo tanto, es crucial diseñar correctamente las secciones sincronizadas y considerar alternativas más eficientes cuando sea posible.

En resumen, la sincronización de hilos es un concepto fundamental en programación multihilo que permite controlar el acceso a recursos compartidos entre múltiples hilos. A través de bloques `synchronized` o la clase `ReentrantLock`, se puede asegurar la consistencia de los datos y mejorar el rendimiento del programa, aunque es importante utilizar estas herramientas con cuidado para evitar problemas de concurrencia.

<a id="comparticion-de-informacion-entre-hilos"></a>
## Compartición de información entre hilos

En la programación multihilo, una de las cuestiones más cruciales es cómo compartir información entre los hilos. La comunicación eficiente entre hilos es fundamental para mantener el flujo de trabajo coherente y evitar conflictos de acceso a recursos compartidos. Para lograr esta comunicación, se utilizan mecanismos específicos que permiten la sincronización y la transferencia de datos.

El primer paso en compartir información entre hilos es entender cómo los hilos interactúan con el mismo espacio de memoria. Cada hilo tiene su propio contexto de ejecución, pero comparten el espacio de memoria del proceso en el que se crearon. Esto significa que cualquier variable declarada en el ámbito global o estático puede ser accedida y modificada por todos los hilos.

Para evitar problemas como la corrupción de datos o inconsistencias, es crucial implementar mecanismos de sincronización adecuados. Las barreras (barriers) son herramientas útiles para asegurar que un hilo no continúe su ejecución hasta que todos los hilos en una colección hayan llegado a un punto específico en el código. Esto es especialmente útil cuando se necesita que varios hilos trabajen juntos en una tarea y deben esperar mutuamente antes de continuar.

Otro mecanismo importante para compartir información entre hilos es la utilización de variables de condición (condition variables). Estas variables permiten a los hilos esperar hasta que ciertas condiciones se cumplan. Por ejemplo, un hilo puede esperar hasta que otro hilo termine de procesar una tarea antes de continuar con su ejecución.

Además de las barreras y las variables de condición, también existen mecanismos como los semáforos (semaphores) y los mutexes (mutexes). Los semáforos son contadores que controlan el acceso a recursos compartidos. Cuando un hilo necesita acceder a un recurso protegido por un semáforo, debe decrementar el contador. Si el contador es mayor que cero, el hilo puede continuar su ejecución; de lo contrario, se bloqueará hasta que otro hilo incremente el contador.

Los mutexes son una forma más simple y directa de controlar el acceso a recursos compartidos. Un mutex es un objeto que puede estar en dos estados: bloqueado o no bloqueado. Cuando un hilo necesita acceder a un recurso protegido por un mutex, debe intentar adquirir el mutex. Si el mutex está disponible, el hilo lo adquiere y puede continuar su ejecución; de lo contrario, se bloqueará hasta que otro hilo libere el mutex.

La compartición de información entre hilos también implica la transferencia de datos. Para esto, existen varias estrategias. Una de las más comunes es usar estructuras de datos como listas o colas sincronizadas. Estas estructuras garantizan que los hilos puedan agregar y eliminar elementos sin conflictos de acceso.

Es importante destacar que la comunicación entre hilos debe ser siempre segura y eficiente. La programación multihilo puede volverse compleja debido a las interacciones entre hilos, por lo que es crucial seguir buenas prácticas y utilizar herramientas adecuadas para evitar problemas como el deadlock o la race condition.

En resumen, compartir información entre hilos en la programación multihilo requiere una comprensión profunda de cómo los hilos interactúan con el espacio de memoria compartido y cómo se pueden implementar mecanismos de sincronización adecuados. La utilización de barreras, variables de condición, semáforos y mutexes es fundamental para garantizar la coherencia y la seguridad de la información compartida entre hilos.

<a id="programacion-de-aplicaciones-multihilo"></a>
## Programación de aplicaciones multihilo

La programación multihilo es una técnica fundamental para crear aplicaciones que pueden realizar múltiples tareas simultáneamente, mejorando así la eficiencia y la respuesta del sistema. En esta subunidad, exploraremos cómo implementar la programación multihilo en diferentes entornos de desarrollo, desde plataformas nativas hasta bibliotecas de alto nivel.

En primer lugar, es importante entender los conceptos básicos de hilos y procesos. Un hilo es una unidad mínima de ejecución dentro de un proceso, lo que permite compartir recursos entre ellas. Cada hilo tiene su propio contexto de ejecución, incluyendo su propia pila de llamadas y variables locales.

La programación multihilo se realiza a través de la creación e inicio de hilos individuales. En muchos lenguajes de programación modernos, como Java o Python, hay bibliotecas específicas que facilitan esta tarea. Por ejemplo, en Java, se puede crear un hilo utilizando la clase `Thread` y sobrescribiendo su método `run()`, mientras que en Python, se pueden utilizar las clases `threading.Thread` y `concurrent.futures.ThreadPoolExecutor`.

La sincronización entre hilos es otro aspecto crucial de la programación multihilo. Cuando varios hilos acceden simultáneamente a los mismos recursos compartidos, puede producirse una condición de carrera, donde el resultado final depende del orden en que se ejecutan las operaciones. Para evitar esto, se utilizan mecanismos como semáforos, barreras y monitores para controlar el acceso a los recursos.

La gestión de hilos también implica la planificación y la priorización. Los sistemas operativos asignan tiempo de procesador a cada hilo en función de su prioridad, lo que puede afectar la respuesta del sistema. Es importante diseñar las aplicaciones multihilo para minimizar el uso de recursos y maximizar la eficiencia.

En aplicaciones móviles, la programación multihilo se utiliza comúnmente para realizar tareas intensivas en segundo plano sin bloquear la interfaz de usuario principal. Esto permite que los usuarios interactúen con la aplicación mientras se realizan operaciones como descargas o procesamiento de datos.

La programación multihilo también es fundamental para el desarrollo de aplicaciones web, donde es común manejar múltiples solicitudes simultáneamente. Frameworks como Node.js utilizan un modelo de programación basado en hilos para manejar la concurrencia eficientemente.

En resumen, la programación multihilo es una habilidad esencial para desarrollar aplicaciones que requieren alta eficiencia y respuesta. A través del uso de hilos, sincronización y planificación adecuada, se pueden crear sistemas capaces de manejar múltiples tareas simultáneamente, mejorando así la experiencia del usuario y el rendimiento general del sistema.


<a id="programacion-de-comunicaciones-en-red"></a>
# Programación de comunicaciones en red

<a id="comunicacion-entre-aplicaciones"></a>
## Comunicación entre aplicaciones

La comunicación entre aplicaciones es un aspecto fundamental del desarrollo de software moderno, permitiendo la interacción eficiente y segura de diferentes componentes de una aplicación o incluso sistemas distribuidos. En esta subunidad, exploraremos los conceptos básicos y técnicas utilizadas para establecer y gestionar comunicaciones entre aplicaciones en red.

La comunicación entre aplicaciones puede realizarse a través de diversos protocolos y mecanismos, cada uno con sus propias ventajas y desventajas. Uno de los protocolos más comunes es el Protocolo de Transferencia de Hipertexto (HTTP), utilizado para la comunicación web. Este protocolo permite que las aplicaciones cliente soliciten recursos a servidores web y reciban respuestas en formato HTML, XML o JSON.

Además de HTTP, existen otros protocolos específicos diseñados para aplicaciones particulares. Por ejemplo, el Protocolo de Transferencia de Archivos (FTP) se utiliza para transferir archivos entre sistemas, mientras que el Protocolo de Mensajería Simple (SMTP) es utilizado para enviar correos electrónicos.

La comunicación entre aplicaciones no solo implica el intercambio de datos, sino también la coordinación de acciones y eventos. Para esto, existen mecanismos como los sockets, que permiten establecer conexiones bidireccionales entre aplicaciones. Los sockets son objetos que proporcionan una interfaz para enviar y recibir datos a través de una red.

Además de los sockets, las aplicaciones pueden utilizar bibliotecas y frameworks específicos para facilitar la comunicación en redes. Por ejemplo, en Java, el paquete `java.net` ofrece clases y interfaces para crear aplicaciones cliente y servidor que utilizan sockets. En Python, la biblioteca `socket` proporciona una interfaz similar.

La seguridad es un aspecto crucial de cualquier comunicación entre aplicaciones, especialmente cuando se trata de transmisiones por Internet. Para garantizar la confidencialidad y integridad de los datos, existen protocolos criptográficos como SSL/TLS que cifran las comunicaciones entre cliente y servidor.

La gestión de errores es otro aspecto importante en la comunicación entre aplicaciones. Es común que ocurran problemas durante el intercambio de datos, como conexiones interrumpidas o paquetes corruptos. Por lo tanto, es necesario implementar mecanismos para detectar y manejar estos errores de manera efectiva.

La eficiencia en la comunicación entre aplicaciones también es un factor clave. Esto implica optimizar el uso de recursos como la banda ancha y el tiempo de respuesta. Para lograr esto, se pueden utilizar técnicas como la multiplexación de conexiones o la implementación de protocolos de transmisión eficientes.

En conclusión, la comunicación entre aplicaciones es un componente fundamental del desarrollo moderno de software. A través de diversos protocolos y mecanismos, las aplicaciones pueden intercambiar datos y coordinar acciones de manera segura y eficiente. Comprender estos conceptos es crucial para desarrolladores que trabajan en sistemas distribuidos o aplicaciones web complejas.

### .env

```
SMTP_SERVER=smtp.ionos.es
SMTP_PORT=587
SMTP_USER=info@dibujant.es
SMTP_PASSWORD=TAME123$
```

### envio smtp

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587  # 465 si usas SSL directo
SMTP_USER = "tuusuario@example.com"
SMTP_PASSWORD = "tu_password"

# Mensaje
remitente = "tuusuario@example.com"
destinatario = "alguien@example.com"
asunto = "Correo enviado desde Python"
cuerpo = "Hola,\n\nEste correo lo he enviado con Python 😄\n\nSaludos!"

# Crear mensaje MIME
mensaje = MIMEMultipart()
mensaje["From"] = remitente
mensaje["To"] = destinatario
mensaje["Subject"] = asunto
mensaje.attach(MIMEText(cuerpo, "plain"))

# Enviar
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Si el servidor requiere TLS
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(remitente, destinatario, mensaje.as_string())
    server.quit()
    print("Correo enviado con éxito ✨")
except Exception as e:
    print("Error enviando el correo:", e)
```

### envio con carga de entorno

```python
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv()  # carga .env automáticamente

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

msg = MIMEText("Hola desde Python con variables ocultas 😎")
msg["Subject"] = "Test"
msg["From"] = SMTP_USER
msg["To"] = "jocarsa2@gmail.com"

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(SMTP_USER, msg["To"], msg.as_string())
```

### leer csv online

```python
import requests
import csv
from io import StringIO

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1whDcBEU6BnFwlVZHICoMdkGU_au42HiWaPoNschUDr2ri7baRZDjWofnMlxnQKk35raLVm9rIKQk/pub?output=csv"

# Descarga del CSV
resp = requests.get(url)
resp.raise_for_status()   # por si algo va mal

# Convertimos texto → CSV
data = list(csv.reader(StringIO(resp.text)))

# Mostrar por consola
for row in data:
    print(row)
```

### resultado como diccionario

```python
import requests
import csv
from io import StringIO

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1whDcBEU6BnFwlVZHICoMdkGU_au42HiWaPoNschUDr2ri7baRZDjWofnMlxnQKk35raLVm9rIKQk/pub?output=csv"

# Descargar CSV
resp = requests.get(url)
resp.raise_for_status()

# Convertir a diccionarios usando la primera fila como keys
f = StringIO(resp.text)
reader = csv.DictReader(f)

rows = list(reader)

# Mostrar cada fila como diccionario
for r in rows:
    print(r)
```

### compruebo dias para que empiece el curso

```python
import requests
import csv
from io import StringIO

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1whDcBEU6BnFwlVZHICoMdkGU_au42HiWaPoNschUDr2ri7baRZDjWofnMlxnQKk35raLVm9rIKQk/pub?output=csv"

# Descargar CSV
resp = requests.get(url)
resp.raise_for_status()

# Convertir a diccionarios usando la primera fila como keys
f = StringIO(resp.text)
reader = csv.DictReader(f)

rows = list(reader)

# Mostrar cada fila como diccionario
for r in rows:
    print("Nombre del alumno: "+r['Nombre completo'])
    print("Curso: "+r['Curso'])
    print("Fecha: "+r['Fecha de inicio'])
    print("######################")
```

### compruebo la fecha ahora si

```python
import requests
import csv
from io import StringIO
from datetime import date, datetime

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1whDcBEU6BnFwlVZHICoMdkGU_au42HiWaPoNschUDr2ri7baRZDjWofnMlxnQKk35raLVm9rIKQk/pub?output=csv"

# Descargar CSV
resp = requests.get(url)
resp.raise_for_status()

# Convertir a diccionarios usando la primera fila como keys
f = StringIO(resp.text)
reader = csv.DictReader(f)

rows = list(reader)

# Mostrar cada fila como diccionario
for r in rows:
    print("Nombre del alumno: "+r['Nombre completo'])
    print("Curso: "+r['Curso'])
    print("Fecha: "+r['Fecha de inicio'])
    fecha_str = r['Fecha de inicio']  # tu fecha
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

    hoy = date.today()
    diff = (hoy - fecha).days
    if diff == -3:
      print("Faltan 3 dias para que empiece el curso")
    print("######################")
```

### envio correo

```python
import requests
import csv
from io import StringIO
from datetime import date, datetime

import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1whDcBEU6BnFwlVZHICoMdkGU_au42HiWaPoNschUDr2ri7baRZDjWofnMlxnQKk35raLVm9rIKQk/pub?output=csv"

# Descargar CSV
resp = requests.get(url)
resp.raise_for_status()

# Convertir a diccionarios usando la primera fila como keys
f = StringIO(resp.text)
reader = csv.DictReader(f)

rows = list(reader)

# Mostrar cada fila como diccionario
for r in rows:
    print("Nombre del alumno: "+r['Nombre completo'])
    print("Curso: "+r['Curso'])
    print("Fecha: "+r['Fecha de inicio'])
    fecha_str = r['Fecha de inicio']  # tu fecha
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

    hoy = date.today()
    diff = (hoy - fecha).days
    if diff == -3:
      print("Faltan 3 dias para que empiece el curso")
      load_dotenv()  # carga .env automáticamente

      SMTP_SERVER = os.getenv("SMTP_SERVER")
      SMTP_PORT = int(os.getenv("SMTP_PORT"))
      SMTP_USER = os.getenv("SMTP_USER")
      SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

      msg = MIMEText("Hola, "+r['Nombre completo']+" tu curso de "+r['Curso']+" empieza dentro de 3 dias")
      msg["Subject"] = "Test"
      msg["From"] = SMTP_USER
      msg["To"] = "jocarsa2@gmail.com"

      with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
          server.starttls()
          server.login(SMTP_USER, SMTP_PASSWORD)
          server.sendmail(SMTP_USER, msg["To"], msg.as_string())
      print("######################")
```

### correo estiloso

```python
import requests
import csv
from io import StringIO
from datetime import date, datetime

import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1whDcBEU6BnFwlVZHICoMdkGU_au42HiWaPoNschUDr2ri7baRZDjWofnMlxnQKk35raLVm9rIKQk/pub?output=csv"

# Descargar CSV
resp = requests.get(url)
resp.raise_for_status()

# Convertir a diccionarios usando la primera fila como keys
f = StringIO(resp.text)
reader = csv.DictReader(f)

rows = list(reader)

# Cargar variables de entorno SOLO una vez
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

hoy = date.today()

for r in rows:
    print("Nombre del alumno: " + r['Nombre completo'])
    print("Curso: " + r['Curso'])
    print("Fecha: " + r['Fecha de inicio'])

    fecha_str = r['Fecha de inicio']
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

    diff = (hoy - fecha).days  # si el curso es dentro de 3 días, diff será -3

    if diff == -3:
        print("Faltan 3 días para que empiece el curso")

        nombre = r['Nombre completo']
        curso = r['Curso']

        # --- HTML bonito con CSS inline ---
        html_body = f"""\
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Tu curso empieza en 3 días</title>
  <style>
    /* Estilos básicos (la mayoría de clientes los respetan) */
    body {{
      margin: 0;
      padding: 0;
      background-color: #0f172a;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    .wrapper {{
      width: 100%;
      padding: 32px 0;
    }}
    .container {{
      max-width: 600px;
      margin: 0 auto;
      background: #020617;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(15,23,42,0.8);
      border: 1px solid rgba(148,163,184,0.25);
    }}
    .header {{
      padding: 24px 32px 16px;
      background: radial-gradient(circle at top left, #22c55e, #0ea5e9 40%, #0b1120);
      color: #e5e7eb;
    }}
    .logo {{
      font-size: 12px;
      letter-spacing: .25em;
      text-transform: uppercase;
      opacity: 0.9;
    }}
    .title {{
      margin-top: 16px;
      font-size: 24px;
      font-weight: 700;
      line-height: 1.3;
    }}
    .badge {{
      display: inline-block;
      margin-top: 16px;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: .15em;
      background: rgba(15,23,42,0.7);
      border: 1px solid rgba(148,163,184,0.6);
      color: #e5e7eb;
    }}
    .content {{
      padding: 24px 32px 28px;
      color: #e5e7eb;
    }}
    .hello {{
      font-size: 15px;
      margin-bottom: 12px;
    }}
    .highlight-box {{
      margin: 18px 0 20px;
      padding: 14px 16px;
      border-radius: 14px;
      background: rgba(15,23,42,0.9);
      border: 1px solid rgba(148,163,184,0.35);
    }}
    .highlight-label {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: .16em;
      color: #9ca3af;
      margin-bottom: 6px;
    }}
    .highlight-value {{
      font-size: 15px;
      font-weight: 600;
      color: #e5e7eb;
    }}
    .date-row {{
      display: flex;
      gap: 10px;
      margin-top: 8px;
      font-size: 12px;
      color: #9ca3af;
    }}
    .pill {{
      padding: 4px 8px;
      border-radius: 999px;
      border: 1px solid rgba(148,163,184,0.4);
      background: rgba(15,23,42,0.85);
    }}
    .cta {{
      margin-top: 18px;
      text-align: center;
    }}
    .cta-button {{
      display: inline-block;
      padding: 10px 20px;
      border-radius: 999px;
      background: linear-gradient(90deg, #22c55e, #0ea5e9);
      color: #020617 !important;
      font-weight: 600;
      font-size: 14px;
      text-decoration: none;
      box-shadow: 0 14px 35px rgba(34,197,94,0.35);
    }}
    .cta-note {{
      margin-top: 10px;
      font-size: 12px;
      color: #9ca3af;
    }}
    .footer {{
      padding: 16px 32px 20px;
      font-size: 11px;
      color: #6b7280;
      background: #020617;
      border-top: 1px solid rgba(31,41,55,0.8);
    }}
    .footer small {{
      display: block;
      margin-top: 4px;
    }}

    @media (max-width: 640px) {{
      .container {{
        border-radius: 0;
      }}
      .header, .content, .footer {{
        padding-left: 18px;
        padding-right: 18px;
      }}
    }}
  </style>
</head>
<body>
  <div class="wrapper">
    <div class="container">
      <div class="header">
        <div class="logo">CAMPUS · CAPITOL FORMACIÓN</div>
        <div class="title">Tu curso empieza en 3 días 🎓</div>
        <div class="badge">Cuenta atrás para empezar</div>
      </div>

      <div class="content">
        <p class="hello">Hola <strong>{nombre}</strong>,</p>
        <p>
          Solo queríamos recordarte que tu curso está a punto de comenzar.
          Es un buen momento para revisar tu correo, acceder al campus y asegurarte
          de que puedes iniciar sesión sin problemas.
        </p>

        <div class="highlight-box">
          <div class="highlight-label">Curso</div>
          <div class="highlight-value">{curso}</div>

          <div class="date-row">
            <div class="pill">Fecha de inicio: {fecha_str}</div>
            <div class="pill">Empieza en 3 días</div>
          </div>
        </div>

        <p>
          El día de inicio tendrás acceso al contenido, actividades y recursos
          del curso. Si tienes cualquier problema de acceso o duda, puedes
          responder a este correo y te ayudaremos.
        </p>

        <div class="cta">
          <a href="https://campus.capitolformacion.com" class="cta-button">
            Ir al campus virtual
          </a>
          <div class="cta-note">
            Consejo: añade este correo a tus contactos para no perder futuras notificaciones.
          </div>
        </div>
      </div>

      <div class="footer">
        Este es un aviso automático de inicio de curso.
        <small>Si ya has recibido este recordatorio o ya has accedido al campus, puedes ignorar este mensaje.</small>
      </div>
    </div>
  </div>
</body>
</html>
"""

        # Crear mensaje MIME como HTML
        msg = MIMEText(html_body, "html", "utf-8")
        msg["Subject"] = f"Tu curso de {curso} empieza en 3 días"
        msg["From"] = SMTP_USER
        msg["To"] = "jocarsa2@gmail.com"  # o el correo del alumno si lo añades al CSV

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(msg["From"], [msg["To"]], msg.as_string())

        print("Correo HTML enviado ✅")
        print("######################")
```

<a id="roles-cliente-y-servidor"></a>
## Roles cliente y servidor

En el campo de la programación de servicios y procesos, una distinción fundamental es la diferencia entre los roles de cliente y servidor. Estos dos papeles desempeñan un papel crucial en la comunicación eficiente y segura en redes.

El cliente es aquel que inicia la solicitud de información o servicio a otro sistema, conocido como servidor. Este puede ser cualquier programa informático que necesite acceso a recursos remotos. Por ejemplo, cuando accedemos a una página web desde nuestro navegador, el navegador actúa como cliente solicitando contenido al servidor web.

Por su parte, el servidor es el sistema que recibe las solicitudes del cliente y proporciona la información o servicio solicitado. En el caso de una página web, el servidor contiene los archivos HTML, CSS y JavaScript que forman la página y responde a las peticiones del navegador para mostrarla.

La comunicación entre cliente y servidor se realiza mediante protocolos estándar como HTTP (Hypertext Transfer Protocol) o HTTPS (Hypertext Transfer Protocol Secure). Estos protocolos definen cómo los datos son enviados y recibidos, asegurando que la información fluya de manera segura y coherente.

El diseño de sistemas cliente-servidor permite una arquitectura escalable y distribuida. Los clientes pueden acceder a servicios desde cualquier lugar con conexión a internet, mientras que el servidor puede manejar múltiples solicitudes simultáneamente, lo que mejora la eficiencia y la capacidad del sistema.

Además de la comunicación básica, los sistemas cliente-servidor también implementan funciones adicionales como autenticación, autorización y encriptación para proteger la información durante el tránsito. La autenticación verifica la identidad del cliente, mientras que la autorización determina qué acciones puede realizar dentro del sistema. La encriptación cifra los datos para evitar su interceptación por terceros.

La programación de comunicaciones en red requiere una comprensión profunda de estos roles y cómo interactúan entre sí. Los desarrolladores deben estar familiarizados con las bibliotecas y componentes disponibles para manejar la comunicación, como sockets, protocolos de transporte y mecanismos de sincronización.

En resumen, el rol de cliente y servidor es fundamental en la programación de servicios y procesos. Comprender estos conceptos y cómo implementarlos correctamente es esencial para crear sistemas eficientes, seguros y escalables que puedan proporcionar acceso a recursos remotos de manera confiable.

### leer correo

```
<?php
// leer_imap.php

// Ruta absoluta recomendada (fuera de /var/www/html si es posible)
require 'imap_config.php';

// Comprobar que $IMAP_CONFIG existe
if (!isset($IMAP_CONFIG) || !is_array($IMAP_CONFIG)) {
    die('Error: configuración IMAP no cargada.');
}

$mailbox = $IMAP_CONFIG['mailbox'];
$user    = $IMAP_CONFIG['user'];
$pass    = $IMAP_CONFIG['pass'];

// Abrir bandeja de entrada
$inbox = @imap_open($mailbox, $user, $pass);

if (!$inbox) {
    die('No se pudo conectar al servidor IMAP: ' . imap_last_error());
}

// Buscar todos los mensajes
$emails = imap_search($inbox, 'ALL');

if ($emails === false) {
    echo "No hay correos o error en la búsqueda.\n";
} else {
    // Mostrar los últimos 10
    rsort($emails); // del más nuevo al más antiguo
    $emails = array_slice($emails, 0, 10);

    foreach ($emails as $num) {
        $overview = imap_fetch_overview($inbox, $num, 0)[0];

        echo "----------------------------------------\n";
        echo "Nº:      {$overview->msgno}\n";
        echo "Fecha:   {$overview->date}\n";
        echo "De:      {$overview->from}\n";
        echo "Asunto:  {$overview->subject}\n";
        echo "Leído:   " . ($overview->seen ? 'Sí' : 'No') . "\n";
    }
}

imap_close($inbox);
```

### correo con estilo

```
<?php
// leer_imap.php

// Ruta absoluta recomendada (fuera de /var/www/html si es posible)
require 'imap_config.php';

// Comprobar que $IMAP_CONFIG existe
if (!isset($IMAP_CONFIG) || !is_array($IMAP_CONFIG)) {
    die('Error: configuración IMAP no cargada.');
}

$mailbox = $IMAP_CONFIG['mailbox'];
$user    = $IMAP_CONFIG['user'];
$pass    = $IMAP_CONFIG['pass'];

// Abrir bandeja de entrada
$inbox = @imap_open($mailbox, $user, $pass);

if (!$inbox) {
    die('No se pudo conectar al servidor IMAP: ' . imap_last_error());
}

// Buscar todos los mensajes
$emails = imap_search($inbox, 'ALL');

if ($emails === false) {
    echo "No hay correos o error en la búsqueda.\n";
} else {
    // Mostrar los últimos 10
    rsort($emails); // del más nuevo al más antiguo
    $emails = array_slice($emails, 0, 10);

    foreach ($emails as $num) {
        $overview = imap_fetch_overview($inbox, $num, 0)[0];

        echo "----------------------------------------\n";
        echo "Nº:      {$overview->msgno}\n";
        echo "Fecha:   {$overview->date}\n";
        echo "De:      {$overview->from}\n";
        echo "Asunto:  {$overview->subject}\n";
        echo "Leído:   " . ($overview->seen ? 'Sí' : 'No') . "\n";
    }
}

imap_close($inbox);
```

### correo como blog

```
<?php
// leer_imap.php

require 'imap_config.php';

if (!isset($IMAP_CONFIG) || !is_array($IMAP_CONFIG)) {
    die('Error: configuración IMAP no cargada.');
}

$mailbox = $IMAP_CONFIG['mailbox'];
$user    = $IMAP_CONFIG['user'];
$pass    = $IMAP_CONFIG['pass'];

// Carpeta para guardar imágenes adjuntas
$attachmentsDir = __DIR__ . '/attachments';
if (!is_dir($attachmentsDir)) {
    mkdir($attachmentsDir, 0775, true);
}

// ----------------- Helpers -----------------

/**
 * Decodifica cabeceras MIME (ej. Subject)
 */
function decode_mime_str($string, $targetCharset = 'UTF-8') {
    $elements = imap_mime_header_decode($string);
    $result = '';
    foreach ($elements as $element) {
        $charset = ($element->charset == 'default') ? 'ISO-8859-1' : $element->charset;
        $result .= iconv($charset, $targetCharset . '//TRANSLIT', $element->text);
    }
    return $result;
}

/**
 * Decodifica el cuerpo según la codificación indicada
 */
function decode_body($body, $encoding) {
    switch ($encoding) {
        case ENCBASE64:
            return base64_decode($body);
        case ENCQUOTEDPRINTABLE:
            return quoted_printable_decode($body);
        default:
            return $body;
    }
}

/**
 * Obtiene el cuerpo del mensaje en HTML si existe, o texto plano si no.
 * Devuelve HTML seguro para mostrar en la web.
 */
function get_body_as_html($inbox, $msgno) {
    $structure = imap_fetchstructure($inbox, $msgno);

    // Función recursiva para recorrer las partes
    $html = null;
    $plain = null;

    $walkParts = function ($structure, $prefix = '') use ($inbox, $msgno, &$html, &$plain, &$walkParts) {
        $partNumber = $prefix === '' ? '1' : $prefix;

        if (!isset($structure->parts)) {
            // Parte simple
            if ($structure->type == TYPETEXT) {
                $subtype = strtoupper($structure->subtype ?? '');
                $body = imap_fetchbody($inbox, $msgno, $partNumber);
                $body = decode_body($body, $structure->encoding);

                if ($subtype === 'HTML') {
                    $html = $body;
                } elseif ($subtype === 'PLAIN') {
                    // Guardamos solo si aún no hay texto plano
                    if ($plain === null) {
                        $plain = $body;
                    }
                }
            }
        } else {
            // Multipart
            foreach ($structure->parts as $index => $part) {
                $subPrefix = $prefix === '' ? strval($index + 1) : $prefix . '.' . ($index + 1);
                $walkParts($part, $subPrefix);
            }
        }
    };

    $walkParts($structure);

    if ($html !== null) {
        // Devolvemos directamente el HTML del correo (opcionalmente podrías sanearlo)
        return $html;
    } elseif ($plain !== null) {
        // Convertimos texto plano a HTML básico
        return nl2br(htmlspecialchars($plain, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'));
    } else {
        return '<p><em>(Sin contenido)</em></p>';
    }
}

/**
 * Guarda la primera imagen adjunta (attachment o inline) y devuelve la ruta relativa para usar en <img>.
 * Si no hay imagen, devuelve null.
 */
function get_first_image_attachment($inbox, $msgno, $attachmentsDir) {
    $structure = imap_fetchstructure($inbox, $msgno);
    if (!isset($structure->parts)) {
        return null; // Sin partes = probablemente sin adjuntos
    }

    $firstImagePath = null;

    $saveImage = function ($part, $partNumber) use ($inbox, $msgno, $attachmentsDir, &$firstImagePath) {
        // Tipos: 0 = text, 1 = multipart, 2 = message, 3 = application, 4 = audio, 5 = image, 6 = video, 7 = other
        $isImageType = ($part->type == 5); // 5 = image
        $subtype = strtoupper($part->subtype ?? '');

        if (!$isImageType) {
            // Algunos servidores pueden poner las imágenes como application/octet-stream,
            // si quisieras ser más agresivo, podrías comprobar solo la extensión del nombre de archivo.
            return;
        }

        // Comprobar que es attachment o inline con nombre de archivo
        $filename = null;

        if (isset($part->dparameters)) {
            foreach ($part->dparameters as $dparam) {
                if (strtolower($dparam->attribute) == 'filename') {
                    $filename = $dparam->value;
                    break;
                }
            }
        }

        if ($filename === null && isset($part->parameters)) {
            foreach ($part->parameters as $param) {
                if (strtolower($param->attribute) == 'name') {
                    $filename = $param->value;
                    break;
                }
            }
        }

        if ($filename === null) {
            // Nombre por defecto si no viene en cabecera
            $filename = 'image_' . $msgno . '_' . str_replace('.', '_', $partNumber) . '.' . strtolower($subtype);
        }

        // Normalizar nombre
        $filename = preg_replace('/[^\w\.\-]/', '_', $filename);

        $body = imap_fetchbody($inbox, $msgno, $partNumber);
        $body = decode_body($body, $part->encoding);

        $fullPath = rtrim($attachmentsDir, '/') . '/' . $filename;
        file_put_contents($fullPath, $body);

        // Guardamos ruta relativa para usar en HTML
        $firstImagePath = 'attachments/' . $filename;
    };

    $walkParts = function ($structure, $prefix = '') use (&$walkParts, $saveImage, &$firstImagePath) {
        if ($firstImagePath !== null) {
            return; // ya tenemos una imagen
        }

        if (!isset($structure->parts)) {
            // Parte simple
            $partNumber = $prefix === '' ? '1' : $prefix;
            $saveImage($structure, $partNumber);
        } else {
            foreach ($structure->parts as $index => $part) {
                $partNumber = $prefix === '' ? strval($index + 1) : $prefix . '.' . ($index + 1);
                // Si la parte es multipart, seguimos bajando
                if (isset($part->parts)) {
                    $walkParts($part, $partNumber);
                } else {
                    $saveImage($part, $partNumber);
                }

                if ($firstImagePath !== null) {
                    break;
                }
            }
        }
    };

    $walkParts($structure);

    return $firstImagePath;
}

// ----------------- Lógica principal -----------------

$inbox = @imap_open($mailbox, $user, $pass);

if (!$inbox) {
    die('No se pudo conectar al servidor IMAP: ' . imap_last_error());
}

$emails = imap_search($inbox, 'ALL');

if ($emails === false) {
    echo "No hay correos o error en la búsqueda.\n";
    imap_close($inbox);
    exit;
}

// Orden más nuevo primero y limitar a 10
rsort($emails);
$emails = array_slice($emails, 0, 10);

// Salida HTML básica
echo "<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n";
echo "<meta charset=\"UTF-8\">\n<title>Correos como artículos</title>\n";
echo "<style>
body { font-family: system-ui, sans-serif; max-width: 800px; margin: 2rem auto; line-height: 1.6; }
article { border-bottom: 1px solid #ddd; padding: 1.5rem 0; }
article img { max-width: 100%; height: auto; display: block; margin: 1rem 0; }
article h2 { margin-top: 0; }
.meta { color: #666; font-size: 0.9em; margin-bottom: 0.5rem; }
</style>\n";
echo "</head>\n<body>\n";

foreach ($emails as $num) {
    // Cabeceras para sacar asunto (título)
    $header = imap_headerinfo($inbox, $num);

    $subject = isset($header->subject) ? decode_mime_str($header->subject) : '(Sin asunto)';
    $from    = isset($header->fromaddress) ? decode_mime_str($header->fromaddress) : '';
    $date    = isset($header->date) ? $header->date : '';

    $bodyHtml = get_body_as_html($inbox, $num);
    $imageSrc = get_first_image_attachment($inbox, $num, $attachmentsDir);

    echo "<article>\n";
    echo "  <h2>" . htmlspecialchars($subject, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . "</h2>\n";
    echo "  <div class=\"meta\">";
    if ($from) {
        echo "De: " . htmlspecialchars($from, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . " &mdash; ";
    }
    if ($date) {
        echo htmlspecialchars($date, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    }
    echo "</div>\n";

    if ($imageSrc !== null) {
        echo "  <img src=\"" . htmlspecialchars($imageSrc, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . "\" alt=\"Imagen del correo\">\n";
    }

    echo "  <div class=\"content\">\n";
    echo $bodyHtml;
    echo "  </div>\n";
    echo "</article>\n\n";
}

echo "</body>\n</html>";

imap_close($inbox);
```

### estilizado

```
<?php
// leer_imap.php

require 'imap_config.php';

if (!isset($IMAP_CONFIG) || !is_array($IMAP_CONFIG)) {
    die('Error: configuración IMAP no cargada.');
}

$mailbox = $IMAP_CONFIG['mailbox'];
$user    = $IMAP_CONFIG['user'];
$pass    = $IMAP_CONFIG['pass'];

// Carpeta para guardar imágenes adjuntas
$attachmentsDir = __DIR__ . '/attachments';
if (!is_dir($attachmentsDir)) {
    mkdir($attachmentsDir, 0775, true);
}

// ----------------- Helpers -----------------

/**
 * Decodifica cabeceras MIME (ej. Subject)
 */
function decode_mime_str($string, $targetCharset = 'UTF-8') {
    $elements = imap_mime_header_decode($string);
    $result = '';
    foreach ($elements as $element) {
        $charset = ($element->charset == 'default') ? 'ISO-8859-1' : $element->charset;
        $result .= iconv($charset, $targetCharset . '//TRANSLIT', $element->text);
    }
    return $result;
}

/**
 * Decodifica el cuerpo según la codificación indicada
 */
function decode_body($body, $encoding) {
    switch ($encoding) {
        case ENCBASE64:
            return base64_decode($body);
        case ENCQUOTEDPRINTABLE:
            return quoted_printable_decode($body);
        default:
            return $body;
    }
}

/**
 * Obtiene el cuerpo del mensaje en HTML si existe, o texto plano si no.
 * Devuelve HTML seguro para mostrar en la web.
 */
function get_body_as_html($inbox, $msgno) {
    $structure = imap_fetchstructure($inbox, $msgno);

    // Función recursiva para recorrer las partes
    $html = null;
    $plain = null;

    $walkParts = function ($structure, $prefix = '') use ($inbox, $msgno, &$html, &$plain, &$walkParts) {
        $partNumber = $prefix === '' ? '1' : $prefix;

        if (!isset($structure->parts)) {
            // Parte simple
            if ($structure->type == TYPETEXT) {
                $subtype = strtoupper($structure->subtype ?? '');
                $body = imap_fetchbody($inbox, $msgno, $partNumber);
                $body = decode_body($body, $structure->encoding);

                if ($subtype === 'HTML') {
                    $html = $body;
                } elseif ($subtype === 'PLAIN') {
                    // Guardamos solo si aún no hay texto plano
                    if ($plain === null) {
                        $plain = $body;
                    }
                }
            }
        } else {
            // Multipart
            foreach ($structure->parts as $index => $part) {
                $subPrefix = $prefix === '' ? strval($index + 1) : $prefix . '.' . ($index + 1);
                $walkParts($part, $subPrefix);
            }
        }
    };

    $walkParts($structure);

    if ($html !== null) {
        // Devolvemos directamente el HTML del correo (opcionalmente podrías sanearlo)
        return $html;
    } elseif ($plain !== null) {
        // Convertimos texto plano a HTML básico
        return nl2br(htmlspecialchars($plain, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'));
    } else {
        return '<p><em>(Sin contenido)</em></p>';
    }
}

/**
 * Guarda la primera imagen adjunta (attachment o inline) y devuelve la ruta relativa para usar en <img>.
 * Si no hay imagen, devuelve null.
 */
function get_first_image_attachment($inbox, $msgno, $attachmentsDir) {
    $structure = imap_fetchstructure($inbox, $msgno);
    if (!isset($structure->parts)) {
        return null; // Sin partes = probablemente sin adjuntos
    }

    $firstImagePath = null;

    $saveImage = function ($part, $partNumber) use ($inbox, $msgno, $attachmentsDir, &$firstImagePath) {
        // Tipos: 0 = text, 1 = multipart, 2 = message, 3 = application, 4 = audio, 5 = image, 6 = video, 7 = other
        $isImageType = ($part->type == 5); // 5 = image
        $subtype = strtoupper($part->subtype ?? '');

        if (!$isImageType) {
            // Algunos servidores pueden poner las imágenes como application/octet-stream,
            // si quisieras ser más agresivo, podrías comprobar solo la extensión del nombre de archivo.
            return;
        }

        // Comprobar que es attachment o inline con nombre de archivo
        $filename = null;

        if (isset($part->dparameters)) {
            foreach ($part->dparameters as $dparam) {
                if (strtolower($dparam->attribute) == 'filename') {
                    $filename = $dparam->value;
                    break;
                }
            }
        }

        if ($filename === null && isset($part->parameters)) {
            foreach ($part->parameters as $param) {
                if (strtolower($param->attribute) == 'name') {
                    $filename = $param->value;
                    break;
                }
            }
        }

        if ($filename === null) {
            // Nombre por defecto si no viene en cabecera
            $filename = 'image_' . $msgno . '_' . str_replace('.', '_', $partNumber) . '.' . strtolower($subtype);
        }

        // Normalizar nombre
        $filename = preg_replace('/[^\w\.\-]/', '_', $filename);

        $body = imap_fetchbody($inbox, $msgno, $partNumber);
        $body = decode_body($body, $part->encoding);

        $fullPath = rtrim($attachmentsDir, '/') . '/' . $filename;
        file_put_contents($fullPath, $body);

        // Guardamos ruta relativa para usar en HTML
        $firstImagePath = 'attachments/' . $filename;
    };

    $walkParts = function ($structure, $prefix = '') use (&$walkParts, $saveImage, &$firstImagePath) {
        if ($firstImagePath !== null) {
            return; // ya tenemos una imagen
        }

        if (!isset($structure->parts)) {
            // Parte simple
            $partNumber = $prefix === '' ? '1' : $prefix;
            $saveImage($structure, $partNumber);
        } else {
            foreach ($structure->parts as $index => $part) {
                $partNumber = $prefix === '' ? strval($index + 1) : $prefix . '.' . ($index + 1);
                // Si la parte es multipart, seguimos bajando
                if (isset($part->parts)) {
                    $walkParts($part, $partNumber);
                } else {
                    $saveImage($part, $partNumber);
                }

                if ($firstImagePath !== null) {
                    break;
                }
            }
        }
    };

    $walkParts($structure);

    return $firstImagePath;
}

// ----------------- Lógica principal -----------------

$inbox = @imap_open($mailbox, $user, $pass);

if (!$inbox) {
    die('No se pudo conectar al servidor IMAP: ' . imap_last_error());
}

$emails = imap_search($inbox, 'ALL');

if ($emails === false) {
    echo "No hay correos o error en la búsqueda.\n";
    imap_close($inbox);
    exit;
}

// Orden más nuevo primero y limitar a 10
rsort($emails);
$emails = array_slice($emails, 0, 10);

// Salida HTML básica
echo "<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n";
echo "<meta charset=\"UTF-8\">\n<title>Correos como artículos</title>\n";
echo "<style>
*{padding:0px;margin:0px;}
body { font-family: system-ui, sans-serif; max-width: 800px; margin: 2rem auto; line-height: 1.6; }
article { border-bottom: 1px solid #ddd; padding: 1.5rem 0; }
article img { max-width: 100%; height: auto; display: block; margin: 1rem 0; }
article h2 { margin-top: 0; }
.meta { color: #666; font-size: 0.9em; margin-bottom: 0.5rem; }
h1,h2{text-align:center;}
</style>\n";
echo "</head>\n<body>
  
  <h1>Jose Vicente Carratalá Sanchis</h1>
  <h2>Blog personal</h2>
\n";

foreach ($emails as $num) {
    // Cabeceras para sacar asunto (título)
    $header = imap_headerinfo($inbox, $num);

    $subject = isset($header->subject) ? decode_mime_str($header->subject) : '(Sin asunto)';
    $from    = isset($header->fromaddress) ? decode_mime_str($header->fromaddress) : '';
    $date    = isset($header->date) ? $header->date : '';

    $bodyHtml = get_body_as_html($inbox, $num);
    $imageSrc = get_first_image_attachment($inbox, $num, $attachmentsDir);

    echo "<article>\n";
    echo "  <h3>" . htmlspecialchars($subject, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . "</h3>\n";
    echo "  <div class=\"meta\">";
    
    if ($date) {
        echo htmlspecialchars($date, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    }
    echo "</div>\n";

    if ($imageSrc !== null) {
        echo "  <img src=\"" . htmlspecialchars($imageSrc, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . "\" alt=\"Imagen del correo\">\n";
    }

    echo "  <div class=\"content\">\n";
    echo $bodyHtml;
    echo "  </div>\n";
    echo "</article>\n\n";
}

echo "</body>\n</html>";

imap_close($inbox);
```

### imap_config

```
<?php
// imap_config.php

// Idealmente este archivo NO está dentro de /var/www/html
// y tiene permisos restrictivos (chmod 600, propietario correcto).

$IMAP_CONFIG = [
    'mailbox' => '{imap.ionos.es:993/imap/ssl}INBOX',
    'user'    => 'info@dibujant.es',
    'pass'    => 'TAME123$',
];
```

<a id="librerias-y-clases-1"></a>
## Librerías y clases

En este capítulo, nos adentramos en la programación de comunicaciones en red, un tema fundamental para el desarrollo de aplicaciones que requieren interacción con otros sistemas o usuarios a través de Internet. La comunicación en red se basa en el establecimiento de conexiones entre dos puntos distintos, donde cada punto puede ser un cliente o un servidor.

La programación de comunicaciones en red implica la utilización de librerías y clases específicas que facilitan la creación de aplicaciones que pueden enviar y recibir datos a través de Internet. Estas librerías proporcionan una interfaz para interactuar con los protocolos de comunicación, como TCP/IP, lo que permite a los desarrolladores centrarse en la lógica de negocio de su aplicación sin preocuparse por los detalles técnicos de la red.

Una de las clases más importantes para el desarrollo de aplicaciones de red es `Socket`. Los sockets son los puntos finales de una conexión de red. Cada socket tiene un dirección IP y un número de puerto que lo identifican dentro del sistema. La clase `Socket` proporciona métodos para crear, conectar, enviar y recibir datos a través de estos sockets.

Además de la clase `Socket`, existen otras clases y librerías que facilitan el desarrollo de aplicaciones de red. Por ejemplo, en Python, la biblioteca `socketserver` ofrece una forma sencilla de implementar servidores TCP/IP. Esta biblioteca proporciona clases para manejar conexiones entrantes y permitir la ejecución de código personalizado cuando se recibe datos.

Otra librería importante es `asyncio`, que permite el desarrollo de aplicaciones asincrónicas de red. Con `asyncio`, los desarrolladores pueden crear servidores y clientes que pueden manejar múltiples conexiones simultáneamente, lo que es crucial para aplicaciones de alta carga o de larga ejecución.

La programación de comunicaciones en red requiere un buen conocimiento de los protocolos de red y la capacidad de gestionar las excepciones que pueden surgir durante el proceso de comunicación. Es importante entender cómo funcionan los sockets, cómo se establecen conexiones, cómo se envían y reciben datos, y cómo se manejan errores.

Además, es crucial considerar la seguridad en la programación de aplicaciones de red. Los ataques como el hacking, la inyección SQL o la modificación de datos sin autorización son posibles si no se implementan medidas de seguridad adecuadas. Es importante utilizar técnicas de criptografía y autenticación para proteger los datos durante su transmisión.

En este capítulo hemos explorado las librerías y clases que facilitan el desarrollo de aplicaciones de red, como `Socket`, `socketserver` y `asyncio`. También hemos discutido la importancia de entender los protocolos de red y cómo gestionar las excepciones y la seguridad en la programación de comunicaciones en red. Con estos conocimientos, los desarrolladores pueden crear aplicaciones robustas y seguras que puedan interactuar eficazmente con otros sistemas a través de Internet.

La programación de comunicaciones en red es un campo dinámico y evolutivo, donde nuevas tecnologías y protocolos están constantemente apareciendo. Es importante mantenerse actualizado sobre las últimas tendencias y mejores prácticas para desarrollar aplicaciones que puedan adaptarse a los cambios del entorno digital.

En el siguiente capítulo, profundizaremos en la programación de servidores y clientes, explorando cómo crear aplicaciones que puedan manejar múltiples conexiones simultáneamente y cómo optimizar su rendimiento. También discutiremos técnicas avanzadas para mejorar la seguridad y la eficiencia de las comunicaciones en red.

En resumen, el desarrollo de aplicaciones que requieren comunicación en red es una tarea compleja pero gratificante. Con las herramientas adecuadas y un buen conocimiento del campo, los desarrolladores pueden crear sistemas robustos y seguros que puedan interactuar eficazmente con otros sistemas a través de Internet.

<a id="sockets-tipos-caracteristicas"></a>
## Sockets. Tipos. Características

En este capítulo, nos adentramos en la fascinante y compleja temática de la programación de comunicaciones en red utilizando sockets. Los sockets son un mecanismo fundamental para la comunicación entre aplicaciones en diferentes máquinas a través de una red. Son como puertas que permiten el intercambio de datos, independientemente del lenguaje de programación o del sistema operativo utilizado.

Los sockets pueden ser de dos tipos principales: orientados a conexión y no orientados a conexión. Los sockets orientados a conexión utilizan un protocolo de establecimiento de conexión antes de comenzar la comunicación, lo que garantiza una comunicación segura y confiable. Por otro lado, los sockets no orientados a conexión son más rápidos pero menos seguros, ya que no requieren el establecimiento de una conexión previa.

Una vez comprendidos los tipos de sockets, es crucial conocer sus características principales. Los sockets tienen propiedades como la dirección IP y el puerto, que identifican únicamente su ubicación en la red. Además, cada socket tiene un estado que puede cambiar durante su vida útil, desde su creación hasta su cierre.

La programación de comunicaciones en red utilizando sockets implica varios pasos clave. Primero, se debe crear un socket y luego establecer una conexión con otro socket remoto. Esto se realiza mediante funciones específicas del sistema operativo o bibliotecas de programación. Una vez establecida la conexión, los datos pueden ser enviados y recibidos utilizando otros conjuntos de funciones.

Es importante destacar que la gestión de errores es un aspecto crucial en la programación de sockets. Los errores pueden surgir durante el establecimiento de la conexión, el envío o recepción de datos, o incluso durante el cierre del socket. Por lo tanto, es necesario implementar mecanismos para detectar y manejar estos errores de manera adecuada.

Además de los sockets orientados a conexión y no orientados a conexión, existen otros tipos de sockets que tienen características específicas. Los sockets Unix dominican la comunicación local dentro del mismo sistema operativo, mientras que los sockets TCP/IP son utilizados para comunicarse entre máquinas en diferentes redes.

La programación de comunicaciones en red utilizando sockets es una habilidad valiosa para desarrolladores que trabajan en aplicaciones que requieren intercambio de datos entre diferentes partes. A través del uso de sockets, se pueden crear aplicaciones robustas y eficientes que puedan funcionar en entornos distribuidos.

En resumen, la programación de comunicaciones en red utilizando sockets es un tema fundamental para cualquier desarrollador interesado en crear aplicaciones que requieran intercambio de datos entre diferentes máquinas. A través del estudio de los tipos de sockets y sus características, así como el proceso de establecimiento y gestión de conexiones, se puede desarrollar una comprensión sólida de este mecanismo esencial para la comunicación en redes.

### Resumen

```markdown
Un socket consiste en la apertura de un canal de comunicación entre dos sistemas informáticos.

Una vez que se abre ese canal, el canal queda abierto para que los dos sistemas informáticos se comuniquen.

Cuando la comunicación ha finalizado, el canal se cierra.

Fetch/AJAX no es sockets - cada vez que se hace una llamada, se abre, se envia, y se cierra.

Ejemplo:
Videojuegos - comunicación constante
Whatsapp - mensajería - comunicación constante

La solución en esos casos concretos son los sockets

Sockets reconocen una red local - pero no reconocen url's - para el caso web tenemos los websockets que son los primos modernos de los sockets
```

### servidor

```python
# server.py
import socket

HOST = "127.0.0.1"   # Localhost
PORT = 5000          # Any free port

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Received:", data.decode("utf-8"))
                conn.sendall(b"Message received")

if __name__ == "__main__":
    main()
```

### cliente

```python
# client.py
import socket

HOST = "127.0.0.1"   # Server address
PORT = 5000          # Same port as server

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        message = "Hello, server"
        client.sendall(message.encode("utf-8"))

        data = client.recv(1024)
        print("Server responded:", data.decode("utf-8"))

if __name__ == "__main__":
    main()
```

### servidor de chat

```python
#!/usr/bin/env python3
import socket
import threading

HOST = "0.0.0.0"   # Escuchar en todas las interfaces
PORT = 5000

# Códigos ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

FG_CYAN = "\033[36m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"
FG_RED = "\033[31m"
FG_MAGENTA = "\033[35m"

clientes = {}  # socket -> apodo
lock_clientes = threading.Lock()


def imprimir_banner():
    banner = f"""
{FG_CYAN}{BOLD}╔═══════════════════════════════════════════════╗
║              💬  SERVIDOR DE CHAT PYTHON        ║
║        Multiusuario · UTF-8 · Emojis 🙂        ║
╚═══════════════════════════════════════════════╝{RESET}
"""
    print(banner)


def enviar_a_todos(mensaje: str, sock_remitente: socket.socket | None = None) -> None:
    """Envía un mensaje a todos los clientes excepto al remitente."""
    datos = mensaje.encode("utf-8", errors="ignore")
    with lock_clientes:
        desconectados = []
        for s in clientes:
            if s is sock_remitente:
                continue
            try:
                s.sendall(datos)
            except OSError:
                desconectados.append(s)

        # Eliminar clientes desconectados
        for s in desconectados:
            apodo = clientes.get(s, "Desconocido")
            del clientes[s]
            print(f"{FG_RED}[DESCONECTADO]{RESET} {apodo} (error de socket)")


def manejar_cliente(conn: socket.socket, addr) -> None:
    try:
        conn.sendall("🟢 Bienvenido. Escribe tu apodo: ".encode("utf-8"))
        apodo_bytes = conn.recv(64)
        if not apodo_bytes:
            conn.close()
            return

        apodo = apodo_bytes.decode("utf-8", errors="ignore").strip()
        if not apodo:
            apodo = f"{addr[0]}:{addr[1]}"

        with lock_clientes:
            clientes[conn] = apodo

        mensaje_union = f"👤 {apodo} se ha unido al chat.\n"
        print(f"{FG_GREEN}[UNIÓN]{RESET} {apodo} desde {addr}")
        enviar_a_todos(mensaje_union)

        conn.sendall("✅ Ya estás conectado. Escribe /salir para desconectarte.\n".encode("utf-8"))

        # Bucle de mensajes
        while True:
            datos = conn.recv(1024)
            if not datos:
                break

            texto = datos.decode("utf-8", errors="ignore").strip()
            if texto == "":
                continue

            if texto.lower() == "/salir":
                break

            mensaje = f"💬 {apodo}: {texto}\n"
            print(f"{FG_MAGENTA}[MENSAJE]{RESET} {apodo}: {texto}")
            enviar_a_todos(mensaje, sock_remitente=conn)

    except ConnectionResetError:
        pass
    finally:
        with lock_clientes:
            apodo = clientes.pop(conn, "Desconocido")
        conn.close()

        mensaje_salida = f"🚪 {apodo} ha salido del chat.\n"
        print(f"{FG_YELLOW}[SALIDA]{RESET} {apodo}")
        enviar_a_todos(mensaje_salida)


def main():
    imprimir_banner()
    print(f"{DIM}Escuchando en {HOST}:{PORT} ...{RESET}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen()

        while True:
            try:
                conn, addr = servidor.accept()
            except KeyboardInterrupt:
                print(f"\n{FG_RED}Cerrando servidor...{RESET}")
                break

            hilo = threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True)
            hilo.start()


if __name__ == "__main__":
    main()
```

### cliente de chat

```python
#!/usr/bin/env python3
import socket
import threading
import sys

HOST = "127.0.0.1"  # Cambia a la IP del servidor si es remoto
PORT = 5000

# Códigos ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

FG_CYAN = "\033[36m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"
FG_RED = "\033[31m"
FG_MAGENTA = "\033[35m"


def imprimir_banner():
    banner = f"""
{FG_CYAN}{BOLD}╔═══════════════════════════════════════════════╗
║                💬  CLIENTE DE CHAT PYTHON       ║
║         Escribe /salir para abandonar el chat   ║
╚═══════════════════════════════════════════════╝{RESET}
"""
    print(banner)


def hilo_receptor(sock: socket.socket) -> None:
    """Hilo que recibe mensajes del servidor y los imprime."""
    try:
        while True:
            datos = sock.recv(1024)
            if not datos:
                print(f"\n{FG_RED}[El servidor se ha desconectado]{RESET}")
                break

            texto = datos.decode("utf-8", errors="ignore")

            # Limpia línea actual y muestra el mensaje
            sys.stdout.write("\r" + " " * 80 + "\r")
            sys.stdout.write(texto)
            sys.stdout.flush()

            # Reponer el prompt
            sys.stdout.write(f"{FG_GREEN}> {RESET}")
            sys.stdout.flush()
    except OSError:
        pass
    finally:
        try:
            sock.close()
        except OSError:
            pass
        salida_segura()


def salida_segura():
    """Salir del proceso desde cualquier hilo."""
    try:
        sys.exit(0)
    except SystemExit:
        import os
        os._exit(0)


def main():
    imprimir_banner()
    apodo = input(f"{FG_YELLOW}Elige un apodo: {RESET}").strip()
    if not apodo:
        apodo = "Anónimo"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
    except OSError as e:
        print(f"{FG_RED}No se pudo conectar a {HOST}:{PORT} → {e}{RESET}")
        return

    receptor = threading.Thread(target=hilo_receptor, args=(sock,), daemon=True)
    receptor.start()

    sock.sendall((apodo + "\n").encode("utf-8"))

    print(f"{FG_GREEN}Conectado. Escribe tus mensajes. /salir para salir.{RESET}")
    try:
        while True:
            msg = input(f"{FG_GREEN}> {RESET}")
            if msg.strip().lower() == "/salir":
                sock.sendall("/salir".encode("utf-8"))
                break
            try:
                sock.sendall(msg.encode("utf-8"))
            except OSError:
                print(f"{FG_RED}Conexión perdida.{RESET}")
                break
    except KeyboardInterrupt:
        try:
            sock.sendall("/salir".encode("utf-8"))
        except OSError:
            pass

    try:
        sock.close()
    except OSError:
        pass
    print(f"{FG_YELLOW}Cerrando cliente...{RESET}")


if __name__ == "__main__":
    main()
```

<a id="creacion-de-sockets"></a>
## Creación de sockets

En este capítulo, nos adentramos en la creación de sockets, un concepto fundamental para la programación de comunicaciones en red. Un socket es una interfaz que permite a los programas interactuar entre sí a través de una red, proporcionando un medio para enviar y recibir datos.

La creación de un socket implica varios pasos clave. Primero, se debe seleccionar el tipo de socket adecuado según las necesidades de la aplicación. Los tipos más comunes son SOCK_STREAM (orientados a conexión) y SOCK_DGRAM (no orientados a conexión), cada uno con sus propias características y usos.

Una vez elegido el tipo de socket, el siguiente paso es crearlo utilizando una función específica del sistema operativo. En sistemas Unix-like, esta función se llama `socket()`, que toma tres parámetros: la familia de direcciones (como AF_INET para IPv4), el tipo de socket y el protocolo a utilizar.

Después de crear el socket, es necesario establecer una dirección asociada con él. Esto se realiza mediante la función `bind()`, que asocia un nombre (dirección IP y número de puerto) al socket. Es importante elegir un puerto no utilizado para evitar conflictos.

El siguiente paso depende del tipo de socket. Para sockets orientados a conexión, como SOCK_STREAM, es necesario establecer una conexión con el servidor utilizando la función `connect()`. Este proceso incluye la verificación de la disponibilidad del servidor y la negociación de parámetros de comunicación.

Para los sockets no orientados a conexión, como SOCK_DGRAM, se utiliza la función `sendto()` para enviar datos directamente al servidor sin necesidad de establecer una conexión previa. Es importante especificar la dirección del destinatario en cada envío.

Una vez que el socket está configurado y listo para la comunicación, los programas pueden comenzar a intercambiar datos utilizando funciones específicas para enviar (`send()` o `sendto()`) y recibir (`recv()` o `recvfrom()`). Estas funciones manejan la transmisión de paquetes de datos entre los sockets.

Es importante tener en cuenta que la comunicación mediante sockets es asíncrona, lo que significa que los programas pueden seguir realizando otras tareas mientras esperan a que lleguen los datos. Esto se logra utilizando mecanismos como select(), poll() o epoll(), que permiten monitorear varios sockets simultáneamente.

Para manejar errores durante la comunicación, es crucial implementar rutinas de control de excepciones y verificar el estado del socket después de cada operación. Funciones como `getsockopt()` pueden ser útiles para obtener información sobre el estado actual del socket.

Finalmente, cuando se termina la comunicación, es importante cerrar el socket utilizando la función `close()`. Esto libera los recursos asociados al socket y permite que otros programas utilicen el puerto liberado.

La creación de sockets es un paso crucial en cualquier aplicación que requiera comunicarse a través de una red. Aunque puede parecer complejo al principio, con práctica se vuelve más intuitivo y es una habilidad fundamental para desarrolladores de software que trabajan en entornos distribuidos o basados en la nube.

### servidor de websockets

```python
#!/usr/bin/env python3
import asyncio
import json
import ssl
import websockets

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Expect JSON
            try:
                data = json.loads(message)
            except json.JSONDecodeError:
                await websocket.send(json.dumps({
                    "type": "error",
                    "error": "invalid_json"
                }))
                continue

            # Broadcast received JSON to all clients
            payload = json.dumps(data)

            disconnected = []
            for client in connected_clients:
                if client.closed:
                    disconnected.append(client)
                    continue
                try:
                    await client.send(payload)
                except Exception:
                    disconnected.append(client)

            # Clean up
            for client in disconnected:
                connected_clients.discard(client)

    finally:
        connected_clients.discard(websocket)

async def main():
    # TLS context using your existing cert and key
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(
        certfile="/etc/apache2/ssl/jocarsa_combined.cer",
        keyfile="/etc/apache2/ssl/jocarsa.key"
    )

    # Listen on port 8766 with TLS
    async with websockets.serve(
        handler,
        "0.0.0.0",
        8766,
        ssl=ssl_context
    ):
        print("Secure WebSocket server on wss://jocarsa.com:8766")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
```

### prueba

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>WSS test</title>
</head>
<body>
  <input id="msg" style="width: 300px"
         value='{"type":"test","text":"Hello from client"}'>
  <button id="send">Send JSON</button>
  <pre id="log"></pre>

  <script>
    const log = (m) => {
      document.getElementById("log").textContent += m + "\n";
    };

    const ws = new WebSocket("wss://jocarsa.com:8766");

    ws.onopen = () => log("Connected");
    ws.onmessage = (event) => {
      log("Received: " + event.data);
      // Here you would normally do:
      // const data = JSON.parse(event.data);
      // and handle that JSON
    };
    ws.onerror = (e) => log("Error: " + e);
    ws.onclose = () => log("Disconnected");

    document.getElementById("send").onclick = () => {
      const txt = document.getElementById("msg").value;
      try {
        const obj = JSON.parse(txt);
        ws.send(JSON.stringify(obj));
        log("Sent: " + JSON.stringify(obj));
      } catch (err) {
        log("Invalid JSON: " + err.message);
      }
    };
  </script>
</body>
</html>
```

<a id="enlazado-y-establecimiento-de-conexiones"></a>
## Enlazado y establecimiento de conexiones

En el mundo digital actual, la comunicación entre aplicaciones es un aspecto fundamental que requiere una comprensión profunda de los protocolos y mecanismos utilizados para establecer y mantener conexiones. En esta subunidad, nos centraremos en el proceso de enlazado y establecimiento de conexiones en redes, un paso crucial antes de la transmisión de información.

El primer paso en el establecimiento de una conexión es el enlace, que implica la configuración adecuada de los sockets. Los sockets son las interfaces de red utilizadas para enviar y recibir datos entre aplicaciones. En Python, por ejemplo, se pueden crear sockets utilizando la biblioteca `socket`. El proceso comienza con la creación del socket mediante la función `socket.socket()`, seguida de la configuración del tipo de conexión (TCP o UDP) y el protocolo a utilizar.

Una vez creado el socket, el siguiente paso es establecer una conexión. Esto se realiza utilizando el método `connect()` en el caso de los sockets cliente, que requiere conocer la dirección IP y el puerto del servidor al que deseamos conectarnos. Para los sockets servidor, el proceso es ligeramente diferente: primero se debe vincular el socket a un puerto específico con el método `bind()`, y luego ponerlo en modo escucha con `listen()`.

Es importante destacar que la seguridad de las conexiones es una preocupación crítica. Durante el establecimiento de la conexión, los sockets pueden implementar mecanismos de autenticación para asegurar que solo aplicaciones autorizadas puedan acceder al servicio. Esto puede implicar el uso de protocolos como SSL/TLS para cifrar la comunicación.

Una vez establecida la conexión, se pueden comenzar a enviar y recibir datos utilizando los métodos `send()` y `recv()`. Es crucial manejar adecuadamente estos flujos de datos para evitar problemas como desbordamientos o bloqueos. Además, es importante tener en cuenta el tamaño máximo del paquete que puede ser enviado en una sola operación.

El establecimiento y mantenimiento de conexiones también implica la gestión de errores. Los sockets proporcionan mecanismos para detectar y manejar excepciones como la pérdida de conexión o problemas de red. Es recomendable implementar manejadores de excepciones adecuados para mantener la robustez del sistema.

En resumen, el enlazado y establecimiento de conexiones son fundamentales para cualquier comunicación entre aplicaciones en redes. A través de la creación y configuración de sockets, el establecimiento de una conexión segura y eficiente, y la gestión adecuada de los flujos de datos, podemos crear sistemas que sean capaces de intercambiar información de manera rápida y confiable. Este proceso es esencial para el desarrollo de aplicaciones modernas que requieren comunicación en tiempo real o acceso a recursos distribuidos.

### conectar con servidor

```
<?php
$url = "https://covalently-untasked-daphne.ngrok-free.dev/api.php";

$ch = curl_init();

// Basic configuration
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Equivalent to curl -k  (disable SSL certificate verification)
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if ($response === false) {
    echo "cURL Error: " . curl_error($ch);
} else {
    echo $response;
}

curl_close($ch);
```

### llamada a api abierta

```
<?php

$url = "https://covalently-untasked-daphne.ngrok-free.dev/api.php";

// La pregunta que quieres enviar
$question = "What is quantum computing?";

// Construimos los datos como application/x-www-form-urlencoded
$postData = http_build_query([
    "question" => $question
]);

$opts = [
    "http" => [
        "method"  => "POST",
        "header"  => "Content-Type: application/x-www-form-urlencoded\r\n" .
                     "Content-Length: " . strlen($postData) . "\r\n",
        "content" => $postData,
        "timeout" => 60
    ],
    "ssl" => [
        // Equivalente aproximado a curl -k (no recomendado en producción)
        "verify_peer"      => false,
        "verify_peer_name" => false,
    ]
];

$context  = stream_context_create($opts);
$response = @file_get_contents($url, false, $context);

if ($response === false) {
    $error = error_get_last();
    echo "Error calling remote API:\n";
    var_dump($error);
} else {
    echo $response . PHP_EOL;
}
```

### instalar mysql

```markdown
sudo apt update

sudo apt install mysql-server

mysql_secure_installation
```

### usuario y contraseña

```
<?php

// Remote API (your ngrok endpoint pointing to api.php)
$url = "https://covalently-untasked-daphne.ngrok-free.dev/api.php";

// Credentials must match $VALID_USER / $VALID_PASS in api.php
$user = 'myuser';        // same as in api.php
$pass = 'mypassword2';    // same as in api.php

// Question to send (you can change this or read from argv)
$question = "What is quantum computing?";

// Build POST data as application/x-www-form-urlencoded
$postData = http_build_query([
    "question" => $question
]);

// Build Authorization header (Basic Auth)
$authHeader = 'Authorization: Basic ' . base64_encode($user . ':' . $pass);

$opts = [
    "http" => [
        "method"  => "POST",
        "header"  =>
            "Content-Type: application/x-www-form-urlencoded\r\n" .
            "Content-Length: " . strlen($postData) . "\r\n" .
            $authHeader . "\r\n",
        "content" => $postData,
        "timeout" => 60
    ],
    "ssl" => [
        // Equivalent of curl -k: disable peer verification (for ngrok / tests)
        "verify_peer"      => false,
        "verify_peer_name" => false,
    ]
];

$context  = stream_context_create($opts);
$response = @file_get_contents($url, false, $context);

if ($response === false) {
    $error = error_get_last();
    echo "Error calling remote API:\n";
    var_dump($error);
    exit;
}

echo $response . PHP_EOL;
```

### crear base de datos

```sql
CREATE DATABASE IF NOT EXISTS ollama_api
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE ollama_api;


CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NULL,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE plans (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255) NULL,
    queries_per_hour INT UNSIGNED NOT NULL DEFAULT 60,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE user_plans (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    plan_id INT UNSIGNED NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NULL DEFAULT NULL,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    CONSTRAINT fk_user_plans_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_user_plans_plan
        FOREIGN KEY (plan_id) REFERENCES plans(id)
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE api_keys (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    api_key VARCHAR(64) NOT NULL UNIQUE,
    description VARCHAR(255) NULL,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP NULL DEFAULT NULL,
    CONSTRAINT fk_api_keys_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO plans (name, description, queries_per_hour)
VALUES ('basic', 'Plan básico con límite por defecto', 100);

INSERT INTO users (username, password, email)
VALUES ('jocarsa', 'jocarsa', 'info@jocarsa.com');


INSERT INTO user_plans (user_id, plan_id)
SELECT u.id, p.id
FROM users u
JOIN plans p ON p.name = 'basic'
WHERE u.username = 'jocarsa';


INSERT INTO api_keys (user_id, api_key, description)
SELECT id, 'TEST_API_KEY_JOCARSA_123', 'Clave inicial de pruebas'
FROM users
WHERE username = 'jocarsa';


USE ollama_api;

CREATE TABLE api_usage (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    api_key_id INT UNSIGNED NOT NULL,
    hour_start DATETIME NOT NULL,
    request_count INT UNSIGNED NOT NULL DEFAULT 0,
    CONSTRAINT fk_api_usage_api_key
        FOREIGN KEY (api_key_id) REFERENCES api_keys(id)
        ON DELETE CASCADE,
    UNIQUE KEY uk_api_usage_key_hour (api_key_id, hour_start)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### api key

```
<?php

// Remote API (ngrok endpoint pointing to api.php)
$url = "https://covalently-untasked-daphne.ngrok-free.dev/api.php";

// This must match an api_key in your `api_keys` table
$apiKey = "TEST_API_KEY_JOCARSA_123";  // adjust to your real key

// Question to send
$question = "What is quantum computing?";

// Build POST body
$postData = http_build_query([
    "question" => $question
]);

$headers =
    "Content-Type: application/x-www-form-urlencoded\r\n" .
    "Content-Length: " . strlen($postData) . "\r\n" .
    "X-API-Key: " . $apiKey . "\r\n";

$opts = [
    "http" => [
        "method"  => "POST",
        "header"  => $headers,
        "content" => $postData,
        "timeout" => 60
    ],
    "ssl" => [
        // Equivalent to curl -k (for ngrok/testing only)
        "verify_peer"      => false,
        "verify_peer_name" => false,
    ]
];

$context  = stream_context_create($opts);
$response = @file_get_contents($url, false, $context);

if ($response === false) {
    $error = error_get_last();
    echo "Error calling remote API:\n";
    var_dump($error);
    exit;
}

echo $response . PHP_EOL;
```

### phpinfo

```
<?php

phpinfo();

?>
```

<a id="utilizacion-de-sockets-para-la-transmision-y-recepcion-de-informacion"></a>
## Utilización de sockets para la transmisión y recepción de información

La programación de comunicaciones en red es un aspecto fundamental del desarrollo de aplicaciones que requieren la interacción con otros sistemas o dispositivos a través de Internet o redes locales. En esta subunidad, nos centraremos en el uso de sockets para la transmisión y recepción de información.

Los sockets son una abstracción que permite la comunicación entre procesos en diferentes máquinas, independientemente del lenguaje de programación utilizado. Son como puertas de entrada y salida que permiten a los programas enviar y recibir datos de manera eficiente. En Python, el módulo `socket` proporciona las herramientas necesarias para crear y gestionar sockets.

Para transmitir información mediante sockets, es necesario establecer una conexión entre dos puntos finales: un cliente y un servidor. El proceso comienza con la creación de un socket en ambos extremos. En el lado del servidor, se configura el socket para escuchar conexiones entrantes, mientras que en el cliente se intenta conectarse al servidor.

Una vez establecida la conexión, los datos pueden ser enviados y recibidos mediante métodos específicos del objeto socket. El método `send()` se utiliza para enviar datos desde el cliente al servidor, mientras que `recv()` permite recibir datos en el servidor o en el cliente. Es importante manejar adecuadamente estos métodos para evitar errores de comunicación.

La transmisión de información a través de sockets puede ser sincrónica o asíncrona. En la sincronización, el programa se bloqueará hasta que los datos sean enviados o recibidos completamente. Por otro lado, en la programación asíncrona, las operaciones de red pueden realizarse sin bloquear el flujo principal del programa.

Es crucial manejar adecuadamente los errores durante la comunicación mediante sockets. Esto incluye capturar excepciones como `ConnectionRefusedError` cuando no se puede establecer una conexión o `TimeoutError` cuando ocurre un tiempo de espera excedido. Además, es importante cerrar correctamente los sockets después de su uso para liberar recursos.

La programación de comunicaciones en red requiere un buen entendimiento de la arquitectura del protocolo TCP/IP y las características específicas de cada socket. Cada socket tiene propiedades como el tipo (TCP o UDP), la dirección IP y el puerto, que son esenciales para establecer una comunicación exitosa.

En resumen, el uso de sockets para la transmisión y recepción de información en aplicaciones de red es un concepto poderoso y flexible. A través del módulo `socket` de Python, podemos crear programas que se comuniquen eficientemente con otros sistemas a nivel de red, lo que abre las puertas a una amplia gama de aplicaciones desde el desarrollo de servidores web hasta la creación de aplicaciones móviles y de juegos.

<a id="programacion-de-aplicaciones-cliente-y-servidor"></a>
## Programación de aplicaciones cliente y servidor

En el mundo digital actual, la comunicación entre aplicaciones es un aspecto fundamental que permite la interacción eficiente y la colaboración entre diferentes sistemas. La programación de comunicaciones en red es una habilidad crucial para desarrolladores que desean crear aplicaciones cliente-servidor robustas y escalables.

La arquitectura cliente-servidor implica dos tipos principales de entidades: el cliente, que solicita servicios o datos, y el servidor, que proporciona dichos recursos. En esta subunidad, nos centraremos en cómo programar tanto clientes como servidores para establecer y mantener conexiones eficientes.

El primer paso es entender los roles del cliente y del servidor. El cliente inicia la comunicación solicitando un servicio o datos específicos al servidor. Por su parte, el servidor recibe estas solicitudes, procesa los datos necesarios y devuelve una respuesta al cliente. Este proceso puede repetirse varias veces para mantener la sesión activa.

Para implementar este flujo de trabajo, se utilizan protocolos estándar como TCP/IP, que es el protocolo de comunicación fundamental en Internet. Estos protocolos definen cómo los datos son enviados y recibidos entre el cliente y el servidor, asegurando una comunicación segura y confiable.

El desarrollo del cliente implica la creación de aplicaciones que puedan enviar solicitudes al servidor y manejar las respuestas que reciban. Esto puede implicar la utilización de bibliotecas o frameworks específicos para facilitar la comunicación, como `Socket.IO` en el caso de aplicaciones web en tiempo real.

Por otro lado, el desarrollo del servidor implica la creación de aplicaciones que puedan escuchar solicitudes entrantes y responder adecuadamente. Esto puede implicar la utilización de lenguajes de programación como Java, Python o Node.js, junto con frameworks específicos para facilitar el manejo de conexiones y solicitudes.

La comunicación entre cliente y servidor no es solo una transmisión de datos; también implica la sincronización del estado entre ambas partes. Esto puede requerir mecanismos adicionales como la actualización de estados en tiempo real o la gestión de sesiones para mantener el contexto de interacción.

Además, la seguridad es un aspecto crucial en la programación de comunicaciones en red. Los clientes y servidores deben implementar medidas de seguridad para proteger los datos en tránsito y evitar accesos no autorizados. Esto puede implicar el uso de protocolos seguros como HTTPS o SSL/TLS, así como la implementación de autenticación y autorización adecuadas.

La programación de aplicaciones cliente-servidor también implica considerar el rendimiento y la escalabilidad. Los servidores deben estar diseñados para manejar múltiples conexiones simultáneas y procesar grandes volúmenes de datos, mientras que los clientes deben ser eficientes en su uso de recursos.

En resumen, la programación de comunicaciones en red es un campo complejo pero fundamental en el desarrollo de aplicaciones modernas. Al entender y dominar los conceptos básicos de cliente-servidor, protocolos estándares, seguridad y rendimiento, los desarrolladores pueden crear sistemas interactivos y eficientes que satisfagan las necesidades de una variedad de usuarios y entornos.

<a id="utilizacion-de-hilos-para-la-implementacion-de-comunicaciones-simultaneas-con-el-servidor"></a>
## Utilización de hilos para la implementación de comunicaciones simultáneas con el servidor

En el mundo digital actual, la capacidad de comunicarse eficientemente entre diferentes componentes es crucial para la creación de aplicaciones robustas y escalables. La programación de comunicaciones en red es un aspecto fundamental que permite a los sistemas intercambiar información de manera rápida y segura. En esta subunidad, nos centraremos en cómo utilizar hilos para implementar comunicaciones simultáneas con el servidor.

Los hilos son unidades de ejecución dentro de un proceso que comparten la misma memoria y recursos del sistema operativo. Al trabajar con hilos, podemos realizar múltiples tareas a la vez, lo que es especialmente útil cuando se necesita mantener una interfaz de usuario responsive mientras se realiza alguna operación en segundo plano. En el contexto de la programación de comunicaciones en red, los hilos nos permiten enviar y recibir datos del servidor sin bloquear el flujo principal del programa.

Para implementar comunicaciones simultáneas con el servidor utilizando hilos, es necesario utilizar bibliotecas específicas que faciliten esta tarea. Por ejemplo, en Java, la clase `Thread` permite crear e iniciar nuevos hilos fácilmente. Cada hilo puede ser responsable de una operación específica, como enviar una solicitud al servidor o procesar la respuesta recibida.

La comunicación con el servidor a través de hilos implica establecer conexiones, enviar solicitudes y recibir respuestas de manera asincrónica. Esto se logra utilizando sockets, que son mecanismos de red que permiten la comunicación entre dos puntos finales. En Java, la clase `Socket` proporciona métodos para crear una conexión con el servidor y enviar datos a través de ella.

La sincronización entre hilos es un aspecto importante cuando se trabaja con comunicaciones en red. Es necesario asegurarse de que los hilos no accedan simultáneamente a recursos compartidos, lo cual podría llevar a errores o inconsistencias en el sistema. Para manejar la sincronización, Java ofrece mecanismos como `synchronized` y bloques `synchronized`, que permiten controlar el acceso a recursos compartidos de manera segura.

Además de la sincronización, es crucial manejar los eventos relacionados con la comunicación en red. Por ejemplo, cuando se recibe una respuesta del servidor, es necesario procesarla adecuadamente y notificar al resto del programa que la operación ha terminado. En Java, esto puede lograrse utilizando mecanismos como `Future` y `Callable`, que permiten ejecutar tareas de manera asíncrona y obtener resultados.

La implementación de comunicaciones simultáneas con el servidor utilizando hilos no solo mejora la eficiencia del programa, sino que también proporciona una mejor experiencia al usuario. Al mantener la interfaz de usuario responsive mientras se realiza alguna operación en segundo plano, los usuarios pueden interactuar con la aplicación sin interrupciones.

En resumen, la programación de comunicaciones en red utilizando hilos es un poderoso mecanismo que permite a los sistemas intercambiar información de manera eficiente y segura. Al utilizar bibliotecas específicas para manejar conexiones, enviar solicitudes y recibir respuestas de manera asincrónica, podemos implementar comunicaciones simultáneas con el servidor sin bloquear el flujo principal del programa. La sincronización entre hilos es un aspecto crucial que debe ser cuidadosamente gestionado para evitar errores o inconsistencias en el sistema. Finalmente, la implementación de comunicaciones en red utilizando hilos mejora la eficiencia del programa y proporciona una mejor experiencia al usuario.


<a id="generacion-de-servicios-en-red"></a>
# Generación de servicios en red

<a id="protocolos-estandar-de-comunicacion-en-red-a-nivel-de-aplicacion"></a>
## Protocolos estándar de comunicación en red a nivel de aplicación

La generación de servicios en red implica la creación de aplicaciones que pueden interactuar entre sí a través de Internet o redes locales. En el nivel de aplicación, los protocolos estándar desempeñan un papel crucial para facilitar esta comunicación eficiente y segura. Uno de los protocolos más utilizados es HTTP (Hypertext Transfer Protocol), que es fundamental para la transferencia de datos en aplicaciones web.

HTTP opera sobre TCP/IP, proporcionando una interfaz simple pero poderosa para el intercambio de información entre clientes y servidores. Este protocolo permite solicitar y recibir recursos como páginas web, imágenes y archivos multimedia. La arquitectura cliente-servidor es la base de muchos servicios en red modernos, donde un cliente realiza solicitudes a un servidor que luego responde con los datos solicitados.

Además de HTTP, existen otros protocolos estándar importantes para el nivel de aplicación. Por ejemplo, SMTP (Simple Mail Transfer Protocol) se utiliza para enviar correos electrónicos, mientras que FTP (File Transfer Protocol) facilita la transferencia de archivos entre sistemas. Cada uno de estos protocolos tiene sus propias características y ventajas, adaptándose a diferentes tipos de aplicaciones y necesidades.

La implementación de servicios en red utilizando protocolos estándar requiere un buen conocimiento de las arquitecturas cliente-servidor y el manejo de conexiones TCP/IP. Es crucial entender cómo establecer y mantener estas conexiones, así como cómo enviar y recibir datos de manera segura y eficiente.

Además de los protocolos de nivel de aplicación, es importante considerar la seguridad en la comunicación. Protocolos como SSL/TLS (Secure Sockets Layer/Transport Layer Security) proporcionan cifrado para proteger las transacciones entre clientes y servidores, evitando el robo de información sensible.

La generación de servicios en red también implica la creación de interfaces que sean fáciles de usar y entender. Esto incluye la definición de endpoints, los métodos HTTP (GET, POST, PUT, DELETE) y las estructuras de datos utilizadas para enviar y recibir información. Buena práctica es documentar estos detalles para facilitar el mantenimiento y la colaboración entre desarrolladores.

En resumen, la generación de servicios en red a nivel de aplicación implica el uso de protocolos estándar como HTTP, SMTP y FTP para facilitar la comunicación entre sistemas. Es crucial entender cómo implementar estas comunicaciones de manera segura y eficiente, así como cómo diseñar interfaces claras y fáciles de usar.

<a id="servicios-web"></a>
## Servicios web

La generación de servicios web es un aspecto crucial del desarrollo moderno de aplicaciones informáticas, permitiendo la comunicación entre diferentes sistemas a través de Internet o redes privadas. Un servicio web es una aplicación que expone funcionalidades a través de protocolos estándar como HTTP y SOAP, facilitando la integración entre sistemas distribuidos.

En este contexto, los servicios web se basan en el concepto de arquitectura cliente-servidor, donde un cliente realiza solicitudes a un servidor, que luego procesa estas solicitudes y devuelve una respuesta. Los servicios web utilizan formatos como XML o JSON para la codificación de datos, lo que permite su intercambio entre diferentes plataformas y lenguajes de programación.

La creación de servicios web implica varios pasos clave. Primero, se define el conjunto de operaciones que el servicio va a ofrecer, utilizando un lenguaje de definición de servicios como WSDL (Web Services Description Language). A continuación, se implementa la lógica del servicio en un servidor, utilizando tecnologías como Java, .NET o PHP. Es importante garantizar que el servicio sea seguro y autenticado para proteger los datos intercambiados.

Una vez implementado, el servicio web debe ser probado para asegurar su correcto funcionamiento. Esto implica realizar pruebas de integración y funcionalidad, verificando que todas las operaciones se ejecuten como se espera y que la comunicación sea eficiente. Además, es recomendable documentar el servicio web para facilitar su uso por otros desarrolladores.

La gestión del ciclo de vida de un servicio web también es crucial. Esto incluye la actualización periódica del código del servidor, la monitorización del rendimiento y la implementación de estrategias de escalado para manejar cargas de trabajo crecientes. Además, es importante realizar respaldos regulares del estado del servicio para prevenir la pérdida de datos en caso de fallos.

En el mundo actual, los servicios web son una herramienta fundamental para la integración de sistemas y la creación de aplicaciones distribuidas. Su uso permite a las empresas ofrecer soluciones escalables y flexibles que pueden adaptarse a las necesidades cambiantes del negocio. A través de la generación de servicios web, se facilita la colaboración entre diferentes equipos y el acceso remoto a recursos críticos, lo que mejora la eficiencia operativa y la productividad.

En resumen, la generación de servicios web es un proceso integral que requiere una combinación de diseño, implementación, pruebas y gestión. Al seguir las mejores prácticas en este campo, los desarrolladores pueden crear sistemas robustos y escalables que satisfagan las necesidades complejas del negocio moderno.

### procesador

```python
# cpu_monitor.py
import psutil
import csv
from datetime import datetime
import os

# File to store CPU usage history
CSV_FILE = 'cpu_usage_history.csv'

def get_cpu_usage():
    """Returns current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def save_cpu_usage(cpu_usage):
    """Saves CPU usage and current date to CSV."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['date', 'cpu_pressure'])
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), cpu_usage])

if __name__ == '__main__':
    cpu_usage = get_cpu_usage()
    save_cpu_usage(cpu_usage)
    print(f"Saved CPU usage: {cpu_usage}%")
```

### procesador

```
<?php
// api_cpu_usage.php
$username = 'your_username'; // Change this
$password = 'your_password'; // Change this

// Check for valid credentials
if (!isset($_SERVER['PHP_AUTH_USER']) ||
    !isset($_SERVER['PHP_AUTH_PW']) ||
    $_SERVER['PHP_AUTH_USER'] != $username ||
    $_SERVER['PHP_AUTH_PW'] != $password) {
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    die('Authentication required.');
}

// CSV file path
$csvFile = 'cpu_usage_history.csv';

// Check if file exists
if (!file_exists($csvFile)) {
    header('Content-Type: application/json');
    die(json_encode(['error' => 'No data available.']));
}

// Read CSV and convert to JSON
$data = [];
$file = fopen($csvFile, 'r');
$header = fgetcsv($file);
while ($row = fgetcsv($file)) {
    $data[] = [
        'date' => $row[0],
        'cpu_pressure' => (float)$row[1]
    ];
}
fclose($file);

// Output as JSON
header('Content-Type: application/json');
echo json_encode($data);
?>
```

### ram

```python
# ram_monitor.py
import psutil
import csv
from datetime import datetime
import os

# File to store RAM usage history
CSV_FILE = 'ram_usage_history.csv'

def get_ram_usage():
    """Returns RAM usage percentage and total RAM in GB."""
    ram = psutil.virtual_memory()
    return ram.percent, round(ram.total / (1024 ** 3), 2)  # Total in GB

def save_ram_usage(ram_percent, ram_total_gb):
    """Saves RAM usage and current date to CSV."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['date', 'ram_pressure_percent', 'ram_total_gb'])
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ram_percent, ram_total_gb])

if __name__ == '__main__':
    ram_percent, ram_total_gb = get_ram_usage()
    save_ram_usage(ram_percent, ram_total_gb)
    print(f"Saved RAM usage: {ram_percent}%, Total: {ram_total_gb} GB")
```

### ram

```
<?php
// api_ram_usage.php
$username = 'your_username'; // Change this
$password = 'your_password'; // Change this

// Check for valid credentials
if (!isset($_SERVER['PHP_AUTH_USER']) ||
    !isset($_SERVER['PHP_AUTH_PW']) ||
    $_SERVER['PHP_AUTH_USER'] != $username ||
    $_SERVER['PHP_AUTH_PW'] != $password) {
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    die('Authentication required.');
}

// CSV file path
$csvFile = 'ram_usage_history.csv';

// Check if file exists
if (!file_exists($csvFile)) {
    header('Content-Type: application/json');
    die(json_encode(['error' => 'No data available.']));
}

// Read CSV and convert to JSON
$data = [];
$file = fopen($csvFile, 'r');
$header = fgetcsv($file);
while ($row = fgetcsv($file)) {
    $data[] = [
        'date' => $row[0],
        'ram_pressure_percent' => (float)$row[1],
        'ram_total_gb' => (float)$row[2]
    ];
}
fclose($file);

// Output as JSON
header('Content-Type: application/json');
echo json_encode($data);
?>
```

### disco

```python
# disk_monitor.py
import psutil
import csv
from datetime import datetime
import os

# File to store disk usage history
CSV_FILE = 'disk_usage_history.csv'

def get_disk_usage():
    """Returns disk usage percentage, total, and free space in GB for the root partition."""
    disk = psutil.disk_usage('/')
    total_gb = round(disk.total / (1024 ** 3), 2)
    free_gb = round(disk.free / (1024 ** 3), 2)
    return disk.percent, total_gb, free_gb

def save_disk_usage(percent, total_gb, free_gb):
    """Saves disk usage and current date to CSV."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['date', 'disk_pressure_percent', 'disk_total_gb', 'disk_free_gb'])
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), percent, total_gb, free_gb])

if __name__ == '__main__':
    percent, total_gb, free_gb = get_disk_usage()
    save_disk_usage(percent, total_gb, free_gb)
    print(f"Saved disk usage: {percent}%, Total: {total_gb} GB, Free: {free_gb} GB")
```

### disco

```
<?php
// api_disk_usage.php
$username = 'your_username'; // Change this
$password = 'your_password'; // Change this

// Check for valid credentials
if (!isset($_SERVER['PHP_AUTH_USER']) ||
    !isset($_SERVER['PHP_AUTH_PW']) ||
    $_SERVER['PHP_AUTH_USER'] != $username ||
    $_SERVER['PHP_AUTH_PW'] != $password) {
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    die('Authentication required.');
}

// CSV file path
$csvFile = 'disk_usage_history.csv';

// Check if file exists
if (!file_exists($csvFile)) {
    header('Content-Type: application/json');
    die(json_encode(['error' => 'No data available.']));
}

// Read CSV and convert to JSON
$data = [];
$file = fopen($csvFile, 'r');
$header = fgetcsv($file);
while ($row = fgetcsv($file)) {
    $data[] = [
        'date' => $row[0],
        'disk_pressure_percent' => (float)$row[1],
        'disk_total_gb' => (float)$row[2],
        'disk_free_gb' => (float)$row[3]
    ];
}
fclose($file);

// Output as JSON
header('Content-Type: application/json');
echo json_encode($data);
?>
```

### discoio

```python
# disk_io_monitor.py
import psutil
import csv
from datetime import datetime
import os

# File to store disk I/O history
CSV_FILE = 'disk_io_history.csv'

def get_disk_io():
    """Returns disk I/O stats: read/write bytes, operations, and latency."""
    disks = psutil.disk_io_counters(perdisk=True)
    data = []
    for disk_name, io in disks.items():
        data.append({
            'disk': disk_name,
            'read_bytes': io.read_bytes,
            'write_bytes': io.write_bytes,
            'read_ops': io.read_count,
            'write_ops': io.write_count,
            'read_time_ms': io.read_time,
            'write_time_ms': io.write_time,
            'busy_time_ms': io.busy_time
        })
    return data

def save_disk_io(data):
    """Saves disk I/O stats and current date to CSV."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                'date', 'disk', 'read_bytes', 'write_bytes',
                'read_ops', 'write_ops', 'read_time_ms',
                'write_time_ms', 'busy_time_ms'
            ])
        for entry in data:
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                entry['disk'], entry['read_bytes'], entry['write_bytes'],
                entry['read_ops'], entry['write_ops'],
                entry['read_time_ms'], entry['write_time_ms'],
                entry['busy_time_ms']
            ])

if __name__ == '__main__':
    data = get_disk_io()
    save_disk_io(data)
    print(f"Saved disk I/O data for {len(data)} disks.")
```

### discoio

```
<?php
// api_disk_io.php
$username = 'your_username'; // Change this
$password = 'your_password'; // Change this

// Check for valid credentials
if (!isset($_SERVER['PHP_AUTH_USER']) ||
    !isset($_SERVER['PHP_AUTH_PW']) ||
    $_SERVER['PHP_AUTH_USER'] != $username ||
    $_SERVER['PHP_AUTH_PW'] != $password) {
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    die('Authentication required.');
}

// CSV file path
$csvFile = 'disk_io_history.csv';

// Check if file exists
if (!file_exists($csvFile)) {
    header('Content-Type: application/json');
    die(json_encode(['error' => 'No data available.']));
}

// Read CSV and convert to JSON
$data = [];
$file = fopen($csvFile, 'r');
$header = fgetcsv($file);
while ($row = fgetcsv($file)) {
    $data[] = [
        'date' => $row[0],
        'disk' => $row[1],
        'read_bytes' => (int)$row[2],
        'write_bytes' => (int)$row[3],
        'read_ops' => (int)$row[4],
        'write_ops' => (int)$row[5],
        'read_time_ms' => (int)$row[6],
        'write_time_ms' => (int)$row[7],
        'busy_time_ms' => (int)$row[8]
    ];
}
fclose($file);

// Output as JSON
header('Content-Type: application/json');
echo json_encode($data);
?>
```

### anchodebanda

```python
# bandwidth_monitor.py
import psutil
import csv
from datetime import datetime
import os

# File to store bandwidth usage history
CSV_FILE = 'bandwidth_usage_history.csv'

def get_bandwidth_usage():
    """Returns bandwidth usage stats: bytes sent/received for each interface."""
    net_io = psutil.net_io_counters(pernic=True)
    data = []
    for iface, io in net_io.items():
        data.append({
            'interface': iface,
            'bytes_sent': io.bytes_sent,
            'bytes_recv': io.bytes_recv,
            'packets_sent': io.packets_sent,
            'packets_recv': io.packets_recv
        })
    return data

def save_bandwidth_usage(data):
    """Saves bandwidth usage stats and current date to CSV."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                'date', 'interface', 'bytes_sent',
                'bytes_recv', 'packets_sent', 'packets_recv'
            ])
        for entry in data:
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                entry['interface'],
                entry['bytes_sent'],
                entry['bytes_recv'],
                entry['packets_sent'],
                entry['packets_recv']
            ])

if __name__ == '__main__':
    data = get_bandwidth_usage()
    save_bandwidth_usage(data)
    print(f"Saved bandwidth usage data for {len(data)} interfaces.")
```

### anchodebanda

```
<?php
// api_bandwidth_usage.php
$username = 'your_username'; // Change this
$password = 'your_password'; // Change this

// Check for valid credentials
if (!isset($_SERVER['PHP_AUTH_USER']) ||
    !isset($_SERVER['PHP_AUTH_PW']) ||
    $_SERVER['PHP_AUTH_USER'] != $username ||
    $_SERVER['PHP_AUTH_PW'] != $password) {
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    die('Authentication required.');
}

// CSV file path
$csvFile = 'bandwidth_usage_history.csv';

// Check if file exists
if (!file_exists($csvFile)) {
    header('Content-Type: application/json');
    die(json_encode(['error' => 'No data available.']));
}

// Read CSV and convert to JSON
$data = [];
$file = fopen($csvFile, 'r');
$header = fgetcsv($file);
while ($row = fgetcsv($file)) {
    $data[] = [
        'date' => $row[0],
        'interface' => $row[1],
        'bytes_sent' => (int)$row[2],
        'bytes_recv' => (int)$row[3],
        'packets_sent' => (int)$row[4],
        'packets_recv' => (int)$row[5]
    ];
}
fclose($file);

// Output as JSON
header('Content-Type: application/json');
echo json_encode($data);
?>
```

### accesosapache

```python
# apache_request_rate_monitor.py
import csv
from datetime import datetime, timedelta
import re
import os

# Path to Apache2 access log
ACCESS_LOG = '/var/log/apache2/access.log'
# File to store request rate history
CSV_FILE = 'apache_request_rate_history.csv'

def parse_apache_log_line(line):
    """Parses a line from the Apache2 access log and returns the timestamp."""
    # Example log format: 127.0.0.1 - - [25/Nov/2025:12:00:00 +0100] "GET / HTTP/1.1" 200 1234
    match = re.search(r'\[([^\]]+)\]', line)
    if match:
        timestamp_str = match.group(1)
        return datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
    return None

def count_requests_per_minute(log_file, minutes=1):
    """Counts requests per minute from the Apache2 access log."""
    request_counts = {}
    current_time = datetime.now()
    time_window = timedelta(minutes=minutes)

    with open(log_file, 'r') as f:
        for line in f:
            timestamp = parse_apache_log_line(line)
            if timestamp and (current_time - timestamp) <= time_window:
                minute_key = timestamp.strftime('%Y-%m-%d %H:%M')
                request_counts[minute_key] = request_counts.get(minute_key, 0) + 1

    return request_counts

def save_request_rate(request_counts):
    """Saves request rate data to CSV."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['date', 'requests_per_minute'])
        for minute, count in request_counts.items():
            writer.writerow([minute, count])

if __name__ == '__main__':
    request_counts = count_requests_per_minute(ACCESS_LOG)
    save_request_rate(request_counts)
    print(f"Saved request rate data for {len(request_counts)} minutes.")
```

### accesosapache

```

```

### api

```
<?php
// api.php
$username = 'jocarsa'; // Change this
$password = 'jocarsa'; // Change this

// Check for valid credentials
if (!isset($_SERVER['PHP_AUTH_USER']) ||
    !isset($_SERVER['PHP_AUTH_PW']) ||
    $_SERVER['PHP_AUTH_USER'] != $username ||
    $_SERVER['PHP_AUTH_PW'] != $password) {
    header('WWW-Authenticate: Basic realm="Restricted Area"');
    header('HTTP/1.0 401 Unauthorized');
    die('Authentication required.');
}

// Get the endpoint from the query string
$endpoint = isset($_GET['endpoint']) ? $_GET['endpoint'] : '';

// Base directory for CSV files
$csvDir = 'monitor_data';

// Function to read CSV and return as JSON
function readCsvAsJson($csvFile) {
    if (!file_exists($csvFile)) {
        return ['error' => 'No data available.'];
    }
    $data = [];
    $file = fopen($csvFile, 'r');
    $header = fgetcsv($file);
    while ($row = fgetcsv($file)) {
        $data[] = array_combine($header, $row);
    }
    fclose($file);
    return $data;
}

// Serve data based on endpoint
header('Content-Type: application/json');
switch ($endpoint) {
    case 'cpu':
        echo json_encode(readCsvAsJson("$csvDir/cpu_usage.csv"));
        break;
    case 'ram':
        echo json_encode(readCsvAsJson("$csvDir/ram_usage.csv"));
        break;
    case 'disk_usage':
        echo json_encode(readCsvAsJson("$csvDir/disk_usage.csv"));
        break;
    case 'disk_io':
        $disk = isset($_GET['disk']) ? $_GET['disk'] : 'sda';
        echo json_encode(readCsvAsJson("$csvDir/disk_io_$disk.csv"));
        break;
    case 'bandwidth':
        $iface = isset($_GET['iface']) ? $_GET['iface'] : 'eth0';
        echo json_encode(readCsvAsJson("$csvDir/bandwidth_$iface.csv"));
        break;
    case 'apache_request_rate':
        echo json_encode(readCsvAsJson("$csvDir/apache_request_rate.csv"));
        break;
    default:
        echo json_encode(['error' => 'Invalid endpoint. Use: cpu, ram, disk_usage, disk_io, bandwidth, apache_request_rate']);
}
?>
```

### server_monitor

```python
# server_monitor.py
import psutil
import csv
from datetime import datetime, timedelta
import re
import os
from pytz import timezone  # You may need to install pytz: pip install pytz

# --- Config ---
CSV_DIR = 'monitor_data'
os.makedirs(CSV_DIR, exist_ok=True)

# --- Helper Functions ---
def save_to_csv(filename, headers, data):
    """Saves data to CSV, creating headers if the file doesn't exist."""
    filepath = os.path.join(CSV_DIR, filename)
    file_exists = os.path.isfile(filepath)
    with open(filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(data)

# --- CPU Monitoring ---
def monitor_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    save_to_csv('cpu_usage.csv', ['date', 'cpu_usage'], [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), cpu_usage])

# --- RAM Monitoring ---
def monitor_ram():
    ram = psutil.virtual_memory()
    save_to_csv('ram_usage.csv', ['date', 'ram_usage_percent', 'ram_total_gb'],
                [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ram.percent, round(ram.total / (1024 ** 3), 2)])

# --- Disk I/O Monitoring ---
def monitor_disk_io():
    disk_io_counters = psutil.disk_io_counters(perdisk=True)  # Fixed: Added this line
    for disk, io in disk_io_counters.items():
        save_to_csv(f'disk_io_{disk}.csv',
                    ['date', 'read_bytes', 'write_bytes', 'read_ops', 'write_ops', 'read_time_ms', 'write_time_ms', 'busy_time_ms'],
                    [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), io.read_bytes, io.write_bytes, io.read_count, io.write_count, io.read_time, io.write_time, io.busy_time])

# --- Disk Usage Monitoring ---
def monitor_disk_usage():
    disk_usage = psutil.disk_usage('/')
    save_to_csv('disk_usage.csv',
                ['date', 'disk_usage_percent', 'disk_total_gb', 'disk_free_gb'],
                [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), disk_usage.percent, round(disk_usage.total / (1024 ** 3), 2), round(disk_usage.free / (1024 ** 3), 2)])

# --- Bandwidth Monitoring ---
def monitor_bandwidth():
    net_io = psutil.net_io_counters(pernic=True)
    for iface, io in net_io.items():
        save_to_csv(f'bandwidth_{iface}.csv',
                    ['date', 'bytes_sent', 'bytes_recv', 'packets_sent', 'packets_recv'],
                    [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), io.bytes_sent, io.bytes_recv, io.packets_sent, io.packets_recv])

# --- Apache2 Request Rate Monitoring ---
def monitor_apache_request_rate():
    ACCESS_LOG = '/var/log/apache2/access.log'
    request_counts = {}
    current_time = datetime.now(timezone('UTC'))  # Make current_time timezone-aware
    time_window = timedelta(minutes=1)

    with open(ACCESS_LOG, 'r') as f:
        for line in f:
            match = re.search(r'\[([^\]]+)\]', line)
            if match:
                timestamp_str = match.group(1)
                timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')  # Already timezone-aware
                if (current_time - timestamp) <= time_window:
                    minute_key = timestamp.strftime('%Y-%m-%d %H:%M')
                    request_counts[minute_key] = request_counts.get(minute_key, 0) + 1

    for minute, count in request_counts.items():
        save_to_csv('apache_request_rate.csv', ['date', 'requests_per_minute'], [minute, count])

# --- Main ---
if __name__ == '__main__':
    monitor_cpu()
    monitor_ram()
    monitor_disk_io()
    monitor_disk_usage()
    monitor_bandwidth()
    monitor_apache_request_rate()
    print("Monitoring data saved.")
```

<a id="librerias-de-clases-y-componentes"></a>
## Librerías de clases y componentes

En este capítulo, nos adentramos en la generación de servicios en red utilizando librerías de clases y componentes. Comenzamos explorando los protocolos estándar de comunicación en red a nivel de aplicación, que son fundamentales para establecer conexiones seguras y eficientes entre diferentes sistemas.

A medida que avanzamos, nos familiarizamos con la arquitectura de servicios web, una forma popular de crear aplicaciones distribuidas. Aprenderemos sobre las librerías y componentes disponibles que facilitan el desarrollo de servidores y clientes web, permitiendo interactuar eficazmente con recursos en Internet.

El estudio de técnicas de programación segura es otro aspecto crucial que examinamos. Aprenderemos cómo implementar criptografía de clave pública y privada para proteger la información sensible durante las comunicaciones en red. También exploraremos los protocolos criptográficos más utilizados y cómo aplicar políticas de seguridad adecuadas para mantener la integridad y confidencialidad de los datos.

Además, nos dedicamos a entender cómo programar mecanismos de control de acceso que limiten el acceso a ciertos recursos solo a usuarios autorizados. Esto es fundamental para prevenir accesos no autorizados y garantizar la seguridad del sistema.

El desarrollo de aplicaciones con comunicaciones seguras es otro tema importante. Aprenderemos cómo utilizar protocolos seguros de comunicación, como HTTPS, para asegurar las transmisiones de datos entre el cliente y el servidor. También exploraremos técnicas avanzadas para mejorar la eficiencia y rendimiento de estas comunicaciones.

En este capítulo, también nos centramos en la implementación de aplicaciones clientes que pueden interactuar con servidores web utilizando librerías y componentes específicos. Aprenderemos cómo establecer conexiones, enviar solicitudes y recibir respuestas de manera eficiente, así como cómo manejar los errores que puedan surgir durante el proceso.

Finalmente, examinamos la monitorización del servicio y las herramientas disponibles para realizar este seguimiento. Aprenderemos cómo utilizar estas herramientas para identificar problemas y mejorar el rendimiento del sistema en tiempo real, garantizando una experiencia de usuario óptima.

A lo largo de esta subunidad, hemos cubierto un amplio espectro de temas relacionados con la generación de servicios en red utilizando librerías de clases y componentes. Desde los protocolos estándar hasta las técnicas avanzadas de programación segura, hemos proporcionado una base sólida para desarrolladores que desean crear aplicaciones robustas y seguras en entornos distribuidos.

<a id="programacion-de-servidores"></a>
## Programación de servidores

En este capítulo, nos adentramos en la generación de servicios en red, un aspecto crucial para el desarrollo de aplicaciones que requieren comunicación entre diferentes componentes o sistemas. Comenzamos por explorar los protocolos estándar de comunicación en red a nivel de aplicación, como HTTP y TCP/IP, que son fundamentales para establecer conexiones seguras y eficientes.

A continuación, nos centramos en la programación de servidores web, una de las aplicaciones más comunes de servicios en red. Aprenderemos cómo crear servidores que puedan manejar solicitudes HTTP, procesar datos y responder a los clientes de manera adecuada. Utilizaremos librerías y componentes específicos para facilitar este proceso, explorando tanto lenguajes como frameworks populares.

El estudio de la programación de servidores también implica el establecimiento y finalización de conexiones, una tarea que requiere un buen manejo de errores y excepciones. Aprenderemos a implementar protocolos seguros de comunicaciones, como HTTPS, para proteger la información en tránsito.

Además, aprenderemos cómo transmitir información entre el servidor y los clientes de manera eficiente, utilizando técnicas avanzadas de codificación y deserialización. Esto nos permitirá crear aplicaciones que puedan manejar grandes volúmenes de datos con alta velocidad y precisión.

La implementación de comunicaciones simultáneas es otro aspecto importante en la programación de servidores. Aprenderemos a utilizar hilos o procesos para manejar múltiples solicitudes al mismo tiempo, lo que mejora significativamente el rendimiento del servidor.

Finalmente, exploraremos técnicas de monitoreo y control del servicio, utilizando herramientas específicas para asegurar su funcionamiento continuo. Aprenderemos a identificar problemas y resolverlos rápidamente, garantizando la disponibilidad y eficiencia del servicio en red.

A lo largo de este capítulo, hemos cubierto los fundamentos necesarios para generar servicios en red efectivos y seguros. Cada concepto se ha desarrollado con un enfoque práctico, proporcionando una base sólida para el desarrollo de aplicaciones que requieren comunicación en red.

<a id="establecimiento-y-finalizacion-de-conexiones"></a>
## Establecimiento y finalización de conexiones

En la generación de servicios en red, establecer y finalizar conexiones es un proceso fundamental que permite la comunicación entre clientes y servidores. Este proceso implica una serie de pasos meticulosamente diseñados para asegurar la transmisión segura y eficiente de datos.

El primer paso en el establecimiento de una conexión consiste en la creación del socket, que es el punto de entrada a la red. En Python, por ejemplo, se utiliza la función `socket.socket()` para crear un objeto socket. Este objeto representa el extremo de la comunicación y puede ser configurado con diversas opciones dependiendo de las necesidades específicas del servicio.

Una vez creado el socket, el siguiente paso es establecer una conexión con el servidor a través del método `connect()`. Este método requiere como parámetro la dirección IP y el puerto del servidor al que se desea conectarse. Es crucial verificar que los valores proporcionados sean correctos para evitar errores de conexión.

La finalización de una conexión es tan importante como su establecimiento, ya que permite liberar recursos y asegurar que no haya fugas de memoria. En Python, esto se logra utilizando el método `close()` del objeto socket. Es recomendable cerrar la conexión tanto cuando todo el intercambio de datos esté completo como en caso de error para evitar situaciones inestables.

Durante el establecimiento y finalización de conexiones, es fundamental manejar excepciones para capturar cualquier error que pueda surgir durante el proceso. Esto se puede hacer utilizando bloques `try-except` en Python, lo que permite ejecutar código alternativo si ocurre un error, como intentar reconectar o notificar al usuario del problema.

Además de la gestión de errores, es crucial considerar la seguridad durante el establecimiento y finalización de conexiones. Esto implica utilizar protocolos seguros como HTTPS en lugar de HTTP para transferir datos sensibles. También es importante implementar medidas de autenticación y autorización para asegurar que solo los usuarios autorizados puedan acceder al servicio.

La optimización del proceso de establecimiento y finalización de conexiones también es una consideración importante, especialmente en aplicaciones con alta carga. Esto puede implicar técnicas como el reutilizar sockets cuando sea posible, utilizar multiplexado de eventos para manejar múltiples conexiones simultáneamente, o incluso implementar técnicas avanzadas como la persistencia de conexión.

En resumen, el establecimiento y finalización de conexiones en servicios de red es un proceso crítico que requiere una atención meticulosa a los detalles. Desde la creación del socket hasta la gestión de excepciones y la seguridad, cada paso debe ser cuidadosamente diseñado para garantizar la eficiencia y la confiabilidad del servicio.

<a id="transmision-de-informacion"></a>
## Transmisión de información

En este capítulo, nos adentramos en la transmisión de información a través de servicios en red, un tema fundamental para el desarrollo de aplicaciones que requieren comunicación entre diferentes componentes o sistemas. Comenzamos por explorar los protocolos estándar de comunicación en red a nivel de aplicación, como HTTP y FTP, que son fundamentales para la transferencia de datos entre clientes y servidores.

A medida que avanzamos, nos familiarizaremos con los servicios web, una forma moderna y eficiente de proporcionar acceso a funcionalidades a través de Internet. Estos servicios utilizan protocolos como SOAP (Simple Object Access Protocol) o REST (Representational State Transfer), cada uno con sus ventajas y desventajas en términos de simplicidad y escalabilidad.

Además, aprenderemos sobre las librerías y componentes disponibles para facilitar la implementación de comunicaciones en red. Estas herramientas abstratan muchos detalles complejos, permitiendo a los desarrolladores se centren en la lógica de negocio mientras el sistema se encarga del transporte seguro y eficiente de datos.

Una parte crucial de esta subunidad es entender cómo establecer y finalizar conexiones con servidores remotos. Esto implica conocer cómo crear sockets, manejar errores y asegurarse de que las comunicaciones sean seguras y confiables. También exploraremos técnicas para implementar comunicaciones simultáneas, lo cual es esencial en aplicaciones web y móviles donde la interactividad es clave.

Finalmente, dedicamos tiempo a monitorear el servicio y utilizar herramientas adecuadas para asegurar su correcto funcionamiento. Esto incluye la detección de problemas, el análisis de rendimiento y la optimización de las comunicaciones para mejorar la experiencia del usuario.

A lo largo de este capítulo, hemos cubierto los aspectos técnicos y prácticos necesarios para transmitir información eficazmente a través de servicios en red. Cada concepto se ha desarrollado con un enfoque práctico, acompañado de ejemplos y explicaciones detalladas, para que los lectores puedan aplicar estos conocimientos en sus propios proyectos.

<a id="implementacion-de-comunicaciones-simultaneas"></a>
## Implementación de comunicaciones simultáneas

En este capítulo, nos adentramos en la implementación de comunicaciones simultáneas en servicios web, una habilidad esencial para el desarrollo de aplicaciones que requieren manejar múltiples solicitudes a la vez. Comenzamos por entender los conceptos básicos de sockets y cómo establecer conexiones entre clientes y servidores.

Los sockets son puntos de conexión entre dos programas que permiten la comunicación en red. En un servidor, se crean sockets para escuchar las solicitudes entrantes, mientras que en el cliente, se utilizan sockets para enviar datos al servidor. La implementación de comunicaciones simultáneas implica mantener múltiples sockets abiertos y gestionarlas eficientemente.

Para manejar varias conexiones simultáneamente, los servidores pueden utilizar diferentes patrones de diseño. Uno de los más comunes es el modelo "thread per connection", donde se crea un hilo para cada conexión entrante. Cada hilo atiende a una solicitud individual hasta que se completa, permitiendo al servidor manejar múltiples solicitudes simultáneamente.

Sin embargo, este enfoque puede llevar a problemas de escalabilidad y rendimiento si el servidor tiene limitaciones en la cantidad de hilos que puede crear. Por lo tanto, es importante considerar alternativas como el modelo "thread pool", donde un grupo fijo de hilos se reutiliza para manejar múltiples solicitudes.

Además de los hilos, también existen técnicas basadas en eventos y selectores que permiten manejar múltiples sockets sin crear un hilo por cada conexión. Estas técnicas son especialmente útiles en entornos con alta carga y pueden ser implementadas utilizando bibliotecas como `selectors` en Python o `libevent` en C.

La gestión de conexiones simultáneas requiere una buena comprensión de los estados de los sockets y cómo cambiar entre ellos. Los estados más comunes son el estado "LISTEN" (escuchando), "ESTABLISHED" (conexión establecida) y "CLOSED" (conexión cerrada). Es crucial mantener un control preciso sobre estos estados para evitar problemas como la congestión de sockets o la pérdida de datos.

Para implementar comunicaciones simultáneas, es necesario tener en cuenta también el manejo de errores. Los servidores deben estar preparados para detectar y gestionar excepciones que puedan surgir durante la comunicación, como conexiones interrumpidas o errores de red.

En este capítulo, hemos explorado los fundamentos de la implementación de comunicaciones simultáneas en servicios web. Aprender a manejar múltiples solicitudes a la vez es crucial para el desarrollo de aplicaciones escalables y eficientes. Con un buen entendimiento de sockets, hilos y técnicas avanzadas como selectores, los desarrolladores pueden crear servidores robustos que puedan procesar una alta carga de trabajo sin problemas.

A medida que avanzamos en este capítulo, profundizaremos en las mejores prácticas para la implementación de comunicaciones simultáneas, incluyendo el uso de bibliotecas y frameworks específicos, así como técnicas de optimización y rendimiento. Este conocimiento es fundamental para cualquier desarrollador que quiera crear aplicaciones web eficientes y escalables.

<a id="utilizacion-de-aplicaciones-clientes"></a>
## Utilización de aplicaciones clientes

En este capítulo, nos adentramos en la generación de servicios en red, una área crucial para el desarrollo de aplicaciones que requieren comunicación entre clientes y servidores. Comenzamos explorando los protocolos estándar de comunicación en red a nivel de aplicación, como HTTP y TCP/IP, que son fundamentales para establecer conexiones seguras y eficientes.

A continuación, nos sumergimos en el estudio de servicios web, una forma popular de implementar aplicaciones distribuidas. Aprenderemos cómo crear servidores web utilizando librerías y componentes específicos, así como cómo manejar las solicitudes y respuestas entre clientes y servidores. Este conocimiento es esencial para desarrollar aplicaciones que requieren acceso a recursos remotos.

Además, exploramos técnicas avanzadas de programación segura en el contexto de servicios web, incluyendo la implementación de criptografía y políticas de seguridad robustas. Aprenderemos cómo proteger nuestras aplicaciones contra amenazas comunes como ataques de inyección SQL y cross-site scripting (XSS), lo que es crucial para mantener la confidencialidad y integridad de los datos.

Continuamos con el estudio de técnicas de programación segura en el contexto de servicios web, incluyendo la implementación de criptografía y políticas de seguridad robustas. Aprenderemos cómo proteger nuestras aplicaciones contra amenazas comunes como ataques de inyección SQL y cross-site scripting (XSS), lo que es crucial para mantener la confidencialidad y integridad de los datos.

A medida que avanzamos, nos familiarizamos con técnicas avanzadas de programación segura en el contexto de servicios web, incluyendo la implementación de criptografía y políticas de seguridad robustas. Aprenderemos cómo proteger nuestras aplicaciones contra amenazas comunes como ataques de inyección SQL y cross-site scripting (XSS), lo que es crucial para mantener la confidencialidad y integridad de los datos.

Finalmente, exploramos técnicas avanzadas de programación segura en el contexto de servicios web, incluyendo la implementación de criptografía y políticas de seguridad robustas. Aprenderemos cómo proteger nuestras aplicaciones contra amenazas comunes como ataques de inyección SQL y cross-site scripting (XSS), lo que es crucial para mantener la confidencialidad y integridad de los datos.

En este capítulo, hemos cubierto una amplia gama de temas relacionados con la generación de servicios en red. Aprendimos sobre protocolos estándar, servicios web, técnicas avanzadas de programación segura y cómo implementarlas en nuestras aplicaciones. Este conocimiento es fundamental para desarrollar sistemas robustos y seguros que puedan comunicarse eficientemente entre clientes y servidores.

<a id="monitorizacion-del-servicio-herramientas"></a>
## Monitorización del servicio. Herramientas

La monitorización del servicio es un aspecto crucial en la generación de servicios en red, ya que permite mantener el rendimiento óptimo y detectar problemas antes de que afecten a los usuarios. Para llevar a cabo esta tarea, existen diversas herramientas disponibles que facilitan la supervisión continua del estado de los servicios.

Una de las herramientas más utilizadas para monitorizar servicios es **Prometheus**, un sistema de alerta y métricas de código abierto. Prometheus recolecta datos sobre el rendimiento de los servicios a través de una red de escraper, que son agentes que se ejecutan en los servidores donde se alojan los servicios. Estos agentes recopilan métricas como la carga del sistema, el uso de memoria y CPU, así como cualquier otra información relevante definida por el usuario.

Otra herramienta popular es **Grafana**, un software de visualización y análisis de datos que puede ser utilizado junto con Prometheus para crear dashboards interactivos. Grafana permite a los administradores visualizar las métricas recopiladas por Prometheus en gráficos y tablas, facilitando la identificación de tendencias y anomalías.

Además de estas herramientas, existen soluciones más especializadas como **Zabbix**, que ofrece una interfaz gráfica intuitiva para monitorizar sistemas y aplicaciones. Zabbix permite configurar alertas basadas en métricas específicas, lo que facilita la respuesta rápida a problemas potenciales.

Para monitorear servicios web, herramientas como **Nagios** son útiles. Nagios puede verificar el estado de los servicios a través de comandos de prueba y enviar alertas cuando se detectan fallos. Esta herramienta es especialmente útil para sistemas que dependen de múltiples servicios interconectados.

En el ámbito de la red, **Wireshark** es una herramienta poderosa para capturar y analizar paquetes de red en tiempo real. Wireshark permite a los administradores identificar problemas de rendimiento o seguridad en la red, proporcionando información detallada sobre el tráfico que atraviesa el sistema.

Además de las herramientas mencionadas, es importante considerar la implementación de **logs** para monitoreo. Los logs registran eventos importantes dentro del sistema y pueden ser analizados posteriormente para identificar problemas o mejorar el rendimiento. Herramientas como **ELK Stack (Elasticsearch, Logstash, Kibana)** proporcionan una plataforma completa para recopilar, almacenar y visualizar logs de aplicaciones y sistemas.

La monitorización continua es un proceso dinámico que requiere ajustes constantes. Es importante establecer indicadores clave de rendimiento (KPIs) relevantes para el servicio en cuestión y configurar alertas basadas en estos KPIs. Además, la documentación detallada del estado del sistema y las acciones realizadas durante la monitorización es crucial para mantener un historial confiable.

En conclusión, la monitorización del servicio es una tarea fundamental en la generación de servicios en red. La elección de las herramientas adecuadas depende del tipo de servicio y las necesidades específicas del sistema. Al utilizar herramientas como Prometheus, Grafana, Nagios y Wireshark, los administradores pueden mantener un control preciso sobre el rendimiento y la disponibilidad de sus servicios, lo que es esencial para garantizar una experiencia óptima para los usuarios finales.


<a id="utilizacion-de-tecnicas-de-programacion-segura"></a>
# Utilización de técnicas de programación segura

<a id="practicas-de-programacion-segura"></a>
## Prácticas de programación segura

La programación segura es una práctica fundamental en cualquier desarrollo de software moderno. En este contexto, las prácticas de programación segura se refieren a las técnicas y métodos utilizados para diseñar, implementar y mantener sistemas que protegen la información sensible y eviten vulnerabilidades potenciales. Estas prácticas abordan desde el diseño del sistema hasta su despliegue en producción.

La primera etapa de cualquier proyecto seguro es la identificación de riesgos potenciales. Esto implica comprender las amenazas a las que está expuesto el sistema y cómo pueden ser mitigadas. Los desarrolladores deben estar constantemente actualizados sobre las últimas amenazas y técnicas de hacking para poder implementar medidas efectivas.

Una práctica crucial es la validación de entradas y salidas de datos. Cualquier dato que entre o salga del sistema debe ser validado para asegurar que cumple con ciertos criterios, como su formato o su contenido. Esto ayuda a prevenir inyecciones SQL, ataques XSS y otros tipos de ataques basados en la manipulación de datos.

El uso de contraseñas seguras es otro aspecto fundamental de la programación segura. Las contraseñas deben ser complejas, únicas y cambiadas regularmente. Además, es importante implementar medidas como el almacenamiento seguro de las contraseñas (mediante hash) y la autenticación multifactor.

La gestión adecuada de errores también es una práctica clave. Los mensajes de error deben ser claros pero no reveladores de detalles internos del sistema. Esto ayuda a prevenir ataques basados en errores, donde un atacante puede intentar descubrir información sensible examinando los mensajes de error que se muestran.

La programación segura también implica la implementación de medidas de autorización y autenticación robustas. Los sistemas deben estar diseñados para permitir el acceso solo a usuarios autorizados, utilizando métodos como tokens de sesión o autenticación basada en roles.

El uso de librerías y frameworks seguros es otro aspecto importante. Estos componentes predefinidos suelen ser más seguros que la implementación propia debido a las pruebas y revisión realizadas por sus desarrolladores. Sin embargo, es crucial seguir las mejores prácticas al usar estas herramientas.

La programación segura también implica el desarrollo de aplicaciones resistentes a los ataques de denegación de servicio (DoS) y ataques DDoS. Esto puede implicar la implementación de técnicas como la limitación de velocidad de solicitud o la distribución del tráfico entre múltiples servidores.

La programación segura también debe considerar el aspecto legal y regulatorio. Muchos países tienen leyes que regulan cómo se maneja la información personal, y los desarrolladores deben estar al tanto de estas regulaciones para evitar problemas legales.

En conclusión, la programación segura es una práctica integral en cualquier proyecto de desarrollo de software. Al seguir las mejores prácticas de programación segura, los desarrolladores pueden crear sistemas que sean más resistentes a las amenazas y protejan la información sensible de sus usuarios.

<a id="criptografia-de-clave-publica-y-clave-privada"></a>
## Criptografía de clave pública y clave privada

La criptografía de clave pública y clave privada es una técnica fundamental para la seguridad en la programación de servicios y procesos. Esta técnica permite que dos partes se comuniquen de forma segura a través de internet o cualquier otro medio de transmisión, garantizando tanto la confidencialidad como la integridad de los datos intercambiados.

La clave pública es un número grande que se comparte públicamente y se utiliza para cifrar mensajes. El destinatario puede usar esta clave para cifrar su mensaje, pero solo él podrá descifrarlo con su correspondiente clave privada, que debe mantenerse en secreto. Por otro lado, la clave privada es utilizada por el remitente para firmar los datos, lo que permite al receptor verificar la autenticidad del emisor.

La criptografía de clave pública y clave privada se utiliza ampliamente en protocolos de seguridad como SSL/TLS para proteger las comunicaciones web, en sistemas de correo electrónico para garantizar la privacidad de los correos electrónicos, y en aplicaciones móviles para proteger los datos almacenados y transmitidos.

Además de cifrar mensajes, la criptografía de clave pública y clave privada también se utiliza para autenticar identidades. Cuando un usuario intenta acceder a un servicio seguro, el servidor le envía una solicitud de autenticación que el usuario responde con su firma digital, generada con su clave privada. El servidor puede verificar la firma utilizando la clave pública del usuario, lo que garantiza que el mensaje ha sido firmado por el usuario y no ha sido alterado.

La implementación de la criptografía de clave pública y clave privada en aplicaciones requiere un buen manejo de las claves y una comprensión profunda de los algoritmos utilizados. Es importante asegurarse de que las claves sean generadas de manera segura, almacenadas adecuadamente y no se expongan a posibles ataques.

En resumen, la criptografía de clave pública y clave privada es una herramienta poderosa para proteger los datos en la programación de servicios y procesos. Al utilizar esta técnica, podemos garantizar que nuestros sistemas sean seguros contra amenazas externas y que solo las partes autorizadas puedan acceder a la información confidencial.

<a id="principales-aplicaciones-de-la-criptografia"></a>
## Principales aplicaciones de la criptografía

La criptografía es una herramienta fundamental para garantizar la seguridad en los sistemas informáticos modernos. En esta subunidad, exploraremos las principales aplicaciones de la criptografía, destacando cómo se utiliza para proteger datos, comunicaciones y transacciones digitales.

Primero, consideremos el ámbito de la comunicación segura. La criptografía juega un papel crucial en los protocolos de seguridad web (HTTPS), donde cifra tanto los datos como las credenciales de usuario para evitar su interceptación por terceros. Además, en aplicaciones móviles y redes sociales, la autenticación de usuarios a través de contraseñas seguras se realiza mediante técnicas criptográficas.

En el ámbito empresarial, la criptografía es esencial para proteger los datos sensibles almacenados en sistemas ERP-CRM. Los algoritmos de cifrado aseguran que solo los usuarios autorizados puedan acceder a información como clientes, productos y transacciones financieras. Esto es especialmente importante en industrias reguladas donde la protección de datos es una cuestión legal.

La seguridad en las comunicaciones entre servidores y clientes también depende de la criptografía. Protocolos como SSL/TLS utilizan algoritmos criptográficos para establecer canales seguros que protegen los datos durante su transmisión a través de Internet. Esto es crucial para mantener la privacidad y confidencialidad en servicios web y aplicaciones móviles.

Además, la criptografía se utiliza en el ámbito del almacenamiento encriptado de datos. Los sistemas operativos modernos ofrecen opciones para cifrar los discos duros o partes específicas del sistema, asegurando que incluso si un dispositivo es robado, los datos sensibles no puedan ser accedidos sin la clave correcta.

En el campo de la inteligencia artificial y aprendizaje automático, la seguridad de los algoritmos y modelos es cada vez más relevante. Los sistemas de recomendación basados en contenido o colaborativo pueden utilizar técnicas criptográficas para proteger las preferencias del usuario y mantener su privacidad.

La seguridad en el mundo de los juegos también requiere la aplicación de criptografía. Algunos motores de juegos utilizan algoritmos criptográficos para proteger los datos de los jugadores, como sus progresos o información personal, asegurando que no puedan ser alterados por terceros.

En resumen, las principales aplicaciones de la criptografía abarcan desde la comunicación segura en Internet hasta la protección de datos sensibles en sistemas empresariales y aplicaciones móviles. Desde el almacenamiento encriptado hasta la seguridad en el mundo del aprendizaje automático, la criptografía es una herramienta esencial para garantizar la confidencialidad, integridad y autenticidad de los datos en un mundo cada vez más digitalizado.

<a id="protocolos-criptograficos"></a>
## Protocolos criptográficos

La seguridad en las aplicaciones es un aspecto crucial que no debe ser subestimado, especialmente cuando se trata de la programación de servicios y procesos. En esta subunidad, nos centraremos en los protocolos criptográficos, que son fundamentales para proteger la información durante su transmisión y almacenamiento.

Los protocolos criptográficos utilizan algoritmos matemáticos complejos para convertir datos legibles (claramente comprensibles) en una forma codificada que solo puede ser descifrada por alguien con el conocimiento de las claves correctas. Este proceso, conocido como cifrado, es crucial para mantener la confidencialidad y integridad de los datos.

Un ejemplo común de protocolo criptográfico es SSL/TLS (Secure Sockets Layer/Transport Layer Security), que se utiliza en muchos sitios web para proteger las comunicaciones entre el cliente y el servidor. Este protocolo establece una conexión segura mediante la negociación de claves, cifrado de datos y autenticación del servidor.

Además de los protocolos de comunicación, también existen algoritmos criptográficos que se utilizan para almacenar información de manera segura en las bases de datos. Por ejemplo, el algoritmo bcrypt es ampliamente utilizado para almacenar contraseñas de forma segura, ya que incluso si un atacante obtiene acceso a la base de datos, no podrá descifrar las contraseñas sin el algoritmo correspondiente.

La implementación correcta de protocolos criptográficos requiere una comprensión profunda de los conceptos matemáticos y de seguridad. Es importante entender cómo funcionan estos protocolos y cómo pueden ser vulnerables si no se implementan correctamente. Por ejemplo, el uso de claves débiles o la exposición de claves en el código fuente son dos errores comunes que pueden comprometer la seguridad.

Además de los protocolos de comunicación y almacenamiento, también hay algoritmos criptográficos utilizados para autenticar usuarios y asegurar las transacciones. Por ejemplo, el protocolo OAuth se utiliza para permitir a los usuarios acceder a recursos protegidos sin compartir sus credenciales directamente.

En resumen, la programación de servicios y procesos requiere un enfoque cuidadoso hacia la seguridad, y los protocolos criptográficos son una herramienta esencial para proteger la información. Al comprender cómo funcionan estos protocolos y cómo implementarlos correctamente, podemos crear aplicaciones más seguras y confiables.

Es importante recordar que la seguridad no debe ser un paso opcional en el desarrollo de software, sino una prioridad desde el principio. Solo con una abordaje integral y riguroso de la seguridad, podremos construir aplicaciones que sean resistentes a las amenazas y protejan la información de nuestros usuarios.

En esta subunidad, hemos explorado los protocolos criptográficos y su importancia en la programación de servicios y procesos. Aprendimos sobre diferentes tipos de protocolos, como SSL/TLS, y cómo implementarlos correctamente para proteger la información. También vimos cómo utilizar algoritmos criptográficos para almacenar información de manera segura y autenticar usuarios.

Esperamos que esta subunidad te haya proporcionado una comprensión sólida de los protocolos criptográficos y su importancia en el desarrollo seguro de aplicaciones. Con este conocimiento, podrás crear sistemas más robustos y confiables que protejan la información de tus usuarios.

<a id="politica-de-seguridad-roles"></a>
## Política de seguridad. Roles

La seguridad es un aspecto crucial en cualquier sistema informático, especialmente cuando se trata de servicios y procesos que manejan datos sensibles o interactúan con múltiples usuarios. En esta subunidad, exploraremos cómo implementar una política de seguridad efectiva y cómo definir roles para asegurar la integridad y confidencialidad de los sistemas.

Primero, es fundamental establecer una política de seguridad clara que defina las medidas a seguir para proteger el sistema contra amenazas. Esta política debe incluir directrices sobre el acceso a recursos, la gestión de contraseñas, la detección y respuesta a incidentes, y la documentación de todas las políticas y procedimientos.

Los roles son un componente esencial de cualquier sistema de seguridad. Cada rol tiene un conjunto específico de permisos que determinan qué acciones pueden realizar los usuarios asignados a ese rol. Por ejemplo, en un sistema ERP-CRM, podríamos tener roles como "Administrador", "Gerente" y "Vendedor". El Administrador tendría acceso completo al sistema, el Gerente tendría permisos limitados para supervisar operaciones y el Vendedor solo tendría acceso a las funciones necesarias para realizar sus tareas.

La asignación de roles debe basarse en el principio del mínimo privilegio, que establece que los usuarios solo deben tener los permisos necesarios para realizar su trabajo. Esto minimiza el daño potencial si un usuario malintencionado obtiene acceso no autorizado a ciertos recursos.

Además de definir roles y asignar permisos, es importante monitorear y auditar el sistema para detectar cualquier actividad sospechosa o inusual. Las herramientas de monitorización pueden ayudar a identificar patrones que podrían indicar un ataque en curso o una violación de la seguridad.

La educación y formación también son aspectos cruciales de la implementación de políticas de seguridad. Los usuarios deben estar conscientes de las mejores prácticas de seguridad y cómo proteger su cuenta contra amenazas comunes. Esto puede incluir la realización de sesiones de formación periódicas, el envío de correos electrónicos informativos y la creación de documentación detallada sobre políticas y procedimientos.

En el contexto de los servicios y procesos, también es importante considerar la seguridad en la comunicación. Los protocolos de comunicación deben estar diseñados para proteger la confidencialidad y integridad de los datos transmitidos entre diferentes componentes del sistema. Esto puede implicar el uso de cifrado SSL/TLS, autenticación de dos factores y otras medidas de seguridad avanzadas.

La implementación de políticas de seguridad y roles debe ser un proceso continuo que se adapte a las necesidades cambiantes del sistema y a los riesgos emergentes. Es importante realizar evaluaciones regulares de la seguridad y actualizar las políticas y procedimientos según sea necesario para mantener el sistema protegido.

En resumen, la implementación de una política de seguridad efectiva y la definición de roles adecuados son fundamentales para proteger los sistemas de servicios y procesos. Al establecer directrices claras sobre el acceso a recursos, asignar permisos limitados según el principio del mínimo privilegio, monitorear y auditar el sistema, educar a los usuarios y considerar la seguridad en la comunicación, podemos crear un entorno seguro que minimice el riesgo de incidentes y proteja los datos sensibles.

<a id="programacion-de-mecanismos-de-control-de-acceso"></a>
## Programación de mecanismos de control de acceso

La programación segura es un aspecto crucial que cada desarrollador debe considerar desde el principio del diseño de cualquier sistema o aplicación. Uno de los mecanismos fundamentales para garantizar la seguridad es implementar mecanismos de control de acceso, que determinan quién puede realizar qué acciones dentro del sistema.

Los mecanismos de control de acceso se basan en dos tipos principales: el control de acceso basado en roles (RBAC) y el control de acceso basado en listas de permitidos/deniedos (ACL). El RBAC es un enfoque que asocia a los usuarios con roles, y luego asigna permisos a esos roles. Por otro lado, el ACL permite especificar directamente qué usuarios o grupos tienen permiso para realizar acciones específicas.

En la práctica, la implementación de estos mecanismos puede variar dependiendo del lenguaje de programación y el framework utilizado. En Java, por ejemplo, se pueden utilizar anotaciones como `@RolesAllowed` y `@DenyAll` para controlar el acceso a métodos en una clase. En Python, la biblioteca `flask-security` proporciona funcionalidades robustas para manejar roles y permisos.

Es importante recordar que los mecanismos de control de acceso no son solo sobre permitir o denegar acciones, sino también sobre monitorear y registrar quién realiza qué acción. Esto es fundamental para la auditoría y el diagnóstico de problemas de seguridad.

Además, la implementación segura de mecanismos de control de acceso debe considerar la autenticación y la autorización. La autenticación verifica la identidad del usuario, mientras que la autorización determina qué acciones puede realizar una vez autenticado. Es crucial que estos procesos sean seguros y confiables para evitar ataques como inyección SQL o XSS.

En el contexto de aplicaciones web, es común utilizar frameworks como Spring Security en Java o Flask-Security en Python para manejar la seguridad. Estos frameworks proporcionan una capa adicional de abstracción que simplifica la implementación de mecanismos de control de acceso y autenticación.

La programación segura no es solo sobre evitar problemas, sino también sobre prevenirlos. Esto implica seguir buenas prácticas como el encriptado de datos sensibles, la validación de entradas del usuario y la minimización de privilegios innecesarios para los usuarios.

En resumen, la programación segura es una tarea compleja pero crucial que requiere un enfoque integral. Los mecanismos de control de acceso son uno de los pilares fundamentales de esta seguridad, y su implementación adecuada puede hacer una gran diferencia en la confianza y el rendimiento de cualquier sistema o aplicación.

<a id="encriptacion-de-informacion"></a>
## Encriptación de información

En un mundo donde la seguridad digital es cada vez más crucial, la encriptación de información se ha convertido en una herramienta fundamental para proteger datos sensibles. Esta subunidad explora los métodos y técnicas utilizados para cifrar información, desde las bases hasta aplicaciones prácticas.

La encriptación es el proceso de codificación de datos para que solo puedan ser descifrados por alguien con la clave correcta. Este método es esencial en cualquier sistema que maneje información confidencial, ya sea en redes, bases de datos o aplicaciones web. La seguridad de los sistemas depende en gran medida de cómo se implementa y gestiona la encriptación.

Existen varios algoritmos de encriptación disponibles, cada uno con sus propias características y niveles de seguridad. Algunos de los más populares incluyen AES (Advanced Encryption Standard), RSA y DES (Data Encryption Standard). Cada uno tiene sus ventajas y desventajas, y la elección del algoritmo adecuado depende de factores como el nivel de confianza requerido, la velocidad de procesamiento y la complejidad de la implementación.

La encriptación no solo protege los datos mientras se transmiten a través de una red, sino que también es crucial para la seguridad local. Almacenar información cifrada en discos duros o servidores aumenta significativamente la resistencia contra ataques cibernéticos. Además, la encriptación permite un acceso controlado a los datos, asegurando que solo las personas autorizadas puedan acceder a ellos.

Además de la encriptación de datos, también es importante considerar la seguridad del proceso de encriptación y desencriptación. La gestión adecuada de claves es crucial para mantener el sistema seguro. Las claves deben ser fuertes, únicas y cambiadas regularmente. Además, es fundamental implementar medidas de autenticación y autorización para controlar quién puede generar, distribuir y usar las claves.

La encriptación también juega un papel importante en la protección contra ataques de interceptación. Al cifrar los datos antes de su envío, cualquier persona que intente interceptarlos no podrá leer el contenido sin la clave correcta. Esto es especialmente relevante en aplicaciones web y servicios en red, donde la seguridad de los datos transmisoros y receptores es fundamental.

En resumen, la encriptación de información es una técnica esencial para proteger datos sensibles en cualquier sistema digital. Desde el algoritmo utilizado hasta la gestión adecuada de claves, cada aspecto del proceso de encriptación debe ser cuidadosamente considerado y gestionado. Al implementar medidas efectivas de encriptación, se puede asegurar que los datos sean seguros tanto durante su transmisión como mientras están almacenados, lo que es crucial para la confianza y el funcionamiento eficiente de cualquier sistema digital moderno.

### encriptar

```
<?php
  $cadena = "Jose Vicente";
  echo $cadena[0];
  
  
?>
```

### ascii

```
<?php
  $cadena = "Jose Vicente";
  $ascii = ord($cadena[0]);
  $ascii += 5;
  $caracter = chr($ascii);
  echo $caracter;
  
  
?>
```

### repetir el proceso ccon la cadena completa

```
<?php
  $cadena = "Jose Vicente";
  $resultado = "";
  for($i = 0;$i<strlen($cadena);$i++){
    $ascii = ord($cadena[$i]);
    $ascii += 5;
    $resultado .= chr($ascii);
  }
  echo $resultado;
  
  $desencriptado = "";
  for($i = 0;$i<strlen($resultado);$i++){
    $ascii = ord($resultado[$i]);
    $ascii -= 5;
    $desencriptado .= chr($ascii);
  }
  echo $desencriptado;
?>
```

### convierto a funciones

```
<?php
  $cadena = "Jose Vicente";
  
  function encripta($objeto){
    $resultado = "";
    for($i = 0;$i<strlen($objeto);$i++){
      $ascii = ord($objeto[$i]);
      $ascii += 5;
      $resultado .= chr($ascii);
    }
    return $resultado;
  }
  function desencripta($objeto){
    $desencriptado = "";
    for($i = 0;$i<strlen($objeto);$i++){
      $ascii = ord($objeto[$i]);
      $ascii -= 5;
      $desencriptado .= chr($ascii);
    }
    return $desencriptado;
  }
  
  echo $cadena."<br>";
  $encriptado = encripta($cadena);
  echo $encriptado."<br>";
  $desencriptado = desencripta($encriptado);
  echo $desencriptado."<br>";
?>
```

### metodos de una clase

```
<?php
  $cadena = "Jose Vicente";
  class Encriptador{
    function encripta($objeto){
      $resultado = "";
      for($i = 0;$i<strlen($objeto);$i++){
        $ascii = ord($objeto[$i]);
        $ascii += 5;
        $resultado .= chr($ascii);
      }
      return $resultado;
    }
    function desencripta($objeto){
      $desencriptado = "";
      for($i = 0;$i<strlen($objeto);$i++){
        $ascii = ord($objeto[$i]);
        $ascii -= 5;
        $desencriptado .= chr($ascii);
      }
      return $desencriptado;
    }
  }
  $encriptador = new Encriptador();
  echo $cadena."<br>";
  $encriptado = $encriptador->encripta($cadena);
  echo $encriptado."<br>";
  $desencriptado = $encriptador->desencripta($encriptado);
  echo $desencriptado."<br>";
?>
```

### encriptar mysql

```
<?php
  $cadena = "Jose Vicente";
  class Encriptador{
    function encripta($objeto){
      $resultado = "";
      for($i = 0;$i<strlen($objeto);$i++){
        $ascii = ord($objeto[$i]);
        $ascii += 5;
        $resultado .= chr($ascii);
      }
      return $resultado;
    }
    function desencripta($objeto){
      $desencriptado = "";
      for($i = 0;$i<strlen($objeto);$i++){
        $ascii = ord($objeto[$i]);
        $ascii -= 5;
        $desencriptado .= chr($ascii);
      }
      return $desencriptado;
    }
  }
  <?php
// Conexión a la base de datos
$mysqli = new mysqli("localhost", "tienda2526", "tienda2526", "tienda2526");

$sql = "SELECT * FROM clientes";
$result = $mysqli->query($sql);

$datos = [];

while ($row = $result->fetch_assoc()) {
    $datos[] = $row;
}

// Imprimir como JSON
header('Content-Type: application/json; charset=utf-8');
echo json_encode($datos, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);


?>
```

### saco como json

```
<?php
  $cadena = "Jose Vicente";
  class Encriptador{
    function encripta($objeto){
      $resultado = "";
      for($i = 0;$i<strlen($objeto);$i++){
        $ascii = ord($objeto[$i]);
        $ascii += 5;
        $resultado .= chr($ascii);
      }
      return $resultado;
    }
    function desencripta($objeto){
      $desencriptado = "";
      for($i = 0;$i<strlen($objeto);$i++){
        $ascii = ord($objeto[$i]);
        $ascii -= 5;
        $desencriptado .= chr($ascii);
      }
      return $desencriptado;
    }
  }

  // Conexión a la base de datos
  $mysqli = new mysqli("localhost", "tienda2526", "tienda2526", "tienda2526");

  $sql = "SELECT * FROM clientes";
  $result = $mysqli->query($sql);

  $datos = [];

  while ($row = $result->fetch_assoc()) {
      $datos[] = $row;
  }

  // Imprimir como JSON
  header('Content-Type: application/json; charset=utf-8');
  echo json_encode($datos, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);


?>
```

### ahora encripto

```
<?php
// MODO DEBUG (actívalo mientras pruebas)
error_reporting(E_ALL);
ini_set('display_errors', 1);

$cadena = "Jose Vicente";

class Encriptador {
    function encripta($objeto){
        $resultado = "";
        for($i = 0; $i < strlen($objeto); $i++){
            $ascii = ord($objeto[$i]);
            $ascii += 5;
            $resultado .= chr($ascii);
        }
        return $resultado;
    }
    function desencripta($objeto){
        $desencriptado = "";
        for($i = 0; $i < strlen($objeto); $i++){
            $ascii = ord($objeto[$i]);
            $ascii -= 5;
            $desencriptado .= chr($ascii);
        }
        return $desencriptado;
    }
}

$enc = new Encriptador();

// Conexión a la base de datos
$mysqli = new mysqli("localhost", "tienda2526", "tienda2526", "tienda2526");

// Comprobar conexión
if ($mysqli->connect_errno) {
    die("Error de conexión: " . $mysqli->connect_error);
}

$sql = "SELECT * FROM clientes";
$result = $mysqli->query($sql);

// Comprobar consulta
if (!$result) {
    die("Error en la consulta: " . $mysqli->error);
}

$datos = [];

while ($row = $result->fetch_assoc()) {
    $filaEncriptada = [];
    foreach ($row as $campo => $valor) {
        $valor = (string)$valor;

        // 1) Cifro con tu algoritmo
        $cifradoBinario = $enc->encripta($valor);
        // 2) Lo convierto a texto seguro para JSON
        $filaEncriptada[$campo] = base64_encode($cifradoBinario);
    }
    $datos[] = $filaEncriptada;
}

// Imprimir como JSON
header('Content-Type: application/json; charset=utf-8');

$json = json_encode($datos, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

// Comprobar errores de json_encode por si acaso
if ($json === false) {
    die("Error al codificar JSON: " . json_last_error_msg());
}

echo $json;
```

### cliente

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Clientes - Encriptados</title>
  <style>
    :root {
      --bg: #0f172a;
      --bg-alt: #020617;
      --card-bg: #020617;
      --accent: #38bdf8;
      --accent-soft: rgba(56, 189, 248, 0.15);
      --text: #e5e7eb;
      --text-muted: #9ca3af;
      --border: #1f2937;
      --radius-lg: 16px;
      --radius-md: 10px;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: radial-gradient(circle at top, #1e293b 0, #020617 40%, #000 100%);
      color: var(--text);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .app {
      width: 100%;
      max-width: 960px;
      background: linear-gradient(135deg, rgba(148,163,184,0.15), rgba(15,23,42,0.9));
      border-radius: 24px;
      border: 1px solid rgba(148,163,184,0.35);
      box-shadow:
        0 18px 80px rgba(15,23,42,0.8),
        0 0 0 1px rgba(15,23,42,1);
      padding: 24px 28px 28px;
      position: relative;
      overflow: hidden;
    }

    .app::before {
      content: "";
      position: absolute;
      inset: -40%;
      background:
        radial-gradient(circle at 0% 0%, rgba(56,189,248,0.18), transparent 55%),
        radial-gradient(circle at 110% 10%, rgba(96,165,250,0.18), transparent 55%);
      opacity: 0.7;
      pointer-events: none;
      z-index: -1;
    }

    .header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 20px;
    }

    .title-block {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    h1 {
      margin: 0;
      font-size: 1.5rem;
      letter-spacing: 0.03em;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .badge {
      font-size: 0.7rem;
      padding: 3px 8px;
      border-radius: 999px;
      border: 1px solid rgba(148,163,184,0.6);
      background: rgba(15,23,42,0.8);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--text-muted);
    }

    .subtitle {
      margin: 0;
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    .status {
      font-size: 0.85rem;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(15,23,42,0.9);
      border: 1px solid rgba(148,163,184,0.5);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 10px rgba(56,189,248,0.8);
    }

    .table-card {
      background: rgba(15,23,42,0.9);
      border-radius: var(--radius-lg);
      border: 1px solid rgba(30,64,175,0.7);
      box-shadow:
        0 16px 45px rgba(15,23,42,0.9),
        0 0 0 1px rgba(15,23,42,0.85);
      padding: 16px;
      position: relative;
      overflow: hidden;
    }

    .table-card::before {
      content: "";
      position: absolute;
      inset: -50%;
      background:
        radial-gradient(circle at 12% 120%, rgba(56,189,248,0.12), transparent 60%),
        radial-gradient(circle at 110% -10%, rgba(129,140,248,0.12), transparent 55%);
      opacity: 0.6;
      pointer-events: none;
      z-index: -1;
    }

    .table-container {
      max-height: 420px;
      overflow: auto;
      border-radius: var(--radius-md);
      border: 1px solid rgba(30,64,175,0.8);
      background: radial-gradient(circle at top, rgba(30,64,175,0.25), rgba(15,23,42,0.98));
      position: relative;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      min-width: 480px;
    }

    thead {
      position: sticky;
      top: 0;
      z-index: 1;
    }

    thead tr {
      background: radial-gradient(circle at top, rgba(56,189,248,0.18), rgba(15,23,42,0.98));
    }

    th, td {
      padding: 9px 12px;
      text-align: left;
      border-bottom: 1px solid rgba(15,23,42,0.9);
      white-space: nowrap;
    }

    th {
      font-weight: 500;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--text-muted);
      border-bottom: 1px solid rgba(37,99,235,0.9);
      backdrop-filter: blur(10px);
    }

    tbody tr {
      background: linear-gradient(
        90deg,
        rgba(15,23,42,0.95),
        rgba(15,23,42,0.98)
      );
      transition: background 0.18s ease, transform 0.18s ease, box-shadow 0.18s ease;
    }

    tbody tr:nth-child(even) {
      background: linear-gradient(
        90deg,
        rgba(15,23,42,0.98),
        rgba(15,23,42,1)
      );
    }

    tbody tr:hover {
      background: linear-gradient(
        90deg,
        rgba(30,64,175,0.35),
        rgba(15,23,42,0.98)
      );
      transform: translateY(-1px);
      box-shadow: 0 8px 22px rgba(15,23,42,0.95);
    }

    td {
      color: var(--text);
      font-variant-numeric: tabular-nums;
    }

    td.key-cell {
      color: var(--accent);
      font-weight: 500;
    }

    .hidden {
      display: none;
    }

    .message {
      margin-top: 8px;
      font-size: 0.82rem;
      color: var(--text-muted);
    }

    .pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border-radius: 999px;
      border: 1px solid rgba(148,163,184,0.5);
      background: rgba(15,23,42,0.9);
      padding: 4px 10px;
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .pill span {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.18em;
    }

    @media (max-width: 640px) {
      .app {
        padding: 16px;
      }
      h1 {
        font-size: 1.25rem;
      }
      .table-card {
        padding: 12px;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <div class="header">
      <div class="title-block">
        <h1>
          Clientes
          <span class="badge">Encrypted API</span>
        </h1>
        <p class="subtitle">
          Data is fetched from <code>clientes.php</code>, decrypted in the browser, and rendered as a table.
        </p>
      </div>
      <div>
        <div id="status" class="status">
          <span class="status-dot"></span>
          <span id="status-text">Loading data…</span>
        </div>
      </div>
    </div>

    <div class="table-card">
      <div class="pill">
        <span>Client side</span>
        decrypt · base64 → shift -5
      </div>
      <div class="table-container" style="margin-top: 10px;">
        <table id="clientesTable" class="hidden">
          <thead id="tableHead"></thead>
          <tbody id="tableBody"></tbody>
        </table>
      </div>
      <div id="message" class="message"></div>
    </div>
  </div>

  <script>
    // Adjust this if your PHP endpoint has a different name or path
    const ENDPOINT = '008-ahora encripto.php';

    // Mirrors your PHP desencripta() after Base64 decoding
    function desencriptaShift(str) {
      let result = '';
      for (let i = 0; i < str.length; i++) {
        const ascii = str.charCodeAt(i);
        result += String.fromCharCode(ascii - 5);
      }
      return result;
    }

    function desencriptaCampo(encodedValue) {
      if (encodedValue == null) return '';
      // 1) Base64 decode
      const shifted = atob(encodedValue);
      // 2) Shift -5 to get original
      return desencriptaShift(shifted);
    }

    function setStatus(text, ok = true) {
      const statusText = document.getElementById('status-text');
      const dot = document.querySelector('.status-dot');
      statusText.textContent = text;
      if (ok) {
        dot.style.background = 'var(--accent)';
        dot.style.boxShadow = '0 0 10px rgba(56,189,248,0.8)';
      } else {
        dot.style.background = '#f97373';
        dot.style.boxShadow = '0 0 10px rgba(248,113,113,0.8)';
      }
    }

    function buildTable(data) {
      const table = document.getElementById('clientesTable');
      const thead = document.getElementById('tableHead');
      const tbody = document.getElementById('tableBody');
      const message = document.getElementById('message');

      // Clear previous content
      thead.innerHTML = '';
      tbody.innerHTML = '';
      message.textContent = '';

      if (!data || data.length === 0) {
        message.textContent = 'No records found.';
        table.classList.add('hidden');
        return;
      }

      // Get column names from first row
      const keys = Object.keys(data[0]);

      // Build header
      const trHead = document.createElement('tr');
      keys.forEach(key => {
        const th = document.createElement('th');
        th.textContent = key;
        trHead.appendChild(th);
      });
      thead.appendChild(trHead);

      // Build body
      data.forEach(row => {
        const tr = document.createElement('tr');
        keys.forEach((key, index) => {
          const td = document.createElement('td');
          const raw = row[key];

          // decrypted value
          const value = desencriptaCampo(raw);

          // first column slightly highlighted (e.g. id / code)
          if (index === 0) {
            td.classList.add('key-cell');
          }

          td.textContent = value;
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });

      table.classList.remove('hidden');
      message.textContent = `${data.length} record(s) loaded and decrypted.`;
    }

    async function cargarClientes() {
      try {
        setStatus('Loading data…');
        const response = await fetch(ENDPOINT);

        if (!response.ok) {
          throw new Error(`HTTP ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        console.log(data)
        buildTable(data);
        setStatus('Data loaded correctly');
      } catch (error) {
        console.error(error);
        setStatus('Error loading data', false);
        const message = document.getElementById('message');
        message.textContent = 'Error loading or decrypting data: ' + error.message;
      }
    }

    cargarClientes();
  </script>
</body>
</html>
```

<a id="protocolos-seguros-de-comunicaciones"></a>
## Protocolos seguros de comunicaciones

En el mundo digital actual, la seguridad es una prioridad incesante. Cuando se habla de programación de servicios y procesos, la seguridad no puede ser ignorada. Los protocolos seguros de comunicación son fundamentales para proteger la información en tránsito entre diferentes sistemas y aplicaciones.

Los protocolos seguros de comunicación utilizan técnicas avanzadas para garantizar que los datos se transmitan de manera confidencial, auténtica e inalterable. Uno de los protocolos más conocidos es HTTPS, que utiliza SSL/TLS para cifrar la información entre el cliente y el servidor web.

Además de HTTPS, existen otros protocolos seguros como SSH (Secure Shell) para conexiones de red seguras, FTPS (FTP sobre SSL/TLS) para transferencias de archivos seguras, y SMTPS (SMTP sobre SSL/TLS) para correos electrónicos seguros. Cada uno de estos protocolos tiene sus propias características y ventajas dependiendo del contexto en el que se utilicen.

La implementación de protocolos seguros no es solo una cuestión técnica, sino también una práctica ética y legal. Muchas jurisdicciones requieren la utilización de protocolos seguros para proteger la información personal y sensible de los usuarios. Por lo tanto, es crucial que cualquier desarrollador o administrador de sistemas tenga un conocimiento sólido sobre cómo implementar y mantener estos protocolos.

Además de los protocolos seguros de comunicación, también es importante considerar la seguridad en el diseño y desarrollo de aplicaciones. Esto incluye la utilización de prácticas de programación segura, como la validación de entradas, la protección contra inyecciones SQL y la gestión adecuada de errores.

La seguridad debe ser un enfoque integral en el desarrollo de software. No es suficiente con implementar protocolos seguros de comunicación; también es necesario considerar la seguridad en todas las capas del sistema, desde la red hasta la aplicación. Solo así se puede garantizar que los datos y la información sean protegidos en un entorno digital cada vez más complejo y amenazado.

En resumen, la utilización de protocolos seguros de comunicación es una parte crucial del desarrollo de software seguro. Al implementar estos protocolos, no solo se protegen los datos en tránsito, sino que también se asegura la confidencialidad, autenticidad e integridad de toda la información procesada por el sistema. Es un aspecto fundamental que debe ser considerado en cada etapa del desarrollo y mantenerse actualizado con las mejores prácticas y tecnologías disponibles.

<a id="programacion-de-aplicaciones-con-comunicaciones-seguras"></a>
## Programación de aplicaciones con comunicaciones seguras

La programación segura es un aspecto crucial que cada desarrollador debe considerar al crear aplicaciones, especialmente cuando se trata de comunicaciones en red. En esta subunidad, nos centraremos en cómo implementar técnicas de seguridad para proteger nuestras aplicaciones contra amenazas potenciales.

Primero, es fundamental entender los principios básicos de la criptografía y cómo se pueden aplicar a las comunicaciones seguras. La criptografía es el arte de codificar información de tal manera que solo pueda ser descifrada por alguien con el conocimiento adecuado. En el contexto de la programación, esto implica utilizar algoritmos de cifrado fuertes para proteger los datos en tránsito.

La seguridad de las comunicaciones también depende del manejo adecuado de claves y certificados digitales. Las claves son fundamentales para la autenticidad y confidencialidad de los datos, mientras que los certificados digitales proporcionan una forma de verificar la identidad de un intercambio.

Además, es importante implementar medidas de seguridad en el nivel del protocolo de comunicación. Por ejemplo, al utilizar HTTP, se recomienda migrar a HTTPS para proteger contra interceptaciones y falsificaciones de datos. Los protocolos seguros como TLS (Transport Layer Security) o SSL (Secure Sockets Layer) son fundamentales para garantizar la integridad y confidencialidad de las comunicaciones.

La autenticación y autorización también son elementos cruciales en la seguridad de las aplicaciones. La autenticación verifica la identidad del usuario, mientras que la autorización determina qué acciones puede realizar ese usuario dentro de la aplicación. Implementar sistemas robustos de autenticación y autorización es esencial para prevenir el acceso no autorizado a los recursos.

La gestión adecuada de sesiones es otro aspecto importante en la seguridad de las comunicaciones. Las sesiones deben ser iniciadas con un proceso seguro, mantenerse activas durante el tiempo necesario y luego cerrarse correctamente. Utilizar técnicas como tokens de sesión o autenticación basada en cookies puede ayudar a mejorar la seguridad.

La protección contra ataques de inyección es otro desafío importante en la programación segura. Las inyecciones ocurren cuando un atacante introduce código malicioso en una entrada del usuario, lo que puede llevar a daños significativos a la aplicación. Usar parámetros preparados y evitar el uso directo de entradas del usuario en consultas SQL es una práctica recomendada para prevenir estas amenazas.

La seguridad contra ataques de fuerza bruta también es crucial, especialmente cuando se trata de autenticación. Estos ataques intentan adivinar contraseñas mediante un exhaustivo intento de todas las posibles combinaciones. Implementar medidas como la limitación del número de intentos fallidos y el uso de técnicas de hash fuerte pueden ayudar a mitigar estos riesgos.

La seguridad en el almacenamiento de datos es otro aspecto importante. Aunque los datos se transmiten seguros, su almacenamiento puede presentar riesgos si no se maneja adecuadamente. Utilizar encriptación para proteger los datos mientras están almacendos y implementar políticas de acceso estrictas pueden ayudar a prevenir el robo o la manipulación de estos datos.

Finalmente, es importante realizar pruebas de seguridad regulares para identificar y corregir vulnerabilidades. Las pruebas de penetración (pen testing) y las auditorías de seguridad pueden ayudar a detectar problemas potenciales antes de que puedan ser explotados por un atacante.

En resumen, la programación segura es una tarea compleja pero crucial en el desarrollo de aplicaciones. Al implementar técnicas de criptografía, manejo adecuado de claves y certificados, seguridad en los protocolos de comunicación, autenticación y autorización, gestión de sesiones, protección contra inyecciones, seguridad contra ataques de fuerza bruta, seguridad en el almacenamiento de datos y pruebas de seguridad regulares, podemos crear aplicaciones que sean más seguras y resistentes a las amenazas potenciales.


<a id="actividad-libre-de-final-de-evaluacion-la-milla-extra"></a>
# Actividad libre de final de evaluación - La milla extra

<a id="la-milla-extra-primera-evaluacion"></a>
## La Milla Extra - Primera evaluación

### ejercicio

```markdown

```
