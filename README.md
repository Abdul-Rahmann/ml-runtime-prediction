# ML Runtime Prediction

Predict the training runtime of machine learning models based on machine specifications, dataset characteristics, and model complexity.

## Overview

This project addresses a common challenge in machine learning workflows: estimating the time it takes to train a model. By predicting runtimes, users can better allocate resources, assess feasibility, and optimize model-building processes.

The solution is built using:
- A synthetic dataset simulating real-world scenarios.
- **XGBoost**, which achieved 95% R² on the test set.
- REST APIs for predictions (using **FastAPI**).
- A user-friendly GUI for visualization (using **Streamlit**).

## Features
1. **Synthetic Dataset Generation**
   - Machine specs: CPU cores, RAM size, disk speed.
   - Dataset properties: Dataset size, number of features.
   - Model properties: Complexity, cross-validation folds.

2. **Model Performance**
   - Train R²: 96%
   - Test R²: 95%

3. **Deployment**
   - FastAPI for REST APIs.
   - Streamlit for GUI-based predictions.

## Installation

### Prerequisites
- Python 3.10 or higher
- `git` installed

### Steps
1. Clone the repository: 
```bash
git clone https://github.com/yourusername/ml-runtime-prediction.git
cd ml-runtime-prediction
```

2.	Install dependencies:

```bash
pip install -r requirements.txt
```

3.	Run the FastAPI server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

4.	Start the Streamlit interface:
```bash
streamlit run streamlit_app.py
```


#### Usage

FastAPI
	- Access the API at http://127.0.0.1:8000/docs.
	- Submit a JSON payload with model, dataset, and machine specs for runtime predictions.

Streamlit
	- Open the Streamlit interface to input specs via a GUI and visualize predictions.

#### Dataset

The dataset simulates:
	- Machine configurations: CPU cores, RAM, and disk speed.
	- Dataset size and features.
	- Model complexities and cross-validation parameters.

Example Prediction

Input
```bash
{
  "cpu_cores": 4,
  "ram_size": 16,
  "disk_speed": 7200,
  "dataset_size": 50000,
  "num_features": 100,
  "model_complexity": "high",
  "cv_folds": 5
}
```

Output
```bash
{
  "predicted_runtime": "45 minutes"
}
```