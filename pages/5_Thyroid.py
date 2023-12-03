import streamlit as st
import os
import numpy as np
import pickle
import pandas as pd 

import sklearn
print(sklearn.__version__)


model_path = os.path.join('.', 'models', 'Thyroid', 'Thyroid.pkl')
features = ['age', 'sex', 'on_thyroxine', 'TSH', 'T3', 'TT4', 'FTI']
feature_list = os.path.join('.', 'models', 'Thyroid', 'THRfeatures.txt') #
class_names = ['Negative', 'Hypothyroid', 'Hyperthyroid']
harmful = ['Hypothyroid', 'Hyperthyroid']
normal = ['Negative']

st.set_page_config(page_title="Thyroid Disease Diagnosis Demo",
                   layout="wide",
                   initial_sidebar_state="expanded")

column1, column2 = st.columns(2)

# Column 1
with column1:

    st.markdown("# Thyroid Disease Diagnosis")
    st.write(
    "This demo illustrates the capabilities of our machine learning model to predict whether a   \n" 
    "patient has a Thyroid disease or not."
    )

    st.markdown(
"""
#### Thyroid Diseases can be classified into two types to the following:
- **Overactive thyroid (hyperthyroidism)** : An overactive thyroid, also known as hyperthyroidism or thyrotoxicosis, is where the thyroid gland produces too much of the thyroid hormones.
Having too much of these hormones can cause unpleasant and potentially serious problems that may need treatment.
An overactive thyroid can affect anyone, but it's about 10 times more common in women than men, and typically happens between 20 and 40 years of age.
- **Underactive thyroid (hypothyroidism)** : An underactive thyroid gland (hypothyroidism) is where your thyroid gland does not produce enough hormones.
Common signs of an underactive thyroid are tiredness, weight gain and feeling depressed.


#### Common symptoms of Overactive thyroid (hyperthyroidism) Disease include:
- nervousness, anxiety and irritability
- mood swings
- difficulty sleeping
- persistent tiredness and weakness
- sensitivity to heat
- swelling in your neck from an enlarged thyroid gland (goitre)
- an irregular and/or unusually fast heart rate (palpitations)
- twitching or trembling
- weight loss

#### Common symptoms of Underactive thyroid (hypothyroidism) Disease include:
- tiredness
- being sensitive to cold
- weight gain
- constipation
- depression
- slow movements and thoughts
- muscle aches and weakness
- muscle cramps
- dry and scaly skin
- brittle hair and nails
""")

with open(model_path, 'rb') as f:
    THRmodel = pickle.load(f)
    f.close()

with open(feature_list, 'rb') as g:
    line = g.readline()
    features_list = [word.decode('utf-8') for word in line.split()]
    
def preprocessinput(inputdata):
    if inputdata[1] == 'Male':
        inputdata[1] = 1
        
    if inputdata[1] == 'Female':
        inputdata[1] = 0

    if inputdata[2] == 'Yes':
        inputdata[2] = 1
        
    if inputdata[2] == 'No':
        inputdata[2] = 0
    
    return pd.DataFrame(data=[inputdata], columns=features_list)

def predictionfrommodel(model, inputdata):
    processedinput = preprocessinput(inputdata)
    pred = model.predict(processedinput)
    return class_names[pred[0]]

# Column 2
with column2:
    
    
    with st.form("Patient Data"):
        st.write("Enter the following data")
        input1 = st.number_input('Age in years', min_value=0, max_value=100) # Integer
        input2 = st.selectbox(label='Sex', options=['Male', 'Female']) # F - M
        input3 = st.selectbox(label='Is patient on thyeroxine', options=['Yes', 'No']) # Yes - No
        input4 = st.number_input('TSH level in blood')
        input5 = st.number_input('T3 level in blood')
        input6 = st.number_input('TT4 level in blood')
        input7 = st.number_input('FTI level in blood')

        submitted = st.form_submit_button("Submit")

        if submitted:
            input_features = [input1, input2 ,input3, input4, input5, input6, input7]
            pred = predictionfrommodel(THRmodel, input_features)
            if pred in harmful:
                prediction = f'<p style="color:Red; font-size: 20px;">{pred}</p>'
            if pred in normal:
                prediction = f'<p style="color:Green; font-size: 20px;">{pred}</p>'
            st.write(f'<p style="color:White; font-size: 20px;">Patient is</p>', prediction, unsafe_allow_html=True)