from flask import Flask

# Esto indica que este es el módulo principal
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/hello')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>')
def hello(name=None, age=None):
    if name is None and age is None:
        return f'<h1>Hello my friend</h1>'
    elif age is None:
        return f'<h1>Hello {name}</h1>'
    else:
        return f'<h1>Hello {name} - {age}</h1>'
