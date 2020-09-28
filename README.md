# API_JIRA
El objetivo del sistema es la creación de tareas y asignación de las mismas a un
usuario.
- Un usuario Administrador puede administrar a otros usuarios, asignandoles un
tipo, administrador o responsable.
- Un usuario Administrador podrá crear tareas y asignar a cada tarea un
responsable de efectuar esa tarea.
- Los usuarios responsables podrán ver solamente las tareas que le hayan sido
asignadas..
- Una tarea puede estar en uno de tres posibles estados. Solamente el usuario
responsable puede actualizar la tarea a uno de los siguientes estados:
    - Por hacer (estado default)
    - Haciendo
    - Hecho
    
**Se requiere:**
- CRUD de usuarios y tareas
- Autenticación de usuarios (administrador y usuarios normales)
- Reportes:
    - Los usuarios responsables de tareas pueden ver un resumen de las tareas
asignadas según su estado, es decir, total de número de tareas por hacer,
total haciendo y total hechas.
    - El administrador podrá ver cuántas tareas hay en cada estado sin importar
el responsable.
    - El administrador puede ver el avance global del proyecto como un
porcentaje de tareas resueltas sobre el total de tareas (tareas en estado por
hacer y haciendo vs tareas en estado Hecho).

Un usuario tipo responsable no debe tener acceso a información de otros usuarios ni
reportes que no le corresponde