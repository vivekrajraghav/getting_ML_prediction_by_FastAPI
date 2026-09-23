from pydantic import BaseModel,Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category:str=Field(...,description="The prediction from the model",examples=["High"])
    confidence:float=Field(...,description="Model's confidence score for the predicted class(from 0 to 1)",examples=[0.8123])
    class_probabalities:Dict[str,float]=Field(...,description="Probabilities of the all possible classes",examples=[{"Low":0.01,"Medium":0.15,"High":0.84}])

