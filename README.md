# rest-python - Exemplo de API REST em Python

O que é REST? Um pouco de Teoria [aqui](rest.md)

Para este projeto, vou usar o [VSCode](https://code.visualstudio.com/) em Windows. Se voce está usando outro sistema operacional ou outro editor de texto, os comandos podem ser ligeiramente diferentes.

Assumindo que o [Python](https://www.python.org/) já está instalado, vamos criar o projeto e iniciar instalando a biblioteca [Flask](https://flask.palletsprojects.com/en/stable/).

No terminal:

```shell
mkdir rest-python
cd rest-python
python -m venv venv
.\venv\Scripts\activate
echo "rest-python Exemplo de API REST em Python" > readme.md
git init
git add .
git commit -m "chore: create project folder
```

## 1. SERVIDOR

Agora vamos criar um servidor em Python usando a biblioteca Flask:

```shell
pip install flask
```

vamos criar o arquivo server.py:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Todo List!"

if __name__ == "__main__":
    app.run(debug=True)
```

Para executar o servidor, digite no terminal ```python server.py```, se tudo deu certo verá a mensagem ```Running on http://127.0.0.1:5000``` indicando que o servidor está no ar. Abra seu navegador na página http://localhost:5000 e verá a mensagem **Hello, Todo List!**.

## 2. API REST

    Um pouco de teoria: se quiser saber mais sobre REST, escrevi uma breve explicação sobre o que é REST e quais são as principais requisições, pode ser lido [aqui](rest.md).

A API que vamos criar será para manipular uma lista simples de tarefas, e disponibilizará os serviços para criar, atualizar, remover e listar as tarefas da lista de tarefas.

Método HTTP|API endpoint|Funcionalidade
---|---|---
POST|/task|Cria uma nova tarefa.
GET|/task|Obtém a lista de tarefas
GET|/task/<task_id>|Obtém uma tarefa específica.
DELETE|/task/<task_id>|Exclui uma tarefa específica.


## 3. Cria uma nova tarefa.

Vamos iniciar criando um contador para numerar as novas tarefas, será o ID da tarefa e será usado para operações específicas nesta tarefa, por exemplo, excluí-la. Ele será acessado através da função *get_new_ID()*.

E vamos utilizar o objeto *request* do Flask para recuperar os dados enviados no corpo da requisição, e o objeto *jsonify* para formatar a resposta como um *json*.

incluir em *server.py*:

```python
from flask import request, jsonify

tasks = []  # Lista para armazenar as tarefas
task_id_control = 1  # Controlador de IDs para garantir unicidade

@app.route("/task", methods=["POST"])
def create_task():
    # pega dados da requisicao
    data = request.get_json()
    # cria nova tarefa incompleta
    new_task = {
        "id": get_new_ID(),
        "title": data.get("title",""),
        "done": data.get("done","False")=="True"
    }
    tasks.append(new_task)  # Adiciona a nova tarefa à lista
    return jsonify({"message": "Tarefa criada com sucesso!", "task": new_task}), 201

```

A rotina **create_task()**, associada ao endpoint **/task** através de uma requisição **POST**, pega os dados do objeto *json* anexado na requisição e cria uma nova entrada no repositório de tarefas, identificando o título, o estado da tarefa e atribuindo ao ID o valor retornado pela função *get_new_ID()*. Note que se não existirem na requisição, serão adotados os valores ```""``` e ```False``` respectivamente para as propriedades **title** e **done** no objeto enviado. A função então retorna o [Código de Status de Resposta HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status) 201 indicando que a requisição foi bem sucedida e um novo recurso foi criado como resultado.

Para testar, utilizamos a ferramenta **CURL** no terminal:
```shell
curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"build payments list\"}" http://127.0.0.1:5000/task
```

obtendo como resposta:
```json
{
  "message": "Tarefa criada com sucesso!",
  "task": {
    "done": false,
    "id": 1,
    "title": "build payments list"
  }
}
```

Testamos ainda os valores padrão mandando mais requisições sem as propriedades *title* e *done* definidas:

```shell
curl -X POST -H "Content-Type: application/json" -d "{\"done\":\"True\"}" http://127.0.0.1:5000/task
{
  "message": "Tarefa criada com sucesso!",
  "task": {
    "done": "True",
    "id": 2,
    "title": "No title"
  }
}

curl -X POST -H "Content-Type: application/json" -d "{}" http://127.0.0.1:5000/task
{
  "message": "Tarefa criada com sucesso!",
  "task": {
    "done": "False",
    "id": 3,
    "title": "No title"
  }
}
```

## 4. Lista as tarefas ou tarefa específica

Vamos criar as pesquisas de tarefas, criando as funções **list_task()** e **list_all_tasks()**, retornando os dados de uma tarefa específica e os dados de todas as tarefas respectivamente. Para retornar uam única tafera, será necessário identificá-la através do ID.

```python
# retorna todas as tarefas
@app.route("/task", methods=["GET"])
def get_task():
    return jsonify({"total": len(tasks), "tasks": tasks}), 200


# retorna tarefa especifica
@app.route("/task/<int:task_id>", methods=["GET"])
def get_tasks(task_id):
    # busca tarefa pelo ID
    task = [t for t in tasks if t["id"] == task_id]
    if task:
        return jsonify(task)
    return jsonify({"message": "Tarefa não existe"}), 404
```

Para testar os retorno, no terminal:

```shell
curl -H "Content-Type: application/json" http://127.0.0.1:5000/task
{
  "tasks": [
    {
      "done": "False",
      "id": 1,
      "title": "build payments list"
    },
    {
      "done": "True",
      "id": 2,
      "title": "No title"
    },
    {
      "done": "False",
      "id": 3,
      "title": "No title"
    }
  ],
  "total": 3
}

curl -H "Content-Type: application/json" http://127.0.0.1:5000/task/2
[
  {
    "done": "True",
    "id": 2,
    "title": "No title"
  }
]

curl -H "Content-Type: application/json" http://127.0.0.1:5000/task/6
{
  "message": "Tarefa n\u00e3o existe"
}
```

## 5. Client HTML

Vamos criar uma [página em HTML](client.html) para facilitar os testes da API. É uma página simples, pode ser executada diretamente no browser.

Mas para não dar erro de CORS, vamos adicionar no *server.py* o uso da biblioteca *flask_cors*, e acrescentar o decorador ```@cross_origin()``` em cada endpoint.
```python
from flask_cors import CORS, cross_origin
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

# retorna todas as tarefas
@app.route("/task", methods=["GET"])
@cross_origin()
def get_task():
    return jsonify({"total": len(tasks), "tasks": tasks}), 200
```


