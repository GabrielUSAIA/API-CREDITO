#import string
from fastapi import FastAPI, Request, Form
import numpy as np
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
from sklearn import pipeline
import uvicorn
import boto3
import os

app =FastAPI()

s3 = boto3.resource('s3', 'us-east-1')
s3.meta.client.download_file('german-credit-model-2022', 'models/pipeline1.joblib','pipeline1.joblib')
s3.meta.client.download_file('german-credit-model-2022', 'models/model01.joblib','model01.joblib')
transformer = joblib.load('pipeline1.joblib')
model = joblib.load('model01.joblib')

@app.post("/predict")
async def predcit(sexo :str=Form(...), 
            edad: int=Form(...), 
            monto: int=Form(...),
            vivienda: str=Form(...)):

    X = transformer.transform([[sexo, edad, monto, vivienda]])
    prob_bad_client = model.predict_proba(X)[0][1]
    return {"prob_bad_client": prob_bad_client}

os.remove('pipeline1.joblib')
os.remove('model01.joblib')