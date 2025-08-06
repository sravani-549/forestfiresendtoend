from flask import Flask,request,render_template,jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

ridgereg=pickle.load(open('MODELS/ridge2.pkl','rb'))
stdscaler=pickle.load(open('MODELS/scaler2.pkl','rb'))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata",methods=("POST","GET"))
def predict_datapoint():
    if request.method=="POST":
        Temperature=float(request.form.get("Temperature"))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        new_data_scaled=stdscaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridgereg.predict(new_data_scaled)
        return render_template("home.html",result=result[0])
    else:
        return render_template("home.html")
if __name__=="__main__":
    app.run(host="0.0.0.0")