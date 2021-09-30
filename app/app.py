from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
import pymongo
import json

app = Flask(__name__)
app.config['DEBUG'] = False
api = Api(app)
data = os.environ.get('MI_DATA', 'Result:')
#url_db = os.environ.get('URL_DB')
#usuario = os.environ.get('user')
#passwd = os.environ.get('pass')

#myclient = pymongo.MongoClient(url_db,username=usuario,password=passwd)
#mydb = myclient["db_dc"]
#mycol = mydb["clientes"]


def checkdata(postedData):

    estate = 200
	
    if not request.json:
        estate = int(302)
        return estate
	
    if "x" not in postedData or "y" not in postedData:
        estate = int(301)
        return estate
    elif "x" not in postedData and "y" not in postedData:
        estate = int(301)
        return estate
    else:
        a = postedData["x"]
        b = postedData["y"]

        if not type(a) == int:
            estate = 301
            return estate

        if not type(b) == int:
            estate = 301
            return estate

    return estate

"""
class Mongo(Resource):
    def post(self):
        postedData = request.get_json()
        nom = postedData["Nombre"]
        eda = postedData["Edad"]
        mydict = {"name": nom, "Edad:": eda}
        x = mycol.insert(mydict)
        
        retMap = {
            'Mongo return': 'ok inserto',
            'Status code': 200
        }
        return jsonify(retMap)
"""

class Add(Resource):
    def post(self):

        # Step 1 get posted data
        retJson = {}
        errore = "Error de datos"
        mess = "Error con los datos recibidos"
        postedData = request.get_json()
        # Step 1 valid los data
        status_code = checkdata(postedData)
        #print(status_code)
        if status_code == 301:
            retMap = {
                'Resultado': errore,
                'Status code': 301
            }
        elif status_code == 302:
            retMap = {
                'Resultado': "Noes un json",
                'Status code': 302
            }
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = x
            y = y

            # Step 2 Add the posted data
            ret = x + y
            retMap = {
                data + ':': ret,
                'Status code': 200
            }

        return jsonify(retMap)


class Subtract(Resource):
    def post(self):

        # Step 1 get posted data
        retJson = {}
        mess = "Error con los datos recibidos"
        postedData = request.get_json()
        # Step 1 valid los data
        status_code = checkdata(postedData)
        if status_code != 200:
            retJson = {
                'Message': mess,
                'Status ': status_code
            }
            retMap = jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)

            # Step 2 Add the posted data
            ret = x - y
            retMap = {
                data + ':': ret,
                'Status code': 200
            }
            return jsonify(retMap)


api.add_resource(Add, '/add')
#api.add_resource(Mongo, '/mongo')
api.add_resource(Subtract, '/subtract')


@app.route('/add_two_num', methods=["POST"])
def add_two_num():
    dataDict = request.get_json()
    if "y" not in dataDict:
        return "Error", 305

    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y
    retJson = {"z": z}
    return jsonify(retJson)


@app.route("/")
def hello_world():
    return "Hello, World!", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')

# curl -X POST -H "Content-Type: application/json" -d '{"x": 2, "y": 7}' http://127.0.0.1:5000/add
# https://blog.entirely.digital/docker-gunicorn-and-flask/
