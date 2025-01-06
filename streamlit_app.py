import streamlit as st
import numpy as np
import pickle


with open('models/xgboost_best_model.pkl','rb') as file:
    model = pickle.load(file)

st.title("XGBoost Prediction App")
st.write("Provide input data to get predictions")

st.sidebar.header("Input Parameters")

def user_input_features():
    import streamlit as st
    import numpy as np
    
    CPU_Cores = st.sidebar.slider("CPU Cores", 2, 64, 16)  # Updated range and default
    RAM_GB = st.sidebar.slider("RAM (GB)", 4, 256, 64)  # Updated range and default
    GPU_Available = st.sidebar.selectbox("GPU Available", [0, 1], index=1)  # Unchanged
    GPU_VRAM_GB = st.sidebar.slider("GPU VRAM (GB)", 0, 48, 16)  # Updated range and default
    Disk_Speed_MBps = st.sidebar.slider("Disk Speed (MBps)", 100.0, 5000.0, 1800.0)  # Updated range and default
    Dataset_Size_MB = st.sidebar.slider("Dataset Size (MB)", 0.1, 20000.0, 7546.0)  # Updated range and default
    Num_Features = st.sidebar.slider("Number of Features", 1, 2000, 755)  # Updated range and default
    Model_Complexity = st.sidebar.slider("Model Complexity", 1.0, 150.0, 40.5)  # Updated range and default
    CV_Folds = st.sidebar.slider("Cross-Validation Folds", 3, 10, 5)  # Updated range and default
    
    data = {
        "CPU_Cores": CPU_Cores,
        "RAM_GB": RAM_GB,
        "GPU_Available": GPU_Available,
        "GPU_VRAM_GB": GPU_VRAM_GB,
        "Disk_Speed_MBps": Disk_Speed_MBps,
        "Dataset_Size_MB": Dataset_Size_MB,
        "Num_Features": Num_Features,
        "Model_Complexity": Model_Complexity,
        "CV_Folds": CV_Folds,
    }
    return np.array([v for v in data.values()]).reshape(1, -1)


input_features = user_input_features()

if st.button("Predict"):
    prediction_in_seconds = model.predict(input_features)[0]
    prediction_in_minutes = prediction_in_seconds / 60

    st.write(f"### Prediction: {prediction_in_seconds:.2f} seconds")
    st.write(f"### Approx: {prediction_in_minutes:.2f} minutes")

st.write("---")



