How to run the project:
Install Python 3.10.13
in terminal
"cd path/to/project/directory/"
"pip install -r requirements.txt"
"streamlit run Home.py"


Our project folder architecture is listed below




Home.py


dashboard
	-Capstone Dashboard Plots.ipynb
	-cause_of_deaths.csv # for all diseases in general
	-pneumonia-and-lower-respiratory-diseases-deaths_saudi_arabia.csv
	-pneumonia-and-lower-respiratory-diseases-deaths.csv


demo data # each folder inside contains demo data for testing the web application
	-brain tumor
	-Cardiovascular Disease
	-pneumonia
	-tuberculosis


models # each folder inside contains the serialized model file in either .keras or .pkl format
	-Brain Tumor
		-BrainTumors.keras

	-CVD
		-CVDclasses.txt
		-CVDfeatures.txt
		-CVDfeaturesformodel.txt
		-GradientBoost-0.1.0.pkl
		-Testing Data.csv

	-Pneumonia
		-Pneumonia.keras

	-Tuberculosis
		-Tuberculosis.keras


notebooks
	-Brain Tumor
		-Brain_Tumor_CNN.ipynb
		-BrainTumors.keras
		-dataset link.txt
		-Dataset Split.ipynb # python script used for splitting the dataset into train, test, validation

	-CVD
		-CVD_ML.ipynb 
		-CVDclasses.txt # Classes saved for decoding purposes
		-CVDfeatures.txt # Features saved after applying feature selection to the data
		-dataset link.txt 
		-GradientBoost-0.1.0.pkl # Serialized pickle model
		-cardio_data_processed.csv # Dataset used for training
		-Testing Data.csv

	-Pneumonia
		-Pneumonia_CNN.ipynb
		-Pneumonia.keras
		-dataset link.txt
		-Dataset Split.ipynb # python script used for splitting the dataset into train, test, validation

	-Tuberculosis
		-Tuberculosis_CNN.ipynb
		-Tuberculosis.keras
		-dataset link.txt
		-Dataset Split.ipynb # python script used for splitting the dataset into train, test, validation

pages
	- 1_Pneumonia.py
	- 2_Tuberculosis.py
	- 3_Brain_Tumor.py
	- 4_Cardiovascular.py
	- 5_Dashboard.py
