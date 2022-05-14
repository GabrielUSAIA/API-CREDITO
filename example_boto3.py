from urllib import response
import boto3
import joblib
from sklearn import pipeline
import os

#client = boto3.client('s3', 'us-east-1')
s3 = boto3.resource('s3', 'us-east-1')
s3.meta.client.download_file('german-credit-model-2022', 'models/pipeline1.joblib','pipeline1.joblib')
s3.meta.client.download_file('german-credit-model-2022', 'models/model01.joblib','model01.joblib')
transformer = joblib.load('pipeline1.joblib')
model = joblib.load('model01.joblib')

print(model.predict_proba(transformer.transform([['male', 23, 200, 'own']])))
#print(transformer)

os.remove('pipeline1.joblib')
os.remove('model01.joblib')
#obj= client.get_object(Bucket='german-credit-model-2022', Key='models/pipeline1.joblib')

#transformer = joblib(obj['Body'.read()])

#response = client.list_buckets()

#print(response)