# Sistema de Gestión de Horarios y Notificaciones Médicas

Una aplicación web para la planificación eficiente del tiempo de trabajo en organizaciones médicas. La aplicación permite a los usuarios revisar y editar el horario de los miembros del personal y los voluntarios de la organización. Brinda acceso a un sistema de notificación confiable para informar a los voluntarios que serán necesitados.

## Contenido
[1. Historias de Usuario](#1-historias-de-usuario)  
[2. Instrucciones de Inicio](#2-instrucciones-de-inicio)  
&nbsp;&nbsp;&nbsp;&nbsp;[2.1. Versiones de las Herramientas](#21-versiones-de-las-herramientas)  
&nbsp;&nbsp;&nbsp;&nbsp;[2.2. Creación del Proyecto](#22-creación-del-proyecto)  
&nbsp;&nbsp;&nbsp;&nbsp;[2.3. Jerarquía de Paquetes](#23-jerarquía-de-paquetes)  
[3. Uso de GitHub](#3-uso-de-github)  
&nbsp;&nbsp;&nbsp;&nbsp;[3.1. Criterios de Evaluación de los Merge Requests](#31-criterios-de-evaluación-de-los-merge-requests)  
&nbsp;&nbsp;&nbsp;&nbsp;[3.2. Convención para los Commits](#32-convención-para-los-commits)  

## 1. Historias de Usuario

A continuación, se muestran las historias de usuario asignadas a cada uno de los grupos de trabajo. 

| **Grupo de Trabajo** | **Historia de Usuario**                                                                                                                                                                                     | **Estimación (Story Points)** |
|:--------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------:|
|       Grupo 1        | **HU5:** Como administrador del personal medico deseo gestionar los horarios de personal para organizar la atención a pacientes y determinar tiempos críticos.                                              |               8               |
|       Grupo 2        | **HU1:** Como voluntario inscrito en el programa de voluntariado quiero que tomen en cuenta mis habilidades y mi disponibilidad para ganar experiencia y adquirir conocimientos prácticos en el área médica. |               3               |
|       Grupo 3        | **HU4:** Como administrador del personal médico, quiero asignar voluntarios a los actividades para atender una emergencia.                                                                               |               5               |
|       Grupo 4        | **HU2:** Como voluntario quiero confirmar mi asistencia a una emergencia médica para ayudar rápidamente cuando se me necesite.                                                                              |               3               |
|       Grupo 5        | **HU6:** Como administrador del personal médico deseo solicitar servicios a los voluntarios, para atender las emergencias médicas.                                                                          |               3               |
|       Grupo 6        | **HU3:** Como administrador quiero priorizar los voluntarios que han confirmado su asistencia para que no se exceda el personal requerido.                                                                  |               5               |

## 2. Instrucciones de Inicio

### 2.1. Versiones de las Herramientas

Para asegurar el correcto funcionamiento del proyecto asegúrate de contar con las versiones adecuadas de las herramientas utilizadas. Para ello, puedes basarte en el listado mostrado a continuación:

* Python 3.11.0
* Django 4.1.7
* Cucumber 11.4.0
* Behave 1.2.6
* Faker 17.3.0
* SQLite 3.40.1
* PyCharm 2022.3.2

### 2.2. Creación del Proyecto

Los pasos necesarios para vincular el proyecto de GitHub con tu repositorio local se muestran a continuación:

**1. Crea un nuevo proyecto en PyCharm desde VCS:** Al abrir PyCharm, crea un nuevo proyecto seleccionando la opción ```Get from VCS```.

![Creación de un Proyecto desde VCS](https://i.ibb.co/WnWBcBp/01.png)

**2. Configura el directorio local del proyecto:** Asegúrate de que el nombre de la carpeta que contendrá el proyecto localmente sea ```notificaciones_medicas```.

![Configuración del directorio local](https://i.ibb.co/h9hjdRB/02.png)

**3. Configura el intérprete de Python del proyecto local:** Ingresa a las configuraciones de tu proyecto local y agrega un nuevo intérprete de Python.

![Configuración del directorio local](https://i.ibb.co/G5pQVh0/03.png)

Es recomendable crear un ambiente virtual de Python que se utilizará únicamente para este proyecto.

![Configuración del directorio local](https://i.ibb.co/Fnvbx5L/04.png)

**4. Instala los paquetes de Django y Behave:** En el intérprete de Python que creaste instala los paquetes de Django y Behave de acuerdo con las versiones acordadas.

![Instalación de paquetes de Django y Behave](https://i.ibb.co/BgNPr7P/05.png)

**5. Ingresa a la configuración del servidor de Django:** En PyCharm selecciona la opción ```Edit Configurations``` para ingresar a la configuración del servidor de Django. 

![Ingreso a la configuración del servidor de Django](https://i.ibb.co/PFgYqGR/06.png)

**6. Configura las variables de entorno del servidor de Django:** Ingresa la variable de entorno ```DJANGO_SETTINGS_MODULE=notificaciones_medicas.settings```.

![Configuración de las variables de entorno del servidor de Django](https://i.ibb.co/C1DNd04/07.png)

**7. Crea una base de datos SQLite:** Abre la pestaña ```Database``` y crea una base de datos SQLite.

![Creación de una base de datos SQLite](https://i.ibb.co/LQMWmFN/08.png)

**8. Configura y prueba la conexión con la base de datos:** Coloca el nombre ```db.sqlite3``` a la base de datos y comprueba su conexión.

![Configuración de la conexión con la base de datos](https://i.ibb.co/rthKs5s/09.png)

**9. Aplica la última migración en la base de datos:** Utiliza el comando ```python manage.py migrate``` desde la terminal de Windows PowerShell para aplicar la última migración en la base de datos.

![Aplicación de la última migración en la base de datos](https://i.ibb.co/h7C3qRw/10.png)

**10. Comprueba la aplicación de la migración en la base de datos:** Recarga la base de datos y comprueba la aplicación de la última migración.

![Comprobación de la última migración](https://i.ibb.co/Kmpg0PL/11.png)

**11. Ejecuta el proyecto y comprueba su funcionamiento:** Ejecuta el proyecto, dirige al navegador e introduce la URL respectiva para comprobar el funcionamiento del proyecto.

![Comprobación del funcionamiento del proyecto](https://i.ibb.co/3sHdDmp/12.png)

### 2.3. Jerarquía de Paquetes

Considerando la [estructura de archivos propuesta en clase](https://coggle.it/diagram/YKwIGLwdFm3ufpye/t/bdd/bbc003c7d1c0544999001d47e8effe4a9987a3226e473307526633410016956a) para el desarrollo de software mediante BDD con Gherkin y Behave se utilizará un directorio ```test``` en cada aplicación del proyecto. El directorio ```test``` tendrá un directorio ```features``` para los archivos de Gherkin y un directorio ```steps``` para los archivos de Behave:

Adicionalmente, se utilizará el archivo ```environment.py``` para gestionar las operaciones que se realizan antes o después de la ejecución de los escenarios de prueba.

La estructura mencionada para el uso de Gherkin y Behave se muestra a continuación:

![Estructura de archivos para BDD con Gherkin y Behave](https://i.ibb.co/p2HQPJ6/tests.png)

Por otro lado, para la arquitectura MVC en cada aplicación del proyecto se utilizarán los paquetes MVC ```controller```, ```model``` y ```view```. Esto con el objetivo de crear un archivo para cada controlador, modelo o vista respectivamente.

Además, se utilizará el directorio ```static``` para almacenar archivos estáticos que son utilizados por las páginas web.

La estructura mencionada para el uso de MVC como arquitectura se muestra a continuación:

![Estructura de paquetes para MVC](https://i.ibb.co/MkzpFPd/mvc.png)

## 3. Uso de GitHub

### 3.1. Criterios de Evaluación de los Merge Requests

La aceptación de un Merge Request se basará en el cumplimiento total de los apartados mostrados a continuación:

* Uso de la Guía de Estilos PEP 8.
* Porcentaje del 100% en los escenarios de prueba.

**Nota:** Puedes revisar la Guía de Estilos PEP 8 ingresando al [sitio web oficial](https://peps.python.org/pep-0008/). 

### 3.2. Convención para los Commits

Para facilitar la comprensión de los commits realizados se recomienda seguir los puntos mencionados a continuación:

* **Utilizar prefijos en el título del commit:** Una buena forma de resumir el commit realizado es utilizando alguno de los siguientes prefijos:

```bash
Feat: Una nueva característica para el usuario.
Fix: Arregla un bug que afecta al usuario.
Refactor: Refactorización del código como cambios de nombre de variables o funciones.
Style: Cambios de formato, tabulaciones, espacios o puntos y coma.
Test: Añade tests o refactoriza uno existente.
```
    
Si utilizas la línea de comandos para escribir tus commits puedes basarte en el siguiente ejemplo:

```bash
git commit -m "Feat: Registro de voluntarios" -m "Se han agregado algunos métodos en la clase Voluntario para permitir el registro de voluntarios."
```

* **Utilizar un título y un cuerpo para el commit:** Aparte del título es recomendable escribir todo el contexto del commit en su cuerpo.

Si utilizas la línea de comandos para escribir tus commits puedes utilizar la siguiente sintaxis:

```bash
git commit -m "Título del commit" -m "Cuerpo del commit."
```

**Nota:** Puedes revisar algunas de las buenas prácticas para escribir commits desde el sitio web [midudev](https://midu.dev/buenas-practicas-escribir-commits-git/). 
