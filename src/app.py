"""Aplicação web TaskFlow usando Flask."""

from flask import Flask, redirect, render_template, request, url_for
from tasks import (
    VALID_PRIORITIES,
    VALID_STATUSES,
    create_task,
    delete_task,
    list_tasks,
    update_task,
)

app = Flask(__name__)


@app.get("/")
def index():
    """Exibe as tarefas cadastradas."""
    return render_template(
        "index.html",
        tasks=list_tasks(),
        statuses=VALID_STATUSES,
    )


@app.post("/tasks")
def add_task():
    """Recebe o formulário e cadastra uma tarefa."""
    try:
        create_task(
            request.form.get("title", ""),
            request.form.get("description", ""),
            request.form.get("priority", "Média"),
        )
    except ValueError as error:
        return str(error), 400
    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/update")
def edit_task(task_id):
    """Atualiza os campos de uma tarefa."""
    try:
        task = update_task(
            task_id,
            request.form.get("title", ""),
            request.form.get("description", ""),
            request.form.get("priority", ""),
            request.form.get("status", ""),
        )
    except ValueError as error:
        return str(error), 400
    if task is None:
        return "Tarefa não encontrada.", 404
    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/delete")
def remove_task(task_id):
    """Exclui uma tarefa."""
    if not delete_task(task_id):
        return "Tarefa não encontrada.", 404
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
