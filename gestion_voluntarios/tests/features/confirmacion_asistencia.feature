# Created by Cris at 2/23/2023
  # language: es
Característica: Registro de emergencias
  Como supervisor
  Quiero verificar si un voluntario ha atendido un número específico de emergencias
  Para asegurarme de que están cumpliendo con sus obligaciones

  Escenario: Verificar número de emergencias atendidas por un voluntario
    Dado que hay un voluntario registrado con el ID "{faker.uuid4}"
    Y este voluntario ha atendido "{faker.random_int(min=1, max=10)}" emergencias confirmadas
    Y se ha asignado al voluntario una nueva emergencia con el ID "{faker.uuid4}"
    Cuando el voluntario accede a la emergencia "{faker.uuid4}"
    Y la confirma
    Entonces debería ver que ha atendido "{faker.random_int(min=2, max=11)}" emergencias confirmadas

  Escenario: Verificar rechazo de emergencia asignada
    Dado que hay un voluntario registrado con el ID "{faker.uuid4}"
    Y este voluntario ha atendido "{faker.random_int(min=1, max=10)}" emergencias confirmadas
    Y se ha asignado al voluntario una nueva emergencia con el ID "{faker.uuid4}"
    Cuando el voluntario accede a la emergencia "{faker.uuid4}"
    Y la rechaza
    Entonces debería ver que sigue habiendo "{faker.random_int(min=1, max=10)}" emergencias confirmadas atendidas por el voluntario


