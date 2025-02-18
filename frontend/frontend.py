import streamlit as st
import requests

# Configuration de l'interface Streamlit
st.title("NYC Yellow Taxi Riding Prediction")
st.markdown("### Prédiction du nombre de passagers pour les trajets de taxi à NYC.")

# Entrées utilisateur : caractéristiques
st.subheader("Paramètres d'entrée")
hour = st.slider("Heure (0-23)", min_value=0, max_value=23, value=12, step=1)
is_business_day = st.selectbox("Jour ouvré ?", [1, 0], help="1 pour oui, 0 pour non")
weather_index = st.selectbox("Conditions météo", [0, 1], format_func=lambda x: "Clear" if x == 0 else "Rainy")
temp_avg = st.slider("Température moyenne (°C)", min_value=-10, max_value=40, value=20)
distance_category_index = st.selectbox("Catégorie de distance", [0, 1], format_func=lambda x: "Short" if x == 0 else "Long")

# Bouton pour prédire
if st.button("Prédire le nombre de passagers"):
    # Préparer les données d'entrée
    input_data = {
        "hour": hour,
        "is_business_day": is_business_day,
        "weather_index": weather_index,
        "temp_avg": temp_avg,
        "distance_category_index": distance_category_index
    }

    # Envoyer les données à l'API Flask
    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            st.success(f"Nombre prédit de passagers : {round(prediction, 2)}")
        else:
            st.error(f"Erreur lors de la prédiction : {response.json()['error']}")
    except Exception as e:
        st.error(f"Erreur de connexion à l'API : {str(e)}")