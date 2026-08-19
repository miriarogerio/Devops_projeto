 
Projeto DevOps (CodeFactory Solutions)

## 📋 Descrição do projeto
API REST simples para gerenciamento de tarefas (to-do list), desenvolvida como parte da Atividade Prática de DevOps e Integração Contínua do Centro Universitário Internacional Uninter. O projeto simula a adoção da Cultura DevOps por uma software house fictícia, a CodeFactory Solutions, demonstrando na prática o uso de versionamento com Git/GitHub, containerização com Docker e automação com CI (GitHub Actions).

## 🎯 Objetivo
Demonstrar como a adoção de práticas DevOps (versionamento estruturado, containerização e integração contínua) resolve problemas reais de um time de desenvolvimento, como atrasos nas entregas, dificuldade de integração de código e demora na configuração de ambientes.

## 🛠️ Tecnologias utilizadas
Python 3.12
Flask — framework web
SQLAlchemy — ORM
PostgreSQL — banco de dados
Docker / Docker Compose — containerização
GitHub Actions — pipeline de integração contínua
Pytest — testes automatizados

## 💻 Funcionalidades

- [ ] Atribuir tarefas 
- [ ] excluir ou alterar informações diarias
- [ ] Define prazos e lembretes
- [ ] Estabelece prioridades
- [ ] Acompanha o progresso


📁 Estrutura de pastas
todo-api/
├── app/
│   ├── __init__.py
│   ├── main.py         # rotas da API
│   ├── models.py       # modelo da tabela Task
│   └── config.py        # configuração do banco
├── tests/
│   └── test_tasks.py    # testes automatizados
├── .github/
│   └── workflows/
│       └── ci.yml        # pipeline de CI
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## ⚙️ Instruções de instalação
Opção 1 — Rodando com Docker (recomendado)
git clone https://github.com/<seu-usuario>/todo-api.git
cd todo-api
docker-compose up --build
A API ficará disponível em http://localhost:5000.

Opção 2 — Rodando localmente sem Docker
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
Nesse caso, é necessário ter um PostgreSQL rodando localmente e ajustar a variável de ambiente DATABASE_URL no arquivo app/config.py.

## ▶️ Instruções de execução
Com os containers rodando, use os endpoints abaixo (via Postman, Insomnia ou curl):

Método	Rota	Descrição
GET	/	Verifica se a API está no ar
GET	/tasks	Lista todas as tarefas
GET	/tasks/<id>	Busca uma tarefa específica
POST	/tasks	Cria uma nova tarefa
PUT	/tasks/<id>	Atualiza uma tarefa
PATCH	/tasks/<id>/complete	Marca tarefa como concluída
DELETE	/tasks/<id>	Remove uma tarefa
Exemplo de criação de tarefa
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar DevOps", "description": "Revisar branches e merges"}'
🧪 Rodando os testes
pytest -v
🐳 Por que utilizar containers neste projeto?
O uso do Docker garante que qualquer novo integrante da equipe consiga rodar a aplicação e o banco de dados com um único comando, sem precisar instalar Python, PostgreSQL ou configurar variáveis manualmente. Isso resolve diretamente o problema relatado pela CodeFactory Solutions, em que novos colaboradores levavam muito tempo para configurar seus ambientes de desenvolvimento. Além disso, os containers garantem que o ambiente de desenvolvimento seja idêntico ao de produção, eliminando o clássico problema de "na minha máquina funciona".

# 📄 Licença
Este projeto está licenciado sob a licença MIT — veja o arquivo LICENSE para mais detalhes.

👥 Equipe

Bruno Sampaio Sobreira — RU: 5217388
Guilherme Santos Silva — RU: 4603410
Miria Rogerio Mangueira da Silva — RU: 5152333


