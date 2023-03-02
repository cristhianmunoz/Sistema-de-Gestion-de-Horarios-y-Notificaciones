# Created by BryanPC at 1/3/2023
# language: es

  Característica: Asignar un horario a una actividad registrada en el sistema
  Como administrador del personal médico deseo
  gestionar los horarios de personal para organizar
  la atención a pacientes y determinar tiempos críticos.

Esquema del escenario: el administrador del personal médico desea asignar un horario a una actividad en un horario ocupado por otra actividad
  Dado que el horario de la institución médica tiene asignado un horario los dias "<dia_asignado>" en el periodo de "<inicio_asignado>" a "<final_asignado>" horas para la actividad "<actividad_asignada>"
  Cuando el administrador del personal médico asigne el horario los dias "<dia_solicitado>" en el periodo de "<inicio_solicitado>" a "<final_solicitado>" horas para la actividad "<actividad_solicitada>"
  Entonces el sistema asignara el horario los dias "<dia_solicitado>" en el periodo de "<inicio_solicitado>" a "<final_solicitado>" horas para la actividad "<actividad_solicitada>" en paralelo a el horario anterior

  Ejemplos:
      | actividad_asignada | dia_asignado   | inicio_asignado   | final_asignado   | dia_solicitado | inicio_solicitado | final_solicitado | actividad_solicitada |
      | Primeros auxilios  | Lunes          | 07:00             | 09:00            | Lunes          | 08:00             | 09:00            | Evacuar              |
      | Primeros auxilios  | Lunes          | 13:00             | 16:00            | Lunes          | 14:00             | 16:00            | Evacuar              |
      | Evacuar            | Miércoles      | 09:00             | 12:00            | Miércoles      | 10:00             | 11:00            | Primeros auxilios    |
      | Evacuar            | Viernes        | 10:00             | 12:00            | Viernes        | 10:00             | 12:00            | Primeros auxilios    |

  Escenario: El administrador del personal médico desea asignar un horario a una actividad registrada en el sistema
  Dado el horario de la institución médica tiene disponible los dias "Lunes" en el periodo de "9:00" a "12:00" horas para asignar una actividad
  Cuando el administrador del personal médico asigne el horario los dias "Lunes" en el periodo de "9:00" a "12:00" horas para la actividad "Primeros auxilios"
  Entonces el sistema asignara el horario los dias "Lunes" en el periodo de "9:00" a "12:00" horas para la actividad "Primeros auxilios"
