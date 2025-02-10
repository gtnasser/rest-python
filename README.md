# rest-python - Exemplo de API REST em Python

    OBS: Vou usar o VSCode em Windows, se voce está usando outro sistema operacional ou outro editor de texto, os comandos podem ser ligeiramente diferentes.

Assumindo que o Python já está instalado, vamso criar o projeto e iniciar instalando a biblioteca Flask.

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
