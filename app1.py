import altair
import altair as alt
import streamlit as st
import pandas as pd
import openpyxl
import numpy as np
import os
# importing the data
os.getcwd()
st.set_page_config(layout='wide')

file = "data/Results.xlsx"
data = pd.ExcelFile(file)
sheet_names=(data.sheet_names)
# adding the sub header
# st.subheader('Selecting data')
col1, col2, col3, col4 = st.beta_columns(4)

# Select box to choose the feature
with col2:
    Select_Features = st.selectbox('Choose any feature ',sheet_names)
sheet_name= pd.read_excel(data, Select_Features)
# st.write(sheet_name)

#Create the select box to choose scaler
uniqueValues = sheet_name['normal_type'].unique()
with col3:
    Select_Scaler = st.selectbox('Choose Normalize Technique ',uniqueValues)
# st.write(Select_Scaler)

#create the select box to choose the Name of store
uniqueValues_1= sheet_name['store_name'].unique()
with col1:
    Select_store = st.selectbox("Choose the store Name",uniqueValues_1)
# st.write(uniqueValues_1)

uniqueValues_2= sheet_name['algorithm'].unique()
with col4:
    Select_algo= st.selectbox("Choose Algorithm",uniqueValues_2)

# selecting the store name and scaler name according to choice:
store= sheet_name[sheet_name["store_name"]==Select_store]
scaler= store[store["normal_type"]==Select_Scaler]
algo= scaler[scaler["algorithm"]==Select_algo]



# chart_data = pd.DataFrame(store["predicted_cal"])
# st.line_chart(chart_data)
# chart_data = pd.DataFrame(scaler["predicted_cal"])
# st.line_chart(chart_data)
#  To write the data frame in application dashboard



data = pd.DataFrame(algo)

df = data[['time','total', 'predicted_cal']]
#df.set_index('time')
df = df.rename(columns={'time':'index'}).set_index('index')
st.line_chart(df)
st.write("\n")
# st.dataframe(data=data.drop(['store_name', 'algorithm', 'scaler'], axis=1), width=20000, height=500)

col1, col2, col3 = st.beta_columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.dataframe(data=data.drop(['store_name', 'algorithm', 'normal_type'], axis=1), width=20000, height=500)

with col3:
    st.write("")



# st.line_chart(chart_data)

# selecting the minimum amd maximum values of MAE from whole table according to store wise

# col1, col2, col3 = st.beta_columns(3)
#
# with col1:
#     maxValue_mae= store['MAE'].max()
#     st.write("Maximum value of MAE",maxValue_mae)
#     minValue_mae = store['MAE'].min()
#     st.write("Minimum value of MAE",minValue_mae)
#
# with col2:
#     maxValue_mse= store['MSE'].max()
#     st.write("Maximum value of MSE",maxValue_mse)
#     minValue_mse = store['MSE'].min()
#     st.write("Minimum value of MSE",minValue_mse)
#
# with col3:
#     maxValue_r2= store['r2'].max()
#     st.write("Maximum value of r2",maxValue_r2)
#     minValue_r2 = store['r2'].min()
#     st.write("Minimum value of r2",minValue_r2)



# if option == ‘Text Summarization’:
#
# max_lengthy = st.slider('Maximum summary length (words)', min_value=30, max_value=150, value=60, step=10)
#
# num_beamer = st.slider('Speed vs quality of summary (1 is fastest)', min_value=1, max_value=8, value=4, step=1)
#
# text = st.text_area('Enter Text Below (maximum 800 words):', height=300)
#
# submit = st.button('Generate')
#
# if submit:
#
#     st.subheader("Summary:")
#
#     with st.spinner(text="This may take a moment..."):
#
#         summWords = sum2(text, max_length=max_lengthy, min_length=15, num_beams=num_beamer, do_sample=True, early_stopping=True, repetition_penalty=1.5, length_penalty=1.5)
#
#     text2 =summWords[0]["summary_text"]
#
#     st.write(text2)



# scaler.style.highlight_max(color = 'lightgreen', axis = 0)




# import plotly.express as px
# st.title('Plotly Penguins')
# fig=px.histogram(df["body_mass_g"])
# st.plotly_chart(fig)
#
# # Seaborn chart and matplotchart
# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns
# st.title("Seaborn and Matplotlib Histograms")
# st.subheader("Seaborn Chart")
# fig_sb, ax_sb = plt.subplots()
# ax_sb = sns.histplot(df['flipper_length_mm'])
# plt.xlabel('Flipper_length_mm')
# st.pyplot(fig_sb)
#