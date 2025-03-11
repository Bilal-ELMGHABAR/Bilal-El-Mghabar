import pickle
import numpy as np

def load_model():
    """
    Loads the trained model from file.
    """
    with open("models/model.pkl", "rb") as file:  
        model = pickle.load(file)   # Hint: Use pickle to load the model
    return model

def model_predict(features):
    """
    Predicts using the loaded model.
    """
    model = load_model()  # Charger le modèle avant la prédiction
    prediction = model.predict([features])  # Utilisation de la méthode predict()
    # Si le mail est spam, renvoyer 1, sinon -1
    prediction = 1 if prediction[0] == 1 else -1 
    return prediction 