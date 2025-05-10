from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Initialiser l'application FastAPI
app = FastAPI()

# Charger le modèle
model = joblib.load('music_recommender.joblib')

# Définir la structure des données attendues
class UserInput(BaseModel):
    age: int
    gender: int

# Définir le point de terminaison pour la prédiction
@app.post('/predict')
def predict(user_input: UserInput):
    prediction = model.predict([[user_input.age, user_input.gender]])
    return {'genre': prediction[0]}
