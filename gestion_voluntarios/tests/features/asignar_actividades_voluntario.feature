# Created by nicol at 27/2/2023
# language: es
  Característica: Asignación de actividades a voluntarios
    Como administrador del personal médico,
    quiero que se asignen actividades a los voluntarios,
    para atender una emergencia.

    Esquema del escenario: : Asignar una actividad a un voluntario en una emergencia
      #Dado: precondiciones
      Dado que se tiene una emergencia con "<nombre_emergencia>" que aún no es atendida
      Y hay un voluntario con "<nombre_voluntario>", "<apellido_voluntario>" y "<edad_voluntario>" que asistirá sin actividades asignadas
      Y existe una actividad con "<nombre_actividad>"
      #Cuando: eventos
      Cuando se les asigna al menos una actividad diferente a cada voluntario
      #Entonces: resultados (los procesos se desarrollan a partir del evento)
      Entonces el estado de la emergencia sera "<estado_emergencia>"
      Y estado de voluntario sera "<tiene_actividad>"
      Y el estado de la actividad sera "<es_asignada>"

      Ejemplos: Asignaciones
      | nombre_emergencia | nombre_voluntario | apellido_voluntario | edad_voluntario | nombre_actividad | estado_emergencia | tiene_actividad | es_asignada |
      | "Choque"          | "Alexis"          | "Vizuete"           | 23              | "Suturar"        | 1                 | 1               | 1           |
      | "Choque"          | "Anahi "          | "Vasquez"           | 22              | "Suturar"        | 1                 | 1               | 1           |



