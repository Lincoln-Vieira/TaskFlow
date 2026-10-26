"""Testes automatizados das operações e rotas do TaskFlow."""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import tasks
from app import app


class TaskFunctionsTests(unittest.TestCase):
    def setUp(self):
        tasks.reset_tasks()

    def test_create_task(self):
        task = tasks.create_task("Estudar Python", "Revisar Flask", "Alta")
        self.assertEqual(task["title"], "Estudar Python")
        self.assertEqual(task["status"], "A Fazer")

    def test_title_is_required(self):
        with self.assertRaises(ValueError):
            tasks.create_task("   ")

    def test_list_tasks(self):
        tasks.create_task("Tarefa A")
        self.assertEqual(len(tasks.list_tasks()), 1)

    def test_update_task(self):
        task = tasks.create_task("Título antigo")
        updated = tasks.update_task(task["id"], "Título novo", "Descrição", "Baixa", "Em Progresso")
        self.assertEqual(updated["title"], "Título novo")
        self.assertEqual(updated["status"], "Em Progresso")

    def test_delete_task(self):
        task = tasks.create_task("Remover")
        self.assertTrue(tasks.delete_task(task["id"]))
        self.assertEqual(tasks.list_tasks(), [])

    def test_invalid_priority_is_rejected(self):
        with self.assertRaises(ValueError):
            tasks.create_task("Tarefa", priority="Urgente")


class TaskRoutesTests(unittest.TestCase):
    def setUp(self):
        tasks.reset_tasks()
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TaskFlow", response.data)

    def test_create_task_route(self):
        response = self.client.post("/tasks", data={"title": "Nova tarefa", "priority": "Média"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(tasks.list_tasks()), 1)

    def test_blank_title_returns_error(self):
        response = self.client.post("/tasks", data={"title": "   "})
        self.assertEqual(response.status_code, 400)

    def test_delete_missing_task_returns_404(self):
        response = self.client.post("/tasks/999/delete")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
