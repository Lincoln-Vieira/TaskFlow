# Diagrama UML — Classes

```mermaid
classDiagram
    class Task {
        +int id
        +str title
        +str description
        +str priority
        +str status
    }

    class TasksModule {
        +create_task(title, description, priority)
        +list_tasks()
        +get_task(task_id)
        +update_task(task_id, title, description, priority, status)
        +delete_task(task_id)
    }

    class WebApp {
        +index()
        +add_task()
        +edit_task(task_id)
        +remove_task(task_id)
    }

    WebApp --> TasksModule : utiliza
    TasksModule --> Task : gerencia
```

![Diagrama UML de classes](diagrama-de-classes.png)

**Observação:** o diagrama representa conceitualmente a estrutura e as responsabilidades do sistema. `Task` representa os dados de uma tarefa, armazenados como dicionário no código Python. `TasksModule` representa o módulo `tasks.py`, responsável pelas operações de gerenciamento, e `WebApp` representa as rotas e funções da aplicação Flask.
