#Creado por el Grupo 6 el  02/28/2023
#language: es

Característica: Priorizar voluntarios
  Como administrador quiero priorizar los voluntarios que han confirmado su asistencia para que no se exceda el personal requerido.

  Esquema del escenario: Priorizar voluntarios confirmados en base a una habilidad requerida
    Dado que tengo una emergencia que necesita de "<vacantes>" voluntarios con la habilidad "<habilidad_solicitada>"
    Y tengo a varios "<lista_voluntarios_confirmados>" que confirmaron la asistencia
    Cuando priorizo los voluntarios con mas experiencia según la habilidad "<habilidad_solicitada>"
    Entonces tendré una lista "<lista_voluntarios_priorizada>" priorizada
    Ejemplos:
      | vacantes | habilidad_solicitada | lista_voluntarios_confirmados | lista_voluntarios_priorizada|
      | 1      | "Anestesiar"          | {"voluntario1": {"nombre":"Andres", "apellido":"Soto", "horas_experiencia": [55.0, 125.0], "habilidad": ["Rcp","Anestesiar"]}, "voluntario2":{"nombre":"Elizabeth","apellido":"Alma","horas_experiencia":[105.0],"habilidad":["Anestesiar"]}}| ['Andres Soto']|
      | 2      | "Rcp"          | {"voluntario1": {"nombre":"Andres", "apellido":"Soto", "horas_experiencia": [55.0, 125.0], "habilidad": ["Rcp","Anestesiar"]}, "voluntario2":{"nombre":"Elizabeth","apellido":"Alma","horas_experiencia":[105.0],"habilidad":["Anestesiar"]}}| ['Andres Soto', 'Elizabeth Alma']|
      | 3      | "Suturar"          | {"voluntario1": {"nombre":"Andres", "apellido":"Soto", "horas_experiencia": [55.0, 125.0], "habilidad": ["Rcp","Anestesiar"]}, "voluntario2":{"nombre":"Elizabeth","apellido":"Alma","horas_experiencia":[105.0],"habilidad":["Anestesiar"]}}| ['Andres Soto', 'Elizabeth Alma']|