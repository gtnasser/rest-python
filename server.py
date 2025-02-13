""" Simple Python Flask REST API Server"""

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# cria uma nova instancia do Flask
app = Flask(__name__)

# habilitar CORS
# CORS(app, resources={r"/api/*": {"origins": "http://example.com"}})
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

# repositorio das tarefas
tasks = []

# contador, armazena o último ID utilizado
task_curr_ID = 0
def get_new_ID():
    global task_curr_ID
    task_curr_ID += 1
    return task_curr_ID


# rotas disponiveis na API
@app.route("/")
def hello():
    return "Hello Todo List!"


# cria uma nova tarefa
@app.route("/task", methods=["POST"])
def create_task():
    # pega dados da requisicao
    data = request.get_json()
    print('# create_task(): received:', data)
    # cria nova tarefa incompleta
    new_task = {
        "id": get_new_ID(),
        "title": data.get("title",""),
        "done": str(data.get("done","False")).lower()=="true"
    }
    tasks.append(new_task)  # Adiciona a nova tarefa à lista
    print('## tasks[]=', tasks)
    return jsonify({"message": "Tarefa criada com sucesso!", "task": new_task}), 201


# retorna todas as tarefas
@app.route("/task", methods=["GET"])
@cross_origin()
def get_task():
    return jsonify({"total": len(tasks), "tasks": tasks}), 200


# retorna tarefa especifica
@app.route("/task/<int:task_id>", methods=["GET"])
def get_tasks(task_id):
    # busca tarefa pelo ID
    task = [t for t in tasks if t["id"] == task_id]
    if task:
        return jsonify({"task": task[0]}), 200
    return jsonify({"message": "Tarefa não existe"}), 404


# atualiza tarefa específica
@app.route("/task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    # busca tarefa pelo ID
    task = [t for t in tasks if t["id"] == task_id]
    if not task:
        return jsonify({"message": "Tarefa não existe"}), 404

    data = request.get_json()
    # atualiza os campos da tarefa com os dados se enviados
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify({"message": "Tarefa atualizada!", "task": task})



# executa o servidor
if __name__ == "__main__":
    app.run(debug=True)