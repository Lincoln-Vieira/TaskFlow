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

O projeto utiliza Kanban para organizar e acompanhar as atividades nas colunas **A Fazer**, **Em Progresso** e **Concluído**. As tarefas são organizadas em cards no GitHub Projects e movimentadas conforme o andamento do desenvolvimento.

## Links do projeto

- **Repositório GitHub:** https://github.com/Lincoln-Vieira/TaskFlow
- **Quadro Kanban (GitHub Projects):** https://github.com/users/Lincoln-Vieira/projects/3/views/1
- **Integração contínua (GitHub Actions):** https://github.com/Lincoln-Vieira/TaskFlow/actions

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

**Escopo inicial:** desenvolver um sistema básico de gerenciamento de tarefas com cadastro, listagem, edição e exclusão, incluindo título, descrição, prioridade e status.

**Mudança de escopo:** melhorar a apresentação visual das tarefas, utilizando etiquetas coloridas para destacar as prioridades (Baixa, Média e Alta) e os status (A Fazer, Em Progresso e Concluído), além de organizar as tarefas em cartões.

**Justificativa:** o cliente fictício identificou a necessidade de visualizar rapidamente a urgência e o andamento das atividades. A melhoria facilita a leitura das informações e torna a utilização do sistema mais organizada.

**Implementação:** a melhoria visual foi registrada no commit `c711ec1`, com a mensagem `style: melhora o visual do TaskFlow`. As funcionalidades de prioridade e status já faziam parte da implementação anterior; a mudança documentada corresponde à forma como essas informações são apresentadas na interface.

**Acompanhamento no Kanban:** a melhoria visual está registrada no GitHub Projects como uma atividade do projeto. O quadro é utilizado para acompanhar as tarefas concluídas e as etapas que ainda estão em andamento.

## 9. UML

Os diagramas de casos de uso e de classes estão na pasta `docs/`.

## 10. Evidências da entrega

As evidências do desenvolvimento estão organizadas na pasta `docs/` e incluem:

- Captura do quadro Kanban do GitHub Projects.
- Captura da execução do GitHub Actions concluída com sucesso.
- Histórico de commits do repositório.
- Imagens dos diagramas UML de casos de uso e de classes.

## 11. Situação do projeto

O TaskFlow é um projeto acadêmico desenvolvido com Python e Flask. A aplicação possui operações de cadastro, listagem, edição e exclusão de tarefas, com prioridade e status.

Os testes automatizados e a verificação de qualidade foram executados localmente com sucesso. A integração contínua também apresentou uma execução bem-sucedida no GitHub Actions.

O projeto continua utilizando armazenamento em memória, sem banco de dados ou autenticação de usuários.
