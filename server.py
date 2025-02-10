from flask import Flask, request, jsonify

# cria uma nova instancia do Flask
app = Flask(__name__)

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
    print(jsonify({"data":data}))
    # cria nova tarefa incompleta
    new_task = {
        "id": get_new_ID(),
        "title": data.get("title","No title"),
        "done": data.get("done","False")
    }
    tasks.append(new_task)  # Adiciona a nova tarefa à lista
    print(tasks)
    return jsonify({"message": "Tarefa criada com sucesso!", "task": new_task}), 201


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

# executa o servidor
if __name__ == "__main__":
    app.run(debug=True)