from flask import Flask
from .catalogo import catalogo
from .inicio import inicio
from .carrito import carrito
from .cuenta import cuenta
from .errores import errores

app = Flask(__name__)
app.secret_key="1234"
app.config.from_pyfile('config/configuracion.cfg')
app.register_blueprint(catalogo)
app.register_blueprint(inicio)
app.register_blueprint(carrito)
app.register_blueprint(cuenta)
app.register_blueprint(errores)
