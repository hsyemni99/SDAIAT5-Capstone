# Installing the prerequisites
### 1. Install Python 3.10

### 2. Create a new Python Environment using Python venv or Anaconda.
###
For Python:
```
python -m venv env-name
```
```
source env-name/bin/activate
```
###
For Anaconda:
```
conda create --name env-name python=3.10

```
```
conda activate env-name
```

### 3. Installing requirements.txt
```
cd path/to/repository
```
For Python Environment:
```
pip install -r requirements.txt
```
For Anaconda Environment:
```
conda install --file requirements.txt
```
# Running the web application
```
streamlit run Home.py
```
# Screenshots of the web application
### Home page containing information about the project and how our project ties in with the Saudi 2030 Vision.

![Home page](https://github.com/hsyemni99/SDAIAT5-Capstone/assets/120262815/e33b3404-3811-4407-9105-fb80ccfebe5d)

### Each disease has it's own web page to diagnose patients and some information about the disease.

![Pneumonia](https://github.com/hsyemni99/SDAIAT5-Capstone/assets/120262815/1e20a94d-caa6-49e9-8511-c957e9b8bf13)

![tuberculosis](https://github.com/hsyemni99/SDAIAT5-Capstone/assets/120262815/5c5045d1-4164-4d46-af53-e74e05a39ec1)

![braintumor](https://github.com/hsyemni99/SDAIAT5-Capstone/assets/120262815/5cb24461-1fcb-4cd4-8d97-ee2d8eb5cf97)

![CVD](https://github.com/hsyemni99/SDAIAT5-Capstone/assets/120262815/c1657a13-542e-4ed7-9dc4-0a690c7c3c94)

![thyroid](https://github.com/hsyemni99/SDAIAT5-Capstone/assets/120262815/2e31e439-d5f5-45d1-8566-b1f50a460792)

### A dashboard that displays insights about death causes in Saudi Arabia and how our chosen diseases affect Saudi Arabia.

![dashboard](https://github.com/hsyemni99/SDAIAT5-Capstone/assets/120262815/62d77b1d-db36-4965-b46c-21684ad40f60)




