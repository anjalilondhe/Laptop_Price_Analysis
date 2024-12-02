import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Laptop_analysis",page_icon=":bar_chart:",layout="wide")
st.title(":bar_chart: Laptop Price Analysis")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html = True)

f1 = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
if f1 is not None:
    filename = f1.name
    st.write(f"Uploaded file:{filename}")

    try:
        if filename.endswith(".csv") or filename.endswith(".txt"):
            df = pd.read_csv(f1)
        elif filename.endswith(".xlsx") or filename.endswith(".xls"):
            df = pd.read_excel(f1)
        else:
            st.error("Unsupported file format")
            df = None

        if df is not None:
            st.write("File Preview")
            st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("No file uploaded. Loading default dataset.")
    try:
        default_path = os.path.join("D:\Data_analytics_Dashboard\Laptop_cleaned.csv")
        df = pd.read_csv(default_path)
        st.write("Default file preview:")
        st.dataframe(df)
    except FileNotFoundError:
        st.error("Default file not found, Please upload a file")

st.markdown("<h2 style='text-align: center;padding:50px;'>Categorical and Numerical Data</h2>",unsafe_allow_html=True)

df = pd.read_csv("Laptop_Cleaned.csv")
cat_cols = ['select column', 'Company', 'TypeName', 'Cpu', 'Gpu', 'OpSys']
num_cols = ['Ram', 'Weight', 'TouchScreen', 'IPS', 'ppi']

all_cols = cat_cols + num_cols
selected_column = st.sidebar.selectbox("Select a column to compare", all_cols)

col1,col2 = st.columns((2))
# Plotting 
if selected_column and selected_column != 'select column':
    if selected_column in cat_cols:
        fig = px.box(df, x=selected_column, y='Price', title=f'Price Variation by {selected_column}')
    elif selected_column in num_cols:
        fig = px.scatter(df, x=selected_column, y='Price', title=f'Price vs {selected_column}')
    else:
        st.error("Selected column is not valid for analysis.")
    st.plotly_chart(fig)
else:
    #st.info("Please select a valid column from the sidebar.")
    with col1:
        #st.subheader("Categorical and Numerical Data")
        fig1 = px.bar(x = df['Company'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']],labels={'x': 'Company', 'y': 'Price'})
        fig1.update_layout(height=400,title='COMPANY VS PRICE', xaxis_title='Company', yaxis_title='Price')
        st.plotly_chart(fig1, use_container_width = True, height = 200)

        fig3 = px.bar(x = df['TypeName'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']],labels={'x': 'Company', 'y': 'Price'})
        fig3.update_layout(height=500,title='TypeName VS PRICE', xaxis_title='TypeName', yaxis_title='Price')
        st.plotly_chart(fig3, use_container_width = True, height = 250)

        fig4 = px.bar(x = df['Cpu'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']],labels={'x': 'Company', 'y': 'Price'})
        fig4.update_layout(height = 400, title = 'CPU VS PRICE', xaxis_title = 'CPU', yaxis_title = 'Price')
        st.plotly_chart(fig4, use_container_width = True, height = 250)

        fig5 = px.bar(x = df['Gpu'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']],labels={'x': 'Gpu', 'y': 'Price'})
        fig5.update_layout(height = 400, title = 'GPU VS PRICE', xaxis_title = 'Gpu', yaxis_title = 'Price')
        st.plotly_chart(fig5, use_container_width = True, height = 250)

        fig6 = px.bar(x = df['OpSys'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']],labels={'x': 'OpSys', 'y': 'Price'})
        fig6.update_layout(height = 500, title = 'OpSys VS PRICE', xaxis_title = 'OpSys', yaxis_title = 'Price')
        st.plotly_chart(fig6, use_container_width = True, height = 250)

    with col2:
        fig2 = px.bar(x = df['Ram'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']], labels = {'x': 'Ram', 'y':'Price'})
        fig2.update_layout(height=400,title='RAM vs Price',xaxis_title='RAM (GB)',yaxis_title='Price ($)')
        st.plotly_chart(fig2, use_container_width = True, height = 200)

        fig7 = px.bar(x = df['Weight'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']], labels = {'x': 'Weight', 'y':'Price'})
        fig7.update_layout(height=500,title='WEIGHT vs Price',xaxis_title='Weight',yaxis_title='Price ($)')
        st.plotly_chart(fig7, use_container_width = True, height = 200)

        fig8 = px.bar(x = df['TouchScreen'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']], labels = {'x': 'TouchScreen', 'y':'Price'})
        fig8.update_layout(height=500,title='TOUCH SCREEN vs Price',xaxis_title='TouchScreen',yaxis_title='Price ($)')
        st.plotly_chart(fig8, use_container_width = True, height = 200)

        fig9 = px.bar(x = df['IPS'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']], labels = {'x': 'IPS', 'y':'Price'})
        fig9.update_layout(height=500,title='IPS vs Price',xaxis_title='IPS',yaxis_title='Price ($)')
        st.plotly_chart(fig9, use_container_width = True, height = 200)

        fig10 = px.bar(x = df['ppi'], y = df['Price'], text=['${:,.2f}'.format(x) for x in df['Price']], labels = {'x': 'ppi', 'y':'Price'})
        fig10.update_layout(height=500,title='PPI vs Price',xaxis_title='ppi',yaxis_title='Price ($)')
        st.plotly_chart(fig10, use_container_width = True, height = 200)


#Plotting for company wise
#Company_name = ['Select Company name','Apple','HP','Acer','Asus','Dell','Lenovo','MSI','Toshiba']
#selected_company = st.sidebar.selectbox("Select Company name",Company_name)
#if Company_name and Company_name != 'select Company name':
#    if selected_company in Company_name:
#        fig1 = px.bar(df, x = selected_company, y = 'Price')
#else:
#    st.info("Select any company")
#    st.plotly_chart(fig1)
    

