# Utiliser une image de base avec Python et OpenJDK
FROM openjdk:8-jdk-slim

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier Spark dans le conteneur
COPY spark-3.5.3-bin-hadoop3.tgz /opt/spark-3.5.3-bin-hadoop3.tgz

# Extraire Spark et le déplacer dans /opt/spark
RUN tar -xvzf /opt/spark-3.5.3-bin-hadoop3.tgz -C /opt \
    && mv /opt/spark-3.5.3-bin-hadoop3 /opt/spark \
    && rm /opt/spark-3.5.3-bin-hadoop3.tgz

# Configurer les variables d'environnement pour Spark
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY requirements.txt .
COPY backend_api.py .

# Installer les dépendances Python
RUN pip3 install -r requirements.txt

# Copier le modèle entraîné
COPY random_forest_model /app/random_forest_model

# Exposer le port 5000 pour l'API Flask
EXPOSE 5000

# Commande pour démarrer l'API Flask
CMD ["python3", "backend_api.py"]