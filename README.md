```markdown
# 🚖 NYC Yellow Taxi Riding Prediction

Ce projet permet de prédire le nombre de passagers pour les trajets de taxi à New York en utilisant un modèle de régression Random Forest entraîné avec PySpark.  
L'application est composée d'un **backend (API Flask) 🖥️** et d'un **frontend (Streamlit) 🎨**.

---

## 📌 Table des matières

1. [🔧 Prérequis](#prérequis)
2. [📂 Structure du projet](#structure-du-projet)
3. [📥 Installation](#installation)
4. [🚀 Exécution](#exécution)
5. [🖱️ Utilisation](#utilisation)
6. [📡 API Endpoints](#api-endpoints)
7. [🛠️ Technologies utilisées](#technologies-utilisées)
8. [👨‍💻 Auteurs](#auteurs)

---

## 🔧 Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- 🐳 **Docker** : Pour exécuter les conteneurs.
- 🛠️ **Docker Compose** : Pour gérer les services multi-conteneurs.
- 🔗 **Git** : Pour cloner le dépôt.

---

## 📂 Structure du projet

Le projet est structuré comme suit :

```
project/
├── backend/
│   ├── Dockerfile 📄
│   ├── backend_api.py 🖥️
│   ├── requirements.txt 📜
│   ├── spark-3.5.3-bin-hadoop3.tgz 📦  # Fichier Spark
│   └── random_forest_model/ 📁  # Dossier contenant le modèle
├── frontend/
│   ├── Dockerfile 📄
│   ├── frontend.py 🎨
│   └── requirements.txt 📜
└── docker-compose.yml ⚙️
```

🚨 **Ajoutez le fichier lourd dans `.gitignore` pour éviter de le pousser sur GitHub** :  

📜 **Fichier `.gitignore`** :
```
backend/spark-3.5.3-bin-hadoop3.tgz
```

---

## 📥 Installation

1. **Cloner le dépôt** 🛎️ :
   ```bash
   git clone https://github.com/votre-utilisateur/NYC-Yellow-Taxi-Riding-Prediction.git
   cd NYC-Yellow-Taxi-Riding-Prediction
   ```

2. **Construire les images Docker** 🏗️ :
   - Le fichier `spark-3.5.3-bin-hadoop3.tgz` est inclus dans le dossier `backend`.
   - Exécutez la commande suivante pour construire les images :
     ```bash
     docker-compose build
     ```

---

## 🚀 Exécution

1. **Démarrer les conteneurs** 🏁 :
   ```bash
   docker-compose up
   ```

2. **Accéder aux services** 🌐 :
   - **Backend (API Flask) 🖥️** : `http://127.0.0.1:5000`
   - **Frontend (Streamlit) 🎨** : `http://127.0.0.1:8501`

---

## 🖱️ Utilisation

1. **Ouvrir l'interface Streamlit** :
   - Accédez à `http://127.0.0.1:8501` dans votre navigateur.
   - Saisissez les caractéristiques du trajet (heure, jour ouvré, météo, etc.).
   - Cliquez sur "Prédire le nombre de passagers" pour obtenir la prédiction.

2. **Utiliser l'API Flask directement** :
   - Envoyez une requête **POST** à `http://127.0.0.1:5000/predict` avec un corps JSON :
     ```json
     {
       "hour": 10,
       "is_business_day": 1,
       "weather_index": 0,
       "temp_avg": 20,
       "distance_category_index": 1
     }
     ```
   - Exemple de réponse :
     ```json
     {
       "prediction": 12.34
     }
     ```

---

## 📡 API Endpoints

- **GET `/`** : Page d'accueil de l'API.
  - Réponse : `"Welcome to the NYC Taxi Prediction API! Use the /predict endpoint for predictions."`

- **POST `/predict`** : Effectue une prédiction en fonction des caractéristiques du trajet.
  - Corps de la requête (JSON) :
    ```json
    {
      "hour": 10,
      "is_business_day": 1,
      "weather_index": 0,
      "temp_avg": 20,
      "distance_category_index": 1
    }
    ```
  - Réponse (JSON) :
    ```json
    {
      "prediction": 12.34
    }
    ```

---

## 🛠️ Technologies utilisées

- **Backend** :
  - Flask (Python) 🐍 : API REST
  - PySpark ⚡ : Modèle de prédiction
  - Docker 🐳 : Conteneurisation

- **Frontend** :
  - Streamlit 🎨 : Interface utilisateur
  - Docker 🐳 : Conteneurisation

- **Autres** :
  - Git 🔗 : Versionnement du code
  - Docker Compose ⚙️ : Gestion des services multi-conteneurs

---

## 👨‍💻 Auteurs

- **Myrem** 👩‍💻 : Développeur principal
- **Ines** 👩‍💻 : Développeur principal
- **Ousmane BA** 👨‍💻 : Développeur principal

---

## 📜 Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## ❗ Remarques

- Assurez-vous que le fichier `spark-3.5.3-bin-hadoop3.tgz` est bien dans le dossier `backend`.
- Si vous utilisez **Git LFS** pour les fichiers volumineux, configurez-le correctement.

---

## 🤝 Contribuer

Les contributions sont **les bienvenues** ! 🚀 Pour contribuer :

1. **Forkez** le projet 🍴.
2. **Créez** une branche (`git checkout -b feature/NouvelleFonctionnalité`).
3. **Committez** vos modifications (`git commit -m "Ajout d'une nouvelle fonctionnalité"`).
4. **Poussez** vers la branche (`git push origin feature/NouvelleFonctionnalité`).
5. **Ouvrez** une **Pull Request** 📬.

---

## ❓ Questions ou problèmes ?

Si vous avez des questions, ouvrez une **issue** sur GitHub ou contactez-moi 📩 à [bousmane733@gmail.com](mailto:bousmane733@gmail.com).
```
