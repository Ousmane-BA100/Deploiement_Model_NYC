from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml.regression import RandomForestRegressionModel
from pyspark.ml.feature import VectorAssembler

# Initialisation de Flask et Spark
app = Flask(__name__)
spark = SparkSession.builder \
    .appName("TaxiPredictionAPI") \
    .config("spark.ui.enabled", "false") \
    .getOrCreate()

# Charger le modèle PySpark
model_path = "/app/random_forest_model"  # Assurez-vous que ce chemin est correct dans le conteneur Docker
try:
    model = RandomForestRegressionModel.load(model_path)
    print(f"Modèle chargé depuis {model_path}")
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")

# Définir la route de base
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the NYC Taxi Prediction API! Use the /predict endpoint for predictions."

# Endpoint pour effectuer une prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données envoyées dans le corps de la requête
        data = request.json  # Exemple : {"hour": 10, "is_business_day": 1, ...}
        if not data:
            return jsonify({"error": "Invalid input. JSON with features is required."}), 400
        
        # Convertir les données en DataFrame Spark
        features = [data]  # Convertir en liste pour Spark
        df = spark.createDataFrame(features)

        # Vectoriser les colonnes nécessaires
        assembler = VectorAssembler(
            inputCols=["hour", "is_business_day", "weather_index", "temp_avg", "distance_category_index"],
            outputCol="features"
        )
        df = assembler.transform(df)

        # Faire une prédiction
        predictions = model.transform(df)
        prediction = predictions.collect()[0]['prediction']

        # Retourner la réponse JSON
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Point d'entrée de l'application
if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(host="0.0.0.0", port=5000, debug=False)  # Désactiver le mode debug