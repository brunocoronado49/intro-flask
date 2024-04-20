from flask import Flask

# Esto indica que este es el módulo principal
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'
