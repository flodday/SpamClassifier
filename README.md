# python -m venv venv 
 permet de créer un environnement 

# pip install flask scikit-learn pandas
Flask pour créer l'API web.
scikit-learn pour entraîner le modèle de classification.
pandas pour la gestion des données (si tu utilises un fichier CSV).

# ajout contenu dans app.py
# pip freeze > requirements.txt
pour enregistrer les dépendances installées dans un environnement virtuel

# création de train_model.py
modèle d'entrainement pour entrainer le jeu de données comme spam.csv

# tests/test_app.py
écrire des tests unitaires de l'API.

# pip install pytest
exécute les tests

# entrainement et sauvegarde du modèle 
PS C:\Users\flori\OneDrive\Bureau\spampython> python train_model.py
Accuracy: 50.00%
Modèle et vectoriseur sauvegardés avec succès.

# mettre un point d'API avec Flask
pip install flask

# création app.py
contient l'API Flask

# tester l'API
pip install pytest requests

# création test_app.py 
permet de tester

# python app.py
pour tester l'api

# puis ouvrir le navigateur 
http://127.0.0.1:5000/check?message=Hello%20World
Si ham
{
  "resp": false
}
Si spam
{
  "resp": true
}