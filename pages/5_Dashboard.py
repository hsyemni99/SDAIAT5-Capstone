import os
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Death Causes Dashboard",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state='collapsed',
)

# Load your data from the CSV file
dataset_url_tb = os.path.join('.','dashboard','cause_of_deaths.csv')
dataset_url_pn = os.path.join('.','dashboard','pneumonia-and-lower-respiratory-diseases-deaths_saudi_arabia.csv')
@st.cache_data
def get_data_tb() -> pd.DataFrame:
    return pd.read_csv(dataset_url_tb)


@st.cache_data
def get_data_pn() -> pd.DataFrame:
    return pd.read_csv(dataset_url_pn)
data_pn = get_data_pn()
data_tb = get_data_tb()
saudi_data = data_tb[data_tb['Country/Territory'] == 'Saudi Arabia']
deathratesbyyear = saudi_data.groupby(["Year"]).sum()
deathratesbyyear = deathratesbyyear.drop(['Country/Territory', 'Code'], axis=1)
top_causes = deathratesbyyear.sum().sort_values(ascending=False).head(15)

# dashboard title
st.title("Death Causes Dashboard")

# create two columns for charts
fig_col1, fig_col2, fig_col3 = st.columns(3)

# Column 1

with fig_col1:
    fig11 = px.bar(top_causes, x=top_causes.index, y=top_causes.values, labels={'x': '', 'y': 'Number of Deaths'})
    fig11.update_layout(title='Top 15 Causes of Death in Saudi Arabia (1990-2019)', xaxis_title='', yaxis_title='Number of Deaths')
    st.write(fig11)
    
    fig12 = px.line(data_frame=deathratesbyyear,
                    x=deathratesbyyear.index, 
                    y='Cardiovascular Diseases', 
                    title="Deaths by Cardiovascular Diseases in Saudi Arabia over time",
                    )
    fig12.update_xaxes(range=[1990, 2019])

    st.write(fig12)


# Column 2

with fig_col2:
    melted_df = pd.melt(data_pn, id_vars=['Entity', 'Code', 'Year'], 
                    value_vars=['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years'],
                    var_name='Age Group', value_name='Count')

    # Group by Age Group and calculate the total count
    age_group_totals = melted_df.groupby('Age Group')['Count'].sum().reset_index()

    # Create a pie chart
    fig21 = px.pie(age_group_totals, names='Age Group', values='Count',
             title='Death Rates by Pneumonia per Age Group in Saudi Arabia (1990-2019)', hole=0.5)
    st.write(fig21)
    
    country_death_count = data_tb.groupby('Country/Territory')['Tuberculosis'].sum().reset_index()
    map = px.choropleth(
    country_death_count,
    locations='Country/Territory',
    locationmode='country names',
    color=np.log1p(country_death_count['Tuberculosis']),
    title='Tuberculosis Deaths by Country',
    color_continuous_scale='bluered',
    labels={'Tuberculosis': 'Number of Deaths'},
    hover_data={'Tuberculosis': True, 'Country/Territory': True},
)
    st.write(map)
    

# Column 3

with fig_col3:
    melted_df = pd.melt(data_pn, id_vars=['Entity', 'Code', 'Year'], 
                    value_vars=['Under 5', '5-14 years', '15-49 years', '50-69 years', '70+ years'],
                    var_name='Age Group', value_name='Count')

    # Create a line chart
    

    fig31 = px.line(melted_df, x='Year', y='Count', color='Age Group', 
              labels={'Count': 'Population Count'},
              title='Deaths from Pneumonia in Saudi Arabia By Age Group Over Time', width=600)
    st.write(fig31)
    selected_data = data_tb[data_tb['Country/Territory'] == 'Saudi Arabia']
    selected_data = selected_data[['Year', 'Tuberculosis']].sort_values(by="Year")

    # Create a line plot using Plotly Express
    fig32 = px.line(selected_data, x='Year', y='Tuberculosis',
              title='Tuberculosis Cases Over Years in Saudi Arabia', width=600)
    st.write(fig32)

st.markdown("### Detailed Data View of Causes of Death in Saudi Arabia")
st.dataframe(deathratesbyyear)

