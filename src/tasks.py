"""Operações básicas de gerenciamento de tarefas."""

tasks = []
next_id = 1

VALID_STATUSES = {"A Fazer", "Em Progresso", "Concluído"}
VALID_PRIORITIES = {"Baixa", "Média", "Alta"}


def reset_tasks():
    """Limpa os dados em memória. Útil para os testes automatizados."""
    global tasks, next_id
    tasks = []
    next_id = 1


def create_task(title, description="", priority="Média"):
    """Cria uma tarefa depois de validar os campos recebidos."""
    global next_id
    title = title.strip()
    if not title:
        raise ValueError("O título da tarefa é obrigatório.")
    if priority not in VALID_PRIORITIES:
        raise ValueError("Prioridade inválida.")

    task = {
        "id": next_id,
        "title": title,
        "description": description.strip(),
        "priority": priority,
        "status": "A Fazer",
    }
    tasks.append(task)
    next_id += 1
    return task


def list_tasks():
    """Retorna todas as tarefas cadastradas."""
    return tasks.copy()


def get_task(task_id):
    """Procura uma tarefa pelo identificador."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(task_id, title, description, priority, status):
    """Atualiza os dados de uma tarefa existente."""
    task = get_task(task_id)
    if task is None:
        return None
    title = title.strip()
    if not title:
        raise ValueError("O título da tarefa é obrigatório.")
    if priority not in VALID_PRIORITIES:
        raise ValueError("Prioridade inválida.")
    if status not in VALID_STATUSES:
        raise ValueError("Status inválido.")

    task.update({
        "title": title,
        "description": description.strip(),
        "priority": priority,
        "status": status,
    })
    return task


def delete_task(task_id):
    """Exclui uma tarefa. Retorna True se ela existia."""
    task = get_task(task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True
