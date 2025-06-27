""" App Main"""

from typing import Union
import pandas as pd
from fastapi import FastAPI, File, UploadFile
import mlflow 
import io 
import uvicorn

from api import inference_router, home_page

from core import config

app = FastAPI(
    title=config.APP_NAME, 
    description=config.APP_DESCRIPTION, 
    version=config.APP_VERSION
)

app.include_router(inference_router)
app.include_router(home_page)

if __name__ == '__main__': 
    #On veut lancer la app qui est dans le fichier main, reload c'est pour prendre les modifs, 
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


"""
#On va predict sur un fichier qu'on va penser en entrée. Donc il faut 
#importer UploadFile
@app.post("/predict")
async def get_predict(file: UploadFile): 
    contents = await file.read()
    buffer = io.BytesIO(contents)
    mlflow.set_tracking_uri(uri="http://127.0.0.1:5001")

    #  On récupère la dernière version du modèle importé sur MLFLOW dans notre registry name
    version = mlflow.search_model_versions(filter_string=f"name='{"TRACKING_RF_FINAL"}'")[0].version
    print("VERSION", version)
    model = mlflow.pyfunc.load_model(model_uri=f'models:/{"TRACKING_RF_FINAL"}/{version}')
    df = pd.read_parquet(buffer)
    Xtest = df.iloc[:, :-1]
    return model.predict(Xtest).tolist()"""
