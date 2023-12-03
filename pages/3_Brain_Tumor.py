import streamlit as st
import os
import numpy as np
import tensorflow as tf
from PIL import Image
model_path = os.path.join('.', 'models', 'Brain Tumor', 'BrainTumors.keras')
class_names = ['Glioma Tumor', 'Meningioma Tumor', 'No Tumor', 'Pituitary Tumor']
harmful = ['Glioma Tumor', 'Meningioma Tumor', 'Pituitary Tumor']
normal = ['No Tumor']
st.set_page_config(page_title="Brain Tumor Diagnosis Demo",
                   layout="wide",
                   initial_sidebar_state="expanded")

column1, column2 = st.columns(2)

# Column 1
with column1:

    st.markdown("# Brain Tumor Diagnosis")
#st.sidebar.header("Pneumonia Diagnosis2")
    st.write(
    "This demo illustrates the capabilities of our deep learning model to predict whether a   \n" 
    "patient has a brain tumor or not."
    )

    st.markdown(
"""### Common symptoms of Brain Tumors include:
1. **Headaches**:
\t- Often more severe in the morning or with changes in position.
2. **Seizures**:
\t- New-onset seizures in adults may be a symptom of a brain tumor.
3. **Neurological Symptoms**:
\t- Changes in vision, hearing, or speech.
\t- Balance and coordination problems.
\t- Weakness or numbness in limbs.
\t- Memory or cognitive issues.
4. **Personality or Mood Changes**:
\t- Irritability, depression, or other unexplained changes in mood or behavior.

### Brain Tumors can be classified into different types but are not limited to the following:
- **Gliomas Tumor**: tumors that form in glial cells in the brain and spinal cord.
- **Meningioma Tumor**: a tumor that arises from the meninges — the membranes that surround the brain and spinal cord. 
- **Pituitary Tumor**: unusual growths that develop in the pituitary gland.""")
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