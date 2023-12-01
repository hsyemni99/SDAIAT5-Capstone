import streamlit as st
import os
import numpy as np
import tensorflow as tf
from PIL import Image
model_path = os.path.join('.', 'models', 'Pneumonia', 'Pneumonia.keras')
class_names = ['COVID-19', 'Normal', 'Pneumonia']
harmful = ['COVID-19', 'Pneumonia']
normal = ['Normal']
st.set_page_config(page_title="Pneumonia Diagnosis Demo",
                   layout="wide",
                   initial_sidebar_state="expanded")

# Column 1
column1, column2 = st.columns(2)

with column1:

    st.markdown("# Pneumonia Diagnosis")
#st.sidebar.header("Pneumonia Diagnosis2")
    st.write(
    "This demo illustrates the capabilities of our deep learning model to predict whether a   \n" 
    "patient has Pneumonia, COVID-19, or not."
    )

    st.markdown(
"""### Common symptoms of pneumonia include:
- Cough: This may produce phlegm (a thick, mucous-like substance).
- Fever: A high body temperature is a common sign of infection.
- Shortness of breath: Difficulty breathing, especially during physical activities.
- Chest pain: This can range from mild to severe and may worsen when breathing deeply or coughing.
- Fatigue: Feeling excessively tired or weak.
### Pneumonia can be classified into different types based on the causative agent:
- **Bacterial Pneumonia**: Caused by various bacteria, including Streptococcus pneumoniae. This type can be severe, especially in older adults and those with weakened immune systems.
- **Viral Pneumonia**: Caused by viruses such as influenza (flu) or respiratory syncytial virus (RSV). Viral pneumonia is often milder than bacterial pneumonia.
- **Mycoplasma Pneumonia**: Caused by Mycoplasma pneumoniae, this type is usually milder than bacterial pneumonia and is sometimes referred to as "walking pneumonia."
- **Fungal Pneumonia**: Caused by fungi, such as Pneumocystis jirovecii. It is more common in individuals with weakened immune systems, such as those with HIV/AIDS.""")
def prediction_decode(image):
    image = image.convert("L")
    image = (np.expand_dims(image,0))
    predictions = loaded_model.predict(image, verbose=0)
    pred=np.argmax(predictions)
    return class_names[pred]
loaded_model = tf.keras.models.load_model(model_path)

# Column 2
with column2:
    
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    if image_file is not None:
        try:
            image_file = Image.open(image_file)
            pred = prediction_decode(image_file)
            if pred in harmful:
                prediction = f'<p style="color:Red; font-size: 20px;">{pred}</p>'
            if pred in normal:
                prediction = f'<p style="color:Green; font-size: 20px;">{pred}</p>'
            st.write(f'<p style="color:White; font-size: 20px;">Image Prediction is</p>', prediction, unsafe_allow_html=True)
            image_file = image_file.resize((600,545))
            st. image(image_file)
        except Exception as e:
            print(e)
    else:
        print("placeholder")