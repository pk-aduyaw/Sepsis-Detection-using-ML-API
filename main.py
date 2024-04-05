from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib


# Initialize application
app = FastAPI()

# Define parameters for prediction
class patient_info(BaseModel):
    ID : str
    PRG : int
    PL : int
    PR : int
    SK : int
    TS : int
    M11 : float
    BD2 : float
    Age : int
    Insurance : int

# Load Machine Learning Models
GradientBoosting_model = joblib.load('./models/gradientBoosting_model.joblib')

RandomForest_model = joblib.load('./models/randomForest_model.joblib')

SVC_model = joblib.load('./models/svc_model.joblib')

# Load LabelEncoder
label_encoder = joblib.load('./models/labelEncoder.joblib')

# Set index page
@app.get('/')
def home():
    return {'message' : 'This is a Sepsis Prediction API'}

# Define gradient boosting prediction endpoint
@app.post('/gradient_boosting_predict')
def gb_prediction(data: patient_info):
    # Dump the input values into a dataframe
    features = pd.DataFrame([data.model_dump()])

    # Make prediction with gradient boosting model
    prediction = GradientBoosting_model.predict(features)

    # Select prediction value
    prediction = int(prediction[0])

    # Inverse transform the predicted value
    prediction_label = label_encoder.inverse_transform([prediction])[0]

    # Get prediction probabily
    prediction_proba = GradientBoosting_model.predict_proba(features)
    
    return {
        'prediction': prediction_label,
        'probability': prediction_proba
    }


# Define random forest prediction endpoint
@app.post('/random_forest_predict')
def rf_prediction(data: patient_info):
    # Dump the input values into a dataframe
    features = pd.DataFrame([data.model_dump()])

    # Make prediction with random forest model
    prediction = RandomForest_model.predict(features)

    # Select prediction value
    prediction = int(prediction[0])

    # Inverse transform the predicted value
    prediction_label = label_encoder.inverse_transform([prediction])[0]

    # Get prediction probabily
    prediction_proba = RandomForest_model.predict_proba(features)

    return {
        'prediction': prediction_label,
        'probability': prediction_proba
    }


# Define svc prediction endpoint
@app.post('/svc_predict')
def svc_prediction(data: patient_info):
    # Dump the input values into a dataframe
    features = pd.DataFrame([data.model_dump()])

    # Make prediction with svc model
    prediction = SVC_model.predict(features)

    # Select prediction value
    prediction = int(prediction[0])

    # Inverse transform the predicted value
    prediction_label = label_encoder.inverse_transform([prediction])[0]

    # Get prediction probabily
    prediction_proba = SVC_model.predict_proba(features)

    return {
        'prediction': prediction_label,
        'probability': prediction_proba
    }


