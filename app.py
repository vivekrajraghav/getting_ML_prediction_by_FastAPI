from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input_validation import UserInput
from schema.prediction_reponse import PredictionResponse
from model.predict import ModelVersion, prediction_output,model

app=FastAPI()

@app.get("/")
def home():
    return {"message":"This is the home page of this API"}

@app.get("/health")
def health_check():
    return {
        "status":"OK",
        "version":ModelVersion,
        "model_loaded":model is not None
    }

@app.post("/predict",response_model=PredictionResponse)
def predict_premium(data:UserInput):
    user_input={
        "bmi":data.bmi,
        "age_group":data.age_group,
        "lifestyle_risk":data.lifestyle_risk,
        "city_tier":data.city_tier,
        "income_lpa":data.income_lpa,
        "occupation":data.occupation
    }

    try:
        prediction=prediction_output(user_input)
        return JSONResponse(status_code=200,content={"response":prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
    