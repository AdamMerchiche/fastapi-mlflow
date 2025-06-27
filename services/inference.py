"""Machine Learning Service Module"""
import pandas as pd
from schemas import InferenceIn

from .model import get_model

def make_prediction(inference_data: InferenceIn): 
    """Predict the species based on input data"""
    input_df = pd.DataFrame(inference_data.model_dump(mode='python'))
    input_df = input_df.rename(
        columns = {
            "sepal_length": "sepal length (cm)",
            "sepal_width":"sepal width (cm)",
            "petal_length":"petal length (cm)",
            "pepal_width":"petal width (cm)"
        }
    )
    model = get_model()
    prediction = model.predict(input_df)
    return prediction.tolist()[0]
