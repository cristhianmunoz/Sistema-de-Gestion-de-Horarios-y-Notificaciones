# Creado por el Grupo 1
# language: es

Característica: Gestión de horarios del personal y actividades
  Como administrador del personal medico deseo gestionar los
  horarios de personal para organizar la atención a pacientes
  y determinar tiempos críticos.

   Escenario: Identificar tiempos críticos de las actividades de una emergencia
    Dado que existe una emergencia registrada en el sistema con el nombre "Emergencia X"
    Y que tengo un grupo de "2" voluntarios con sus horarios de disponibilidad
    Y la emergencia tiene registradas "2" actividades con horarios definidos
    Cuando al comparar los horarios de disponibilidad de cada voluntario con los horarios de cada actividad
    Entonces debería poder identificar los períodos en los que no hay ningún voluntario disponible para cada actividad de la emergencia
    Y debería poder visualizar los tiempos críticos de la emergencia "Emergencia X" de manera clara y detallada


   Escenario: Asignar un horario a una actividad
    Dado que el sistema tiene la actividad "Limpieza de Salas" registrada en el sistema
    Cuando el administrador del personal médico asigna un horario los dias "Lunes" en el periodo de "8:00" a "12:00" horas para la actividad
    Entonces se registra la asignación del horario para la actividad