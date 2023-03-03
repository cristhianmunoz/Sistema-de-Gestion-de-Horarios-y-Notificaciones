# Created by el Grupo 5 at 2/23/2023
# language: es




Característica: Solicitar servicios
  Como administrador del personal médico deseo solicitar servicios a los voluntarios, para atender las emergencias médicas
  #Falta cuantos para atender la emergencia
  #Los voluntaripos tengan habilidades
  #Match de los voluntarios requeridos para atender la emergencia
  #Crear un escenario que permita atender todas las emergencias medicas
  Esquema del escenario: Solicitar servicios a los voluntarios necesarios para satisfacer la emergencia necesitada
    Dado que tengo una emergencia con titulo "<tituloEmergencia>" y su descripción "<descripcionEmergencia>"
    Y necesito "<numeroDeVoluntariosRequeridos>" voluntarios para atender la emergencia con las siguientes habilidades requeridas: "<habilidadesRequeridas>"
    Cuando solicite servicios a los "<voluntarios>" registrados en el sistema
    Y las "<habilidadesVoluntarios>" coincidan con las "<habilidadesRequeridas>"
    Y el "<numeroDeVoluntariosRequeridos>" sea igual a la cantidad de "<voluntariosSeleccionados>"
    Entonces se enviara "<numeroDeNotificaciones>" en base a los "<voluntariosSeleccionados>"
    Ejemplos:
      | tituloEmergencia | descripcionEmergencia                                  | numeroDeVoluntariosRequeridos | habilidadesRequeridas   | habilidadesVoluntarios  | numeroDeVoluntariosRequeridos | voluntariosSeleccionados | numeroDeNotificaciones |
      | Terremoto        | Se solicita ayuda para atender la emergencia terremoto | 3                             | Saturar, RCP            | Saturar, RCP            | 3                             | Juan, Andres, Carlos     | 3                      |
      | Incendio         | Se solicita ayuda para atender la emergencia incendio  | 2                             | Quemaduras, Respiracion | Quemaduras, Respiracion | 2                             | Fernando, Kevin          | 2                      |



