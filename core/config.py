"""Configuration module for FastAPI application"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    """Configuration settings for the FastAPI application"""
    MLFLOW_TRACKING_URI: str = "http://localhost:5000"
    MLFLOW_MODEL_URI: str = "models:/TRACKING_RF_FINAL/1"


    APP_NAME : str = "FastAPI MLFLOW App"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Descritpion"

    # Tout le contenu du fichier .env est injecté dans les variables d'environnement
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8'
    )
config = Config()