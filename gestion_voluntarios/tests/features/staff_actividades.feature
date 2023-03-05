# Created by Dan at 02/03/2023
# language: es

Característica: Asignar staff médico a una actividad
  Como administrador del personal médico deseo gestionar los horarios del personal para así organizar
  la atención de pacientes y determinar tiempos críticos faltantes

  Escenario: El administrador del personal médico desea asignar a un staff médico a una actividad regular
    Dado que tengo un miembro del staff médico llamado "Alberto" disponible los días "martes" y "jueves" de "10:00" a "14:00"
    Y hay una actividad regular de "primeros auxilios" los días "martes" y "jueves" de "12:00" a "13:00" en "enfermería"
    Cuando el administrador del personal médico asigna a Alberto para "primeros auxilios" los días "martes" y "jueves" en "enfermería"
    Entonces el sistema actualiza automáticamente el horario de Alberto
    Y "Alberto" recibe una notificación sobre su participación en la actividad regular de "primeros auxilios" los días "martes" y "jueves" en "enfermería"