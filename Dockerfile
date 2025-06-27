FROM python:3.9-slim

#Set working directory
WORKDIR /app

# Copy requirement file - from ... to 
COPY requirements.txt .

#Install dependencies 
RUN pip install -r requirements.txt

# On copie du dossier courant au dossier app = workdir mentionne au dessus
COPY . . 

#Expose the port FastAPII will run on 
EXPOSE 5000

# command to run the application -- on specifie le nombre de workers en fonction des performances que nous visons
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "3"]

# docker build -t fastapi-mflow .  (. car dockerfile est dans notre dossier courant, et on ajoute le tag)
# On peut ajouter dans le docker run -e .env NOM IMAGE
# permettra de passer les elements de configs / variables


# Apres, il faut prendre l'id de l'image, et trouver l'adresse du conteneur avec docker inspect 472e4008f2af
#Pour rentrer dans un docker container, docker run -it NOM IMAGE 
# Dès qu'on sort du conteneur, il s'efface 