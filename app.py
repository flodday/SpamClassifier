from flask import Flask, request, jsonify
import pickle
import re

# Charger le modèle et le vectoriseur sauvegardés
with open('spam_classifier_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Créer l'application Flask
app = Flask(__name__)

# Fonction de prétraitement
def preprocess_text(text):
    if isinstance(text, str):
        text = text.lower()  # Convertir en minuscule
        text = re.sub(r'\W', ' ', text)  # Enlever les caractères non alphabétiques
        text = re.sub(r'\s+', ' ', text)  # Remplacer les espaces multiples par un seul
    else:
        text = ''  # Si ce n'est pas une chaîne, on retourne une chaîne vide
    return text

# Endpoint pour tester un message
@app.route('/check', methods=['GET'])
def check_message():
    message = request.args.get('message')
    if message:
        # Prétraiter le message
        cleaned_message = preprocess_text(message)
        
        # Transformer le message en vecteur
        message_vect = vectorizer.transform([cleaned_message])
        
        # Prédire si le message est spam ou ham
        prediction = model.predict(message_vect)
        
        # Retourner la réponse
        result = {"resp": prediction[0] == "spam"}
        return jsonify(result), 200
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
