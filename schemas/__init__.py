# On pourra faire les importations à partir de ce dossier directement, grace à ce fichier d
# Dans schemas, on aura tout ce qui concerne fast api (application, structure...) + les donnees que l'application nous ramène 
"""Manage app schemas"""

# En faisant ça, on pourra importer ces classes dans d'autres modules simplement en faisant from schemas import InferenceIn.... au lieu de from schema.inference import ...
#from .user import UserIn, UserOut, UserUpdate
from .inference import InferenceIn, InferenceOut