#Creado por el Grupo 6 el  02/28/2023
#language: es

Característica: Priorizar voluntarios
  Como administrador quiero priorizar los voluntarios que han confirmado su asistencia para que no se exceda el personal requerido.

  Esquema del escenario: Priorizar voluntarios confirmados en base a una habilidad requerida
    Dado que tengo una emergencia que necesita de "<vacantes>" voluntarios con la habilidad "<habilidad_solicitada>"
    Y tengo a varios "<lista_voluntarios_confirmados>" que confirmaron la asistencia
    Cuando quiera priorizar los voluntarios con mas experiencia en la habilidad "<habilidad_solicitada>"
    Entonces tendré a los voluntarios priorizados con mayor experiencia con la habilidad "<habilidad_solicitada>"
    Ejemplos:
      | vacantes | habilidad_solicitada | lista_voluntarios_confirmados                                                                                                                                         |
      | 10.0     | suturar            | {"voluntario1": {"Nombre":"Andres", "horas_experiencia": 25.0, "Habilidad": "SUTURAR"}, "voluntario2":{"Nombre":"Juan","horas_experiencia":25.0,"Habilidad":"SUTURAR"}} |
      | 20.0     | "RCP"                | {"voluntario1": {"Nombre":"Juan", "horas_experiencia": 25.0, "Habilidad": "SUTURAR"}, "voluntario2":{"Nombre":"Juan","horas_experiencia":25.0,"Habilidad":"SUTURAR"}} |
      | 5.0      | "RCP"                | {"voluntario1": {"Nombre":"Juan", "horas_experiencia": 25.0, "Habilidad": "SUTURAR"}, "voluntario2":{"Nombre":"Juan","horas_experiencia":25.0,"Habilidad":"SUTURAR"}} |