from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline   

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Extract form data
        data = CustomData(
            gender=request.form['gender'],
            ethnicity=request.form['ethnicity'],
            parental_level_of_education=request.form['parental_level_of_education'],
            lunch=request.form['lunch'],
            test_preparation_course=request.form['test_preparation_course'],
            writing_score=float(request.form['writing_score']),
            reading_score=float(request.form['reading_score'])
        )
        # Convert data to DataFrame
        pred_df = data.get_data_as_dataframe()

        # Make prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Pass results to the template
        return render_template('main.html', results=results[0])

    # For GET requests, render the page without results
    return render_template('main.html', results=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

