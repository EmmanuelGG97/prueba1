from flask import Flask, request
import json
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not "registro" in request.form:
            dicc=respuestaToJson('no','no salio bien')
            return json.dumps(dicc)
        print(request.form['registro'])
        dicc=respuestaToJson('ok','operacion exitosa')
        return json.dumps(dicc)
    else:
        return 'aqui no hay nada'

def respuestaToJson(operacion,texto):
    dicc=    {
                'operacion': operacion,
                'texto': texto
            }
    return dicc

if __name__ =='__main__':
    app.run(port='5000', debug=True)


    