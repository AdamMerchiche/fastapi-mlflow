"""Load MLFlow model"""

import mlflow 
from core import config

# mlflow.set_tracking_uri("") -- plus besoin de l'utiliser car il est inscrit en variable par défaut


def get_model(model_name: str, model_version: int=1): 
    """Load a model from MLFlow"""
    return mlflow.pyfunc.load_model(model_uri=config.MLFLOW_MODEL_URI)