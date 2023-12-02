# Utilisez une image Python de base
FROM python:3.8-slim

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY . .

# Installez les dépendances Python
RUN pip install schedule

# Exécutez votre script principal lors du démarrage du conteneur
CMD ["python", "main.py"]
