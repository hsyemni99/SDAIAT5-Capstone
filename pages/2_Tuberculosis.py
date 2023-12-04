import streamlit as st
import os
import numpy as np
import tensorflow as tf
from PIL import Image
model_path = os.path.join('.', 'models', 'Tuberculosis', 'Tuberculosis.keras')
class_names = ['NORMAL', 'TURBERCULOSIS']
harmful = ['TURBERCULOSIS']
normal = ['NORMAL']
st.set_page_config(page_title="Tuberculosis Diagnosis Demo",
                   layout="wide",
                   initial_sidebar_state="expanded")

# Column 1
column1, column2 = st.columns(2)

with column1:

    st.markdown("#  Tuberculosis Diagnosis")
#st.sidebar.header("Pneumonia Diagnosis2")
    st.write(
    "This demo illustrates the capabilities of our deep learning model to predict whether a   \n" 
    "patient has postive or negative for Tuberculosis."
    )

    st.markdown(
"""### Symptoms:
##### 1. Pulmonary Tuberculosis:
- Persistent cough that lasts three weeks or longer.
- Coughing up blood or sputum.
- Chest pain and discomfort.
- Fatigue, weakness, and unintentional weight loss.
##### 2. Extrapulmonary Tuberculosis:
- Tuberculosis can affect other organs, such as the kidneys, spine, and brain, leading to a range of symptoms
depending on the affected area.
### Tuberculosis can be classified into different types based on the stage:
- **Primary TB infection**: The first stage is called the primary infection. Immune system cells find and capture the germs. The immune system may completely destroy the germs. But some captured germs may still survive and multiply.
- **Latent TB infection**: Primary infection is usually followed by the stage called latent TB infection. Immune system cells build a wall around lung tissue with TB germs. The germs can't do any more harm if the immune system keeps them under control.
- **Active TB disease**: Active TB disease happens when the immune system can't control an infection. Germs cause disease throughout the lungs or other parts of the body.""")
def prediction_decode(image):
    image = image.convert("L")
    image = (np.expand_dims(image,0))
    predictions = loaded_model.predict(image, verbose=0)
    pred=np.argmax(predictions)
    prob = predictions.max()
    prob = prob * 100
    return class_names[pred], prob
loaded_model = tf.keras.models.load_model(model_path)

# Column 2
with column2:
    
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    if image_file is not None:
        try:
            image_file = Image.open(image_file)
            pred, prob = prediction_decode(image_file)
            prob = round(prob, 2)
            if pred in harmful:
                prediction = f'<p style="color:Red; font-size: 20px;">{pred}</p>'
            if pred in normal:
                prediction = f'<p style="color:Green; font-size: 20px;">{pred}</p>'
            st.write(f'<p style="color:White; font-size: 20px;">Image Prediction is</p>', prediction, f'<p style="color:White; font-size: 20px;">with confidence of {prob}%</p>', unsafe_allow_html=True)
            image_file = image_file.resize((600,545))
            st. image(image_file)
        except Exception as e:
            print(e)
    