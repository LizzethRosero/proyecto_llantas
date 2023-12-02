from flask import render_template
from . import errores


@errores.errorhandler(404)
def page_not_found(error):
    return (render_template("error.html", error="Página no encontrada..."),404)
    # return render_template("error.html", error=error.description), 404