from flask import Flask,jsonify,render_template,request,url_for,json
from medical_expert_system import sistemita

app = Flask(__name__)

@app.route("/")
def hello_world():
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


  