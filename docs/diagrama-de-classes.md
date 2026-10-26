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

**Observação:** o diagrama apresenta os conceitos e as responsabilidades do sistema. `TasksModule` representa o módulo `tasks.py`, que contém as funções de gerenciamento das tarefas. `WebApp` representa conceitualmente a aplicação web.
