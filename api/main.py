from fastapi import FastAPI
from pydantic import BaseModel
import joblib # type: ignore
import numpy as np

app = FastAPI()

# Cargar modelo entrenado
model = joblib.load("models/model.pkl")

# Definir esquema de entrada
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.post("/predict")
def predict(data: DiabetesInput):
    input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure,
                            data.SkinThickness, data.Insulin, data.BMI,
                            data.DiabetesPedigreeFunction, data.Age]])
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}
