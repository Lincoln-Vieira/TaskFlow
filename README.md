# TaskFlow — Sistema de Gerenciamento de Tarefas

## 1. Objetivo

O TaskFlow é uma aplicação web acadêmica que simula o gerenciamento de tarefas de uma equipe. Permite cadastrar, listar, editar e excluir tarefas, além de acompanhar status e prioridade.

## 2. Escopo inicial

- Cadastro de tarefas com título, descrição e prioridade.
- Listagem das tarefas cadastradas.
- Edição do conteúdo, prioridade e status.
- Exclusão de tarefas.
- Testes automatizados e integração contínua com GitHub Actions.

## 3. Tecnologias

- Python e Flask: aplicação web.
- Pytest: execução dos testes automatizados.
- Ruff: verificação estática básica do código.
- Git e GitHub: versionamento e colaboração.
- GitHub Actions: automação dos testes e da verificação de qualidade.

## 4. Metodologia

Será utilizado Kanban para visualizar o trabalho nas colunas **A Fazer**, **Em Progresso** e **Concluído**. As tarefas serão pequenas, priorizadas e movimentadas conforme o avanço. O GitHub Projects será utilizado para acompanhar o quadro.

## 5. Como executar localmente

Requer Python 3.10 ou superior.

1. Crie e ative um ambiente virtual.
2. Instale as dependências:
   `pip install -r requirements.txt`
3. Inicie o sistema:
   `python src/app.py`
4. Abra `http://127.0.0.1:5000` no navegador.

### Executar os testes

Na pasta raiz do projeto, execute:
`python -m pytest -v`

### Verificar a qualidade do código

`ruff check src tests`

## 6. Estrutura de pastas

- `src/`: aplicação e regras de tarefas.
- `src/templates/`: página HTML.
- `tests/`: testes automatizados.
- `docs/`: documentação e diagramas.
- `.github/workflows/`: pipeline de integração contínua.

## 7. Limitações da versão acadêmica

Nesta primeira versão, as tarefas ficam armazenadas em memória. Isso significa que elas são apagadas quando a aplicação é reiniciada. A versão demonstra o CRUD básico, mas não utiliza banco de dados nem autenticação de usuários.

## 8. Mudança de escopo simulada

**Escopo inicial:** cadastrar, listar, editar e excluir tarefas, utilizando título e descrição.

**Mudança de escopo:** adicionar prioridades (Baixa, Média e Alta) e permitir a atualização do status das tarefas (A Fazer, Em Progresso e Concluído).

**Justificativa:** o cliente fictício precisa acompanhar o andamento das tarefas e identificar quais são mais urgentes. A mudança amplia o sistema inicial e facilita a organização do trabalho da equipe.

**Implementação:** a versão atual do TaskFlow já inclui as funcionalidades de prioridade e status. Para documentar a mudança no GitHub, será criado um card específico no Projects e um commit relacionado à implementação, registrando o desenvolvimento de forma coerente com o histórico do projeto.

## 9. UML

Os diagramas de casos de uso e de classes estão na pasta `docs/`.

## 10. Evidências a incluir na entrega

- Captura do quadro GitHub Projects com pelo menos 10 cards.
- Capturas de commits relevantes (mínimo de 10 commits).
- Captura do workflow do GitHub Actions concluído com sucesso.
- Capturas comentadas no documento teórico.

## 11. Situação do projeto

Este repositório é um projeto acadêmico demonstrativo. Antes da entrega, execute os testes, confirme o workflow no GitHub e substitua ou complemente as evidências com capturas reais do seu repositório.
