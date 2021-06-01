from flask import Flask,jsonify,render_template,request,url_for,json,redirect
from medical_expert_system import sistemita
from flask_googletrans import translator
import os.path
import os
import json
import time

app = Flask(__name__)
ts = translator(app)

@app.route("/")
def hello_world():
    if os.path.exists('gen/data.txt'):
        return redirect(url_for('test'))

    return render_template('index.html')



@app.route('/receiver', methods = ['POST'])
def getDatod():
    if request.method == "POST":
        #obtenemos los datos del usario
        data = request.form.get('javascript_data')
        nelson  = json.loads(data)
        #llamar la clase experta
        sistemita(nelson)
        
        resul = ''
    return resul

@app.route('/extra')
def test():
    while not os.path.exists('gen/data.txt'):
        time.sleep(1)
    if os.path.exists('gen/data.txt'):
        with open('gen/data.txt') as json_file:
            datos = json.load(json_file)
            for p in datos['data']:
                titulo = p['Title']
                subt = p['subtitle']
                desarrollo = p['info']
                trata =p['end']
        os.remove('gen/data.txt')       
        return render_template('result.html',titulo=titulo,subt=subt,desarrollo=desarrollo,trata=trata)
    else:
         raise ValueError("%s isn't a file! 'gen/data.txt'")
  