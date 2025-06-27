"""APIs for inference operations"""

from fastapi import APIRouter

from schemas import InferenceIn, InferenceOut

from services import make_prediction

inference_router = APIRouter(prefix='/inference', tags=['Inference Operations'])

@inference_router.post("/predict", response_model=InferenceOut)
async def predict(inference_data: InferenceIn)-> InferenceOut: 
    """Endpoint for making predictions based on input data"""
    preds = make_prediction(inference_data)
    return InferenceOut(species=preds) 