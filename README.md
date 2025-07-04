# Mental Health Prediction using Streamlit and ML 🧠

A Python-based web application that helps assess mental health-related workplace factors using a trained machine learning model. This repository demonstrates how to build, customize, and deploy a Streamlit app using a decision tree classifier for real-time mental health prediction.

---

## Features

- **Interactive UI**: Built with Streamlit to collect user responses through radio buttons and dropdowns.
- **ML Model Integration**: Uses a Decision Tree Classifier trained on mental health survey data.
- **Real-Time Prediction**: Instantly provides feedback based on inputs.
- **Fully in Python**: The entire codebase is written in Python for accessibility and flexibility.

---

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Trained `.pkl` model file (already included or generated from training)
- (Optional) Virtual environment tool such as `venv` or `conda`

---

### Installation

1. **Clone the repository**:

```bash
git clone https://github.com/RITWIK4959/Mental_Health_Prediction.git
cd Mental_Health_Prediction
```
2.**Python dependencies**:

```bash
pip install -r requirements.txt
```
### Usage
Run the app with:

```bash
streamlit run app.py
```
You may need to adjust the entry point if your main script is named differently.

## Configuration
To change the prediction model, replace best_model.pkl in the model/ folder.

To modify the question prompts, update the Streamlit inputs in app.py.

Extend with new inputs or logic by modifying the Python code accordingly.

## Project Structure
```bash
mental-health-prediction-app/
├── app.py                 # Main Streamlit app
├── model/
│   └── best_model.pkl     # Trained ML model
├── notebook/
│   └── training.ipynb     # Notebook for model training
├── requirements.txt       # Python package dependencies
└── README.md              # Project documentation
```
## Acknowledgments
Streamlit

Scikit-learn

Pandas

