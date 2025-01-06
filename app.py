from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

with open('models/xgboost_best_model.pkl','rb') as file:
    model = pickle.load(file)

app = FastAPI()

class ModelInput(BaseModel):
    CPU_Cores: int
    RAM_GB: int
    GPU_Available: int
    GPU_VRAM_GB: int
    Disk_Speed_MBps: float
    Dataset_Size_MB: int
    Num_Features: int
    Model_Complexity: float
    CV_Folds: int

@app.post("/predict")
def predict(input_data: ModelInput):
    input_array = np.array([
        input_data.CPU_Cores,
        input_data.RAM_GB,
        input_data.GPU_Available,
        input_data.GPU_VRAM_GB,
        input_data.Disk_Speed_MBps,
        input_data.Dataset_Size_MB,
        input_data.Num_Features,
        input_data.Model_Complexity,
        input_data.CV_Folds
    ]).reshape(1, -1)

    prediction = model.predict(input_array)

    return {"prediction": prediction.tolist()}