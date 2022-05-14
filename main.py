#import string
from fastapi import FastAPI, Request, Form
import numpy as np
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
from sklearn import pipeline
import uvicorn

app =FastAPI()
model= joblib.load("Models/model01.joblib")
pipeline= joblib.load("Models/pipeline1.joblib")

@app.post("/predict")
async def predcit(sexo :str=Form(...), 
            edad: int=Form(...), 
            monto: int=Form(...),
            vivienda: str=Form(...)):

    X = pipeline.transform([[sexo, edad, monto, vivienda]])
    prob_bad_client = model.predict_proba(X)[0][1]
    return {"prob_bad_client": prob_bad_client}