# Created by Giancarlo Naranjo at 2/23/2023
# language: es

Característica: Solicitar servicios
  Como administrador del personal médico deseo solicitar servicios a los voluntarios, para atender las emergencias médicas

  Escenario: Solicitar servicios para atender una emergencia médica
    Dado que tengo una emergencia y existe un registro de voluntarios
    Cuando realice una petición de servicios con las habilidades requeridas para atender esa emergencia
    Entonces se enviara una notificación a los voluntarios con la emergencia y la lista de habilidades requeridas

