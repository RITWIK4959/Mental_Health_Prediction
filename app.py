import joblib
import streamlit as st

# Page config
st.set_page_config(page_title="Mental Health Prediction", layout="centered")

# Custom dark theme CSS
st.markdown("""
    <style>
        body, .main, .block-container {
            background-color: #000000 !important;
            color: white !important;
        }
        label, .css-1cpxqw2, .stTextInput > div > div > input {
            color: white !important;
        }
        .stRadio > div, .stSelectbox > div, .stSlider > div {
            color: white !important;
        }
        .stButton>button {
            background-color: white !important;
            color: black !important;
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: bold;
        }
        .stSelectbox div[data-baseweb="select"] {
            background-color: #111111 !important;
            color: white !important;
        }
        .stTextInput > div > div > input {
            background-color: #111111 !important;
            color: white !important;
            border-radius: 5px;
        }
        hr {
            border: 1px solid #444;
        }
            .stRadio label {
    color: white !important;
}
    </style>
""", unsafe_allow_html=True)

# Load model and encoder
model = joblib.load('model/decision_tree_model.pkl')
country_encoder = joblib.load('model/label_encoder.pkl')

# Header
st.markdown("""
    <h1 style='text-align: center; color: #4B9CD3;'>Mental Health Treatment Predictor</h1>
    <p style='text-align: center; font-size:18px;'>Complete the form below to predict if someone may need mental health support.</p>
    <hr>
""", unsafe_allow_html=True)

# Inputs
age = st.slider("Age", 10, 100, 25)
gender = st.selectbox("Gender", [0, 1, 2], format_func=lambda x: ['Male', 'Female', 'Other'][x])

col1, col2 = st.columns(2)
with col1:
    self_employed = st.radio("Are you self-employed?", ['Yes', 'No'])
    remote_work = st.radio("Remote Work?", ['Yes', 'No'])
    tech_company = st.radio("Tech Company?", ['Yes', 'No'])
    country = st.text_input("Country")

with col2:
    family_history = st.radio("Family history of mental illness?", ['Yes', 'No'])
    obs_consequence = st.radio("Observed consequences at work?", ['Yes', 'No'])

# Selectboxes
work_interfere = st.selectbox("How often does mental health interfere with work?", ['Never', 'Rarely', 'Sometimes', 'Often'])
no_employees = st.selectbox("Company size", ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000'])
benefits = st.selectbox("Mental health benefits?", ['Yes', "Don't know", 'No'])
care_options = st.selectbox("Care options provided?", ['Yes', "Not sure", 'No'])
wellness_program = st.selectbox("Wellness program?", ['Yes', "Don't know", 'No'])
seek_help = st.selectbox("Help-seeking support?", ['Yes', "Don't know", 'No'])
anonymity = st.selectbox("Anonymity maintained?", ['Yes', "Don't know", 'No'])
leave = st.selectbox("Ease of taking leave?", ['Very difficult', 'Somewhat difficult', "Don't know", 'Somewhat easy', 'Very easy'])
mental_health_consequence = st.selectbox("Negative consequence for mental health disclosure?", ['Yes', "Maybe", 'No'])
phys_health_consequence = st.selectbox("Negative consequence for physical health disclosure?", ['Yes', "Maybe", 'No'])
coworkers = st.selectbox("Discuss with coworkers?", ['No', 'Some of them', 'Yes'])
supervisor = st.selectbox("Discuss with supervisor?", ['No', 'Some of them', 'Yes'])
mental_health_interview = st.selectbox("Talk mental health in interview?", ['No', 'Maybe', 'Yes'])
phys_health_interview = st.selectbox("Talk physical health in interview?", ['No', 'Maybe', 'Yes'])
mental_vs_physical = st.selectbox("Is mental health as important as physical?", ['No', "Don't know", 'Yes'])

# Encode inputs
work_interfere = {'Never': 0, 'Rarely': 1, 'Sometimes': 2, 'Often': 3}[work_interfere]
no_employees = {'1-5': 0, '6-25': 1, '26-100': 2, '100-500': 3, '500-1000': 4, 'More than 1000': 5}[no_employees]
benefits = {'Yes': 2, "Don't know": 1, 'No': 0}[benefits]
care_options = {'Yes': 2, "Not sure": 1, 'No': 0}[care_options]
wellness_program = {'Yes': 2, "Don't know": 1, 'No': 0}[wellness_program]
seek_help = {'Yes': 2, "Don't know": 1, 'No': 0}[seek_help]
anonymity = {'Yes': 2, "Don't know": 1, 'No': 0}[anonymity]
leave = {'Very difficult': 0, 'Somewhat difficult': 1, "Don't know": 2, 'Somewhat easy': 3, 'Very easy': 4}[leave]
mental_health_consequence = {'Yes': 2, "Maybe": 1, 'No': 0}[mental_health_consequence]
phys_health_consequence = {'Yes': 2, "Maybe": 1, 'No': 0}[phys_health_consequence]
coworkers = {'No': 0, 'Some of them': 1, 'Yes': 2}[coworkers]
supervisor = {'No': 0, 'Some of them': 1, 'Yes': 2}[supervisor]
mental_health_interview = {'No': 0, 'Maybe': 1, 'Yes': 2}[mental_health_interview]
phys_health_interview = {'No': 0, 'Maybe': 1, 'Yes': 2}[phys_health_interview]
mental_vs_physical = {'No': 0, "Don't know": 1, 'Yes': 2}[mental_vs_physical]
self_employed = 1 if self_employed == 'Yes' else 0
family_history = 1 if family_history == 'Yes' else 0
remote_work = 1 if remote_work == 'Yes' else 0
tech_company = 1 if tech_company == 'Yes' else 0
obs_consequence = 1 if obs_consequence == 'Yes' else 0

# Predict
if st.button("Predict"):
    try:
        country_encoded = country_encoder.transform([country])[0]
        input_features = [
            age, gender, country_encoded, self_employed, family_history,
            work_interfere, no_employees, remote_work, tech_company,
            benefits, care_options, wellness_program, seek_help,
            anonymity, leave, mental_health_consequence,
            phys_health_consequence, coworkers, supervisor,
            mental_health_interview, phys_health_interview,
            mental_vs_physical, obs_consequence
        ]

        prediction = model.predict([input_features])[0]
        if prediction == 1:
            st.success("✅ Prediction: The person likely needs mental health treatment.")
        else:
            st.info("🟢 Prediction: The person likely does NOT need mental health treatment.")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
