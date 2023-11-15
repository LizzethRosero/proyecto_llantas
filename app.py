from flask import Flask, render_template

app = Flask(__name__)
# pagina inicial
@app.route('/')
def inicio():
   return render_template('inicio.html')


@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/marcas/michelin')
def michelin():
   return render_template('michelin.html')


@app.errorhandler(404)
def page_not_found(error):
    return (render_template("error.html", error="Página no encontrada..."),
            404)
    # return render_template("error.html", error=error.description), 404


if __name__ == '__main__':
 app.run(port=5000,debug=True)
