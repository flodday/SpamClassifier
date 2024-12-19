import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Charger les données depuis le fichier CSV
data = pd.read_csv('spam.csv', encoding='latin-1')

# Nettoyer les données (sélectionner les colonnes nécessaires)
data = data[['label', 'message']]
data.columns = ['label', 'message']

# Prétraiter les messages
def preprocess_text(text):
    if isinstance(text, str):  # Vérifier si le texte est une chaîne de caractères
        text = text.lower()  # Convertir en minuscule
        text = re.sub(r'\W', ' ', text)  # Enlever les caractères non alphabétiques
        text = re.sub(r'\s+', ' ', text)  # Remplacer les espaces multiples par un seul
    else:
        text = ''  # Si ce n'est pas une chaîne, on retourne une chaîne vide
    return text


data['cleaned_message'] = data['message'].apply(preprocess_text)

# Séparer les données en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data['cleaned_message'], data['label'], test_size=0.2, random_state=42)

# Transformer les messages en vecteurs de caractéristiques
vectorizer = CountVectorizer(stop_words='english')
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Entraîner le modèle Naive Bayes
model = MultinomialNB()
model.fit(X_train_vect, y_train)

# Évaluer le modèle
accuracy = model.score(X_test_vect, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Sauvegarder le modèle et le vectoriseur dans des fichiers pickle
with open('spam_classifier_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Modèle et vectoriseur sauvegardés avec succès.")
