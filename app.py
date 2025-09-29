from flask import Flask, request, render_template
import numpy as np 
import pandas as pd
###
from sklearn.preprocessing import StandardScaler 
from src.pipeline.prediction_pipeline import CustomeData, PredictPipeline

# application = Flask(__name__)
# app = application

app = Flask(__name__) 

# Home Page 
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
    else:
        # get the data 
        data = CustomeData(
            gender = request.form.get("gender"),
            race_ethnicity = request.form.get('ethnicity'),
            parental_level_of_education = request.form.get("parental_level_of_education"),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        # turn data into df 
        df = data.get_data_as_DataFrame()
        # use predict pipeline 
        predict_pipeleine = PredictPipeline()
        results = predict_pipeleine.predict(df)
        # return homepage with result 
        return render_template("home.html", results=results[0])

if __name__ == "__main__":
    app.run(debug=False, port="0.0.0.0", host=5000)
