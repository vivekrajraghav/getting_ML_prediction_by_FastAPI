import pickle
import pandas as pd

with open("model/model.pkl","rb") as f:
    model=pickle.load(f)

ModelVersion="1.0.0"

class_labels=model.classes_.tolist()
def prediction_output(user_input:dict):
    df=pd.DataFrame([user_input])
    predicted_classes=model.predict(df)[0]
    probabilities=model.predict_proba(df)[0]
    confidence=max(probabilities)
    class_prob=dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))
    return {
        "predicted_category":predicted_classes,
        "confidence":confidence,
        "class_probabalities":class_prob
    }