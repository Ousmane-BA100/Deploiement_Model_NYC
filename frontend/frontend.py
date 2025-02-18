import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# Configuration de l'interface Streamlit
st.title("NYC Yellow Taxi Riding Prediction")
st.markdown("### Prédiction du nombre de passagers pour les trajets de taxi à NYC.")

# Carte interactive pour sélectionner un emplacement
st.header("Choose a Pick-Up Place")
m = folium.Map(location=[40.730610, -73.935242], zoom_start=12)  # NYC par défaut
folium.Marker([40.730610, -73.935242], popup="Pick-Up Point").add_to(m)
output = st_folium(m, width=700, height=500)

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
        response = requests.post("http://backend:5000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            st.success(f"Nombre prédit de passagers : {round(prediction, 2)}")
        else:
            st.error(f"Erreur lors de la prédiction : {response.json()['error']}")
    except Exception as e:
        st.error(f"Erreur de connexion à l'API : {str(e)}")