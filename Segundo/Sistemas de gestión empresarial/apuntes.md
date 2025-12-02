# Sistemas de gestión empresarial

**Author:** Jose Vicente Carratala Sanchis

## Table of contents

- [Identificación de sistemas ERP-CRM](#identificacion-de-sistemas-erp-crm)
  - [Concepto de ERP](#concepto-de-erp)
  - [Revisión de los ERP actuales](#revision-de-los-erp-actuales)
  - [Concepto de CRM](#concepto-de-crm)
  - [Revisión de los CRM actuales](#revision-de-los-crm-actuales)
  - [Tipos de licencias de los ERP-CRM](#tipos-de-licencias-de-los-erp-crm)
  - [Sistemas gestores de bases de datos compatibles con el software](#sistemas-gestores-de-bases-de-datos-compatibles-con-el-software)
  - [Instalación y configuración del sistema informático](#instalacion-y-configuracion-del-sistema-informatico)
  - [Verificación de la instalación y configuración](#verificacion-de-la-instalacion-y-configuracion)
  - [Documentación de las operaciones realizadas](#documentacion-de-las-operaciones-realizadas)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad)
- [Instalación y configuración de sistemas ERP-CRM](#instalacion-y-configuracion-de-sistemas-erp-crm)
  - [Tipos de instalación.](#tipos-de-instalacion)
  - [Módulos de un sistema ERP-CRM](#modulos-de-un-sistema-erp-crm)
  - [Procesos de instalación del sistema ERP-CRM](#procesos-de-instalacion-del-sistema-erp-crm)
  - [Parámetros de configuración del sistema ERP-CRM](#parametros-de-configuracion-del-sistema-erp-crm)
  - [Actualización del sistema ERP-CRM y aplicación de actualizaciones](#actualizacion-del-sistema-erp-crm-y-aplicacion-de-actualizaciones)
  - [Servicios de acceso al sistema ERP-CRM](#servicios-de-acceso-al-sistema-erp-crm)
  - [Entornos de desarrollo, pruebas y explotación](#entornos-de-desarrollo-pruebas-y-explotacion)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad-1)
  - [Examen final](#examen-final)
- [Organización y consulta de la información](#organizacion-y-consulta-de-la-informacion)
  - [Definición de campos](#definicion-de-campos)
  - [Consultas de acceso a datos](#consultas-de-acceso-a-datos)
  - [Interfaces de entrada de datos y de procesos.](#interfaces-de-entrada-de-datos-y-de-procesos)
  - [Informes y listados de la aplicación](#informes-y-listados-de-la-aplicacion)
  - [Gestión de pedidos](#gestion-de-pedidos)
  - [Gráficos](#graficos)
  - [Herramientas de monitorización y de evaluación del rendimiento](#herramientas-de-monitorizacion-y-de-evaluacion-del-rendimiento)
  - [Incidencias identificación y resolución](#incidencias-identificacion-y-resolucion)
  - [Procesos de extracción de datos en sistemas de ERP-CRM y almacenes de datos](#procesos-de-extraccion-de-datos-en-sistemas-de-erp-crm-y-almacenes-de-datos)
  - [Inteligencia de negocio (Business Intelligence)](#inteligencia-de-negocio-business-intelligence)
- [Implantación de sistemas ERP-CRM en una empresa](#implantacion-de-sistemas-erp-crm-en-una-empresa)
  - [Tipos de empresa. Necesidades de la empresa](#tipos-de-empresa-necesidades-de-la-empresa)
  - [Selección de los módulos del sistema ERP-CRM](#seleccion-de-los-modulos-del-sistema-erp-crm)
  - [Tablas y vistas que es preciso adaptar](#tablas-y-vistas-que-es-preciso-adaptar)
  - [Consultas necesarias para obtener información](#consultas-necesarias-para-obtener-informacion)
  - [Creación de formularios personalizados](#creacion-de-formularios-personalizados)
  - [Creación de informes personalizados](#creacion-de-informes-personalizados)
  - [Paneles de control (Dashboards)](#paneles-de-control-dashboards)
  - [Integración con otros sistemas de gestión](#integracion-con-otros-sistemas-de-gestion)
- [Desarrollo de componentes](#desarrollo-de-componentes)
  - [Arquitectura del ERP-CRM](#arquitectura-del-erp-crm)
  - [Lenguaje proporcionado](#lenguaje-proporcionado)
  - [Entornos de desarrollo y herramientas del sistema ERP y CRM](#entornos-de-desarrollo-y-herramientas-del-sistema-erp-y-crm)
  - [Inserción, modificación y eliminación de datos en los objetos](#insercion-modificacion-y-eliminacion-de-datos-en-los-objetos)
  - [Operaciones de consulta. Herramientas](#operaciones-de-consulta-herramientas)
  - [Formularios e informes](#formularios-e-informes)
  - [Procesamiento de datos y obtención de la información](#procesamiento-de-datos-y-obtencion-de-la-informacion)
  - [Llamadas a funciones, librerías de funciones (APIs)](#llamadas-a-funciones-librerias-de-funciones-apis)
  - [Depuración y tratamiento de errores](#depuracion-y-tratamiento-de-errores)
- [Actividad libre de final de evaluación - La milla extra](#actividad-libre-de-final-de-evaluacion-la-milla-extra)
  - [La Milla Extra - Primera evaluación](#la-milla-extra-primera-evaluacion)

---

<a id="identificacion-de-sistemas-erp-crm"></a>
# Identificación de sistemas ERP-CRM

<a id="concepto-de-erp"></a>
## Concepto de ERP

En el ámbito empresarial, los sistemas ERP (Enterprise Resource Planning) desempeñan un papel crucial como centros de control y coordinación de todas las operaciones internas de una organización. Estos sistemas integran diversos procesos clave, desde la gestión financiera hasta la producción y la cadena de suministro, permitiendo una visión global y coherente del negocio.

El concepto de ERP se basa en el principio de que todos los datos relevantes para la operación empresarial deben estar disponibles en un solo lugar. Esto facilita la toma de decisiones informadas, mejora la eficiencia operativa y permite una mejor comunicación entre diferentes departamentos. Los sistemas ERP no son solo herramientas de almacenamiento de información; también proporcionan funcionalidades avanzadas como análisis prediccional, optimización de procesos y gestión de riesgos.

La arquitectura típica de un sistema ERP incluye módulos especializados que abordan diferentes aspectos del negocio. Algunos de los principales módulos son el financiero (gestión de cuentas por cobrar y por pagar, presupuesto), la operativa (producción, inventario, almacenes), la comercial (venta, compras, clientes y proveedores) y la gestión de recursos humanos (nomina, contratación, formación). Cada uno de estos módulos está diseñado para interactuar entre sí, asegurando que toda la información esté actualizada y coherente.

La implementación de un sistema ERP requiere una planificación cuidadosa. Esto incluye el análisis de las necesidades del negocio, la selección adecuada del sistema, la formación del personal y la adaptación de los procesos existentes. La integración con otros sistemas de la empresa es fundamental para garantizar que todos los datos se gestionen de manera consistente.

Los beneficios de un sistema ERP son numerosos. Mejoran la eficiencia operativa al reducir el tiempo y los errores en las tareas repetitivas, permitiendo a los ejecutivos tomar decisiones basadas en información precisa y actualizada. Además, facilitan la colaboración entre diferentes departamentos y promueven una cultura de transparencia dentro de la organización.

En resumen, un sistema ERP es una herramienta integral para el funcionamiento eficiente de una empresa. Su implementación adecuada puede transformar significativamente los procesos internos, mejorando la toma de decisiones, la productividad y la competitividad del negocio.

<a id="revision-de-los-erp-actuales"></a>
## Revisión de los ERP actuales

En este capítulo, nos adentramos en la exploración de los sistemas ERP (Enterprise Resource Planning) actuales, que son herramientas fundamentales para la gestión integral de una organización. Los ERP no solo gestionan operaciones internas como producción y ventas, sino que también coordinan procesos financieros, recursos humanos y logísticos. Este sistema integra todos estos aspectos en un único entorno digital, permitiendo una visión global y eficiente del negocio.

Los ERP actuales ofrecen una variedad de funcionalidades avanzadas, desde la planificación estratégica hasta el análisis financiero detallado. Algunas de las principales características incluyen la gestión de inventario, control de calidad, procesos de compras y ventas, y sistemas de contabilidad automatizados. Estas herramientas no solo optimizan los procesos internos, sino que también facilitan la toma de decisiones basada en datos precisos.

La elección del ERP adecuado es crucial para el éxito empresarial. Los sistemas modernos ofrecen opciones personalizadas y escalables, adaptándose a las necesidades específicas de cada organización. Además, los ERP integran fácilmente con otros sistemas de gestión, como CRM (Customer Relationship Management) o BI (Business Intelligence), creando una plataforma unificada para la toma de decisiones.

La implementación de un ERP requiere una planificación cuidadosa y una formación adecuada del personal. Los usuarios deben entender completamente las funcionalidades del sistema para aprovechar al máximo su potencial. Además, es importante considerar el impacto en los procesos existentes y la necesidad de adaptaciones.

Los ERP actuales también incorporan tecnologías emergentes como la inteligencia artificial y la aprendizaje automático, lo que permite una predicción más precisa del comportamiento del negocio y la optimización de recursos. Estas herramientas pueden identificar tendencias ocultas en los datos, mejorar la eficiencia operativa y anticipar problemas potenciales.

En resumen, los ERP actuales representan un paso importante hacia la digitalización y la automatización de las operaciones empresariales. Al seleccionar y implementar el sistema adecuado, una organización puede mejorar significativamente su productividad, eficiencia y capacidad para tomar decisiones informadas. Este capítulo ha proporcionado una visión general de los ERP actuales, sus funcionalidades y la importancia de su elección y implementación en un entorno empresarial moderno.

<a id="concepto-de-crm"></a>
## Concepto de CRM

En el ámbito empresarial, la gestión eficiente es un elemento clave para el éxito de cualquier organización. Para abordar este desafío, se han desarrollado diversos sistemas que facilitan la administración de los procesos internos, incluyendo los sistemas ERP (Enterprise Resource Planning) y CRM (Customer Relationship Management). Aunque ambos son herramientas valiosas, su enfoque y funcionalidades tienen diferencias significativas.

El CRM, o Customer Relationship Management, se centra específicamente en la gestión de relaciones con los clientes. Este sistema es diseñado para recopilar, almacenar y analizar datos sobre los clientes, lo que permite una mejor comprensión del comportamiento y las preferencias individuales de cada uno. A través del CRM, las empresas pueden personalizar sus estrategias de marketing y ventas, mejorar la satisfacción del cliente y aumentar la retención.

La principal ventaja del CRM radica en su capacidad para centralizar toda la información relacionada con los clientes en un solo lugar. Esto facilita el seguimiento de interacciones pasadas y futuras, así como el acceso a datos demográficos, comportamentales y de compra. Además, permite la creación de perfiles detallados de cada cliente, lo que es crucial para segmentar mercados y diseñar campañas publicitarias más efectivas.

Además del seguimiento de clientes, los sistemas CRM también ofrecen herramientas para gestionar las interacciones internas de la empresa. Esto incluye el seguimiento de oportunidades de negocio, gestión de proyectos y colaboración entre equipos. La integración con otros sistemas empresariales como ERP permite una visión completa de la operación total de la organización.

El CRM no solo es una herramienta de gestión de datos; también es un recurso estratégico que apoya decisiones comerciales. Al proporcionar análisis detallados y visualizaciones, las empresas pueden identificar tendencias, patrones y oportunidades para mejorar su negocio. Además, facilita la toma de decisiones basada en datos, lo que puede llevar a una mayor eficiencia operativa y rentabilidad.

En resumen, el CRM es un sistema integral diseñado para optimizar las relaciones con los clientes y mejorar la gestión empresarial en su conjunto. Su capacidad para recopilar, almacenar y analizar datos de manera centralizada proporciona una visión única del cliente y la empresa, lo que es fundamental para el éxito a largo plazo en cualquier sector.

<a id="revision-de-los-crm-actuales"></a>
## Revisión de los CRM actuales

En este capítulo, nos adentramos en la exploración de los sistemas de gestión relacional (CRM) actuales, complementando nuestra visión previa sobre los sistemas ERP. A diferencia de los ERP que se centran en todas las operaciones empresariales, los CRM se enfocan específicamente en el manejo y análisis de datos relacionados con los clientes.

Los CRM modernos ofrecen una gama de funcionalidades avanzadas para recopilar, almacenar y analizar información detallada sobre los clientes. Estas herramientas permiten a las empresas no solo mantener un registro preciso de sus relaciones comerciales, sino también utilizar esta información para mejorar la experiencia del cliente y optimizar procesos internos.

Una característica distintiva de los CRM actuales es su capacidad para integrarse con otros sistemas empresariales, facilitando la sincronización de datos entre diferentes departamentos. Esto permite una visión holística de las operaciones de la empresa y un análisis más profundo de los patrones de comportamiento del cliente.

Además, los CRM modernos incorporan herramientas de inteligencia de negocio (BI) que permiten crear informes personalizados y gráficos interactivos. Estas visualizaciones facilitan la toma de decisiones estratégicas basadas en datos reales y actualizados.

Es importante destacar que la elección del CRM adecuado depende de las necesidades específicas de cada empresa. Algunos sistemas son más orientados a pequeñas empresas, ofreciendo funcionalidades básicas y un costo accesible, mientras que otros están diseñados para grandes corporaciones con requerimientos complejos y altos niveles de personalización.

La implementación exitosa de un CRM requiere una planificación cuidadosa. Esto incluye la identificación de los procesos a automatizar, la selección de campos relevantes para el registro de clientes, y la definición de roles y privilegios adecuados para diferentes usuarios dentro de la organización.

En resumen, los CRM actuales representan una herramienta poderosa para mejorar la eficiencia operativa y la satisfacción del cliente. Su capacidad para integrarse con otros sistemas empresariales y proporcionar análisis detallados de datos es fundamental en un entorno competitivo. A medida que las empresas continúan evolucionando, los CRM seguirán adaptándose para ofrecer soluciones cada vez más sofisticadas y centradas en el cliente.

<a id="tipos-de-licencias-de-los-erp-crm"></a>
## Tipos de licencias de los ERP-CRM

En el mundo empresarial, los sistemas ERP-CRM (Enterprise Resource Planning - Planificación de Recursos Empresariales y Customer Relationship Management - Gestión Relacional de Clientes) son herramientas cruciales que optimizan la eficiencia operativa y facilitan la toma de decisiones estratégicas. Uno de los aspectos importantes a considerar al seleccionar un sistema ERP-CRM es su licenciatura, ya que esto puede tener un impacto significativo en el costo total de implementación y en las capacidades del software.

Existen varios tipos de licencias para sistemas ERP-CRM, cada una con sus propias ventajas y desventajas. La licencia más común es la licencia por usuario (User License), que se basa en el número de usuarios activos que utilizarán el sistema. Esta opción ofrece un control preciso sobre los recursos disponibles y puede ser adecuada para empresas con un uso variable o fluctuante.

Otra opción popular es la licencia por módulo (Module License). En este caso, el software se divide en diferentes módulos, cada uno con su propio conjunto de funciones. Las empresas pueden elegir solo los módulos que necesitan, lo que puede resultar en una mayor eficiencia económica y un uso más personalizado del sistema.

Además, existen licencias basadas en la cantidad de datos gestionados (Data License). Esta opción es especialmente útil para empresas con grandes volúmenes de información a manejar. La tarifa se calcula según el tamaño del conjunto de datos almacenado, lo que puede ser más económico si la empresa espera un crecimiento significativo.

La licencia por uso (Usage License) es otra variante interesante. En este modelo, el costo se basa en la cantidad de tiempo que los usuarios pasan utilizando el sistema. Esta opción puede ser útil para empresas con flujos de trabajo altamente dinámicos o para aquellos que desean pagar solo por lo que utilizan.

Es importante destacar que cada tipo de licencia tiene sus propias consideraciones y requisitos. Por ejemplo, algunas licencias pueden requerir una adquisición inicial más alta pero ofrecen un mayor control sobre los recursos disponibles. En cambio, las licencias basadas en el uso pueden ser más económicas a corto plazo pero pueden resultar costosas a largo plazo si la empresa experimenta un crecimiento significativo.

Además de considerar el tipo de licencia, también es crucial evaluar cómo se aplican los términos y condiciones asociados. Algunas licencias pueden incluir restricciones sobre la exportación del software o la capacidad de utilizarlo en múltiples ubicaciones geográficas. Es fundamental que las empresas comprendan estos detalles para evitar futuros problemas legales.

En resumen, al seleccionar un sistema ERP-CRM y su tipo de licencia, las empresas deben considerar cuidadosamente sus necesidades específicas, el tamaño del equipo de usuarios y los factores económicos. Cada tipo de licencia tiene sus ventajas y desventajas, por lo que es crucial realizar una evaluación exhaustiva para tomar la decisión más informada posible. Una buena comprensión de las diferentes opciones disponibles permitirá a las empresas encontrar la solución ERP-CRM que mejor se adapte a su situación empresarial, optimizando así su eficiencia operativa y reduciendo los costos asociados con el software.

<a id="sistemas-gestores-de-bases-de-datos-compatibles-con-el-software"></a>
## Sistemas gestores de bases de datos compatibles con el software

En la identificación de sistemas ERP-CRM, es crucial entender que estos programas requieren una base de datos sólida para almacenar y gestionar toda la información empresarial. Los sistemas gestores de bases de datos (SGBDs) desempeñan un papel fundamental en esta tarea, proporcionando las herramientas necesarias para crear, mantener y optimizar el almacenamiento de datos.

Existen varios tipos de SGBDs que son compatibles con los sistemas ERP-CRM, cada uno con sus propias características y ventajas. Algunos de los más populares incluyen MySQL, PostgreSQL, Oracle Database y Microsoft SQL Server. Cada uno de estos SGBDs ofrece diferentes niveles de escalabilidad, rendimiento y funcionalidad que pueden adaptarse a las necesidades específicas de una empresa.

MySQL es conocido por su alta disponibilidad y facilidad de uso, lo que lo hace ideal para aplicaciones ERP-CRM que requieren un alto nivel de confiabilidad. PostgreSQL ofrece características avanzadas como soporte para transacciones ACID, lo que lo convierte en una opción sólida para entornos empresariales complejos.

Oracle Database es una solución robusta y segura, especialmente adecuada para grandes empresas con requisitos de alta disponibilidad y rendimiento. Su capacidad para manejar grandes volúmenes de datos y su soporte para múltiples usuarios simultáneos lo hacen una opción popular en el mercado.

Microsoft SQL Server, por otro lado, es conocido por su integridad y compatibilidad con otros productos Microsoft, lo que facilita la implementación y gestión de sistemas ERP-CRM dentro de entornos corporativos. Su soporte para transacciones distribuidas y su capacidad para manejar grandes volúmenes de datos hacen de SQL Server una opción sólida para aplicaciones empresariales.

Al seleccionar un SGBD compatible con los sistemas ERP-CRM, es importante considerar factores como la escalabilidad, el rendimiento, la seguridad, la compatibilidad con otros productos y las capacidades de soporte técnico. Cada empresa tendrá sus propias necesidades específicas, por lo que es crucial realizar una evaluación cuidadosa para seleccionar el SGBD más adecuado.

Además, es importante tener en cuenta que los sistemas ERP-CRM suelen requerir un alto nivel de integridad y seguridad en la gestión de datos. Por lo tanto, es fundamental elegir un SGBD que ofrezca características avanzadas como control de transacciones, autenticación y autorización, y copias de seguridad regulares.

En resumen, al identificar sistemas ERP-CRM, es crucial considerar el tipo de SGBD que mejor se adapte a las necesidades específicas de la empresa. Cada SGBD tiene sus propias características y ventajas, por lo que es importante realizar una evaluación cuidadosa para seleccionar el más adecuado. Además, es fundamental tener en cuenta factores como la escalabilidad, el rendimiento, la seguridad y la compatibilidad con otros productos al elegir un SGBD compatible con los sistemas ERP-CRM.

<a id="instalacion-y-configuracion-del-sistema-informatico"></a>
## Instalación y configuración del sistema informático

La instalación y configuración del sistema informático es un proceso fundamental que garantiza la correcta operativa de cualquier software empresarial, como los sistemas ERP (Enterprise Resource Planning) y CRM (Customer Relationship Management). Este proceso implica no solo el despliegue del software en el entorno adecuado sino también su ajuste a las necesidades específicas de la organización. 

El primer paso es seleccionar un sistema ERP o CRM que se adapte a los requisitos de la empresa, considerando factores como la escala operativa, la complejidad de los procesos y el presupuesto disponible. Una vez elegido el software, se procede con la instalación, que puede realizarse de manera local en servidores dedicados o en la nube, dependiendo de las preferencias organizacionales.

La configuración del sistema es igualmente crucial. Involucra la definición de parámetros y ajustes específicos para que el software funcione según las necesidades de la empresa. Esto puede incluir la creación de campos personalizados, la configuración de roles y permisos, y la definición de procesos de negocio específicos.

Es importante destacar que la instalación y configuración no son tareas una sola vez, sino un proceso continuo que debe adaptarse a los cambios en las necesidades de la empresa. Por lo tanto, es recomendable establecer un sistema de mantenimiento y actualización regular para asegurar el funcionamiento óptimo del software.

Además, durante este proceso, es fundamental documentar todas las operaciones realizadas. Esto no solo facilita el seguimiento y auditoría de los cambios, sino que también es invaluable en caso de problemas o necesidades de soporte futuro.

La instalación y configuración del sistema informático requiere un conocimiento profundo del software y una comprensión clara de las necesidades organizacionales. Es recomendable contar con la asistencia de profesionales experimentados para garantizar que el proceso se realice correctamente y que el sistema funcione eficientemente desde el primer día.

En resumen, la instalación y configuración del sistema informático es un paso crucial en la implementación de sistemas ERP-CRM. Involucra la selección adecuada del software, su despliegue y ajuste a las necesidades organizacionales, así como un proceso continuo de mantenimiento y documentación para asegurar su funcionamiento óptimo.

<a id="verificacion-de-la-instalacion-y-configuracion"></a>
## Verificación de la instalación y configuración

La verificación de la instalación y configuración es un paso crucial que garantiza que el sistema ERP-CRM funcione correctamente una vez implementado. Este proceso implica comprobar que todos los componentes del sistema están correctamente instalados y configurados, lo que asegura su integridad y eficiencia operativa.

Para realizar esta verificación, se deben seguir varios pasos fundamentales. Primero, es necesario revisar la documentación proporcionada por el proveedor del ERP-CRM para entender los requisitos específicos de instalación y configuración. Esta documentación suele incluir instrucciones detalladas sobre cómo instalar el software en diferentes entornos (desarrollo, pruebas, producción), así como las configuraciones necesarias para que el sistema funcione correctamente.

Una vez completada la instalación, se debe realizar una serie de pruebas básicas para asegurar que todos los módulos del ERP-CRM están funcionando. Esto puede incluir la creación y gestión de usuarios, la realización de consultas básicas en las bases de datos, y la generación de informes simples. Estas pruebas ayudan a identificar cualquier problema o incompatibilidad que pueda haber surgido durante el proceso de instalación.

Además de las pruebas funcionales, es importante verificar que los permisos y roles estén correctamente configurados. Esto asegura que solo los usuarios autorizados puedan acceder a ciertas partes del sistema, lo que protege la información sensible y prevenir el acceso no autorizado.

La verificación también debe incluir la comprobación de las conexiones con otros sistemas o bases de datos que el ERP-CRM necesita para funcionar. Esto puede implicar la configuración de interfaces de comunicación, la creación de enlaces a bases de datos externas, y la realización de pruebas de integración.

Es crucial también revisar los logs del sistema para identificar cualquier error o advertencia durante el proceso de instalación y configuración. Los logs proporcionan una visión detallada de lo que sucedió en el sistema, lo que puede ser invaluable para diagnosticar problemas y solucionarlos rápidamente.

Además, se debe realizar una verificación de rendimiento inicial para asegurar que el ERP-CRM está funcionando eficientemente. Esto puede implicar la realización de pruebas de carga simuladas o la observación del uso de recursos del sistema (CPU, memoria, disco). Un buen rendimiento es fundamental para mantener un sistema ERP-CRM operativo y satisfactorio.

La verificación también debe incluir una revisión de seguridad para asegurar que el sistema está protegido contra amenazas potenciales. Esto puede implicar la configuración de firewalls, la realización de pruebas de penetración, y la revisión de políticas de acceso y control de usuarios.

Finalmente, es importante documentar todos los pasos realizados durante la verificación de instalación y configuración. Esta documentación debe incluir detalles sobre cualquier problema encontrado, las soluciones implementadas, y las acciones futuras recomendadas para mantener el sistema funcionando correctamente.

La verificación de la instalación y configuración es un proceso integral que asegura que el ERP-CRM esté listo para su uso en producción. Al seguir los pasos adecuados y realizar una revisión exhaustiva, se puede garantizar que el sistema funcione eficientemente y satisfactoriamente, proporcionando a la empresa las herramientas necesarias para mejorar su operación y tomar decisiones informadas.

### mapear xml

```python
from lxml import etree

tree = etree.parse('interfaz.xml')
root = tree.getroot()

print(root)
```

### parsear entero

```python
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('interfaz.xml')
root = tree.getroot()

# Print the root element
print("Root element:", root.tag)

# Iterate over each child element
for campo in root:
    print(f"Etiqueta: {campo.tag}, atributo nombre: {campo.get('nombre')}")
```

### mapeo

```python
import xml.etree.ElementTree as ET

def miInterfaz(destino):
  cadena = ""
  # Parse the XML file
  tree = ET.parse()
  root = tree.getroot(destino)

  # Print the root element
  print("Root element:", root.tag)

  # Iterate over each child element
  for campo in root:
      print(f"Etiqueta: {campo.tag}, atributo nombre: {campo.get('nombre')}")
      if campo.tag == "campotexto":
        cadena += "<input type='text' name='"+campo.get('nombre')+"'>"
      elif campo.tag == "areadetexto":
        cadena += "<textarea name='"+campo.get('nombre')+"'></textarea>"
  return cadena
      
```

### servidor que convierte

```python
from flask import Flask
from mifuncion import miInterfaz

app = Flask(__name__)

@app.route('/')
def home():
    return miInterfaz("interfaz.xml")

if __name__ == '__main__':
    app.run()
```

### servidor que recibe

```python
from flask import Flask, request
from mifuncion2 import miInterfaz, tablaInterfaz

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # GET -> muestra formulario, POST -> inserta datos
    return miInterfaz("interfaz.xml")

@app.route('/tabla')
def tabla():
    # Tabla con todos los registros guardados
    return tablaInterfaz("interfaz.xml")

if __name__ == '__main__':
    app.run(debug=True)
```

### interfaz

```xml
<?xml version="1.0" encoding="UTF-8"?>
<formulario>
  <campotexto nombre="nombre"></campotexto>
  <campotexto nombre="apellidos"></campotexto>
  <campotexto nombre="email"></campotexto>
  <campotexto nombre="direccion"></campotexto>
  <campotexto nombre="pais"></campotexto>
  <areadetexto nombre="mensaje"></areadetexto>
</formulario>
```

### mifuncion

```python
import xml.etree.ElementTree as ET
import sqlite3


def miInterfaz(destino):
  conexion = sqlite3.connect("odoo.db")
  cursor = conexion.cursor()
  cadena = ""
  peticion = '''
      CREATE TABLE IF NOT EXISTS "interfaz" (
	    "Identificador"	INTEGER,
	    '''
	
	    
  # Parse the XML file
  tree = ET.parse(destino)
  root = tree.getroot()

  # Print the root element
  print("Root element:", root.tag)

  # Iterate over each child element
  for campo in root:
    print(f"Etiqueta: {campo.tag}, atributo nombre: {campo.get('nombre')}")
    if campo.tag == "campotexto":
        cadena += "<input type='text' name='"+campo.get('nombre')+"' placeholder='"+campo.get('nombre')+"'>"
    elif campo.tag == "areadetexto":
      cadena += "<textarea name='"+campo.get('nombre')+"'></textarea>"
    peticion += '"'+campo.get('nombre')+'"	TEXT,'   
       
  peticion += '''
	    
	    PRIMARY KEY("Identificador" AUTOINCREMENT)
    );
    ''' 
  #print(peticion)
  cursor.execute(peticion)
  conexion.commit()
      
  return cadena
      
```

### mifuncion2

```python
import xml.etree.ElementTree as ET
import sqlite3
from flask import request

DB_NAME = "odoo.db"
TABLE_NAME = "interfaz"


def _get_fields_from_xml(root):
    """
    Devuelve lista de tuplas (tipo, nombre) en el orden del XML.
    Tipos esperados en este ejemplo: campotexto, areadetexto
    """
    fields = []
    for nodo in root:
        nombre = nodo.get("nombre")
        if not nombre:
            continue
        if nodo.tag in ("campotexto", "areadetexto"):
            fields.append((nodo.tag, nombre))
    return fields


def _ensure_table(root):
    """
    Crea la tabla 'interfaz' si no existe, con columnas a partir del XML.
    """
    fields = _get_fields_from_xml(root)

    cols_sql = []
    for _, nombre in fields:
        # Todas TEXT para simplicidad; se puede sofisticar por tipo
        cols_sql.append(f'"{nombre}" TEXT')

    create_sql = f'''
        CREATE TABLE IF NOT EXISTS "{TABLE_NAME}" (
            "Identificador" INTEGER PRIMARY KEY AUTOINCREMENT,
            {", ".join(cols_sql)}
        );
    '''

    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(create_sql)
        con.commit()


def miInterfaz(destino_xml: str):
    """
    - GET: renderiza formulario basado en XML.
    - POST: inserta datos recibidos y confirma guardado.
    """
    tree = ET.parse(destino_xml)
    root = tree.getroot()
    fields = _get_fields_from_xml(root)
    _ensure_table(root)

    if request.method == "POST":
        # Recoger datos en el orden del XML
        nombres = [nombre for _, nombre in fields]
        valores = [request.form.get(nombre, "") for nombre in nombres]

        placeholders = ", ".join(["?"] * len(nombres))
        columnas = ", ".join([f'"{n}"' for n in nombres])
        insert_sql = f'INSERT INTO "{TABLE_NAME}" ({columnas}) VALUES ({placeholders})'

        with sqlite3.connect(DB_NAME) as con:
            cur = con.cursor()
            cur.execute(insert_sql, valores)
            con.commit()

        return (
            "<!doctype html>"
            "<html><head><meta charset='utf-8'><title>Guardado</title>"
            "<style>body{font-family:system-ui;margin:2rem} a{display:inline-block;margin-top:1rem}</style>"
            "</head><body>"
            "<h1>✅ Datos guardados correctamente</h1>"
            "<p><a href='/'>Volver al formulario</a> | <a href='/tabla'>Ver tabla</a></p>"
            "</body></html>"
        )

    # GET → Render del formulario
    inputs_html = []
    for tipo, nombre in fields:
        label = f"<label for='{nombre}'>{nombre}</label>"
        if tipo == "campotexto":
            control = f"<input id='{nombre}' type='text' name='{nombre}' placeholder='{nombre}'>"
        elif tipo == "areadetexto":
            control = f"<textarea id='{nombre}' name='{nombre}' rows='5' placeholder='{nombre}'></textarea>"
        else:
            # Por si se añaden más tipos en el futuro
            control = f"<input id='{nombre}' type='text' name='{nombre}' placeholder='{nombre}'>"

        inputs_html.append(f"<div class='campo'>{label}{control}</div>")

    html = f"""
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Formulario</title>
        <style>
          :root {{ --gap: 12px; }}
          body {{ font-family: system-ui, sans-serif; margin: 2rem; }}
          form {{ max-width: 720px; display:grid; gap: var(--gap); }}
          .campo {{ display:flex; flex-direction:column; gap:6px; }}
          input, textarea {{
            padding: 10px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px;
          }}
          button {{
            padding: 10px 16px; border: 0; border-radius: 8px; font-size: 16px; cursor: pointer;
          }}
          .actions {{ display:flex; gap: var(--gap); }}
        </style>
      </head>
      <body>
        <h1>Formulario</h1>
        <form method="post" action="/">
          {"".join(inputs_html)}
          <div class="actions">
            <button type="submit">Enviar</button>
            <a href="/tabla">Ver tabla</a>
          </div>
        </form>
      </body>
    </html>
    """
    return html


def tablaInterfaz(destino_xml: str):
    """
    Renderiza una tabla HTML con todos los registros de la base de datos,
    usando las columnas definidas por el XML (mismo mapeo campos ⇄ columnas).
    """
    tree = ET.parse(destino_xml)
    root = tree.getroot()
    fields = _get_fields_from_xml(root)
    _ensure_table(root)

    headers = ["Identificador"] + [nombre for _, nombre in fields]

    # Query de todos los registros (ordenados por Identificador desc)
    select_cols = ", ".join([f'"{TABLE_NAME}"."Identificador"'] + [f'"{TABLE_NAME}"."{n}"' for _, n in fields])
    select_sql = f'SELECT {select_cols} FROM "{TABLE_NAME}" ORDER BY "Identificador" DESC'

    rows = []
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(select_sql)
        rows = cur.fetchall()

    # Construcción HTML de tabla
    thead = "".join([f"<th>{h}</th>" for h in headers])
    trs = []
    for row in rows:
        tds = "".join([f"<td>{(c if c is not None else '')}</td>" for c in row])
        trs.append(f"<tr>{tds}</tr>")

    html = f"""
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Tabla de registros</title>
        <style>
          body {{ font-family: system-ui, sans-serif; margin: 2rem; }}
          table {{ border-collapse: collapse; width: 100%; max-width: 1000px; }}
          th, td {{ border: 1px solid #ddd; padding: 8px; }}
          th {{ background: #f5f5f5; text-align: left; }}
          caption {{ text-align:left; font-weight:600; margin-bottom: .5rem; }}
          .actions a {{ display:inline-block; margin-right: .75rem; }}
        </style>
      </head>
      <body>
        <h1>Registros</h1>
        <div class="actions">
          <a href="/">← Volver al formulario</a>
        </div>
        <table>
          <caption>Total: {len(rows)} registro(s)</caption>
          <thead><tr>{thead}</tr></thead>
          <tbody>
            {"".join(trs) if trs else "<tr><td colspan='{len(headers)}'>Sin datos</td></tr>"}
          </tbody>
        </table>
      </body>
    </html>
    """
    return html
```

### servidor

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hola mundo desde Flask</h1>"

if __name__ == '__main__':
    app.run()
```

<a id="documentacion-de-las-operaciones-realizadas"></a>
## Documentación de las operaciones realizadas

La documentación es un componente crucial en cualquier proyecto de desarrollo, especialmente cuando se trata de sistemas complejos como los ERP-CRM (Enterprise Resource Planning - Planificación de Recursos Empresariales y Customer Relationship Management - Gestión Relacional de Clientes). Esta subunidad se centra específicamente en la documentación de las operaciones realizadas durante el proceso de instalación, configuración y posterior uso del sistema ERP-CRM.

La documentación de las operaciones realizadas es una práctica que permite a los usuarios entender completamente cómo funciona el sistema, identificar cualquier problema o anomalía que pueda surgir y facilitar la actualización y mantenimiento del software. Esta documentación debe abordar varios aspectos importantes: desde la instalación inicial hasta la configuración de módulos específicos, pasando por la creación de formularios personalizados y el desarrollo de informes.

Durante la fase de instalación, es fundamental registrar todos los pasos realizados, incluyendo la selección del sistema ERP-CRM, la configuración del entorno de ejecución, la instalación de dependencias necesarias y cualquier ajuste adicional que se realice. Esta documentación ayudará a prevenir problemas futuros y facilitará el soporte técnico en caso de necesidad.

La configuración del sistema es otro aspecto crucial que debe ser documentado detalladamente. Esto incluye la selección de módulos, la personalización de parámetros de configuración, la creación de tablas y vistas adaptadas a las necesidades específicas de la empresa, y la definición de consultas necesarias para obtener información relevante. Documentar estos procesos permite a los usuarios entender cómo el sistema está estructurado y cómo interactuar con él.

Además, la documentación debe abordar el desarrollo de componentes personalizados, como formularios e informes. Es importante registrar todos los cambios realizados en estos elementos, incluyendo las modificaciones en el código fuente, las pruebas realizadas y cualquier problema encontrado durante este proceso. Esta documentación es esencial para garantizar la integridad del sistema y facilitar futuras actualizaciones.

La creación de paneles de control (dashboards) también debe ser documentada, incluyendo los pasos realizados para configurar las gráficos y listas que se mostrarán en el panel. Esta documentación ayudará a los usuarios entender cómo interpretar la información presentada en el dashboard y cómo realizar ajustes si es necesario.

La integración del sistema ERP-CRM con otros sistemas de gestión es otro aspecto importante que debe ser documentado. Esto incluye la configuración de interfaces de entrada de datos, la creación de formularios personalizados para sincronizar información entre sistemas, y la definición de procesos de extracción de datos. Documentar estos procesos facilitará el mantenimiento del sistema y permitirá a los usuarios entender cómo el sistema interactúa con otros sistemas.

La documentación también debe abordar la inteligencia de negocio (Business Intelligence), incluyendo la creación de informes personalizados, paneles de control y gráficos que ayuden a analizar datos y tomar decisiones estratégicas. Es importante registrar todos los pasos realizados en este proceso, incluyendo las consultas SQL utilizadas y cualquier problema encontrado durante el análisis.

En resumen, la documentación de las operaciones realizadas es un componente fundamental del desarrollo y mantenimiento de sistemas ERP-CRM. Al detallar cada paso del proceso, desde la instalación inicial hasta la creación de componentes personalizados y la inteligencia de negocio, se facilita la comprensión del sistema, el diagnóstico de problemas y la actualización del software. Esta documentación es esencial para garantizar la integridad del sistema y facilitar su uso por parte de los usuarios finales.

<a id="ejercicio-de-final-de-unidad"></a>
## Ejercicio de final de unidad

### ejercicio

```markdown

```


<a id="instalacion-y-configuracion-de-sistemas-erp-crm"></a>
# Instalación y configuración de sistemas ERP-CRM

<a id="tipos-de-instalacion"></a>
## Tipos de instalación.

En la instalación y configuración de sistemas ERP-CRM, los primeros pasos son fundamentales para asegurar que el software funcione correctamente y satisfaga las necesidades específicas de la empresa. Existen varios tipos de instalaciones que dependen del tamaño, la complejidad y las preferencias de cada organización.

La primera opción es la instalación local, donde el sistema ERP-CRM se instala en los servidores internos de la empresa. Esta solución ofrece un alto nivel de control y seguridad, ya que todos los datos permanecen dentro del entorno corporativo. Sin embargo, requiere una mayor inversión inicial y administración técnica.

La segunda opción es la instalación en la nube, también conocida como SaaS (Software as a Service). En este caso, el proveedor de ERP-CRM gestiona todo el hardware, software y mantenimiento, lo que permite a las empresas centrarse en sus operaciones principales. Aunque puede ser más costoso a largo plazo, ofrece la ventaja de escalabilidad y accesibilidad desde cualquier lugar.

La tercera opción es la instalación híbrida, que combina elementos de la instalación local y en la nube. Esta configuración permite una mayor flexibilidad, ya que los datos críticos pueden almacenarse en el entorno corporativo mientras que otros tipos de información se almacenan en la nube.

La elección del tipo de instalación depende de varios factores, como la infraestructura existente, las necesidades de seguridad, los presupuestos y los objetivos estratégicos de la empresa. Es crucial realizar una evaluación detallada para determinar cuál es la opción más adecuada.

Una vez elegido el tipo de instalación, se procede a la configuración del sistema ERP-CRM. Esto implica la definición de parámetros como las monedas, los idiomas, los formatos de fecha y hora, entre otros. Además, se configuran los módulos que serán utilizados según las necesidades específicas de la empresa.

Es importante destacar que la configuración del sistema ERP-CRM no es una tarea rápida ni sencilla. Requiere un conocimiento profundo del software y una comprensión clara de los procesos empresariales. Es recomendable contar con el apoyo de profesionales experimentados para asegurar una instalación correcta.

Durante la configuración, se deben definir campos personalizados según las necesidades específicas de la empresa. Esto puede incluir campos adicionales en formularios y tablas para almacenar información relevante que no esté contemplada por el software por defecto.

Además, es crucial realizar pruebas exhaustivas después de la instalación y configuración para verificar que todo funciona correctamente. Se deben probar los procesos clave del ERP-CRM, como la creación de pedidos, la gestión de inventario o la generación de informes financieros.

La documentación de las operaciones realizadas durante la instalación y configuración es otro aspecto importante. Esta documentación debe incluir detalles sobre el tipo de instalación elegido, los parámetros de configuración, los módulos activados y cualquier ajuste personalizado realizado. La documentación facilitará futuras actualizaciones o cambios en el sistema.

En resumen, la instalación y configuración de sistemas ERP-CRM requiere una planificación cuidadosa y una ejecución meticulosa. Al elegir el tipo de instalación adecuado y seguir un proceso de configuración riguroso, se puede asegurar que el software funcione eficientemente y satisfaga las necesidades empresariales.

<a id="modulos-de-un-sistema-erp-crm"></a>
## Módulos de un sistema ERP-CRM

En la instalación y configuración de sistemas ERP-CRM, los módulos desempeñan un papel crucial ya que representan las funcionalidades específicas que el sistema ofrecerá a la organización. Cada módulo es una unidad independiente del software que puede ser activado o desactivado según las necesidades particulares de la empresa. Por ejemplo, si la empresa opera en el sector retail, los módulos de gestión de inventario y ventas podrían ser fundamentales para su operación diaria.

Los módulos de un sistema ERP-CRM pueden variar ampliamente dependiendo del proveedor y del tipo específico de software que se esté utilizando. Algunos ejemplos comunes incluyen el módulo de gestión financiera, que maneja las cuentas por cobrar y por pagar; el módulo de recursos humanos, que administra contratos laborales y beneficios; y el módulo de marketing digital, que gestiona campañas publicitarias y relaciones con clientes.

La configuración de los módulos es un proceso integral en la instalación del sistema ERP-CRM. Durante este paso, se deben definir las opciones específicas para cada módulo según las preferencias de la empresa. Por ejemplo, en el módulo de recursos humanos, se puede configurar cómo se manejarán los contratos laborales, qué tipos de beneficios estarán disponibles y cómo se calculará el salario neto.

Además de la configuración básica, es importante considerar la integración entre los diferentes módulos del sistema ERP-CRM. La coherencia en los datos y las operaciones entre estos módulos es crucial para evitar inconsistencias y errores en la información empresarial. Por ejemplo, si el módulo de ventas se integra correctamente con el módulo de inventario, cuando se realiza una venta, automáticamente se actualizará el stock disponible.

La configuración también puede incluir la personalización de interfaces de usuario y formularios para que sean más intuitivos y adecuados a las necesidades específicas de la empresa. Esto puede implicar la creación de formularios personalizados o la modificación de los campos existentes para reflejar mejor los procesos internos de la organización.

Además, es importante establecer políticas de seguridad y acceso a los módulos del sistema ERP-CRM. Los roles y privilegios deben ser definidos de manera que solo los usuarios autorizados puedan acceder a las funciones específicas necesarias para su trabajo. Esto ayuda a proteger la integridad y confidencialidad de la información empresarial.

La configuración de los módulos también puede implicar la definición de procesos de negocio personalizados. Por ejemplo, si la empresa tiene un proceso único para gestionar las solicitudes de presupuesto, este proceso debe ser integrado en el sistema ERP-CRM y configurado de manera que se pueda seguir automáticamente.

La documentación de los módulos es otro aspecto importante a considerar durante la instalación y configuración del sistema ERP-CRM. Es crucial mantener un registro detallado de todas las configuraciones realizadas, las opciones seleccionadas y cualquier personalización aplicada. Esta documentación será invaluable para el mantenimiento futuro del sistema y para la formación de nuevos usuarios.

En resumen, los módulos desempeñan un papel central en la instalación y configuración de sistemas ERP-CRM, proporcionando las funcionalidades específicas necesarias para la operación empresarial. La configuración adecuada de estos módulos es crucial para asegurar la integridad, coherencia y eficiencia del sistema, así como para facilitar el trabajo diario de los usuarios.

### Listado de pantallas a desarrollar

```markdown
# Pantallas a desarrollar

Listado de modulos - Grid de tarjetas

Ventas	Odoo S.A.	https://www.odoo.com/app/sales	18.0.1.0	
Restaurante	Odoo S.A.	https://www.odoo.com/app/point-of-sale-restaurant	18.0.1.0	
Facturación / Contabilidad	Odoo S.A.	https://www.odoo.com/app/invoicing	18.0.1.3	
CRM	Odoo S.A.	https://www.odoo.com/app/crm	18.0.1.8	
MRP II	Odoo S.A.	https://www.odoo.com/page/manufacturing?utm_source=db&utm_medium=module	18.0.1.0	
Sitio web	Odoo S.A.	https://www.odoo.com/app/website	18.0.1.0	
Inventario	Odoo S.A.	https://www.odoo.com/app/inventory	18.0.1.1	
Contabilidad	Odoo S.A.	https://www.odoo.com/app/accounting?utm_source=db&utm_medium=module	18.0.1.0	
Información	Odoo S.A.	https://www.odoo.com/app/knowledge?utm_source=db&utm_medium=module	18.0.1.0	
Compra	Odoo S.A.	https://www.odoo.com/app/purchase	18.0.1.2	
Punto de venta	Odoo S.A.	https://www.odoo.com/app/point-of-sale-shop	18.0.1.0.2	
Proyecto	Odoo S.A.	https://www.odoo.com/app/project	18.0.1.3	
Comercio electrónico	Odoo S.A.	https://www.odoo.com/app/ecommerce	18.0.1.1	
Fabricación	Odoo S.A.	https://www.odoo.com/app/manufacturing	18.0.2.0	
Marketing por correo electrónico	Odoo S.A.	https://www.odoo.com/app/email-marketing	18.0.2.7	
Partes de horas	Odoo S.A.	https://www.odoo.com/app/timesheet?utm_source=db&utm_medium=module	18.0.1.0	
Gastos	Odoo S.A.	https://www.odoo.com/app/expenses	18.0.2.0	
Studio	Odoo S.A.	https://odoo.com/app/studio?utm_source=db&utm_medium=module	18.0.1.0	
Ausencias	Odoo S.A.	https://www.odoo.com/app/time-off	18.0.1.6	
Reclutamiento	Odoo S.A.	https://www.odoo.com/app/recruitment	18.0.1.1	
Servicio de campo	Odoo S.A.	https://www.odoo.com/app/field-service?utm_source=db&utm_medium=module	18.0.1.0	
Empleados	Odoo S.A.	https://www.odoo.com/app/employees	18.0.1.1	
Reciclaje de datos	Odoo S.A.		18.0.1.3	
Mantenimiento	Odoo S.A.	https://www.odoo.com/app/maintenance	18.0.1.0	
Tarjeta de marketing	Odoo S.A.		18.0.1.1	
Firma electrónica	Odoo S.A.	https://www.odoo.com/app/sign?utm_source=db&utm_medium=module	18.0.1.0	
Servicio de asistencia	Odoo S.A.	https://www.odoo.com/app/helpdesk?utm_source=db&utm_medium=module	18.0.1.0	
Suscripciones	Odoo S.A.	https://www.odoo.com/app/subscriptions?utm_source=db&utm_medium=module	18.0.1.0	
Calidad	Odoo S.A.	https://www.odoo.com/app/quality?utm_source=db&utm_medium=module	18.0.1.0	
eLearning	Odoo S.A.	https://www.odoo.com/app/elearning	18.0.2.7	
Planificación	Odoo S.A.	https://www.odoo.com/app/planning?utm_source=db&utm_medium=module	18.0.1.0	
Eventos	Odoo S.A.	https://www.odoo.com/app/events	18.0.1.4	
Conversaciones	Odoo S.A.	https://www.odoo.com/app/discuss	18.0.1.18	
Contactos	Odoo S.A.		18.0.1.0	
Gestión del ciclo de vida del producto (PLM)	Odoo S.A.	https://www.odoo.com/app/plm?utm_source=db&utm_medium=module	18.0.1.0	
Calendario	Odoo S.A.		18.0.1.1	
Marketing social	Odoo S.A.	https://www.odoo.com/app/social-marketing	18.0.1.0	
Evaluación	Odoo S.A.	https://www.odoo.com/app/appraisals?utm_source=db&utm_medium=module	18.0.1.0	
Flota	Odoo S.A.	https://www.odoo.com/app/fleet	18.0.0.1	
Automatización de marketing	Odoo S.A.	https://www.odoo.com/app/marketing-automation?utm_source=db&utm_medium=module	18.0.1.0	
Chat en directo	Odoo S.A.	https://www.odoo.com/app/live-chat	18.0.1.0	
Citas	Odoo S.A.	https://www.odoo.com/app/appointments?utm_source=db&utm_medium=module	18.0.1.0	
Encuestas	Odoo S.A.	https://www.odoo.com/app/surveys	18.0.3.7	
Móvil	Odoo S.A.	https://play.google.com/store/apps/details?id=com.odoo.mobile	18.0.1.0	
Reparaciones	Odoo S.A.		18.0.1.0	
Asistencias	Odoo S.A.	https://www.odoo.com/app/employees	18.0.2.0	
Marketing por SMS	Odoo S.A.	https://www.odoo.com/app/sms-marketing	18.0.1.1	
Código de barras	Odoo S.A.	https://www.odoo.com/app/inventory?utm_source=db&utm_medium=module	18.0.1.0	
Actividades pendientes	Odoo S.A.		18.0.1.0	
Administración de habilidades	Odoo S.A.		18.0.1.0	
VoIP	Odoo S.A.	https://www.odoo.com/app/crm?utm_source=db&utm_medium=module	18.0.1.0	
Comida	Odoo S.A.		18.0.1.0	
Trabajos en línea	Odoo S.A.		18.0.1.1	
Conector de Amazon	Odoo S.A.	https://www.odoo.com/app/amazon-connector?utm_source=db&utm_medium=module	18.0.1.0	
Contratos de los empleados	Odoo S.A.	https://www.odoo.com/app/employees

Vistas:
- Vista de kanban
Pasando tarjetas de una columna a otra
Vista de clientes: grid de tarjetas
Vista de detalles de cliente - pantalla partida con formulario y correo
Vista de empleados - vista de tarjetas
Vista de calendario - mensual, anual, semanal, diario
Vista de diseño de formularios - para encuestas etc
Vista de ajustes tipo panel de control de wordpress
Vista de tablero
Vista de factura a dos columnas
Vista previa de la factura
Vista del terminal de punto de venta
```

<a id="procesos-de-instalacion-del-sistema-erp-crm"></a>
## Procesos de instalación del sistema ERP-CRM

La instalación y configuración del sistema ERP-CRM es un proceso integral que requiere una planificación cuidadosa y atención a los detalles para asegurar su correcto funcionamiento. El primer paso consiste en la selección de los módulos adecuados, considerando las necesidades específicas de la empresa. Una vez seleccionados los módulos, se procede a la instalación del sistema ERP-CRM, que puede realizarse a través de diferentes métodos como instalaciones locales o despliegues en la nube.

Durante el proceso de instalación, es crucial configurar adecuadamente parámetros cruciales como la base de datos, los usuarios y roles, y las preferencias generales del sistema. Es importante realizar pruebas exhaustivas para verificar que todos los módulos se han instalado correctamente y que no hay errores o inconvenientes.

La configuración del sistema ERP-CRM implica también la personalización de formularios y informes según las necesidades específicas de la empresa. Esto puede implicar la creación de nuevas vistas, el ajuste de campos existentes y la definición de consultas personalizadas para facilitar el acceso a la información.

Además, es fundamental establecer los servicios de acceso al sistema ERP-CRM, lo que incluye la configuración de servidores web, bases de datos y interfaces de usuario. La seguridad del sistema debe ser una prioridad durante este proceso, implementando medidas como autenticación de usuarios, encriptación de datos y políticas de acceso controlado.

El entorno de desarrollo, pruebas y explotación es otro aspecto crucial a considerar durante la instalación y configuración del sistema ERP-CRM. Es necesario definir los diferentes entornos donde se realizarán las pruebas y el despliegue final del sistema, asegurando que cada uno tenga las configuraciones adecuadas para su uso.

La documentación de las operaciones realizadas durante la instalación y configuración es otro elemento importante. Esta documentación debe incluir detalles sobre los pasos seguidos, cualquier problema encontrado y cómo se solucionó, así como una guía paso a paso para futuras referencias o actualizaciones del sistema.

En resumen, el proceso de instalación y configuración del sistema ERP-CRM es un trabajo meticuloso que requiere una planificación cuidadosa y atención a los detalles. Desde la selección de módulos hasta la documentación final, cada paso debe ser ejecutado con precisión para asegurar el correcto funcionamiento del sistema en el entorno empresarial.

### Instalación de una máquina virtual

```markdown
sudo apt update

sudo apt upgrade -y

Odoo funciona con stack
Python3 
PostgreSQL para la base de datos

sudo apt install -y postgresql

sudo apt install openssh-server

sudo apt install net-tools

ifconfig
```

### Repositorio de Odoo

```markdown
wget -q -O https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg

echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/18.0/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list

sudo apt update

sudo apt install odoo
```

### dependencias

```markdown
wkhtmltopdf

wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6-1.bionic_amd64.deb
sudo apt install -f

wkhtmltopdf --version
wkhtmltoimage --version

sudo apt install wkhtmltopdf
```

### iniciar servicios

```markdown
sudo systemctl enable odoo
sudo systemctl start odoo
sudo systemctl status odoo

# Arreglo de librerias

sudo apt install python3-pip -y
sudo pip install lxml[html_clean] --break-system-packages

Arrancamos manualmente

dpkg -l | grep -i odoo
apt policy odoo
ls -l /etc/init.d/odoo || true
command -v odoo || ls -l /usr/bin/odoo* /usr/local/bin/odoo* 2>/dev/null || true
```

### reparacion

```markdown
sudo apt purge -y odoo-16
sudo rm -f /etc/init.d/odoo
sudo systemctl daemon-reload
```

### preparamos base de datos

```markdown
sudo apt update
sudo apt install -y postgresql
sudo systemctl enable --now postgresql
sudo -u postgres createuser -s odoo || true
```

### odoo 18

```markdown
wget -q -O - https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg
echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/18.0/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list

sudo apt update
sudo apt install -y odoo

sudo service odoo restart
sudo service odoo status
```

### acceso y configuracion

```markdown
http://[ip]:8069/web/database/selector

Instalación

usuario: info@jocarsa.com

Contraseña y contraseña maestra:
DAM123$
```

### entrar en debug

```markdown
http://192.168.1.151:8069/odoo/apps?debug=1

josevicente@josevicente-VirtualBox:~$ pip3 install phonenumbers --break-system-packages

sudo systemctl restart odoo

sudo apt update
sudo apt install python3-phonenumbers
sudo systemctl restart odoo
```

### modulo de odoo

```markdown
cd /usr/lib/python3/dist-packages/odoo/addons/

ls -l


total 52
drwxr-xr-x 3 root root 4096 oct 17 16:48 controllers
drwxr-xr-x 2 root root 4096 oct 17 16:48 data
drwxr-xr-x 2 root root 4096 oct 17 16:48 i18n
-rw-r--r-- 1 root root  189 dic 15  2020 __init__.py
-rw-r--r-- 1 root root 2955 dic 15  2020 __manifest__.py
drwxr-xr-x 3 root root 4096 oct 17 16:48 models
drwxr-xr-x 2 root root 4096 oct 17 16:48 __pycache__
drwxr-xr-x 3 root root 4096 oct 17 16:48 report
drwxr-xr-x 2 root root 4096 oct 17 16:48 security
drwxr-xr-x 8 root root 4096 oct 17 16:47 static
drwxr-xr-x 3 root root 4096 oct 17 16:48 tests
drwxr-xr-x 2 root root 4096 oct 17 16:48 views
drwxr-xr-x 3 root root 4096 oct 17 16:48 wizard
```

### modulo personalizado

```markdown
cd /opt/odoo/custom-addons/

Si no existe:

cd /opt/
sudo mkdir odoo
cd odoo
sudo mkdir custom-addons


sudo mkdir el_modulo_de_jose_vicente

sudo mkdir -p /opt/odoo/custom-addons/mi_modulo_ejemplo
cd /opt/odoo/custom-addons/mi_modulo_ejemplo
```

### archivo de configuracion de odoo

```markdown
sudo nano /etc/odoo/odoo.conf

addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom-addons

Control+O = Guardar
Control+X = Salir

Reiniciamos odoo
sudo systemctl restart odoo
systemctl daemon-reload

Actualizar aplicaciones (boton en la barra superior)
```

### añadir modelo

```markdown
sudo nano /opt/odoo/custom-addons/mi_modulo_ejemplo/security/ir.model.access.csv


id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_nota_public,access_nota_public,model_mi_modulo_ejemplo_nota,base.group_user,1,1,1,1

Actualizamos desde consola

sudo -u odoo /usr/bin/odoo -d odoo --update=mi_modulo_ejemplo --stop-after-init

Reiniciamos odoo
sudo systemctl restart odoo || sudo service odoo restart

sudo -u odoo /usr/bin/odoo -d odoo --update=mi_modulo_ejemplo --stop-after-init
```

### estructura de un modulo

```markdown


## 🧱 1. Estructura básica del módulo

Por convención, los módulos se guardan en una carpeta personalizada, normalmente en:

```
/usr/lib/python3/dist-packages/odoo/addons/
```

o si prefieres mantenerlos aparte:

```
/opt/odoo/custom-addons/
```

Creemos ese directorio y nuestro módulo:

```bash
sudo mkdir -p /opt/odoo/custom-addons/mi_modulo_ejemplo
cd /opt/odoo/custom-addons/mi_modulo_ejemplo
```

---

## 📁 2. Estructura mínima de archivos

Crea esta jerarquía:

```
mi_modulo_ejemplo/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── ejemplo.py
└── views/
    └── ejemplo_views.xml
```

Crea los archivos así:

---

### **`__manifest__.py`**

Describe el módulo (nombre, versión, dependencias, etc.):

```python
{
    'name': 'Módulo de Ejemplo',
    'version': '1.0',
    'summary': 'Un módulo básico de ejemplo para Odoo 18 Community',
    'author': 'Jose Vicente Carratala',
    'category': 'Tutorial',
    'depends': ['base'],
    'data': [
        'views/ejemplo_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
```

---

### **`__init__.py`**

Importa los modelos:

```python
from . import models
```

---

### **`models/__init__.py`**

```python
from . import ejemplo
```

---

### **`models/ejemplo.py`**

Aquí definimos un modelo simple, por ejemplo una tabla de “Notas personales”:

```python
from odoo import models, fields

class NotaEjemplo(models.Model):
    _name = 'mi_modulo_ejemplo.nota'
    _description = 'Nota de Ejemplo'

    name = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha')
```

Esto creará una nueva tabla SQL llamada `mi_modulo_ejemplo_nota`.

---

### **`views/ejemplo_views.xml`**

Diseñamos la vista (interfaz en Odoo):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <record id="view_nota_form" model="ir.ui.view">
        <field name="name">nota.form</field>
        <field name="model">mi_modulo_ejemplo.nota</field>
        <field name="arch" type="xml">
            <form string="Nota de Ejemplo">
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="descripcion"/>
                        <field name="fecha"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="view_nota_tree" model="ir.ui.view">
        <field name="name">nota.tree</field>
        <field name="model">mi_modulo_ejemplo.nota</field>
        <field name="arch" type="xml">
            <tree string="Notas de Ejemplo">
                <field name="name"/>
                <field name="fecha"/>
            </tree>
        </field>
    </record>

    <menuitem id="menu_mi_modulo_root" name="Notas de Ejemplo"/>

    <menuitem id="menu_mi_modulo_notas"
              name="Notas"
              parent="menu_mi_modulo_root"
              action="action_nota"/>

    <record id="action_nota" model="ir.actions.act_window">
        <field name="name">Notas de Ejemplo</field>
        <field name="res_model">mi_modulo_ejemplo.nota</field>
        <field name="view_mode">tree,form</field>
    </record>
</odoo>
```

---

## ⚙️ 3. Añadir el módulo al `addons_path`

Abre tu archivo de configuración de Odoo (normalmente `/etc/odoo/odoo.conf`) y añade tu ruta personalizada:

```ini
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom-addons
```

Guarda y reinicia el servicio:

```bash
sudo systemctl restart odoo
```

---

## 🧩 4. Activar el modo desarrollador y cargar el módulo

1. Entra en Odoo:
   👉 `http://localhost:8069`
2. Crea o entra en una base de datos.
3. Ve a **Configuración → Activar Modo Desarrollador**.

-Entrar en modo desarrollo: http://localhost:8069?debug=1

4. Entra en **Aplicaciones**, pulsa “Actualizar lista de aplicaciones”.
5. Busca **“Módulo de Ejemplo”** y haz clic en **Instalar**.

---

## ✅ 5. Probar

Tras instalarlo, en el menú superior aparecerá una nueva entrada **“Notas de Ejemplo”**, donde podrás crear, editar y listar tus registros.
```

<a id="parametros-de-configuracion-del-sistema-erp-crm"></a>
## Parámetros de configuración del sistema ERP-CRM

En este capítulo, nos adentramos en la configuración detallada de los sistemas ERP-CRM, una tarea esencial para asegurar su correcto funcionamiento y adaptación a las necesidades específicas de cada organización. La configuración inicial implica la definición de parámetros que controlan el comportamiento del sistema, desde aspectos técnicos hasta funcionalidades empresariales.

El primer paso en la configuración de un ERP-CRM es identificar los módulos y características que serán activados o desactivados según las necesidades de la empresa. Cada módulo tiene sus propias opciones de configuración, como el formato de documentos, los tipos de informes disponibles o las políticas de acceso a ciertas funciones.

Una vez seleccionados los módulos, se procede a la configuración técnica del sistema. Esto incluye ajustes en la base de datos, como la definición de tablas adicionales para almacenar información específica de la empresa, o la personalización de vistas y pantallas para facilitar el acceso a la información relevante.

Además de los parámetros técnicos, es crucial configurar las políticas de seguridad del sistema. Esto implica establecer roles y permisos que determinan quién puede acceder a qué partes del ERP-CRM y qué acciones pueden realizar. La configuración adecuada de estos roles asegura la protección tanto de la información sensible como de los procesos empresariales.

La configuración también debe incluir la definición de parámetros funcionales específicos para cada módulo, como las políticas de facturación en el ERP o las estrategias de marketing en el CRM. Estas configuraciones permiten al sistema adaptarse a las prácticas y procesos internos de la empresa.

Es importante también considerar la integración del ERP-CRM con otros sistemas de gestión empresarial, como sistemas financieros o sistemas de recursos humanos. La configuración adecuada de estas integrações asegura una transmisión fluida de información y un flujo eficiente de trabajo entre diferentes departamentos.

Además, la configuración del sistema debe incluir la definición de parámetros para el manejo de datos, como la codificación de productos o los códigos de cliente. Estos parámetros aseguran que la información se almacene y procese de manera consistente y precisa.

La configuración final del ERP-CRM implica la personalización de formularios y informes para facilitar el acceso a la información relevante y mejorar la eficiencia operativa. Esto puede incluir la creación de formularios personalizados para capturar datos específicos o la definición de informes que proporcionen una visión detallada del desempeño empresarial.

La configuración del sistema ERP-CRM es un proceso integral que requiere una comprensión profunda de las necesidades y procesos internos de la empresa. A través de la configuración adecuada, se puede asegurar que el sistema ERP-CRM no solo funcione correctamente, sino que también contribuya significativamente a mejorar la eficiencia operativa y la toma de decisiones estratégicas.

La configuración del sistema ERP-CRM es un paso crucial en su implantación exitosa. Al seguir los pasos descritos en este capítulo, puede asegurarse de que el sistema esté correctamente configurado para satisfacer las necesidades específicas de su empresa y contribuir al éxito empresarial.

### Introduccion

```markdown
Lenguaje visual
  Disparadores de eventos
  Control del flujo de la ejecución
  Acciones
  Acceso a mi maquina
  Consumo de API's (lectura y escritura)
  
API - consumo de datos, Gmail, Drive, Office, etc
Conexión con bloques de inteligencia artificial
```

### escritorio

```html
<!doctype html>
<html lang="es">
  <head>
    <title></title>
    <meta charset="utf8">
  </head>
  <body>
    <div id="izquierda">
    </div>
    <div id="centro">
    </div>
    <div id="derecha">
    </div>
  </body>
</html>
```

### un poco de css

```html
<!doctype html>
<html lang="es">
  <head>
    <title></title>
    <meta charset="utf8">
    <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      #izquierda,#derecha{flex:1;}
      #centro{flex:6;border-left:1px solid grey;border-right:1px solid grey;background:url(rejilla.jpg);}
    </style>
  </head>
  <body>
    <div id="izquierda">
    </div>
    <div id="centro">
    </div>
    <div id="derecha">
    </div>
  </body>
</html>
```

### ajustes visuales

```html
<!doctype html>
<html lang="es">
  <head>
    <title></title>
    <meta charset="utf8">
    <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      #izquierda,#derecha{flex:1;}
      #centro{flex:6;box-shadow:0px 0px 20px rgba(0,0,0,0.3) inset;background:url(rejilla.jpg);}
    </style>
  </head>
  <body>
    <div id="izquierda">
    </div>
    <div id="centro">
    </div>
    <div id="derecha">
    </div>
  </body>
</html>
```

### nodo

```html
<!doctype html>
<html lang="es">
  <head>
    <title></title>
    <meta charset="utf8">
    <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      #izquierda,#derecha{flex:1;}
      #centro{flex:6;box-shadow:0px 0px 20px rgba(0,0,0,0.3) inset;background:url(rejilla.jpg);}
      article{border:1px solid grey;width:100px;height:100px;border-radius:10px;background:white;box-shadow:0px 4px 10px rgba(0,0,0,0.3);}
    </style>
  </head>
  <body>
    <div id="izquierda">
    </div>
    <div id="centro">
      <article>
      </article>
    </div>
    <div id="derecha">
    </div>
  </body>
</html>
```

### draggable

```html
<!doctype html>
<html lang="es">
  <head>
    <title></title>
    <meta charset="utf8">
    <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
    <style>
      body{display:flex;}
      #izquierda,#derecha{flex:1;}
      #centro{flex:6;box-shadow:0px 0px 20px rgba(0,0,0,0.3) inset;background:url(rejilla.jpg);}
      article{border:1px solid grey;width:100px;height:100px;border-radius:10px;background:white;box-shadow:0px 4px 10px rgba(0,0,0,0.3);}
    </style>
  </head>
  <body>
    <div id="izquierda">
    </div>
    <div id="centro">
      <article draggable="true">
      </article>
    </div>
    <div id="derecha">
    </div>
    <script>
      const art = document.querySelector("article");
      let offsetX, offsetY;

      art.addEventListener("dragstart", e=>{
        offsetX = e.offsetX;
        offsetY = e.offsetY;
      });

      document.getElementById("centro").addEventListener("dragover", e=>{
        e.preventDefault();
        art.style.left = (e.offsetX - offsetX) + "px";
        art.style.top = (e.offsetY - offsetY) + "px";
      });
    </script>
  </body>
</html>
```

### drag js

```html
<!doctype html>
<html lang="es">
<head>
  <title></title>
  <meta charset="utf8">
  <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
  <style>
    body{display:flex;}
    #izquierda,#derecha{flex:1;}
    #centro{flex:6;position:relative;box-shadow:0 0 20px rgba(0,0,0,0.3) inset;background:url(rejilla.jpg);}
    article{border:1px solid grey;width:100px;height:100px;border-radius:10px;background:white;
      box-shadow:0 4px 10px rgba(0,0,0,0.3);position:absolute;cursor:move;}
  </style>
</head>
<body>
  <div id="izquierda"></div>
  <div id="centro">
    <article></article>
  </div>
  <div id="derecha"></div>

  <script>
    const art = document.querySelector("article");
    let offsetX, offsetY;

    art.addEventListener("dragstart", e=>{
      offsetX = e.offsetX;
      offsetY = e.offsetY;
    });

    document.getElementById("centro").addEventListener("dragover", e=>{
      e.preventDefault();
      art.style.left = (e.offsetX - offsetX) + "px";
      art.style.top = (e.offsetY - offsetY) + "px";
    });
  </script>
</body>
</html>
```

### boton de añadir

```html
<!doctype html>
<html lang="es">
<head>
  <title></title>
  <meta charset="utf8">
  <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
  <style>
    body{display:flex;}
    #izquierda,#derecha{flex:1;}
    #centro{flex:6;position:relative;box-shadow:0 0 20px rgba(0,0,0,0.3) inset;background:url(rejilla.jpg);}
    article{border:1px solid grey;width:100px;height:100px;border-radius:10px;background:white;
      box-shadow:0 4px 10px rgba(0,0,0,0.3);position:absolute;cursor:move;}
  </style>
</head>
<body>
  <div id="izquierda"></div>
  <div id="centro">
    
  </div>
  <div id="derecha">
    <button id="anyadir">+</button>
  </div>

  <script>
    class Nodo(){
      constructor(x,y){
        this.x = x
        this.y = y
      }
    }
    const art = document.querySelector("article");
    let offsetX, offsetY;

    art.addEventListener("dragstart", e=>{
      offsetX = e.offsetX;
      offsetY = e.offsetY;
    });

    document.getElementById("centro").addEventListener("dragover", e=>{
      e.preventDefault();
      art.style.left = (e.offsetX - offsetX) + "px";
      art.style.top = (e.offsetY - offsetY) + "px";
    });
  </script>
</body>
</html>
```

### nodos como elementos

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Nodos drag & drop</title>
  <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
  <style>
    body{display:flex;min-height:100vh;gap:10px;padding:10px;box-sizing:border-box;}
    #izquierda,#derecha{flex:1;display:flex;align-items:flex-start;justify-content:center;}
    #centro{flex:6;position:relative;box-shadow:0 0 20px rgba(0,0,0,0.3) inset;background:url(rejilla.jpg);border-radius:10px;min-height:70vh}
    #derecha button{font-size:24px;line-height:1;padding:.25em .6em;border-radius:999px;border:1px solid #aaa;background:#fff;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,.15)}
    article{
      position:absolute; left:0; top:0;
      width:100px;height:100px;border-radius:10px;background:white;border:1px solid grey;
      box-shadow:0 4px 10px rgba(0,0,0,0.3); cursor:grab; user-select:none;
      display:flex;align-items:center;justify-content:center;font:14px/1.2 system-ui;
    }
    article.dragging{cursor:grabbing;opacity:.9}
  </style>
</head>
<body>
  <div id="izquierda"></div>
  <div id="centro" id="lienzo" aria-label="zona de nodos"></div>
  <div id="derecha">
    <button id="anyadir" title="Añadir nodo">+</button>
  </div>

  <script>
    // Modelo de datos
    class Nodo {
      constructor(x, y, el){
        this.x = x;
        this.y = y;
        this.el = el; // referencia al artículo en pantalla
      }
    }

    const centro = document.getElementById("centro");
    const boton = document.getElementById("anyadir");
    const nodos = []; // almacén de nodos en memoria

    // Drag & drop sencillo con puntero (sin HTML5 drag)
    let dragging = null;
    let startMouseX = 0, startMouseY = 0;
    let startLeft = 0, startTop = 0;

    // Crea un <article> y su Nodo asociado
    function crearNodo(x, y){
      const el = document.createElement("article");
      el.style.left = x + "px";
      el.style.top  = y + "px";
      el.textContent = `(${x}, ${y})`;
      el.tabIndex = 0; // accesible

      // Registrar eventos de arrastre para ESTE elemento
      el.addEventListener("mousedown", (e) => iniciarDrag(e, el));
      el.addEventListener("touchstart", (e) => iniciarDrag(e.touches[0], el), {passive:false});

      centro.appendChild(el);

      const nodo = new Nodo(x, y, el);
      el.dataset.index = nodos.length.toString(); // vínculo el→nodo
      nodos.push(nodo);
      return nodo;
    }

    function iniciarDrag(e, el){
      e.preventDefault();
      dragging = el;
      dragging.classList.add("dragging");

      const rect = dragging.getBoundingClientRect();
      startMouseX = e.clientX;
      startMouseY = e.clientY;
      // posición inicial relativa al contenedor
      startLeft = parseInt(dragging.style.left || 0, 10);
      startTop  = parseInt(dragging.style.top  || 0, 10);

      document.addEventListener("mousemove", moverDrag);
      document.addEventListener("mouseup", terminarDrag);
      document.addEventListener("touchmove", moverDragTouch, {passive:false});
      document.addEventListener("touchend", terminarDrag);
    }

    function moverDrag(e){
      if(!dragging) return;
      const dx = e.clientX - startMouseX;
      const dy = e.clientY - startMouseY;
      posicionar(dragging, startLeft + dx, startTop + dy);
    }

    function moverDragTouch(e){
      if(!dragging) return;
      const t = e.touches[0];
      const dx = t.clientX - startMouseX;
      const dy = t.clientY - startMouseY;
      posicionar(dragging, startLeft + dx, startTop + dy);
      e.preventDefault();
    }

    function terminarDrag(){
      if(!dragging) return;
      dragging.classList.remove("dragging");

      // Actualizar el Nodo en memoria con la posición final
      const idx = parseInt(dragging.dataset.index, 10);
      const nodo = nodos[idx];
      nodo.x = parseInt(dragging.style.left, 10);
      nodo.y = parseInt(dragging.style.top, 10);
      dragging.textContent = `(${nodo.x}, ${nodo.y})`;

      document.removeEventListener("mousemove", moverDrag);
      document.removeEventListener("mouseup", terminarDrag);
      document.removeEventListener("touchmove", moverDragTouch);
      document.removeEventListener("touchend", terminarDrag);
      dragging = null;
    }

    // Coloca el elemento dentro de los límites del contenedor
    function posicionar(el, x, y){
      const contRect = centro.getBoundingClientRect();
      const elRect = el.getBoundingClientRect();
      const maxX = contRect.width - elRect.width;
      const maxY = contRect.height - elRect.height;
      const nx = Math.max(0, Math.min(x, maxX));
      const ny = Math.max(0, Math.min(y, maxY));
      el.style.left = nx + "px";
      el.style.top  = ny + "px";
    }

    // Añadir nuevo nodo al pulsar el botón
    boton.addEventListener("click", () => {
      // posición inicial: centrado aproximado del contenedor
      const w = 100, h = 100; // tamaño del article en CSS
      const rect = centro.getBoundingClientRect();
      const x = Math.max(0, Math.round(rect.width/2 - w/2));
      const y = Math.max(0, Math.round(rect.height/2 - h/2));
      crearNodo(x, y);
    });

    // (Opcional) Crear uno inicial
    crearNodo(20, 20);
  </script>
</body>
</html>
```

### nodos control de pantalla

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Nodos con pan & zoom</title>
  <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
  <style>
    :root { --nodo-w: 100px; --nodo-h: 100px; }
    body{display:flex;min-height:100vh;gap:10px;padding:10px;box-sizing:border-box;}
    #izquierda,#derecha{flex:1;display:flex;align-items:flex-start;justify-content:center;}
    #centro{
      flex:6; position:relative; overflow:hidden; border-radius:10px;
      box-shadow:0 0 20px rgba(0,0,0,0.3) inset; background:#f6f6f6;
      user-select:none; touch-action:none;
    }

    /* El mundo es el lienzo interno que se pan/zoom-ea */
    #mundo{
      position:absolute; left:0; top:0;
      width:4000px; height:3000px; /* gran área para moverse */
      background-image:url(rejilla.png);
     
      transform-origin: 0 0;
    }

    #derecha button{
      font-size:24px;line-height:1;padding:.25em .6em;border-radius:999px;
      border:1px solid #aaa;background:#fff;cursor:pointer;
      box-shadow:0 2px 6px rgba(0,0,0,.15)
    }
    article{
      position:absolute; left:0; top:0; width:var(--nodo-w); height:var(--nodo-h);
      border-radius:10px;background:white;border:1px solid grey;
      box-shadow:0 4px 10px rgba(0,0,0,0.3); cursor:grab; user-select:none;
      display:flex;align-items:center;justify-content:center;font:14px/1.2 system-ui;
    }
    article.dragging{cursor:grabbing;opacity:.9}
    #hint{
      position:absolute; right:10px; bottom:10px; background:rgba(255,255,255,.85);
      padding:.35rem .5rem; border:1px solid #ccc; border-radius:6px; font:12px system-ui;
    }
  </style>
</head>
<body>
  <div id="izquierda"></div>
  <div id="centro" aria-label="zona de trabajo">
    <div id="mundo"></div>
    <div id="hint">Ctrl + rueda: zoom · Ctrl + arrastrar: pan</div>
  </div>
  <div id="derecha">
    <button id="anyadir" title="Añadir nodo">+</button>
  </div>

  <script>
    // ===== Modelo =====
    class Nodo {
      constructor(x, y, el){ this.x = x; this.y = y; this.el = el; }
    }
    const centro = document.getElementById("centro");
    const mundo  = document.getElementById("mundo");
    const boton  = document.getElementById("anyadir");
    const nodos  = [];

    // ===== Estado de vista (pan/zoom global) =====
    let scale = 1;                 // zoom actual
    let translateX = 0, translateY = 0; // pan actual (px en pantalla)

    function aplicarTransform(){
      mundo.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
    }
    aplicarTransform();

    // ===== Crear nodos =====
    function crearNodo(x, y){
      const el = document.createElement("article");
      el.style.left = x + "px"; // coord en mundo (no pantalla)
      el.style.top  = y + "px";
      el.textContent = `(${x}, ${y})`;
      el.tabIndex = 0;

      el.addEventListener("mousedown", (e) => {
        // Si está pulsado Ctrl, este mousedown se usa para pan global, no para drag de nodo
        if(e.ctrlKey) return;
        iniciarDragNodo(e, el);
      });
      // (touch opcional omitido por brevedad)

      mundo.appendChild(el);

      const nodo = new Nodo(x, y, el);
      el.dataset.index = nodos.length.toString();
      nodos.push(nodo);
      return nodo;
    }

    // ===== Drag de nodos (respeta el zoom) =====
    let dragging = null;
    let startMouseX = 0, startMouseY = 0;
    let startLeft = 0, startTop = 0;

    function iniciarDragNodo(e, el){
      e.preventDefault();
      dragging = el;
      dragging.classList.add("dragging");
      startMouseX = e.clientX;
      startMouseY = e.clientY;
      startLeft = parseFloat(dragging.style.left) || 0; // coords de mundo
      startTop  = parseFloat(dragging.style.top)  || 0;

      document.addEventListener("mousemove", moverDragNodo);
      document.addEventListener("mouseup", terminarDragNodo);
    }

    function moverDragNodo(e){
      if(!dragging) return;
      // delta de pantalla => delta de mundo (dividir por escala)
      const dxWorld = (e.clientX - startMouseX) / scale;
      const dyWorld = (e.clientY - startMouseY) / scale;

      const nx = startLeft + dxWorld;
      const ny = startTop  + dyWorld;

      posicionarEnMundo(dragging, nx, ny);
    }

    function terminarDragNodo(){
      if(!dragging) return;
      dragging.classList.remove("dragging");
      const idx = parseInt(dragging.dataset.index, 10);
      const nodo = nodos[idx];
      nodo.x = parseFloat(dragging.style.left) || 0;
      nodo.y = parseFloat(dragging.style.top)  || 0;
      dragging.textContent = `(${Math.round(nodo.x)}, ${Math.round(nodo.y)})`;
      document.removeEventListener("mousemove", moverDragNodo);
      document.removeEventListener("mouseup", terminarDragNodo);
      dragging = null;
    }

    // Mantener nodos dentro del mundo
    function posicionarEnMundo(el, x, y){
      const w = parseFloat(getComputedStyle(el).width);
      const h = parseFloat(getComputedStyle(el).height);
      const maxX = mundo.clientWidth  - w;
      const maxY = mundo.clientHeight - h;
      const nx = Math.max(0, Math.min(x, maxX));
      const ny = Math.max(0, Math.min(y, maxY));
      el.style.left = nx + "px";
      el.style.top  = ny + "px";
    }

    // ===== Pan global con Ctrl + arrastrar =====
    let panning = false;
    let panStartX = 0, panStartY = 0;
    let startTX = 0, startTY = 0;

    centro.addEventListener("mousedown", (e) => {
      // Solo pan si Ctrl está presionado y botón izq dentro del centro
      if(e.ctrlKey && e.button === 0){
        panning = true;
        panStartX = e.clientX;
        panStartY = e.clientY;
        startTX = translateX;
        startTY = translateY;
        e.preventDefault();
      }
    });

    document.addEventListener("mousemove", (e) => {
      if(!panning) return;
      const dx = e.clientX - panStartX;
      const dy = e.clientY - panStartY;
      translateX = startTX + dx;
      translateY = startTY + dy;
      aplicarTransform();
    });

    document.addEventListener("mouseup", () => { panning = false; });

    // ===== Zoom con Ctrl + scroll (centrado en el cursor) =====
    centro.addEventListener("wheel", (e) => {
      if(!e.ctrlKey) return; // solo si Ctrl
      e.preventDefault();

      const rect = centro.getBoundingClientRect();
      const mouseX = e.clientX - rect.left; // coords de pantalla relativas a #centro
      const mouseY = e.clientY - rect.top;

      // Punto de mundo bajo el cursor antes del zoom
      const worldX = (mouseX - translateX) / scale;
      const worldY = (mouseY - translateY) / scale;

      // Ajuste de escala
      const zoomIntensity = 0.0015; // más pequeño = más suave
      const newScale = clamp(scale * (1 - e.deltaY * zoomIntensity), 0.2, 3.5);

      // Mantener el mismo punto de mundo bajo el puntero
      translateX = mouseX - worldX * newScale;
      translateY = mouseY - worldY * newScale;
      scale = newScale;

      aplicarTransform();
    }, { passive:false });

    function clamp(v, a, b){ return Math.max(a, Math.min(b, v)); }

    // ===== Botón añadir =====
    boton.addEventListener("click", () => {
      // crear en el centro visible actual
      const rect = centro.getBoundingClientRect();
      // Centro de pantalla → convertir a coords de mundo
      const screenX = rect.width/2, screenY = rect.height/2;
      const worldX = (screenX - translateX) / scale - parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nodo-w'))/2;
      const worldY = (screenY - translateY) / scale - parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nodo-h'))/2;
      crearNodo(Math.round(worldX), Math.round(worldY));
    });

    // Nodo de ejemplo
    crearNodo(40, 40);
  </script>
</body>
</html>
```

### nodos de conector

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Nodos con puertos, conexiones, pan & zoom</title>
  <link rel="stylesheet" href="https://jocarsa.github.io/cssreset/cssreset.css">
  <style>
    :root { --nodo-w: 140px; --nodo-h: 100px; --port: 16px; }

    body{display:flex;min-height:100vh;gap:10px;padding:10px;box-sizing:border-box;background:linear-gradient(135deg,#f7f8fb,#eef1f7);}
    #izquierda,#derecha{flex:1;display:flex;align-items:flex-start;justify-content:center;}
    #centro{
      flex:6; position:relative; overflow:hidden; border-radius:14px;
      box-shadow:0 10px 40px rgba(0,0,0,0.18); background:#f6f6f9;
      user-select:none; touch-action:none; border:1px solid #e5e7f0;
    }

    /* Mundo pan/zoom + rejilla */
    #mundo{
      position:absolute; left:0; top:0; width:4000px; height:3000px;
      background-image:
        radial-gradient(circle at 1px 1px, rgba(0,0,0,0.06) 1px, transparent 1px),
        linear-gradient(transparent,transparent);
      background-size: 40px 40px, 100% 100%;
      transform-origin: 0 0;
    }

    /* SVG de conexiones ocupando todo el mundo */
    #edges {
      position:absolute; left:0; top:0; width:100%; height:100%;
      pointer-events:none; /* las líneas no bloquean el ratón */
    }

    #derecha button{
      font-size:24px;line-height:1;padding:.25em .6em;border-radius:999px;
      border:1px solid #aeb6c7;background:#ffffffa6;backdrop-filter: blur(4px);
      cursor:pointer; box-shadow:0 6px 18px rgba(79,114,205,.25);
      transition: transform .08s ease;
    }
    #derecha button:active{ transform: scale(.96); }

    /* Nodo */
    article{
      position:absolute; left:0; top:0; width:var(--nodo-w); height:var(--nodo-h);
      border-radius:14px; background:linear-gradient(180deg, rgba(255,255,255,.9), rgba(250,251,255,.7));
      border:1px solid #dfe4ef; box-shadow:
        0 12px 30px rgba(30,60,120,0.18),
        inset 0 1px 0 rgba(255,255,255,.6);
      cursor:grab; user-select:none; display:flex; align-items:center; justify-content:center;
      font:600 14px/1.2 ui-sans-serif, system-ui, -apple-system, "Segoe UI";
      color:#2b3a55;
    }
    article::before{
      content:""; position:absolute; left:0; top:0; right:0; height:34px;
      border-radius:14px 14px 10px 10px;
      background:linear-gradient(90deg,#6aa3ff,#9c7bff);
      box-shadow:inset 0 -1px 0 rgba(255,255,255,.35);
      opacity:.9;
    }
    article span.title{
      position:absolute; top:8px; left:12px; font:600 12px/1 ui-sans-serif; color:white; text-shadow:0 1px 2px rgba(0,0,0,.25);
    }
    article.dragging{ cursor:grabbing; opacity:.95; }

    /* Puertos */
    .port{
      position:absolute; width:var(--port); height:var(--port); border-radius:50%;
      background: radial-gradient(circle at 30% 30%, #fff, #cfe0ff);
      border:1px solid #9db5ff; box-shadow: 0 0 0 2px #ffffffaa, 0 6px 14px rgba(90,120,200,.35);
      display:grid; place-items:center;
    }
    .port::after{
      content:""; width:6px; height:6px; border-radius:50%; background:#4a7dff; box-shadow:0 0 10px #6aa3ff;
    }
    .port.in  { left: calc(-.5 * var(--port)); top: 50%; transform: translateY(-50%); }
    .port.out { right: calc(-.5 * var(--port)); top: 50%; transform: translateY(-50%); }
    .port.highlight { border-color:#53e3a6; box-shadow:0 0 0 2px #eafff5, 0 0 24px rgba(83,227,166,.7); }
    .port.block { pointer-events:none; filter:grayscale(1) opacity(.6); }

    /* Tooltip de ayuda */
    #hint{
      position:absolute; right:10px; bottom:10px; background:rgba(255,255,255,.9);
      padding:.4rem .6rem; border:1px solid #dfe4ef; border-radius:8px;
      font:12px system-ui; box-shadow:0 8px 20px rgba(0,0,0,.08);
    }

    /* Estética de aristas */
    .edge-path{
      fill:none; stroke:#6a86ff; stroke-width:3;
      filter: drop-shadow(0 2px 2px rgba(0,0,0,.15));
    }
    .edge-path.bg{ stroke:#cdd8ff; stroke-width:7; opacity:.75; }
    .edge-path.preview{ stroke-dasharray:8 8; opacity:.85; }
    .edge-glow{ filter: blur(8px); opacity:.45; }
  </style>
</head>
<body>
  <div id="izquierda"></div>

  <div id="centro" aria-label="zona de trabajo">
    <div id="mundo">
      <svg id="edges" viewBox="0 0 4000 3000" preserveAspectRatio="none"></svg>
      <!-- nodos se insertan aquí -->
    </div>
    <div id="hint">Ctrl + rueda: zoom · Ctrl + arrastrar: pan · Arrastra salida → entrada para conectar</div>
  </div>

  <div id="derecha">
    <button id="anyadir" title="Añadir nodo">+</button>
  </div>

  <script>
    // ===== Modelo =====
    class Nodo {
      constructor(x, y, el){ this.x = x; this.y = y; this.el = el; }
    }
    const centro = document.getElementById("centro");
    const mundo  = document.getElementById("mundo");
    const edgesSvg = document.getElementById("edges");
    const boton  = document.getElementById("anyadir");
    const nodos  = [];
    const conexiones = []; // {from: idxA, to: idxB, pathBg, path, glow}

    // ===== Estado de vista (pan/zoom global) =====
    let scale = 1;
    let translateX = 0, translateY = 0;
    function aplicarTransform(){
      mundo.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
    }
    aplicarTransform();

    // ==== Utilidades coords
    function screenToWorld(x, y){
      const rect = centro.getBoundingClientRect();
      return { x: (x - rect.left - translateX) / scale,
               y: (y - rect.top  - translateY) / scale };
    }
    function clamp(v, a, b){ return Math.max(a, Math.min(b, v)); }

    // ===== Crear nodos =====
    let nodoCounter = 1;
    function crearNodo(x, y){
      const el = document.createElement("article");
      el.style.left = x + "px";
      el.style.top  = y + "px";
      el.innerHTML = `<span class="title">Nodo ${nodoCounter++}</span>`;
      el.tabIndex = 0;

      // Puertos
      const portIn  = document.createElement('div');
      portIn.className = 'port in';
      const portOut = document.createElement('div');
      portOut.className = 'port out';
      el.appendChild(portIn);
      el.appendChild(portOut);

      // Arrastre de nodo (Ctrl anula: pan global)
      el.addEventListener("mousedown", (e) => {
        if(e.ctrlKey) return; // pan global gestiona #centro
        if(e.target.classList.contains('port')) return; // si se pincha puerto, no mover nodo
        iniciarDragNodo(e, el);
      });

      // Iniciar conexión desde salida
      portOut.addEventListener('mousedown', (e)=>{
        e.stopPropagation();
        iniciarConexionDesdeSalida(e, el, portOut);
      });

      // Recibir conexión en entrada
      portIn.addEventListener('mouseup', (e)=>{
        e.stopPropagation();
        if(conexionEnCurso) finalizarConexionEnEntrada(el, portIn);
      });

      mundo.appendChild(el);

      const nodo = new Nodo(x, y, el);
      el.dataset.index = nodos.length.toString();
      nodos.push(nodo);
      return nodo;
    }

    // ===== Drag de nodos (respeta el zoom) =====
    let dragging = null;
    let startMouseX = 0, startMouseY = 0;
    let startLeft = 0, startTop = 0;

    function iniciarDragNodo(e, el){
      e.preventDefault();
      dragging = el;
      dragging.classList.add("dragging");
      startMouseX = e.clientX;
      startMouseY = e.clientY;
      startLeft = parseFloat(dragging.style.left) || 0;
      startTop  = parseFloat(dragging.style.top)  || 0;

      document.addEventListener("mousemove", moverDragNodo);
      document.addEventListener("mouseup", terminarDragNodo);
    }

    function moverDragNodo(e){
      if(!dragging) return;
      const dxWorld = (e.clientX - startMouseX) / scale;
      const dyWorld = (e.clientY - startMouseY) / scale;
      const nx = startLeft + dxWorld;
      const ny = startTop  + dyWorld;
      posicionarEnMundo(dragging, nx, ny);
      // actualizar conexiones relacionadas
      const idx = parseInt(dragging.dataset.index, 10);
      actualizarConexionesDeNodo(idx);
    }

    function terminarDragNodo(){
      if(!dragging) return;
      dragging.classList.remove("dragging");
      const idx = parseInt(dragging.dataset.index, 10);
      const nodo = nodos[idx];
      nodo.x = parseFloat(dragging.style.left) || 0;
      nodo.y = parseFloat(dragging.style.top)  || 0;
      document.removeEventListener("mousemove", moverDragNodo);
      document.removeEventListener("mouseup", terminarDragNodo);
      dragging = null;
    }

    function posicionarEnMundo(el, x, y){
      const w = parseFloat(getComputedStyle(el).width);
      const h = parseFloat(getComputedStyle(el).height);
      const maxX = mundo.clientWidth  - w;
      const maxY = mundo.clientHeight - h;
      const nx = Math.max(0, Math.min(x, maxX));
      const ny = Math.max(0, Math.min(y, maxY));
      el.style.left = nx + "px";
      el.style.top  = ny + "px";
    }

    // ===== Pan global Ctrl + arrastrar =====
    let panning = false;
    let panStartX = 0, panStartY = 0;
    let startTX = 0, startTY = 0;

    centro.addEventListener("mousedown", (e) => {
      if(e.ctrlKey && e.button === 0){
        panning = true;
        panStartX = e.clientX;
        panStartY = e.clientY;
        startTX = translateX;
        startTY = translateY;
        e.preventDefault();
      }
    });
    document.addEventListener("mousemove", (e) => {
      if(!panning) return;
      const dx = e.clientX - panStartX;
      const dy = e.clientY - panStartY;
      translateX = startTX + dx;
      translateY = startTY + dy;
      aplicarTransform();
    });
    document.addEventListener("mouseup", () => { panning = false; });

    // ===== Zoom Ctrl + rueda (centrado en cursor) =====
    centro.addEventListener("wheel", (e) => {
      if(!e.ctrlKey) return;
      e.preventDefault();

      const rect = centro.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      const worldX = (mouseX - translateX) / scale;
      const worldY = (mouseY - translateY) / scale;

      const zoomIntensity = 0.0015;
      const newScale = clamp(scale * (1 - e.deltaY * zoomIntensity), 0.2, 3.5);

      translateX = mouseX - worldX * newScale;
      translateY = mouseY - worldY * newScale;
      scale = newScale;

      aplicarTransform();
    }, { passive:false });

    // ===== Conexiones =====
    let conexionEnCurso = null; // {fromIdx, pathBg, path, glow}
    function getPortCenterWorld(portEl){
      // Tomamos el centro del rectángulo en pantalla y lo convertimos a mundo
      const r = portEl.getBoundingClientRect();
      const cx = r.left + r.width/2;
      const cy = r.top  + r.height/2;
      return screenToWorld(cx, cy);
    }

    function crearPathsSVG(claseExtra=""){
      const pathBg = document.createElementNS("http://www.w3.org/2000/svg","path");
      const path = document.createElementNS("http://www.w3.org/2000/svg","path");
      const glow = document.createElementNS("http://www.w3.org/2000/svg","path");
      pathBg.setAttribute("class", `edge-path bg ${claseExtra}`);
      path.setAttribute("class", `edge-path ${claseExtra}`);
      glow.setAttribute("class", `edge-path edge-glow ${claseExtra}`);
      glow.setAttribute("stroke", "#6a86ff");
      glow.setAttribute("stroke-width", "8");
      edgesSvg.appendChild(glow);
      edgesSvg.appendChild(pathBg);
      edgesSvg.appendChild(path);
      return { pathBg, path, glow };
    }

    function makePathD(x1,y1,x2,y2){
      const dx = Math.max(40, Math.abs(x2-x1)*0.5);
      const c1x = x1 + dx, c1y = y1;
      const c2x = x2 - dx, c2y = y2;
      return `M ${x1} ${y1} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${x2} ${y2}`;
    }

    function drawPaths(paths, x1,y1,x2,y2){
      const d = makePathD(x1,y1,x2,y2);
      paths.pathBg.setAttribute("d", d);
      paths.path.setAttribute("d", d);
      paths.glow.setAttribute("d", d);
    }

    function iniciarConexionDesdeSalida(e, nodoEl, portOut){
      const fromIdx = parseInt(nodoEl.dataset.index,10);
      const {x:x1,y:y1} = getPortCenterWorld(portOut);
      const paths = crearPathsSVG("preview");
      conexionEnCurso = { fromIdx, paths };

      // Resaltar entradas
      document.querySelectorAll('.port.in').forEach(p=>p.classList.add('highlight'));

      const move = (ev)=>{
        const world = screenToWorld(ev.clientX, ev.clientY);
        drawPaths(paths, x1, y1, world.x, world.y);
      };
      const up = ()=>{
        // cancelar si no terminó en entrada
        cancelarPreview();
        document.removeEventListener('mousemove', move);
        document.removeEventListener('mouseup', up);
      };

      document.addEventListener('mousemove', move);
      document.addEventListener('mouseup', up);
    }

    function finalizarConexionEnEntrada(targetNodoEl, portIn){
      if(!conexionEnCurso) return;
      const toIdx = parseInt(targetNodoEl.dataset.index,10);
      if(conexionEnCurso.fromIdx === toIdx){ cancelarPreview(); return; } // no autoconectar

      // Crear conexión definitiva
      const fromIdx = conexionEnCurso.fromIdx;
      const fromNodoEl = nodos[fromIdx].el;
      const portOut = fromNodoEl.querySelector('.port.out');

      const {x:x1,y:y1} = getPortCenterWorld(portOut);
      const {x:x2,y:y2} = getPortCenterWorld(portIn);

      const paths = crearPathsSVG();
      drawPaths(paths, x1,y1,x2,y2);

      conexiones.push({ from: fromIdx, to: toIdx, ...paths });

      cancelarPreview();
    }

    function cancelarPreview(){
      if(!conexionEnCurso) return;
      const { paths } = conexionEnCurso;
      // quitar resaltado de entradas
      document.querySelectorAll('.port.in').forEach(p=>p.classList.remove('highlight'));
      // borrar paths preview
      [paths.path, paths.pathBg, paths.glow].forEach(el=> el.remove());
      conexionEnCurso = null;
    }

    function actualizarConexionesDeNodo(idx){
      conexiones.forEach(con=>{
        if(con.from === idx || con.to === idx){
          const fromEl = nodos[con.from].el.querySelector('.port.out');
          const toEl   = nodos[con.to].el.querySelector('.port.in');
          const a = getPortCenterWorld(fromEl);
          const b = getPortCenterWorld(toEl);
          drawPaths(con, a.x, a.y, b.x, b.y);
        }
      });
    }

    // ===== Botón añadir =====
    boton.addEventListener("click", () => {
      const rect = centro.getBoundingClientRect();
      const screenX = rect.width/2, screenY = rect.height/2;
      const worldX = (screenX - translateX) / scale - parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nodo-w'))/2;
      const worldY = (screenY - translateY) / scale - parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nodo-h'))/2;
      crearNodo(Math.round(worldX), Math.round(worldY));
    });

    // ===== Nodos demo
    crearNodo(120, 120);
    crearNodo(420, 260);
    crearNodo(760, 180);
  </script>
</body>
</html>
```

<a id="actualizacion-del-sistema-erp-crm-y-aplicacion-de-actualizaciones"></a>
## Actualización del sistema ERP-CRM y aplicación de actualizaciones

En este capítulo, nos adentramos en la actualización del sistema ERP-CRM y su aplicación de actualizaciones. La evolución constante de estos sistemas es crucial para mantener su eficiencia y adaptabilidad a las necesidades cambiantes de una organización.

La actualización del sistema ERP-CRM implica no solo la introducción de nuevas funcionalidades, sino también mejoras en el rendimiento y seguridad. Este proceso puede ser desafiante debido a la complejidad de los sistemas existentes y la posibilidad de interrupciones en las operaciones diarias.

Antes de proceder con la actualización, es fundamental realizar una evaluación detallada del sistema actual. Esto incluye identificar áreas que requieren mejora, analizar el impacto potencial de las nuevas funcionalidades y planificar los recursos necesarios para la implementación. Es crucial contar con un equipo de expertos en sistemas ERP-CRM para llevar a cabo esta evaluación.

Una vez definido el plan de actualización, se procede al proceso de instalación. Esto implica descargar la nueva versión del sistema desde el proveedor oficial, realizar una copia de seguridad completa del sistema actual y preparar los entornos de desarrollo y pruebas necesarios. Es importante seguir las instrucciones proporcionadas por el proveedor para asegurar una instalación correcta.

Durante la fase de prueba, se realizan diversas pruebas exhaustivas para verificar que todas las nuevas funcionalidades funcionen correctamente y que no hay conflictos con los módulos existentes. Se llevan a cabo pruebas de integración y pruebas de rendimiento para asegurar que el sistema pueda manejar la carga de trabajo esperada.

La aplicación de actualizaciones es un proceso delicado que requiere cuidado especial. Es importante realizar esta tarea durante periodos de baja actividad del sistema, si es posible, para minimizar las interrupciones en las operaciones diarias. Además, se debe tener a mano los procedimientos de deshacer la actualización en caso de problemas inesperados.

Una vez que la actualización ha sido exitosamente aplicada y probada, se realiza una fase final de integración con el resto del sistema ERP-CRM. Esto implica configurar las nuevas funcionalidades para trabajar coherentemente con los módulos existentes y realizar ajustes finales en formularios e informes.

La documentación es un aspecto crucial de la actualización del sistema ERP-CRM. Es importante mantener registros detallados de todas las modificaciones realizadas, incluyendo el motivo de la actualización, los cambios implementados y cualquier problema que haya surgido durante el proceso. Esta documentación será invaluable para futuras referencias y para el soporte técnico.

La post-actualización es un período crucial para evaluar el rendimiento del sistema y recoger feedback de los usuarios. Es importante realizar pruebas adicionales para verificar que todas las funcionalidades nuevas estén funcionando correctamente y que no haya surgido ningún problema inesperado. Además, se debe llevar a cabo una capacitación adecuada para los usuarios finales sobre cómo utilizar las nuevas características del sistema.

La actualización del sistema ERP-CRM es un proceso integral que requiere planificación cuidadosa, ejecución meticulosa y evaluación exhaustiva. Al seguir estos pasos, podemos asegurarnos de que el sistema esté siempre alineado con las necesidades cambiantes de la organización y funcione eficientemente en todo momento.

En resumen, la actualización del sistema ERP-CRM es un proceso crucial para mantener su relevancia y eficiencia. Al seguir los pasos adecuados y llevar a cabo una evaluación exhaustiva, podemos asegurarnos de que el sistema esté siempre alineado con las necesidades cambiantes de la organización y funcione eficientemente en todo momento.

<a id="servicios-de-acceso-al-sistema-erp-crm"></a>
## Servicios de acceso al sistema ERP-CRM

En este capítulo, nos adentramos en la configuración avanzada del acceso a sistemas ERP-CRM, un aspecto crucial para su correcto funcionamiento. Comenzamos explorando los diferentes tipos de servicios que pueden proporcionar estos sistemas, desde el acceso remoto hasta las funcionalidades de integración con otros sistemas.

El primer paso es entender cómo establecer conexiones seguras y eficientes al sistema ERP-CRM. Esto implica conocer los protocolos de comunicación disponibles, como HTTP o HTTPS, y configurar correctamente los certificados digitales para garantizar la autenticidad del servidor. Además, se deben considerar las políticas de seguridad internas de la organización, incluyendo el uso de autenticación multifactor y la gestión de sesiones.

Una vez establecida la conexión inicial, es fundamental configurar los permisos y roles que determinarán qué funcionalidades estarán disponibles para cada usuario. Esto se realiza a través de interfaces gráficas o mediante scripts de configuración, dependiendo del sistema ERP-CRM utilizado. Es importante asegurarse de que los privilegios asignados sean mínimos pero suficientes para el desempeño del usuario, lo que contribuirá a la seguridad y eficiencia operativa.

Además de los servicios de acceso directo, muchos sistemas ERP-CRM ofrecen interfaces API (Aplicaciones Programables por Internet) que permiten integrar sus funcionalidades con otras aplicaciones. Esto es especialmente útil para automatizar procesos o para crear reportes personalizados que combinan datos de diferentes fuentes. La documentación detallada del sistema ERP-CRM es esencial en este proceso, ya que proporciona la información necesaria para entender cómo utilizar las APIs y cómo manejar los datos.

La configuración también implica el establecimiento de procesos de mantenimiento y actualización periódica del acceso al sistema. Esto incluye la revisión regular de las políticas de seguridad, la aplicación de parches y actualizaciones del software, y la monitorización del rendimiento para identificar y solucionar problemas antes de que afecten a los usuarios.

Es importante también considerar el aspecto legal y regulatorio en la configuración del acceso al sistema ERP-CRM. Esto puede implicar cumplir con normativas como GDPR (Reglamento General sobre Protección de Datos) o SOX (Ley de Contabilidad Interna), lo que requiere una configuración adecuada para proteger los datos personales y garantizar el cumplimiento legal.

Finalmente, la documentación detallada del proceso de instalación y configuración es un elemento crucial. Debe incluir instrucciones paso a paso, capturas de pantalla y ejemplos prácticos que ayuden a los usuarios a entender cada etapa del proceso. Además, se debe proporcionar soporte técnico para resolver cualquier problema que pueda surgir durante la configuración o el uso del sistema.

En resumen, la configuración avanzada del acceso al sistema ERP-CRM es un proceso integral que requiere una comprensión profunda de los sistemas y las políticas organizativas. Al seguir estos pasos, se asegurará que el sistema esté correctamente instalado y configurado para su uso eficiente y seguro por parte de todos los usuarios.

<a id="entornos-de-desarrollo-pruebas-y-explotacion"></a>
## Entornos de desarrollo, pruebas y explotación

En la instalación y configuración de sistemas ERP-CRM, es crucial considerar los entornos específicos para desarrollo, pruebas y explotación. Cada uno de estos entornos requiere una configuración adecuada para garantizar que el sistema funcione correctamente en diferentes fases del ciclo de vida del proyecto.

El entorno de desarrollo debe estar equipado con herramientas avanzadas que faciliten la creación y depuración del código. Esto incluye un editor de texto o IDE (Entorno de Desarrollo Integrado) que ofrezca autocompletado, resaltado de sintaxis y otras funcionalidades útiles. Además, es fundamental contar con versiones controladas de los códigos fuente para facilitar el seguimiento de cambios y colaboración entre los miembros del equipo.

El entorno de pruebas debe ser replicado lo más fielmente posible al entorno de producción. Esto implica la instalación de las mismas herramientas, bibliotecas y dependencias que se utilizarán en el sistema final. El objetivo es identificar problemas potenciales antes de que lleguen a la fase de explotación, minimizando así el tiempo de inactividad y los costos asociados.

El entorno de explotación es donde reside el sistema ERP-CRM una vez que ha sido implementado en producción. Es crucial que este entorno esté optimizado para el rendimiento y la seguridad. Esto incluye la configuración adecuada del servidor, la gestión eficiente de los recursos y la implementación de medidas de protección contra amenazas cibernéticas.

Además de estos entornos físicos o virtuales, es importante considerar también los entornos de configuración y despliegue. Esto implica la creación de scripts y procedimientos que faciliten la instalación y actualización del sistema en diferentes entornos. La automatización de este proceso puede ahorrar tiempo y reducir errores humanos.

En el contexto de sistemas ERP-CRM, es común utilizar herramientas de gestión de proyectos para monitorear y controlar los cambios en los entornos de desarrollo, pruebas y explotación. Estas herramientas permiten realizar seguimiento del progreso, asignar tareas y gestionar las incidencias que puedan surgir.

La configuración adecuada de los entornos de desarrollo, pruebas y explotación es un paso crucial en el ciclo de vida de cualquier sistema ERP-CRM. Una configuración incorrecta puede llevar a problemas significativos durante la fase de implementación y operaciones, lo que requiere tiempo adicional para solucionar y puede resultar en costos adicionales.

En resumen, la configuración adecuada de los entornos de desarrollo, pruebas y explotación es fundamental para el éxito del sistema ERP-CRM. Cada uno de estos entornos debe ser cuidadosamente planificado y ejecutado para garantizar que el sistema funcione correctamente en diferentes fases del ciclo de vida del proyecto.

<a id="ejercicio-de-final-de-unidad-1"></a>
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


<a id="organizacion-y-consulta-de-la-informacion"></a>
# Organización y consulta de la información

<a id="definicion-de-campos"></a>
## Definición de campos

En este capítulo, nos adentramos en la definición de campos, un concepto fundamental para el correcto funcionamiento de sistemas ERP-CRM. Los campos son las unidades básicas de información que se almacenan y manipulan dentro del sistema. Cada campo tiene un nombre descriptivo, un tipo de dato específico y una serie de atributos que determinan su comportamiento y uso.

El primer paso para definir un campo es elegir un nombre adecuado que refleje el propósito del mismo. Este nombre debe ser claro y conciso, evitando términos técnicos innecesarios o ambiguos. Por ejemplo, si estamos creando un sistema de gestión de clientes, un campo podría llamarse "Nombre del Cliente" en lugar de "nombre_cli".

El tipo de dato es otro aspecto crucial en la definición de campos. Determina qué tipo de información puede almacenar el campo y cómo se debe tratar. Algunos ejemplos comunes de tipos de datos son texto, número entero, número decimal, fecha y hora, booleano, etc. Cada tipo de dato tiene sus propias características y restricciones que deben ser consideradas al momento de su definición.

Además de los campos básicos, es común incluir atributos adicionales para mejorar la funcionalidad del campo. Por ejemplo, se pueden establecer restricciones como obligatoriedad (que el campo debe tener un valor), longitud máxima (para cadenas de texto), valores predeterminados o incluso opciones de selección predefinidas. Estos atributos ayudan a garantizar que los datos ingresados sean consistentes y cumplen con las necesidades del sistema.

La organización de campos en tablas es otro aspecto importante. Una tabla en un sistema ERP-CRM es una colección de campos que representan un concepto o entidad específica. Por ejemplo, podríamos tener una tabla llamada "Clientes" que contenga campos como Nombre del Cliente, DNI, Dirección, Teléfono, Email, etc. La organización de los campos en tablas permite una estructura lógica y coherente del sistema.

La definición de campos también implica considerar la integridad de los datos. Esto significa asegurarse de que los valores ingresados en un campo sean válidos según las reglas establecidas. Por ejemplo, si un campo es de tipo número entero, se debe evitar que se ingrese texto o números decimales. Las restricciones de validación son herramientas clave para mantener la calidad y precisión de los datos almacenados.

Además de la definición de campos básicos, también es importante considerar la escalabilidad del sistema. A medida que el sistema crece y evoluciona, puede ser necesario agregar nuevos campos o modificar los existentes. Por lo tanto, es recomendable diseñar los campos con flexibilidad en mente, permitiendo futuras modificaciones sin afectar la funcionalidad del sistema.

La definición de campos también implica considerar la seguridad de los datos. Es crucial asegurarse de que solo los usuarios autorizados puedan acceder y modificar ciertos campos. Esto se puede lograr mediante el uso de roles y permisos dentro del sistema, permitiendo un control preciso sobre quién puede ver o editar qué información.

En resumen, la definición de campos es una tarea fundamental en la configuración de sistemas ERP-CRM. Al elegir nombres descriptivos, tipos de datos apropiados y atributos adicionales, podemos crear tablas estructuradas y funcionales que almacenen y manipulen los datos de manera eficiente y segura. Esta fase es crucial para garantizar que el sistema cumpla con las necesidades del negocio y pueda ser utilizado de manera efectiva por sus usuarios finales.

### .htaccess

```
RewriteEngine On
RewriteBase /dam2526/Segundo/Sistemas%20de%20gesti%C3%B3n%20empresarial/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/001-Definici%C3%B3n%20de%20campos/101-Ejercicios/

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php [QSA,L]
```

### index

```
<?php
/*
   Enrutador de muestra
   Sistemas de gestión empresarial
   Alimenta a la interfaz, bebe de la base de datos
*/

$routes = [
    'GET' => [
        '/' => function() { echo "Home Page"; },
        '/contact' => function() { echo "Contact Page"; },
        '/menu' => function() { 
            $elementos = ['Productos','Servicios','Empleados'];
            echo json_encode($elementos, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
          },
        '/tabla' => function() { 

            $alumnos = [
                [
                    "id" => 1,
                    "nombre" => "Ana",
                    "apellidos" => "García López",
                    "curso" => "DAM 1",
                    "nota" => 8.5,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 2,
                    "nombre" => "Luis",
                    "apellidos" => "Martínez Pérez",
                    "curso" => "DAW 2",
                    "nota" => 6.7,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 3,
                    "nombre" => "María",
                    "apellidos" => "Sánchez Ruiz",
                    "curso" => "ASIR 1",
                    "nota" => 4.9,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 4,
                    "nombre" => "Carlos",
                    "apellidos" => "Fernández Gil",
                    "curso" => "DAM 2",
                    "nota" => 9.1,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 5,
                    "nombre" => "Elena",
                    "apellidos" => "Hernández Soto",
                    "curso" => "DAW 1",
                    "nota" => 7.3,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 6,
                    "nombre" => "Javier",
                    "apellidos" => "Romero Ortiz",
                    "curso" => "ASIR 2",
                    "nota" => 5.0,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 7,
                    "nombre" => "Laura",
                    "apellidos" => "Navas Peña",
                    "curso" => "DAM 1",
                    "nota" => 3.8,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 8,
                    "nombre" => "Sergio",
                    "apellidos" => "Molina Torres",
                    "curso" => "DAW 2",
                    "nota" => 9.4,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 9,
                    "nombre" => "Patricia",
                    "apellidos" => "Ibáñez Campos",
                    "curso" => "ASIR 1",
                    "nota" => 6.1,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 10,
                    "nombre" => "Pablo",
                    "apellidos" => "Vidal Rubio",
                    "curso" => "DAM 2",
                    "nota" => 4.2,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 11,
                    "nombre" => "Daniel",
                    "apellidos" => "Santos Muñoz",
                    "curso" => "DAW 1",
                    "nota" => 7.9,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 12,
                    "nombre" => "Irene",
                    "apellidos" => "López Cordero",
                    "curso" => "ASIR 2",
                    "nota" => 8.2,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 13,
                    "nombre" => "Raúl",
                    "apellidos" => "Castro Herrero",
                    "curso" => "DAM 1",
                    "nota" => 2.7,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 14,
                    "nombre" => "Cristina",
                    "apellidos" => "Requena Bravo",
                    "curso" => "DAW 2",
                    "nota" => 5.5,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 15,
                    "nombre" => "Alberto",
                    "apellidos" => "Morales Sanz",
                    "curso" => "ASIR 1",
                    "nota" => 6.9,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 16,
                    "nombre" => "Lucía",
                    "apellidos" => "Jiménez Gallego",
                    "curso" => "DAM 2",
                    "nota" => 9.8,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 17,
                    "nombre" => "Álvaro",
                    "apellidos" => "Rivas Lozano",
                    "curso" => "DAW 1",
                    "nota" => 4.6,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 18,
                    "nombre" => "Noelia",
                    "apellidos" => "Benítez Roldán",
                    "curso" => "ASIR 2",
                    "nota" => 7.1,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 19,
                    "nombre" => "Rubén",
                    "apellidos" => "Marín León",
                    "curso" => "DAM 1",
                    "nota" => 5.9,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 20,
                    "nombre" => "Sara",
                    "apellidos" => "Pascual Arias",
                    "curso" => "DAW 2",
                    "nota" => 3.5,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 21,
                    "nombre" => "Hugo",
                    "apellidos" => "Suárez Crespo",
                    "curso" => "ASIR 1",
                    "nota" => 8.0,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 22,
                    "nombre" => "Alba",
                    "apellidos" => "Domínguez Vega",
                    "curso" => "DAM 2",
                    "nota" => 7.7,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 23,
                    "nombre" => "Mario",
                    "apellidos" => "Serrano Lozano",
                    "curso" => "DAW 1",
                    "nota" => 2.9,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 24,
                    "nombre" => "Nuria",
                    "apellidos" => "Calvo Riera",
                    "curso" => "ASIR 2",
                    "nota" => 6.4,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 25,
                    "nombre" => "Jorge",
                    "apellidos" => "Vega Carrasco",
                    "curso" => "DAM 1",
                    "nota" => 9.0,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 26,
                    "nombre" => "Paula",
                    "apellidos" => "Silva Costa",
                    "curso" => "DAW 2",
                    "nota" => 5.2,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 27,
                    "nombre" => "Óscar",
                    "apellidos" => "Navarro Castaño",
                    "curso" => "ASIR 1",
                    "nota" => 4.0,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 28,
                    "nombre" => "Beatriz",
                    "apellidos" => "Herrera Pardo",
                    "curso" => "DAM 2",
                    "nota" => 7.0,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 29,
                    "nombre" => "Víctor",
                    "apellidos" => "Prieto Dávila",
                    "curso" => "DAW 1",
                    "nota" => 6.3,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 30,
                    "nombre" => "Rocío",
                    "apellidos" => "Aguilar Pino",
                    "curso" => "ASIR 2",
                    "nota" => 3.3,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 31,
                    "nombre" => "Gonzalo",
                    "apellidos" => "Campos Valdés",
                    "curso" => "DAM 1",
                    "nota" => 8.9,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 32,
                    "nombre" => "Marta",
                    "apellidos" => "Soler Martí",
                    "curso" => "DAW 2",
                    "nota" => 7.6,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 33,
                    "nombre" => "Adrián",
                    "apellidos" => "Pérez Lafuente",
                    "curso" => "ASIR 1",
                    "nota" => 5.8,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 34,
                    "nombre" => "Natalia",
                    "apellidos" => "Varela Rico",
                    "curso" => "DAM 2",
                    "nota" => 4.4,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 35,
                    "nombre" => "Diego",
                    "apellidos" => "Soto Rivas",
                    "curso" => "DAW 1",
                    "nota" => 8.1,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 36,
                    "nombre" => "Claudia",
                    "apellidos" => "Rey Serrat",
                    "curso" => "ASIR 2",
                    "nota" => 6.0,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 37,
                    "nombre" => "Iván",
                    "apellidos" => "Muñoz Rueda",
                    "curso" => "DAM 1",
                    "nota" => 2.5,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 38,
                    "nombre" => "Silvia",
                    "apellidos" => "Carrasco Roca",
                    "curso" => "DAW 2",
                    "nota" => 9.3,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 39,
                    "nombre" => "Tomás",
                    "apellidos" => "Durán Lillo",
                    "curso" => "ASIR 1",
                    "nota" => 7.4,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 40,
                    "nombre" => "Alicia",
                    "apellidos" => "Campos Naranjo",
                    "curso" => "DAM 2",
                    "nota" => 3.9,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 41,
                    "nombre" => "Felipe",
                    "apellidos" => "Casas Nieto",
                    "curso" => "DAW 1",
                    "nota" => 5.7,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 42,
                    "nombre" => "Helena",
                    "apellidos" => "Cano Vidal",
                    "curso" => "ASIR 2",
                    "nota" => 8.7,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 43,
                    "nombre" => "Andrés",
                    "apellidos" => "Franco Ríos",
                    "curso" => "DAM 1",
                    "nota" => 4.1,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 44,
                    "nombre" => "Verónica",
                    "apellidos" => "Ortega Alba",
                    "curso" => "DAW 2",
                    "nota" => 6.8,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 45,
                    "nombre" => "Ismael",
                    "apellidos" => "León Méndez",
                    "curso" => "ASIR 1",
                    "nota" => 7.2,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 46,
                    "nombre" => "Eva",
                    "apellidos" => "Rubio Cuesta",
                    "curso" => "DAM 2",
                    "nota" => 9.6,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 47,
                    "nombre" => "Mateo",
                    "apellidos" => "Álvarez Bravo",
                    "curso" => "DAW 1",
                    "nota" => 3.0,
                    "estado" => "Suspenso"
                ],
                [
                    "id" => 48,
                    "nombre" => "Sofía",
                    "apellidos" => "Delgado Ríos",
                    "curso" => "ASIR 2",
                    "nota" => 5.3,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 49,
                    "nombre" => "Bruno",
                    "apellidos" => "Cortés Lara",
                    "curso" => "DAM 1",
                    "nota" => 6.6,
                    "estado" => "Aprobado"
                ],
                [
                    "id" => 50,
                    "nombre" => "Julia",
                    "apellidos" => "Peña Soria",
                    "curso" => "DAW 2",
                    "nota" => 4.7,
                    "estado" => "Suspenso"
                ]
            ];


            echo json_encode($alumnos, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
          },
    ]
];

$method = $_SERVER['REQUEST_METHOD'];
$path = $_SERVER['REQUEST_URI'];



$parsed = parse_url($path);
$cleanPath = $parsed['path'];

// Remove your project base path
$base = '/dam2526/Segundo/Sistemas%20de%20gesti%C3%B3n%20empresarial/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/001-Definici%C3%B3n%20de%20campos/101-Ejercicios';
$finalPath = str_replace($base, '', $cleanPath);

if (empty($finalPath)) {
    $finalPath = '/';
}


if (isset($routes[$method][$finalPath])) {
    $routes[$method][$finalPath]();
} else {
    print_r(array_keys($routes['GET']));
    echo "<h2>404 - Route not found</h2>";
}
```

<a id="consultas-de-acceso-a-datos"></a>
## Consultas de acceso a datos

En la subunidad "Consultas de acceso a datos", nos adentramos en el aspecto fundamental de cómo interactuar con los sistemas ERP-CRM para recuperar información relevante. Las consultas de acceso a datos son una parte esencial del flujo de trabajo diario, permitiendo a los usuarios y administradores extraer y analizar datos de manera eficiente.

La estructura de las consultas varía según el sistema ERP-CRM utilizado, pero generalmente se basa en la definición de campos relevantes y la formulación de condiciones para filtrar los resultados. Este proceso implica una comprensión profunda del modelo de datos subyacente, que incluye entidades, relaciones y atributos.

La creación de consultas puede realizarse a través de interfaces gráficas o mediante lenguajes específicos como SQL (Structured Query Language) en sistemas basados en bases de datos. Cada sistema ERP-CRM tiene su propio conjunto de funciones y métodos para ejecutar estas consultas, lo que requiere un conocimiento específico del entorno.

Es importante destacar la importancia de la optimización de las consultas. Un buen diseño de consulta puede mejorar significativamente el rendimiento del sistema, reduciendo tiempos de respuesta y minimizando el uso de recursos. Esto se logra mediante la selección adecuada de índices, la minimización de los campos seleccionados y la estructuración de las condiciones de búsqueda.

Además de las consultas básicas, muchos sistemas ERP-CRM ofrecen funcionalidades avanzadas como consultas complejas, agregaciones y resúmenes. Estas herramientas permiten a los usuarios obtener información detallada y perspectivas valiosas sobre el desempeño de la empresa, facilitando toma de decisiones estratégicas.

La consulta de datos también implica la gestión adecuada de las relaciones entre diferentes entidades. En sistemas ERP-CRM, estas relaciones pueden ser complejas y requieren un enfoque cuidadoso para asegurar que los resultados sean precisos y completos. Esto puede implicar el uso de joins o subconsultas para combinar información de múltiples tablas.

La seguridad es otro aspecto crucial a considerar al realizar consultas de acceso a datos. Es fundamental garantizar que solo los usuarios autorizados puedan acceder a ciertos conjuntos de datos, lo que se logra mediante el control de privilegios y roles dentro del sistema ERP-CRM.

En conclusión, las consultas de acceso a datos son una herramienta poderosa en la gestión empresarial, permitiendo la extracción y análisis de información relevante para mejorar la eficiencia operativa y tomar decisiones informadas. A través de un enfoque estructurado y optimizado, los usuarios pueden aprovechar al máximo las capacidades de sus sistemas ERP-CRM, facilitando el acceso a datos precisos y actualizados.

### microERP

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>

<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      main{background:aliceblue;flex:6;padding:var(--margen);}
    </style>
  </head>
  <body>
    <nav>
      <?php
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
      ?>
    </nav>
    <main>
    </main>
  </body>
</html>
```

### muestro botones

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav a{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);}
      main{background:aliceblue;flex:6;padding:var(--margen);}
    </style>
  </head>
  <body>
    <nav>
      <?php
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){echo "<a href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";}
      ?>
    </nav>
    <main>
    </main>
  </body>
</html>
```

### cargo la tabla

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav a{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);}
      main{background:aliceblue;flex:6;padding:var(--margen);}
    </style>
  </head>
  <body>
    <nav>
      <?php
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){echo "<a href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";}
      ?>
    </nav>
    <main>
      <table>
      <?php
        $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");
        while($fila = mysqli_fetch_assoc($resultado)){
          echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "</tr>";
        }
      ?>
      </table>
    </main>
  </body>
</html>
```

### estilo de la tabla

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav a{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      .activo{width:105%;}
    </style>
  </head>
  <body>
    <nav>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<a class='".$clase."' href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";}
      ?>
    </nav>
    <main>
      <table>
      <?php // Listado de la tabla actualmente seleccionada
        $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");
        while($fila = mysqli_fetch_assoc($resultado)){
          echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "</tr>";
        }
      ?>
      </table>
    </main>
  </body>
</html>
```

### cabeceras de tabla

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav a{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;}
      .activo{width:105%;}
    </style>
  </head>
  <body>
    <nav>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<a class='".$clase."' href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";}
      ?>
    </nav>
    <main>
      <table>
      <?php // Listado de la tabla actualmente seleccionada
        $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");$contador=0;
        while($fila = mysqli_fetch_assoc($resultado)){
          if($contador == 0){echo "<tr>";foreach($fila as $clave=>$valor){echo "<th>".$clave."</th>";}echo "</tr>";}
          echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "</tr>";$contador++;
        }
      ?>
      </table>
    </main>
  </body>
</html>
```

### logo

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav a{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;}
      .activo{width:105%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo"><img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg"><p>jocarsa</p></div>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<a class='".$clase."' href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";}
      ?>
    </nav>
    <main>
      <table>
      <?php // Listado de la tabla actualmente seleccionada
        $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");$contador=0;
        while($fila = mysqli_fetch_assoc($resultado)){
          if($contador == 0){echo "<tr>";foreach($fila as $clave=>$valor){echo "<th>".$clave."</th>";}echo "</tr>";}
          echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "</tr>";$contador++;
        }
      ?>
      </table>
    </main>
  </body>
</html>
```

### añadimos boton de añadir

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo"><img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg"><p>jocarsa</p></div>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<button class='".$clase."'>";
        echo "<a href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){echo "<a href='?operacion=añadir' class='anadir'>+</a>";}
        echo "</button>";}
      ?>
    </nav>
    <main>
      <table>
      <?php // Listado de la tabla actualmente seleccionada
        $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");$contador=0;
        while($fila = mysqli_fetch_assoc($resultado)){
          if($contador == 0){echo "<tr>";foreach($fila as $clave=>$valor){echo "<th>".$clave."</th>";}echo "</tr>";}
          echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "</tr>";$contador++;
        }
      ?>
      </table>
    </main>
  </body>
</html>
```

### creo formulario

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo"><img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg"><p>jocarsa</p></div>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<button class='".$clase."'>";
        echo "<a href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){echo "<a href='?operacion=añadir&tabla=".$_GET['tabla']."' class='anadir'>+</a>";}
        echo "</button>";}
      ?>
    </nav>
    <main>
      <table>
      <?php // Listado de la tabla actualmente seleccionada
        if(isset($_GET['tabla'])){
          if(isset($_GET['operacion'])){
            echo "<form>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla']." LIMIT 1;");
            while($fila = mysqli_fetch_assoc($resultado)){
              foreach($fila as $clave=>$valor){echo "<input type='text' placeholder='".$clave."'>";}
            }
            echo "<input type='submit'></form>";
          }else{
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");$contador=0;
            while($fila = mysqli_fetch_assoc($resultado)){
              if($contador == 0){echo "<tr>";foreach($fila as $clave=>$valor){echo "<th>".$clave."</th>";}echo "</tr>";}
              echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "</tr>";$contador++;
            }
          }
        }
      ?>
      </table>
    </main>
  </body>
</html>
```

### estilo del formulario

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;}
      form{padding:var(--margen);columns:2;gap:var(--margen);}
      form input{width:100%;padding:var(--margen);box-sizing:border-box;margin-bottom:var(--margen);border:1px solid var(--color_primario);border-radius:var(--radio);}
      form input[type=submit]{background:var(--color_primario);color:white;}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo"><img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg"><p>jocarsa</p></div>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<button class='".$clase."'>";
        echo "<a href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){echo "<a href='?operacion=añadir&tabla=".$_GET['tabla']."' class='anadir'>+</a>";}
        echo "</button>";}
      ?>
    </nav>
    <main>
      
      <?php // Listado de la tabla actualmente seleccionada
        if(isset($_GET['tabla'])){
          if(isset($_GET['operacion'])){
            echo "<form action='hola' method='POST'>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla']." LIMIT 1;");
            while($fila = mysqli_fetch_assoc($resultado)){
              foreach($fila as $clave=>$valor){echo "<input type='text' placeholder='".$clave."'>";}
            }
            echo "<input type='submit'></form>";
          }else{
            echo "<table>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");$contador=0;
            while($fila = mysqli_fetch_assoc($resultado)){
              if($contador == 0){echo "<tr>";foreach($fila as $clave=>$valor){echo "<th>".$clave."</th>";}echo "</tr>";}
              echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "</tr>";$contador++;
            }
            echo "</table>";
          }
        }
      ?>
      
    </main>
  </body>
</html>
```

### pequeña animacion

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;animation:aparece 1s;}
      form{padding:var(--margen);columns:2;gap:var(--margen);}
      form input{width:100%;padding:var(--margen);box-sizing:border-box;margin-bottom:var(--margen);border:1px solid var(--color_primario);border-radius:var(--radio);}
      form input[type=submit]{background:var(--color_primario);color:white;}
      @keyframes aparece{0%{opacity:0;transform:translateX(-30px);}100%{opacity:1;transform:translateX(0px);}}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo"><img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg"><p>jocarsa</p></div>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<button class='".$clase."'>";
        echo "<a href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){echo "<a href='?operacion=añadir&tabla=".$_GET['tabla']."' class='anadir'>+</a>";}
        echo "</button>";}
      ?>
    </nav>
    <main>
      
      <?php // Listado de la tabla actualmente seleccionada
        if(isset($_GET['tabla'])){
          if(isset($_GET['operacion'])){
            echo "<form action='hola' method='POST'>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla']." LIMIT 1;");
            while($fila = mysqli_fetch_assoc($resultado)){
              foreach($fila as $clave=>$valor){echo "<input type='text' placeholder='".$clave."'>";}
            }
            echo "<input type='submit'></form>";
          }else{
            echo "<table>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");$contador=0;
            while($fila = mysqli_fetch_assoc($resultado)){
              if($contador == 0){echo "<tr>";foreach($fila as $clave=>$valor){echo "<th>".$clave."</th>";}echo "</tr>";}
              echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "</tr>";$contador++;
            }
            echo "</table>";
          }
        }
      ?>
      
    </main>
  </body>
</html>
```

### eliminar

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;animation:aparece 1s;}
      form{columns:2;gap:var(--margen);}
      form input{width:100%;padding:var(--margen);box-sizing:border-box;margin-bottom:var(--margen);border:1px solid var(--color_primario);border-radius:var(--radio);}
      form input[type=submit]{background:var(--color_primario);color:white;}
      @keyframes aparece{0%{opacity:0;transform:translateX(-30px);}100%{opacity:1;transform:translateX(0px);}}
      .eliminar{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;display:block;text-decoration:none;text-align:center;}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo"><img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg"><p>jocarsa</p></div>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<button class='".$clase."'>";
        echo "<a href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){echo "<a href='?operacion=añadir&tabla=".$_GET['tabla']."' class='anadir'>+</a>";}
        echo "</button>";}
      ?>
    </nav>
    <main>
      
      <?php // Listado de la tabla actualmente seleccionada
        if(isset($_GET['tabla'])){
          if(isset($_GET['operacion']) && $_GET['operacion'] == "añadir"){
            echo "<form action='hola' method='POST'>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla']." LIMIT 1;");
            while($fila = mysqli_fetch_assoc($resultado)){
              foreach($fila as $clave=>$valor){echo "<input type='text' placeholder='".$clave."'>";}
            }
            echo "<input type='submit'></form>";
          }else{
            if(isset($_GET['operacion']) && $_GET['operacion'] == "eliminar"){
              mysqli_query($conexion, "DELETE FROM ".$_GET['tabla']." WHERE Identificador = ".$_GET['id'].";");
            }
            echo "<table>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");$contador=0;
            while($fila = mysqli_fetch_assoc($resultado)){
              if($contador == 0){echo "<tr>";foreach($fila as $clave=>$valor){echo "<th>".$clave."</th>";}echo "<th></th></tr>";}
              echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "<td><a href='?operacion=eliminar&tabla=".$_GET['tabla']."&id=".$fila['Identificador']."' class='eliminar'>x</a></td></tr>";$contador++;
            }
            echo "</table>";
          }
        }
      ?>
      
    </main>
  </body>
</html>
```

<a id="interfaces-de-entrada-de-datos-y-de-procesos"></a>
## Interfaces de entrada de datos y de procesos.

En el mundo empresarial digital, la organización y consulta de la información son procesos fundamentales que permiten a las empresas operar eficientemente y tomar decisiones informadas. La gestión adecuada de estos datos es crucial para mantener la competitividad y la sostenibilidad del negocio.

Las interfaces de entrada de datos y de procesos desempeñan un papel vital en este proceso. Estas interfaces son los puntos donde los usuarios interactúan con el sistema, ingresando información o solicitando servicios. En una aplicación empresarial, estas interfaces pueden variar desde formularios web hasta aplicaciones móviles y sistemas de escritorio.

La organización de la información es un aspecto fundamental de las interfaces de entrada. Los campos de entrada deben estar bien definidos y organizados para facilitar la captura de datos precisos y completos. Por ejemplo, en un sistema de gestión de pedidos, los campos podrían incluir detalles del cliente, productos solicitados, cantidades y fechas de entrega.

Las interfaces de entrada también permiten la consulta de información existente. Los usuarios deben poder buscar y recuperar datos de manera rápida y precisa. Esto puede hacerse mediante formularios de búsqueda o consultas directas a la base de datos. Por ejemplo, en un sistema CRM, los usuarios podrían consultar registros de clientes específicos o generar informes sobre ventas por período.

La integración entre interfaces de entrada y procesos es otro aspecto importante. Una vez que se capturan los datos, estos deben ser procesados para su análisis y utilización. Los formularios web pueden estar vinculados a flujos de trabajo automatizados que generan informes o actualizan bases de datos en consecuencia.

Las interfaces de entrada también son cruciales para la interacción con otros sistemas de gestión empresarial. Por ejemplo, un sistema ERP puede tener interfaces que permiten la importación y exportación de datos con sistemas de inventario o contabilidad. Esta integración asegura la coherencia y actualización de los datos en toda la organización.

La personalización de las interfaces de entrada es otro aspecto importante. Los formularios y pantallas deben estar diseñados para facilitar el trabajo del usuario, adaptándose a sus necesidades específicas. Por ejemplo, un sistema CRM podría ofrecer diferentes vistas y opciones dependiendo del rol del usuario (vendedor, gerente, administrador).

La gestión de errores es otro aspecto crucial en las interfaces de entrada. Los sistemas deben estar preparados para manejar situaciones inesperadas o malas entradas de datos. Esto puede hacerse mediante validaciones automatizadas y mensajes de error claros.

En conclusión, las interfaces de entrada de datos y procesos son elementos esenciales en la gestión empresarial digital. Su diseño y organización adecuados pueden mejorar significativamente la eficiencia operativa y la toma de decisiones basada en datos. Al considerar aspectos como la organización de los campos, la consulta de información, la integración con otros sistemas y la personalización del usuario, se puede crear una experiencia de interacción que facilita el trabajo empresarial y mejora la productividad.

### definir tipos de campos

```
<?php $conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial"); ?>
<!doctype html>
<html lang="es">
  <head><title>microERP</title><meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;animation:aparece 1s;}
      form{columns:2;gap:var(--margen);}
      form input{width:100%;padding:var(--margen);box-sizing:border-box;margin-bottom:var(--margen);border:1px solid var(--color_primario);border-radius:var(--radio);}
      form input[type=submit]{background:var(--color_primario);color:white;}
      @keyframes aparece{0%{opacity:0;transform:translateX(-30px);}100%{opacity:1;transform:translateX(0px);}}
      .eliminar{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;display:block;text-decoration:none;text-align:center;}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo"><img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg"><p>jocarsa</p></div>
      <?php // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        while($fila = mysqli_fetch_assoc($resultado)){
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){$clase = "activo";}else{$clase = "";}
        echo "<button class='".$clase."'>";
        echo "<a href='?tabla=".$fila['Tables_in_empresarial']."'>".$fila['Tables_in_empresarial']."</a>";
        if($fila['Tables_in_empresarial'] == $_GET['tabla']){echo "<a href='?operacion=añadir&tabla=".$_GET['tabla']."' class='anadir'>+</a>";}
        echo "</button>";}
      ?>
    </nav>
    <main>
      
      <?php // Listado de la tabla actualmente seleccionada
        if(isset($_GET['tabla'])){
          if(isset($_GET['operacion']) && $_GET['operacion'] == "añadir"){
            echo "<form action='hola' method='POST'>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla']." LIMIT 1;");
            while($fila = mysqli_fetch_assoc($resultado)){
              foreach($fila as $clave=>$valor){echo "<input type='text' placeholder='".$clave."'>";}
            }
            echo "<input type='submit'></form>";
          }else{
            if(isset($_GET['operacion']) && $_GET['operacion'] == "eliminar"){
              mysqli_query($conexion, "DELETE FROM ".$_GET['tabla']." WHERE Identificador = ".$_GET['id'].";");
            }
            echo "<table>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$_GET['tabla'].";");$contador=0;
            while($fila = mysqli_fetch_assoc($resultado)){
              if($contador == 0){echo "<tr>";foreach($fila as $clave=>$valor){echo "<th>".$clave."</th>";}echo "<th></th></tr>";}
              echo "<tr>";foreach($fila as $clave=>$valor){echo "<td>".$valor."</td>";}echo "<td><a href='?operacion=eliminar&tabla=".$_GET['tabla']."&id=".$fila['Identificador']."' class='eliminar'>x</a></td></tr>";$contador++;
            }
            echo "</table>";
          }
        }
      ?>
      
    </main>
  </body>
</html>
```

### campos vinculados

```
<?php
$conexion = mysqli_connect("localhost","usuarioempresarial","usuarioempresarial","empresarial");
if(!$conexion){
  die("Error de conexión: ".mysqli_connect_error());
}

/**
 * Devuelve las claves foráneas de una tabla como:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd = 'empresarial'){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;align-items:center;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);overflow:auto;}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);vertical-align:top;}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;text-align:left;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);align-items:center;}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;margin:0;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;animation:aparece 1s;text-align:center;text-decoration:none;display:inline-block;}
      form{columns:2;gap:var(--margen);}
      form input,form select{width:100%;padding:var(--margen);box-sizing:border-box;margin-bottom:var(--margen);border:1px solid var(--color_primario);border-radius:var(--radio);}
      form input[type=submit]{background:var(--color_primario);color:white;cursor:pointer;}
      @keyframes aparece{0%{opacity:0;transform:translateX(-30px);}100%{opacity:1;transform:translateX(0px);}}
      .eliminar{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;display:block;text-decoration:none;text-align:center;}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo">
        <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
        <p>jocarsa</p>
      </div>
      <?php
        // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        $tabla_actual = isset($_GET['tabla']) ? $_GET['tabla'] : "";
        while($fila = mysqli_fetch_assoc($resultado)){
          $nombre_tabla = $fila['Tables_in_empresarial'];
          $clase = ($nombre_tabla == $tabla_actual) ? "activo" : "";
          echo "<button class='".$clase."'>";
            echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
            if($nombre_tabla == $tabla_actual){
              echo "<a href='?operacion=añadir&tabla=".$tabla_actual."' class='anadir'>+</a>";
            }
          echo "</button>";
        }
      ?>
    </nav>
    <main>
      <?php
        if(isset($_GET['tabla'])){
          $tabla = $_GET['tabla'];
          $foreignKeys = obtener_claves_foraneas($conexion, $tabla);

          // Eliminación
          if(isset($_GET['operacion']) && $_GET['operacion'] == "eliminar" && isset($_GET['id'])){
            mysqli_query(
              $conexion,
              "DELETE FROM ".$tabla." WHERE Identificador = ".intval($_GET['id']).";"
            );
          }

          // Inserción
          if(isset($_GET['operacion']) && $_GET['operacion'] == "añadir"){
            // Si viene por POST, procesamos inserción
            if($_SERVER['REQUEST_METHOD'] === 'POST'){
              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla." LIMIT 1;");
              if($resultado && $fila_ejemplo = mysqli_fetch_assoc($resultado)){
                $columnas = [];
                $valores = [];
                foreach($fila_ejemplo as $clave=>$valor){
                  // Suponemos que Identificador es autoincremental
                  if($clave == 'Identificador'){ continue; }
                  if(isset($_POST[$clave]) && $_POST[$clave] !== ''){
                    $columnas[] = "`".$clave."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$clave])."'";
                  }
                }
                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }
            }

            // Formulario de alta
            echo "<h2>Añadir registro en ".$tabla."</h2>";
            echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla." LIMIT 1;");
            if($resultado && $fila = mysqli_fetch_assoc($resultado)){
              foreach($fila as $clave=>$valor){
                // Omitimos el identificador
                if($clave == 'Identificador'){ continue; }

                // Si es FK: select con filas de la tabla relacionada
                if(isset($foreignKeys[$clave])){
                  $fk = $foreignKeys[$clave];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  echo "<label>".$clave."</label>";
                  echo "<select name='".$clave."'>";
                  echo "<option value=''>-- seleccionar --</option>";

                  $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                  if($res_fk){
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_opcion = implode(" | ", $partes);
                      $value_opcion = $fila_fk[$columna_fk];
                      echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                    }
                  }

                  echo "</select>";
                }else{
                  // Campo normal: input texto
                  echo "<input type='text' name='".$clave."' placeholder='".$clave."'>";
                }
              }
            }
            echo "<input type='submit' value='Guardar'>";
            echo "</form>";

          }else{
            // Listado
            echo "<h2>Listado de ".$tabla."</h2>";
            echo "<table>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
            $contador = 0;
            while($fila = mysqli_fetch_assoc($resultado)){
              if($contador == 0){
                echo "<tr>";
                  foreach($fila as $clave=>$valor){
                    echo "<th>".$clave."</th>";
                  }
                  echo "<th></th>";
                echo "</tr>";
              }

              echo "<tr>";
              foreach($fila as $clave=>$valor){
                // Si el campo es FK, mostramos fila de la tabla referenciada
                if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                  $fk = $foreignKeys[$clave];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  $sql_fk = "
                    SELECT *
                    FROM ".$tabla_fk."
                    WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                    LIMIT 1
                  ";
                  $res_fk = mysqli_query($conexion, $sql_fk);
                  if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                    $partes = [];
                    foreach($fila_fk as $k2=>$v2){
                      $partes[] = $v2;
                    }
                    $texto_celda = implode(" | ", $partes);
                    echo "<td>".$texto_celda."</td>";
                  }else{
                    // Si no encontramos la fila referenciada, mostramos el valor bruto
                    echo "<td>".$valor."</td>";
                  }
                }else{
                  // Campo normal
                  echo "<td>".$valor."</td>";
                }
              }

              // Columna de eliminar
              echo "<td><a href='?operacion=eliminar&tabla=".$tabla."&id=".$fila['Identificador']."' class='eliminar'>x</a></td>";
              echo "</tr>";

              $contador++;
            }
            echo "</table>";
          }
        }
      ?>
    </main>
  </body>
</html>
```

### variables

```
<?php
// Parámetros de conexión
$db_host = "localhost";
$db_name = "empresarial";
$db_user = "usuarioempresarial";
$db_pass = "usuarioempresarial";

$conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
if(!$conexion){
  die("Error de conexión: ".mysqli_connect_error());
}

/**
 * Devuelve las claves foráneas de una tabla como:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Devuelve metadatos de columnas de una tabla como:
 * [
 *   'campo' => [
 *      'COLUMN_NAME' => ...,
 *      'DATA_TYPE'   => ...,
 *      'IS_NULLABLE' => ...,
 *      'COLUMN_DEFAULT' => ...,
 *      'COLUMN_KEY'  => ...,
 *      'EXTRA'       => ...,
 *      'CHARACTER_MAXIMUM_LENGTH' => ...,
 *      'COLUMN_TYPE' => ...,
 *   ],
 *   ...
 * ]
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Genera el control de formulario HTML adecuado para una columna NO FK.
 * Tiene en cuenta el DATA_TYPE de MySQL y mapea a tipos HTML.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type  = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // Detectar tipos especiales
  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      // datetime-local espera formato 'YYYY-MM-DDThh:mm'
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos (blob, binary, etc.) -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;align-items:center;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);overflow:auto;}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);vertical-align:top;}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;text-align:left;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);align-items:center;}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;margin:0;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;animation:aparece 1s;text-align:center;text-decoration:none;display:inline-block;}
      form{columns:2;gap:var(--margen);}
      form label{display:block;font-weight:bold;margin-bottom:4px;}
      form input,form select{width:100%;padding:var(--margen);box-sizing:border-box;margin-bottom:var(--margen);border:1px solid var(--color_primario);border-radius:var(--radio);}
      form input[type=checkbox]{width:auto;padding:0;margin-top:5px;}
      form input[type=submit]{background:var(--color_primario);color:white;cursor:pointer;}
      @keyframes aparece{0%{opacity:0;transform:translateX(-30px);}100%{opacity:1;transform:translateX(0px);}}
      .eliminar{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;display:block;text-decoration:none;text-align:center;}
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo">
        <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
        <p>jocarsa</p>
      </div>
      <?php
        // Listado de los botones en base a las tablas de la base de datos
        $resultado = mysqli_query($conexion, "SHOW TABLES;");
        $tabla_actual = isset($_GET['tabla']) ? $_GET['tabla'] : "";
        while($fila = mysqli_fetch_assoc($resultado)){
          // En vez de 'Tables_in_empresarial', usamos el primer valor del array
          $nombre_tabla = array_values($fila)[0];
          $clase = ($nombre_tabla == $tabla_actual) ? "activo" : "";
          echo "<button class='".$clase."'>";
            echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
            if($nombre_tabla == $tabla_actual){
              echo "<a href='?operacion=añadir&tabla=".$tabla_actual."' class='anadir'>+</a>";
            }
          echo "</button>";
        }
      ?>
    </nav>
    <main>
      <?php
        if(isset($_GET['tabla'])){
          $tabla = $_GET['tabla'];
          $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
          $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);

          // Eliminación
          if(isset($_GET['operacion']) && $_GET['operacion'] == "eliminar" && isset($_GET['id'])){
            mysqli_query(
              $conexion,
              "DELETE FROM ".$tabla." WHERE Identificador = ".intval($_GET['id']).";"
            );
          }

          // Añadir / Insertar
          if(isset($_GET['operacion']) && $_GET['operacion'] == "añadir"){
            // Procesar inserción si viene por POST
            if($_SERVER['REQUEST_METHOD'] === 'POST'){
              $columnas = [];
              $valores  = [];

              foreach($columnMeta as $nombre_columna => $meta_columna){
                // Suponemos que Identificador es autoincremental
                if($nombre_columna == 'Identificador'){ continue; }

                $data_type  = strtolower($meta_columna['DATA_TYPE']);
                $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                // tinyint(1) como checkbox: si no viene en POST, lo consideramos 0
                if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                  $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                  $columnas[] = "`".$nombre_columna."`";
                  $valores[]  = intval($valor);
                  continue;
                }

                if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                  $columnas[] = "`".$nombre_columna."`";
                  $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                }
              }

              if(count($columnas) > 0){
                $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                mysqli_query($conexion, $sql_insert);
              }
            }

            // Formulario de alta
            echo "<h2>Añadir registro en ".$tabla."</h2>";
            echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";

            foreach($columnMeta as $nombre_columna => $meta_columna){
              // Omitimos el identificador
              if($nombre_columna == 'Identificador'){ continue; }

              // Si es FK: select con filas de la tabla relacionada
              if(isset($foreignKeys[$nombre_columna])){
                $fk = $foreignKeys[$nombre_columna];
                $tabla_fk   = $fk['tabla'];
                $columna_fk = $fk['columna'];

                echo "<label>".$nombre_columna."</label>";
                echo "<select name='".$nombre_columna."'>";
                echo "<option value=''>-- seleccionar --</option>";

                $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                if($res_fk){
                  while($fila_fk = mysqli_fetch_assoc($res_fk)){
                    $partes = [];
                    foreach($fila_fk as $k2=>$v2){
                      $partes[] = $v2;
                    }
                    $texto_opcion = implode(" | ", $partes);
                    $value_opcion = $fila_fk[$columna_fk];
                    echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                  }
                }

                echo "</select>";
              }else{
                // Campo normal: se elige tipo de input según DATA_TYPE
                echo render_input_para_columna($nombre_columna, $meta_columna);
              }
            }

            echo "<input type='submit' value='Guardar'>";
            echo "</form>";

          }else{
            // Listado
            echo "<h2>Listado de ".$tabla."</h2>";
            echo "<table>";
            $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
            $contador = 0;
            while($fila = mysqli_fetch_assoc($resultado)){
              if($contador == 0){
                echo "<tr>";
                  foreach($fila as $clave=>$valor){
                    echo "<th>".$clave."</th>";
                  }
                  echo "<th></th>";
                echo "</tr>";
              }

              echo "<tr>";
              foreach($fila as $clave=>$valor){
                // Si el campo es FK, mostramos fila de la tabla referenciada
                if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                  $fk = $foreignKeys[$clave];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  $sql_fk = "
                    SELECT *
                    FROM ".$tabla_fk."
                    WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                    LIMIT 1
                  ";
                  $res_fk = mysqli_query($conexion, $sql_fk);
                  if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                    $partes = [];
                    foreach($fila_fk as $k2=>$v2){
                      $partes[] = $v2;
                    }
                    $texto_celda = implode(" | ", $partes);
                    echo "<td>".$texto_celda."</td>";
                  }else{
                    // Si no encontramos la fila referenciada, mostramos el valor bruto
                    echo "<td>".$valor."</td>";
                  }
                }else{
                  // Campo normal
                  echo "<td>".$valor."</td>";
                }
              }

              // Columna de eliminar
              echo "<td><a href='?operacion=eliminar&tabla=".$tabla."&id=".$fila['Identificador']."' class='eliminar'>x</a></td>";
              echo "</tr>";

              $contador++;
            }
            echo "</table>";
          }
        }
      ?>
    </main>
  </body>
</html>
```

### con usuarios

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "empresarial";
$db_user = "usuarioempresarial";
$db_pass = "usuarioempresarial";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: ?");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: ?");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * Devuelve las claves foráneas de una tabla como:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Devuelve metadatos de columnas de una tabla como:
 * [
 *   'campo' => [
 *      'COLUMN_NAME' => ...,
 *      'DATA_TYPE'   => ...,
 *      'IS_NULLABLE' => ...,
 *      'COLUMN_DEFAULT' => ...,
 *      'COLUMN_KEY'  => ...,
 *      'EXTRA'       => ...,
 *      'CHARACTER_MAXIMUM_LENGTH' => ...,
 *      'COLUMN_TYPE' => ...,
 *   ],
 *   ...
 * ]
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Genera el control de formulario HTML adecuado para una columna NO FK.
 * Tiene en cuenta el DATA_TYPE de MySQL y mapea a tipos HTML.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      // datetime-local espera formato 'YYYY-MM-DDThh:mm'
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos (blob, binary, etc.) -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;align-items:center;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);overflow:auto;}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);vertical-align:top;}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;text-align:left;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);align-items:center;justify-content:space-between;}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;margin:0;}
      .logout{background:aliceblue;color:var(--color_primario);padding:6px 10px;border-radius:var(--radio);text-decoration:none;font-size:12px;font-weight:bold;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;animation:aparece 1s;text-align:center;text-decoration:none;display:inline-block;}
      form{columns:2;gap:var(--margen);}
      form label{display:block;font-weight:bold;margin-bottom:4px;}
      form input,form select{width:100%;padding:var(--margen);box-sizing:border-box;margin-bottom:var(--margen);border:1px solid var(--color_primario);border-radius:var(--radio);}
      form input[type=checkbox]{width:auto;padding:0;margin-top:5px;}
      form input[type=submit]{background:var(--color_primario);color:white;cursor:pointer;}
      @keyframes aparece{0%{opacity:0;transform:translateX(-30px);}100%{opacity:1;transform:translateX(0px);}}
      .eliminar{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;display:block;text-decoration:none;text-align:center;}

      /* Caja de login reutilizando estilos */
      .login-box{
        max-width:400px;
        margin:80px auto;
        background:white;
        padding:var(--margen);
        border-radius:var(--radio);
        border:1px solid var(--color_primario);
        box-shadow:0 0 10px rgba(0,0,0,0.1);
        column-count:1;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
      }
      .login-box form{
        columns:1;
      }
      .login-error{
        background:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
      }
      .login-user-label{
        font-size:12px;
        color:white;
        opacity:0.8;
        margin-left:8px;
      }
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo">
        <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
          <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
          <p>jocarsa</p>
        </div>
        <?php if($logged_in): ?>
          <div>
            <span class="login-user-label"><?php echo htmlspecialchars($_SESSION['usuario']); ?></span>
            <a href="?logout=1" class="logout">Salir</a>
          </div>
        <?php endif; ?>
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual) ? "activo" : "";
            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual){
                echo "<a href='?operacion=añadir&tabla=".$tabla_actual."' class='anadir'>+</a>";
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> mostrar login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {
          // Lógica del microERP (solo si logueado)
          if(isset($_GET['tabla'])){
            $tabla = $_GET['tabla'];
            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);

            // Eliminación
            if(isset($_GET['operacion']) && $_GET['operacion'] == "eliminar" && isset($_GET['id'])){
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE Identificador = ".intval($_GET['id']).";"
              );
            }

            // Añadir / Insertar
            if(isset($_GET['operacion']) && $_GET['operacion'] == "añadir"){
              // Procesar inserción si viene por POST
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  // Suponemos que Identificador es autoincremental
                  if($nombre_columna == 'Identificador'){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  // tinyint(1) como checkbox: si no viene en POST, lo consideramos 0
                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              // Formulario de alta
              echo "<h2>Añadir registro en ".$tabla."</h2>";
              echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";

              foreach($columnMeta as $nombre_columna => $meta_columna){
                // Omitimos el identificador
                if($nombre_columna == 'Identificador'){ continue; }

                // Si es FK: select con filas de la tabla relacionada
                if(isset($foreignKeys[$nombre_columna])){
                  $fk = $foreignKeys[$nombre_columna];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  echo "<label>".$nombre_columna."</label>";
                  echo "<select name='".$nombre_columna."'>";
                  echo "<option value=''>-- seleccionar --</option>";

                  $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                  if($res_fk){
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_opcion = implode(" | ", $partes);
                      $value_opcion = $fila_fk[$columna_fk];
                      echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                    }
                  }

                  echo "</select>";
                }else{
                  // Campo normal: se elige tipo de input según DATA_TYPE
                  echo render_input_para_columna($nombre_columna, $meta_columna);
                }
              }

              echo "<input type='submit' value='Guardar'>";
              echo "</form>";

            }else{
              // Listado
              echo "<h2>Listado de ".$tabla."</h2>";
              echo "<table>";
              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $contador = 0;
              while($fila = mysqli_fetch_assoc($resultado)){
                if($contador == 0){
                  echo "<tr>";
                    foreach($fila as $clave=>$valor){
                      echo "<th>".$clave."</th>";
                    }
                    echo "<th></th>";
                  echo "</tr>";
                }

                echo "<tr>";
                foreach($fila as $clave=>$valor){
                  // Si el campo es FK, mostramos fila de la tabla referenciada
                  if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                    $fk = $foreignKeys[$clave];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    $sql_fk = "
                      SELECT *
                      FROM ".$tabla_fk."
                      WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                      LIMIT 1
                    ";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_celda = implode(" | ", $partes);
                      echo "<td>".$texto_celda."</td>";
                    }else{
                      // Si no encontramos la fila referenciada, mostramos el valor bruto
                      echo "<td>".$valor."</td>";
                    }
                  }else{
                    // Campo normal
                    echo "<td>".$valor."</td>";
                  }
                }

                // Columna de eliminar
                echo "<td><a href='?operacion=eliminar&tabla=".$tabla."&id=".$fila['Identificador']."' class='eliminar'>x</a></td>";
                echo "</tr>";

                $contador++;
              }
              echo "</table>";
            }
          } else {
            // Pantalla inicial si está logueado pero no hay tabla seleccionada
            echo "<h2>Bienvenido a microERP</h2>";
            echo "<p>Selecciona una tabla en el menú de la izquierda para comenzar.</p>";
          }
        }
      ?>
    </main>
  </body>
</html>
```

### actualizacion informes y graficas

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "empresarial";
$db_user = "usuarioempresarial";
$db_pass = "usuarioempresarial";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: index.php");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: index.php");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * FKs salientes desde una tabla:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Metadatos de columnas de una tabla:
 * [
 *   'campo' => [
 *      'COLUMN_NAME' => ...,
 *      'DATA_TYPE'   => ...,
 *      'IS_NULLABLE' => ...,
 *      'COLUMN_DEFAULT' => ...,
 *      'COLUMN_KEY'  => ...,
 *      'EXTRA'       => ...,
 *      'CHARACTER_MAXIMUM_LENGTH' => ...,
 *      'COLUMN_TYPE' => ...,
 *   ],
 *   ...
 * ]
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Tablas que referencian a una tabla dada (FK entrantes):
 * [
 *   ['tabla' => 'lineas', 'columna' => 'id_cabecera'],
 *   ...
 * ]
 */
function obtener_tablas_que_referencian($conexion, $tabla_referenciada, $bd){
  $refs = [];
  $sql = "
    SELECT TABLE_NAME, COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND REFERENCED_TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla_referenciada)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $refs[] = [
        'tabla'   => $fila['TABLE_NAME'],
        'columna' => $fila['COLUMN_NAME']
      ];
    }
  }
  return $refs;
}

/**
 * Control de formulario adecuado para una columna NO FK.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      // datetime-local espera formato 'YYYY-MM-DDThh:mm'
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
      :root{--margen: 20px;--color_primario: indigo;--radio: 5px;}
      html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;padding:var(--margen);display:flex;flex-direction:column;gap:var(--margen);}
      nav>button{background:aliceblue;color:var(--color_primario);text-decoration:none;padding:calc(var(--margen)/2);border-radius:var(--radio);border:none;display:flex;justify-content: space-between;align-items:center;}
      nav button a{text-decoration:none;color:inherit;}
      main{background:aliceblue;flex:6;padding:var(--margen);overflow:auto;}
      main table{width:100%;border:3px solid var(--color_primario);border-collapse:collapse;}
      main table tr:nth-child(even){background:white;}
      main table td{padding:calc(var(--margen)/2);vertical-align:top;}
      main table th{background:var(--color_primario);padding:calc(var(--margen)/2);color:aliceblue;text-align:left;}
      .activo{width:120%;}
      #corporativo{display:flex;color:white;gap:calc(var(--margen)/2);align-items:center;justify-content:space-between;}
      #corporativo img{width:50px;}
      #corporativo p{font-size:30px;margin:0;}
      .logout{background:aliceblue;color:var(--color_primario);padding:6px 10px;border-radius:var(--radio);text-decoration:none;font-size:12px;font-weight:bold;}
      .anadir{width:20px;height:20px;background:var(--color_primario);color:white;border-radius:50px;line-height:20px;font-weight:bold;position:relative;z-index:100000;animation:aparece 1s;text-align:center;text-decoration:none;display:inline-block;}
      form{columns:2;gap:var(--margen);}
      form label{display:block;font-weight:bold;margin-bottom:4px;}
      form input,form select{width:100%;padding:var(--margen);box-sizing:border-box;margin-bottom:var(--margen);border:1px solid var(--color_primario);border-radius:var(--radio);}
      form input[type=checkbox]{width:auto;padding:0;margin-top:5px;}
      form input[type=submit]{background:var(--color_primario);color:white;cursor:pointer;}
      @keyframes aparece{0%{opacity:0;transform:translateX(-30px);}100%{opacity:1;transform:translateX(0px);}}
      .eliminar,
      .editar,
      .reportar{
        display:inline-block;
        width:20px;
        height:20px;
        border-radius:50px;
        line-height:20px;
        font-weight:bold;
        text-align:center;
        text-decoration:none;
        color:white;
        margin-left:5px;
        background:var(--color_primario);
      }
      .editar{background:darkorange;}
      .reportar{background:seagreen;}
      .login-box{
        max-width:400px;
        margin:80px auto;
        background:white;
        padding:var(--margen);
        border-radius:var(--radio);
        border:1px solid var(--color_primario);
        box-shadow:0 0 10px rgba(0,0,0,0.1);
        column-count:1;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
      }
      .login-box form{
        columns:1;
      }
      .login-error{
        background:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
      }
      .login-user-label{
        font-size:12px;
        color:white;
        opacity:0.8;
        margin-left:8px;
      }

      /* Dashboard charts */
      .dashboard-intro{
        margin-bottom:var(--margen);
      }
      .charts-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
        gap:var(--margen);
      }
      .chart{
        background:white;
        border-radius:var(--radio);
        border:1px solid var(--color_primario);
        padding:var(--margen);
        box-sizing:border-box;
      }
      .chart h3{
        margin-top:0;
        margin-bottom:10px;
        font-size:16px;
        color:var(--color_primario);
      }
      .chart-bars{
        display:flex;
        flex-direction:column;
        gap:6px;
      }
      .chart-bar{
        position:relative;
        height:24px;
        background:rgba(75,0,130,0.1);
        border-radius:12px;
        overflow:hidden;
      }
      .chart-fill{
        height:100%;
        background:var(--color_primario);
        opacity:0.7;
      }
      .chart-label{
        position:absolute;
        left:8px;
        top:3px;
        font-size:12px;
        color:white;
        text-shadow:0 0 3px rgba(0,0,0,0.5);
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
        right:4px;
      }
      .back-link{
        margin-bottom:var(--margen);
        display:inline-block;
        text-decoration:none;
        color:var(--color_primario);
        font-size:14px;
      }
      .back-link::before{
        content:"← ";
      }
      .subsection{
        margin-top:var(--margen);
      }
      .subsection h3{
        margin-bottom:6px;
      }
      .subsection table{
        margin-bottom:var(--margen);
      }
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo">
        <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
          <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
          <p>jocarsa</p>
        </div>
        <?php if($logged_in): ?>
          <div>
            <span class="login-user-label"><?php echo htmlspecialchars($_SESSION['usuario']); ?></span>
            <a href="?logout=1" class="logout">Salir</a>
          </div>
        <?php endif; ?>
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual) ? "activo" : "";
            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual){
                echo "<a href='?operacion=añadir&tabla=".$tabla_actual."' class='anadir'>+</a>";
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {
          // Lógica del microERP
          if(isset($_GET['tabla'])){
            $tabla      = $_GET['tabla'];
            $operacion  = $_GET['operacion'] ?? '';
            $id         = isset($_GET['id']) ? intval($_GET['id']) : null;

            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);

            // Eliminación
            if($operacion === "eliminar" && $id !== null){
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE Identificador = ".$id.";"
              );
              // Tras borrar, volvemos al listado
              $operacion = '';
            }

            // AÑADIR
            if($operacion === "añadir"){
              // Procesar inserción si viene por POST
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($nombre_columna == 'Identificador'){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  // tinyint(1) checkbox
                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              // Formulario de alta
              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
              echo "<h2>Añadir registro en ".$tabla."</h2>";
              echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";

              foreach($columnMeta as $nombre_columna => $meta_columna){
                if($nombre_columna == 'Identificador'){ continue; }

                // FK: select
                if(isset($foreignKeys[$nombre_columna])){
                  $fk = $foreignKeys[$nombre_columna];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  echo "<label>".$nombre_columna."</label>";
                  echo "<select name='".$nombre_columna."'>";
                  echo "<option value=''>-- seleccionar --</option>";

                  $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                  if($res_fk){
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_opcion = implode(" | ", $partes);
                      $value_opcion = $fila_fk[$columna_fk];
                      echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                    }
                  }

                  echo "</select>";
                }else{
                  echo render_input_para_columna($nombre_columna, $meta_columna);
                }
              }

              echo "<input type='submit' value='Guardar'>";
              echo "</form>";

            // EDITAR
            } elseif($operacion === "editar" && $id !== null){

              // Cargamos la fila actual
              $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE Identificador = ".$id." LIMIT 1;");
              $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

              if(!$fila_actual){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>No se ha encontrado el registro a editar.</p>";
              } else {
                // Procesar actualización
                if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                  $sets = [];

                  foreach($columnMeta as $nombre_columna => $meta_columna){
                    if($nombre_columna == 'Identificador'){ continue; }

                    $data_type   = strtolower($meta_columna['DATA_TYPE']);
                    $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                    // tinyint(1) checkbox
                    if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                      $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                      $sets[] = "`".$nombre_columna."`=".intval($valor);
                      continue;
                    }

                    if(isset($_POST[$nombre_columna])){
                      $valor = $_POST[$nombre_columna];
                      $sets[] = "`".$nombre_columna."` = '".mysqli_real_escape_string($conexion,$valor)."'";
                    }
                  }

                  if(count($sets) > 0){
                    $sql_update = "UPDATE ".$tabla." SET ".implode(", ",$sets)." WHERE Identificador = ".$id;
                    mysqli_query($conexion, $sql_update);
                  }

                  // Recargar fila actualizada
                  $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE Identificador = ".$id." LIMIT 1;");
                  $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : $fila_actual;
                }

                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<h2>Editar registro en ".$tabla." (ID ".$id.")</h2>";
                echo "<form action='?operacion=editar&tabla=".$tabla."&id=".$id."' method='POST'>";

                // Opcional: mostramos Identificador como solo lectura
                if(isset($fila_actual['Identificador'])){
                  echo "<label>Identificador</label>";
                  echo "<input type='text' value='".htmlspecialchars($fila_actual['Identificador'],ENT_QUOTES)."' disabled>";
                }

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($nombre_columna == 'Identificador'){ continue; }
                  $valor_actual = $fila_actual[$nombre_columna] ?? "";

                  if(isset($foreignKeys[$nombre_columna])){
                    $fk = $foreignKeys[$nombre_columna];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    echo "<label>".$nombre_columna."</label>";
                    echo "<select name='".$nombre_columna."'>";
                    echo "<option value=''>-- seleccionar --</option>";

                    $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                    if($res_fk){
                      while($fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $texto_opcion = implode(" | ", $partes);
                        $value_opcion = $fila_fk[$columna_fk];
                        $selected = ($valor_actual == $value_opcion) ? "selected" : "";
                        echo "<option value='".$value_opcion."' ".$selected.">".$texto_opcion."</option>";
                      }
                    }

                    echo "</select>";
                  }else{
                    echo render_input_para_columna($nombre_columna, $meta_columna, $valor_actual);
                  }
                }

                echo "<input type='submit' value='Guardar cambios'>";
                echo "</form>";
              }

            // INFORME
            } elseif($operacion === "report" && $id !== null){

              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

              // Fila actual
              $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE Identificador = ".$id." LIMIT 1;");
              $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

              if(!$fila_actual){
                echo "<p>No se ha encontrado el registro solicitado.</p>";
              } else {
                echo "<h2>Informe de ".$tabla." (ID ".$id.")</h2>";

                // Tabla principal
                echo "<div class='subsection'>";
                echo "<h3>Registro principal</h3>";
                echo "<table>";
                echo "<tr>";
                foreach($fila_actual as $clave=>$valor){
                  echo "<th>".$clave."</th>";
                }
                echo "</tr><tr>";
                foreach($fila_actual as $clave=>$valor){
                  echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                }
                echo "</tr></table>";
                echo "</div>";

                // Datos que este registro referencia (FK salientes)
                echo "<div class='subsection'>";
                echo "<h3>Datos referenciados por este registro</h3>";

                $hay_referenciados = false;
                foreach($foreignKeys as $columna_fk_local => $info_fk){
                  $valor_fk = $fila_actual[$columna_fk_local] ?? null;
                  if($valor_fk === null || $valor_fk === ''){ continue; }

                  $tabla_fk   = $info_fk['tabla'];
                  $col_fk     = $info_fk['columna'];

                  $sql_fk = "SELECT * FROM ".$tabla_fk." WHERE ".$col_fk." = '".mysqli_real_escape_string($conexion,$valor_fk)."'";
                  $res_fk = mysqli_query($conexion, $sql_fk);
                  if($res_fk && mysqli_num_rows($res_fk) > 0){
                    $hay_referenciados = true;
                    echo "<h4>".$tabla_fk." (por ".$columna_fk_local.")</h4>";
                    echo "<table>";
                    $primera = true;
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      if($primera){
                        echo "<tr>";
                        foreach($fila_fk as $k=>$v){ echo "<th>".$k."</th>"; }
                        echo "</tr>";
                        $primera = false;
                      }
                      echo "<tr>";
                      foreach($fila_fk as $k=>$v){
                        echo "<td>".htmlspecialchars($v,ENT_QUOTES)."</td>";
                      }
                      echo "</tr>";
                    }
                    echo "</table>";
                  }
                }
                if(!$hay_referenciados){
                  echo "<p>No hay referencias salientes.</p>";
                }
                echo "</div>";

                // Tablas que referencian a este registro (FK entrantes)
                echo "<div class='subsection'>";
                echo "<h3>Datos relacionados que apuntan a este registro</h3>";

                $refs_entrantes = obtener_tablas_que_referencian($conexion, $tabla, $db_name);
                if(count($refs_entrantes) === 0){
                  echo "<p>No hay tablas que referencien a esta entidad.</p>";
                } else {
                  $hay_entrantes = false;
                  foreach($refs_entrantes as $ref){
                    $tabla_hija   = $ref['tabla'];
                    $columna_hija = $ref['columna'];

                    $sql_hija = "SELECT * FROM ".$tabla_hija." WHERE ".$columna_hija." = ".$id;
                    $res_hija = mysqli_query($conexion, $sql_hija);
                    if($res_hija && mysqli_num_rows($res_hija) > 0){
                      $hay_entrantes = true;
                      echo "<h4>".$tabla_hija." (columna ".$columna_hija.")</h4>";
                      echo "<table>";
                      $primera = true;
                      while($fila_hija = mysqli_fetch_assoc($res_hija)){
                        if($primera){
                          echo "<tr>";
                          foreach($fila_hija as $k=>$v){ echo "<th>".$k."</th>"; }
                          echo "</tr>";
                          $primera = false;
                        }
                        echo "<tr>";
                        foreach($fila_hija as $k=>$v){
                          echo "<td>".htmlspecialchars($v,ENT_QUOTES)."</td>";
                        }
                        echo "</tr>";
                      }
                      echo "</table>";
                    }
                  }
                  if(!$hay_entrantes){
                    echo "<p>No hay registros entrantes que apunten a este ID.</p>";
                  }
                }

                echo "</div>";
              }

            // LISTADO
            } else {
              echo "<h2>Listado de ".$tabla."</h2>";
              echo "<table>";
              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $contador = 0;
              while($fila = mysqli_fetch_assoc($resultado)){
                if($contador == 0){
                  echo "<tr>";
                    foreach($fila as $clave=>$valor){
                      echo "<th>".$clave."</th>";
                    }
                    echo "<th>Acciones</th>";
                  echo "</tr>";
                }

                echo "<tr>";
                foreach($fila as $clave=>$valor){
                  // Si es FK, mostramos fila referenciada
                  if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                    $fk = $foreignKeys[$clave];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    $sql_fk = "
                      SELECT *
                      FROM ".$tabla_fk."
                      WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                      LIMIT 1
                    ";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_celda = implode(" | ", $partes);
                      echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
                    }else{
                      echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                    }
                  }else{
                    echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                  }
                }

                // Acciones: editar, informe, eliminar
                $id_fila = isset($fila['Identificador']) ? intval($fila['Identificador']) : 0;
                echo "<td>";
                echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_fila."' class='editar'>✏</a>";
                echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_fila."' class='reportar'>i</a>";
                echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_fila."' class='eliminar'>x</a>";
                echo "</td>";

                echo "</tr>";

                $contador++;
              }
              echo "</table>";
            }
          } else {
            // DASHBOARD INICIAL: gráficos de campos ENUM/SET en todas las tablas
            echo "<h2>Dashboard de microERP</h2>";
            echo "<p class='dashboard-intro'>Resumen gráfico de los campos categóricos (ENUM/SET) de todas las tablas.</p>";

            $resultado = mysqli_query($conexion, "SHOW TABLES;");
            echo "<div class='charts-grid'>";
            while($fila = mysqli_fetch_assoc($resultado)){
              $tabla = array_values($fila)[0];
              $meta  = obtener_meta_columnas($conexion, $tabla, $db_name);

              // Buscar columnas ENUM/SET
              foreach($meta as $nombre_columna => $meta_columna){
                $data_type = strtolower($meta_columna['DATA_TYPE']);
                if($data_type !== 'enum' && $data_type !== 'set'){ continue; }

                // Sacar distribución
                $sql_dist = "
                  SELECT ".$nombre_columna." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$nombre_columna."
                  ORDER BY total DESC
                ";
                $res_dist = mysqli_query($conexion, $sql_dist);
                if(!$res_dist || mysqli_num_rows($res_dist) < 1){ continue; }

                $valores = [];
                $max = 0;
                $total_registros = 0;
                while($fila_dist = mysqli_fetch_assoc($res_dist)){
                  $v = $fila_dist['valor'];
                  $c = (int)$fila_dist['total'];
                  $valores[] = ['valor' => $v, 'total' => $c];
                  $total_registros += $c;
                  if($c > $max){ $max = $c; }
                }
                if($max == 0){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$nombre_columna."</h3>";
                echo "<div class='chart-bars'>";
                foreach($valores as $dato){
                  $v = $dato['valor'] === null || $dato['valor'] === '' ? '(vacío)' : $dato['valor'];
                  $c = $dato['total'];
                  $width = round(($c / $max) * 100, 2);
                  $label = htmlspecialchars($v,ENT_QUOTES)." (".$c.")";
                  echo "<div class='chart-bar'>";
                  echo "<div class='chart-fill' style='width:".$width."%;'></div>";
                  echo "<div class='chart-label'>".$label."</div>";
                  echo "</div>";
                }
                echo "</div>";
                echo "</div>";
              }
            }
            echo "</div>";
          }
        }
      ?>
    </main>
  </body>
</html>
```

### mejoras

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "tienda2526";
$db_user = "tienda2526";
$db_pass = "tienda2526";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: index.php");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: index.php");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * FKs salientes desde una tabla:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Metadatos de columnas de una tabla.
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Tablas que referencian a una tabla dada (FK entrantes)
 */
function obtener_tablas_que_referencian($conexion, $tabla_referenciada, $bd){
  $refs = [];
  $sql = "
    SELECT TABLE_NAME, COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND REFERENCED_TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla_referenciada)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $refs[] = [
        'tabla'   => $fila['TABLE_NAME'],
        'columna' => $fila['COLUMN_NAME']
      ];
    }
  }
  return $refs;
}

/**
 * Control de formulario adecuado para una columna NO FK.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      // datetime-local espera formato 'YYYY-MM-DDThh:mm'
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}

/**
 * Renderizar tabla HTML de resultados usando la misma lógica de FKs
 * que el listado principal (para los informes).
 */
function render_tabla_html_con_links($conexion, $tabla, $rows, $bd){
  if(!$rows || count($rows) === 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }
  $foreignKeysLocal = obtener_claves_foraneas($conexion, $tabla, $bd);

  echo "<table class='report-table'>";
  // Cabecera
  $first = $rows[0];
  echo "<tr>";
  foreach($first as $k => $_){
    echo "<th>".$k."</th>";
  }
  echo "</tr>";

  // Filas
  foreach($rows as $fila){
    echo "<tr>";
    foreach($fila as $clave=>$valor){
      if(isset($foreignKeysLocal[$clave]) && $valor !== null && $valor !== ''){
        $fk = $foreignKeysLocal[$clave];
        $tabla_fk   = $fk['tabla'];
        $columna_fk = $fk['columna'];

        $sql_fk = "
          SELECT *
          FROM ".$tabla_fk."
          WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
          LIMIT 1
        ";
        $res_fk = mysqli_query($conexion, $sql_fk);
        if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
          $partes = [];
          foreach($fila_fk as $k2=>$v2){
            $partes[] = $v2;
          }
          $texto_celda = implode(" | ", $partes);
          echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
        }else{
          echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
        }
      }else{
        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
      }
    }
    echo "</tr>";
  }

  echo "</table>";
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
      :root{
        --margen: 20px;
        --color_primario: indigo;
        --color_primario_suave: rgba(75,0,130,0.08);
        --color_secundario: aliceblue;
        --radio: 8px;
      }
      *{
        box-sizing:border-box;
      }
      html,body{
        width:100%;
        height:100%;
        padding:0;
        margin:0;
        font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      body{
        display:flex;
        background:linear-gradient(135deg, #f5f7ff 0%, #e8f0ff 50%, #fdfdff 100%);
        color:#222;
      }
      /* NAV LATERAL */
      nav{
        flex:1;
        min-width:240px;
        max-width:320px;
        padding:var(--margen);
        display:flex;
        flex-direction:column;
        gap:var(--margen);
        background:radial-gradient(circle at top left,#4b0082 0%,#2b004d 40%,#120024 100%);
        box-shadow:4px 0 20px rgba(0,0,0,0.25);
        color:white;
        position:relative;
        z-index:2;
      }
      #corporativo{
        display:flex;
        color:white;
        gap:calc(var(--margen)/2);
        align-items:center;
        justify-content:space-between;
        padding-bottom:var(--margen);
        border-bottom:1px solid rgba(255,255,255,0.15);
      }
      #corporativo img{
        width:56px;
        filter:drop-shadow(0 0 6px rgba(255,255,255,0.3));
      }
      #corporativo p{
        font-size:26px;
        margin:0;
        font-weight:700;
        letter-spacing:1px;
        text-shadow:0 0 6px rgba(0,0,0,0.3);
      }
      .logout{
        background:rgba(240,248,255,0.2);
        color:aliceblue;
        padding:6px 12px;
        border-radius:999px;
        text-decoration:none;
        font-size:12px;
        font-weight:600;
        border:1px solid rgba(240,248,255,0.4);
        transition:all 0.2s ease;
      }
      .logout:hover{
        background:aliceblue;
        color:var(--color_primario);
      }
      .login-user-label{
        font-size:11px;
        color:aliceblue;
        opacity:0.85;
        margin-right:6px;
      }

      nav>button{
        background:rgba(240,248,255,0.06);
        color:var(--color_secundario);
        padding:10px 12px;
        border-radius:var(--radio);
        border:1px solid transparent;
        display:flex;
        justify-content: space-between;
        align-items:center;
        cursor:pointer;
        transition:all 0.2s ease;
      }
      nav>button:hover{
        background:rgba(240,248,255,0.16);
        border-color:rgba(240,248,255,0.3);
        transform:translateX(2px);
      }
      .activo{
        background:rgba(240,248,255,0.25);
        border-color:rgba(240,248,255,0.7);
        transform:translateX(4px);
        box-shadow:0 0 10px rgba(240,248,255,0.4);
      }
      nav button a{
        text-decoration:none;
        color:inherit;
        font-size:13px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
      }
      .anadir{
        width:22px;
        height:22px;
        background:aliceblue;
        color:var(--color_primario);
        border-radius:50%;
        line-height:22px;
        font-weight:bold;
        text-align:center;
        text-decoration:none;
        display:inline-block;
        box-shadow:0 0 6px rgba(0,0,0,0.3);
      }

      /* MAIN / DASHBOARD */
      main{
        flex:6;
        padding:var(--margen);
        overflow:auto;
        background:radial-gradient(circle at top,rgba(240,248,255,0.7) 0%,rgba(230,235,255,0.9) 40%,#f9fbff 100%);
        position:relative;
      }
      main::before{
        content:"";
        position:absolute;
        inset:0;
        background:radial-gradient(circle at bottom right,rgba(75,0,130,0.08) 0%,transparent 55%);
        pointer-events:none;
        z-index:-1;
      }
      h2{
        margin-top:0;
        margin-bottom:10px;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }

      /* TABLAS */
      main table{
        width:100%;
        border:1px solid rgba(75,0,130,0.2);
        border-collapse:collapse;
        border-radius:var(--radio);
        overflow:hidden;
        background:white;
        box-shadow:0 4px 14px rgba(0,0,0,0.06);
      }
      main table tr:nth-child(even){
        background:#f9f9ff;
      }
      main table tr:hover{
        background:#eef2ff;
      }
      main table td{
        padding:10px 12px;
        vertical-align:top;
        font-size:13px;
      }
      main table th{
        background:linear-gradient(90deg,var(--color_primario),#7b3fb0);
        padding:10px 12px;
        color:aliceblue;
        text-align:left;
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:0.7px;
      }

      .report-table{
        margin-bottom:var(--margen);
      }
      .no-data{
        font-size:13px;
        color:#666;
      }

      /* ACCIONES */
      .eliminar,
      .editar,
      .reportar{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:24px;
        height:24px;
        border-radius:999px;
        text-decoration:none;
        color:white;
        margin-left:4px;
        font-size:12px;
        box-shadow:0 0 6px rgba(0,0,0,0.25);
        transition:transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
      }
      .eliminar{
        background:#c0392b;
      }
      .editar{
        background:#e67e22;
      }
      .reportar{
        background:#16a085;
      }
      .eliminar:hover,
      .editar:hover,
      .reportar:hover{
        transform:translateY(-1px) scale(1.03);
        box-shadow:0 0 10px rgba(0,0,0,0.35);
        opacity:0.95;
      }

      @keyframes aparece{
        0%{opacity:0;transform:translateX(-30px);}
        100%{opacity:1;transform:translateX(0px);}
      }

      /* FORMULARIOS */
      form{
        columns:2;
        gap:var(--margen);
        margin-top:10px;
      }
      form label{
        display:block;
        font-weight:600;
        margin-bottom:4px;
        font-size:12px;
        color:#444;
      }
      form input,
      form select{
        width:100%;
        padding:10px 12px;
        box-sizing:border-box;
        margin-bottom:var(--margen);
        border:1px solid rgba(75,0,130,0.3);
        border-radius:var(--radio);
        background:rgba(255,255,255,0.9);
        font-size:13px;
        transition:border 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
      }
      form input:focus,
      form select:focus{
        outline:none;
        border-color:var(--color_primario);
        box-shadow:0 0 0 2px rgba(75,0,130,0.15);
        background:white;
      }
      form input[type=checkbox]{
        width:auto;
        padding:0;
        margin-top:5px;
        box-shadow:none;
      }
      form input[type=submit]{
        background:linear-gradient(90deg,var(--color_primario),#7b3fb0);
        color:white;
        cursor:pointer;
        border:none;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.8px;
        box-shadow:0 4px 10px rgba(75,0,130,0.4);
      }
      form input[type=submit]:hover{
        box-shadow:0 5px 14px rgba(75,0,130,0.6);
        transform:translateY(-1px);
      }

      /* LOGIN */
      .login-box{
        max-width:420px;
        margin:80px auto;
        background:white;
        padding:var(--margen);
        border-radius:16px;
        border:1px solid rgba(75,0,130,0.2);
        box-shadow:0 14px 40px rgba(0,0,0,0.18);
        column-count:1;
        position:relative;
        overflow:hidden;
      }
      .login-box::before{
        content:"";
        position:absolute;
        inset:0;
        background:radial-gradient(circle at top,#eef0ff 0%,transparent 55%);
        opacity:0.9;
        pointer-events:none;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .login-box form{
        columns:1;
        position:relative;
        z-index:1;
      }
      .login-error{
        background:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
        position:relative;
        z-index:1;
      }

      /* DASHBOARD / CHARTS */
      .dashboard-intro{
        margin-bottom:var(--margen);
        font-size:14px;
        color:#555;
        max-width:700px;
      }
      .charts-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
        gap:var(--margen);
      }
      .chart{
        background:white;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-sizing:border-box;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        position:relative;
        overflow:hidden;
      }
      .chart::before{
        content:"";
        position:absolute;
        inset:0;
        background:radial-gradient(circle at top right,rgba(75,0,130,0.08) 0%,transparent 60%);
        pointer-events:none;
      }
      .chart h3{
        margin-top:0;
        margin-bottom:10px;
        font-size:15px;
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .chart-subtitle{
        font-size:11px;
        color:#777;
        margin-bottom:8px;
        position:relative;
        z-index:1;
      }
      .chart-bars{
        display:flex;
        flex-direction:column;
        gap:6px;
        position:relative;
        z-index:1;
      }
      .chart-bar{
        position:relative;
        height:24px;
        background:var(--color_primario_suave);
        border-radius:12px;
        overflow:hidden;
      }
      .chart-fill{
        height:100%;
        background:linear-gradient(90deg,var(--color_primario),#7b3fb0);
        opacity:0.85;
      }
      .chart-label{
        position:absolute;
        left:10px;
        top:4px;
        font-size:11px;
        color:white;
        text-shadow:0 0 3px rgba(0,0,0,0.4);
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
        right:6px;
      }

      .back-link{
        margin-bottom:var(--margen);
        display:inline-block;
        text-decoration:none;
        color:var(--color_primario);
        font-size:13px;
        padding:4px 8px;
        border-radius:999px;
        background:rgba(75,0,130,0.07);
      }
      .back-link::before{
        content:"← ";
      }
      .subsection{
        margin-top:var(--margen);
      }
      .subsection h3{
        margin-bottom:6px;
        color:#333;
      }
      .subsection h4{
        margin:8px 0 4px;
        font-size:13px;
        color:#555;
      }

      @media (max-width:900px){
        body{flex-direction:column;}
        nav{
          flex:none;
          max-width:none;
          box-shadow:0 4px 12px rgba(0,0,0,0.2);
        }
      }
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo">
        <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
          <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
          <p>jocarsa</p>
        </div>
        <?php if($logged_in): ?>
          <div>
            <span class="login-user-label"><?php echo htmlspecialchars($_SESSION['usuario']); ?></span>
            <a href="?logout=1" class="logout">Salir</a>
          </div>
        <?php endif; ?>
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual) ? "activo" : "";
            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual){
                echo "<a href='?operacion=añadir&tabla=".$tabla_actual."' class='anadir'>+</a>";
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {
          // Lógica del microERP
          if(isset($_GET['tabla'])){
            $tabla      = $_GET['tabla'];
            $operacion  = $_GET['operacion'] ?? '';
            $id         = isset($_GET['id']) ? intval($_GET['id']) : null;

            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);

            // Eliminación
            if($operacion === "eliminar" && $id !== null){
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE Identificador = ".$id.";"
              );
              $operacion = '';
            }

            // AÑADIR
            if($operacion === "añadir"){
              // Procesar inserción si viene por POST
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($nombre_columna == 'Identificador'){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  // tinyint(1) checkbox
                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              // Formulario de alta
              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
              echo "<h2>Añadir registro en ".$tabla."</h2>";
              echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";

              foreach($columnMeta as $nombre_columna => $meta_columna){
                if($nombre_columna == 'Identificador'){ continue; }

                // FK: select
                if(isset($foreignKeys[$nombre_columna])){
                  $fk = $foreignKeys[$nombre_columna];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  echo "<label>".$nombre_columna."</label>";
                  echo "<select name='".$nombre_columna."'>";
                  echo "<option value=''>-- seleccionar --</option>";

                  $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                  if($res_fk){
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_opcion = implode(" | ", $partes);
                      $value_opcion = $fila_fk[$columna_fk];
                      echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                    }
                  }

                  echo "</select>";
                }else{
                  echo render_input_para_columna($nombre_columna, $meta_columna);
                }
              }

              echo "<input type='submit' value='Guardar'>";
              echo "</form>";

            // EDITAR
            } elseif($operacion === "editar" && $id !== null){

              // Cargamos la fila actual
              $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE Identificador = ".$id." LIMIT 1;");
              $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

              if(!$fila_actual){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>No se ha encontrado el registro a editar.</p>";
              } else {
                // Procesar actualización
                if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                  $sets = [];

                  foreach($columnMeta as $nombre_columna => $meta_columna){
                    if($nombre_columna == 'Identificador'){ continue; }

                    $data_type   = strtolower($meta_columna['DATA_TYPE']);
                    $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                    // tinyint(1) checkbox
                    if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                      $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                      $sets[] = "`".$nombre_columna."`=".intval($valor);
                      continue;
                    }

                    if(isset($_POST[$nombre_columna])){
                      $valor = $_POST[$nombre_columna];
                      $sets[] = "`".$nombre_columna."` = '".mysqli_real_escape_string($conexion,$valor)."'";
                    }
                  }

                  if(count($sets) > 0){
                    $sql_update = "UPDATE ".$tabla." SET ".implode(", ",$sets)." WHERE Identificador = ".$id;
                    mysqli_query($conexion, $sql_update);
                  }

                  // Recargar fila actualizada
                  $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE Identificador = ".$id." LIMIT 1;");
                  $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : $fila_actual;
                }

                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<h2>Editar registro en ".$tabla." (ID ".$id.")</h2>";
                echo "<form action='?operacion=editar&tabla=".$tabla."&id=".$id."' method='POST'>";

                // Identificador como solo lectura
                if(isset($fila_actual['Identificador'])){
                  echo "<label>Identificador</label>";
                  echo "<input type='text' value='".htmlspecialchars($fila_actual['Identificador'],ENT_QUOTES)."' disabled>";
                }

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($nombre_columna == 'Identificador'){ continue; }
                  $valor_actual = $fila_actual[$nombre_columna] ?? "";

                  if(isset($foreignKeys[$nombre_columna])){
                    $fk = $foreignKeys[$nombre_columna];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    echo "<label>".$nombre_columna."</label>";
                    echo "<select name='".$nombre_columna."'>";
                    echo "<option value=''>-- seleccionar --</option>";

                    $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                    if($res_fk){
                      while($fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $texto_opcion = implode(" | ", $partes);
                        $value_opcion = $fila_fk[$columna_fk];
                        $selected = ($valor_actual == $value_opcion) ? "selected" : "";
                        echo "<option value='".$value_opcion."' ".$selected.">".$texto_opcion."</option>";
                      }
                    }

                    echo "</select>";
                  }else{
                    echo render_input_para_columna($nombre_columna, $meta_columna, $valor_actual);
                  }
                }

                echo "<input type='submit' value='Guardar cambios'>";
                echo "</form>";
              }

            // INFORME
            } elseif($operacion === "report" && $id !== null){

              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

              // Fila actual
              $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE Identificador = ".$id." LIMIT 1;");
              $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

              if(!$fila_actual){
                echo "<p>No se ha encontrado el registro solicitado.</p>";
              } else {
                echo "<h2>Informe de ".$tabla." (ID ".$id.")</h2>";

                // Registro principal (con misma lógica de FKs)
                echo "<div class='subsection'>";
                echo "<h3>Registro principal</h3>";
                render_tabla_html_con_links($conexion, $tabla, [$fila_actual], $db_name);
                echo "</div>";

                // Datos que este registro referencia (FK salientes)
                echo "<div class='subsection'>";
                echo "<h3>Datos referenciados por este registro</h3>";

                $hay_referenciados = false;
                foreach($foreignKeys as $columna_fk_local => $info_fk){
                  $valor_fk = $fila_actual[$columna_fk_local] ?? null;
                  if($valor_fk === null || $valor_fk === ''){ continue; }

                  $tabla_fk   = $info_fk['tabla'];
                  $col_fk     = $info_fk['columna'];

                  $sql_fk = "SELECT * FROM ".$tabla_fk." WHERE ".$col_fk." = '".mysqli_real_escape_string($conexion,$valor_fk)."'";
                  $res_fk = mysqli_query($conexion, $sql_fk);
                  if($res_fk && mysqli_num_rows($res_fk) > 0){
                    $hay_referenciados = true;
                    $rows_fk = [];
                    while($row_fk = mysqli_fetch_assoc($res_fk)){
                      $rows_fk[] = $row_fk;
                    }

                    echo "<h4>".$tabla_fk." (por ".$columna_fk_local.")</h4>";
                    render_tabla_html_con_links($conexion, $tabla_fk, $rows_fk, $db_name);
                  }
                }
                if(!$hay_referenciados){
                  echo "<p class='no-data'>No hay referencias salientes.</p>";
                }
                echo "</div>";

                // Tablas que referencian a este registro (FK entrantes)
                echo "<div class='subsection'>";
                echo "<h3>Datos relacionados que apuntan a este registro</h3>";

                $refs_entrantes = obtener_tablas_que_referencian($conexion, $tabla, $db_name);
                if(count($refs_entrantes) === 0){
                  echo "<p class='no-data'>No hay tablas que referencien a esta entidad.</p>";
                } else {
                  $hay_entrantes = false;
                  foreach($refs_entrantes as $ref){
                    $tabla_hija   = $ref['tabla'];
                    $columna_hija = $ref['columna'];

                    $sql_hija = "SELECT * FROM ".$tabla_hija." WHERE ".$columna_hija." = ".$id;
                    $res_hija = mysqli_query($conexion, $sql_hija);
                    if($res_hija && mysqli_num_rows($res_hija) > 0){
                      $hay_entrantes = true;
                      $rows_hija = [];
                      while($fila_hija = mysqli_fetch_assoc($res_hija)){
                        $rows_hija[] = $fila_hija;
                      }

                      echo "<h4>".$tabla_hija." (columna ".$columna_hija.")</h4>";
                      render_tabla_html_con_links($conexion, $tabla_hija, $rows_hija, $db_name);
                    }
                  }
                  if(!$hay_entrantes){
                    echo "<p class='no-data'>No hay registros entrantes que apunten a este ID.</p>";
                  }
                }

                echo "</div>";
              }

            // LISTADO
            } else {
              echo "<h2>Listado de ".$tabla."</h2>";
              echo "<table>";
              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $contador = 0;
              while($fila = mysqli_fetch_assoc($resultado)){
                if($contador == 0){
                  echo "<tr>";
                    foreach($fila as $clave=>$valor){
                      echo "<th>".$clave."</th>";
                    }
                    echo "<th>Acciones</th>";
                  echo "</tr>";
                }

                echo "<tr>";
                foreach($fila as $clave=>$valor){
                  // Si es FK, mostramos fila referenciada
                  if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                    $fk = $foreignKeys[$clave];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    $sql_fk = "
                      SELECT *
                      FROM ".$tabla_fk."
                      WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                      LIMIT 1
                    ";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_celda = implode(" | ", $partes);
                      echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
                    }else{
                      echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                    }
                  }else{
                    echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                  }
                }

                // Acciones: editar, informe, eliminar
                $id_fila = isset($fila['Identificador']) ? intval($fila['Identificador']) : 0;
                echo "<td>";
                echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_fila."' class='editar'>✏</a>";
                echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_fila."' class='reportar'>i</a>";
                echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_fila."' class='eliminar'>×</a>";
                echo "</td>";

                echo "</tr>";

                $contador++;
              }
              echo "</table>";
            }
          } else {
            // DASHBOARD INICIAL: gráficos de campos ENUM/SET y FKs
            echo "<h2>Dashboard de microERP</h2>";
            echo "<p class='dashboard-intro'>
              Resumen gráfico de la información categórica y relacional del sistema:
              campos <b>ENUM/SET</b> y campos de <b>clave foránea</b> en todas las tablas.
            </p>";

            $resultado = mysqli_query($conexion, "SHOW TABLES;");
            echo "<div class='charts-grid'>";
            while($fila = mysqli_fetch_assoc($resultado)){
              $tabla = array_values($fila)[0];
              $meta  = obtener_meta_columnas($conexion, $tabla, $db_name);
              $fksTabla = obtener_claves_foraneas($conexion, $tabla, $db_name);

              // 1) Campos ENUM/SET
              foreach($meta as $nombre_columna => $meta_columna){
                $data_type = strtolower($meta_columna['DATA_TYPE']);
                if($data_type !== 'enum' && $data_type !== 'set'){ continue; }

                $sql_dist = "
                  SELECT ".$nombre_columna." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$nombre_columna."
                  ORDER BY total DESC
                ";
                $res_dist = mysqli_query($conexion, $sql_dist);
                if(!$res_dist || mysqli_num_rows($res_dist) < 1){ continue; }

                $valores = [];
                $max = 0;
                while($fila_dist = mysqli_fetch_assoc($res_dist)){
                  $v = $fila_dist['valor'];
                  $c = (int)$fila_dist['total'];
                  $valores[] = [
                    'label' => ($v === null || $v === '' ? '(vacío)' : $v),
                    'total' => $c
                  ];
                  if($c > $max){ $max = $c; }
                }
                if($max == 0){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$nombre_columna."</h3>";
                echo "<div class='chart-subtitle'>Distribución de valores ENUM/SET</div>";
                echo "<div class='chart-bars'>";
                foreach($valores as $dato){
                  $label = $dato['label'];
                  $c     = $dato['total'];
                  $width = round(($c / $max) * 100, 2);
                  $text  = htmlspecialchars($label,ENT_QUOTES)." (".$c.")";
                  echo "<div class='chart-bar'>";
                  echo "<div class='chart-fill' style='width:".$width."%;'></div>";
                  echo "<div class='chart-label'>".$text."</div>";
                  echo "</div>";
                }
                echo "</div>";
                echo "</div>";
              }

              // 2) Campos FK: distribución por valor referenciado
              foreach($fksTabla as $columna_fk => $info_fk){
                $tabla_ref = $info_fk['tabla'];
                $col_ref   = $info_fk['columna'];

                $sql_dist_fk = "
                  SELECT ".$columna_fk." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$columna_fk."
                  ORDER BY total DESC
                ";
                $res_dist_fk = mysqli_query($conexion, $sql_dist_fk);
                if(!$res_dist_fk || mysqli_num_rows($res_dist_fk) < 1){ continue; }

                $valores_fk = [];
                $max_fk = 0;

                while($fila_dist = mysqli_fetch_assoc($res_dist_fk)){
                  $valor_fk = $fila_dist['valor'];
                  $c        = (int)$fila_dist['total'];

                  if($valor_fk === null || $valor_fk === ''){
                    $label = '(sin valor)';
                  }else{
                    // Miramos fila referenciada para label
                    $sql_ref = "
                      SELECT *
                      FROM ".$tabla_ref."
                      WHERE ".$col_ref." = '".mysqli_real_escape_string($conexion,$valor_fk)."'
                      LIMIT 1
                    ";
                    $res_ref = mysqli_query($conexion, $sql_ref);
                    if($res_ref && $fila_ref = mysqli_fetch_assoc($res_ref)){
                      $partes = [];
                      foreach($fila_ref as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $label = implode(" | ", $partes);
                    }else{
                      $label = 'ID '.$valor_fk.' (huérfano)';
                    }
                  }

                  $valores_fk[] = [
                    'label' => $label,
                    'total' => $c
                  ];
                  if($c > $max_fk){ $max_fk = $c; }
                }

                if($max_fk == 0){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$columna_fk."</h3>";
                echo "<div class='chart-subtitle'>Distribución por referencia a ".$tabla_ref."</div>";
                echo "<div class='chart-bars'>";
                foreach($valores_fk as $dato){
                  $label = $dato['label'];
                  $c     = $dato['total'];
                  $width = round(($c / $max_fk) * 100, 2);
                  $text  = htmlspecialchars($label,ENT_QUOTES)." (".$c.")";
                  echo "<div class='chart-bar'>";
                  echo "<div class='chart-fill' style='width:".$width."%;'></div>";
                  echo "<div class='chart-label'>".$text."</div>";
                  echo "</div>";
                }
                echo "</div>";
                echo "</div>";
              }
            }
            echo "</div>";
          }
        }
      ?>
    </main>
  </body>
</html>
```

### claves primarias dinamicas

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "tienda2526";
$db_user = "tienda2526";
$db_pass = "tienda2526";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: index.php");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: index.php");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * FKs salientes desde una tabla:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Metadatos de columnas de una tabla.
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Obtener nombre de la columna PK (primer PRIMARY KEY definido).
 * Devuelve null si la tabla no tiene PK.
 */
function obtener_pk_columna($conexion, $tabla, $bd){
  $sql = "
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND COLUMN_KEY = 'PRI'
    ORDER BY ORDINAL_POSITION
    LIMIT 1
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado && $fila = mysqli_fetch_assoc($resultado)){
    return $fila['COLUMN_NAME'];
  }
  return null;
}

/**
 * Tablas que referencian a una tabla dada (FK entrantes)
 * [
 *   ['tabla' => 'lineas', 'columna' => 'id_cabecera', 'columna_referenciada' => 'IdCabecera'],
 *   ...
 * ]
 */
function obtener_tablas_que_referencian($conexion, $tabla_referenciada, $bd){
  $refs = [];
  $sql = "
    SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND REFERENCED_TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla_referenciada)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $refs[] = [
        'tabla'                => $fila['TABLE_NAME'],
        'columna'              => $fila['COLUMN_NAME'],
        'columna_referenciada' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $refs;
}

/**
 * Control de formulario adecuado para una columna NO FK.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      // datetime-local espera formato 'YYYY-MM-DDThh:mm'
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}

/**
 * Renderizar tabla HTML de resultados usando la misma lógica de FKs
 * que el listado principal (para los informes).
 */
function render_tabla_html_con_links($conexion, $tabla, $rows, $bd){
  if(!$rows || count($rows) === 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }
  $foreignKeysLocal = obtener_claves_foraneas($conexion, $tabla, $bd);

  echo "<table class='report-table'>";
  // Cabecera
  $first = $rows[0];
  echo "<tr>";
  foreach($first as $k => $_){
    echo "<th>".$k."</th>";
  }
  echo "</tr>";

  // Filas
  foreach($rows as $fila){
    echo "<tr>";
    foreach($fila as $clave=>$valor){
      if(isset($foreignKeysLocal[$clave]) && $valor !== null && $valor !== ''){
        $fk = $foreignKeysLocal[$clave];
        $tabla_fk   = $fk['tabla'];
        $columna_fk = $fk['columna'];

        $sql_fk = "
          SELECT *
          FROM ".$tabla_fk."
          WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
          LIMIT 1
        ";
        $res_fk = mysqli_query($conexion, $sql_fk);
        if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
          $partes = [];
          foreach($fila_fk as $k2=>$v2){
            $partes[] = $v2;
          }
          $texto_celda = implode(" | ", $partes);
          echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
        }else{
          echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
        }
      }else{
        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
      }
    }
    echo "</tr>";
  }

  echo "</table>";
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
      :root{
        --margen: 20px;
        --color_primario: indigo;
        --color_primario_suave: rgba(75,0,130,0.08);
        --color_secundario: aliceblue;
        --radio: 8px;
      }
      *{
        box-sizing:border-box;
      }
      html,body{
        width:100%;
        height:100%;
        padding:0;
        margin:0;
        font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      body{
        display:flex;
        background:linear-gradient(135deg, #f5f7ff 0%, #e8f0ff 50%, #fdfdff 100%);
        color:#222;
      }
      /* NAV LATERAL */
      nav{
        flex:1;
        min-width:240px;
        max-width:320px;
        padding:var(--margen);
        display:flex;
        flex-direction:column;
        gap:var(--margen);
        background:radial-gradient(circle at top left,#4b0082 0%,#2b004d 40%,#120024 100%);
        box-shadow:4px 0 20px rgba(0,0,0,0.25);
        color:white;
        position:relative;
        z-index:2;
      }
      #corporativo{
        display:flex;
        color:white;
        gap:calc(var(--margen)/2);
        align-items:center;
        justify-content:space-between;
        padding-bottom:var(--margen);
        border-bottom:1px solid rgba(255,255,255,0.15);
      }
      #corporativo img{
        width:56px;
        filter:drop-shadow(0 0 6px rgba(255,255,255,0.3));
      }
      #corporativo p{
        font-size:26px;
        margin:0;
        font-weight:700;
        letter-spacing:1px;
        text-shadow:0 0 6px rgba(0,0,0,0.3);
      }
      .logout{
        background:rgba(240,248,255,0.2);
        color:aliceblue;
        padding:6px 12px;
        border-radius:999px;
        text-decoration:none;
        font-size:12px;
        font-weight:600;
        border:1px solid rgba(240,248,255,0.4);
        transition:all 0.2s ease;
      }
      .logout:hover{
        background:aliceblue;
        color:var(--color_primario);
      }
      .login-user-label{
        font-size:11px;
        color:aliceblue;
        opacity:0.85;
        margin-right:6px;
      }

      nav>button{
        background:rgba(240,248,255,0.06);
        color:var(--color_secundario);
        padding:10px 12px;
        border-radius:var(--radio);
        border:1px solid transparent;
        display:flex;
        justify-content: space-between;
        align-items:center;
        cursor:pointer;
        transition:all 0.2s ease;
      }
      nav>button:hover{
        background:rgba(240,248,255,0.16);
        border-color:rgba(240,248,255,0.3);
        transform:translateX(2px);
      }
      .activo{
        background:rgba(240,248,255,0.25);
        border-color:rgba(240,248,255,0.7);
        transform:translateX(4px);
        box-shadow:0 0 10px rgba(240,248,255,0.4);
      }
      nav button a{
        text-decoration:none;
        color:inherit;
        font-size:13px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
      }
      .anadir{
        width:22px;
        height:22px;
        background:aliceblue;
        color:var(--color_primario);
        border-radius:50%;
        line-height:22px;
        font-weight:bold;
        text-align:center;
        text-decoration:none;
        display:inline-block;
        box-shadow:0 0 6px rgba(0,0,0,0.3);
      }

      /* MAIN / DASHBOARD */
      main{
        flex:6;
        padding:var(--margen);
        overflow:auto;
        background:radial-gradient(circle at top,rgba(240,248,255,0.7) 0%,rgba(230,235,255,0.9) 40%,#f9fbff 100%);
        position:relative;
      }
      main::before{
        content:"";
        position:absolute;
        inset:0;
        background:radial-gradient(circle at bottom right,rgba(75,0,130,0.08) 0%,transparent 55%);
        pointer-events:none;
        z-index:-1;
      }
      h2{
        margin-top:0;
        margin-bottom:10px;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }

      /* TABLAS */
      main table{
        width:100%;
        border:1px solid rgba(75,0,130,0.2);
        border-collapse:collapse;
        border-radius:var(--radio);
        overflow:hidden;
        background:white;
        box-shadow:0 4px 14px rgba(0,0,0,0.06);
      }
      main table tr:nth-child(even){
        background:#f9f9ff;
      }
      main table tr:hover{
        background:#eef2ff;
      }
      main table td{
        padding:10px 12px;
        vertical-align:top;
        font-size:13px;
      }
      main table th{
        background:linear-gradient(90deg,var(--color_primario),#7b3fb0);
        padding:10px 12px;
        color:aliceblue;
        text-align:left;
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:0.7px;
      }

      .report-table{
        margin-bottom:var(--margen);
      }
      .no-data{
        font-size:13px;
        color:#666;
      }

      /* ACCIONES */
      .eliminar,
      .editar,
      .reportar{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:24px;
        height:24px;
        border-radius:999px;
        text-decoration:none;
        color:white;
        margin-left:4px;
        font-size:12px;
        box-shadow:0 0 6px rgba(0,0,0,0.25);
        transition:transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
      }
      .eliminar{
        background:#c0392b;
      }
      .editar{
        background:#e67e22;
      }
      .reportar{
        background:#16a085;
      }
      .eliminar:hover,
      .editar:hover,
      .reportar:hover{
        transform:translateY(-1px) scale(1.03);
        box-shadow:0 0 10px rgba(0,0,0,0.35);
        opacity:0.95;
      }

      @keyframes aparece{
        0%{opacity:0;transform:translateX(-30px);}
        100%{opacity:1;transform:translateX(0px);}
      }

      /* FORMULARIOS */
      form{
        columns:2;
        gap:var(--margen);
        margin-top:10px;
      }
      form label{
        display:block;
        font-weight:600;
        margin-bottom:4px;
        font-size:12px;
        color:#444;
      }
      form input,
      form select{
        width:100%;
        padding:10px 12px;
        box-sizing:border-box;
        margin-bottom:var(--margen);
        border:1px solid rgba(75,0,130,0.3);
        border-radius:var(--radio);
        background:rgba(255,255,255,0.9);
        font-size:13px;
        transition:border 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
      }
      form input:focus,
      form select:focus{
        outline:none;
        border-color:var(--color_primario);
        box-shadow:0 0 0 2px rgba(75,0,130,0.15);
        background:white;
      }
      form input[type=checkbox]{
        width:auto;
        padding:0;
        margin-top:5px;
        box-shadow:none;
      }
      form input[type=submit]{
        background:linear-gradient(90deg,var(--color_primario),#7b3fb0);
        color:white;
        cursor:pointer;
        border:none;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.8px;
        box-shadow:0 4px 10px rgba(75,0,130,0.4);
      }
      form input[type=submit]:hover{
        box-shadow:0 5px 14px rgba(75,0,130,0.6);
        transform:translateY(-1px);
      }

      /* LOGIN */
      .login-box{
        max-width:420px;
        margin:80px auto;
        background:white;
        padding:var(--margen);
        border-radius:16px;
        border:1px solid rgba(75,0,130,0.2);
        box-shadow:0 14px 40px rgba(0,0,0,0.18);
        column-count:1;
        position:relative;
        overflow:hidden;
      }
      .login-box::before{
        content:"";
        position:absolute;
        inset:0;
        background:radial-gradient(circle at top,#eef0ff 0%,transparent 55%);
        opacity:0.9;
        pointer-events:none;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .login-box form{
        columns:1;
        position:relative;
        z-index:1;
      }
      .login-error{
        background:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
        position:relative;
        z-index:1;
      }

      /* DASHBOARD / CHARTS */
      .dashboard-intro{
        margin-bottom:var(--margen);
        font-size:14px;
        color:#555;
        max-width:700px;
      }
      .charts-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
        gap:var(--margen);
      }
      .chart{
        background:white;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-sizing:border-box;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        position:relative;
        overflow:hidden;
      }
      .chart::before{
        content:"";
        position:absolute;
        inset:0;
        background:radial-gradient(circle at top right,rgba(75,0,130,0.08) 0%,transparent 60%);
        pointer-events:none;
      }
      .chart h3{
        margin-top:0;
        margin-bottom:10px;
        font-size:15px;
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .chart-subtitle{
        font-size:11px;
        color:#777;
        margin-bottom:8px;
        position:relative;
        z-index:1;
      }
      .chart-bars{
        display:flex;
        flex-direction:column;
        gap:6px;
        position:relative;
        z-index:1;
      }
      .chart-bar{
        position:relative;
        height:24px;
        background:var(--color_primario_suave);
        border-radius:12px;
        overflow:hidden;
      }
      .chart-fill{
        height:100%;
        background:linear-gradient(90deg,var(--color_primario),#7b3fb0);
        opacity:0.85;
      }
      .chart-label{
        position:absolute;
        left:10px;
        top:4px;
        font-size:11px;
        color:white;
        text-shadow:0 0 3px rgba(0,0,0,0.4);
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
        right:6px;
      }

      .back-link{
        margin-bottom:var(--margen);
        display:inline-block;
        text-decoration:none;
        color:var(--color_primario);
        font-size:13px;
        padding:4px 8px;
        border-radius:999px;
        background:rgba(75,0,130,0.07);
      }
      .back-link::before{
        content:"← ";
      }
      .subsection{
        margin-top:var(--margen);
      }
      .subsection h3{
        margin-bottom:6px;
        color:#333;
      }
      .subsection h4{
        margin:8px 0 4px;
        font-size:13px;
        color:#555;
      }

      @media (max-width:900px){
        body{flex-direction:column;}
        nav{
          flex:none;
          max-width:none;
          box-shadow:0 4px 12px rgba(0,0,0,0.2);
        }
      }
    </style>
  </head>
  <body>
    <nav>
      <div id="corporativo">
        <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
          <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
          <p>jocarsa</p>
        </div>
        <?php if($logged_in): ?>
          <div>
            <span class="login-user-label"><?php echo htmlspecialchars($_SESSION['usuario']); ?></span>
            <a href="?logout=1" class="logout">Salir</a>
          </div>
        <?php endif; ?>
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual) ? "activo" : "";
            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual){
                echo "<a href='?operacion=añadir&tabla=".$tabla_actual."' class='anadir'>+</a>";
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {
          // Lógica del microERP
          if(isset($_GET['tabla'])){
            $tabla      = $_GET['tabla'];
            $operacion  = $_GET['operacion'] ?? '';
            $id         = isset($_GET['id']) ? $_GET['id'] : null; // string, no asumimos numérico

            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);
            $primaryKey   = obtener_pk_columna($conexion, $tabla, $db_name);

            // Eliminación
            if($operacion === "eliminar" && $id !== null && $primaryKey){
              $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql.";"
              );
              $operacion = '';
            }

            // AÑADIR
            if($operacion === "añadir"){
              // Procesar inserción si viene por POST
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  // Omitimos PK en inserción si es autoincremental (o en general)
                  if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  // tinyint(1) checkbox
                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              // Formulario de alta
              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
              echo "<h2>Añadir registro en ".$tabla."</h2>";
              echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";

              foreach($columnMeta as $nombre_columna => $meta_columna){
                if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                // FK: select
                if(isset($foreignKeys[$nombre_columna])){
                  $fk = $foreignKeys[$nombre_columna];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  echo "<label>".$nombre_columna."</label>";
                  echo "<select name='".$nombre_columna."'>";
                  echo "<option value=''>-- seleccionar --</option>";

                  $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                  if($res_fk){
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_opcion = implode(" | ", $partes);
                      $value_opcion = $fila_fk[$columna_fk];
                      echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                    }
                  }

                  echo "</select>";
                }else{
                  echo render_input_para_columna($nombre_columna, $meta_columna);
                }
              }

              echo "<input type='submit' value='Guardar'>";
              echo "</form>";

            // EDITAR
            } elseif($operacion === "editar" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede editar un registro concreto.</p>";
              } else {
                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                // Cargamos la fila actual
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<p>No se ha encontrado el registro a editar.</p>";
                } else {
                  // Procesar actualización
                  if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                    $sets = [];

                    foreach($columnMeta as $nombre_columna => $meta_columna){
                      if($nombre_columna === $primaryKey){ continue; }

                      $data_type   = strtolower($meta_columna['DATA_TYPE']);
                      $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                      // tinyint(1) checkbox
                      if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                        $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                        $sets[] = "`".$nombre_columna."`=".intval($valor);
                        continue;
                      }

                      if(isset($_POST[$nombre_columna])){
                        $valor = $_POST[$nombre_columna];
                        $sets[] = "`".$nombre_columna."` = '".mysqli_real_escape_string($conexion,$valor)."'";
                      }
                    }

                    if(count($sets) > 0){
                      $sql_update = "UPDATE ".$tabla." SET ".implode(", ",$sets)." WHERE `".$primaryKey."` = ".$id_sql;
                      mysqli_query($conexion, $sql_update);
                    }

                    // Recargar fila actualizada
                    $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                    $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : $fila_actual;
                  }

                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<h2>Editar registro en ".$tabla." (".$primaryKey." = ".htmlspecialchars($id,ENT_QUOTES).")</h2>";
                  echo "<form action='?operacion=editar&tabla=".$tabla."&id=".urlencode($id)."' method='POST'>";

                  // PK como solo lectura
                  if($primaryKey && isset($fila_actual[$primaryKey])){
                    echo "<label>".$primaryKey."</label>";
                    echo "<input type='text' value='".htmlspecialchars($fila_actual[$primaryKey],ENT_QUOTES)."' disabled>";
                  }

                  foreach($columnMeta as $nombre_columna => $meta_columna){
                    if($nombre_columna === $primaryKey){ continue; }
                    $valor_actual = $fila_actual[$nombre_columna] ?? "";

                    if(isset($foreignKeys[$nombre_columna])){
                      $fk = $foreignKeys[$nombre_columna];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      echo "<label>".$nombre_columna."</label>";
                      echo "<select name='".$nombre_columna."'>";
                      echo "<option value=''>-- seleccionar --</option>";

                      $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                      if($res_fk){
                        while($fila_fk = mysqli_fetch_assoc($res_fk)){
                          $partes = [];
                          foreach($fila_fk as $k2=>$v2){
                            $partes[] = $v2;
                          }
                          $texto_opcion = implode(" | ", $partes);
                          $value_opcion = $fila_fk[$columna_fk];
                          $selected = ($valor_actual == $value_opcion) ? "selected" : "";
                          echo "<option value='".$value_opcion."' ".$selected.">".$texto_opcion."</option>";
                        }
                      }

                      echo "</select>";
                    }else{
                      echo render_input_para_columna($nombre_columna, $meta_columna, $valor_actual);
                    }
                  }

                  echo "<input type='submit' value='Guardar cambios'>";
                  echo "</form>";
                }
              }

            // INFORME
            } elseif($operacion === "report" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede generar un informe por registro.</p>";
              } else {
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                // Fila actual
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<p>No se ha encontrado el registro solicitado.</p>";
                } else {
                  echo "<h2>Informe de ".$tabla." (".$primaryKey." = ".htmlspecialchars($id,ENT_QUOTES).")</h2>";

                  // Registro principal
                  echo "<div class='subsection'>";
                  echo "<h3>Registro principal</h3>";
                  render_tabla_html_con_links($conexion, $tabla, [$fila_actual], $db_name);
                  echo "</div>";

                  // Datos que este registro referencia (FK salientes)
                  echo "<div class='subsection'>";
                  echo "<h3>Datos referenciados por este registro</h3>";

                  $hay_referenciados = false;
                  foreach($foreignKeys as $columna_fk_local => $info_fk){
                    $valor_fk = $fila_actual[$columna_fk_local] ?? null;
                    if($valor_fk === null || $valor_fk === ''){ continue; }

                    $tabla_fk   = $info_fk['tabla'];
                    $col_fk     = $info_fk['columna'];

                    $sql_fk = "SELECT * FROM ".$tabla_fk." WHERE ".$col_fk." = '".mysqli_real_escape_string($conexion,$valor_fk)."'";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && mysqli_num_rows($res_fk) > 0){
                      $hay_referenciados = true;
                      $rows_fk = [];
                      while($row_fk = mysqli_fetch_assoc($res_fk)){
                        $rows_fk[] = $row_fk;
                      }

                      echo "<h4>".$tabla_fk." (por ".$columna_fk_local.")</h4>";
                      render_tabla_html_con_links($conexion, $tabla_fk, $rows_fk, $db_name);
                    }
                  }
                  if(!$hay_referenciados){
                    echo "<p class='no-data'>No hay referencias salientes.</p>";
                  }
                  echo "</div>";

                  // Tablas que referencian a este registro (FK entrantes)
                  echo "<div class='subsection'>";
                  echo "<h3>Datos relacionados que apuntan a este registro</h3>";

                  $refs_entrantes = obtener_tablas_que_referencian($conexion, $tabla, $db_name);
                  if(count($refs_entrantes) === 0){
                    echo "<p class='no-data'>No hay tablas que referencien a esta entidad.</p>";
                  } else {
                    $hay_entrantes = false;
                    foreach($refs_entrantes as $ref){
                      $tabla_hija        = $ref['tabla'];
                      $columna_hija      = $ref['columna'];
                      $col_ref_padre     = $ref['columna_referenciada'];

                      $valor_ref_padre = $fila_actual[$col_ref_padre] ?? null;
                      if($valor_ref_padre === null){ continue; }

                      $sql_hija = "SELECT * FROM ".$tabla_hija." WHERE ".$columna_hija." = '".mysqli_real_escape_string($conexion,$valor_ref_padre)."'";
                      $res_hija = mysqli_query($conexion, $sql_hija);
                      if($res_hija && mysqli_num_rows($res_hija) > 0){
                        $hay_entrantes = true;
                        $rows_hija = [];
                        while($fila_hija = mysqli_fetch_assoc($res_hija)){
                          $rows_hija[] = $fila_hija;
                        }

                        echo "<h4>".$tabla_hija." (columna ".$columna_hija.")</h4>";
                        render_tabla_html_con_links($conexion, $tabla_hija, $rows_hija, $db_name);
                      }
                    }
                    if(!$hay_entrantes){
                      echo "<p class='no-data'>No hay registros entrantes que apunten a este registro.</p>";
                    }
                  }

                  echo "</div>";
                }
              }

            // LISTADO
            } else {
              echo "<h2>Listado de ".$tabla."</h2>";
              if(!$primaryKey){
                echo "<p class='no-data'>Aviso: la tabla <b>".$tabla."</b> no tiene clave primaria definida. No se podrán editar ni eliminar registros individualmente.</p>";
              }
              echo "<table>";
              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $contador = 0;
              while($fila = mysqli_fetch_assoc($resultado)){
                if($contador == 0){
                  echo "<tr>";
                    foreach($fila as $clave=>$valor){
                      echo "<th>".$clave."</th>";
                    }
                    echo "<th>Acciones</th>";
                  echo "</tr>";
                }

                echo "<tr>";
                foreach($fila as $clave=>$valor){
                  // Si es FK, mostramos fila referenciada
                  if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                    $fk = $foreignKeys[$clave];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    $sql_fk = "
                      SELECT *
                      FROM ".$tabla_fk."
                      WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                      LIMIT 1
                    ";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_celda = implode(" | ", $partes);
                      echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
                    }else{
                      echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                    }
                  }else{
                    echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                  }
                }

                // Acciones: editar, informe, eliminar (solo si hay PK)
                echo "<td>";
                if($primaryKey && isset($fila[$primaryKey])){
                  $id_fila = $fila[$primaryKey];
                  $id_url  = urlencode($id_fila);
                  echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                  echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                  echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                } else {
                  echo "<span style='font-size:11px;color:#777;'>—</span>";
                }
                echo "</td>";

                echo "</tr>";

                $contador++;
              }
              echo "</table>";
            }
          } else {
            // DASHBOARD INICIAL: gráficos de campos ENUM/SET y FKs
            echo "<h2>Dashboard de microERP</h2>";
            echo "<p class='dashboard-intro'>
              Resumen gráfico de la información categórica y relacional del sistema:
              campos <b>ENUM/SET</b> y campos de <b>clave foránea</b> en todas las tablas.
            </p>";

            $resultado = mysqli_query($conexion, "SHOW TABLES;");
            echo "<div class='charts-grid'>";
            while($fila = mysqli_fetch_assoc($resultado)){
              $tabla = array_values($fila)[0];
              $meta  = obtener_meta_columnas($conexion, $tabla, $db_name);
              $fksTabla = obtener_claves_foraneas($conexion, $tabla, $db_name);

              // 1) Campos ENUM/SET
              foreach($meta as $nombre_columna => $meta_columna){
                $data_type = strtolower($meta_columna['DATA_TYPE']);
                if($data_type !== 'enum' && $data_type !== 'set'){ continue; }

                $sql_dist = "
                  SELECT ".$nombre_columna." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$nombre_columna."
                  ORDER BY total DESC
                ";
                $res_dist = mysqli_query($conexion, $sql_dist);
                if(!$res_dist || mysqli_num_rows($res_dist) < 1){ continue; }

                $valores = [];
                $max = 0;
                while($fila_dist = mysqli_fetch_assoc($res_dist)){
                  $v = $fila_dist['valor'];
                  $c = (int)$fila_dist['total'];
                  $valores[] = [
                    'label' => ($v === null || $v === '' ? '(vacío)' : $v),
                    'total' => $c
                  ];
                  if($c > $max){ $max = $c; }
                }
                if($max == 0){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$nombre_columna."</h3>";
                echo "<div class='chart-subtitle'>Distribución de valores ENUM/SET</div>";
                echo "<div class='chart-bars'>";
                foreach($valores as $dato){
                  $label = $dato['label'];
                  $c     = $dato['total'];
                  $width = round(($c / $max) * 100, 2);
                  $text  = htmlspecialchars($label,ENT_QUOTES)." (".$c.")";
                  echo "<div class='chart-bar'>";
                  echo "<div class='chart-fill' style='width:".$width."%;'></div>";
                  echo "<div class='chart-label'>".$text."</div>";
                  echo "</div>";
                }
                echo "</div>";
                echo "</div>";
              }

              // 2) Campos FK: distribución por valor referenciado
              foreach($fksTabla as $columna_fk => $info_fk){
                $tabla_ref = $info_fk['tabla'];
                $col_ref   = $info_fk['columna'];

                $sql_dist_fk = "
                  SELECT ".$columna_fk." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$columna_fk."
                  ORDER BY total DESC
                ";
                $res_dist_fk = mysqli_query($conexion, $sql_dist_fk);
                if(!$res_dist_fk || mysqli_num_rows($res_dist_fk) < 1){ continue; }

                $valores_fk = [];
                $max_fk = 0;

                while($fila_dist = mysqli_fetch_assoc($res_dist_fk)){
                  $valor_fk = $fila_dist['valor'];
                  $c        = (int)$fila_dist['total'];

                  if($valor_fk === null || $valor_fk === ''){
                    $label = '(sin valor)';
                  }else{
                    // Miramos fila referenciada para label
                    $sql_ref = "
                      SELECT *
                      FROM ".$tabla_ref."
                      WHERE ".$col_ref." = '".mysqli_real_escape_string($conexion,$valor_fk)."'
                      LIMIT 1
                    ";
                    $res_ref = mysqli_query($conexion, $sql_ref);
                    if($res_ref && $fila_ref = mysqli_fetch_assoc($res_ref)){
                      $partes = [];
                      foreach($fila_ref as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $label = implode(" | ", $partes);
                    }else{
                      $label = 'ID '.$valor_fk.' (huérfano)';
                    }
                  }

                  $valores_fk[] = [
                    'label' => $label,
                    'total' => $c
                  ];
                  if($c > $max_fk){ $max_fk = $c; }
                }

                if($max_fk == 0){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$columna_fk."</h3>";
                echo "<div class='chart-subtitle'>Distribución por referencia a ".$tabla_ref."</div>";
                echo "<div class='chart-bars'>";
                foreach($valores_fk as $dato){
                  $label = $dato['label'];
                  $c     = $dato['total'];
                  $width = round(($c / $max_fk) * 100, 2);
                  $text  = htmlspecialchars($label,ENT_QUOTES)." (".$c.")";
                  echo "<div class='chart-bar'>";
                  echo "<div class='chart-fill' style='width:".$width."%;'></div>";
                  echo "<div class='chart-label'>".$text."</div>";
                  echo "</div>";
                }
                echo "</div>";
                echo "</div>";
              }
            }
            echo "</div>";
          }
        }
      ?>
    </main>
  </body>
</html>
```

### graficas y degradados

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "tienda2526";
$db_user = "tienda2526";
$db_pass = "tienda2526";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: ?");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: ?");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * FKs salientes desde una tabla:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Metadatos de columnas de una tabla.
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Obtener nombre de la columna PK (primer PRIMARY KEY definido).
 * Devuelve null si la tabla no tiene PK.
 */
function obtener_pk_columna($conexion, $tabla, $bd){
  $sql = "
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND COLUMN_KEY = 'PRI'
    ORDER BY ORDINAL_POSITION
    LIMIT 1
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado && $fila = mysqli_fetch_assoc($resultado)){
    return $fila['COLUMN_NAME'];
  }
  return null;
}

/**
 * Tablas que referencian a una tabla dada (FK entrantes)
 * [
 *   ['tabla' => 'lineas', 'columna' => 'id_cabecera', 'columna_referenciada' => 'IdCabecera'],
 *   ...
 * ]
 */
function obtener_tablas_que_referencian($conexion, $tabla_referenciada, $bd){
  $refs = [];
  $sql = "
    SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND REFERENCED_TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla_referenciada)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $refs[] = [
        'tabla'                => $fila['TABLE_NAME'],
        'columna'              => $fila['COLUMN_NAME'],
        'columna_referenciada' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $refs;
}

/**
 * Control de formulario adecuado para una columna NO FK.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      // datetime-local espera formato 'YYYY-MM-DDThh:mm'
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}

/**
 * Renderizar tabla HTML de resultados usando la misma lógica de FKs
 * que el listado principal (para los informes).
 */
function render_tabla_html_con_links($conexion, $tabla, $rows, $bd){
  if(!$rows || count($rows) === 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }
  $foreignKeysLocal = obtener_claves_foraneas($conexion, $tabla, $bd);

  echo "<table class='report-table'>";
  // Cabecera
  $first = $rows[0];
  echo "<tr>";
  foreach($first as $k => $_){
    echo "<th>".$k."</th>";
  }
  echo "</tr>";

  // Filas
  foreach($rows as $fila){
    echo "<tr>";
    foreach($fila as $clave=>$valor){
      if(isset($foreignKeysLocal[$clave]) && $valor !== null && $valor !== ''){
        $fk = $foreignKeysLocal[$clave];
        $tabla_fk   = $fk['tabla'];
        $columna_fk = $fk['columna'];

        $sql_fk = "
          SELECT *
          FROM ".$tabla_fk."
          WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
          LIMIT 1
        ";
        $res_fk = mysqli_query($conexion, $sql_fk);
        if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
          $partes = [];
          foreach($fila_fk as $k2=>$v2){
            $partes[] = $v2;
          }
          $texto_celda = implode(" | ", $partes);
          echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
        }else{
          echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
        }
      }else{
        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
      }
    }
    echo "</tr>";
  }

  echo "</table>";
}

/**
 * Renderiza un gráfico de tipo donut (pie chart) como SVG.
 * $segmentos = [
 *   ['label' => 'Texto', 'total' => 10],
 *   ...
 * ]
 */
function render_pie_chart($segmentos, $chart_id){
  $total = 0;
  foreach($segmentos as $s){
    $total += $s['total'];
  }
  if($total <= 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }

  // Donut típico: 100 unidades de perímetro "virtual".
  $acumulado = 0.0;

  echo "<div class='chart-pie-wrapper'>";
  echo "<div class='chart-pie'>";
  echo "<svg viewBox='0 0 42 42' class='donut'>";

  // Círculo de fondo
  echo "<circle class='donut-ring' cx='21' cy='21' r='15.915'></circle>";

  $index = 0;
  foreach($segmentos as $s){
    $valor = $s['total'];
    $percent = ($valor / $total) * 100.0;
    $dasharray = $percent." ".(100 - $percent);
    $dashoffset = 25 - $acumulado; // empezamos arriba

    echo "<circle class='donut-segment segment-".$index."' cx='21' cy='21' r='15.915' ";
    echo "stroke-dasharray='".$dasharray."' stroke-dashoffset='".$dashoffset."'></circle>";

    $acumulado += $percent;
    $index++;
  }

  echo "</svg>";
  echo "</div>";

  // Leyenda
  echo "<ul class='chart-legend'>";
  $index = 0;
  foreach($segmentos as $s){
    $label = htmlspecialchars($s['label'],ENT_QUOTES);
    $valor = (int)$s['total'];
    echo "<li>";
    echo "<span class='legend-color segment-".$index."'></span>";
    echo "<span class='legend-label'>".$label."</span>";
    echo "<span class='legend-value'>(".$valor.")</span>";
    echo "</li>";
    $index++;
  }
  echo "</ul>";

  echo "</div>";
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
      :root{
        --margen: 20px;
        --color_primario: indigo;
        --color_secundario: aliceblue;
        --color_nav_fondo: #1f0033;
        --color_main_fondo: #edf0ff;
        --color_tabla_header: indigo;
        --color_tabla_borde: #b3b5e0;
        --color_tabla_fila_par: #f7f7ff;
        --color_tabla_fila_impar: #ffffff;
        --radio: 8px;

        --chart-color-0: #4b0082;
        --chart-color-1: #7b3fb0;
        --chart-color-2: #ff8c42;
        --chart-color-3: #16a085;
        --chart-color-4: #3498db;
        --chart-color-5: #c0392b;
        --chart-color-6: #2ecc71;
        --chart-color-7: #f1c40f;
      }
      *{
        box-sizing:border-box;
      }
      html,body{
        width:100%;
        height:100%;
        padding:0;
        margin:0;
        font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      body{
        display:flex;
        background-color:#f3f4ff;
        color:#222;
      }

      /* NAV LATERAL */
      nav{
        flex:1;
        min-width:240px;
        max-width:320px;
        padding:var(--margen);
        display:flex;
        flex-direction:column;
        gap:var(--margen);
        background-color:var(--color_nav_fondo);
        box-shadow:4px 0 20px rgba(0,0,0,0.25);
        color:white;
        position:relative;
        z-index:2;
      }
      #corporativo{
        display:flex;
        color:white;
        gap:calc(var(--margen)/2);
        align-items:center;
        justify-content:space-between;
        padding-bottom:var(--margen);
        border-bottom:1px solid rgba(255,255,255,0.15);
      }
      #corporativo img{
        width:56px;
        filter:drop-shadow(0 0 6px rgba(255,255,255,0.3));
      }
      #corporativo p{
        font-size:26px;
        margin:0;
        font-weight:700;
        letter-spacing:1px;
        text-shadow:0 0 6px rgba(0,0,0,0.3);
      }
      .logout{
        background-color:rgba(240,248,255,0.1);
        color:aliceblue;
        padding:6px 12px;
        border-radius:999px;
        text-decoration:none;
        font-size:12px;
        font-weight:600;
        border:1px solid rgba(240,248,255,0.4);
        transition:all 0.2s ease;
        background: indigo;
      }
      .logout:hover{
        background-color:aliceblue;
        color:var(--color_primario);
      }
      .login-user-label{
        font-size:11px;
      
        opacity:0.85;
        margin-right:6px;
      }

      nav>button{
        background-color:rgba(240,248,255,0.08);
        color:var(--color_secundario);
        padding:10px 12px;
        border-radius:var(--radio);
        border:1px solid transparent;
        display:flex;
        justify-content: space-between;
        align-items:center;
        cursor:pointer;
        transition:all 0.2s ease;
      }
      nav>button:hover{
        background-color:rgba(240,248,255,0.18);
        border-color:rgba(240,248,255,0.4);
        transform:translateX(2px);
      }
      .activo{
        background-color: var(--color_main_fondo);
    border-color: rgba(240, 248, 255, 0.8);
    transform: translateX(4px);
    /* box-shadow: 0 0 10px rgba(240, 248, 255, 0.4); */
    color: indigo;
    width: 120%;
      }
      nav button a{
        text-decoration:none;
        color:inherit;
        font-size:13px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
      }
      .anadir{
        width: 22px;
    height: 22px;
    background-color: aliceblue;
    /* color: var(--color_primario); */
    border-radius: 50%;
    line-height: 22px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    box-shadow: 0 0 6px rgba(0, 0, 0, 0.3);
    color: white;
    background: indigo;
      }

      /* MAIN / DASHBOARD */
      main{
        flex:6;
        padding:var(--margen);
        overflow:auto;
        background-color:var(--color_main_fondo);
        position:relative;
      }
      main::before{
        content:"";
        position:absolute;
        inset:0;
        background-color:transparent;
        pointer-events:none;
        z-index:-1;
      }
      h2{
        margin-top:0;
        margin-bottom:10px;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }

      /* TABLAS */
      main table{
        width:100%;
        border:1px solid var(--color_tabla_borde);
        border-collapse:collapse;
        border-radius:var(--radio);
        overflow:hidden;
        background-color:var(--color_tabla_fila_impar);
        box-shadow:0 4px 14px rgba(0,0,0,0.06);
      }
      main table tr:nth-child(even){
        background-color:var(--color_tabla_fila_par);
      }
      main table tr:hover{
        background-color:#e4e6ff;
      }
      main table td{
        padding:10px 12px;
        vertical-align:top;
        font-size:13px;
      }
      main table th{
        background-color:var(--color_tabla_header);
        padding:10px 12px;
        color:aliceblue;
        text-align:left;
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:0.7px;
      }

      .report-table{
        margin-bottom:var(--margen);
      }
      .no-data{
        font-size:13px;
        color:#666;
      }

      /* ACCIONES */
      .eliminar,
      .editar,
      .reportar{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:24px;
        height:24px;
        border-radius:999px;
        text-decoration:none;
        color:white;
        margin-left:4px;
        font-size:12px;
        box-shadow:0 0 6px rgba(0,0,0,0.25);
        transition:transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
      }
      .eliminar{
        background-color:#c0392b;
      }
      .editar{
        background-color:#e67e22;
      }
      .reportar{
        background-color:#16a085;
      }
      .eliminar:hover,
      .editar:hover,
      .reportar:hover{
        transform:translateY(-1px) scale(1.03);
        box-shadow:0 0 10px rgba(0,0,0,0.35);
        opacity:0.95;
      }

      @keyframes aparece{
        0%{opacity:0;transform:translateX(-30px);}
        100%{opacity:1;transform:translateX(0px);}
      }

      /* FORMULARIOS */
      form{
        columns:2;
        gap:var(--margen);
        margin-top:10px;
      }
      form label{
        display:block;
        font-weight:600;
        margin-bottom:4px;
        font-size:12px;
        color:#444;
      }
      form input,
      form select{
        width:100%;
        padding:10px 12px;
        box-sizing:border-box;
        margin-bottom:var(--margen);
        border:1px solid rgba(75,0,130,0.3);
        border-radius:var(--radio);
        background-color:#ffffff;
        font-size:13px;
        transition:border 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease;
      }
      form input:focus,
      form select:focus{
        outline:none;
        border-color:var(--color_primario);
        box-shadow:0 0 0 2px rgba(75,0,130,0.15);
        background-color:#ffffff;
      }
      form input[type=checkbox]{
        width:auto;
        padding:0;
        margin-top:5px;
        box-shadow:none;
      }
      form input[type=submit]{
        background-color:var(--color_primario);
        color:white;
        cursor:pointer;
        border:none;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.8px;
        box-shadow:0 4px 10px rgba(75,0,130,0.4);
      }
      form input[type=submit]:hover{
        box-shadow:0 5px 14px rgba(75,0,130,0.6);
        transform:translateY(-1px);
      }

      /* LOGIN */
      .login-box{
        max-width:420px;
        margin:80px auto;
        background-color:#ffffff;
        padding:var(--margen);
        border-radius:16px;
        border:1px solid rgba(75,0,130,0.2);
        box-shadow:0 14px 40px rgba(0,0,0,0.18);
        column-count:1;
        position:relative;
        overflow:hidden;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .login-box form{
        columns:1;
        position:relative;
        z-index:1;
      }
      .login-error{
        background-color:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
        position:relative;
        z-index:1;
      }

      /* DASHBOARD / PIE CHARTS */
      .dashboard-intro{
        margin-bottom:var(--margen);
        font-size:14px;
        color:#555;
        max-width:700px;
      }
      .charts-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
        gap:var(--margen);
      }
      .chart{
        background-color:#ffffff;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-sizing:border-box;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        position:relative;
        overflow:hidden;
      }
      .chart h3{
        margin-top:0;
        margin-bottom:8px;
        font-size:15px;
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .chart-subtitle{
        font-size:11px;
        color:#777;
        margin-bottom:8px;
        position:relative;
        z-index:1;
      }

      .chart-pie-wrapper{
        display:flex;
        align-items:center;
        gap:12px;
      }
      .chart-pie{
        width:120px;
        height:120px;
        flex:0 0 auto;
      }
      .chart-pie svg{
        width:100%;
        height:100%;
        transform:rotate(-90deg);
      }
      .donut-ring{
        fill:none;
        stroke:#e0e2ff;
        stroke-width:10;
      }
      .donut-segment{
        fill:none;
        stroke-width:10;
      }
      .segment-0{ stroke:var(--chart-color-0); }
      .segment-1{ stroke:var(--chart-color-1); }
      .segment-2{ stroke:var(--chart-color-2); }
      .segment-3{ stroke:var(--chart-color-3); }
      .segment-4{ stroke:var(--chart-color-4); }
      .segment-5{ stroke:var(--chart-color-5); }
      .segment-6{ stroke:var(--chart-color-6); }
      .segment-7{ stroke:var(--chart-color-7); }

      .chart-legend{
        list-style:none;
        padding:0;
        margin:0;
        font-size:11px;
        color:#555;
        flex:1 1 auto;
      }
      .chart-legend li{
        display:flex;
        align-items:center;
        margin-bottom:4px;
      }
      .legend-color{
        width:10px;
        height:10px;
        border-radius:50%;
        margin-right:6px;
        flex:0 0 auto;
      }
      .legend-color.segment-0{ background-color:var(--chart-color-0); }
      .legend-color.segment-1{ background-color:var(--chart-color-1); }
      .legend-color.segment-2{ background-color:var(--chart-color-2); }
      .legend-color.segment-3{ background-color:var(--chart-color-3); }
      .legend-color.segment-4{ background-color:var(--chart-color-4); }
      .legend-color.segment-5{ background-color:var(--chart-color-5); }
      .legend-color.segment-6{ background-color:var(--chart-color-6); }
      .legend-color.segment-7{ background-color:var(--chart-color-7); }
      .legend-label{
        flex:1 1 auto;
        overflow:hidden;
        text-overflow:ellipsis;
        white-space:nowrap;
      }
      .legend-value{
        margin-left:4px;
        color:#333;
      }

      .back-link{
        margin-bottom:var(--margen);
        display:inline-block;
        text-decoration:none;
        color:var(--color_primario);
        font-size:13px;
        padding:4px 8px;
        border-radius:999px;
        background-color:#dadfff;
      }
      .back-link::before{
        content:"← ";
      }
      .subsection{
        margin-top:var(--margen);
      }
      .subsection h3{
        margin-bottom:6px;
        color:#333;
      }
      .subsection h4{
        margin:8px 0 4px;
        font-size:13px;
        color:#555;
      }

      @media (max-width:900px){
        body{flex-direction:column;}
        nav{
          flex:none;
          max-width:none;
          box-shadow:0 4px 12px rgba(0,0,0,0.2);
        }
        .chart-pie-wrapper{
          flex-direction:column;
          align-items:flex-start;
        }
      }
      #corporativo a{color:inherit;text-decoration:none;}
      #logout{position:absolute;top:10px;right:25px;color:indigo;}
    </style>
  </head>
  <body>
  
    <nav>
      <div id="corporativo">
      <a href="?">
        <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
        
          <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
          <p>jocarsa</p>
         
        </div>
         </a>
        
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual) ? "activo" : "";
            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual){
                echo "<a href='?operacion=añadir&tabla=".$tabla_actual."' class='anadir'>+</a>";
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {
          // Lógica del microERP
          if(isset($_GET['tabla'])){
            $tabla      = $_GET['tabla'];
            $operacion  = $_GET['operacion'] ?? '';
            $id         = isset($_GET['id']) ? $_GET['id'] : null; // string, no asumimos numérico

            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);
            $primaryKey   = obtener_pk_columna($conexion, $tabla, $db_name);

            // Eliminación
            if($operacion === "eliminar" && $id !== null && $primaryKey){
              $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql.";"
              );
              $operacion = '';
            }

            // AÑADIR
            if($operacion === "añadir"){
              // Procesar inserción si viene por POST
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  // tinyint(1) checkbox
                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              // Formulario de alta
              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
              echo "<h2>Añadir registro en ".$tabla."</h2>";
              echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";

              foreach($columnMeta as $nombre_columna => $meta_columna){
                if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                // FK: select
                if(isset($foreignKeys[$nombre_columna])){
                  $fk = $foreignKeys[$nombre_columna];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  echo "<label>".$nombre_columna."</label>";
                  echo "<select name='".$nombre_columna."'>";
                  echo "<option value=''>-- seleccionar --</option>";

                  $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                  if($res_fk){
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_opcion = implode(" | ", $partes);
                      $value_opcion = $fila_fk[$columna_fk];
                      echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                    }
                  }

                  echo "</select>";
                }else{
                  echo render_input_para_columna($nombre_columna, $meta_columna);
                }
              }

              echo "<input type='submit' value='Guardar'>";
              echo "</form>";

            // EDITAR
            } elseif($operacion === "editar" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede editar un registro concreto.</p>";
              } else {
                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                // Cargamos la fila actual
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<p>No se ha encontrado el registro a editar.</p>";
                } else {
                  // Procesar actualización
                  if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                    $sets = [];

                    foreach($columnMeta as $nombre_columna => $meta_columna){
                      if($nombre_columna === $primaryKey){ continue; }

                      $data_type   = strtolower($meta_columna['DATA_TYPE']);
                      $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                      // tinyint(1) checkbox
                      if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                        $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                        $sets[] = "`".$nombre_columna."`=".intval($valor);
                        continue;
                      }

                      if(isset($_POST[$nombre_columna])){
                        $valor = $_POST[$nombre_columna];
                        $sets[] = "`".$nombre_columna."` = '".mysqli_real_escape_string($conexion,$valor)."'";
                      }
                    }

                    if(count($sets) > 0){
                      $sql_update = "UPDATE ".$tabla." SET ".implode(", ",$sets)." WHERE `".$primaryKey."` = ".$id_sql;
                      mysqli_query($conexion, $sql_update);
                    }

                    // Recargar fila actualizada
                    $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                    $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : $fila_actual;
                  }

                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<h2>Editar registro en ".$tabla." (".$primaryKey." = ".htmlspecialchars($id,ENT_QUOTES).")</h2>";
                  echo "<form action='?operacion=editar&tabla=".$tabla."&id=".urlencode($id)."' method='POST'>";

                  // PK como solo lectura
                  if($primaryKey && isset($fila_actual[$primaryKey])){
                    echo "<label>".$primaryKey."</label>";
                    echo "<input type='text' value='".htmlspecialchars($fila_actual[$primaryKey],ENT_QUOTES)."' disabled>";
                  }

                  foreach($columnMeta as $nombre_columna => $meta_columna){
                    if($nombre_columna === $primaryKey){ continue; }
                    $valor_actual = $fila_actual[$nombre_columna] ?? "";

                    if(isset($foreignKeys[$nombre_columna])){
                      $fk = $foreignKeys[$nombre_columna];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      echo "<label>".$nombre_columna."</label>";
                      echo "<select name='".$nombre_columna."'>";
                      echo "<option value=''>-- seleccionar --</option>";

                      $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                      if($res_fk){
                        while($fila_fk = mysqli_fetch_assoc($res_fk)){
                          $partes = [];
                          foreach($fila_fk as $k2=>$v2){
                            $partes[] = $v2;
                          }
                          $texto_opcion = implode(" | ", $partes);
                          $value_opcion = $fila_fk[$columna_fk];
                          $selected = ($valor_actual == $value_opcion) ? "selected" : "";
                          echo "<option value='".$value_opcion."' ".$selected.">".$texto_opcion."</option>";
                        }
                      }

                      echo "</select>";
                    }else{
                      echo render_input_para_columna($nombre_columna, $meta_columna, $valor_actual);
                    }
                  }

                  echo "<input type='submit' value='Guardar cambios'>";
                  echo "</form>";
                }
              }

            // INFORME
            } elseif($operacion === "report" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede generar un informe por registro.</p>";
              } else {
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                // Fila actual
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<p>No se ha encontrado el registro solicitado.</p>";
                } else {
                  echo "<h2>Informe de ".$tabla." (".$primaryKey." = ".htmlspecialchars($id,ENT_QUOTES).")</h2>";

                  // Registro principal
                  echo "<div class='subsection'>";
                  echo "<h3>Registro principal</h3>";
                  render_tabla_html_con_links($conexion, $tabla, [$fila_actual], $db_name);
                  echo "</div>";

                  // Datos que este registro referencia (FK salientes)
                  echo "<div class='subsection'>";
                  echo "<h3>Datos referenciados por este registro</h3>";

                  $hay_referenciados = false;
                  foreach($foreignKeys as $columna_fk_local => $info_fk){
                    $valor_fk = $fila_actual[$columna_fk_local] ?? null;
                    if($valor_fk === null || $valor_fk === ''){ continue; }

                    $tabla_fk   = $info_fk['tabla'];
                    $col_fk     = $info_fk['columna'];

                    $sql_fk = "SELECT * FROM ".$tabla_fk." WHERE ".$col_fk." = '".mysqli_real_escape_string($conexion,$valor_fk)."'";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && mysqli_num_rows($res_fk) > 0){
                      $hay_referenciados = true;
                      $rows_fk = [];
                      while($row_fk = mysqli_fetch_assoc($res_fk)){
                        $rows_fk[] = $row_fk;
                      }

                      echo "<h4>".$tabla_fk." (por ".$columna_fk_local.")</h4>";
                      render_tabla_html_con_links($conexion, $tabla_fk, $rows_fk, $db_name);
                    }
                  }
                  if(!$hay_referenciados){
                    echo "<p class='no-data'>No hay referencias salientes.</p>";
                  }
                  echo "</div>";

                  // Tablas que referencian a este registro (FK entrantes)
                  echo "<div class='subsection'>";
                  echo "<h3>Datos relacionados que apuntan a este registro</h3>";

                  $refs_entrantes = obtener_tablas_que_referencian($conexion, $tabla, $db_name);
                  if(count($refs_entrantes) === 0){
                    echo "<p class='no-data'>No hay tablas que referencien a esta entidad.</p>";
                  } else {
                    $hay_entrantes = false;
                    foreach($refs_entrantes as $ref){
                      $tabla_hija        = $ref['tabla'];
                      $columna_hija      = $ref['columna'];
                      $col_ref_padre     = $ref['columna_referenciada'];

                      $valor_ref_padre = $fila_actual[$col_ref_padre] ?? null;
                      if($valor_ref_padre === null){ continue; }

                      $sql_hija = "SELECT * FROM ".$tabla_hija." WHERE ".$columna_hija." = '".mysqli_real_escape_string($conexion,$valor_ref_padre)."'";
                      $res_hija = mysqli_query($conexion, $sql_hija);
                      if($res_hija && mysqli_num_rows($res_hija) > 0){
                        $hay_entrantes = true;
                        $rows_hija = [];
                        while($fila_hija = mysqli_fetch_assoc($res_hija)){
                          $rows_hija[] = $fila_hija;
                        }

                        echo "<h4>".$tabla_hija." (columna ".$columna_hija.")</h4>";
                        render_tabla_html_con_links($conexion, $tabla_hija, $rows_hija, $db_name);
                      }
                    }
                    if(!$hay_entrantes){
                      echo "<p class='no-data'>No hay registros entrantes que apunten a este registro.</p>";
                    }
                  }

                  echo "</div>";
                }
              }

            // LISTADO
            } else {
              echo "<h2>Listado de ".$tabla."</h2>";
              if(!$primaryKey){
                echo "<p class='no-data'>Aviso: la tabla <b>".$tabla."</b> no tiene clave primaria definida. No se podrán editar ni eliminar registros individualmente.</p>";
              }
              echo "<table>";
              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $contador = 0;
              while($fila = mysqli_fetch_assoc($resultado)){
                if($contador == 0){
                  echo "<tr>";
                    foreach($fila as $clave=>$valor){
                      echo "<th>".$clave."</th>";
                    }
                    echo "<th>Acciones</th>";
                  echo "</tr>";
                }

                echo "<tr>";
                foreach($fila as $clave=>$valor){
                  // Si es FK, mostramos fila referenciada
                  if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                    $fk = $foreignKeys[$clave];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    $sql_fk = "
                      SELECT *
                      FROM ".$tabla_fk."
                      WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                      LIMIT 1
                    ";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_celda = implode(" | ", $partes);
                      echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
                    }else{
                      echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                    }
                  }else{
                    echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                  }
                }

                // Acciones: editar, informe, eliminar (solo si hay PK)
                echo "<td>";
                if($primaryKey && isset($fila[$primaryKey])){
                  $id_fila = $fila[$primaryKey];
                  $id_url  = urlencode($id_fila);
                  echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                  echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                  echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                } else {
                  echo "<span style='font-size:11px;color:#777;'>—</span>";
                }
                echo "</td>";

                echo "</tr>";

                $contador++;
              }
              echo "</table>";
            }
          } else {
            // DASHBOARD INICIAL: gráficos de campos ENUM/SET y FKs como PIE
            echo "<h2>Dashboard de microERP</h2>";
            echo "<p class='dashboard-intro'>
              Resumen gráfico de la información categórica y relacional del sistema:
              campos <b>ENUM/SET</b> y campos de <b>clave foránea</b> en todas las tablas, representados como gráficos de tipo donut.
            </p>";

            $resultado = mysqli_query($conexion, "SHOW TABLES;");
            echo "<div class='charts-grid'>";
            while($fila = mysqli_fetch_assoc($resultado)){
              $tabla = array_values($fila)[0];
              $meta  = obtener_meta_columnas($conexion, $tabla, $db_name);
              $fksTabla = obtener_claves_foraneas($conexion, $tabla, $db_name);

              // 1) Campos ENUM/SET
              foreach($meta as $nombre_columna => $meta_columna){
                $data_type = strtolower($meta_columna['DATA_TYPE']);
                if($data_type !== 'enum' && $data_type !== 'set'){ continue; }

                $sql_dist = "
                  SELECT ".$nombre_columna." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$nombre_columna."
                  ORDER BY total DESC
                ";
                $res_dist = mysqli_query($conexion, $sql_dist);
                if(!$res_dist || mysqli_num_rows($res_dist) < 1){ continue; }

                $segmentos = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist)){
                  $v = $fila_dist['valor'];
                  $c = (int)$fila_dist['total'];
                  $segmentos[] = [
                    'label' => ($v === null || $v === '' ? '(vacío)' : $v),
                    'total' => $c
                  ];
                }
                if(empty($segmentos)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$nombre_columna."</h3>";
                echo "<div class='chart-subtitle'>Distribución de valores ENUM/SET</div>";
                render_pie_chart($segmentos, $tabla."_".$nombre_columna."_enum");
                echo "</div>";
              }

              // 2) Campos FK: distribución por valor referenciado
              foreach($fksTabla as $columna_fk => $info_fk){
                $tabla_ref = $info_fk['tabla'];
                $col_ref   = $info_fk['columna'];

                $sql_dist_fk = "
                  SELECT ".$columna_fk." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$columna_fk."
                  ORDER BY total DESC
                ";
                $res_dist_fk = mysqli_query($conexion, $sql_dist_fk);
                if(!$res_dist_fk || mysqli_num_rows($res_dist_fk) < 1){ continue; }

                $segmentos_fk = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist_fk)){
                  $valor_fk = $fila_dist['valor'];
                  $c        = (int)$fila_dist['total'];

                  if($valor_fk === null || $valor_fk === ''){
                    $label = '(sin valor)';
                  }else{
                    // Miramos fila referenciada para label
                    $sql_ref = "
                      SELECT *
                      FROM ".$tabla_ref."
                      WHERE ".$col_ref." = '".mysqli_real_escape_string($conexion,$valor_fk)."'
                      LIMIT 1
                    ";
                    $res_ref = mysqli_query($conexion, $sql_ref);
                    if($res_ref && $fila_ref = mysqli_fetch_assoc($res_ref)){
                      $partes = [];
                      foreach($fila_ref as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $label = implode(" | ", $partes);
                    }else{
                      $label = 'ID '.$valor_fk.' (huérfano)';
                    }
                  }

                  $segmentos_fk[] = [
                    'label' => $label,
                    'total' => $c
                  ];
                }
                if(empty($segmentos_fk)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$columna_fk."</h3>";
                echo "<div class='chart-subtitle'>Distribución por referencia a ".$tabla_ref."</div>";
                render_pie_chart($segmentos_fk, $tabla."_".$columna_fk."_fk");
                echo "</div>";
              }
            }
            echo "</div>";
          }
        }
      ?>
    </main>
    <?php if($logged_in): ?>
          <div id="logout">
            <span class="login-user-label"><?php echo htmlspecialchars($_SESSION['usuario']); ?></span>
            <a href="?logout=1" class="logout">Salir</a>
          </div>
        <?php endif; ?>
  </body>
</html>
```

### fuente

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "tienda2526";
$db_user = "tienda2526";
$db_pass = "tienda2526";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: ?");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: ?");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * FKs salientes desde una tabla:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Metadatos de columnas de una tabla.
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Obtener nombre de la columna PK (primer PRIMARY KEY definido).
 * Devuelve null si la tabla no tiene PK.
 */
function obtener_pk_columna($conexion, $tabla, $bd){
  $sql = "
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND COLUMN_KEY = 'PRI'
    ORDER BY ORDINAL_POSITION
    LIMIT 1
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado && $fila = mysqli_fetch_assoc($resultado)){
    return $fila['COLUMN_NAME'];
  }
  return null;
}

/**
 * Tablas que referencian a una tabla dada (FK entrantes)
 * [
 *   ['tabla' => 'lineas', 'columna' => 'id_cabecera', 'columna_referenciada' => 'IdCabecera'],
 *   ...
 * ]
 */
function obtener_tablas_que_referencian($conexion, $tabla_referenciada, $bd){
  $refs = [];
  $sql = "
    SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND REFERENCED_TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla_referenciada)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $refs[] = [
        'tabla'                => $fila['TABLE_NAME'],
        'columna'              => $fila['COLUMN_NAME'],
        'columna_referenciada' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $refs;
}

/**
 * Control de formulario adecuado para una columna NO FK.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      // datetime-local espera formato 'YYYY-MM-DDThh:mm'
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}

/**
 * Renderizar tabla HTML de resultados usando la misma lógica de FKs
 * que el listado principal (para los informes).
 */
function render_tabla_html_con_links($conexion, $tabla, $rows, $bd){
  if(!$rows || count($rows) === 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }
  $foreignKeysLocal = obtener_claves_foraneas($conexion, $tabla, $bd);

  echo "<table class='report-table'>";
  // Cabecera
  $first = $rows[0];
  echo "<tr>";
  foreach($first as $k => $_){
    echo "<th>".$k."</th>";
  }
  echo "</tr>";

  // Filas
  foreach($rows as $fila){
    echo "<tr>";
    foreach($fila as $clave=>$valor){
      if(isset($foreignKeysLocal[$clave]) && $valor !== null && $valor !== ''){
        $fk = $foreignKeysLocal[$clave];
        $tabla_fk   = $fk['tabla'];
        $columna_fk = $fk['columna'];

        $sql_fk = "
          SELECT *
          FROM ".$tabla_fk."
          WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
          LIMIT 1
        ";
        $res_fk = mysqli_query($conexion, $sql_fk);
        if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
          $partes = [];
          foreach($fila_fk as $k2=>$v2){
            $partes[] = $v2;
          }
          $texto_celda = implode(" | ", $partes);
          echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
        }else{
          echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
        }
      }else{
        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
      }
    }
    echo "</tr>";
  }

  echo "</table>";
}

/**
 * Renderiza un gráfico de tipo donut (pie chart) como SVG.
 * $segmentos = [
 *   ['label' => 'Texto', 'total' => 10],
 *   ...
 * ]
 */
function render_pie_chart($segmentos, $chart_id){
  $total = 0;
  foreach($segmentos as $s){
    $total += $s['total'];
  }
  if($total <= 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }

  // Donut típico: 100 unidades de perímetro "virtual".
  $acumulado = 0.0;

  echo "<div class='chart-pie-wrapper'>";
  echo "<div class='chart-pie'>";
  echo "<svg viewBox='0 0 42 42' class='donut'>";

  // Círculo de fondo
  echo "<circle class='donut-ring' cx='21' cy='21' r='15.915'></circle>";

  $index = 0;
  foreach($segmentos as $s){
    $valor = $s['total'];
    $percent = ($valor / $total) * 100.0;
    $dasharray = $percent." ".(100 - $percent);
    $dashoffset = 25 - $acumulado; // empezamos arriba

    echo "<circle class='donut-segment segment-".$index."' cx='21' cy='21' r='15.915' ";
    echo "stroke-dasharray='".$dasharray."' stroke-dashoffset='".$dashoffset."'></circle>";

    $acumulado += $percent;
    $index++;
  }

  echo "</svg>";
  echo "</div>";

  // Leyenda
  echo "<ul class='chart-legend'>";
  $index = 0;
  foreach($segmentos as $s){
    $label = htmlspecialchars($s['label'],ENT_QUOTES);
    $valor = (int)$s['total'];
    echo "<li>";
    echo "<span class='legend-color segment-".$index."'></span>";
    echo "<span class='legend-label'>".$label."</span>";
    echo "<span class='legend-value'>(".$valor.")</span>";
    echo "</li>";
    $index++;
  }
  echo "</ul>";

  echo "</div>";
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap'); 
      :root{
        --margen: 20px;
        --color_primario: indigo;
        --color_secundario: aliceblue;
        --color_nav_fondo: #1f0033;
        --color_main_fondo: #edf0ff;
        --color_tabla_header: indigo;
        --color_tabla_borde: #b3b5e0;
        --color_tabla_fila_par: #f7f7ff;
        --color_tabla_fila_impar: #ffffff;
        --radio: 8px;

        --chart-color-0: #4b0082;
        --chart-color-1: #7b3fb0;
        --chart-color-2: #ff8c42;
        --chart-color-3: #16a085;
        --chart-color-4: #3498db;
        --chart-color-5: #c0392b;
        --chart-color-6: #2ecc71;
        --chart-color-7: #f1c40f;
      }
      *{
        box-sizing:border-box;
      }
      html,body{
        width:100%;
        height:100%;
        padding:0;
        margin:0;
        font-family:ubuntu,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      body{
        display:flex;
        background-color:#f3f4ff;
        color:#222;
      }

      /* NAV LATERAL */
      nav{
        flex:1;
        min-width:240px;
        max-width:320px;
        padding:var(--margen);
        display:flex;
        flex-direction:column;
        gap:var(--margen);
        background-color:var(--color_nav_fondo);
        box-shadow:4px 0 20px rgba(0,0,0,0.25);
        color:white;
        position:relative;
        z-index:2;
      }
      #corporativo{
        display:flex;
        color:white;
        gap:calc(var(--margen)/2);
        align-items:center;
        justify-content:space-between;
        padding-bottom:var(--margen);
        border-bottom:1px solid rgba(255,255,255,0.15);
      }
      #corporativo img{
        width:56px;
        filter:drop-shadow(0 0 6px rgba(255,255,255,0.3));
      }
      #corporativo p{
        font-size:26px;
        margin:0;
        font-weight:700;
        letter-spacing:1px;
        text-shadow:0 0 6px rgba(0,0,0,0.3);
      }
      .logout{
        background-color:rgba(240,248,255,0.1);
        color:aliceblue;
        padding:6px 12px;
        border-radius:999px;
        text-decoration:none;
        font-size:12px;
        font-weight:600;
        border:1px solid rgba(240,248,255,0.4);
        transition:all 0.2s ease;
        background: indigo;
      }
      .logout:hover{
        background-color:aliceblue;
        color:var(--color_primario);
      }
      .login-user-label{
        font-size:11px;
      
        opacity:0.85;
        margin-right:6px;
      }

      nav>button{
        background-color:rgba(240,248,255,0.08);
        color:var(--color_secundario);
        padding:10px 12px;
        border-radius:var(--radio);
        border:1px solid transparent;
        display:flex;
        justify-content: space-between;
        align-items:center;
        cursor:pointer;
        transition:all 0.2s ease;
      }
      nav>button:hover{
        background-color:rgba(240,248,255,0.18);
        border-color:rgba(240,248,255,0.4);
        transform:translateX(2px);
      }
      .activo{
        background-color: var(--color_main_fondo);
    border-color: rgba(240, 248, 255, 0.8);
    transform: translateX(4px);
    /* box-shadow: 0 0 10px rgba(240, 248, 255, 0.4); */
    color: indigo;
    width: 120%;
      }
      nav button a{
        text-decoration:none;
        color:inherit;
        font-size:13px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
      }
      .anadir{
        width: 22px;
    height: 22px;
    background-color: aliceblue;
    /* color: var(--color_primario); */
    border-radius: 50%;
    line-height: 22px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    box-shadow: 0 0 6px rgba(0, 0, 0, 0.3);
    color: white;
    background: indigo;
      }

      /* MAIN / DASHBOARD */
      main{
        flex:6;
        padding:var(--margen);
        overflow:auto;
        background-color:var(--color_main_fondo);
        position:relative;
      }
      main::before{
        content:"";
        position:absolute;
        inset:0;
        background-color:transparent;
        pointer-events:none;
        z-index:-1;
      }
      h2{
        margin-top:0;
        margin-bottom:10px;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }

      /* TABLAS */
      main table{
        width:100%;
        border:1px solid var(--color_tabla_borde);
        border-collapse:collapse;
        border-radius:var(--radio);
        overflow:hidden;
        background-color:var(--color_tabla_fila_impar);
        box-shadow:0 4px 14px rgba(0,0,0,0.06);
      }
      main table tr:nth-child(even){
        background-color:var(--color_tabla_fila_par);
      }
      main table tr:hover{
        background-color:#e4e6ff;
      }
      main table td{
        padding:10px 12px;
        vertical-align:top;
        font-size:13px;
      }
      main table th{
        background-color:var(--color_tabla_header);
        padding:10px 12px;
        color:aliceblue;
        text-align:left;
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:0.7px;
      }

      .report-table{
        margin-bottom:var(--margen);
      }
      .no-data{
        font-size:13px;
        color:#666;
      }

      /* ACCIONES */
      .eliminar,
      .editar,
      .reportar{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:24px;
        height:24px;
        border-radius:999px;
        text-decoration:none;
        color:white;
        margin-left:4px;
        font-size:12px;
        box-shadow:0 0 6px rgba(0,0,0,0.25);
        transition:transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
      }
      .eliminar{
        background-color:#c0392b;
      }
      .editar{
        background-color:#e67e22;
      }
      .reportar{
        background-color:#16a085;
      }
      .eliminar:hover,
      .editar:hover,
      .reportar:hover{
        transform:translateY(-1px) scale(1.03);
        box-shadow:0 0 10px rgba(0,0,0,0.35);
        opacity:0.95;
      }

      @keyframes aparece{
        0%{opacity:0;transform:translateX(-30px);}
        100%{opacity:1;transform:translateX(0px);}
      }

      /* FORMULARIOS */
      form{
        columns:2;
        gap:var(--margen);
        margin-top:10px;
      }
      form label{
        display:block;
        font-weight:600;
        margin-bottom:4px;
        font-size:12px;
        color:#444;
      }
      form input,
      form select{
        width:100%;
        padding:10px 12px;
        box-sizing:border-box;
        margin-bottom:var(--margen);
        border:1px solid rgba(75,0,130,0.3);
        border-radius:var(--radio);
        background-color:#ffffff;
        font-size:13px;
        transition:border 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease;
      }
      form input:focus,
      form select:focus{
        outline:none;
        border-color:var(--color_primario);
        box-shadow:0 0 0 2px rgba(75,0,130,0.15);
        background-color:#ffffff;
      }
      form input[type=checkbox]{
        width:auto;
        padding:0;
        margin-top:5px;
        box-shadow:none;
      }
      form input[type=submit]{
        background-color:var(--color_primario);
        color:white;
        cursor:pointer;
        border:none;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.8px;
        box-shadow:0 4px 10px rgba(75,0,130,0.4);
      }
      form input[type=submit]:hover{
        box-shadow:0 5px 14px rgba(75,0,130,0.6);
        transform:translateY(-1px);
      }

      /* LOGIN */
      .login-box{
        max-width:420px;
        margin:80px auto;
        background-color:#ffffff;
        padding:var(--margen);
        border-radius:16px;
        border:1px solid rgba(75,0,130,0.2);
        box-shadow:0 14px 40px rgba(0,0,0,0.18);
        column-count:1;
        position:relative;
        overflow:hidden;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .login-box form{
        columns:1;
        position:relative;
        z-index:1;
      }
      .login-error{
        background-color:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
        position:relative;
        z-index:1;
      }

      /* DASHBOARD / PIE CHARTS */
      .dashboard-intro{
        margin-bottom:var(--margen);
        font-size:14px;
        color:#555;
        max-width:700px;
      }
      .charts-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(360px,1fr));
        gap:var(--margen);
      }
      .chart{
        background-color:#ffffff;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-sizing:border-box;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        position:relative;
        overflow:hidden;
      }
      .chart h3{
        margin-top:0;
        margin-bottom:8px;
        font-size:15px;
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .chart-subtitle{
        font-size:11px;
        color:#777;
        margin-bottom:8px;
        position:relative;
        z-index:1;
      }

      .chart-pie-wrapper{
        display:flex;
        align-items:center;
        gap:12px;
      }
      .chart-pie{
        width:120px;
        height:120px;
        flex:0 0 auto;
      }
      .chart-pie svg{
        width:100%;
        height:100%;
        transform:rotate(-90deg);
      }
      .donut-ring{
        fill:none;
        stroke:#e0e2ff;
        stroke-width:10;
      }
      .donut-segment{
        fill:none;
        stroke-width:10;
      }
      .segment-0{ stroke:var(--chart-color-0); }
      .segment-1{ stroke:var(--chart-color-1); }
      .segment-2{ stroke:var(--chart-color-2); }
      .segment-3{ stroke:var(--chart-color-3); }
      .segment-4{ stroke:var(--chart-color-4); }
      .segment-5{ stroke:var(--chart-color-5); }
      .segment-6{ stroke:var(--chart-color-6); }
      .segment-7{ stroke:var(--chart-color-7); }

      .chart-legend{
        list-style:none;
        padding:0;
        margin:0;
        font-size:11px;
        color:#555;
        flex:1 1 auto;
      }
      .chart-legend li{
        display:flex;
        align-items:center;
        margin-bottom:4px;
      }
      .legend-color{
        width:10px;
        height:10px;
        border-radius:50%;
        margin-right:6px;
        flex:0 0 auto;
      }
      .legend-color.segment-0{ background-color:var(--chart-color-0); }
      .legend-color.segment-1{ background-color:var(--chart-color-1); }
      .legend-color.segment-2{ background-color:var(--chart-color-2); }
      .legend-color.segment-3{ background-color:var(--chart-color-3); }
      .legend-color.segment-4{ background-color:var(--chart-color-4); }
      .legend-color.segment-5{ background-color:var(--chart-color-5); }
      .legend-color.segment-6{ background-color:var(--chart-color-6); }
      .legend-color.segment-7{ background-color:var(--chart-color-7); }
      .legend-label{
        flex:1 1 auto;
        overflow:hidden;
        text-overflow:ellipsis;
        white-space:nowrap;
      }
      .legend-value{
        margin-left:4px;
        color:#333;
      }

      .back-link{
        margin-bottom:var(--margen);
        display:inline-block;
        text-decoration:none;
        color:var(--color_primario);
        font-size:13px;
        padding:4px 8px;
        border-radius:999px;
        background-color:#dadfff;
      }
      .back-link::before{
        content:"← ";
      }
      .subsection{
        margin-top:var(--margen);
      }
      .subsection h3{
        margin-bottom:6px;
        color:#333;
      }
      .subsection h4{
        margin:8px 0 4px;
        font-size:13px;
        color:#555;
      }

      @media (max-width:900px){
        body{flex-direction:column;}
        nav{
          flex:none;
          max-width:none;
          box-shadow:0 4px 12px rgba(0,0,0,0.2);
        }
        .chart-pie-wrapper{
          flex-direction:column;
          align-items:flex-start;
        }
      }
      #corporativo a{color:inherit;text-decoration:none;}
      #logout{position:absolute;top:10px;right:25px;color:indigo;}
    </style>
  </head>
  <body>
  
    <nav>
      <div id="corporativo">
      <a href="?">
        <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
        
          <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
          <p>jocarsa</p>
         
        </div>
         </a>
        
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual) ? "activo" : "";
            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual){
                echo "<a href='?operacion=añadir&tabla=".$tabla_actual."' class='anadir'>+</a>";
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {
          // Lógica del microERP
          if(isset($_GET['tabla'])){
            $tabla      = $_GET['tabla'];
            $operacion  = $_GET['operacion'] ?? '';
            $id         = isset($_GET['id']) ? $_GET['id'] : null; // string, no asumimos numérico

            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);
            $primaryKey   = obtener_pk_columna($conexion, $tabla, $db_name);

            // Eliminación
            if($operacion === "eliminar" && $id !== null && $primaryKey){
              $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql.";"
              );
              $operacion = '';
            }

            // AÑADIR
            if($operacion === "añadir"){
              // Procesar inserción si viene por POST
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  // tinyint(1) checkbox
                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              // Formulario de alta
              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
              echo "<h2>Añadir registro en ".$tabla."</h2>";
              echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";

              foreach($columnMeta as $nombre_columna => $meta_columna){
                if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                // FK: select
                if(isset($foreignKeys[$nombre_columna])){
                  $fk = $foreignKeys[$nombre_columna];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  echo "<label>".$nombre_columna."</label>";
                  echo "<select name='".$nombre_columna."'>";
                  echo "<option value=''>-- seleccionar --</option>";

                  $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                  if($res_fk){
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_opcion = implode(" | ", $partes);
                      $value_opcion = $fila_fk[$columna_fk];
                      echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                    }
                  }

                  echo "</select>";
                }else{
                  echo render_input_para_columna($nombre_columna, $meta_columna);
                }
              }

              echo "<input type='submit' value='Guardar'>";
              echo "</form>";

            // EDITAR
            } elseif($operacion === "editar" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede editar un registro concreto.</p>";
              } else {
                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                // Cargamos la fila actual
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<p>No se ha encontrado el registro a editar.</p>";
                } else {
                  // Procesar actualización
                  if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                    $sets = [];

                    foreach($columnMeta as $nombre_columna => $meta_columna){
                      if($nombre_columna === $primaryKey){ continue; }

                      $data_type   = strtolower($meta_columna['DATA_TYPE']);
                      $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                      // tinyint(1) checkbox
                      if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                        $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                        $sets[] = "`".$nombre_columna."`=".intval($valor);
                        continue;
                      }

                      if(isset($_POST[$nombre_columna])){
                        $valor = $_POST[$nombre_columna];
                        $sets[] = "`".$nombre_columna."` = '".mysqli_real_escape_string($conexion,$valor)."'";
                      }
                    }

                    if(count($sets) > 0){
                      $sql_update = "UPDATE ".$tabla." SET ".implode(", ",$sets)." WHERE `".$primaryKey."` = ".$id_sql;
                      mysqli_query($conexion, $sql_update);
                    }

                    // Recargar fila actualizada
                    $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                    $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : $fila_actual;
                  }

                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<h2>Editar registro en ".$tabla." (".$primaryKey." = ".htmlspecialchars($id,ENT_QUOTES).")</h2>";
                  echo "<form action='?operacion=editar&tabla=".$tabla."&id=".urlencode($id)."' method='POST'>";

                  // PK como solo lectura
                  if($primaryKey && isset($fila_actual[$primaryKey])){
                    echo "<label>".$primaryKey."</label>";
                    echo "<input type='text' value='".htmlspecialchars($fila_actual[$primaryKey],ENT_QUOTES)."' disabled>";
                  }

                  foreach($columnMeta as $nombre_columna => $meta_columna){
                    if($nombre_columna === $primaryKey){ continue; }
                    $valor_actual = $fila_actual[$nombre_columna] ?? "";

                    if(isset($foreignKeys[$nombre_columna])){
                      $fk = $foreignKeys[$nombre_columna];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      echo "<label>".$nombre_columna."</label>";
                      echo "<select name='".$nombre_columna."'>";
                      echo "<option value=''>-- seleccionar --</option>";

                      $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                      if($res_fk){
                        while($fila_fk = mysqli_fetch_assoc($res_fk)){
                          $partes = [];
                          foreach($fila_fk as $k2=>$v2){
                            $partes[] = $v2;
                          }
                          $texto_opcion = implode(" | ", $partes);
                          $value_opcion = $fila_fk[$columna_fk];
                          $selected = ($valor_actual == $value_opcion) ? "selected" : "";
                          echo "<option value='".$value_opcion."' ".$selected.">".$texto_opcion."</option>";
                        }
                      }

                      echo "</select>";
                    }else{
                      echo render_input_para_columna($nombre_columna, $meta_columna, $valor_actual);
                    }
                  }

                  echo "<input type='submit' value='Guardar cambios'>";
                  echo "</form>";
                }
              }

            // INFORME
            } elseif($operacion === "report" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede generar un informe por registro.</p>";
              } else {
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                // Fila actual
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<p>No se ha encontrado el registro solicitado.</p>";
                } else {
                  echo "<h2>Informe de ".$tabla." (".$primaryKey." = ".htmlspecialchars($id,ENT_QUOTES).")</h2>";

                  // Registro principal
                  echo "<div class='subsection'>";
                  echo "<h3>Registro principal</h3>";
                  render_tabla_html_con_links($conexion, $tabla, [$fila_actual], $db_name);
                  echo "</div>";

                  // Datos que este registro referencia (FK salientes)
                  echo "<div class='subsection'>";
                  echo "<h3>Datos referenciados por este registro</h3>";

                  $hay_referenciados = false;
                  foreach($foreignKeys as $columna_fk_local => $info_fk){
                    $valor_fk = $fila_actual[$columna_fk_local] ?? null;
                    if($valor_fk === null || $valor_fk === ''){ continue; }

                    $tabla_fk   = $info_fk['tabla'];
                    $col_fk     = $info_fk['columna'];

                    $sql_fk = "SELECT * FROM ".$tabla_fk." WHERE ".$col_fk." = '".mysqli_real_escape_string($conexion,$valor_fk)."'";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && mysqli_num_rows($res_fk) > 0){
                      $hay_referenciados = true;
                      $rows_fk = [];
                      while($row_fk = mysqli_fetch_assoc($res_fk)){
                        $rows_fk[] = $row_fk;
                      }

                      echo "<h4>".$tabla_fk." (por ".$columna_fk_local.")</h4>";
                      render_tabla_html_con_links($conexion, $tabla_fk, $rows_fk, $db_name);
                    }
                  }
                  if(!$hay_referenciados){
                    echo "<p class='no-data'>No hay referencias salientes.</p>";
                  }
                  echo "</div>";

                  // Tablas que referencian a este registro (FK entrantes)
                  echo "<div class='subsection'>";
                  echo "<h3>Datos relacionados que apuntan a este registro</h3>";

                  $refs_entrantes = obtener_tablas_que_referencian($conexion, $tabla, $db_name);
                  if(count($refs_entrantes) === 0){
                    echo "<p class='no-data'>No hay tablas que referencien a esta entidad.</p>";
                  } else {
                    $hay_entrantes = false;
                    foreach($refs_entrantes as $ref){
                      $tabla_hija        = $ref['tabla'];
                      $columna_hija      = $ref['columna'];
                      $col_ref_padre     = $ref['columna_referenciada'];

                      $valor_ref_padre = $fila_actual[$col_ref_padre] ?? null;
                      if($valor_ref_padre === null){ continue; }

                      $sql_hija = "SELECT * FROM ".$tabla_hija." WHERE ".$columna_hija." = '".mysqli_real_escape_string($conexion,$valor_ref_padre)."'";
                      $res_hija = mysqli_query($conexion, $sql_hija);
                      if($res_hija && mysqli_num_rows($res_hija) > 0){
                        $hay_entrantes = true;
                        $rows_hija = [];
                        while($fila_hija = mysqli_fetch_assoc($res_hija)){
                          $rows_hija[] = $fila_hija;
                        }

                        echo "<h4>".$tabla_hija." (columna ".$columna_hija.")</h4>";
                        render_tabla_html_con_links($conexion, $tabla_hija, $rows_hija, $db_name);
                      }
                    }
                    if(!$hay_entrantes){
                      echo "<p class='no-data'>No hay registros entrantes que apunten a este registro.</p>";
                    }
                  }

                  echo "</div>";
                }
              }

            // LISTADO
            } else {
              echo "<h2>Listado de ".$tabla."</h2>";
              if(!$primaryKey){
                echo "<p class='no-data'>Aviso: la tabla <b>".$tabla."</b> no tiene clave primaria definida. No se podrán editar ni eliminar registros individualmente.</p>";
              }
              echo "<table>";
              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $contador = 0;
              while($fila = mysqli_fetch_assoc($resultado)){
                if($contador == 0){
                  echo "<tr>";
                    foreach($fila as $clave=>$valor){
                      echo "<th>".$clave."</th>";
                    }
                    echo "<th>Acciones</th>";
                  echo "</tr>";
                }

                echo "<tr>";
                foreach($fila as $clave=>$valor){
                  // Si es FK, mostramos fila referenciada
                  if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                    $fk = $foreignKeys[$clave];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    $sql_fk = "
                      SELECT *
                      FROM ".$tabla_fk."
                      WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                      LIMIT 1
                    ";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_celda = implode(" | ", $partes);
                      echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
                    }else{
                      echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                    }
                  }else{
                    echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                  }
                }

                // Acciones: editar, informe, eliminar (solo si hay PK)
                echo "<td>";
                if($primaryKey && isset($fila[$primaryKey])){
                  $id_fila = $fila[$primaryKey];
                  $id_url  = urlencode($id_fila);
                  echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                  echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                  echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                } else {
                  echo "<span style='font-size:11px;color:#777;'>—</span>";
                }
                echo "</td>";

                echo "</tr>";

                $contador++;
              }
              echo "</table>";
            }
          } else {
            // DASHBOARD INICIAL: gráficos de campos ENUM/SET y FKs como PIE
            echo "<h2>Dashboard de microERP</h2>";
            echo "<p class='dashboard-intro'>
              Resumen gráfico de la información categórica y relacional del sistema:
              campos <b>ENUM/SET</b> y campos de <b>clave foránea</b> en todas las tablas, representados como gráficos de tipo donut.
            </p>";

            $resultado = mysqli_query($conexion, "SHOW TABLES;");
            echo "<div class='charts-grid'>";
            while($fila = mysqli_fetch_assoc($resultado)){
              $tabla = array_values($fila)[0];
              $meta  = obtener_meta_columnas($conexion, $tabla, $db_name);
              $fksTabla = obtener_claves_foraneas($conexion, $tabla, $db_name);

              // 1) Campos ENUM/SET
              foreach($meta as $nombre_columna => $meta_columna){
                $data_type = strtolower($meta_columna['DATA_TYPE']);
                if($data_type !== 'enum' && $data_type !== 'set'){ continue; }

                $sql_dist = "
                  SELECT ".$nombre_columna." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$nombre_columna."
                  ORDER BY total DESC
                ";
                $res_dist = mysqli_query($conexion, $sql_dist);
                if(!$res_dist || mysqli_num_rows($res_dist) < 1){ continue; }

                $segmentos = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist)){
                  $v = $fila_dist['valor'];
                  $c = (int)$fila_dist['total'];
                  $segmentos[] = [
                    'label' => ($v === null || $v === '' ? '(vacío)' : $v),
                    'total' => $c
                  ];
                }
                if(empty($segmentos)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$nombre_columna."</h3>";
                echo "<div class='chart-subtitle'>Distribución de valores ENUM/SET</div>";
                render_pie_chart($segmentos, $tabla."_".$nombre_columna."_enum");
                echo "</div>";
              }

              // 2) Campos FK: distribución por valor referenciado
              foreach($fksTabla as $columna_fk => $info_fk){
                $tabla_ref = $info_fk['tabla'];
                $col_ref   = $info_fk['columna'];

                $sql_dist_fk = "
                  SELECT ".$columna_fk." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$columna_fk."
                  ORDER BY total DESC
                ";
                $res_dist_fk = mysqli_query($conexion, $sql_dist_fk);
                if(!$res_dist_fk || mysqli_num_rows($res_dist_fk) < 1){ continue; }

                $segmentos_fk = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist_fk)){
                  $valor_fk = $fila_dist['valor'];
                  $c        = (int)$fila_dist['total'];

                  if($valor_fk === null || $valor_fk === ''){
                    $label = '(sin valor)';
                  }else{
                    // Miramos fila referenciada para label
                    $sql_ref = "
                      SELECT *
                      FROM ".$tabla_ref."
                      WHERE ".$col_ref." = '".mysqli_real_escape_string($conexion,$valor_fk)."'
                      LIMIT 1
                    ";
                    $res_ref = mysqli_query($conexion, $sql_ref);
                    if($res_ref && $fila_ref = mysqli_fetch_assoc($res_ref)){
                      $partes = [];
                      foreach($fila_ref as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $label = implode(" | ", $partes);
                    }else{
                      $label = 'ID '.$valor_fk.' (huérfano)';
                    }
                  }

                  $segmentos_fk[] = [
                    'label' => $label,
                    'total' => $c
                  ];
                }
                if(empty($segmentos_fk)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$columna_fk."</h3>";
                echo "<div class='chart-subtitle'>Distribución por referencia a ".$tabla_ref."</div>";
                render_pie_chart($segmentos_fk, $tabla."_".$columna_fk."_fk");
                echo "</div>";
              }
            }
            echo "</div>";
          }
        }
      ?>
    </main>
    <?php if($logged_in): ?>
          <div id="logout">
            <span class="login-user-label"><?php echo htmlspecialchars($_SESSION['usuario']); ?></span>
            <a href="?logout=1" class="logout">Salir</a>
          </div>
        <?php endif; ?>
  </body>
</html>
```

### ajustes

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "tienda2526";
$db_user = "tienda2526";
$db_pass = "tienda2526";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: ?");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: ?");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * FKs salientes desde una tabla:
 * [
 *   'id_cliente' => ['tabla' => 'clientes', 'columna' => 'Identificador'],
 *   ...
 * ]
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Metadatos de columnas de una tabla.
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Obtener nombre de la columna PK (primer PRIMARY KEY definido).
 * Devuelve null si la tabla no tiene PK.
 */
function obtener_pk_columna($conexion, $tabla, $bd){
  $sql = "
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND COLUMN_KEY = 'PRI'
    ORDER BY ORDINAL_POSITION
    LIMIT 1
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado && $fila = mysqli_fetch_assoc($resultado)){
    return $fila['COLUMN_NAME'];
  }
  return null;
}

/**
 * Tablas que referencian a una tabla dada (FK entrantes)
 * [
 *   ['tabla' => 'lineas', 'columna' => 'id_cabecera', 'columna_referenciada' => 'IdCabecera'],
 *   ...
 * ]
 */
function obtener_tablas_que_referencian($conexion, $tabla_referenciada, $bd){
  $refs = [];
  $sql = "
    SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND REFERENCED_TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla_referenciada)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $refs[] = [
        'tabla'                => $fila['TABLE_NAME'],
        'columna'              => $fila['COLUMN_NAME'],
        'columna_referenciada' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $refs;
}

/**
 * Control de formulario adecuado para una columna NO FK.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      // datetime-local espera formato 'YYYY-MM-DDThh:mm'
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}

/**
 * Renderizar tabla HTML de resultados usando la misma lógica de FKs
 * que el listado principal (para los informes).
 */
function render_tabla_html_con_links($conexion, $tabla, $rows, $bd){
  if(!$rows || count($rows) === 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }
  $foreignKeysLocal = obtener_claves_foraneas($conexion, $tabla, $bd);

  echo "<table class='report-table'>";
  // Cabecera
  $first = $rows[0];
  echo "<tr>";
  foreach($first as $k => $_){
    echo "<th>".$k."</th>";
  }
  echo "</tr>";

  // Filas
  foreach($rows as $fila){
    echo "<tr>";
    foreach($fila as $clave=>$valor){
      if(isset($foreignKeysLocal[$clave]) && $valor !== null && $valor !== ''){
        $fk = $foreignKeysLocal[$clave];
        $tabla_fk   = $fk['tabla'];
        $columna_fk = $fk['columna'];

        $sql_fk = "
          SELECT *
          FROM ".$tabla_fk."
          WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
          LIMIT 1
        ";
        $res_fk = mysqli_query($conexion, $sql_fk);
        if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
          $partes = [];
          foreach($fila_fk as $k2=>$v2){
            $partes[] = $v2;
          }
          $texto_celda = implode(" | ", $partes);
          echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
        }else{
          echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
        }
      }else{
        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
      }
    }
    echo "</tr>";
  }

  echo "</table>";
}

/**
 * Renderiza un gráfico de tipo donut (pie chart) como SVG.
 * $segmentos = [
 *   ['label' => 'Texto', 'total' => 10],
 *   ...
 * ]
 */
function render_pie_chart($segmentos, $chart_id){
  $total = 0;
  foreach($segmentos as $s){
    $total += $s['total'];
  }
  if($total <= 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }

  // Donut típico: 100 unidades de perímetro "virtual".
  $acumulado = 0.0;

  echo "<div class='chart-pie-wrapper'>";
  echo "<div class='chart-pie'>";
  echo "<svg viewBox='0 0 42 42' class='donut'>";

  // Círculo de fondo
  echo "<circle class='donut-ring' cx='21' cy='21' r='15.915'></circle>";

  $index = 0;
  foreach($segmentos as $s){
    $valor = $s['total'];
    $percent = ($valor / $total) * 100.0;
    $dasharray = $percent." ".(100 - $percent);
    $dashoffset = 25 - $acumulado; // empezamos arriba

    echo "<circle class='donut-segment segment-".$index."' cx='21' cy='21' r='15.915' ";
    echo "stroke-dasharray='".$dasharray."' stroke-dashoffset='".$dashoffset."'></circle>";

    $acumulado += $percent;
    $index++;
  }

  echo "</svg>";
  echo "</div>";

  // Leyenda
  echo "<ul class='chart-legend'>";
  $index = 0;
  foreach($segmentos as $s){
    $label = htmlspecialchars($s['label'],ENT_QUOTES);
    $valor = (int)$s['total'];
    echo "<li>";
    echo "<span class='legend-color segment-".$index."'></span>";
    echo "<span class='legend-label'>".$label."</span>";
    echo "<span class='legend-value'>(".$valor.")</span>";
    echo "</li>";
    $index++;
  }
  echo "</ul>";

  echo "</div>";
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap'); 
      :root{
        --margen: 20px;
        --color_primario: indigo;
        --color_secundario: aliceblue;
        --color_nav_fondo: #1f0033;
        --color_main_fondo: #edf0ff;
        --color_tabla_header: indigo;
        --color_tabla_borde: #b3b5e0;
        --color_tabla_fila_par: #f7f7ff;
        --color_tabla_fila_impar: #ffffff;
        --radio: 8px;

        --chart-color-0: #4b0082;
        --chart-color-1: #7b3fb0;
        --chart-color-2: #ff8c42;
        --chart-color-3: #16a085;
        --chart-color-4: #3498db;
        --chart-color-5: #c0392b;
        --chart-color-6: #2ecc71;
        --chart-color-7: #f1c40f;
      }
      *{
        box-sizing:border-box;
      }
      html,body{
        width:100%;
        height:100%;
        padding:0;
        margin:0;
        font-family:ubuntu,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      body{
        display:flex;
        background-color:#f3f4ff;
        color:#222;
      }

      /* NAV LATERAL */
      nav{
        flex:1;
        min-width:240px;
        max-width:320px;
        padding:var(--margen);
        display:flex;
        flex-direction:column;
        gap:var(--margen);
        background-color:var(--color_nav_fondo);
        box-shadow:4px 0 20px rgba(0,0,0,0.25);
        color:white;
        position:relative;
        z-index:2;
      }
      #corporativo{
        display:flex;
        color:white;
        gap:calc(var(--margen)/2);
        align-items:center;
        justify-content:space-between;
        padding-bottom:var(--margen);
        border-bottom:1px solid rgba(255,255,255,0.15);
      }
      #corporativo img{
        width:56px;
        filter:drop-shadow(0 0 6px rgba(255,255,255,0.3));
      }
      #corporativo p{
        font-size:26px;
        margin:0;
        font-weight:700;
        letter-spacing:1px;
        text-shadow:0 0 6px rgba(0,0,0,0.3);
      }
      .logout{
        background-color:rgba(240,248,255,0.1);
        color:aliceblue;
        padding:6px 12px;
        border-radius:999px;
        text-decoration:none;
        font-size:12px;
        font-weight:600;
        border:1px solid rgba(240,248,255,0.4);
        transition:all 0.2s ease;
        background: indigo;
      }
      .logout:hover{
        background-color:aliceblue;
        color:var(--color_primario);
      }
      .login-user-label{
        font-size:11px;
        opacity:0.85;
        margin-right:6px;
      }

      nav>button{
        background-color:rgba(240,248,255,0.08);
        color:var(--color_secundario);
        padding:10px 12px;
        border-radius:var(--radio);
        border:1px solid transparent;
        display:flex;
        justify-content: space-between;
        align-items:center;
        cursor:pointer;
        transition:all 0.2s ease;
      }
      nav>button:hover{
        background-color:rgba(240,248,255,0.18);
        border-color:rgba(240,248,255,0.4);
        transform:translateX(2px);
      }
      .activo{
        background-color: var(--color_main_fondo);
        border-color: rgba(240, 248, 255, 0.8);
        transform: translateX(4px);
        color: indigo;
        width: 120%;
      }
      nav button a{
        text-decoration:none;
        color:inherit;
        font-size:13px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
      }
      .anadir{
        width: 22px;
        height: 22px;
        background-color: aliceblue;
        border-radius: 50%;
        line-height: 22px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 6px rgba(0, 0, 0, 0.3);
        color: white;
        background: indigo;
      }

      /* MAIN / DASHBOARD */
      main{
        flex:6;
        padding:var(--margen);
        overflow:auto;
        background-color:var(--color_main_fondo);
        position:relative;
      }
      main::before{
        content:"";
        position:absolute;
        inset:0;
        background-color:transparent;
        pointer-events:none;
        z-index:-1;
      }
      h2{
        margin-top:0;
        margin-bottom:10px;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }

      /* HEADER PRINCIPAL EN MAIN */
      .main-header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:var(--margen);
      }
      .main-title{
        font-size:20px;
        font-weight:600;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }
      .main-actions{
        display:flex;
        align-items:center;
        gap:8px;
      }
      .view-toggle{
        border:1px solid rgba(75,0,130,0.4);
        background-color:transparent;
        color:var(--color_primario);
        padding:6px 10px;
        border-radius:999px;
        font-size:11px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
        cursor:pointer;
        transition:all 0.15s ease;
      }
      .view-toggle:hover{
        background-color:#dadfff;
      }
      .view-toggle.active{
        background-color:var(--color_primario);
        color:white;
      }

      /* TABLAS */
      main table{
        width:100%;
        border:1px solid var(--color_tabla_borde);
        border-collapse:collapse;
        border-radius:var(--radio);
        overflow:hidden;
        background-color:var(--color_tabla_fila_impar);
        box-shadow:0 4px 14px rgba(0,0,0,0.06);
      }
      main table tr:nth-child(even){
        background-color:var(--color_tabla_fila_par);
      }
      main table tr:hover{
        background-color:#e4e6ff;
      }
      main table td{
        padding:10px 12px;
        vertical-align:top;
        font-size:13px;
      }
      main table th{
        background-color:var(--color_tabla_header);
        padding:10px 12px;
        color:aliceblue;
        text-align:left;
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:0.7px;
      }

      .report-table{
        margin-bottom:var(--margen);
      }
      .no-data{
        font-size:13px;
        color:#666;
      }

      /* ACCIONES */
      .eliminar,
      .editar,
      .reportar{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:24px;
        height:24px;
        border-radius:999px;
        text-decoration:none;
        color:white;
        margin-left:4px;
        font-size:12px;
        box-shadow:0 0 6px rgba(0,0,0,0.25);
        transition:transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
      }
      .eliminar{
        background-color:#c0392b;
      }
      .editar{
        background-color:#e67e22;
      }
      .reportar{
        background-color:#16a085;
      }
      .eliminar:hover,
      .editar:hover,
      .reportar:hover{
        transform:translateY(-1px) scale(1.03);
        box-shadow:0 0 10px rgba(0,0,0,0.35);
        opacity:0.95;
      }

      @keyframes aparece{
        0%{opacity:0;transform:translateX(-30px);}
        100%{opacity:1;transform:translateX(0px);}
      }

      /* FORMULARIOS */
      form{
        columns:2;
        gap:var(--margen);
        margin-top:10px;
      }
      form label{
        display:block;
        font-weight:600;
        margin-bottom:4px;
        font-size:12px;
        color:#444;
      }
      form input,
      form select{
        width:100%;
        padding:10px 12px;
        box-sizing:border-box;
        margin-bottom:var(--margen);
        border:1px solid rgba(75,0,130,0.3);
        border-radius:var(--radio);
        background-color:#ffffff;
        font-size:13px;
        transition:border 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease;
      }
      form input:focus,
      form select:focus{
        outline:none;
        border-color:var(--color_primario);
        box-shadow:0 0 0 2px rgba(75,0,130,0.15);
        background-color:#ffffff;
      }
      form input[type=checkbox]{
        width:auto;
        padding:0;
        margin-top:5px;
        box-shadow:none;
      }
      form input[type=submit]{
        background-color:var(--color_primario);
        color:white;
        cursor:pointer;
        border:none;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.8px;
        box-shadow:0 4px 10px rgba(75,0,130,0.4);
      }
      form input[type=submit]:hover{
        box-shadow:0 5px 14px rgba(75,0,130,0.6);
        transform:translateY(-1px);
      }

      /* LOGIN */
      .login-box{
        max-width:420px;
        margin:80px auto;
        background-color:#ffffff;
        padding:var(--margen);
        border-radius:16px;
        border:1px solid rgba(75,0,130,0.2);
        box-shadow:0 14px 40px rgba(0,0,0,0.18);
        column-count:1;
        position:relative;
        overflow:hidden;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .login-box form{
        columns:1;
        position:relative;
        z-index:1;
      }
      .login-error{
        background-color:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
        position:relative;
        z-index:1;
      }

      /* DASHBOARD / PIE CHARTS */
      .dashboard-intro{
        margin-bottom:var(--margen);
        font-size:14px;
        color:#555;
        max-width:700px;
      }
      .charts-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(360px,1fr));
        gap:var(--margen);
      }
      .chart{
        background-color:#ffffff;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-sizing:border-box;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        position:relative;
        overflow:hidden;
      }
      .chart h3{
        margin-top:0;
        margin-bottom:8px;
        font-size:15px;
        color:var(--color_primario);
        position:relative;
        z-index:1;
      }
      .chart-subtitle{
        font-size:11px;
        color:#777;
        margin-bottom:8px;
        position:relative;
        z-index:1;
      }

      .chart-pie-wrapper{
        display:flex;
        align-items:center;
        gap:12px;
      }
      .chart-pie{
        width:120px;
        height:120px;
        flex:0 0 auto;
      }
      .chart-pie svg{
        width:100%;
        height:100%;
        transform:rotate(-90deg);
      }
      .donut-ring{
        fill:none;
        stroke:#e0e2ff;
        stroke-width:10;
      }
      .donut-segment{
        fill:none;
        stroke-width:10;
      }
      .segment-0{ stroke:var(--chart-color-0); }
      .segment-1{ stroke:var(--chart-color-1); }
      .segment-2{ stroke:var(--chart-color-2); }
      .segment-3{ stroke:var(--chart-color-3); }
      .segment-4{ stroke:var(--chart-color-4); }
      .segment-5{ stroke:var(--chart-color-5); }
      .segment-6{ stroke:var(--chart-color-6); }
      .segment-7{ stroke:var(--chart-color-7); }

      .chart-legend{
        list-style:none;
        padding:0;
        margin:0;
        font-size:11px;
        color:#555;
        flex:1 1 auto;
      }
      .chart-legend li{
        display:flex;
        align-items:center;
        margin-bottom:4px;
      }
      .legend-color{
        width:10px;
        height:10px;
        border-radius:50%;
        margin-right:6px;
        flex:0 0 auto;
      }
      .legend-color.segment-0{ background-color:var(--chart-color-0); }
      .legend-color.segment-1{ background-color:var(--chart-color-1); }
      .legend-color.segment-2{ background-color:var(--chart-color-2); }
      .legend-color.segment-3{ background-color:var(--chart-color-3); }
      .legend-color.segment-4{ background-color:var(--chart-color-4); }
      .legend-color.segment-5{ background-color:var(--chart-color-5); }
      .legend-color.segment-6{ background-color:var(--chart-color-6); }
      .legend-color.segment-7{ background-color:var(--chart-color-7); }
      .legend-label{
        flex:1 1 auto;
        overflow:hidden;
        text-overflow:ellipsis;
        white-space:nowrap;
      }
      .legend-value{
        margin-left:4px;
        color:#333;
      }

      .back-link{
        margin-bottom:var(--margen);
        display:inline-block;
        text-decoration:none;
        color:var(--color_primario);
        font-size:13px;
        padding:4px 8px;
        border-radius:999px;
        background-color:#dadfff;
      }
      .back-link::before{
        content:"← ";
      }
      .subsection{
        margin-top:var(--margen);
      }
      .subsection h3{
        margin-bottom:6px;
        color:#333;
      }
      .subsection h4{
        margin:8px 0 4px;
        font-size:13px;
        color:#555;
      }

      /* VISTAS TABLA / TARJETAS */
      .vista-activa{display:block;}
      .vista-oculta{display:none;}

      .cards-container{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
        gap:var(--margen);
      }
      .card-registro{
        background-color:#ffffff;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        display:flex;
        flex-direction:column;
        justify-content:space-between;
      }
      .card-fields{
        margin-bottom:10px;
      }
      .card-field{
        margin-bottom:6px;
        font-size:12px;
      }
      .card-field-label{
        font-weight:600;
        color:#555;
        margin-bottom:2px;
      }
      .card-field-value{
        color:#222;
        word-break:break-word;
      }
      .card-actions{
        align-self:flex-end;
        margin-top:8px;
      }
      .card-actions .eliminar,
      .card-actions .editar,
      .card-actions .reportar{
        margin-left:0;
        margin-right:4px;
      }

      @media (max-width:900px){
        body{flex-direction:column;}
        nav{
          flex:none;
          max-width:none;
          box-shadow:0 4px 12px rgba(0,0,0,0.2);
        }
        .chart-pie-wrapper{
          flex-direction:column;
          align-items:flex-start;
        }
      }
      #corporativo a{color:inherit;text-decoration:none;}
    </style>
  </head>
  <body>
  
    <nav>
      <div id="corporativo">
      <a href="?">
        <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
        
          <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
          <p>jocarsa</p>
         
        </div>
         </a>
        
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual_nav = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual_nav) ? "activo" : "";
            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual_nav){
                echo "<a href='?operacion=añadir&tabla=".$tabla_actual_nav."' class='anadir'>+</a>";
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {

          // --------- HEADER PRINCIPAL DINÁMICO EN MAIN ----------
          $tabla_header     = $_GET['tabla']     ?? null;
          $operacion_header = $_GET['operacion'] ?? '';
          $page_title = "Dashboard de microERP";

          if($tabla_header){
            switch($operacion_header){
              case 'añadir':
                $page_title = "Añadir registro en ".$tabla_header;
                break;
              case 'editar':
                $page_title = "Editar registro en ".$tabla_header;
                break;
              case 'report':
                $page_title = "Informe de ".$tabla_header;
                break;
              default:
                $page_title = "Listado de ".$tabla_header;
            }
          }

          echo "<header class='main-header'>";
          echo "<div class='main-title'>".$page_title."</div>";
          echo "<div class='main-actions'>";

          // Botones de cambio de vista solo en listados simples
          if($tabla_header && $operacion_header === ''){
            echo "<button type='button' id='btn-vista-tabla' class='view-toggle active'>Tabla</button>";
            echo "<button type='button' id='btn-vista-tarjetas' class='view-toggle'>Tarjetas</button>";
          }

          echo "<span class='login-user-label'>".htmlspecialchars($_SESSION['usuario'])."</span>";
          echo "<a href='?logout=1' class='logout'>Salir</a>";
          echo "</div>";
          echo "</header>";
          // -----------------------------------------------------

          // Lógica del microERP
          if(isset($_GET['tabla'])){
            $tabla      = $_GET['tabla'];
            $operacion  = $_GET['operacion'] ?? '';
            $id         = isset($_GET['id']) ? $_GET['id'] : null; // string, no asumimos numérico

            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);
            $primaryKey   = obtener_pk_columna($conexion, $tabla, $db_name);

            // Eliminación
            if($operacion === "eliminar" && $id !== null && $primaryKey){
              $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql.";"
              );
              $operacion = '';
            }

            // AÑADIR
            if($operacion === "añadir"){
              // Procesar inserción si viene por POST
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  // tinyint(1) checkbox
                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              // Formulario de alta
              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
              echo "<form action='?operacion=añadir&tabla=".$tabla."' method='POST'>";

              foreach($columnMeta as $nombre_columna => $meta_columna){
                if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                // FK: select
                if(isset($foreignKeys[$nombre_columna])){
                  $fk = $foreignKeys[$nombre_columna];
                  $tabla_fk   = $fk['tabla'];
                  $columna_fk = $fk['columna'];

                  echo "<label>".$nombre_columna."</label>";
                  echo "<select name='".$nombre_columna."'>";
                  echo "<option value=''>-- seleccionar --</option>";

                  $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                  if($res_fk){
                    while($fila_fk = mysqli_fetch_assoc($res_fk)){
                      $partes = [];
                      foreach($fila_fk as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $texto_opcion = implode(" | ", $partes);
                      $value_opcion = $fila_fk[$columna_fk];
                      echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                    }
                  }

                  echo "</select>";
                }else{
                  echo render_input_para_columna($nombre_columna, $meta_columna);
                }
              }

              echo "<input type='submit' value='Guardar'>";
              echo "</form>";

            // EDITAR
            } elseif($operacion === "editar" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede editar un registro concreto.</p>";
              } else {
                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                // Cargamos la fila actual
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<p>No se ha encontrado el registro a editar.</p>";
                } else {
                  // Procesar actualización
                  if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                    $sets = [];

                    foreach($columnMeta as $nombre_columna => $meta_columna){
                      if($nombre_columna === $primaryKey){ continue; }

                      $data_type   = strtolower($meta_columna['DATA_TYPE']);
                      $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                      // tinyint(1) checkbox
                      if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                        $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                        $sets[] = "`".$nombre_columna."`=".intval($valor);
                        continue;
                      }

                      if(isset($_POST[$nombre_columna])){
                        $valor = $_POST[$nombre_columna];
                        $sets[] = "`".$nombre_columna."` = '".mysqli_real_escape_string($conexion,$valor)."'";
                      }
                    }

                    if(count($sets) > 0){
                      $sql_update = "UPDATE ".$tabla." SET ".implode(", ",$sets)." WHERE `".$primaryKey."` = ".$id_sql;
                      mysqli_query($conexion, $sql_update);
                    }

                    // Recargar fila actualizada
                    $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                    $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : $fila_actual;
                  }

                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<form action='?operacion=editar&tabla=".$tabla."&id=".urlencode($id)."' method='POST'>";

                  // PK como solo lectura
                  if($primaryKey && isset($fila_actual[$primaryKey])){
                    echo "<label>".$primaryKey."</label>";
                    echo "<input type='text' value='".htmlspecialchars($fila_actual[$primaryKey],ENT_QUOTES)."' disabled>";
                  }

                  foreach($columnMeta as $nombre_columna => $meta_columna){
                    if($nombre_columna === $primaryKey){ continue; }
                    $valor_actual = $fila_actual[$nombre_columna] ?? "";

                    if(isset($foreignKeys[$nombre_columna])){
                      $fk = $foreignKeys[$nombre_columna];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      echo "<label>".$nombre_columna."</label>";
                      echo "<select name='".$nombre_columna."'>";
                      echo "<option value=''>-- seleccionar --</option>";

                      $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                      if($res_fk){
                        while($fila_fk = mysqli_fetch_assoc($res_fk)){
                          $partes = [];
                          foreach($fila_fk as $k2=>$v2){
                            $partes[] = $v2;
                          }
                          $texto_opcion = implode(" | ", $partes);
                          $value_opcion = $fila_fk[$columna_fk];
                          $selected = ($valor_actual == $value_opcion) ? "selected" : "";
                          echo "<option value='".$value_opcion."' ".$selected.">".$texto_opcion."</option>";
                        }
                      }

                      echo "</select>";
                    }else{
                      echo render_input_para_columna($nombre_columna, $meta_columna, $valor_actual);
                    }
                  }

                  echo "<input type='submit' value='Guardar cambios'>";
                  echo "</form>";
                }
              }

            // INFORME
            } elseif($operacion === "report" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede generar un informe por registro.</p>";
              } else {
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                // Fila actual
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<p>No se ha encontrado el registro solicitado.</p>";
                } else {
                  echo "<div class='subsection'>";
                  echo "<h3>Registro principal</h3>";
                  render_tabla_html_con_links($conexion, $tabla, [$fila_actual], $db_name);
                  echo "</div>";

                  // Datos que este registro referencia (FK salientes)
                  echo "<div class='subsection'>";
                  echo "<h3>Datos referenciados por este registro</h3>";

                  $hay_referenciados = false;
                  foreach($foreignKeys as $columna_fk_local => $info_fk){
                    $valor_fk = $fila_actual[$columna_fk_local] ?? null;
                    if($valor_fk === null || $valor_fk === ''){ continue; }

                    $tabla_fk   = $info_fk['tabla'];
                    $col_fk     = $info_fk['columna'];

                    $sql_fk = "SELECT * FROM ".$tabla_fk." WHERE ".$col_fk." = '".mysqli_real_escape_string($conexion,$valor_fk)."'";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && mysqli_num_rows($res_fk) > 0){
                      $hay_referenciados = true;
                      $rows_fk = [];
                      while($row_fk = mysqli_fetch_assoc($res_fk)){
                        $rows_fk[] = $row_fk;
                      }

                      echo "<h4>".$tabla_fk." (por ".$columna_fk_local.")</h4>";
                      render_tabla_html_con_links($conexion, $tabla_fk, $rows_fk, $db_name);
                    }
                  }
                  if(!$hay_referenciados){
                    echo "<p class='no-data'>No hay referencias salientes.</p>";
                  }
                  echo "</div>";

                  // Tablas que referencian a este registro (FK entrantes)
                  echo "<div class='subsection'>";
                  echo "<h3>Datos relacionados que apuntan a este registro</h3>";

                  $refs_entrantes = obtener_tablas_que_referencian($conexion, $tabla, $db_name);
                  if(count($refs_entrantes) === 0){
                    echo "<p class='no-data'>No hay tablas que referencien a esta entidad.</p>";
                  } else {
                    $hay_entrantes = false;
                    foreach($refs_entrantes as $ref){
                      $tabla_hija        = $ref['tabla'];
                      $columna_hija      = $ref['columna'];
                      $col_ref_padre     = $ref['columna_referenciada'];

                      $valor_ref_padre = $fila_actual[$col_ref_padre] ?? null;
                      if($valor_ref_padre === null){ continue; }

                      $sql_hija = "SELECT * FROM ".$tabla_hija." WHERE ".$columna_hija." = '".mysqli_real_escape_string($conexion,$valor_ref_padre)."'";
                      $res_hija = mysqli_query($conexion, $sql_hija);
                      if($res_hija && mysqli_num_rows($res_hija) > 0){
                        $hay_entrantes = true;
                        $rows_hija = [];
                        while($fila_hija = mysqli_fetch_assoc($res_hija)){
                          $rows_hija[] = $fila_hija;
                        }

                        echo "<h4>".$tabla_hija." (columna ".$columna_hija.")</h4>";
                        render_tabla_html_con_links($conexion, $tabla_hija, $rows_hija, $db_name);
                      }
                    }
                    if(!$hay_entrantes){
                      echo "<p class='no-data'>No hay registros entrantes que apunten a este registro.</p>";
                    }
                  }

                  echo "</div>";
                }
              }

            // LISTADO
            } else {
              if(!$primaryKey){
                echo "<p class='no-data'>Aviso: la tabla <b>".$tabla."</b> no tiene clave primaria definida. No se podrán editar ni eliminar registros individualmente.</p>";
              }

              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $rows = [];
              if($resultado){
                while($fila = mysqli_fetch_assoc($resultado)){
                  $rows[] = $fila;
                }
              }

              if(count($rows) === 0){
                echo "<p class='no-data'>No hay registros en esta tabla.</p>";
              } else {

                // VISTA TABLA
                echo "<div id='vista-tabla' class='vista-activa'>";
                echo "<table>";
                $contador = 0;
                foreach($rows as $fila){
                  if($contador == 0){
                    echo "<tr>";
                      foreach($fila as $clave=>$valor){
                        echo "<th>".$clave."</th>";
                      }
                      echo "<th>Acciones</th>";
                    echo "</tr>";
                  }

                  echo "<tr>";
                  foreach($fila as $clave=>$valor){
                    // Si es FK, mostramos fila referenciada
                    if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                      $fk = $foreignKeys[$clave];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      $sql_fk = "
                        SELECT *
                        FROM ".$tabla_fk."
                        WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                        LIMIT 1
                      ";
                      $res_fk = mysqli_query($conexion, $sql_fk);
                      if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $texto_celda = implode(" | ", $partes);
                        echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
                      }else{
                        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                      }
                    }else{
                      echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                    }
                  }

                  // Acciones: editar, informe, eliminar (solo si hay PK)
                  echo "<td>";
                  if($primaryKey && isset($fila[$primaryKey])){
                    $id_fila = $fila[$primaryKey];
                    $id_url  = urlencode($id_fila);
                    echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                    echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                    echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                  } else {
                    echo "<span style='font-size:11px;color:#777;'>—</span>";
                  }
                  echo "</td>";

                  echo "</tr>";

                  $contador++;
                }
                echo "</table>";
                echo "</div>";

                // VISTA TARJETAS
                echo "<div id='vista-tarjetas' class='vista-oculta'>";
                echo "<div class='cards-container'>";
                foreach($rows as $fila){
                  echo "<article class='card-registro'>";
                  echo "<div class='card-fields'>";
                  foreach($fila as $clave=>$valor){
                    echo "<div class='card-field'>";
                    echo "<div class='card-field-label'>".$clave."</div>";

                    $display_value = $valor;

                    if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                      $fk = $foreignKeys[$clave];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      $sql_fk = "
                        SELECT *
                        FROM ".$tabla_fk."
                        WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                        LIMIT 1
                      ";
                      $res_fk = mysqli_query($conexion, $sql_fk);
                      if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $display_value = implode(" | ", $partes);
                      }else{
                        $display_value = $valor;
                      }
                    }

                    echo "<div class='card-field-value'>".htmlspecialchars($display_value,ENT_QUOTES)."</div>";
                    echo "</div>";
                  }
                  echo "</div>"; // card-fields

                  echo "<div class='card-actions'>";
                  if($primaryKey && isset($fila[$primaryKey])){
                    $id_fila = $fila[$primaryKey];
                    $id_url  = urlencode($id_fila);
                    echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                    echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                    echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                  }
                  echo "</div>";

                  echo "</article>";
                }
                echo "</div>"; // cards-container
                echo "</div>"; // vista-tarjetas
              }
            }
          } else {
            // DASHBOARD INICIAL: gráficos de campos ENUM/SET y FKs como PIE
            echo "<p class='dashboard-intro'>
              Resumen gráfico de la información categórica y relacional del sistema:
              campos <b>ENUM/SET</b> y campos de <b>clave foránea</b> en todas las tablas, representados como gráficos de tipo donut.
            </p>";

            $resultado = mysqli_query($conexion, "SHOW TABLES;");
            echo "<div class='charts-grid'>";
            while($fila = mysqli_fetch_assoc($resultado)){
              $tabla = array_values($fila)[0];
              $meta  = obtener_meta_columnas($conexion, $tabla, $db_name);
              $fksTabla = obtener_claves_foraneas($conexion, $tabla, $db_name);

              // 1) Campos ENUM/SET
              foreach($meta as $nombre_columna => $meta_columna){
                $data_type = strtolower($meta_columna['DATA_TYPE']);
                if($data_type !== 'enum' && $data_type !== 'set'){ continue; }

                $sql_dist = "
                  SELECT ".$nombre_columna." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$nombre_columna."
                  ORDER BY total DESC
                ";
                $res_dist = mysqli_query($conexion, $sql_dist);
                if(!$res_dist || mysqli_num_rows($res_dist) < 1){ continue; }

                $segmentos = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist)){
                  $v = $fila_dist['valor'];
                  $c = (int)$fila_dist['total'];
                  $segmentos[] = [
                    'label' => ($v === null || $v === '' ? '(vacío)' : $v),
                    'total' => $c
                  ];
                }
                if(empty($segmentos)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$nombre_columna."</h3>";
                echo "<div class='chart-subtitle'>Distribución de valores ENUM/SET</div>";
                render_pie_chart($segmentos, $tabla."_".$nombre_columna."_enum");
                echo "</div>";
              }

              // 2) Campos FK: distribución por valor referenciado
              foreach($fksTabla as $columna_fk => $info_fk){
                $tabla_ref = $info_fk['tabla'];
                $col_ref   = $info_fk['columna'];

                $sql_dist_fk = "
                  SELECT ".$columna_fk." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$columna_fk."
                  ORDER BY total DESC
                ";
                $res_dist_fk = mysqli_query($conexion, $sql_dist_fk);
                if(!$res_dist_fk || mysqli_num_rows($res_dist_fk) < 1){ continue; }

                $segmentos_fk = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist_fk)){
                  $valor_fk = $fila_dist['valor'];
                  $c        = (int)$fila_dist['total'];

                  if($valor_fk === null || $valor_fk === ''){
                    $label = '(sin valor)';
                  }else{
                    // Miramos fila referenciada para label
                    $sql_ref = "
                      SELECT *
                      FROM ".$tabla_ref."
                      WHERE ".$col_ref." = '".mysqli_real_escape_string($conexion,$valor_fk)."'
                      LIMIT 1
                    ";
                    $res_ref = mysqli_query($conexion, $sql_ref);
                    if($res_ref && $fila_ref = mysqli_fetch_assoc($res_ref)){
                      $partes = [];
                      foreach($fila_ref as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $label = implode(" | ", $partes);
                    }else{
                      $label = 'ID '.$valor_fk.' (huérfano)';
                    }
                  }

                  $segmentos_fk[] = [
                    'label' => $label,
                    'total' => $c
                  ];
                }
                if(empty($segmentos_fk)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$columna_fk."</h3>";
                echo "<div class='chart-subtitle'>Distribución por referencia a ".$tabla_ref."</div>";
                render_pie_chart($segmentos_fk, $tabla."_".$columna_fk."_fk");
                echo "</div>";
              }
            }
            echo "</div>";
          }
        }
      ?>
    </main>

    <script>
      document.addEventListener('DOMContentLoaded', function(){
        var btnTabla     = document.getElementById('btn-vista-tabla');
        var btnTarjetas  = document.getElementById('btn-vista-tarjetas');
        var vistaTabla   = document.getElementById('vista-tabla');
        var vistaTarjetas= document.getElementById('vista-tarjetas');

        if(btnTabla && btnTarjetas && vistaTabla && vistaTarjetas){
          btnTabla.addEventListener('click', function(){
            vistaTabla.classList.add('vista-activa');
            vistaTabla.classList.remove('vista-oculta');
            vistaTarjetas.classList.add('vista-oculta');
            vistaTarjetas.classList.remove('vista-activa');
            btnTabla.classList.add('active');
            btnTarjetas.classList.remove('active');
          });
          btnTarjetas.addEventListener('click', function(){
            vistaTabla.classList.add('vista-oculta');
            vistaTabla.classList.remove('vista-activa');
            vistaTarjetas.classList.add('vista-activa');
            vistaTarjetas.classList.remove('vista-oculta');
            btnTarjetas.classList.add('active');
            btnTabla.classList.remove('active');
          });
        }
      });
    </script>
  </body>
</html>
```

### deteccion de plantillas

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "tienda2526";
$db_user = "tienda2526";
$db_pass = "tienda2526";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: ?");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: ?");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * FKs salientes desde una tabla
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Metadatos de columnas de una tabla.
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Obtener nombre de la columna PK (primer PRIMARY KEY definido).
 */
function obtener_pk_columna($conexion, $tabla, $bd){
  $sql = "
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND COLUMN_KEY = 'PRI'
    ORDER BY ORDINAL_POSITION
    LIMIT 1
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado && $fila = mysqli_fetch_assoc($resultado)){
    return $fila['COLUMN_NAME'];
  }
  return null;
}

/**
 * Tablas que referencian a una tabla dada (FK entrantes)
 */
function obtener_tablas_que_referencian($conexion, $tabla_referenciada, $bd){
  $refs = [];
  $sql = "
    SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND REFERENCED_TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla_referenciada)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $refs[] = [
        'tabla'                => $fila['TABLE_NAME'],
        'columna'              => $fila['COLUMN_NAME'],
        'columna_referenciada' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $refs;
}

/**
 * Control de formulario adecuado para una columna NO FK.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}

/**
 * Renderizar tabla HTML de resultados (para informes).
 */
function render_tabla_html_con_links($conexion, $tabla, $rows, $bd){
  if(!$rows || count($rows) === 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }
  $foreignKeysLocal = obtener_claves_foraneas($conexion, $tabla, $bd);

  echo "<table class='report-table'>";
  $first = $rows[0];
  echo "<tr>";
  foreach($first as $k => $_){
    echo "<th>".$k."</th>";
  }
  echo "</tr>";

  foreach($rows as $fila){
    echo "<tr>";
    foreach($fila as $clave=>$valor){
      if(isset($foreignKeysLocal[$clave]) && $valor !== null && $valor !== ''){
        $fk = $foreignKeysLocal[$clave];
        $tabla_fk   = $fk['tabla'];
        $columna_fk = $fk['columna'];

        $sql_fk = "
          SELECT *
          FROM ".$tabla_fk."
          WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
          LIMIT 1
        ";
        $res_fk = mysqli_query($conexion, $sql_fk);
        if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
          $partes = [];
          foreach($fila_fk as $k2=>$v2){
            $partes[] = $v2;
          }
          $texto_celda = implode(" | ", $partes);
          echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
        }else{
          echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
        }
      }else{
        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
      }
    }
    echo "</tr>";
  }

  echo "</table>";
}

/**
 * Renderiza un gráfico de tipo donut (pie chart) como SVG.
 */
function render_pie_chart($segmentos, $chart_id){
  $total = 0;
  foreach($segmentos as $s){
    $total += $s['total'];
  }
  if($total <= 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }

  $acumulado = 0.0;

  echo "<div class='chart-pie-wrapper'>";
  echo "<div class='chart-pie'>";
  echo "<svg viewBox='0 0 42 42' class='donut'>";

  echo "<circle class='donut-ring' cx='21' cy='21' r='15.915'></circle>";

  $index = 0;
  foreach($segmentos as $s){
    $valor = $s['total'];
    $percent = ($valor / $total) * 100.0;
    $dasharray = $percent." ".(100 - $percent);
    $dashoffset = 25 - $acumulado;

    echo "<circle class='donut-segment segment-".$index."' cx='21' cy='21' r='15.915' ";
    echo "stroke-dasharray='".$dasharray."' stroke-dashoffset='".$dashoffset."'></circle>";

    $acumulado += $percent;
    $index++;
  }

  echo "</svg>";
  echo "</div>";

  echo "<ul class='chart-legend'>";
  $index = 0;
  foreach($segmentos as $s){
    $label = htmlspecialchars($s['label'],ENT_QUOTES);
    $valor = (int)$s['total'];
    echo "<li>";
    echo "<span class='legend-color segment-".$index."'></span>";
    echo "<span class='legend-label'>".$label."</span>";
    echo "<span class='legend-value'>(".$valor.")</span>";
    echo "</li>";
    $index++;
  }
  echo "</ul>";
  echo "</div>";
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap'); 
      :root{
        --margen: 20px;
        --color_primario: indigo;
        --color_secundario: aliceblue;
        --color_nav_fondo: #1f0033;
        --color_main_fondo: #edf0ff;
        --color_tabla_header: indigo;
        --color_tabla_borde: #b3b5e0;
        --color_tabla_fila_par: #f7f7ff;
        --color_tabla_fila_impar: #ffffff;
        --radio: 8px;

        --chart-color-0: #4b0082;
        --chart-color-1: #7b3fb0;
        --chart-color-2: #ff8c42;
        --chart-color-3: #16a085;
        --chart-color-4: #3498db;
        --chart-color-5: #c0392b;
        --chart-color-6: #2ecc71;
        --chart-color-7: #f1c40f;
      }
      *{
        box-sizing:border-box;
      }
      html,body{
        width:100%;
        height:100%;
        padding:0;
        margin:0;
        font-family:ubuntu,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      body{
        display:flex;
        background-color:#f3f4ff;
        color:#222;
      }

      /* NAV LATERAL */
      nav{
        flex:1;
        min-width:240px;
        max-width:320px;
        padding:var(--margen);
        display:flex;
        flex-direction:column;
        gap:var(--margen);
        background-color:var(--color_nav_fondo);
        box-shadow:4px 0 20px rgba(0,0,0,0.25);
        color:white;
        position:relative;
        z-index:2;
      }
      #corporativo{
        display:flex;
        color:white;
        gap:calc(var(--margen)/2);
        align-items:center;
        justify-content:space-between;
        padding-bottom:var(--margen);
        border-bottom:1px solid rgba(255,255,255,0.15);
      }
      #corporativo img{
        width:56px;
        filter:drop-shadow(0 0 6px rgba(255,255,255,0.3));
      }
      #corporativo p{
        font-size:26px;
        margin:0;
        font-weight:700;
        letter-spacing:1px;
        text-shadow:0 0 6px rgba(0,0,0,0.3);
      }
      .logout{
        background-color:rgba(240,248,255,0.1);
        color:aliceblue;
        padding:6px 12px;
        border-radius:999px;
        text-decoration:none;
        font-size:12px;
        font-weight:600;
        border:1px solid rgba(240,248,255,0.4);
        transition:all 0.2s ease;
        background: indigo;
      }
      .logout:hover{
        background-color:aliceblue;
        color:var(--color_primario);
      }
      .login-user-label{
        font-size:11px;
        opacity:0.85;
        margin-right:6px;
      }

      nav>button{
        background-color:rgba(240,248,255,0.08);
        color:var(--color_secundario);
        padding:10px 12px;
        border-radius:var(--radio);
        border:1px solid transparent;
        display:flex;
        justify-content: space-between;
        align-items:center;
        cursor:pointer;
        transition:all 0.2s ease;
      }
      nav>button:hover{
        background-color:rgba(240,248,255,0.18);
        border-color:rgba(240,248,255,0.4);
        transform:translateX(2px);
      }
      .activo{
        background-color: var(--color_main_fondo);
        border-color: rgba(240, 248, 255, 0.8);
        transform: translateX(4px);
        color: indigo;
        width: 120%;
      }
      nav button a{
        text-decoration:none;
        color:inherit;
        font-size:13px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
      }
      .anadir{
        width: 22px;
        height: 22px;
        background-color: aliceblue;
        border-radius: 50%;
        line-height: 22px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 6px rgba(0, 0, 0, 0.3);
        color: white;
        background: indigo;
        margin-left:6px;
      }
      .anadir-template{
        background-color:#c0392b;
      }

      /* MAIN / DASHBOARD */
      main{
        flex:6;
        padding:var(--margen);
        overflow:auto;
        background-color:var(--color_main_fondo);
        position:relative;
      }
      main::before{
        content:"";
        position:absolute;
        inset:0;
        background-color:transparent;
        pointer-events:none;
        z-index:-1;
      }
      h2{
        margin-top:0;
        margin-bottom:10px;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }

      /* HEADER PRINCIPAL EN MAIN */
      .main-header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:var(--margen);
      }
      .main-title{
        font-size:20px;
        font-weight:600;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }
      .main-actions{
        display:flex;
        align-items:center;
        gap:8px;
      }
      .view-toggle{
        border:1px solid rgba(75,0,130,0.4);
        background-color:transparent;
        color:var(--color_primario);
        padding:6px 10px;
        border-radius:999px;
        font-size:11px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
        cursor:pointer;
        transition:all 0.15s ease;
      }
      .view-toggle:hover{
        background-color:#dadfff;
      }
      .view-toggle.active{
        background-color:var(--color_primario);
        color:white;
      }

      /* TABLAS */
      main table{
        width:100%;
        border:1px solid var(--color_tabla_borde);
        border-collapse:collapse;
        border-radius:var(--radio);
        overflow:hidden;
        background-color:var(--color_tabla_fila_impar);
        box-shadow:0 4px 14px rgba(0,0,0,0.06);
      }
      main table tr:nth-child(even){
        background-color:var(--color_tabla_fila_par);
      }
      main table tr:hover{
        background-color:#e4e6ff;
      }
      main table td{
        padding:10px 12px;
        vertical-align:top;
        font-size:13px;
      }
      main table th{
        background-color:var(--color_tabla_header);
        padding:10px 12px;
        color:aliceblue;
        text-align:left;
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:0.7px;
      }

      .report-table{
        margin-bottom:var(--margen);
      }
      .no-data{
        font-size:13px;
        color:#666;
      }

      /* ACCIONES */
      .eliminar,
      .editar,
      .reportar{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:24px;
        height:24px;
        border-radius:999px;
        text-decoration:none;
        color:white;
        margin-left:4px;
        font-size:12px;
        box-shadow:0 0 6px rgba(0,0,0,0.25);
        transition:transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
      }
      .eliminar{
        background-color:#c0392b;
      }
      .editar{
        background-color:var(--color_primario);
      }
      .editar-template{
        background-color:#c0392b;
      }
      .reportar{
        background-color:#16a085;
      }
      .eliminar:hover,
      .editar:hover,
      .reportar:hover{
        transform:translateY(-1px) scale(1.03);
        box-shadow:0 0 10px rgba(0,0,0,0.35);
        opacity:0.95;
      }

      @keyframes aparece{
        0%{opacity:0;transform:translateX(-30px);}
        100%{opacity:1;transform:translateX(0px);}
      }

      /* FORMULARIOS */
      form{
        columns:2;
        gap:var(--margen);
        margin-top:10px;
      }
      form label{
        display:block;
        font-weight:600;
        margin-bottom:4px;
        font-size:12px;
        color:#444;
      }
      form input,
      form select{
        width:100%;
        padding:10px 12px;
        box-sizing:border-box;
        margin-bottom:var(--margen);
        border:1px solid rgba(75,0,130,0.3);
        border-radius:var(--radio);
        background-color:#ffffff;
        font-size:13px;
        transition:border 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease;
      }
      form input:focus,
      form select:focus{
        outline:none;
        border-color:var(--color_primario);
        box-shadow:0 0 0 2px rgba(75,0,130,0.15);
        background-color:#ffffff;
      }
      form input[type=checkbox]{
        width:auto;
        padding:0;
        margin-top:5px;
        box-shadow:none;
      }
      form input[type=submit]{
        background-color:var(--color_primario);
        color:white;
        cursor:pointer;
        border:none;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.8px;
        box-shadow:0 4px 10px rgba(75,0,130,0.4);
      }
      form input[type=submit]:hover{
        box-shadow:0 5px 14px rgba(75,0,130,0.6);
        transform:translateY(-1px);
      }

      /* LOGIN */
      .login-box{
        max-width:420px;
        margin:80px auto;
        background-color:#ffffff;
        padding:var(--margen);
        border-radius:16px;
        border:1px solid rgba(75,0,130,0.2);
        box-shadow:0 14px 40px rgba(0,0,0,0.18);
        column-count:1;
        position:relative;
        overflow:hidden;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
      }
      .login-box form{
        columns:1;
      }
      .login-error{
        background-color:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
      }

      /* DASHBOARD / PIE CHARTS */
      .dashboard-intro{
        margin-bottom:var(--margen);
        font-size:14px;
        color:#555;
        max-width:700px;
      }
      .charts-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(360px,1fr));
        gap:var(--margen);
      }
      .chart{
        background-color:#ffffff;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        position:relative;
        overflow:hidden;
      }
      .chart h3{
        margin-top:0;
        margin-bottom:8px;
        font-size:15px;
        color:var(--color_primario);
      }
      .chart-subtitle{
        font-size:11px;
        color:#777;
        margin-bottom:8px;
      }

      .chart-pie-wrapper{
        display:flex;
        align-items:center;
        gap:12px;
      }
      .chart-pie{
        width:120px;
        height:120px;
        flex:0 0 auto;
      }
      .chart-pie svg{
        width:100%;
        height:100%;
        transform:rotate(-90deg);
      }
      .donut-ring{
        fill:none;
        stroke:#e0e2ff;
        stroke-width:10;
      }
      .donut-segment{
        fill:none;
        stroke-width:10;
      }
      .segment-0{ stroke:var(--chart-color-0); }
      .segment-1{ stroke:var(--chart-color-1); }
      .segment-2{ stroke:var(--chart-color-2); }
      .segment-3{ stroke:var(--chart-color-3); }
      .segment-4{ stroke:var(--chart-color-4); }
      .segment-5{ stroke:var(--chart-color-5); }
      .segment-6{ stroke:var(--chart-color-6); }
      .segment-7{ stroke:var(--chart-color-7); }

      .chart-legend{
        list-style:none;
        padding:0;
        margin:0;
        font-size:11px;
        color:#555;
        flex:1 1 auto;
      }
      .chart-legend li{
        display:flex;
        align-items:center;
        margin-bottom:4px;
      }
      .legend-color{
        width:10px;
        height:10px;
        border-radius:50%;
        margin-right:6px;
        flex:0 0 auto;
      }
      .legend-color.segment-0{ background-color:var(--chart-color-0); }
      .legend-color.segment-1{ background-color:var(--chart-color-1); }
      .legend-color.segment-2{ background-color:var(--chart-color-2); }
      .legend-color.segment-3{ background-color:var(--chart-color-3); }
      .legend-color.segment-4{ background-color:var(--chart-color-4); }
      .legend-color.segment-5{ background-color:var(--chart-color-5); }
      .legend-color.segment-6{ background-color:var(--chart-color-6); }
      .legend-color.segment-7{ background-color:var(--chart-color-7); }
      .legend-label{
        flex:1 1 auto;
        overflow:hidden;
        text-overflow:ellipsis;
        white-space:nowrap;
      }
      .legend-value{
        margin-left:4px;
        color:#333;
      }

      .back-link{
        margin-bottom:var(--margen);
        display:inline-block;
        text-decoration:none;
        color:var(--color_primario);
        font-size:13px;
        padding:4px 8px;
        border-radius:999px;
        background-color:#dadfff;
      }
      .back-link::before{
        content:"← ";
      }
      .subsection{
        margin-top:var(--margen);
      }
      .subsection h3{
        margin-bottom:6px;
        color:#333;
      }
      .subsection h4{
        margin:8px 0 4px;
        font-size:13px;
        color:#555;
      }

      /* VISTAS TABLA / TARJETAS */
      .vista-activa{display:block;}
      .vista-oculta{display:none;}

      .cards-container{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
        gap:var(--margen);
      }
      .card-registro{
        background-color:#ffffff;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        display:flex;
        flex-direction:column;
        justify-content:space-between;
      }
      .card-fields{
        margin-bottom:10px;
      }
      .card-field{
        margin-bottom:6px;
        font-size:12px;
      }
      .card-field-label{
        font-weight:600;
        color:#555;
        margin-bottom:2px;
      }
      .card-field-value{
        color:#222;
        word-break:break-word;
      }
      .card-actions{
        align-self:flex-end;
        margin-top:8px;
      }
      .card-actions .eliminar,
      .card-actions .editar,
      .card-actions .reportar{
        margin-left:0;
        margin-right:4px;
      }

      @media (max-width:900px){
        body{flex-direction:column;}
        nav{
          flex:none;
          max-width:none;
          box-shadow:0 4px 12px rgba(0,0,0,0.2);
        }
        .chart-pie-wrapper{
          flex-direction:column;
          align-items:flex-start;
        }
      }
      #corporativo a{color:inherit;text-decoration:none;}
    </style>
  </head>
  <body>
  
    <nav>
      <div id="corporativo">
        <a href="?">
          <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
            <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
            <p>jocarsa</p>
          </div>
        </a>
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual_nav = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual_nav) ? "activo" : "";
            $template_file_nav = __DIR__ . "/templates/".$nombre_tabla.".php";
            $tiene_template_nav = file_exists($template_file_nav);

            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual_nav){
                if($tiene_template_nav){
                  echo "<a href='?operacion=añadir&tabla=".$tabla_actual_nav."' class='anadir anadir-normal'>+</a>";
                  echo "<a href='?operacion=añadir&tabla=".$tabla_actual_nav."&template=1' class='anadir anadir-template'>+</a>";
                }else{
                  echo "<a href='?operacion=añadir&tabla=".$tabla_actual_nav."' class='anadir anadir-normal'>+</a>";
                }
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {

          // HEADER PRINCIPAL DINÁMICO
          $tabla_header     = $_GET['tabla']     ?? null;
          $operacion_header = $_GET['operacion'] ?? '';
          $page_title = "Dashboard de microERP";

          if($tabla_header){
            switch($operacion_header){
              case 'añadir':
                $page_title = "Añadir registro en ".$tabla_header;
                break;
              case 'editar':
                $page_title = "Editar registro en ".$tabla_header;
                break;
              case 'report':
                $page_title = "Informe de ".$tabla_header;
                break;
              default:
                $page_title = "Listado de ".$tabla_header;
            }
          }

          echo "<header class='main-header'>";
          echo "<div class='main-title'>".$page_title."</div>";
          echo "<div class='main-actions'>";

          if($tabla_header && $operacion_header === ''){
            echo "<button type='button' id='btn-vista-tabla' class='view-toggle active'>Tabla</button>";
            echo "<button type='button' id='btn-vista-tarjetas' class='view-toggle'>Tarjetas</button>";
          }

          echo "<span class='login-user-label'>".htmlspecialchars($_SESSION['usuario'])."</span>";
          echo "<a href='?logout=1' class='logout'>Salir</a>";
          echo "</div>";
          echo "</header>";

          // Lógica del microERP
          if(isset($_GET['tabla'])){
            $tabla      = $_GET['tabla'];
            $operacion  = $_GET['operacion'] ?? '';
            $id         = isset($_GET['id']) ? $_GET['id'] : null;

            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);
            $primaryKey   = obtener_pk_columna($conexion, $tabla, $db_name);

            // Gestión de plantillas
            $templates_dir        = __DIR__ . "/templates";
            $template_file        = $templates_dir . "/".$tabla.".php";
            $hay_template_tabla   = file_exists($template_file);
            $usar_template        = (isset($_GET['template']) && $_GET['template'] === '1' && $hay_template_tabla);

            // Eliminación
            if($operacion === "eliminar" && $id !== null && $primaryKey){
              $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql.";"
              );
              $operacion = '';
            }

            // AÑADIR
            if($operacion === "añadir"){
              // Procesar inserción
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

              $form_action   = "?operacion=añadir&tabla=".$tabla;
              if($usar_template){ $form_action .= "&template=1"; }

              if($usar_template){
                $template_mode = 'insert';
                $fila_actual   = null;
                include $template_file;
              }else{
                echo "<form action='".$form_action."' method='POST'>";

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                  if(isset($foreignKeys[$nombre_columna])){
                    $fk = $foreignKeys[$nombre_columna];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    echo "<label>".$nombre_columna."</label>";
                    echo "<select name='".$nombre_columna."'>";
                    echo "<option value=''>-- seleccionar --</option>";

                    $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                    if($res_fk){
                      while($fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $texto_opcion = implode(" | ", $partes);
                        $value_opcion = $fila_fk[$columna_fk];
                        echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                      }
                    }

                    echo "</select>";
                  }else{
                    echo render_input_para_columna($nombre_columna, $meta_columna);
                  }
                }
                echo "<input type='submit' value='Guardar'>";
                echo "</form>";
              }

            // EDITAR
            } elseif($operacion === "editar" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede editar un registro concreto.</p>";
              } else {
                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<p>No se ha encontrado el registro a editar.</p>";
                } else {
                  // Procesar actualización
                  if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                    $sets = [];

                    foreach($columnMeta as $nombre_columna => $meta_columna){
                      if($nombre_columna === $primaryKey){ continue; }

                      $data_type   = strtolower($meta_columna['DATA_TYPE']);
                      $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                      if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                        $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                        $sets[] = "`".$nombre_columna."`=".intval($valor);
                        continue;
                      }

                      if(isset($_POST[$nombre_columna])){
                        $valor = $_POST[$nombre_columna];
                        $sets[] = "`".$nombre_columna."` = '".mysqli_real_escape_string($conexion,$valor)."'";
                      }
                    }

                    if(count($sets) > 0){
                      $sql_update = "UPDATE ".$tabla." SET ".implode(", ",$sets)." WHERE `".$primaryKey."` = ".$id_sql;
                      mysqli_query($conexion, $sql_update);
                    }

                    $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                    $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : $fila_actual;
                  }

                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

                  $form_action = "?operacion=editar&tabla=".$tabla."&id=".urlencode($id);
                  if($usar_template){ $form_action .= "&template=1"; }

                  if($usar_template){
                    $template_mode = 'update';
                    include $template_file;
                  }else{
                    echo "<form action='".$form_action."' method='POST'>";

                    if($primaryKey && isset($fila_actual[$primaryKey])){
                      echo "<label>".$primaryKey."</label>";
                      echo "<input type='text' value='".htmlspecialchars($fila_actual[$primaryKey],ENT_QUOTES)."' disabled>";
                    }

                    foreach($columnMeta as $nombre_columna => $meta_columna){
                      if($nombre_columna === $primaryKey){ continue; }
                      $valor_actual = $fila_actual[$nombre_columna] ?? "";

                      if(isset($foreignKeys[$nombre_columna])){
                        $fk = $foreignKeys[$nombre_columna];
                        $tabla_fk   = $fk['tabla'];
                        $columna_fk = $fk['columna'];

                        echo "<label>".$nombre_columna."</label>";
                        echo "<select name='".$nombre_columna."'>";
                        echo "<option value=''>-- seleccionar --</option>";

                        $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                        if($res_fk){
                          while($fila_fk = mysqli_fetch_assoc($res_fk)){
                            $partes = [];
                            foreach($fila_fk as $k2=>$v2){
                              $partes[] = $v2;
                            }
                            $texto_opcion = implode(" | ", $partes);
                            $value_opcion = $fila_fk[$columna_fk];
                            $selected = ($valor_actual == $value_opcion) ? "selected" : "";
                            echo "<option value='".$value_opcion."' ".$selected.">".$texto_opcion."</option>";
                          }
                        }

                        echo "</select>";
                      }else{
                        echo render_input_para_columna($nombre_columna, $meta_columna, $valor_actual);
                      }
                    }

                    echo "<input type='submit' value='Guardar cambios'>";
                    echo "</form>";
                  }
                }
              }

            // INFORME
            } elseif($operacion === "report" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede generar un informe por registro.</p>";
              } else {
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<p>No se ha encontrado el registro solicitado.</p>";
                } else {
                  echo "<div class='subsection'>";
                  echo "<h3>Registro principal</h3>";
                  render_tabla_html_con_links($conexion, $tabla, [$fila_actual], $db_name);
                  echo "</div>";

                  echo "<div class='subsection'>";
                  echo "<h3>Datos referenciados por este registro</h3>";

                  $hay_referenciados = false;
                  foreach($foreignKeys as $columna_fk_local => $info_fk){
                    $valor_fk = $fila_actual[$columna_fk_local] ?? null;
                    if($valor_fk === null || $valor_fk === ''){ continue; }

                    $tabla_fk   = $info_fk['tabla'];
                    $col_fk     = $info_fk['columna'];

                    $sql_fk = "SELECT * FROM ".$tabla_fk." WHERE ".$col_fk." = '".mysqli_real_escape_string($conexion,$valor_fk)."'";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && mysqli_num_rows($res_fk) > 0){
                      $hay_referenciados = true;
                      $rows_fk = [];
                      while($row_fk = mysqli_fetch_assoc($res_fk)){
                        $rows_fk[] = $row_fk;
                      }

                      echo "<h4>".$tabla_fk." (por ".$columna_fk_local.")</h4>";
                      render_tabla_html_con_links($conexion, $tabla_fk, $rows_fk, $db_name);
                    }
                  }
                  if(!$hay_referenciados){
                    echo "<p class='no-data'>No hay referencias salientes.</p>";
                  }
                  echo "</div>";

                  echo "<div class='subsection'>";
                  echo "<h3>Datos relacionados que apuntan a este registro</h3>";

                  $refs_entrantes = obtener_tablas_que_referencian($conexion, $tabla, $db_name);
                  if(count($refs_entrantes) === 0){
                    echo "<p class='no-data'>No hay tablas que referencien a esta entidad.</p>";
                  } else {
                    $hay_entrantes = false;
                    foreach($refs_entrantes as $ref){
                      $tabla_hija        = $ref['tabla'];
                      $columna_hija      = $ref['columna'];
                      $col_ref_padre     = $ref['columna_referenciada'];

                      $valor_ref_padre = $fila_actual[$col_ref_padre] ?? null;
                      if($valor_ref_padre === null){ continue; }

                      $sql_hija = "SELECT * FROM ".$tabla_hija." WHERE ".$columna_hija." = '".mysqli_real_escape_string($conexion,$valor_ref_padre)."'";
                      $res_hija = mysqli_query($conexion, $sql_hija);
                      if($res_hija && mysqli_num_rows($res_hija) > 0){
                        $hay_entrantes = true;
                        $rows_hija = [];
                        while($fila_hija = mysqli_fetch_assoc($res_hija)){
                          $rows_hija[] = $fila_hija;
                        }

                        echo "<h4>".$tabla_hija." (columna ".$columna_hija.")</h4>";
                        render_tabla_html_con_links($conexion, $tabla_hija, $rows_hija, $db_name);
                      }
                    }
                    if(!$hay_entrantes){
                      echo "<p class='no-data'>No hay registros entrantes que apunten a este registro.</p>";
                    }
                  }

                  echo "</div>";
                }
              }

            // LISTADO
            } else {

              if(!$primaryKey){
                echo "<p class='no-data'>Aviso: la tabla <b>".$tabla."</b> no tiene clave primaria definida. No se podrán editar ni eliminar registros individualmente.</p>";
              }

              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $rows = [];
              if($resultado){
                while($fila = mysqli_fetch_assoc($resultado)){
                  $rows[] = $fila;
                }
              }

              if(count($rows) === 0){
                echo "<p class='no-data'>No hay registros en esta tabla.</p>";
              } else {

                // VISTA TABLA
                echo "<div id='vista-tabla' class='vista-activa'>";
                echo "<table>";
                $contador = 0;
                foreach($rows as $fila){
                  if($contador == 0){
                    echo "<tr>";
                      foreach($fila as $clave=>$valor){
                        echo "<th>".$clave."</th>";
                      }
                      echo "<th>Acciones</th>";
                    echo "</tr>";
                  }

                  echo "<tr>";
                  foreach($fila as $clave=>$valor){
                    if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                      $fk = $foreignKeys[$clave];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      $sql_fk = "
                        SELECT *
                        FROM ".$tabla_fk."
                        WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                        LIMIT 1
                      ";
                      $res_fk = mysqli_query($conexion, $sql_fk);
                      if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $texto_celda = implode(" | ", $partes);
                        echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
                      }else{
                        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                      }
                    }else{
                      echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                    }
                  }

                  echo "<td>";
                  if($primaryKey && isset($fila[$primaryKey])){
                    $id_fila = $fila[$primaryKey];
                    $id_url  = urlencode($id_fila);
                    echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                    if($hay_template_tabla){
                      echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."&template=1' class='editar editar-template'>✏</a>";
                    }
                    echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                    echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                  } else {
                    echo "<span style='font-size:11px;color:#777;'>—</span>";
                  }
                  echo "</td>";

                  echo "</tr>";
                  $contador++;
                }
                echo "</table>";
                echo "</div>";

                // VISTA TARJETAS
                echo "<div id='vista-tarjetas' class='vista-oculta'>";
                echo "<div class='cards-container'>";
                foreach($rows as $fila){
                  echo "<article class='card-registro'>";
                  echo "<div class='card-fields'>";
                  foreach($fila as $clave=>$valor){
                    echo "<div class='card-field'>";
                    echo "<div class='card-field-label'>".$clave."</div>";

                    $display_value = $valor;

                    if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                      $fk = $foreignKeys[$clave];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      $sql_fk = "
                        SELECT *
                        FROM ".$tabla_fk."
                        WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                        LIMIT 1
                      ";
                      $res_fk = mysqli_query($conexion, $sql_fk);
                      if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $display_value = implode(" | ", $partes);
                      }else{
                        $display_value = $valor;
                      }
                    }

                    echo "<div class='card-field-value'>".htmlspecialchars($display_value,ENT_QUOTES)."</div>";
                    echo "</div>";
                  }
                  echo "</div>";

                  echo "<div class='card-actions'>";
                  if($primaryKey && isset($fila[$primaryKey])){
                    $id_fila = $fila[$primaryKey];
                    $id_url  = urlencode($id_fila);
                    echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                    if($hay_template_tabla){
                      echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."&template=1' class='editar editar-template'>✏</a>";
                    }
                    echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                    echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                  }
                  echo "</div>";

                  echo "</article>";
                }
                echo "</div>";
                echo "</div>";
              }
            }
          } else {
            // DASHBOARD INICIAL
            echo "<p class='dashboard-intro'>
              Resumen gráfico de la información categórica y relacional del sistema:
              campos <b>ENUM/SET</b> y campos de <b>clave foránea</b> en todas las tablas, representados como gráficos de tipo donut.
            </p>";

            $resultado = mysqli_query($conexion, "SHOW TABLES;");
            echo "<div class='charts-grid'>";
            while($fila = mysqli_fetch_assoc($resultado)){
              $tabla = array_values($fila)[0];
              $meta  = obtener_meta_columnas($conexion, $tabla, $db_name);
              $fksTabla = obtener_claves_foraneas($conexion, $tabla, $db_name);

              // ENUM/SET
              foreach($meta as $nombre_columna => $meta_columna){
                $data_type = strtolower($meta_columna['DATA_TYPE']);
                if($data_type !== 'enum' && $data_type !== 'set'){ continue; }

                $sql_dist = "
                  SELECT ".$nombre_columna." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$nombre_columna."
                  ORDER BY total DESC
                ";
                $res_dist = mysqli_query($conexion, $sql_dist);
                if(!$res_dist || mysqli_num_rows($res_dist) < 1){ continue; }

                $segmentos = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist)){
                  $v = $fila_dist['valor'];
                  $c = (int)$fila_dist['total'];
                  $segmentos[] = [
                    'label' => ($v === null || $v === '' ? '(vacío)' : $v),
                    'total' => $c
                  ];
                }
                if(empty($segmentos)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$nombre_columna."</h3>";
                echo "<div class='chart-subtitle'>Distribución de valores ENUM/SET</div>";
                render_pie_chart($segmentos, $tabla."_".$nombre_columna."_enum");
                echo "</div>";
              }

              // FKs
              foreach($fksTabla as $columna_fk => $info_fk){
                $tabla_ref = $info_fk['tabla'];
                $col_ref   = $info_fk['columna'];

                $sql_dist_fk = "
                  SELECT ".$columna_fk." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$columna_fk."
                  ORDER BY total DESC
                ";
                $res_dist_fk = mysqli_query($conexion, $sql_dist_fk);
                if(!$res_dist_fk || mysqli_num_rows($res_dist_fk) < 1){ continue; }

                $segmentos_fk = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist_fk)){
                  $valor_fk = $fila_dist['valor'];
                  $c        = (int)$fila_dist['total'];

                  if($valor_fk === null || $valor_fk === ''){
                    $label = '(sin valor)';
                  }else{
                    $sql_ref = "
                      SELECT *
                      FROM ".$tabla_ref."
                      WHERE ".$col_ref." = '".mysqli_real_escape_string($conexion,$valor_fk)."'
                      LIMIT 1
                    ";
                    $res_ref = mysqli_query($conexion, $sql_ref);
                    if($res_ref && $fila_ref = mysqli_fetch_assoc($res_ref)){
                      $partes = [];
                      foreach($fila_ref as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $label = implode(" | ", $partes);
                    }else{
                      $label = 'ID '.$valor_fk.' (huérfano)';
                    }
                  }

                  $segmentos_fk[] = [
                    'label' => $label,
                    'total' => $c
                  ];
                }
                if(empty($segmentos_fk)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$columna_fk."</h3>";
                echo "<div class='chart-subtitle'>Distribución por referencia a ".$tabla_ref."</div>";
                render_pie_chart($segmentos_fk, $tabla."_".$columna_fk."_fk");
                echo "</div>";
              }
            }
            echo "</div>";
          }
        }
      ?>
    </main>

    <script>
      document.addEventListener('DOMContentLoaded', function(){
        var btnTabla     = document.getElementById('btn-vista-tabla');
        var btnTarjetas  = document.getElementById('btn-vista-tarjetas');
        var vistaTabla   = document.getElementById('vista-tabla');
        var vistaTarjetas= document.getElementById('vista-tarjetas');

        if(btnTabla && btnTarjetas && vistaTabla && vistaTarjetas){
          btnTabla.addEventListener('click', function(){
            vistaTabla.classList.add('vista-activa');
            vistaTabla.classList.remove('vista-oculta');
            vistaTarjetas.classList.add('vista-oculta');
            vistaTarjetas.classList.remove('vista-activa');
            btnTabla.classList.add('active');
            btnTarjetas.classList.remove('active');
          });
          btnTarjetas.addEventListener('click', function(){
            vistaTabla.classList.add('vista-oculta');
            vistaTabla.classList.remove('vista-activa');
            vistaTarjetas.classList.add('vista-activa');
            vistaTarjetas.classList.remove('vista-oculta');
            btnTarjetas.classList.add('active');
            btnTabla.classList.remove('active');
          });
        }
      });
    </script>
  </body>
</html>
```

### junto los botones

```
<?php
session_start();

// Parámetros de conexión
$db_host = "localhost";
$db_name = "tienda2526";
$db_user = "tienda2526";
$db_pass = "tienda2526";

// Credenciales iniciales
$usuario_valido     = "jocarsa";
$contrasena_valida  = "jocarsa";

$login_error = "";

// Logout
if (isset($_GET['logout'])) {
  session_unset();
  session_destroy();
  header("Location: ?");
  exit;
}

// Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['accion']) && $_POST['accion'] === 'login') {
  $user = $_POST['usuario']     ?? '';
  $pass = $_POST['contrasena']  ?? '';

  if ($user === $usuario_valido && $pass === $contrasena_valida) {
    $_SESSION['usuario'] = $user;
    header("Location: ?");
    exit;
  } else {
    $login_error = "Usuario o contraseña incorrectos";
  }
}

$logged_in = isset($_SESSION['usuario']);

// Solo conectamos a la base de datos si hay sesión iniciada
if ($logged_in) {
  $conexion = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
  if(!$conexion){
    die("Error de conexión: ".mysqli_connect_error());
  }
}

/**
 * FKs salientes desde una tabla
 */
function obtener_claves_foraneas($conexion, $tabla, $bd){
  $fk = [];
  $sql = "
    SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND REFERENCED_TABLE_NAME IS NOT NULL
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $fk[$fila['COLUMN_NAME']] = [
        'tabla'   => $fila['REFERENCED_TABLE_NAME'],
        'columna' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $fk;
}

/**
 * Metadatos de columnas de una tabla.
 */
function obtener_meta_columnas($conexion, $tabla, $bd){
  $meta = [];
  $sql = "
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT,
           COLUMN_KEY, EXTRA, CHARACTER_MAXIMUM_LENGTH, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $meta[$fila['COLUMN_NAME']] = $fila;
    }
  }
  return $meta;
}

/**
 * Obtener nombre de la columna PK (primer PRIMARY KEY definido).
 */
function obtener_pk_columna($conexion, $tabla, $bd){
  $sql = "
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla)."'
      AND COLUMN_KEY = 'PRI'
    ORDER BY ORDINAL_POSITION
    LIMIT 1
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado && $fila = mysqli_fetch_assoc($resultado)){
    return $fila['COLUMN_NAME'];
  }
  return null;
}

/**
 * Tablas que referencian a una tabla dada (FK entrantes)
 */
function obtener_tablas_que_referencian($conexion, $tabla_referenciada, $bd){
  $refs = [];
  $sql = "
    SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '".mysqli_real_escape_string($conexion,$bd)."'
      AND REFERENCED_TABLE_NAME = '".mysqli_real_escape_string($conexion,$tabla_referenciada)."'
  ";
  $resultado = mysqli_query($conexion, $sql);
  if($resultado){
    while($fila = mysqli_fetch_assoc($resultado)){
      $refs[] = [
        'tabla'                => $fila['TABLE_NAME'],
        'columna'              => $fila['COLUMN_NAME'],
        'columna_referenciada' => $fila['REFERENCED_COLUMN_NAME']
      ];
    }
  }
  return $refs;
}

/**
 * Control de formulario adecuado para una columna NO FK.
 */
function render_input_para_columna($nombre_columna, $meta_columna, $valor_actual = ""){
  $data_type   = strtolower($meta_columna['DATA_TYPE']);
  $column_type = strtolower($meta_columna['COLUMN_TYPE']);
  $html = "";

  // Etiqueta
  $html .= "<label>".$nombre_columna."</label>";

  // tinyint(1) -> checkbox
  if($data_type === 'tinyint' && strpos($column_type, '(1)') !== false){
    $checked = ($valor_actual == 1 || $valor_actual === "1") ? "checked" : "";
    $html .= "<input type='checkbox' name='".$nombre_columna."' value='1' ".$checked.">";
    return $html;
  }

  switch($data_type){
    // Textos
    case 'varchar':
    case 'char':
    case 'tinytext':
    case 'text':
    case 'mediumtext':
    case 'longtext':
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // Números enteros
    case 'int':
    case 'integer':
    case 'tinyint':
    case 'smallint':
    case 'mediumint':
    case 'bigint':
    case 'year':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='1'>";
      break;

    // Números decimales
    case 'decimal':
    case 'numeric':
    case 'float':
    case 'double':
    case 'real':
      $html .= "<input type='number' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."' step='any'>";
      break;

    // Fechas
    case 'date':
      $html .= "<input type='date' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    case 'datetime':
    case 'timestamp':
      $valor = str_replace(" ", "T", $valor_actual);
      $html .= "<input type='datetime-local' name='".$nombre_columna."' value='".htmlspecialchars($valor,ENT_QUOTES)."'>";
      break;

    case 'time':
      $html .= "<input type='time' name='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;

    // ENUM y SET -> select
    case 'enum':
    case 'set':
      $html .= "<select name='".$nombre_columna."'>";
      $html .= "<option value=''>-- seleccionar --</option>";
      if(preg_match_all("/'([^']*)'/", $meta_columna['COLUMN_TYPE'], $matches)){
        foreach($matches[1] as $opcion){
          $selected = ($valor_actual == $opcion) ? "selected" : "";
          $html .= "<option value='".htmlspecialchars($opcion,ENT_QUOTES)."' ".$selected.">".$opcion."</option>";
        }
      }
      $html .= "</select>";
      break;

    // Otros tipos -> text genérico
    default:
      $html .= "<input type='text' name='".$nombre_columna."' placeholder='".$nombre_columna."' value='".htmlspecialchars($valor_actual,ENT_QUOTES)."'>";
      break;
  }

  return $html;
}

/**
 * Renderizar tabla HTML de resultados (para informes).
 */
function render_tabla_html_con_links($conexion, $tabla, $rows, $bd){
  if(!$rows || count($rows) === 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }
  $foreignKeysLocal = obtener_claves_foraneas($conexion, $tabla, $bd);

  echo "<table class='report-table'>";
  $first = $rows[0];
  echo "<tr>";
  foreach($first as $k => $_){
    echo "<th>".$k."</th>";
  }
  echo "</tr>";

  foreach($rows as $fila){
    echo "<tr>";
    foreach($fila as $clave=>$valor){
      if(isset($foreignKeysLocal[$clave]) && $valor !== null && $valor !== ''){
        $fk = $foreignKeysLocal[$clave];
        $tabla_fk   = $fk['tabla'];
        $columna_fk = $fk['columna'];

        $sql_fk = "
          SELECT *
          FROM ".$tabla_fk."
          WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
          LIMIT 1
        ";
        $res_fk = mysqli_query($conexion, $sql_fk);
        if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
          $partes = [];
          foreach($fila_fk as $k2=>$v2){
            $partes[] = $v2;
          }
          $texto_celda = implode(" | ", $partes);
          echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
        }else{
          echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
        }
      }else{
        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
      }
    }
    echo "</tr>";
  }

  echo "</table>";
}

/**
 * Renderiza un gráfico de tipo donut (pie chart) como SVG.
 */
function render_pie_chart($segmentos, $chart_id){
  $total = 0;
  foreach($segmentos as $s){
    $total += $s['total'];
  }
  if($total <= 0){
    echo "<p class='no-data'>Sin datos.</p>";
    return;
  }

  $acumulado = 0.0;

  echo "<div class='chart-pie-wrapper'>";
  echo "<div class='chart-pie'>";
  echo "<svg viewBox='0 0 42 42' class='donut'>";

  echo "<circle class='donut-ring' cx='21' cy='21' r='15.915'></circle>";

  $index = 0;
  foreach($segmentos as $s){
    $valor = $s['total'];
    $percent = ($valor / $total) * 100.0;
    $dasharray = $percent." ".(100 - $percent);
    $dashoffset = 25 - $acumulado;

    echo "<circle class='donut-segment segment-".$index."' cx='21' cy='21' r='15.915' ";
    echo "stroke-dasharray='".$dasharray."' stroke-dashoffset='".$dashoffset."'></circle>";

    $acumulado += $percent;
    $index++;
  }

  echo "</svg>";
  echo "</div>";

  echo "<ul class='chart-legend'>";
  $index = 0;
  foreach($segmentos as $s){
    $label = htmlspecialchars($s['label'],ENT_QUOTES);
    $valor = (int)$s['total'];
    echo "<li>";
    echo "<span class='legend-color segment-".$index."'></span>";
    echo "<span class='legend-label'>".$label."</span>";
    echo "<span class='legend-value'>(".$valor.")</span>";
    echo "</li>";
    $index++;
  }
  echo "</ul>";
  echo "</div>";
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>microERP</title>
    <meta charset="utf-8">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap'); 
      :root{
        --margen: 20px;
        --color_primario: indigo;
        --color_secundario: aliceblue;
        --color_nav_fondo: #1f0033;
        --color_main_fondo: #edf0ff;
        --color_tabla_header: indigo;
        --color_tabla_borde: #b3b5e0;
        --color_tabla_fila_par: #f7f7ff;
        --color_tabla_fila_impar: #ffffff;
        --radio: 8px;

        --chart-color-0: #4b0082;
        --chart-color-1: #7b3fb0;
        --chart-color-2: #ff8c42;
        --chart-color-3: #16a085;
        --chart-color-4: #3498db;
        --chart-color-5: #c0392b;
        --chart-color-6: #2ecc71;
        --chart-color-7: #f1c40f;
      }
      *{
        box-sizing:border-box;
      }
      html,body{
        width:100%;
        height:100%;
        padding:0;
        margin:0;
        font-family:ubuntu,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      }
      body{
        display:flex;
        background-color:#f3f4ff;
        color:#222;
      }

      /* NAV LATERAL */
      nav{
        flex:1;
        min-width:240px;
        max-width:320px;
        padding:var(--margen);
        display:flex;
        flex-direction:column;
        gap:var(--margen);
        background-color:var(--color_nav_fondo);
        box-shadow:4px 0 20px rgba(0,0,0,0.25);
        color:white;
        position:relative;
        z-index:2;
      }
      #corporativo{
        display:flex;
        color:white;
        gap:calc(var(--margen)/2);
        align-items:center;
        justify-content:space-between;
        padding-bottom:var(--margen);
        border-bottom:1px solid rgba(255,255,255,0.15);
      }
      #corporativo img{
        width:56px;
        filter:drop-shadow(0 0 6px rgba(255,255,255,0.3));
      }
      #corporativo p{
        font-size:26px;
        margin:0;
        font-weight:700;
        letter-spacing:1px;
        text-shadow:0 0 6px rgba(0,0,0,0.3);
      }
      .logout{
        background-color:rgba(240,248,255,0.1);
        color:aliceblue;
        padding:6px 12px;
        border-radius:999px;
        text-decoration:none;
        font-size:12px;
        font-weight:600;
        border:1px solid rgba(240,248,255,0.4);
        transition:all 0.2s ease;
        background: indigo;
      }
      .logout:hover{
        background-color:aliceblue;
        color:var(--color_primario);
      }
      .login-user-label{
        font-size:11px;
        opacity:0.85;
        margin-right:6px;
      }

      nav>button{
        background-color:rgba(240,248,255,0.08);
        color:var(--color_secundario);
        padding:10px 12px;
        border-radius:var(--radio);
        border:1px solid transparent;
        display:flex;
        justify-content: space-between;
        align-items:center;
        cursor:pointer;
        transition:all 0.2s ease;
      }
      nav>button:hover{
        background-color:rgba(240,248,255,0.18);
        border-color:rgba(240,248,255,0.4);
        transform:translateX(2px);
      }
      .activo{
        background-color: var(--color_main_fondo);
        border-color: rgba(240, 248, 255, 0.8);
        transform: translateX(4px);
        color: indigo;
        width: 120%;
      }
      .activo:hover{
        background:white;
      }
      nav button a{
        text-decoration:none;
        color:inherit;
        font-size:13px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
      }
      .anadir{
        width: 22px;
        height: 22px;
        background-color: aliceblue;
        border-radius: 50%;
        line-height: 22px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 6px rgba(0, 0, 0, 0.3);
        color: white;
        background: indigo;
        margin-left:6px;
      }
      .anadir-template{
        background-color:#c0392b;
      }

      /* MAIN / DASHBOARD */
      main{
        flex:6;
        padding:var(--margen);
        overflow:auto;
        background-color:var(--color_main_fondo);
        position:relative;
      }
      main::before{
        content:"";
        position:absolute;
        inset:0;
        background-color:transparent;
        pointer-events:none;
        z-index:-1;
      }
      h2{
        margin-top:0;
        margin-bottom:10px;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }

      /* HEADER PRINCIPAL EN MAIN */
      .main-header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:var(--margen);
      }
      .main-title{
        font-size:20px;
        font-weight:600;
        color:var(--color_primario);
        text-shadow:0 0 4px rgba(255,255,255,0.8);
      }
      .main-actions{
        display:flex;
        align-items:center;
        gap:8px;
      }
      .view-toggle{
        border:1px solid rgba(75,0,130,0.4);
        background-color:transparent;
        color:var(--color_primario);
        padding:6px 10px;
        border-radius:999px;
        font-size:11px;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.5px;
        cursor:pointer;
        transition:all 0.15s ease;
      }
      .view-toggle:hover{
        background-color:#dadfff;
      }
      .view-toggle.active{
        background-color:var(--color_primario);
        color:white;
      }

      /* TABLAS */
      main table{
        width:100%;
        border:1px solid var(--color_tabla_borde);
        border-collapse:collapse;
        border-radius:var(--radio);
        overflow:hidden;
        background-color:var(--color_tabla_fila_impar);
        box-shadow:0 4px 14px rgba(0,0,0,0.06);
      }
      main table tr:nth-child(even){
        background-color:var(--color_tabla_fila_par);
      }
      main table tr:hover{
        background-color:#e4e6ff;
      }
      main table td{
        padding:10px 12px;
        vertical-align:top;
        font-size:13px;
      }
      main table th{
        background-color:var(--color_tabla_header);
        padding:10px 12px;
        color:aliceblue;
        text-align:left;
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:0.7px;
      }

      .report-table{
        margin-bottom:var(--margen);
      }
      .no-data{
        font-size:13px;
        color:#666;
      }

      /* ACCIONES */
      .eliminar,
      .editar,
      .reportar{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:24px;
        height:24px;
        border-radius:999px;
        text-decoration:none;
        color:white;
        margin-left:4px;
        font-size:12px;
        box-shadow:0 0 6px rgba(0,0,0,0.25);
        transition:transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
      }
      .eliminar{
        background-color:#c0392b;
      }
      .editar{
        background-color:var(--color_primario);
      }
      .editar-template{
        background-color:#c0392b;
      }
      .reportar{
        background-color:#16a085;
      }
      .eliminar:hover,
      .editar:hover,
      .reportar:hover{
        transform:translateY(-1px) scale(1.03);
        box-shadow:0 0 10px rgba(0,0,0,0.35);
        opacity:0.95;
      }

      @keyframes aparece{
        0%{opacity:0;transform:translateX(-30px);}
        100%{opacity:1;transform:translateX(0px);}
      }

      /* FORMULARIOS */
      form{
        columns:2;
        gap:var(--margen);
        margin-top:10px;
      }
      form label{
        display:block;
        font-weight:600;
        margin-bottom:4px;
        font-size:12px;
        color:#444;
      }
      form input,
      form select{
        width:100%;
        padding:10px 12px;
        box-sizing:border-box;
        margin-bottom:var(--margen);
        border:1px solid rgba(75,0,130,0.3);
        border-radius:var(--radio);
        background-color:#ffffff;
        font-size:13px;
        transition:border 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease;
      }
      form input:focus,
      form select:focus{
        outline:none;
        border-color:var(--color_primario);
        box-shadow:0 0 0 2px rgba(75,0,130,0.15);
        background-color:#ffffff;
      }
      form input[type=checkbox]{
        width:auto;
        padding:0;
        margin-top:5px;
        box-shadow:none;
      }
      form input[type=submit]{
        background-color:var(--color_primario);
        color:white;
        cursor:pointer;
        border:none;
        font-weight:600;
        text-transform:uppercase;
        letter-spacing:0.8px;
        box-shadow:0 4px 10px rgba(75,0,130,0.4);
      }
      form input[type=submit]:hover{
        box-shadow:0 5px 14px rgba(75,0,130,0.6);
        transform:translateY(-1px);
      }

      /* LOGIN */
      .login-box{
        max-width:420px;
        margin:80px auto;
        background-color:#ffffff;
        padding:var(--margen);
        border-radius:16px;
        border:1px solid rgba(75,0,130,0.2);
        box-shadow:0 14px 40px rgba(0,0,0,0.18);
        column-count:1;
        position:relative;
        overflow:hidden;
      }
      .login-box h2{
        margin-top:0;
        margin-bottom:var(--margen);
        color:var(--color_primario);
      }
      .login-box form{
        columns:1;
      }
      .login-error{
        background-color:#ffdddd;
        border:1px solid #cc0000;
        color:#660000;
        padding:10px;
        border-radius:var(--radio);
        margin-bottom:var(--margen);
        font-size:14px;
      }

      /* DASHBOARD / PIE CHARTS */
      .dashboard-intro{
        margin-bottom:var(--margen);
        font-size:14px;
        color:#555;
        max-width:700px;
      }
      .charts-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(360px,1fr));
        gap:var(--margen);
      }
      .chart{
        background-color:#ffffff;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        position:relative;
        overflow:hidden;
      }
      .chart h3{
        margin-top:0;
        margin-bottom:8px;
        font-size:15px;
        color:var(--color_primario);
      }
      .chart-subtitle{
        font-size:11px;
        color:#777;
        margin-bottom:8px;
      }

      .chart-pie-wrapper{
        display:flex;
        align-items:center;
        gap:12px;
      }
      .chart-pie{
        width:120px;
        height:120px;
        flex:0 0 auto;
      }
      .chart-pie svg{
        width:100%;
        height:100%;
        transform:rotate(-90deg);
      }
      .donut-ring{
        fill:none;
        stroke:#e0e2ff;
        stroke-width:10;
      }
      .donut-segment{
        fill:none;
        stroke-width:10;
      }
      .segment-0{ stroke:var(--chart-color-0); }
      .segment-1{ stroke:var(--chart-color-1); }
      .segment-2{ stroke:var(--chart-color-2); }
      .segment-3{ stroke:var(--chart-color-3); }
      .segment-4{ stroke:var(--chart-color-4); }
      .segment-5{ stroke:var(--chart-color-5); }
      .segment-6{ stroke:var(--chart-color-6); }
      .segment-7{ stroke:var(--chart-color-7); }

      .chart-legend{
        list-style:none;
        padding:0;
        margin:0;
        font-size:11px;
        color:#555;
        flex:1 1 auto;
      }
      .chart-legend li{
        display:flex;
        align-items:center;
        margin-bottom:4px;
      }
      .legend-color{
        width:10px;
        height:10px;
        border-radius:50%;
        margin-right:6px;
        flex:0 0 auto;
      }
      .legend-color.segment-0{ background-color:var(--chart-color-0); }
      .legend-color.segment-1{ background-color:var(--chart-color-1); }
      .legend-color.segment-2{ background-color:var(--chart-color-2); }
      .legend-color.segment-3{ background-color:var(--chart-color-3); }
      .legend-color.segment-4{ background-color:var(--chart-color-4); }
      .legend-color.segment-5{ background-color:var(--chart-color-5); }
      .legend-color.segment-6{ background-color:var(--chart-color-6); }
      .legend-color.segment-7{ background-color:var(--chart-color-7); }
      .legend-label{
        flex:1 1 auto;
        overflow:hidden;
        text-overflow:ellipsis;
        white-space:nowrap;
      }
      .legend-value{
        margin-left:4px;
        color:#333;
      }

      .back-link{
        margin-bottom:var(--margen);
        display:inline-block;
        text-decoration:none;
        color:var(--color_primario);
        font-size:13px;
        padding:4px 8px;
        border-radius:999px;
        background-color:#dadfff;
      }
      .back-link::before{
        content:"← ";
      }
      .subsection{
        margin-top:var(--margen);
      }
      .subsection h3{
        margin-bottom:6px;
        color:#333;
      }
      .subsection h4{
        margin:8px 0 4px;
        font-size:13px;
        color:#555;
      }

      /* VISTAS TABLA / TARJETAS */
      .vista-activa{display:block;}
      .vista-oculta{display:none;}

      .cards-container{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
        gap:var(--margen);
      }
      .card-registro{
        background-color:#ffffff;
        border-radius:var(--radio);
        border:1px solid rgba(75,0,130,0.18);
        padding:var(--margen);
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        display:flex;
        flex-direction:column;
        justify-content:space-between;
      }
      .card-fields{
        margin-bottom:10px;
      }
      .card-field{
        margin-bottom:6px;
        font-size:12px;
      }
      .card-field-label{
        font-weight:600;
        color:#555;
        margin-bottom:2px;
      }
      .card-field-value{
        color:#222;
        word-break:break-word;
      }
      .card-actions{
        align-self:flex-end;
        margin-top:8px;
      }
      .card-actions .eliminar,
      .card-actions .editar,
      .card-actions .reportar{
        margin-left:0;
        margin-right:4px;
      }

      @media (max-width:900px){
        body{flex-direction:column;}
        nav{
          flex:none;
          max-width:none;
          box-shadow:0 4px 12px rgba(0,0,0,0.2);
        }
        .chart-pie-wrapper{
          flex-direction:column;
          align-items:flex-start;
        }
      }
      #corporativo a{color:inherit;text-decoration:none;}
    </style>
  </head>
  <body>
  
    <nav>
      <div id="corporativo">
        <a href="?">
          <div style="display:flex;align-items:center;gap:calc(var(--margen)/2);">
            <img src="https://jocarsa.github.io/logos/logos/jocarsa%20%7C%20AliceBlue.svg" alt="jocarsa">
            <p>jocarsa</p>
          </div>
        </a>
      </div>

      <?php
        // Listado de tablas SOLO si está logueado
        if ($logged_in && isset($conexion) && $conexion){
          $resultado = mysqli_query($conexion, "SHOW TABLES;");
          $tabla_actual_nav = isset($_GET['tabla']) ? $_GET['tabla'] : "";
          while($fila = mysqli_fetch_assoc($resultado)){
            $nombre_tabla = array_values($fila)[0];
            $clase = ($nombre_tabla == $tabla_actual_nav) ? "activo" : "";
            $template_file_nav = __DIR__ . "/templates/".$nombre_tabla.".php";
            $tiene_template_nav = file_exists($template_file_nav);

            echo "<button class='".$clase."'>";
              echo "<a href='?tabla=".$nombre_tabla."'>".$nombre_tabla."</a>";
              if($nombre_tabla == $tabla_actual_nav){
                if($tiene_template_nav){
                  echo "<div class='dos_botones'><a href='?operacion=añadir&tabla=".$tabla_actual_nav."' class='anadir anadir-normal'>+</a>";
                  echo "<a href='?operacion=añadir&tabla=".$tabla_actual_nav."&template=1' class='anadir anadir-template'>+</a></div>";
                }else{
                  echo "<a href='?operacion=añadir&tabla=".$tabla_actual_nav."' class='anadir anadir-normal'>+</a>";
                }
              }
            echo "</button>";
          }
        }
      ?>
    </nav>
    <main>
      <?php
        // Si NO está logueado -> login
        if(!$logged_in){
          echo "<div class='login-box'>";
          echo "<h2>Acceso a microERP</h2>";
          if($login_error){
            echo "<div class='login-error'>".$login_error."</div>";
          }
          echo "<form method='POST' action=''>";
          echo "<input type='hidden' name='accion' value='login'>";
          echo "<input type='text' name='usuario' placeholder='Usuario' autofocus>";
          echo "<input type='password' name='contrasena' placeholder='Contraseña'>";
          echo "<input type='submit' value='Entrar'>";
          echo "</form>";
          echo "<p style='font-size:12px;color:#555;margin-top:10px;'>Usuario inicial: <b>jocarsa</b> · Contraseña: <b>jocarsa</b></p>";
          echo "</div>";
        } else {

          // HEADER PRINCIPAL DINÁMICO
          $tabla_header     = $_GET['tabla']     ?? null;
          $operacion_header = $_GET['operacion'] ?? '';
          $page_title = "Dashboard de microERP";

          if($tabla_header){
            switch($operacion_header){
              case 'añadir':
                $page_title = "Añadir registro en ".$tabla_header;
                break;
              case 'editar':
                $page_title = "Editar registro en ".$tabla_header;
                break;
              case 'report':
                $page_title = "Informe de ".$tabla_header;
                break;
              default:
                $page_title = "Listado de ".$tabla_header;
            }
          }

          echo "<header class='main-header'>";
          echo "<div class='main-title'>".$page_title."</div>";
          echo "<div class='main-actions'>";

          if($tabla_header && $operacion_header === ''){
            echo "<button type='button' id='btn-vista-tabla' class='view-toggle active'>Tabla</button>";
            echo "<button type='button' id='btn-vista-tarjetas' class='view-toggle'>Tarjetas</button>";
          }

          echo "<span class='login-user-label'>".htmlspecialchars($_SESSION['usuario'])."</span>";
          echo "<a href='?logout=1' class='logout'>Salir</a>";
          echo "</div>";
          echo "</header>";

          // Lógica del microERP
          if(isset($_GET['tabla'])){
            $tabla      = $_GET['tabla'];
            $operacion  = $_GET['operacion'] ?? '';
            $id         = isset($_GET['id']) ? $_GET['id'] : null;

            $foreignKeys  = obtener_claves_foraneas($conexion, $tabla, $db_name);
            $columnMeta   = obtener_meta_columnas($conexion, $tabla, $db_name);
            $primaryKey   = obtener_pk_columna($conexion, $tabla, $db_name);

            // Gestión de plantillas
            $templates_dir        = __DIR__ . "/templates";
            $template_file        = $templates_dir . "/".$tabla.".php";
            $hay_template_tabla   = file_exists($template_file);
            $usar_template        = (isset($_GET['template']) && $_GET['template'] === '1' && $hay_template_tabla);

            // Eliminación
            if($operacion === "eliminar" && $id !== null && $primaryKey){
              $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
              mysqli_query(
                $conexion,
                "DELETE FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql.";"
              );
              $operacion = '';
            }

            // AÑADIR
            if($operacion === "añadir"){
              // Procesar inserción
              if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                $columnas = [];
                $valores  = [];

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                  $data_type   = strtolower($meta_columna['DATA_TYPE']);
                  $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                  if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                    $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = intval($valor);
                    continue;
                  }

                  if(isset($_POST[$nombre_columna]) && $_POST[$nombre_columna] !== ''){
                    $columnas[] = "`".$nombre_columna."`";
                    $valores[]  = "'".mysqli_real_escape_string($conexion,$_POST[$nombre_columna])."'";
                  }
                }

                if(count($columnas) > 0){
                  $sql_insert = "INSERT INTO ".$tabla." (".implode(",",$columnas).") VALUES (".implode(",",$valores).")";
                  mysqli_query($conexion, $sql_insert);
                }
              }

              echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

              $form_action   = "?operacion=añadir&tabla=".$tabla;
              if($usar_template){ $form_action .= "&template=1"; }

              if($usar_template){
                $template_mode = 'insert';
                $fila_actual   = null;
                include $template_file;
              }else{
                echo "<form action='".$form_action."' method='POST'>";

                foreach($columnMeta as $nombre_columna => $meta_columna){
                  if($primaryKey && $nombre_columna === $primaryKey){ continue; }

                  if(isset($foreignKeys[$nombre_columna])){
                    $fk = $foreignKeys[$nombre_columna];
                    $tabla_fk   = $fk['tabla'];
                    $columna_fk = $fk['columna'];

                    echo "<label>".$nombre_columna."</label>";
                    echo "<select name='".$nombre_columna."'>";
                    echo "<option value=''>-- seleccionar --</option>";

                    $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                    if($res_fk){
                      while($fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $texto_opcion = implode(" | ", $partes);
                        $value_opcion = $fila_fk[$columna_fk];
                        echo "<option value='".$value_opcion."'>".$texto_opcion."</option>";
                      }
                    }

                    echo "</select>";
                  }else{
                    echo render_input_para_columna($nombre_columna, $meta_columna);
                  }
                }
                echo "<input type='submit' value='Guardar'>";
                echo "</form>";
              }

            // EDITAR
            } elseif($operacion === "editar" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede editar un registro concreto.</p>";
              } else {
                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                  echo "<p>No se ha encontrado el registro a editar.</p>";
                } else {
                  // Procesar actualización
                  if($_SERVER['REQUEST_METHOD'] === 'POST' && (!isset($_POST['accion']) || $_POST['accion'] !== 'login')){
                    $sets = [];

                    foreach($columnMeta as $nombre_columna => $meta_columna){
                      if($nombre_columna === $primaryKey){ continue; }

                      $data_type   = strtolower($meta_columna['DATA_TYPE']);
                      $column_type = strtolower($meta_columna['COLUMN_TYPE']);

                      if($data_type === 'tinyint' && strpos($column_type,'(1)') !== false){
                        $valor = isset($_POST[$nombre_columna]) ? 1 : 0;
                        $sets[] = "`".$nombre_columna."`=".intval($valor);
                        continue;
                      }

                      if(isset($_POST[$nombre_columna])){
                        $valor = $_POST[$nombre_columna];
                        $sets[] = "`".$nombre_columna."` = '".mysqli_real_escape_string($conexion,$valor)."'";
                      }
                    }

                    if(count($sets) > 0){
                      $sql_update = "UPDATE ".$tabla." SET ".implode(", ",$sets)." WHERE `".$primaryKey."` = ".$id_sql;
                      mysqli_query($conexion, $sql_update);
                    }

                    $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                    $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : $fila_actual;
                  }

                  echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

                  $form_action = "?operacion=editar&tabla=".$tabla."&id=".urlencode($id);
                  if($usar_template){ $form_action .= "&template=1"; }

                  if($usar_template){
                    $template_mode = 'update';
                    include $template_file;
                  }else{
                    echo "<form action='".$form_action."' method='POST'>";

                    if($primaryKey && isset($fila_actual[$primaryKey])){
                      echo "<label>".$primaryKey."</label>";
                      echo "<input type='text' value='".htmlspecialchars($fila_actual[$primaryKey],ENT_QUOTES)."' disabled>";
                    }

                    foreach($columnMeta as $nombre_columna => $meta_columna){
                      if($nombre_columna === $primaryKey){ continue; }
                      $valor_actual = $fila_actual[$nombre_columna] ?? "";

                      if(isset($foreignKeys[$nombre_columna])){
                        $fk = $foreignKeys[$nombre_columna];
                        $tabla_fk   = $fk['tabla'];
                        $columna_fk = $fk['columna'];

                        echo "<label>".$nombre_columna."</label>";
                        echo "<select name='".$nombre_columna."'>";
                        echo "<option value=''>-- seleccionar --</option>";

                        $res_fk = mysqli_query($conexion, "SELECT * FROM ".$tabla_fk.";");
                        if($res_fk){
                          while($fila_fk = mysqli_fetch_assoc($res_fk)){
                            $partes = [];
                            foreach($fila_fk as $k2=>$v2){
                              $partes[] = $v2;
                            }
                            $texto_opcion = implode(" | ", $partes);
                            $value_opcion = $fila_fk[$columna_fk];
                            $selected = ($valor_actual == $value_opcion) ? "selected" : "";
                            echo "<option value='".$value_opcion."' ".$selected.">".$texto_opcion."</option>";
                          }
                        }

                        echo "</select>";
                      }else{
                        echo render_input_para_columna($nombre_columna, $meta_columna, $valor_actual);
                      }
                    }

                    echo "<input type='submit' value='Guardar cambios'>";
                    echo "</form>";
                  }
                }
              }

            // INFORME
            } elseif($operacion === "report" && $id !== null){

              if(!$primaryKey){
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";
                echo "<p>La tabla <b>".$tabla."</b> no tiene clave primaria definida en el esquema, por lo que no se puede generar un informe por registro.</p>";
              } else {
                echo "<a href='?tabla=".$tabla."' class='back-link'>Volver al listado</a>";

                $id_sql = "'".mysqli_real_escape_string($conexion,$id)."'";
                $res_actual = mysqli_query($conexion, "SELECT * FROM ".$tabla." WHERE `".$primaryKey."` = ".$id_sql." LIMIT 1;");
                $fila_actual = $res_actual ? mysqli_fetch_assoc($res_actual) : null;

                if(!$fila_actual){
                  echo "<p>No se ha encontrado el registro solicitado.</p>";
                } else {
                  echo "<div class='subsection'>";
                  echo "<h3>Registro principal</h3>";
                  render_tabla_html_con_links($conexion, $tabla, [$fila_actual], $db_name);
                  echo "</div>";

                  echo "<div class='subsection'>";
                  echo "<h3>Datos referenciados por este registro</h3>";

                  $hay_referenciados = false;
                  foreach($foreignKeys as $columna_fk_local => $info_fk){
                    $valor_fk = $fila_actual[$columna_fk_local] ?? null;
                    if($valor_fk === null || $valor_fk === ''){ continue; }

                    $tabla_fk   = $info_fk['tabla'];
                    $col_fk     = $info_fk['columna'];

                    $sql_fk = "SELECT * FROM ".$tabla_fk." WHERE ".$col_fk." = '".mysqli_real_escape_string($conexion,$valor_fk)."'";
                    $res_fk = mysqli_query($conexion, $sql_fk);
                    if($res_fk && mysqli_num_rows($res_fk) > 0){
                      $hay_referenciados = true;
                      $rows_fk = [];
                      while($row_fk = mysqli_fetch_assoc($res_fk)){
                        $rows_fk[] = $row_fk;
                      }

                      echo "<h4>".$tabla_fk." (por ".$columna_fk_local.")</h4>";
                      render_tabla_html_con_links($conexion, $tabla_fk, $rows_fk, $db_name);
                    }
                  }
                  if(!$hay_referenciados){
                    echo "<p class='no-data'>No hay referencias salientes.</p>";
                  }
                  echo "</div>";

                  echo "<div class='subsection'>";
                  echo "<h3>Datos relacionados que apuntan a este registro</h3>";

                  $refs_entrantes = obtener_tablas_que_referencian($conexion, $tabla, $db_name);
                  if(count($refs_entrantes) === 0){
                    echo "<p class='no-data'>No hay tablas que referencien a esta entidad.</p>";
                  } else {
                    $hay_entrantes = false;
                    foreach($refs_entrantes as $ref){
                      $tabla_hija        = $ref['tabla'];
                      $columna_hija      = $ref['columna'];
                      $col_ref_padre     = $ref['columna_referenciada'];

                      $valor_ref_padre = $fila_actual[$col_ref_padre] ?? null;
                      if($valor_ref_padre === null){ continue; }

                      $sql_hija = "SELECT * FROM ".$tabla_hija." WHERE ".$columna_hija." = '".mysqli_real_escape_string($conexion,$valor_ref_padre)."'";
                      $res_hija = mysqli_query($conexion, $sql_hija);
                      if($res_hija && mysqli_num_rows($res_hija) > 0){
                        $hay_entrantes = true;
                        $rows_hija = [];
                        while($fila_hija = mysqli_fetch_assoc($res_hija)){
                          $rows_hija[] = $fila_hija;
                        }

                        echo "<h4>".$tabla_hija." (columna ".$columna_hija.")</h4>";
                        render_tabla_html_con_links($conexion, $tabla_hija, $rows_hija, $db_name);
                      }
                    }
                    if(!$hay_entrantes){
                      echo "<p class='no-data'>No hay registros entrantes que apunten a este registro.</p>";
                    }
                  }

                  echo "</div>";
                }
              }

            // LISTADO
            } else {

              if(!$primaryKey){
                echo "<p class='no-data'>Aviso: la tabla <b>".$tabla."</b> no tiene clave primaria definida. No se podrán editar ni eliminar registros individualmente.</p>";
              }

              $resultado = mysqli_query($conexion, "SELECT * FROM ".$tabla.";");
              $rows = [];
              if($resultado){
                while($fila = mysqli_fetch_assoc($resultado)){
                  $rows[] = $fila;
                }
              }

              if(count($rows) === 0){
                echo "<p class='no-data'>No hay registros en esta tabla.</p>";
              } else {

                // VISTA TABLA
                echo "<div id='vista-tabla' class='vista-activa'>";
                echo "<table>";
                $contador = 0;
                foreach($rows as $fila){
                  if($contador == 0){
                    echo "<tr>";
                      foreach($fila as $clave=>$valor){
                        echo "<th>".$clave."</th>";
                      }
                      echo "<th>Acciones</th>";
                    echo "</tr>";
                  }

                  echo "<tr>";
                  foreach($fila as $clave=>$valor){
                    if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                      $fk = $foreignKeys[$clave];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      $sql_fk = "
                        SELECT *
                        FROM ".$tabla_fk."
                        WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                        LIMIT 1
                      ";
                      $res_fk = mysqli_query($conexion, $sql_fk);
                      if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $texto_celda = implode(" | ", $partes);
                        echo "<td>".htmlspecialchars($texto_celda,ENT_QUOTES)."</td>";
                      }else{
                        echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                      }
                    }else{
                      echo "<td>".htmlspecialchars($valor,ENT_QUOTES)."</td>";
                    }
                  }

                  echo "<td>";
                  if($primaryKey && isset($fila[$primaryKey])){
                    $id_fila = $fila[$primaryKey];
                    $id_url  = urlencode($id_fila);
                    echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                    if($hay_template_tabla){
                      echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."&template=1' class='editar editar-template'>✏</a>";
                    }
                    echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                    echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                  } else {
                    echo "<span style='font-size:11px;color:#777;'>—</span>";
                  }
                  echo "</td>";

                  echo "</tr>";
                  $contador++;
                }
                echo "</table>";
                echo "</div>";

                // VISTA TARJETAS
                echo "<div id='vista-tarjetas' class='vista-oculta'>";
                echo "<div class='cards-container'>";
                foreach($rows as $fila){
                  echo "<article class='card-registro'>";
                  echo "<div class='card-fields'>";
                  foreach($fila as $clave=>$valor){
                    echo "<div class='card-field'>";
                    echo "<div class='card-field-label'>".$clave."</div>";

                    $display_value = $valor;

                    if(isset($foreignKeys[$clave]) && $valor !== null && $valor !== ''){
                      $fk = $foreignKeys[$clave];
                      $tabla_fk   = $fk['tabla'];
                      $columna_fk = $fk['columna'];

                      $sql_fk = "
                        SELECT *
                        FROM ".$tabla_fk."
                        WHERE ".$columna_fk." = '".mysqli_real_escape_string($conexion,$valor)."'
                        LIMIT 1
                      ";
                      $res_fk = mysqli_query($conexion, $sql_fk);
                      if($res_fk && $fila_fk = mysqli_fetch_assoc($res_fk)){
                        $partes = [];
                        foreach($fila_fk as $k2=>$v2){
                          $partes[] = $v2;
                        }
                        $display_value = implode(" | ", $partes);
                      }else{
                        $display_value = $valor;
                      }
                    }

                    echo "<div class='card-field-value'>".htmlspecialchars($display_value,ENT_QUOTES)."</div>";
                    echo "</div>";
                  }
                  echo "</div>";

                  echo "<div class='card-actions'>";
                  if($primaryKey && isset($fila[$primaryKey])){
                    $id_fila = $fila[$primaryKey];
                    $id_url  = urlencode($id_fila);
                    echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."' class='editar'>✏</a>";
                    if($hay_template_tabla){
                      echo "<a href='?operacion=editar&tabla=".$tabla."&id=".$id_url."&template=1' class='editar editar-template'>✏</a>";
                    }
                    echo "<a href='?operacion=report&tabla=".$tabla."&id=".$id_url."' class='reportar'>i</a>";
                    echo "<a href='?operacion=eliminar&tabla=".$tabla."&id=".$id_url."' class='eliminar'>×</a>";
                  }
                  echo "</div>";

                  echo "</article>";
                }
                echo "</div>";
                echo "</div>";
              }
            }
          } else {
            // DASHBOARD INICIAL
            echo "<p class='dashboard-intro'>
              Resumen gráfico de la información categórica y relacional del sistema:
              campos <b>ENUM/SET</b> y campos de <b>clave foránea</b> en todas las tablas, representados como gráficos de tipo donut.
            </p>";

            $resultado = mysqli_query($conexion, "SHOW TABLES;");
            echo "<div class='charts-grid'>";
            while($fila = mysqli_fetch_assoc($resultado)){
              $tabla = array_values($fila)[0];
              $meta  = obtener_meta_columnas($conexion, $tabla, $db_name);
              $fksTabla = obtener_claves_foraneas($conexion, $tabla, $db_name);

              // ENUM/SET
              foreach($meta as $nombre_columna => $meta_columna){
                $data_type = strtolower($meta_columna['DATA_TYPE']);
                if($data_type !== 'enum' && $data_type !== 'set'){ continue; }

                $sql_dist = "
                  SELECT ".$nombre_columna." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$nombre_columna."
                  ORDER BY total DESC
                ";
                $res_dist = mysqli_query($conexion, $sql_dist);
                if(!$res_dist || mysqli_num_rows($res_dist) < 1){ continue; }

                $segmentos = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist)){
                  $v = $fila_dist['valor'];
                  $c = (int)$fila_dist['total'];
                  $segmentos[] = [
                    'label' => ($v === null || $v === '' ? '(vacío)' : $v),
                    'total' => $c
                  ];
                }
                if(empty($segmentos)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$nombre_columna."</h3>";
                echo "<div class='chart-subtitle'>Distribución de valores ENUM/SET</div>";
                render_pie_chart($segmentos, $tabla."_".$nombre_columna."_enum");
                echo "</div>";
              }

              // FKs
              foreach($fksTabla as $columna_fk => $info_fk){
                $tabla_ref = $info_fk['tabla'];
                $col_ref   = $info_fk['columna'];

                $sql_dist_fk = "
                  SELECT ".$columna_fk." AS valor, COUNT(*) AS total
                  FROM ".$tabla."
                  GROUP BY ".$columna_fk."
                  ORDER BY total DESC
                ";
                $res_dist_fk = mysqli_query($conexion, $sql_dist_fk);
                if(!$res_dist_fk || mysqli_num_rows($res_dist_fk) < 1){ continue; }

                $segmentos_fk = [];
                while($fila_dist = mysqli_fetch_assoc($res_dist_fk)){
                  $valor_fk = $fila_dist['valor'];
                  $c        = (int)$fila_dist['total'];

                  if($valor_fk === null || $valor_fk === ''){
                    $label = '(sin valor)';
                  }else{
                    $sql_ref = "
                      SELECT *
                      FROM ".$tabla_ref."
                      WHERE ".$col_ref." = '".mysqli_real_escape_string($conexion,$valor_fk)."'
                      LIMIT 1
                    ";
                    $res_ref = mysqli_query($conexion, $sql_ref);
                    if($res_ref && $fila_ref = mysqli_fetch_assoc($res_ref)){
                      $partes = [];
                      foreach($fila_ref as $k2=>$v2){
                        $partes[] = $v2;
                      }
                      $label = implode(" | ", $partes);
                    }else{
                      $label = 'ID '.$valor_fk.' (huérfano)';
                    }
                  }

                  $segmentos_fk[] = [
                    'label' => $label,
                    'total' => $c
                  ];
                }
                if(empty($segmentos_fk)){ continue; }

                echo "<div class='chart'>";
                echo "<h3>".$tabla." · ".$columna_fk."</h3>";
                echo "<div class='chart-subtitle'>Distribución por referencia a ".$tabla_ref."</div>";
                render_pie_chart($segmentos_fk, $tabla."_".$columna_fk."_fk");
                echo "</div>";
              }
            }
            echo "</div>";
          }
        }
      ?>
    </main>

    <script>
      document.addEventListener('DOMContentLoaded', function(){
        var btnTabla     = document.getElementById('btn-vista-tabla');
        var btnTarjetas  = document.getElementById('btn-vista-tarjetas');
        var vistaTabla   = document.getElementById('vista-tabla');
        var vistaTarjetas= document.getElementById('vista-tarjetas');

        if(btnTabla && btnTarjetas && vistaTabla && vistaTarjetas){
          btnTabla.addEventListener('click', function(){
            vistaTabla.classList.add('vista-activa');
            vistaTabla.classList.remove('vista-oculta');
            vistaTarjetas.classList.add('vista-oculta');
            vistaTarjetas.classList.remove('vista-activa');
            btnTabla.classList.add('active');
            btnTarjetas.classList.remove('active');
          });
          btnTarjetas.addEventListener('click', function(){
            vistaTabla.classList.add('vista-oculta');
            vistaTabla.classList.remove('vista-activa');
            vistaTarjetas.classList.add('vista-activa');
            vistaTarjetas.classList.remove('vista-oculta');
            btnTarjetas.classList.add('active');
            btnTabla.classList.remove('active');
          });
        }
      });
    </script>
  </body>
</html>
```

### tiendaonline

```sql
-- =============================================
-- ONLINE SHOP DATABASE SCHEMA
-- =============================================

-- Drop tables if they exist (in reverse order of dependencies)
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS cart_items;
DROP TABLE IF EXISTS product_images;
DROP TABLE IF EXISTS product_reviews;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS payment_methods;
DROP TABLE IF EXISTS shipping_methods;
DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS order_statuses;
DROP TABLE IF EXISTS payment_statuses;

-- =============================================
-- LOOKUP/REFERENCE TABLES
-- =============================================

-- Countries table
CREATE TABLE countries (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) NOT NULL UNIQUE,
    country_code CHAR(2) NOT NULL UNIQUE,
    phone_prefix VARCHAR(10)
);

-- Cities table
CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    postal_code VARCHAR(20),
    FOREIGN KEY (country_id) REFERENCES countries(country_id),
    UNIQUE KEY unique_city_country (city_name, country_id)
);

-- Order statuses
CREATE TABLE order_statuses (
    status_id INT PRIMARY KEY AUTO_INCREMENT,
    status_name VARCHAR(50) NOT NULL UNIQUE,
    status_description VARCHAR(255)
);

-- Payment statuses
CREATE TABLE payment_statuses (
    payment_status_id INT PRIMARY KEY AUTO_INCREMENT,
    status_name VARCHAR(50) NOT NULL UNIQUE
);

-- Shipping methods
CREATE TABLE shipping_methods (
    shipping_method_id INT PRIMARY KEY AUTO_INCREMENT,
    method_name VARCHAR(100) NOT NULL UNIQUE,
    base_cost DECIMAL(10, 2) NOT NULL,
    estimated_days INT,
    description TEXT
);

-- Payment methods
CREATE TABLE payment_methods (
    payment_method_id INT PRIMARY KEY AUTO_INCREMENT,
    method_name VARCHAR(50) NOT NULL UNIQUE,
    is_active BOOLEAN DEFAULT TRUE
);

-- Brands table
CREATE TABLE brands (
    brand_id INT PRIMARY KEY AUTO_INCREMENT,
    brand_name VARCHAR(100) NOT NULL UNIQUE,
    brand_description TEXT,
    website_url VARCHAR(255)
);

-- Categories table
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    parent_category_id INT,
    category_description TEXT,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id)
);

-- =============================================
-- CUSTOMER RELATED TABLES
-- =============================================

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Addresses table
CREATE TABLE addresses (
    address_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    address_type ENUM('billing', 'shipping', 'both') NOT NULL,
    street_address VARCHAR(255) NOT NULL,
    apartment VARCHAR(50),
    city_id INT NOT NULL,
    postal_code VARCHAR(20),
    is_default BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- =============================================
-- PRODUCT RELATED TABLES
-- =============================================

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    sku VARCHAR(100) NOT NULL UNIQUE,
    category_id INT NOT NULL,
    brand_id INT,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    discount_percentage DECIMAL(5, 2) DEFAULT 0,
    stock_quantity INT NOT NULL DEFAULT 0,
    weight_kg DECIMAL(8, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id)
);

-- Product images table
CREATE TABLE product_images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    image_url VARCHAR(500) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product reviews table
CREATE TABLE product_reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_title VARCHAR(255),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_verified_purchase BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- =============================================
-- SHOPPING CART TABLES
-- =============================================

-- Cart items table
CREATE TABLE cart_items (
    cart_item_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    UNIQUE KEY unique_customer_product (customer_id, product_id)
);

-- =============================================
-- ORDER RELATED TABLES
-- =============================================

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_number VARCHAR(50) NOT NULL UNIQUE,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status_id INT NOT NULL,
    payment_status_id INT NOT NULL,
    payment_method_id INT NOT NULL,
    shipping_method_id INT NOT NULL,
    shipping_address_id INT NOT NULL,
    billing_address_id INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    shipping_cost DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0,
    total_amount DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (status_id) REFERENCES order_statuses(status_id),
    FOREIGN KEY (payment_status_id) REFERENCES payment_statuses(payment_status_id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(payment_method_id),
    FOREIGN KEY (shipping_method_id) REFERENCES shipping_methods(shipping_method_id),
    FOREIGN KEY (shipping_address_id) REFERENCES addresses(address_id),
    FOREIGN KEY (billing_address_id) REFERENCES addresses(address_id)
);

-- Order items table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0,
    total_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- =============================================
-- INSERT SAMPLE DATA
-- =============================================

-- Insert Countries
INSERT INTO countries (country_name, country_code, phone_prefix) VALUES
('Spain', 'ES', '+34'),
('United States', 'US', '+1'),
('United Kingdom', 'UK', '+44'),
('Germany', 'DE', '+49'),
('France', 'FR', '+33');

-- Insert Cities
INSERT INTO cities (city_name, country_id, postal_code) VALUES
('Madrid', 1, '28001'),
('Barcelona', 1, '08001'),
('New York', 2, '10001'),
('Los Angeles', 2, '90001'),
('London', 3, 'SW1A'),
('Berlin', 4, '10115'),
('Paris', 5, '75001');

-- Insert Order Statuses
INSERT INTO order_statuses (status_name, status_description) VALUES
('Pending', 'Order has been placed but not yet processed'),
('Processing', 'Order is being prepared'),
('Shipped', 'Order has been shipped'),
('Delivered', 'Order has been delivered'),
('Cancelled', 'Order has been cancelled'),
('Refunded', 'Order has been refunded');

-- Insert Payment Statuses
INSERT INTO payment_statuses (status_name) VALUES
('Pending'),
('Completed'),
('Failed'),
('Refunded');

-- Insert Shipping Methods
INSERT INTO shipping_methods (method_name, base_cost, estimated_days, description) VALUES
('Standard Shipping', 5.99, 7, 'Regular delivery within 5-7 business days'),
('Express Shipping', 14.99, 3, 'Fast delivery within 2-3 business days'),
('Overnight Shipping', 29.99, 1, 'Next day delivery'),
('Free Shipping', 0.00, 10, 'Free standard delivery for orders over $50');

-- Insert Payment Methods
INSERT INTO payment_methods (method_name, is_active) VALUES
('Credit Card', TRUE),
('Debit Card', TRUE),
('PayPal', TRUE),
('Apple Pay', TRUE),
('Google Pay', TRUE),
('Bank Transfer', TRUE);

-- Insert Brands
INSERT INTO brands (brand_name, brand_description, website_url) VALUES
('TechMaster', 'Leading electronics manufacturer', 'https://techmaster.example.com'),
('StyleWear', 'Fashion and apparel brand', 'https://stylewear.example.com'),
('HomeComfort', 'Home and living products', 'https://homecomfort.example.com'),
('SportPro', 'Sports and fitness equipment', 'https://sportpro.example.com'),
('BeautyGlow', 'Beauty and cosmetics', 'https://beautyglow.example.com');

-- Insert Categories
INSERT INTO categories (category_name, parent_category_id, category_description) VALUES
('Electronics', NULL, 'Electronic devices and accessories'),
('Clothing', NULL, 'Apparel and fashion items'),
('Home & Garden', NULL, 'Home improvement and garden supplies'),
('Sports & Outdoors', NULL, 'Sports equipment and outdoor gear'),
('Beauty & Health', NULL, 'Beauty products and health items'),
('Smartphones', 1, 'Mobile phones and accessories'),
('Laptops', 1, 'Laptop computers'),
('Men''s Clothing', 2, 'Clothing for men'),
('Women''s Clothing', 2, 'Clothing for women'),
('Furniture', 3, 'Home furniture');

-- Insert Customers
INSERT INTO customers (email, password_hash, first_name, last_name, phone, date_of_birth) VALUES
('john.doe@email.com', 'hash123abc', 'John', 'Doe', '+34600123456', '1985-03-15'),
('maria.garcia@email.com', 'hash456def', 'Maria', 'Garcia', '+34600234567', '1990-07-22'),
('james.smith@email.com', 'hash789ghi', 'James', 'Smith', '+1555123456', '1988-11-30'),
('sophie.martin@email.com', 'hash012jkl', 'Sophie', 'Martin', '+33612345678', '1992-05-18'),
('hans.mueller@email.com', 'hash345mno', 'Hans', 'Mueller', '+49151234567', '1987-09-25');

-- Insert Addresses
INSERT INTO addresses (customer_id, address_type, street_address, apartment, city_id, postal_code, is_default) VALUES
(1, 'both', 'Calle Gran Via 123', '3A', 1, '28013', TRUE),
(2, 'shipping', 'Paseo de Gracia 456', NULL, 2, '08007', TRUE),
(2, 'billing', 'Rambla Catalunya 789', '2B', 2, '08008', FALSE),
(3, 'both', '5th Avenue 789', 'Apt 12C', 3, '10022', TRUE),
(4, 'both', 'Champs-Élysées 101', NULL, 7, '75008', TRUE),
(5, 'both', 'Unter den Linden 55', NULL, 6, '10117', TRUE);

-- Insert Products
INSERT INTO products (product_name, sku, category_id, brand_id, description, price, discount_percentage, stock_quantity, weight_kg) VALUES
('TechMaster Smartphone X1', 'TM-SP-X1-001', 6, 1, 'Latest smartphone with 128GB storage and 5G connectivity', 699.99, 10, 50, 0.18),
('TechMaster Laptop Pro 15', 'TM-LP-PRO15-001', 7, 1, '15-inch laptop with Intel i7 processor and 16GB RAM', 1299.99, 15, 25, 2.1),
('StyleWear Men''s Cotton T-Shirt', 'SW-TS-MCT-BLU-M', 8, 2, 'Comfortable cotton t-shirt in blue - Medium size', 29.99, 0, 100, 0.2),
('StyleWear Women''s Summer Dress', 'SW-DR-WSD-RED-M', 9, 2, 'Elegant summer dress in red - Medium size', 79.99, 20, 45, 0.3),
('HomeComfort Office Chair', 'HC-CH-OFF-BLK', 10, 3, 'Ergonomic office chair with lumbar support', 249.99, 0, 30, 15.5),
('SportPro Running Shoes', 'SP-SH-RUN-BLK-42', 4, 4, 'Professional running shoes - Size 42', 119.99, 25, 60, 0.8),
('BeautyGlow Face Cream', 'BG-FC-HYD-50ML', 5, 5, 'Hydrating face cream 50ml', 49.99, 0, 150, 0.1),
('TechMaster Wireless Earbuds', 'TM-EB-WRL-001', 6, 1, 'Noise-cancelling wireless earbuds with charging case', 149.99, 5, 80, 0.05);

-- Insert Product Images
INSERT INTO product_images (product_id, image_url, is_primary, display_order) VALUES
(1, 'https://cdn.example.com/products/smartphone-x1-front.jpg', TRUE, 1),
(1, 'https://cdn.example.com/products/smartphone-x1-back.jpg', FALSE, 2),
(2, 'https://cdn.example.com/products/laptop-pro15-main.jpg', TRUE, 1),
(3, 'https://cdn.example.com/products/tshirt-blue-front.jpg', TRUE, 1),
(4, 'https://cdn.example.com/products/dress-red-front.jpg', TRUE, 1),
(5, 'https://cdn.example.com/products/office-chair-main.jpg', TRUE, 1),
(6, 'https://cdn.example.com/products/running-shoes-main.jpg', TRUE, 1),
(7, 'https://cdn.example.com/products/face-cream-main.jpg', TRUE, 1),
(8, 'https://cdn.example.com/products/earbuds-main.jpg', TRUE, 1);

-- Insert Product Reviews
INSERT INTO product_reviews (product_id, customer_id, rating, review_title, review_text, is_verified_purchase) VALUES
(1, 1, 5, 'Excellent phone!', 'Best smartphone I have ever owned. Fast, reliable, and great camera quality.', TRUE),
(1, 3, 4, 'Good but expensive', 'Great phone overall, but a bit pricey. Battery life could be better.', TRUE),
(2, 2, 5, 'Perfect for work', 'This laptop handles all my work tasks effortlessly. Highly recommend!', TRUE),
(3, 4, 5, 'Very comfortable', 'Great quality t-shirt, fits perfectly and the fabric is soft.', TRUE),
(6, 5, 4, 'Great running shoes', 'Comfortable and lightweight. Perfect for my daily runs.', TRUE);

-- Insert Cart Items
INSERT INTO cart_items (customer_id, product_id, quantity) VALUES
(1, 8, 1),
(1, 7, 2),
(3, 3, 3),
(5, 6, 1);

-- Insert Orders
INSERT INTO orders (customer_id, order_number, status_id, payment_status_id, payment_method_id, shipping_method_id, 
                   shipping_address_id, billing_address_id, subtotal, tax_amount, shipping_cost, discount_amount, total_amount) VALUES
(1, 'ORD-2024-001', 4, 2, 1, 2, 1, 1, 629.99, 132.30, 14.99, 70.00, 707.28),
(2, 'ORD-2024-002', 3, 2, 3, 1, 2, 3, 63.99, 13.44, 5.99, 16.00, 67.42),
(3, 'ORD-2024-003', 2, 2, 2, 3, 4, 4, 89.97, 18.89, 29.99, 0, 138.85),
(4, 'ORD-2024-004', 4, 2, 4, 1, 5, 5, 1299.99, 273.00, 0.00, 194.99, 1378.00),
(5, 'ORD-2024-005', 1, 1, 1, 1, 6, 6, 89.99, 18.90, 5.99, 30.00, 84.88);

-- Insert Order Items
INSERT INTO order_items (order_id, product_id, quantity, unit_price, discount_amount, total_price) VALUES
(1, 1, 1, 699.99, 70.00, 629.99),
(2, 4, 1, 79.99, 16.00, 63.99),
(3, 3, 3, 29.99, 0, 89.97),
(4, 2, 1, 1299.99, 194.99, 1105.00),
(5, 6, 1, 119.99, 30.00, 89.99);

-- =============================================
-- USEFUL QUERIES
-- =============================================

-- Show all products with their categories and brands
SELECT 
    p.product_name,
    p.sku,
    c.category_name,
    b.brand_name,
    p.price,
    p.stock_quantity
FROM products p
LEFT JOIN categories c ON p.category_id = c.category_id
LEFT JOIN brands b ON p.brand_id = b.brand_id;

-- Show customer orders with details
SELECT 
    o.order_number,
    CONCAT(cu.first_name, ' ', cu.last_name) AS customer_name,
    o.order_date,
    os.status_name,
    o.total_amount
FROM orders o
JOIN customers cu ON o.customer_id = cu.customer_id
JOIN order_statuses os ON o.status_id = os.status_id
ORDER BY o.order_date DESC;
```

### tiendaonlineespanol

```sql
-- =============================================
-- ESQUEMA DE BASE DE DATOS TIENDA ONLINE
-- =============================================

-- Eliminar tablas si existen (en orden inverso de dependencias)
DROP TABLE IF EXISTS articulos_pedido;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS articulos_carrito;
DROP TABLE IF EXISTS imagenes_producto;
DROP TABLE IF EXISTS resenas_producto;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS marcas;
DROP TABLE IF EXISTS metodos_pago;
DROP TABLE IF EXISTS metodos_envio;
DROP TABLE IF EXISTS direcciones;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS paises;
DROP TABLE IF EXISTS ciudades;
DROP TABLE IF EXISTS estados_pedido;
DROP TABLE IF EXISTS estados_pago;

-- =============================================
-- TABLAS DE BÚSQUEDA/REFERENCIA
-- =============================================

-- Tabla de países
CREATE TABLE paises (
    id_pais INT PRIMARY KEY AUTO_INCREMENT,
    nombre_pais VARCHAR(100) NOT NULL UNIQUE,
    codigo_pais CHAR(2) NOT NULL UNIQUE,
    prefijo_telefono VARCHAR(10)
);

-- Tabla de ciudades
CREATE TABLE ciudades (
    id_ciudad INT PRIMARY KEY AUTO_INCREMENT,
    nombre_ciudad VARCHAR(100) NOT NULL,
    id_pais INT NOT NULL,
    codigo_postal VARCHAR(20),
    FOREIGN KEY (id_pais) REFERENCES paises(id_pais),
    UNIQUE KEY ciudad_pais_unico (nombre_ciudad, id_pais)
);

-- Estados de pedido
CREATE TABLE estados_pedido (
    id_estado INT PRIMARY KEY AUTO_INCREMENT,
    nombre_estado VARCHAR(50) NOT NULL UNIQUE,
    descripcion_estado VARCHAR(255)
);

-- Estados de pago
CREATE TABLE estados_pago (
    id_estado_pago INT PRIMARY KEY AUTO_INCREMENT,
    nombre_estado VARCHAR(50) NOT NULL UNIQUE
);

-- Métodos de envío
CREATE TABLE metodos_envio (
    id_metodo_envio INT PRIMARY KEY AUTO_INCREMENT,
    nombre_metodo VARCHAR(100) NOT NULL UNIQUE,
    coste_base DECIMAL(10, 2) NOT NULL,
    dias_estimados INT,
    descripcion TEXT
);

-- Métodos de pago
CREATE TABLE metodos_pago (
    id_metodo_pago INT PRIMARY KEY AUTO_INCREMENT,
    nombre_metodo VARCHAR(50) NOT NULL UNIQUE,
    esta_activo BOOLEAN DEFAULT TRUE
);

-- Tabla de marcas
CREATE TABLE marcas (
    id_marca INT PRIMARY KEY AUTO_INCREMENT,
    nombre_marca VARCHAR(100) NOT NULL UNIQUE,
    descripcion_marca TEXT,
    url_sitio_web VARCHAR(255)
);

-- Tabla de categorías
CREATE TABLE categorias (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(100) NOT NULL UNIQUE,
    id_categoria_padre INT,
    descripcion_categoria TEXT,
    FOREIGN KEY (id_categoria_padre) REFERENCES categorias(id_categoria)
);

-- =============================================
-- TABLAS RELACIONADAS CON CLIENTES
-- =============================================

-- Tabla de clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    hash_contrasena VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    fecha_nacimiento DATE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_acceso TIMESTAMP,
    esta_activo BOOLEAN DEFAULT TRUE
);

-- Tabla de direcciones
CREATE TABLE direcciones (
    id_direccion INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    tipo_direccion ENUM('facturacion', 'envio', 'ambos') NOT NULL,
    direccion_calle VARCHAR(255) NOT NULL,
    apartamento VARCHAR(50),
    id_ciudad INT NOT NULL,
    codigo_postal VARCHAR(20),
    es_predeterminada BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad)
);

-- =============================================
-- TABLAS RELACIONADAS CON PRODUCTOS
-- =============================================

-- Tabla de productos
CREATE TABLE productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre_producto VARCHAR(255) NOT NULL,
    sku VARCHAR(100) NOT NULL UNIQUE,
    id_categoria INT NOT NULL,
    id_marca INT,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    porcentaje_descuento DECIMAL(5, 2) DEFAULT 0,
    cantidad_stock INT NOT NULL DEFAULT 0,
    peso_kg DECIMAL(8, 2),
    esta_activo BOOLEAN DEFAULT TRUE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_marca) REFERENCES marcas(id_marca)
);

-- Tabla de imágenes de productos
CREATE TABLE imagenes_producto (
    id_imagen INT PRIMARY KEY AUTO_INCREMENT,
    id_producto INT NOT NULL,
    url_imagen VARCHAR(500) NOT NULL,
    es_principal BOOLEAN DEFAULT FALSE,
    orden_visualizacion INT DEFAULT 0,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE
);

-- Tabla de reseñas de productos
CREATE TABLE resenas_producto (
    id_resena INT PRIMARY KEY AUTO_INCREMENT,
    id_producto INT NOT NULL,
    id_cliente INT NOT NULL,
    valoracion INT NOT NULL CHECK (valoracion BETWEEN 1 AND 5),
    titulo_resena VARCHAR(255),
    texto_resena TEXT,
    fecha_resena TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    es_compra_verificada BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE
);

-- =============================================
-- TABLAS DE CARRITO DE COMPRAS
-- =============================================

-- Tabla de artículos del carrito
CREATE TABLE articulos_carrito (
    id_articulo_carrito INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE,
    UNIQUE KEY cliente_producto_unico (id_cliente, id_producto)
);

-- =============================================
-- TABLAS RELACIONADAS CON PEDIDOS
-- =============================================

-- Tabla de pedidos
CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    numero_pedido VARCHAR(50) NOT NULL UNIQUE,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_estado INT NOT NULL,
    id_estado_pago INT NOT NULL,
    id_metodo_pago INT NOT NULL,
    id_metodo_envio INT NOT NULL,
    id_direccion_envio INT NOT NULL,
    id_direccion_facturacion INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    monto_impuestos DECIMAL(10, 2) NOT NULL,
    coste_envio DECIMAL(10, 2) NOT NULL,
    monto_descuento DECIMAL(10, 2) DEFAULT 0,
    monto_total DECIMAL(10, 2) NOT NULL,
    notas TEXT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_estado) REFERENCES estados_pedido(id_estado),
    FOREIGN KEY (id_estado_pago) REFERENCES estados_pago(id_estado_pago),
    FOREIGN KEY (id_metodo_pago) REFERENCES metodos_pago(id_metodo_pago),
    FOREIGN KEY (id_metodo_envio) REFERENCES metodos_envio(id_metodo_envio),
    FOREIGN KEY (id_direccion_envio) REFERENCES direcciones(id_direccion),
    FOREIGN KEY (id_direccion_facturacion) REFERENCES direcciones(id_direccion)
);

-- Tabla de artículos del pedido
CREATE TABLE articulos_pedido (
    id_articulo_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    monto_descuento DECIMAL(10, 2) DEFAULT 0,
    precio_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- =============================================
-- INSERTAR DATOS DE EJEMPLO
-- =============================================

-- Insertar Países
INSERT INTO paises (nombre_pais, codigo_pais, prefijo_telefono) VALUES
('España', 'ES', '+34'),
('Estados Unidos', 'US', '+1'),
('Reino Unido', 'UK', '+44'),
('Alemania', 'DE', '+49'),
('Francia', 'FR', '+33');

-- Insertar Ciudades
INSERT INTO ciudades (nombre_ciudad, id_pais, codigo_postal) VALUES
('Madrid', 1, '28001'),
('Barcelona', 1, '08001'),
('Nueva York', 2, '10001'),
('Los Ángeles', 2, '90001'),
('Londres', 3, 'SW1A'),
('Berlín', 4, '10115'),
('París', 5, '75001');

-- Insertar Estados de Pedido
INSERT INTO estados_pedido (nombre_estado, descripcion_estado) VALUES
('Pendiente', 'El pedido ha sido realizado pero aún no procesado'),
('En Proceso', 'El pedido se está preparando'),
('Enviado', 'El pedido ha sido enviado'),
('Entregado', 'El pedido ha sido entregado'),
('Cancelado', 'El pedido ha sido cancelado'),
('Reembolsado', 'El pedido ha sido reembolsado');

-- Insertar Estados de Pago
INSERT INTO estados_pago (nombre_estado) VALUES
('Pendiente'),
('Completado'),
('Fallido'),
('Reembolsado');

-- Insertar Métodos de Envío
INSERT INTO metodos_envio (nombre_metodo, coste_base, dias_estimados, descripcion) VALUES
('Envío Estándar', 5.99, 7, 'Entrega regular en 5-7 días laborables'),
('Envío Exprés', 14.99, 3, 'Entrega rápida en 2-3 días laborables'),
('Envío Urgente', 29.99, 1, 'Entrega al día siguiente'),
('Envío Gratuito', 0.00, 10, 'Entrega estándar gratuita para pedidos superiores a 50€');

-- Insertar Métodos de Pago
INSERT INTO metodos_pago (nombre_metodo, esta_activo) VALUES
('Tarjeta de Crédito', TRUE),
('Tarjeta de Débito', TRUE),
('PayPal', TRUE),
('Apple Pay', TRUE),
('Google Pay', TRUE),
('Transferencia Bancaria', TRUE);

-- Insertar Marcas
INSERT INTO marcas (nombre_marca, descripcion_marca, url_sitio_web) VALUES
('TechMaster', 'Fabricante líder de electrónica', 'https://techmaster.example.com'),
('StyleWear', 'Marca de moda y ropa', 'https://stylewear.example.com'),
('HomeComfort', 'Productos para el hogar', 'https://homecomfort.example.com'),
('SportPro', 'Equipamiento deportivo y fitness', 'https://sportpro.example.com'),
('BeautyGlow', 'Belleza y cosmética', 'https://beautyglow.example.com');

-- Insertar Categorías
INSERT INTO categorias (nombre_categoria, id_categoria_padre, descripcion_categoria) VALUES
('Electrónica', NULL, 'Dispositivos electrónicos y accesorios'),
('Ropa', NULL, 'Ropa y artículos de moda'),
('Hogar y Jardín', NULL, 'Mejoras para el hogar y suministros de jardín'),
('Deportes y Aire Libre', NULL, 'Equipamiento deportivo y artículos de exterior'),
('Belleza y Salud', NULL, 'Productos de belleza y artículos de salud'),
('Smartphones', 1, 'Teléfonos móviles y accesorios'),
('Portátiles', 1, 'Ordenadores portátiles'),
('Ropa de Hombre', 2, 'Ropa para hombres'),
('Ropa de Mujer', 2, 'Ropa para mujeres'),
('Muebles', 3, 'Muebles para el hogar');

-- Insertar Clientes
INSERT INTO clientes (email, hash_contrasena, nombre, apellido, telefono, fecha_nacimiento) VALUES
('juan.perez@email.com', 'hash123abc', 'Juan', 'Pérez', '+34600123456', '1985-03-15'),
('maria.garcia@email.com', 'hash456def', 'María', 'García', '+34600234567', '1990-07-22'),
('james.smith@email.com', 'hash789ghi', 'James', 'Smith', '+1555123456', '1988-11-30'),
('sophie.martin@email.com', 'hash012jkl', 'Sophie', 'Martin', '+33612345678', '1992-05-18'),
('hans.mueller@email.com', 'hash345mno', 'Hans', 'Müller', '+49151234567', '1987-09-25');

-- Insertar Direcciones
INSERT INTO direcciones (id_cliente, tipo_direccion, direccion_calle, apartamento, id_ciudad, codigo_postal, es_predeterminada) VALUES
(1, 'ambos', 'Calle Gran Vía 123', '3A', 1, '28013', TRUE),
(2, 'envio', 'Paseo de Gracia 456', NULL, 2, '08007', TRUE),
(2, 'facturacion', 'Rambla Catalunya 789', '2B', 2, '08008', FALSE),
(3, 'ambos', '5th Avenue 789', 'Apt 12C', 3, '10022', TRUE),
(4, 'ambos', 'Champs-Élysées 101', NULL, 7, '75008', TRUE),
(5, 'ambos', 'Unter den Linden 55', NULL, 6, '10117', TRUE);

-- Insertar Productos
INSERT INTO productos (nombre_producto, sku, id_categoria, id_marca, descripcion, precio, porcentaje_descuento, cantidad_stock, peso_kg) VALUES
('Smartphone TechMaster X1', 'TM-SP-X1-001', 6, 1, 'Último smartphone con 128GB de almacenamiento y conectividad 5G', 699.99, 10, 50, 0.18),
('Portátil TechMaster Pro 15', 'TM-LP-PRO15-001', 7, 1, 'Portátil de 15 pulgadas con procesador Intel i7 y 16GB RAM', 1299.99, 15, 25, 2.1),
('Camiseta de Algodón para Hombre StyleWear', 'SW-TS-MCT-BLU-M', 8, 2, 'Cómoda camiseta de algodón en azul - Talla M', 29.99, 0, 100, 0.2),
('Vestido de Verano para Mujer StyleWear', 'SW-DR-WSD-RED-M', 9, 2, 'Elegante vestido de verano en rojo - Talla M', 79.99, 20, 45, 0.3),
('Silla de Oficina HomeComfort', 'HC-CH-OFF-BLK', 10, 3, 'Silla de oficina ergonómica con soporte lumbar', 249.99, 0, 30, 15.5),
('Zapatillas para Correr SportPro', 'SP-SH-RUN-BLK-42', 4, 4, 'Zapatillas profesionales para correr - Talla 42', 119.99, 25, 60, 0.8),
('Crema Facial BeautyGlow', 'BG-FC-HYD-50ML', 5, 5, 'Crema facial hidratante 50ml', 49.99, 0, 150, 0.1),
('Auriculares Inalámbricos TechMaster', 'TM-EB-WRL-001', 6, 1, 'Auriculares inalámbricos con cancelación de ruido y estuche de carga', 149.99, 5, 80, 0.05);

-- Insertar Imágenes de Productos
INSERT INTO imagenes_producto (id_producto, url_imagen, es_principal, orden_visualizacion) VALUES
(1, 'https://cdn.example.com/productos/smartphone-x1-frontal.jpg', TRUE, 1),
(1, 'https://cdn.example.com/productos/smartphone-x1-trasera.jpg', FALSE, 2),
(2, 'https://cdn.example.com/productos/portatil-pro15-principal.jpg', TRUE, 1),
(3, 'https://cdn.example.com/productos/camiseta-azul-frontal.jpg', TRUE, 1),
(4, 'https://cdn.example.com/productos/vestido-rojo-frontal.jpg', TRUE, 1),
(5, 'https://cdn.example.com/productos/silla-oficina-principal.jpg', TRUE, 1),
(6, 'https://cdn.example.com/productos/zapatillas-correr-principal.jpg', TRUE, 1),
(7, 'https://cdn.example.com/productos/crema-facial-principal.jpg', TRUE, 1),
(8, 'https://cdn.example.com/productos/auriculares-principal.jpg', TRUE, 1);

-- Insertar Reseñas de Productos
INSERT INTO resenas_producto (id_producto, id_cliente, valoracion, titulo_resena, texto_resena, es_compra_verificada) VALUES
(1, 1, 5, '¡Teléfono excelente!', 'El mejor smartphone que he tenido. Rápido, confiable y con una gran calidad de cámara.', TRUE),
(1, 3, 4, 'Bueno pero caro', 'Muy buen teléfono en general, pero un poco caro. La batería podría durar más.', TRUE),
(2, 2, 5, 'Perfecto para trabajar', 'Este portátil maneja todas mis tareas de trabajo sin esfuerzo. ¡Muy recomendable!', TRUE),
(3, 4, 5, 'Muy cómoda', 'Camiseta de gran calidad, se ajusta perfectamente y la tela es suave.', TRUE),
(6, 5, 4, 'Excelentes zapatillas para correr', 'Cómodas y ligeras. Perfectas para mis carreras diarias.', TRUE);

-- Insertar Artículos del Carrito
INSERT INTO articulos_carrito (id_cliente, id_producto, cantidad) VALUES
(1, 8, 1),
(1, 7, 2),
(3, 3, 3),
(5, 6, 1);

-- Insertar Pedidos
INSERT INTO pedidos (id_cliente, numero_pedido, id_estado, id_estado_pago, id_metodo_pago, id_metodo_envio, 
                   id_direccion_envio, id_direccion_facturacion, subtotal, monto_impuestos, coste_envio, monto_descuento, monto_total) VALUES
(1, 'PED-2024-001', 4, 2, 1, 2, 1, 1, 629.99, 132.30, 14.99, 70.00, 707.28),
(2, 'PED-2024-002', 3, 2, 3, 1, 2, 3, 63.99, 13.44, 5.99, 16.00, 67.42),
(3, 'PED-2024-003', 2, 2, 2, 3, 4, 4, 89.97, 18.89, 29.99, 0, 138.85),
(4, 'PED-2024-004', 4, 2, 4, 1, 5, 5, 1299.99, 273.00, 0.00, 194.99, 1378.00),
(5, 'PED-2024-005', 1, 1, 1, 1, 6, 6, 89.99, 18.90, 5.99, 30.00, 84.88);

-- Insertar Artículos del Pedido
INSERT INTO articulos_pedido (id_pedido, id_producto, cantidad, precio_unitario, monto_descuento, precio_total) VALUES
(1, 1, 1, 699.99, 70.00, 629.99),
(2, 4, 1, 79.99, 16.00, 63.99),
(3, 3, 3, 29.99, 0, 89.97),
(4, 2, 1, 1299.99, 194.99, 1105.00),
(5, 6, 1, 119.99, 30.00, 89.99);

-- =============================================
-- CONSULTAS ÚTILES
-- =============================================

-- Mostrar todos los productos con sus categorías y marcas
SELECT 
    p.nombre_producto,
    p.sku,
    c.nombre_categoria,
    m.nombre_marca,
    p.precio,
    p.cantidad_stock
FROM productos p
LEFT JOIN categorias c ON p.id_categoria = c.id_categoria
LEFT JOIN marcas m ON p.id_marca = m.id_marca;

-- Mostrar pedidos de clientes con detalles
SELECT 
    pe.numero_pedido,
    CONCAT(cl.nombre, ' ', cl.apellido) AS nombre_cliente,
    pe.fecha_pedido,
    ep.nombre_estado,
    pe.monto_total
FROM pedidos pe
JOIN clientes cl ON pe.id_cliente = cl.id_cliente
JOIN estados_pedido ep ON pe.id_estado = ep.id_estado
ORDER BY pe.fecha_pedido DESC;
```

<a id="informes-y-listados-de-la-aplicacion"></a>
## Informes y listados de la aplicación

En este capítulo, nos adentramos en la organización y consulta de la información dentro de sistemas ERP-CRM, un tema fundamental para el funcionamiento eficiente de estos sistemas. Comenzamos por definir los campos que son esenciales para una base de datos organizada y accesible.

La consulta de acceso a datos es otro aspecto crucial que permite extraer información relevante en forma rápida y precisa. A través de interfaces de entrada de datos y procesos, se pueden realizar consultas complejas que abarcan múltiples tablas y campos, proporcionando una visión integral del estado actual de la empresa.

Los informes y listados son herramientas poderosas para presentar los resultados de las consultas de manera visual y fácilmente interpretable. Se pueden crear formularios personalizados que reflejen las necesidades específicas de cada área de la empresa, desde ventas hasta recursos humanos.

La gestión de pedidos es otro ejemplo práctico de cómo se organiza y consulta información en sistemas ERP-CRM. Los procesos automatizados permiten un seguimiento preciso del flujo de pedidos, desde su creación hasta su entrega final, facilitando la toma de decisiones basada en datos.

Los gráficos son una forma efectiva de representar datos de manera visual, ayudando a identificar tendencias y patrones que pueden no ser evidentes en tablas simples. Herramientas de monitorización y evaluación del rendimiento permiten seguir el desempeño del sistema y realizar ajustes necesarios.

La incidencia es otro aspecto importante de la consulta y organización de información. Identificar y resolver problemas rápidamente es clave para mantener el funcionamiento óptimo de los sistemas ERP-CRM, lo que implica un proceso eficiente de diagnóstico y solución.

Finalmente, la integración con otros sistemas de gestión es una característica fundamental de los sistemas ERP-CRM modernos. Permite la extracción de datos en almacenes de datos centralizados, facilitando la realización de análisis complejos y la toma de decisiones estratégicas basadas en información unificada.

A lo largo de este capítulo, hemos explorado cómo se organiza y consulta la información dentro de sistemas ERP-CRM, desde la definición de campos hasta la creación de informes personalizados. Cada uno de estos elementos contribuye al funcionamiento eficiente y efectivo de estos sistemas, permitiendo a las empresas tomar decisiones basadas en datos precisos y actualizados.

<a id="gestion-de-pedidos"></a>
## Gestión de pedidos

En el mundo empresarial, la gestión eficiente de los pedidos es un componente fundamental para mantener la fluidez operativa y satisfacer las necesidades del cliente. Este proceso implica una serie de etapas que van desde la recepción del pedido hasta su entrega final. En esta subunidad, exploraremos cómo organizar y gestionar estos pedidos de manera efectiva.

La organización de los pedidos comienza con la definición de campos relevantes. Estos campos pueden incluir detalles como el número de pedido, fecha, cliente, productos solicitados, cantidades, precios unitarios y totales. La precisión en la definición de estos campos es crucial para facilitar la consulta y análisis de los datos.

Una vez que se han definido los campos, los pedidos deben ser consultados de manera eficiente. Esto puede implicar el uso de interfaces de entrada de datos y procesos específicos diseñados para facilitar la búsqueda y recuperación de información. Las herramientas de consulta permiten filtrar y ordenar los pedidos según diversos criterios, como cliente, fecha o estado del pedido.

Los formularios personalizados son otro elemento importante en la gestión de pedidos. Estos formularios pueden adaptarse a las necesidades específicas de la empresa y facilitan el ingreso y modificación de datos. Por ejemplo, un formulario para pedidos internos puede incluir campos adicionales como departamento solicitante o urgencia.

Los informes y listados son herramientas valiosas para analizar los datos de los pedidos. Estos informes pueden mostrar información detallada sobre el historial de ventas, tendencias de pedido y productos más populares. La generación de gráficos basados en estos datos puede proporcionar una visión visual clara de la situación empresarial.

La gestión de pedidos también implica procesos de extracción de datos. Esto puede implicar la creación de consultas SQL para obtener información específica de los sistemas de ERP-CRM y almacenes de datos. La eficiencia en esta etapa es crucial para mantener el flujo operativo sin interrupciones.

La inteligencia de negocio (Business Intelligence) juega un papel importante en la gestión de pedidos. Herramientas de BI permiten analizar los datos de los pedidos y generar informes detallados que proporcionan insights valiosos sobre las tendencias y comportamientos del cliente. Esta información puede ser utilizada para mejorar los procesos de pedido y optimizar la estrategia comercial.

En conclusión, la gestión de pedidos es un proceso complejo pero crucial en el mundo empresarial. La organización adecuada de los datos, la eficiencia en las consultas y la creación de formularios personalizados son fundamentales para facilitar este proceso. Los informes detallados y la inteligencia de negocio proporcionan herramientas valiosas para analizar y mejorar la gestión de pedidos, contribuyendo así a la satisfacción del cliente y el éxito empresarial.

<a id="graficos"></a>
## Gráficos

En este capítulo, nos adentramos en la organización y consulta de la información dentro de los sistemas ERP-CRM, centrándonos específicamente en el uso de gráficos para visualizar datos. Los gráficos son una herramienta poderosa que permite representar información compleja de manera clara y accesible, facilitando la toma de decisiones basada en datos.

La creación de gráficos en sistemas ERP-CRM implica la selección adecuada del tipo de gráfico que mejor se adapta a los datos a visualizar. Por ejemplo, si estamos interesados en comparar cantidades o porcentajes entre diferentes categorías, un gráfico de barras o de sectores puede ser ideal. En cambio, para mostrar tendencias a lo largo del tiempo, un gráfico de líneas sería más apropiado.

El proceso de creación de gráficos generalmente implica la definición de los campos que se utilizarán en el eje X y Y, así como la elección de las etiquetas y leyendas. Además, es importante considerar la escala del eje para evitar distorsiones en la interpretación de los datos.

Una vez creados los gráficos, su visualización dentro del sistema ERP-CRM debe ser intuitiva y fácil de entender. Esto implica el uso de colores contrastantes, etiquetas claras y leyendas precisas. Además, es recomendable proporcionar opciones para personalizar la apariencia del gráfico, como cambiar los colores o ajustar las etiquetas.

La consulta de información mediante gráficos en ERP-CRM no se limita a la visualización estática. Muchos sistemas modernos ofrecen funcionalidades interactivas que permiten explorar los datos de manera dinámica. Por ejemplo, al hacer clic en una barra de un gráfico de barras, puede aparecer una ventana emergente con detalles adicionales sobre esa categoría.

Además de la visualización estática y dinámica, los sistemas ERP-CRM también ofrecen herramientas para generar informes a partir de gráficos. Esto permite exportar los datos en formato PDF o Excel, facilitando su análisis posterior en otras aplicaciones.

La organización y consulta de la información mediante gráficos es una práctica fundamental en el análisis de datos empresariales. Permite identificar tendencias, patrones y anomalías que pueden no ser evidentes al examinar los datos brutos. Además, facilita la comunicación de resultados a partes interesadas, ya que los gráficos son intuitivos y accesibles para personas con diferentes niveles de conocimiento técnico.

En conclusión, el uso de gráficos en sistemas ERP-CRM es una herramienta valiosa para organizar y consultar información empresarial. Al seleccionar adecuadamente el tipo de gráfico, definir los campos y etiquetas correctamente, y proporcionar opciones interactivas y de exportación, se pueden crear visualizaciones que faciliten la toma de decisiones basada en datos y mejorar la comunicación dentro del equipo.

<a id="herramientas-de-monitorizacion-y-de-evaluacion-del-rendimiento"></a>
## Herramientas de monitorización y de evaluación del rendimiento

En la subunidad "Herramientas de monitorización y evaluación del rendimiento", nos centramos en las técnicas y herramientas utilizadas para mantener un control constante sobre el funcionamiento eficiente de los sistemas ERP-CRM. La monitorización es una práctica fundamental que permite identificar problemas temprano, optimizar recursos y asegurar la continuidad operativa.

Las herramientas de evaluación del rendimiento son instrumentos valiosos que nos permiten medir y analizar el desempeño de los sistemas ERP-CRM. Estas herramientas pueden variar desde simples indicadores de rendimiento (KPIs) hasta sistemas complejos de análisis avanzados. Cada una de estas herramientas juega un papel crucial en la toma de decisiones estratégicas y en la mejora continua del sistema.

Una de las principales ventajas de utilizar herramientas de monitorización y evaluación es que proporcionan visibilidad en tiempo real sobre el estado del sistema, lo que facilita la identificación rápida de anomalías. Por ejemplo, si un indicador de rendimiento muestra una disminución significativa en los tiempos de respuesta, esto puede ser una señal de problemas técnicos o de carga excesiva.

Además de las herramientas internas proporcionadas por los sistemas ERP-CRM, existen soluciones de terceros que pueden integrarse fácilmente. Estas soluciones ofrecen un análisis más profundo y detallado del rendimiento, permitiendo la identificación de tendencias y patrones que podrían no ser evidentes con las herramientas básicas.

La evaluación del rendimiento es un proceso continuo que requiere una comprensión profunda del sistema y su entorno. Es importante no solo monitorizar los indicadores de rendimiento, sino también analizar la información recopilada para entender cómo afecta a la operación general del negocio. Esto puede implicar el desarrollo de procesos de análisis personalizados o la integración con sistemas de inteligencia artificial para automatizar y mejorar la toma de decisiones.

La monitorización y evaluación del rendimiento también son cruciales para la optimización de recursos. Al identificar áreas de bajo rendimiento, se pueden implementar soluciones que mejoren la eficiencia y reduzcan los costos operativos. Esto puede incluir el ajuste de parámetros del sistema, la adquisición de nuevos hardware o incluso la reorganización de procesos de negocio.

En conclusión, las herramientas de monitorización y evaluación del rendimiento son elementos esenciales en la gestión eficiente de los sistemas ERP-CRM. Al utilizar estas herramientas de manera efectiva, se puede asegurar que el sistema esté siempre optimizado para satisfacer las necesidades del negocio, lo que a su vez contribuye al crecimiento y éxito empresarial.

<a id="incidencias-identificacion-y-resolucion"></a>
## Incidencias identificación y resolución

En la subunidad "Organización y consulta de la información", nos centramos específicamente en el manejo eficiente de incidencias dentro del sistema ERP-CRM. La identificación precisa de las incidencias es crucial para mantener un funcionamiento óptimo del sistema, ya que permite una rápida respuesta a problemas y mejoras continuas.

Para organizar adecuadamente las incidencias, se requiere la definición clara de campos específicos. Estos campos pueden incluir detalles como el tipo de incidencia, su estado actual (pendiente, en proceso, resuelta), fecha de creación y modificación, así como información sobre el usuario que reportó la incidencia. La organización eficiente de estos datos facilita la búsqueda y análisis futuros.

La consulta de incidencias es otro aspecto fundamental de esta sección. Se deben desarrollar herramientas y interfaces que permitan a los usuarios buscar rápidamente las incidencias según diversos criterios, como el estado actual, el tipo o la fecha de creación. Estas consultas pueden ser realizadas tanto por usuarios finales como por técnicos de soporte, lo que asegura una comunicación fluida y eficiente.

Además de la organización y consulta, es esencial implementar procesos claros para la identificación y resolución de incidencias. Esto implica establecer protocolos específicos para cada tipo de problema, desde fallos en el sistema hasta problemas con los datos. La identificación precisa de las causas raíz de las incidencias permite una resolución más eficiente y preventiva.

La resolución de incidencias debe ser un proceso sistemático que incluya la asignación a técnicos competentes, la documentación detallada del problema y su solución, así como el seguimiento para asegurar que el problema ha sido completamente resuelto. La implementación de herramientas de seguimiento y control de calidad es crucial para mantener un alto nivel de satisfacción con los usuarios.

Es importante también considerar la retroalimentación post-resolución. Los usuarios deben ser informados sobre el estado final de su incidencia y, si es necesario, proporcionado soporte adicional. Esta comunicación abierta y transparente mejora la confianza en el sistema y reduce el riesgo de problemas recurrentes.

En conclusión, la organización y consulta de incidencias son pilares fundamentales para mantener un ERP-CRM funcionando eficientemente. La implementación de procesos claros y herramientas adecuadas facilita la identificación rápida de problemas y su resolución, lo que a su vez mejora la satisfacción del usuario y la eficiencia operativa de la empresa.

<a id="procesos-de-extraccion-de-datos-en-sistemas-de-erp-crm-y-almacenes-de-datos"></a>
## Procesos de extracción de datos en sistemas de ERP-CRM y almacenes de datos

En los sistemas de gestión empresariales (ERP-CRM), la organización y consulta de la información son fundamentales para el funcionamiento eficiente del negocio. Uno de los aspectos cruciales es la capacidad de extraer datos de manera precisa y eficaz, tanto desde los sistemas ERP como desde almacenes de datos externos.

La extracción de datos en estos contextos implica identificar las necesidades específicas del negocio y diseñar consultas que recuperen solo la información relevante. En un sistema ERP, esto puede implicar el uso de consultas SQL para seleccionar campos específicos de tablas o vistas predefinidas. Por ejemplo, si se necesita obtener una lista de todos los clientes que han realizado compras en el último mes, se podría escribir una consulta como la siguiente:

```sql
SELECT cliente_id, nombre, apellido, fecha_ultima_compra 
FROM clientes 
WHERE fecha_ultima_compra >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH);
```

Esta consulta selecciona los identificadores de cliente, nombres y apellidos, junto con la fecha de la última compra, para aquellos clientes que hayan realizado una compra en el último mes. La cláusula `WHERE` filtra los resultados basándose en la condición especificada.

En almacenes de datos externos, como bases de datos NoSQL o sistemas de análisis big data, la extracción de datos puede implicar consultas más complejas y específicas a las características del sistema. Por ejemplo, en una base de datos documental MongoDB, se podría escribir una consulta para obtener todos los registros de clientes que han realizado compras por un monto mayor a 1000 euros:

```javascript
db.clientes.find({ "compras.monto": { $gt: 1000 } })
```

Esta consulta busca en la colección `clientes` aquellos documentos donde el campo `compras.monto` tenga un valor mayor que 1000. La sintaxis de MongoDB permite expresar consultas muy específicas y poderosas.

La extracción de datos es una tarea recurrente en sistemas ERP-CRM, ya que los informes y listados generados a partir de estos datos son cruciales para la toma de decisiones estratégicas y operativas. Además, el procesamiento de estos datos puede implicar la creación de nuevas tablas o vistas personalizadas, lo que permite obtener información en formatos más útiles y accesibles.

Es importante destacar que la extracción de datos debe ser segura y respetuosa con los derechos de privacidad de los clientes. Por lo tanto, es crucial implementar medidas de seguridad adecuadas, como el uso de consultas parametrizadas para prevenir inyecciones SQL, y garantizar que solo los usuarios autorizados puedan acceder a la información sensible.

En resumen, la extracción de datos en sistemas ERP-CRM y almacenes de datos es una tarea compleja pero fundamental. Requiere un conocimiento profundo del sistema y habilidades en consultas específicas para recuperar la información necesaria. Además, es crucial considerar aspectos como la seguridad y el rendimiento para asegurar que los procesos de extracción sean eficientes y confiables.

<a id="inteligencia-de-negocio-business-intelligence"></a>
## Inteligencia de negocio (Business Intelligence)

La inteligencia de negocio (Business Intelligence, BI) es una disciplina que se ocupa del análisis, la recopilación, el procesamiento y la presentación de datos empresariales con el fin de mejorar las decisiones estratégicas. En este contexto, los sistemas ERP-CRM son fundamentales para la gestión de información empresarial, proporcionando un conjunto completo de herramientas para organizar y consultar datos relevantes.

La organización de la información en sistemas ERP-CRM implica la definición de campos que reflejen las necesidades específicas de la empresa. Estos campos pueden variar desde los datos financieros hasta la información sobre clientes y proveedores, pasando por el seguimiento de proyectos y tareas. La importancia de esta organización radica en su capacidad para facilitar la consulta y análisis de los datos.

Las consultas de acceso a datos son una parte esencial del BI. Estas permiten extraer información específica basada en criterios definidos, como fechas, ubicaciones o tipos de productos. Los sistemas ERP-CRM ofrecen herramientas avanzadas para crear consultas complejas que pueden incluir múltiples tablas y condiciones, proporcionando una visión detallada del estado actual de la empresa.

Las interfaces de entrada de datos y de procesos son componentes cruciales en el flujo de trabajo empresarial. Estas interfaces permiten a los usuarios interactuar con el sistema, ingresando o modificando información según sea necesario. La eficiencia de estas interfaces puede influir significativamente en la productividad del personal.

Los informes y listados son una forma visual de presentar la información recopilada. Son herramientas poderosas para comunicar tendencias, patrones y insights clave a los stakeholders de la empresa. Los sistemas ERP-CRM ofrecen diversas opciones para crear informes personalizados que pueden adaptarse a las necesidades específicas de cada usuario.

El gestión de pedidos es otro aspecto importante del BI en sistemas ERP-CRM. Permite rastrear el flujo de pedidos desde su creación hasta su entrega, proporcionando información detallada sobre la satisfacción del cliente y los tiempos de respuesta. Esta información puede ser utilizada para mejorar procesos y optimizar recursos.

Los gráficos son una forma efectiva de representar datos complejos de manera visual. En el BI, los gráficos pueden mostrar tendencias a lo largo del tiempo, comparaciones entre diferentes períodos o segmentos de la empresa. La capacidad de crear gráficos interactivos puede facilitar la exploración y análisis de los datos.

Las herramientas de monitorización y evaluación del rendimiento son fundamentales para el BI en sistemas ERP-CRM. Permiten a las empresas rastrear y analizar su desempeño en diferentes áreas, como ventas, producción o servicio al cliente. Esta información puede ser utilizada para identificar oportunidades de mejora y tomar decisiones estratégicas.

Las incidencias identificación y resolución son otro aspecto del BI en sistemas ERP-CRM. Permite rastrear problemas que surgen durante el proceso de negocio y analizar sus causas. La capacidad de generar informes sobre las incidencias puede ayudar a prevenir su repetición y mejorar la eficiencia operativa.

La extracción de datos en sistemas ERP-CRM y almacenes de datos es un paso crucial para el BI. Permite combinar información de diferentes fuentes, creando una visión integral del estado empresarial. La capacidad de realizar consultas complejas sobre estos almacenes de datos puede facilitar la identificación de tendencias y patrones que pueden no ser evidentes en los sistemas individuales.

La inteligencia de negocio (BI) en sistemas ERP-CRM es un proceso continuo que implica la organización, consulta, presentación y análisis de datos empresariales. A través de estas herramientas, las empresas pueden tomar decisiones informadas basadas en información precisa y relevante, lo que les permite mejorar su eficiencia operativa y competitividad en el mercado.


<a id="implantacion-de-sistemas-erp-crm-en-una-empresa"></a>
# Implantación de sistemas ERP-CRM en una empresa

<a id="tipos-de-empresa-necesidades-de-la-empresa"></a>
## Tipos de empresa. Necesidades de la empresa

En la implantación de sistemas ERP-CRM en una empresa, es crucial entender primero el tipo de organización que se está abordando. Cada tipo de empresa tiene necesidades específicas que un sistema ERP-CRM debe satisfacer para optimizar su operación eficiente. Por ejemplo, las empresas manufatureras pueden requerir sistemas que gestionen la producción y la cadena de suministro de manera integral, mientras que las empresas de servicios financieros necesitarán herramientas avanzadas para el seguimiento de clientes y transacciones financieras.

La selección del tipo de sistema ERP-CRM debe basarse en factores como el tamaño de la empresa, su industria, los procesos existentes y los objetivos estratégicos a alcanzar. Por ejemplo, una pequeña empresa puede optar por un sistema ERP-CRM que sea más simple y económico, mientras que una corporación global necesitará un sistema robusto y escalable capaz de manejar grandes volúmenes de datos y procesos complejos.

Además de la naturaleza organizacional, las necesidades específicas de cada empresa también juegan un papel crucial en la elección del sistema ERP-CRM. Por ejemplo, si una empresa se centra en el servicio al cliente, puede priorizar características como la gestión avanzada de pedidos y facturas, así como herramientas para el seguimiento del servicio postventa. En cambio, si la empresa opera en un sector con alto nivel de competitividad, podría necesitar sistemas que ofrezcan análisis predictivos y decisiones basadas en datos.

La implantación de un sistema ERP-CRM no es solo una cuestión técnica; también implica cambios organizacionales significativos. Es necesario involucrar a todos los stakeholders, desde el departamento de TI hasta las áreas operativas y financieras, para asegurar que la implementación sea exitosa. Esto incluye la formación del personal en el uso del nuevo sistema, la planificación de la transición gradual hacia el nuevo entorno tecnológico y la definición de procesos de trabajo optimizados.

Además, es fundamental considerar las capacidades existentes de la empresa al momento de implantar un sistema ERP-CRM. Si la empresa ya cuenta con sistemas legacy o herramientas específicas para ciertos procesos, puede ser necesario integrar estos sistemas con el nuevo ERP-CRM para evitar una migración total y minimizar el impacto en los operaciones diarias.

La selección y configuración adecuados de un sistema ERP-CRM pueden llevar a mejoras significativas en la eficiencia operativa, la toma de decisiones basada en datos y la satisfacción del cliente. Sin embargo, es importante recordar que el éxito de una implantación no depende solo del sistema elegido, sino también del enfoque integral que se adopte, incluyendo la formación del personal, la planificación cuidadosa y la adaptación a las necesidades específicas de la empresa.

La selección del tipo de empresa y sus necesidades es un paso fundamental en el proceso de implantación de sistemas ERP-CRM. Al entender estas necesidades y adaptar el sistema al contexto organizacional, se puede maximizar la eficiencia operativa y alcanzar los objetivos estratégicos de la empresa.

<a id="seleccion-de-los-modulos-del-sistema-erp-crm"></a>
## Selección de los módulos del sistema ERP-CRM

La selección de los módulos del sistema ERP-CRM es un paso crucial en el proceso de implantación, ya que determinará la funcionalidad completa y adaptabilidad del software a las necesidades específicas de la empresa. En primer lugar, es fundamental identificar qué aspectos operativos y administrativos son cruciales para la organización. Esto puede incluir gestión financiera, recursos humanos, ventas, compras, inventario, entre otros.

Una vez identificados los sectores clave, se debe investigar en profundidad las capacidades de cada módulo del ERP-CRM que pueda cubrir estas áreas. Es importante examinar cómo cada módulo interactúa con los demás y cómo facilita la integración con sistemas existentes. Además, es relevante evaluar la facilidad de uso y personalización de los módulos para asegurar una adopción óptima por parte del personal.

Además de las funcionalidades técnicas, también se deben considerar factores como el soporte técnico disponible, la actualización regular del software y la compatibilidad con otros sistemas internos. Es crucial que el proveedor ofrezca un servicio sólido de asistencia y que los módulos estén diseñados para futuras necesidades de crecimiento empresarial.

Una vez seleccionados los módulos, es necesario realizar una planificación detallada del proceso de implementación. Esto incluye la definición de objetivos claros, el establecimiento de un cronograma y la asignación de recursos humanos adecuados. Es importante también preparar un plan de contingencia para abordar cualquier problema que pueda surgir durante el proceso.

Durante la fase de configuración, es esencial ajustar los módulos según las necesidades específicas de la empresa. Esto puede implicar la creación de formularios personalizados, la definición de procesos de trabajo y la configuración de parámetros de seguridad. Es crucial que esta etapa sea meticulosa para evitar problemas futuros.

Una vez completada la configuración inicial, es necesario realizar pruebas exhaustivas del sistema. Esto debe incluir pruebas funcionales para asegurar que todos los módulos trabajan correctamente juntos y pruebas de rendimiento para evaluar su capacidad para manejar el volumen de datos esperado. Es importante documentar todos los hallazgos durante este proceso para facilitar la corrección de problemas y la optimización del sistema.

Finalmente, es crucial realizar una formación adecuada para el personal que utilizará el ERP-CRM. Esto debe incluir no solo la enseñanza de cómo usar las funcionalidades básicas, sino también estrategias para maximizar su eficiencia y adaptarse a nuevas características en el futuro. Una buena formación puede ser la diferencia entre un sistema implementado con éxito y uno que resulte en frustración y deserción del personal.

La selección de los módulos del ERP-CRM es, por lo tanto, un proceso integral que requiere una combinación de conocimiento técnico, análisis de necesidades y planificación estratégica. Al seguir estos pasos y considerar cuidadosamente todas las implicaciones, se puede asegurar una implantación exitosa que mejore significativamente la eficiencia operativa y la toma de decisiones empresariales.

<a id="tablas-y-vistas-que-es-preciso-adaptar"></a>
## Tablas y vistas que es preciso adaptar

En la etapa de implantación de sistemas ERP-CRM en una empresa, es crucial adaptar las tablas y vistas existentes para integrarlos eficazmente con el nuevo sistema. Esta adaptación no solo asegura que los datos existentes no se pierdan, sino que también facilita la transición a un flujo de trabajo más optimizado.

La primera consideración al adaptar tablas es evaluar su estructura actual. Es importante identificar qué campos son relevantes para el ERP-CRM y cómo pueden ser integrados en las nuevas entidades del sistema. Por ejemplo, si el ERP-CRM requiere información sobre los clientes, se deben revisar las tablas de clientes actuales y determinar cuáles campos son necesarios para la gestión completa de estos registros.

Además de adaptar las tablas, también es necesario crear o modificar vistas que faciliten el acceso a la información. Las vistas permiten presentar los datos de manera más amigable y estructurada, ocultando detalles innecesarios y agrupando información relevante en una sola vista. Por ejemplo, si se desea un informe sobre las ventas por cliente, se puede crear una vista que combine información de la tabla de clientes con la tabla de ventas.

La adaptación de tablas y vistas no es solo una tarea técnica; también implica trabajar estrechamente con los departamentos de negocio para entender sus necesidades específicas. Es importante mantener un diálogo abierto con estos equipos para asegurar que las adaptaciones realizadas sean útiles y efectivas en el contexto operativo de la empresa.

Además, es crucial realizar pruebas exhaustivas antes de implementar cualquier cambio en las tablas y vistas. Esto incluye pruebas unitarias para verificar que los cambios no afecten la integridad de los datos existentes y pruebas funcionales para asegurar que el nuevo sistema funcione como se espera. Las pruebas deben abordar todos los aspectos del flujo de trabajo, desde la entrada de datos hasta la generación de informes.

Una vez completadas las pruebas, es momento de realizar la migración de los datos existentes a las nuevas tablas y vistas del ERP-CRM. Esta migración debe ser realizada con cuidado para evitar pérdidas de información o inconsistencias en los datos. Es posible que sea necesario desarrollar scripts personalizados para realizar esta tarea.

Después de la migración, es importante revisar el rendimiento del sistema y hacer ajustes si es necesario. Esto puede implicar optimizar consultas, mejorar la eficiencia de las operaciones de inserción y actualización o incluso reorganizar tablas para mejorar el acceso a los datos.

La adaptación de tablas y vistas es un proceso iterativo que requiere paciencia y atención al detalle. Es importante mantener una comunicación clara con todos los stakeholders involucrados en la implantación del ERP-CRM, desde los departamentos de negocio hasta los equipos de TI. La colaboración y el compromiso son fundamentales para asegurar un éxito en esta etapa crítica del proyecto.

En conclusión, adaptar las tablas y vistas es una tarea fundamental en la implantación de sistemas ERP-CRM. Requiere una comprensión profunda de la estructura actual de los datos, habilidades técnicas sólidas y una colaboración estrecha con los departamentos de negocio. A través de un proceso cuidadoso y exhaustivo, es posible integrar el nuevo sistema de manera efectiva, asegurando que todos los aspectos del flujo de trabajo empresarial sean optimizados y facilitados por la tecnología moderna.

<a id="consultas-necesarias-para-obtener-informacion"></a>
## Consultas necesarias para obtener información

En la fase de implantación de sistemas ERP-CRM en una empresa, es crucial identificar las consultas necesarias para obtener información relevante y eficiente. Estas consultas son el puente entre los datos almacenados en el sistema y la toma de decisiones estratégicas dentro del negocio.

Comenzamos por definir los campos que serán relevantes para nuestras consultas. Esto puede incluir detalles como clientes, productos, ventas, inventario y proveedores. Cada campo debe estar bien documentado y tener un propósito claro en el contexto empresarial.

A continuación, se procede a la creación de consultas SQL específicas para cada tipo de información necesaria. Por ejemplo, si estamos interesados en los clientes que han realizado compras en el último mes, la consulta podría ser algo así:

```sql
SELECT cliente_id, nombre, apellido, total_compras 
FROM ventas 
WHERE fecha >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH);
```

Esta consulta nos proporcionará una lista de clientes con sus respectivos nombres y totales de compras en el último mes. Es importante que estas consultas sean optimizadas para minimizar el tiempo de respuesta, lo cual puede implicar la creación de índices apropiados sobre los campos utilizados en las cláusulas WHERE.

Además de las consultas simples, también es necesario considerar consultas más complejas que involucren múltiples tablas. Por ejemplo, si queremos obtener información detallada sobre el inventario de productos junto con sus ventas y proveedores, podríamos utilizar una consulta JOIN:

```sql
SELECT p.producto_id, p.nombre, i.cantidad, v.total_ventas, pr.nombre_proveedor 
FROM productos p 
JOIN inventario i ON p.producto_id = i.producto_id 
JOIN ventas v ON p.producto_id = v.producto_id 
JOIN proveedores pr ON p.proveedor_id = pr.proveedor_id;
```

Esta consulta nos proporcionará una visión integral del estado actual del inventario, incluyendo información sobre las ventas y los proveedores asociados a cada producto.

Es importante también considerar la seguridad de las consultas. Asegurarse de que solo los usuarios autorizados puedan ejecutar ciertas consultas puede ser crucial para mantener la integridad de los datos. Esto puede implicar el uso de roles y privilegios específicos dentro del sistema ERP-CRM.

Además, es recomendable realizar pruebas exhaustivas sobre las consultas antes de su implementación en producción. Esto puede incluir pruebas unitarias individuales de cada consulta así como pruebas de integración para asegurarse de que todas las partes funcionan juntas sin conflictos.

La documentación de estas consultas también es fundamental. Debe incluir información sobre el propósito de la consulta, los campos utilizados y cualquier criterio de filtro aplicado. Esto facilitará el mantenimiento futuro del sistema y permitirá a otros miembros del equipo entender rápidamente qué hace cada consulta.

Finalmente, es importante monitorear el rendimiento de las consultas en producción. Si se encuentran problemas de rendimiento, puede ser necesario optimizarlas o incluso reescribirlas para mejorar su eficiencia.

En resumen, la identificación y creación de consultas necesarias para obtener información relevante es un paso crucial en la implantación de sistemas ERP-CRM. Al definir campos relevantes, crear consultas SQL específicas, considerar consultas complejas, asegurar la seguridad, probar exhaustivamente, documentar adecuadamente y monitorear el rendimiento, se puede garantizar que el sistema funcione eficientemente y proporciona información valiosa para la toma de decisiones empresariales.

<a id="creacion-de-formularios-personalizados"></a>
## Creación de formularios personalizados

La implantación de sistemas ERP-CRM en una empresa requiere un enfoque cuidadoso para asegurar que los formularios personalizados sean útiles, eficientes y alineados con las necesidades específicas del negocio. En esta subunidad, exploraremos el proceso detallado de creación de formularios personalizados dentro de un sistema ERP-CRM.

El primer paso es entender la estructura general del sistema ERP-CRM que se utilizará. Esto implica conocer los módulos disponibles y cómo interactúan entre sí. Los formularios son una parte integral de esta arquitectura, ya que permiten a los usuarios ingresar y gestionar datos de manera intuitiva.

Para crear formularios personalizados, es necesario identificar las áreas específicas del negocio donde se necesitan cambios o mejoras en la interfaz de usuario. Esto puede implicar la creación de nuevos formularios para procesos adicionales o la modificación de los existentes para mejorar su funcionalidad.

El proceso de creación de formularios personalizados comienza con el diseño visual. Se debe definir la disposición de los campos, las etiquetas y cualquier otro elemento gráfico que sea necesario para facilitar la entrada de datos. Es importante mantener un enfoque en la simplicidad y la claridad, evitando sobrecargar el formulario con demasiada información.

Una vez diseñado el layout visual, se pasa al desarrollo del formulario. Esto implica escribir código o utilizar herramientas gráficas para definir las propiedades de los campos, como su tipo de dato, restricciones y comportamientos específicos. Es crucial que estos detalles estén bien definidos para asegurar la integridad de los datos.

Durante el desarrollo, es importante probar el formulario en diferentes escenarios para identificar problemas o áreas de mejora. Esto puede implicar pruebas manuales o automatizadas para verificar que el formulario funcione correctamente y que no interfiera con otros procesos del sistema.

Una vez que el formulario ha sido probado y aprobado, se debe implementarlo en el entorno de producción. Es importante tener un plan detallado para la migración de los datos existentes y la configuración inicial del nuevo formulario. Esto puede implicar la creación de scripts o procedimientos específicos para facilitar el proceso.

La implantación final del formulario personalizado implica la formación de los usuarios finales sobre su uso. Es importante proporcionar documentación detallada y realizar sesiones de capacitación para asegurar que todos entiendan cómo utilizar el nuevo formulario eficazmente.

Durante todo el proceso, es crucial mantener un enfoque en la seguridad y la privacidad de los datos. Se debe implementar cualquier medida necesaria para proteger la información sensible y garantizar que solo los usuarios autorizados puedan acceder a ella.

La creación de formularios personalizados no es una tarea sencilla, pero con un enfoque cuidadoso y un buen conocimiento del sistema ERP-CRM, puede ser una herramienta poderosa para mejorar la eficiencia operativa y la satisfacción del cliente. Al seguir los pasos descritos en esta subunidad, se puede asegurar que el proceso de creación de formularios personalizados sea exitoso y alineado con las necesidades específicas del negocio.

<a id="creacion-de-informes-personalizados"></a>
## Creación de informes personalizados

La implantación de sistemas ERP-CRM en una empresa implica no solo la instalación inicial del software, sino también el desarrollo de componentes personalizados para satisfacer las necesidades específicas del negocio. En esta subunidad, nos centramos en la creación de informes personalizados, un aspecto crucial para obtener información valiosa y tomar decisiones estratégicas.

La creación de informes personalizados comienza con la definición de los campos que se desean incluir en el informe. Esto implica entender las necesidades del usuario final y seleccionar los datos relevantes para su análisis. A continuación, se crea una estructura básica del informe, utilizando herramientas gráficas o interfaces de desarrollo proporcionadas por el sistema ERP-CRM.

Una vez definida la estructura, se procede a la codificación de las consultas necesarias para obtener los datos requeridos. Esto puede implicar la creación de nuevas consultas SQL o el uso de funciones específicas del sistema ERP-CRM, dependiendo de su funcionalidad y la complejidad de los datos a recuperar.

El siguiente paso es diseñar la interfaz de entrada de datos y procesos que permitirá al usuario interactuar con el informe. Esto puede incluir formularios para ingresar parámetros o filtros específicos, así como interfaces gráficas para visualizar los resultados en forma tabular o gráfica.

Una vez completados estos pasos, se procede a la creación de informes personalizados. Estos informes pueden ser generados automáticamente cuando se cumplen ciertas condiciones o pueden ser ejecutados manualmente por el usuario. Es importante que los informes sean fáciles de entender y visualizar, lo que puede implicar el uso de gráficos y tablas para representar la información de manera efectiva.

Además, es crucial implementar procesos de mantenimiento y actualización del sistema de informes personalizados. Esto incluye la revisión periódica de los informes para asegurar su relevancia y precisión, así como la adaptación a cambios en las necesidades del negocio o en el formato de los datos.

La creación de informes personalizados también implica considerar aspectos de seguridad y privacidad. Es importante que solo los usuarios autorizados puedan acceder a ciertos informes y que se implementen medidas para proteger la información sensible almacenada en estos informes.

Finalmente, es necesario documentar todos los procesos relacionados con la creación de informes personalizados. Esto incluye la explicación de cómo funciona el sistema, las instrucciones paso a paso para crear un informe y cualquier otra información relevante que pueda ser útil para otros usuarios del sistema.

La creación de informes personalizados es una tarea compleja pero fundamental en la implantación de sistemas ERP-CRM. A través de este proceso, las empresas pueden obtener información valiosa y tomar decisiones estratégicas basadas en datos precisos y actualizados. Es importante que los profesionales encargados de esta tarea tengan un buen conocimiento del sistema y habilidades técnicas para desarrollar informes eficientes y efectivos.

<a id="paneles-de-control-dashboards"></a>
## Paneles de control (Dashboards)

La implantación de sistemas ERP-CRM en una empresa implica no solo la instalación y configuración del software, sino también el diseño y creación de paneles de control o dashboards. Estos paneles son herramientas esenciales para visualizar y monitorear los datos clave de la organización, facilitando así la toma de decisiones informadas.

El primer paso en la creación de un dashboard consiste en identificar las métricas más importantes que el negocio necesita monitorear. Esto puede incluir cifras financieras como ingresos, gastos y margen de beneficio, así como indicadores operativos como el tiempo de respuesta del servicio al cliente o la satisfacción del cliente.

Una vez identificadas las métricas clave, se procede a diseñar el layout del dashboard. Esto implica elegir una disposición visual que permita una rápida y fácil interpretación de los datos. Se utilizan gráficos y tablas para representar los datos de manera efectiva, asegurando que la información sea accesible y comprensible.

El proceso de diseño también incluye la elección de las herramientas y tecnologías adecuadas para crear el dashboard. Esto puede variar según la complejidad del sistema ERP-CRM y las preferencias organizacionales. Algunos sistemas pueden ofrecer funcionalidades internas para crear dashboards, mientras que otros pueden requerir la utilización de herramientas externas.

La creación de un dashboard es un proceso iterativo. Es común experimentar con diferentes diseños y layouts hasta encontrar el que mejor se adapta a las necesidades del negocio y facilita la comprensión de los datos. Además, es importante considerar la accesibilidad del dashboard para todos los usuarios, asegurando que sea fácilmente navegable y visualmente atractivo.

Una vez diseñado el layout, se procede a implementar el dashboard en el sistema ERP-CRM. Esto implica configurar las consultas necesarias para obtener los datos que se mostrarán en el panel de control. Es importante que estas consultas sean eficientes y rápidas, ya que un dashboard con consultas lentas puede afectar negativamente la experiencia del usuario.

Durante la implementación, es crucial realizar pruebas exhaustivas para asegurar que el dashboard funcione correctamente y muestre los datos de manera precisa. Esto incluye verificar que las consultas estén devolviendo los resultados esperados y que el diseño sea visualmente atractivo y fácil de interpretar.

Una vez implementado, es importante documentar todo el proceso para futuras referencias. Esto debe incluir detalles sobre la configuración del dashboard, las consultas utilizadas y cualquier personalización realizada. La documentación también debe facilitar la actualización del sistema en el futuro, asegurando que los cambios se realicen de manera eficiente.

El uso de paneles de control o dashboards es una práctica cada vez más común en la gestión empresarial moderna. Estos herramientas no solo facilitan la visualización y monitoreo de los datos clave, sino que también permiten una toma de decisiones informada basada en información actualizada y relevante. La implantación de un dashboard efectivo puede llevar a mejoras significativas en la eficiencia operativa y la satisfacción del cliente.

En conclusión, el diseño y creación de paneles de control o dashboards es una tarea crucial en la implantación de sistemas ERP-CRM. A través de un proceso iterativo que incluye la identificación de métricas clave, diseño visual, elección de herramientas adecuadas, implementación y pruebas exhaustivas, se puede crear un sistema que facilita la toma de decisiones informadas y mejora la eficiencia operativa.

<a id="integracion-con-otros-sistemas-de-gestion"></a>
## Integración con otros sistemas de gestión

La implantación de sistemas ERP-CRM en una empresa implica no solo la instalación y configuración del software, sino también su integración con otros sistemas existentes para garantizar un flujo eficiente de información. Esta integración es crucial para mantener la coherencia y la actualización de los datos entre diferentes departamentos y aplicaciones.

La primera etapa en la integración consiste en identificar los sistemas que necesitan ser conectados al ERP-CRM. Esto puede incluir sistemas de contabilidad, inventario, gestión de recursos humanos (HR), marketing y ventas, entre otros. Cada sistema tiene sus propias características y formatos de datos, por lo que es necesario realizar una evaluación detallada para determinar las necesidades específicas de cada uno.

Una vez identificados los sistemas a integrar, se procede a la configuración del ERP-CRM para establecer las conexiones adecuadas. Esto puede implicar la creación de interfaces o adaptadores que permitan el intercambio de datos entre los sistemas. Es importante asegurarse de que estos interfaces sean seguros y cumplen con los estándares de interoperabilidad relevantes.

La integración también implica la definición de procesos de sincronización de datos. Esto puede ser automático o manual, dependiendo del sistema y las necesidades específicas. Por ejemplo, el ERP-CRM puede actualizarse automáticamente cuando se realiza una entrada en el sistema de inventario, o viceversa.

Es crucial también considerar la seguridad durante la integración. Los sistemas deben estar protegidos contra accesos no autorizados y los datos sensibles deben ser cifrados durante su transmisión y almacenamiento. Además, es importante establecer políticas de acceso y control para garantizar que solo los usuarios autorizados puedan acceder a la información.

La integración del ERP-CRM con otros sistemas también puede implicar la creación de formularios personalizados y informes que reflejen las necesidades específicas de cada departamento. Esto puede requerir el desarrollo de componentes adicionales o la adaptación de los existentes para asegurar una interfaz amigable y eficiente.

Además, es importante realizar pruebas exhaustivas antes de la implantación final. Esto incluye pruebas de integración para asegurarse de que todos los sistemas funcionen correctamente juntos, así como pruebas de rendimiento para verificar que el sistema ERP-CRM no sobrecargue los recursos del servidor.

La documentación es otro aspecto crucial en la integración de sistemas ERP-CRM. Es importante mantener un registro detallado de todas las configuraciones realizadas, las interfaces creadas y los procesos de sincronización establecidos. Esta documentación será invaluable para el mantenimiento futuro del sistema y para la formación del personal.

Finalmente, la implantación del ERP-CRM con otros sistemas debe considerar la adaptabilidad a cambios futuros. Los sistemas deben estar diseñados de manera que puedan ser actualizados o modificados sin afectar los demás componentes del entorno empresarial. Esto puede implicar el uso de arquitecturas modulares y componentes desacoplados.

En resumen, la integración de sistemas ERP-CRM en una empresa es un proceso complejo pero fundamental para garantizar la eficiencia operativa y la coherencia de los datos. Requiere una evaluación cuidadosa, configuraciones precisas, procesos de sincronización adecuados y una consideración especializada en seguridad y adaptabilidad a cambios futuros.


<a id="desarrollo-de-componentes"></a>
# Desarrollo de componentes

<a id="arquitectura-del-erp-crm"></a>
## Arquitectura del ERP-CRM

En la subunidad "Arquitectura del ERP-CRM", nos adentramos en el diseño interno de los sistemas de gestión empresarial y de clientes (ERP-CRM). Comenzamos por entender que una arquitectura bien definida es fundamental para garantizar la eficiencia, escalabilidad y mantenibilidad de estos sistemas. La arquitectura del ERP-CRM se compone de varias capas, cada una con un propósito específico.

La primera capa es la de acceso a datos, donde se gestionan las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los datos almacenados en la base de datos. Esta capa interactúa directamente con el sistema de gestión de bases de datos y proporciona una interfaz para que otras partes del sistema accedan y manipulen los datos.

La segunda capa es la lógica de negocio, donde se implementan las reglas y procesos específicos de la empresa. Esta capa contiene la lógica empresarial que permite realizar operaciones complejas como el cálculo de precios, la gestión de inventario o la planificación de proyectos.

La tercera capa es la interfaz de usuario (UI), donde los usuarios interactúan con el sistema. La UI puede ser basada en gráficos y pantallas para aplicaciones web o escritorio, o bien en interfaces táctiles para dispositivos móviles. Esta capa se encarga de presentar los datos al usuario de una manera que sea intuitiva y fácil de usar.

La cuarta capa es la capa de servicios, donde se definen las operaciones que pueden ser invocadas por otras aplicaciones o sistemas externos. Estos servicios permiten integrar el ERP-CRM con otros sistemas de gestión empresarial o terceros, facilitando la interoperabilidad y la automatización de procesos.

La quinta capa es la capa de seguridad, donde se implementan los mecanismos para proteger los datos y garantizar que solo los usuarios autorizados puedan acceder a ciertas funcionalidades. Esta capa puede incluir autenticación, autorización y encriptación de datos.

La sexta capa es la capa de monitoreo y mantenimiento, donde se gestionan las operaciones diarias del sistema, como el seguimiento del rendimiento, la detección y solución de problemas y la actualización del software.

Cada una de estas capas desempeña un papel crucial en la funcionalidad global del ERP-CRM. La arquitectura bien definida permite una separación clara de responsabilidades, facilitando el desarrollo, la pruebas y el mantenimiento del sistema. Además, esta arquitectura permite una escalabilidad eficiente, ya que cada capa puede ser optimizada según sus necesidades específicas.

La comprensión de la arquitectura del ERP-CRM es fundamental para cualquier desarrollador o administrador de sistemas que quiera trabajar con estos tipos de aplicaciones. Permite entender cómo se organizan los componentes internos y cómo interactúan entre sí, lo que facilita el diagnóstico y solución de problemas, así como la implementación de mejoras y actualizaciones.

En resumen, la arquitectura del ERP-CRM es un aspecto crucial de su diseño y desarrollo. Una arquitectura bien definida permite una estructura clara, escalable y segura para los sistemas de gestión empresarial y de clientes, facilitando así su implementación y uso en entornos empresariales complejos.

<a id="lenguaje-proporcionado"></a>
## Lenguaje proporcionado

En la subunidad "Lenguaje proporcionado", se aborda el aspecto fundamental del desarrollo de componentes dentro de sistemas ERP-CRM. El lenguaje proporcionado es una herramienta esencial que permite a los desarrolladores crear funcionalidades personalizadas, adaptando el sistema ERP-CRM a las necesidades específicas de la empresa. Este lenguaje suele ser específico del software y puede variar según el sistema utilizado.

El lenguaje proporcionado facilita la manipulación de datos, la creación de formularios y informes personalizados, así como el procesamiento de información compleja. Permite a los desarrolladores integrar funcionalidades adicionales que no están disponibles en las interfaces estándar del sistema ERP-CRM, mejorando así su eficiencia operativa.

Además, este lenguaje proporcionado suele ofrecer una serie de funciones y librerías predefinidas que facilitan el desarrollo de componentes. Estas herramientas permiten realizar tareas como la inserción, modificación y eliminación de datos en los objetos del sistema, así como la realización de consultas complejas para obtener información relevante.

La documentación asociada al lenguaje proporcionado es crucial para el desarrollo exitoso de componentes. Ofrece una guía detallada sobre cómo utilizar las funciones disponibles, cómo estructurar el código y cómo depurar posibles errores. Esta documentación suele estar disponible en formato digital dentro del sistema ERP-CRM o puede ser consultada en línea.

El lenguaje proporcionado también permite la creación de formularios e informes personalizados. Esto es especialmente útil para mostrar información de manera más clara y accesible, adaptándola a las necesidades específicas de los usuarios finales. Los desarrolladores pueden diseñar formularios que incluyan campos personalizados, validaciones específicas y lógica adicional.

Además del desarrollo de componentes, el lenguaje proporcionado también facilita la integración con otros sistemas de gestión. Esto es crucial en entornos empresariales complejos donde múltiples sistemas están interconectados. El lenguaje proporcionado permite realizar llamadas a funciones y librerías (APIs) que permiten la comunicación entre diferentes sistemas, asegurando una integridad de datos y flujo de trabajo eficiente.

El desarrollo de componentes utilizando el lenguaje proporcionado requiere un enfoque estructurado. Los desarrolladores deben seguir ciertas prácticas recomendadas para garantizar la calidad del código y su mantenibilidad a largo plazo. Esto incluye la escritura de código limpio, modularizado y bien documentado.

En conclusión, el lenguaje proporcionado es una herramienta poderosa y flexible que permite al desarrollo de componentes en sistemas ERP-CRM un alto nivel de personalización y adaptabilidad. Su uso adecuado puede llevar a soluciones empresariales más eficientes y satisfactorias, mejorando así la productividad y el rendimiento operativo de las empresas.

<a id="entornos-de-desarrollo-y-herramientas-del-sistema-erp-y-crm"></a>
## Entornos de desarrollo y herramientas del sistema ERP y CRM

En el desarrollo de componentes para sistemas ERP-CRM, es crucial entender los entornos de desarrollo y las herramientas disponibles que facilitan esta tarea. Estos entornos proporcionan un espacio seguro y controlado donde se pueden crear, probar y depurar componentes sin afectar el sistema operativo o la aplicación principal.

El primer paso en la configuración del entorno de desarrollo es seleccionar una plataforma adecuada. Las plataformas modernas ofrecen herramientas integradas que facilitan la creación y gestión de componentes. Estas herramientas suelen incluir editores de código, compiladores, depuradores y simuladores, lo que permite un flujo de trabajo eficiente.

Una vez configurado el entorno, se pueden comenzar a crear componentes. Los componentes son unidades reutilizables de código que realizan una función específica. En el contexto de ERP-CRM, estos componentes pueden ser formularios personalizados, informes, paneles de control o incluso funciones auxiliares.

La creación de componentes implica la definición de interfaces y propiedades. Las interfaces definen qué funcionalidades puede realizar un componente, mientras que las propiedades permiten configurar su comportamiento y apariencia. Es importante diseñar estas interfaces de manera clara y coherente para facilitar su uso y mantenimiento.

Durante el desarrollo, es fundamental probar los componentes para asegurar que funcionan correctamente. Las herramientas de depuración proporcionan una serie de funciones útiles para identificar y solucionar problemas en el código. Además, se pueden utilizar pruebas unitarias para verificar que cada componente cumple con sus requisitos.

Una vez que un componente ha sido probado y aprobado, puede ser integrado en la aplicación principal. La integración implica la configuración de las relaciones entre componentes y la definición de flujos de trabajo. Es importante mantener una buena documentación durante este proceso para facilitar el mantenimiento futuro.

El desarrollo de componentes también implica la gestión del ciclo de vida de estos componentes. Esto incluye la creación, actualización, eliminación y reutilización de componentes a lo largo del tiempo. Las herramientas modernas ofrecen funcionalidades que facilitan esta gestión, como versionado y control de cambios.

En el ámbito de ERP-CRM, los componentes pueden interactuar con bases de datos para almacenar y recuperar información. Es importante diseñar estos componentes de manera eficiente para optimizar el rendimiento y la seguridad del sistema. Las herramientas proporcionadas por las plataformas modernas facilitan esta tarea, permitiendo realizar consultas complejas y gestionar transacciones de forma segura.

Finalmente, es crucial documentar los componentes durante todo el proceso de desarrollo. La documentación debe incluir información sobre la funcionalidad, configuración y uso del componente. Esta documentación será invaluable para otros desarrolladores que trabajen en el sistema o para futuras versiones del mismo.

En resumen, el desarrollo de componentes para sistemas ERP-CRM requiere un entorno adecuado, una buena planificación, pruebas rigurosas y una gestión eficiente del ciclo de vida. Las herramientas modernas ofrecen soluciones integrales que facilitan estos procesos, lo que permite crear componentes robustos y reutilizables para mejorar la funcionalidad y eficiencia de los sistemas ERP-CRM.

<a id="insercion-modificacion-y-eliminacion-de-datos-en-los-objetos"></a>
## Inserción, modificación y eliminación de datos en los objetos

En este capítulo, nos adentramos en la práctica del desarrollo de componentes dentro de sistemas de gestión empresariales, con un énfasis en las operaciones fundamentales de inserción, modificación y eliminación de datos en los objetos. Comenzamos por entender cómo estructurar estos componentes para que puedan interactuar eficazmente con el sistema.

La inserción de datos es la primera operación que debemos considerar. Un componente debe ser capaz de recibir nuevos registros o objetos desde una interfaz de usuario o desde otro componente del sistema, y luego almacenarlos en la base de datos correspondiente. Este proceso implica la creación de instancias de los objetos y su persistencia en el almacenamiento persistente.

La modificación de datos es un paso crucial para mantener la actualidad de la información en el sistema. Un componente debe permitir la edición de los atributos de los objetos existentes, asegurándose de que las modificaciones sean coherentes y seguras. Esto puede implicar la validación de los datos antes de su actualización y la gestión adecuada de las transacciones para mantener la integridad del sistema.

La eliminación de datos es otro aspecto fundamental en el desarrollo de componentes. Es importante diseñar sistemas que puedan eliminar objetos o registros cuando ya no sean necesarios, liberando así recursos y manteniendo la eficiencia del sistema. La eliminación debe ser segura y reversible, permitiendo recuperar los datos si es necesario.

En todos estos procesos, el manejo de excepciones es una cuestión crítica. Los componentes deben estar preparados para capturar y gestionar cualquier error que pueda surgir durante la inserción, modificación o eliminación de datos, asegurando que el sistema no se quede en un estado inconsistente.

Además, la persistencia de los objetos es otro aspecto importante a considerar. Los componentes deben ser capaces de serializar y deserializar los objetos para su almacenamiento y recuperación, utilizando formatos como JSON o XML. Esto permite que los datos sean transferibles entre diferentes sistemas y que puedan ser manipulados por herramientas externas.

La gestión de transacciones es otro tema clave en el desarrollo de componentes. Los componentes deben estar diseñados para manejar las transacciones de manera coherente, asegurando que todas las operaciones dentro de una transacción sean realizadas juntas o no se realicen ninguna. Esto implica la utilización de mecanismos como los bloques `try-catch` y el control de la concurrencia para evitar problemas de integridad.

En conclusión, el desarrollo de componentes en sistemas de gestión empresariales requiere una comprensión profunda de las operaciones básicas de inserción, modificación y eliminación de datos. Al diseñar estos componentes, debemos considerar no solo la funcionalidad necesaria, sino también la eficiencia, la seguridad y la capacidad de manejar errores para garantizar que el sistema sea robusto y confiable.

<a id="operaciones-de-consulta-herramientas"></a>
## Operaciones de consulta. Herramientas

En este capítulo, nos adentramos en las operaciones de consulta y las herramientas disponibles para realizarlas en sistemas de gestión empresariales (ERP-CRM). Comenzamos por entender que las consultas son una parte esencial del acceso a la información almacenada en estos sistemas. Las operaciones de consulta permiten recuperar, filtrar y analizar datos de manera eficiente, lo cual es crucial para tomar decisiones informadas.

La herramienta más común utilizada para realizar estas operaciones es el lenguaje SQL (Structured Query Language), que proporciona una forma estándar para interactuar con las bases de datos. A través de SQL, podemos crear consultas complejas que seleccionan, agrupan y ordenan los datos según nuestras necesidades. Los comandos básicos como SELECT, FROM, WHERE, GROUP BY y ORDER BY son fundamentales para cualquier consulta en un ERP-CRM.

Además de SQL, muchos sistemas ERP-CRM ofrecen interfaces gráficas intuitivas que permiten realizar consultas sin conocimiento previo de lenguaje SQL. Estas herramientas proporcionan una forma visual de seleccionar campos, establecer filtros y organizar los resultados, lo que facilita el acceso a la información para usuarios no técnicos.

Es importante destacar que las operaciones de consulta no se limitan solo a recuperar datos; también incluyen la creación de vistas personalizadas, que son consultas predefinidas que pueden ser ejecutadas en cualquier momento. Las vistas facilitan el acceso a conjuntos recurrentes de datos y suelen estar optimizadas para mejorar el rendimiento.

Otra herramienta valiosa es el uso de macros o scripts dentro del ERP-CRM. Estos permiten automatizar tareas repetitivas, como la creación de informes periódicos o la actualización de campos en múltiples registros. Las macros pueden ser escritas en lenguajes específicos del sistema y ejecutadas desde interfaces gráficas o a través de comandos.

En el contexto de sistemas ERP-CRM, las consultas también pueden involucrar la manipulación de datos. Esto puede incluir la creación de nuevos registros, la modificación de campos existentes y la eliminación de información no necesaria. Las operaciones de inserción (INSERT), actualización (UPDATE) y eliminación (DELETE) son fundamentales para mantener los datos en un estado actualizado y relevante.

Además de las consultas básicas, muchos ERP-CRM ofrecen funciones avanzadas como el uso de subconsultas y la combinación de múltiples selecciones. Las subconsultas permiten realizar consultas dentro de otras consultas, lo que es útil para obtener información condicional o filtrada. La combinación de múltiples selecciones permite un análisis más detallado de los datos, combinando resultados de diferentes consultas en una sola vista.

La eficiencia y precisión de las operaciones de consulta son cruciales en sistemas ERP-CRM, ya que afectan directamente a la toma de decisiones empresariales. Por lo tanto, es importante no solo conocer cómo realizar estas operaciones, sino también cómo optimizarlas para mejorar el rendimiento del sistema.

En resumen, las operaciones de consulta y las herramientas disponibles para realizarlas son fundamentales en sistemas de gestión empresariales. Desde la utilización de SQL hasta interfaces gráficas y macros, cada opción ofrece diferentes ventajas dependiendo del nivel de conocimiento técnico y las necesidades específicas del usuario. Comprender cómo utilizar estas herramientas eficazmente es una habilidad clave para cualquier profesional que trabaje con sistemas ERP-CRM.

<a id="formularios-e-informes"></a>
## Formularios e informes

En la subunidad "Formularios e informes", nos centramos en los elementos clave que permiten interactuar con el usuario y presentar información de manera estructurada. Los formularios son interfaces gráficas que recopilan datos del usuario, mientras que los informes proporcionan una visualización organizada de la información almacenada.

Los formularios son fundamentales para la interacción directa entre el usuario y el sistema. Son componentes visuales que permiten al usuario ingresar o seleccionar datos, lo que facilita la entrada de información en sistemas empresariales. Cada formulario está compuesto por diversos tipos de campos, como cajas de texto, botones, listas desplegables y checkboxes, cada uno con un propósito específico para recopilar diferentes tipos de datos.

Los informes, por otro lado, son documentos que presentan la información de manera clara y organizada. Son herramientas esenciales para el análisis y la toma de decisiones basadas en los datos del sistema. Los informes pueden incluir gráficos, tablas y listados detallados, proporcionando una visión completa y fácilmente interpretable de los datos relevantes.

En esta subunidad, exploramos cómo crear formularios e informes utilizando herramientas y lenguajes específicos para el desarrollo de aplicaciones empresariales. Aprenderemos a diseñar interfaces gráficas que sean intuitivas y eficientes, así como a generar documentos informativos que faciliten la comprensión y análisis de los datos.

Además, discutiremos técnicas avanzadas para mejorar la experiencia del usuario en formularios, como el uso de validaciones dinámicas y mensajes de error claros. También exploraremos cómo optimizar la presentación de informes para maximizar su utilidad y facilitar su comprensión.

A lo largo de esta subunidad, trabajaremos con ejemplos prácticos y proyectos que permitan aplicar los conocimientos adquiridos en el desarrollo de formularios e informes. Estos proyectos nos ayudarán a entender cómo integrar estos elementos en sistemas empresariales reales, mejorando así la eficiencia y la toma de decisiones.

En resumen, "Formularios e informes" es una sección crucial para el desarrollo de aplicaciones empresariales, ya que proporciona las herramientas necesarias para interactuar con los usuarios y presentar información de manera efectiva. A través de esta subunidad, adquiriremos habilidades valiosas en diseño y programación de interfaces gráficas, lo que nos permitirá crear soluciones informáticas más robustas y eficientes.

<a id="procesamiento-de-datos-y-obtencion-de-la-informacion"></a>
## Procesamiento de datos y obtención de la información

En la subunidad "Procesamiento de datos y obtención de la información", nos sumergimos en el núcleo del desarrollo de componentes dentro de sistemas ERP-CRM. Este proceso es fundamental para que los componentes puedan interactuar eficazmente con los datos almacenados, permitiendo así una gestión precisa y eficiente de la información empresarial.

El primer paso en este flujo es entender cómo insertar, modificar y eliminar datos en los objetos del sistema. Esta operación es esencial para mantener la integridad y actualidad de la información. A través de métodos específicos proporcionados por el lenguaje o framework utilizado, se pueden realizar estas acciones con precisión, asegurando que los cambios sean reflejados de manera consistente en la base de datos.

La obtención de información es otro aspecto crucial del procesamiento de datos. Los componentes deben ser capaces de consultar y recuperar datos de manera eficiente y precisa. Utilizando herramientas como consultas SQL o APIs específicas, los componentes pueden realizar búsquedas complejas y filtrados para obtener solo la información relevante. Esta capacidad es fundamental para proporcionar informes precisos y actualizados a los usuarios del sistema.

El procesamiento de datos también implica la manipulación de estos mismos para extraer información valiosa. Esto puede implicar cálculos, agrupaciones o transformaciones de los datos originales. A través de funciones específicas o métodos de programación, los componentes pueden realizar estas operaciones con facilidad, generando resultados útiles que pueden ser utilizados en informes o análisis adicionales.

La obtención y procesamiento de información también implican la gestión de errores y excepciones. Es importante que los componentes estén diseñados para manejar situaciones inesperadas o datos incompletos, asegurando que el sistema no se bloquee ni produzca resultados incorrectos. Utilizando técnicas de depuración y control de excepciones, los desarrolladores pueden garantizar la robustez del componente.

Además, es crucial que los componentes sean capaces de interactuar con otros sistemas o bases de datos para obtener información adicional. Esto puede implicar la realización de llamadas a APIs externas o la integración con sistemas de almacenamiento alternativos. A través de métodos específicos proporcionados por el lenguaje o framework, los componentes pueden realizar estas operaciones de manera eficiente y segura.

La obtención y procesamiento de información también implican la creación de formularios e informes personalizados. Los componentes deben ser capaces de generar interfaces gráficas que permitan a los usuarios interactuar con la información en una forma intuitiva y visualmente atractiva. A través de herramientas específicas proporcionadas por el lenguaje o framework, los desarrolladores pueden crear formularios e informes personalizados que reflejen las necesidades específicas del usuario.

El procesamiento de datos también implica la obtención de información en tiempo real. En sistemas empresariales dinámicos, es crucial que los componentes puedan recuperar y mostrar información actualizada en tiempo real. A través de técnicas como el manejo de eventos o la realización de consultas periódicas, los componentes pueden garantizar que la información mostrada al usuario sea siempre precisa.

La obtención y procesamiento de información también implican la generación de gráficos y visualizaciones. Los componentes deben ser capaces de generar gráficos y diagramas que permitan a los usuarios visualizar datos complejos de manera intuitiva. A través de herramientas específicas proporcionadas por el lenguaje o framework, los desarrolladores pueden crear gráficos y visualizaciones personalizados que reflejen las necesidades específicas del usuario.

En resumen, el procesamiento de datos y obtención de la información es un aspecto crucial del desarrollo de componentes dentro de sistemas ERP-CRM. A través de métodos específicos proporcionados por el lenguaje o framework utilizado, los componentes pueden realizar inserciones, modificaciones y eliminaciones de datos con precisión, así como obtener y procesar información de manera eficiente y segura. La capacidad de manejar errores y excepciones, interactuar con otros sistemas o bases de datos, crear formularios e informes personalizados, generar gráficos y visualizaciones es fundamental para garantizar la robustez, precisión y utilidad del componente en el sistema empresarial.

<a id="llamadas-a-funciones-librerias-de-funciones-apis"></a>
## Llamadas a funciones, librerías de funciones (APIs)

En este capítulo, nos adentramos en la profundidad del desarrollo de componentes dentro de sistemas ERP-CRM, explorando cómo interactúan con funciones y librerías de funciones conocidas como APIs (Application Programming Interfaces). Las APIs son una puerta abierta que permite a diferentes aplicaciones o programas comunicarse entre sí, facilitando el intercambio de datos y la ejecución de operaciones específicas.

La primera parte de este capítulo se centra en cómo insertar, modificar y eliminar datos en los objetos. A través de las APIs proporcionadas por el sistema ERP-CRM, podemos realizar estas acciones con precisión y eficiencia. Por ejemplo, para insertar un nuevo cliente, simplemente necesitamos llamar a la función correspondiente pasando los parámetros necesarios. El proceso es similar para modificar o eliminar registros existentes.

La siguiente sección del capítulo explora las operaciones de consulta. A través de APIs, podemos realizar consultas complejas y obtener información detallada sobre nuestros datos. Las herramientas proporcionadas por el sistema nos permiten filtrar, ordenar y agrupar los resultados según nuestras necesidades específicas. Esta funcionalidad es crucial para la organización y análisis de la información en sistemas ERP-CRM.

El capítulo también aborda la creación de formularios e informes personalizados. A través de las APIs disponibles, podemos diseñar interfaces de usuario interactivas que permitan a los usuarios interactuar con los datos del sistema de manera intuitiva. Además, podemos generar informes y listados detallados que proporcionen una visión clara y completa de la información relevante.

La sección siguiente se centra en el procesamiento de datos y obtención de información. A través de las APIs, podemos realizar operaciones avanzadas sobre los datos almacenados en el sistema ERP-CRM. Esto puede incluir cálculos complejos, análisis estadísticos y transformación de datos para su uso en informes o análisis adicionales.

El capítulo también explora cómo llamar a funciones y librerías de funciones (APIs). A través de las APIs proporcionadas por el sistema ERP-CRM, podemos acceder a una amplia gama de operaciones específicas. Esto puede incluir la ejecución de procedimientos almacenados, la realización de consultas complejas y la manipulación de datos en tiempo real.

La sección final del capítulo aborda la depuración y tratamiento de errores. A través de las APIs proporcionadas por el sistema ERP-CRM, podemos realizar operaciones avanzadas sobre los datos almacenados en el sistema ERP-CRM. Esto puede incluir cálculos complejos, análisis estadísticos y transformación de datos para su uso en informes o análisis adicionales.

En resumen, este capítulo nos ha proporcionado una visión detallada del desarrollo de componentes dentro de sistemas ERP-CRM, explorando cómo interactúan con funciones y librerías de funciones conocidas como APIs. A través de las APIs proporcionadas por el sistema ERP-CRM, podemos realizar operaciones avanzadas sobre los datos almacenados en el sistema ERP-CRM, facilitando la organización y análisis de la información en sistemas ERP-CRM.

<a id="depuracion-y-tratamiento-de-errores"></a>
## Depuración y tratamiento de errores

En la etapa final del desarrollo de componentes para sistemas ERP-CRM, depuración y tratamiento de errores son aspectos cruciales que no pueden ser ignorados. La depuración es el proceso mediante el cual se identifican y solucionan los problemas o errores en el código fuente de un programa. En el contexto de los componentes del ERP-CRM, esto puede implicar la revisión detallada de las operaciones realizadas por cada componente para asegurar que funcionen correctamente.

El tratamiento de errores es una práctica complementaria a la depuración, enfocándose en cómo manejar y reportar los problemas cuando ocurren. Esto incluye el uso de mecanismos como excepciones para capturar errores inesperados y proporcionar respuestas adecuadas al usuario o al sistema.

La depuración y tratamiento de errores son interrelacionados, ya que una vez identificado un error, es necesario tratarlo con el fin de mantener la estabilidad y la funcionalidad del componente. En el desarrollo de componentes para ERP-CRM, es común utilizar herramientas de depuración integradas en los IDEs (Entornos de Desarrollo Integrados) que facilitan la identificación y análisis de errores.

Además de las técnicas manuales de depuración, como el uso del depurador visual o la impresión de variables para rastrear su valor a lo largo del tiempo, existen métodos automáticos como el análisis estático del código. Estos métodos pueden detectar posibles errores antes de que se produzcan en tiempo de ejecución, lo que puede ahorrar tiempo y esfuerzo en la depuración posterior.

El tratamiento de errores implica no solo identificar los problemas, sino también proporcionar soluciones efectivas. Esto puede implicar el ajuste del código para corregir el error o el uso de mecanismos como el manejo de excepciones para capturar y gestionar los errores sin interrumpir la ejecución del programa.

En el desarrollo de componentes para ERP-CRM, es crucial mantener un enfoque proactivo en la depuración y tratamiento de errores. Esto no solo mejora la calidad del software final, sino que también aumenta la confianza del usuario en su funcionalidad y seguridad. Además, una buena práctica de depuración y tratamiento de errores facilita el mantenimiento y actualización del sistema a lo largo del tiempo.

En conclusión, la depuración y tratamiento de errores son aspectos fundamentales del desarrollo de componentes para sistemas ERP-CRM. A través de técnicas manuales y automáticas, es posible identificar y gestionar los problemas que surgen durante el proceso de desarrollo, asegurando así la estabilidad y funcionalidad del software final.


<a id="actividad-libre-de-final-de-evaluacion-la-milla-extra"></a>
# Actividad libre de final de evaluación - La milla extra

<a id="la-milla-extra-primera-evaluacion"></a>
## La Milla Extra - Primera evaluación

### ejercicio

```markdown

```
