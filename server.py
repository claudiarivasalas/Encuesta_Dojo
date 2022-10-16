from encuesta_dojo_app import app
from encuesta_dojo_app.controllers import controlador
app.secret_key = "estessecreto"


if __name__=="__main__":
    app.run(debug=True)