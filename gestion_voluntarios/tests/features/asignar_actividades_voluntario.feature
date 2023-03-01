# Created by nicol at 27/2/2023
# language: es
  Característica: Asignación de voluntarios a actividades
    Como administrador del personal médico,
    quiero que se asignen voluntarios a las actividades,
    para atender una emergencia.

    Esquema del escenario: : Asignar un voluntario a una actividad en una emergencia
      #Dado: precondiciones
      Dado que se tiene una emergencia con "<nombre_emergencia>" que aún no es atendida
      Y hay un voluntario con "<nombre_voluntario>", "<apellido_voluntario>" y "<edad_voluntario>" que asistirá sin actividades asignadas
      Y existe una actividad con "<nombre_actividad>" sin voluntarios asignados
      #Cuando: eventos
      Cuando se le asigna un voluntario a una actividad
      #Entonces: resultados
      Entonces el estado de voluntario sera "<es_asignado>"
      Y el estado de la actividad sera "<tiene_voluntario>"
      Y el estado de la emergencia sera "<estado_emergencia>"

      Ejemplos: Asignaciones
      | nombre_emergencia | nombre_voluntario | apellido_voluntario | edad_voluntario | nombre_actividad | es_asignado | tiene_voluntario | estado_emergencia |
      | "Choque"          | "Alexis"          | "Vizuete"           | 23              | "Suturar"        | 1           | 1                | 1                 |
      # | "Choque"          | "Anahi "          | "Vasquez"           | 22              | "Suturar"        | 1           | 1                | 1                 |
