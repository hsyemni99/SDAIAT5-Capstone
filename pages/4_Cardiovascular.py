import streamlit as st
import os
import numpy as np
import pickle
import pandas as pd 
model_path = os.path.join('.', 'models', 'CVD', 'GradientBoost-0.1.0.pkl')
features = ['Weight', 'Systolic blood pressure', 'Diastolic blood pressure', 'Cholesterol levels. (1: Normal, 2: Above Normal, 3: Well Above Normal).', 'Age in years', 'Body Mass Index']
feature_list = os.path.join('.', 'models', 'CVD', 'CVDfeaturesformodel.txt')
class_names = ['Negative', 'Positive']
harmful = ['Positive']
normal = ['Negative']
st.set_page_config(page_title="Cardiovascular Disease Diagnosis Demo",
                   layout="wide",
                   initial_sidebar_state="expanded")

column1, column2 = st.columns(2)

# Column 1
with column1:

    st.markdown("# Cardiovascular Disease Diagnosis")
    st.write(
    "This demo illustrates the capabilities of our machine learning model to predict whether a   \n" 
    "patient has a cardiovascular disease or not."
    )

    st.markdown(
"""### Common symptoms of Cardiovascular Disease include:
- chest pain.
- pain, weakness or numb legs and/or arms.
- breathlessness.
- very fast or slow heartbeat, or palpitations.
- feeling dizzy, lightheaded or faint.
- fatigue.
- swollen limbs.


##### Cardiovascular Dieases can be classified into different types but are not limited to the following:
- **coronary heart disease** : occurs when your heart muscle’s blood supply is blocked or interrupted by a build-up of fatty substances (atheroma) in the coronary arteries.
- **stroke** : is a serious medical condition that occurs when the blood supply to the brain is disturbed.
- **peripheral arterial disease** : occurs when there is a blockage in the arteries to your limbs (usually your legs).
- **aortic disease** : The aorta is the largest blood vessel in the body. It carries blood from your heart to the rest of your body.
""")

with open(model_path, 'rb') as f:
    CVDmodel = pickle.load(f)
    f.close()

with open(feature_list, 'rb') as g:
    line = g.readline()
    features_list = [word.decode('utf-8') for word in line.split()]
    
def preprocessinput(inputdata):
    if inputdata[3] == 'Normal':
        inputdata[3] = 1
        
    if inputdata[3] == 'Above Normal':
        inputdata[3] = 2
        
    if inputdata[3] == 'Well Above Normal':
        inputdata[3] = 3
    return pd.DataFrame(data=[inputdata], columns=features_list)

def predictionfrommodel(model, inputdata):
    processedinput = preprocessinput(inputdata)
    pred = model.predict(processedinput)
    prob = model.predict_proba(processedinput)
    prob = prob.max()
    prob *= 100
    return class_names[pred[0]], prob

# Column 2
with column2:
    
    
    with st.form("Patient Data"):
        st.write("Enter the following data")
        input1 = st.number_input('Weight')
        input2 = st.number_input('Systolic blood pressure')
        input3 = st.number_input('Diastolic blood pressure')
        input4 = st.selectbox(label='Cholesterol levels. (1: Normal, 2: Above Normal, 3: Well Above Normal).', options=['Normal', 'Above Normal', 'Well Above Normal'])
        input5 = st.number_input('Age in years')
        input6 = st.number_input('Body Mass Index')

        submitted = st.form_submit_button("Submit")

        if submitted:
            input_features = [input1, input2 ,input3, input4, input5, input6]
            pred, prob = predictionfrommodel(CVDmodel, input_features)
            prob = round(prob, 2)            
            if pred in harmful:
                prediction = f'<p style="color:Red; font-size: 20px;">{pred}</p>'
            if pred in normal:
                prediction = f'<p style="color:Green; font-size: 20px;">{pred}</p>'
            st.write(f'<p style="color:White; font-size: 20px;">Prediction is</p>', prediction, f'<p style="color:White; font-size: 20px;">with confidence of {prob}%</p>', unsafe_allow_html=True)
