from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd

import pickle

from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

# import ridge regression and standard scaler
ridge_model=pickle.load(open("models/ridge.pkl","rb"))
Standard_Scaler=pickle.load(open("models/scaler.pkl","rb"))



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictData",methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        temp = float(request.form['Temperature'])
        rh = float(request.form['RH'])
        ws = float(request.form['Ws'])
        rain = float(request.form['Rain'])
        ffmc = float(request.form['FFMC'])
        dmc = float(request.form['DMC'])
        isi = float(request.form['ISI'])
        classes = float(request.form['Classes'])   # ✅ cast safely
        region = float(request.form['Region'])     # ✅ cast safely

        input_data = np.array([[temp, rh, ws, rain, ffmc, dmc, isi, classes, region]])
        new_data_scaled = Standard_Scaler.transform(input_data)

        result=ridge_model.predict(new_data_scaled)
        return render_template("home.html",results=result[0])

    else:
        return render_template("home.html")


if __name__=="__main__":
    app.run(host="0.0.0.0")
