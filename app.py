# Import necessary libraries
from flask import Flask, request, render_template, jsonify  # Pour gérer les requêtes, templates et JSON
from utils import model_predict  # Importer la fonction de prédiction

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Charger la page HTML principale depuis templates/

@app.route('/predict', methods=['POST'])  # Utiliser la méthode POST pour soumettre les données
def predict():
    """
    Handles form submission and returns prediction.
    """
    email = request.form.get('email')  # Récupérer les données du formulaire
    
    if not email:  
        return render_template("index.html", error="Veuillez entrer un email.")  # Gérer l'erreur

    prediction = model_predict(email)  # Faire la prédiction
    return render_template("index.html", email=email, prediction=prediction)  # Retourner les résultats

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])  
def predict_api():
    """
    API endpoint that accepts a JSON payload and returns a prediction.
    """
    try:
        data = request.get_json()  # Extraire le JSON envoyé par le client
        email = data.get("email")  # Récupérer l'email de la requête
        
        if not email:  
            return jsonify({'error': 'Email requis'}), 400  # Retourner une erreur JSON si vide

        prediction = model_predict(email)  
        return jsonify({'email': email, 'prediction': prediction})  # Retourner la réponse JSON

    except Exception as e:  # Gérer les erreurs
        return jsonify({'error': str(e)}), 400  

if __name__ == "__main__":
    print("Démarrage du serveur Flask...")  # Message de log
    app.run(host="0.0.0.0", port=5000, debug=True)