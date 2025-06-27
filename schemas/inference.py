""" Inference schema module"""

from pydantic import BaseModel

class InferenceIn(BaseModel): 
    """Schema for inference input data -> Format des données en entrée attendues"""
    
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class InferenceOut(BaseModel): 
    """Scema for inference output data -> format du retour de notre modèle"""
    species: str