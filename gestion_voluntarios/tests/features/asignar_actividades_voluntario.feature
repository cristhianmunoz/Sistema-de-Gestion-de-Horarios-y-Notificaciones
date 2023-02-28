# Created by nicol at 27/2/2023
# language: es
  Característica: Asignación de actividades a voluntarios
    Como administrador del personal médico, quiero que se asignen actividades a los voluntarios para atender una emergencia.

    Escenario: Asignar una actividad a un grupo de voluntarios en una emergencia
      #Dado: precondiciones
      Dado que se tiene una emergencia que aún no es atendida
      Y hay un grupo de voluntarios que asistirán sin actividades asignadas
      #Cuando: eventos
      Cuando se les asigna al menos una actividad a cada voluntario
      #Entonces: resultados (los procesos se desarrollan a partir del evento)
      Entonces la emergencia será atendida




