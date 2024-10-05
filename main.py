import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import plotly.express as px

# Title and description
st.title("Demand Forecasting for Top Products")
st.write("Forecast the next 15 weeks demand for top-selling products using historical data.")

# Step 1: Upload datasets
uploaded_file1 = st.file_uploader("Upload Transactional Data File 1", type="csv")
uploaded_file2 = st.file_uploader("Upload Transactional Data File 2", type="csv")

# Data preprocessing (simplified)
    # Read transactional data
df1 = pd.read_csv('Transactional_data_retail_02.csv')
df2 = pd.read_csv('Transactional_data_retail_01.csv')
df = pd.concat([df1, df2])

    # EDA: Summary statistics and top 10 products
st.subheader("Top 10 Products by Quantity Sold")
top_10_products = df.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).head(10)
st.write(top_10_products)

    # Step 2: Select stock code and forecast horizon
selected_stock = st.selectbox("Select a stock code to forecast", top_10_products.index)
forecast_weeks = st.slider("Select the number of weeks to forecast", 1, 15, 10)

    # Step 3: Filter data for the selected stock code
product_data = df[df['StockCode'] == selected_stock]
    
    # Time series forecasting using ARIMA
product_data['InvoiceDate'] = pd.to_datetime(product_data['InvoiceDate'], errors='coerce')
st.subheader(f"Forecasting for Stock Code: {selected_stock}")
product_data_ts = product_data[['InvoiceDate', 'Quantity']].set_index('InvoiceDate').resample('W').sum()
    #st.write(product_data_ts)

    # Model training (ARIMA example)
model = ARIMA(product_data_ts, order=(5,1,0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=forecast_weeks)

    # Display forecasted values
st.write(f"Forecasted values for next {forecast_weeks} weeks:")
st.write(forecast)

    # Plot historical and forecasted demand
fig, ax = plt.subplots()
product_data_ts.plot(ax=ax, label="Historical Demand")
forecast.plot(ax=ax, label="Forecasted Demand")
plt.legend()
st.pyplot(fig)

    

    # Option to download forecast as CSV
st.subheader("Download Forecast Data")
csv = forecast.to_csv().encode('utf-8')
st.download_button(
        label="Download as CSV",
        data=csv,
        file_name=f'forecast_{selected_stock}.csv',
        mime='text/csv',
    )
