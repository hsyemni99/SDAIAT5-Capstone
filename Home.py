import streamlit as st
import tensorflow as tf
import pickle
import plotly.express as px
import pandas as pd 

st.set_page_config(
    page_title="Home",
    layout="wide",
)

st.write("# Fast Diagnosis System.")


st.markdown(
    """
    Our Application consists of multiple deep learning and machine learning models that diagnose five different diseases. \n
    The diseases are :
    - Pneumonia.
    - Tuberculosis.
    - Brain Tumors.
    - Cardiovascular Disease.
    - Thyroid Disease.
"""
)

st.write("#### How our project ties in with the Saudi 2030 Vision for the Kingdom:")
st.markdown('''
            By emphasizing early diagnosis, digital solutions, and innovation, your project aligns with the broader vision of transforming and modernizing Saudi Arabia's healthcare sector, \n
            ensuring that it becomes more comprehensive, effective, and integrated.
            
            ##### **Improving Access to Healthcare Services**:

            - Our project contributes to easing access to healthcare by providing a platform for users to perform preliminary disease diagnosis without the need for immediate physical medical consultation.
            
            ##### **Enhancing Digital Solutions**:

            - The inclusion of deep learning and machine learning models in our project reflects the emphasis on digital solutions in the Health Sector Transformation Program. It aligns with the vision's goal of achieving 100% coverage by the unified digital medical records system.
            ##### **Disease Prevention and Early Diagnosis**:

            - By incorporating machine learning models for disease prediction, our project supports the vision's focus on strengthening prevention against health threats. Early diagnosis is crucial for effective disease management and prevention.
            ''')


st.write("#### Our goals with diagnosing the diseases are:")
st.markdown('''
            - Identify the types of disease.
            - Identify different symptoms of the diseases.
            - Ensure prompt and effective treatment of cases in the early detection of disease symptoms.
            - Early Detection and Diagnosis that Enhance Diagnostic Capabilities Improve access to rapid and accurate diagnostic tools, including molecular tests and imaging technologies.
            - Raise Awareness that increase public awareness about risk factors and symptoms of the diseases to promote early detection.
            ''')
