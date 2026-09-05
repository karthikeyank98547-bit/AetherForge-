from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.linear_model import LogisticRegression
app=FastAPI(title='AetherForge ML Service',version='1.0.0')
X=np.array([[1,50,0.1,1000],[2,55,.2,900],[3,60,.35,800],[4,66,.55,650],[5,72,.7,450],[6,78,.88,250]],dtype=float)
y=np.array([0,0,0,1,1,1])
model=LogisticRegression().fit(X,y)
class Features(BaseModel):
    vibration:float
    temperature:float
    anomaly_score:float
    rul_hours:float
@app.get('/health')
def health(): return {'status':'UP','model_version':'sklearn-logistic-v1'}
@app.post('/predict')
def predict(f:Features):
    x=np.array([[f.vibration,f.temperature,f.anomaly_score,f.rul_hours]],dtype=float)
    p=float(model.predict_proba(x)[0,1]); return {'failure_probability':p,'model_version':'sklearn-logistic-v1','explanation':'Probability produced by the synthetic training pipeline from vibration, temperature, anomaly score and RUL features.'}
