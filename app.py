
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Mi Aplicación Flask</h1><p>Bienvenido a mi proyecto</p>'


if __name__ == '__main__':
    app.run(debug=True)