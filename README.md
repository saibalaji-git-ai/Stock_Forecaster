# Demand Forecasting for Top Products

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-success?logo=streamlit)](https://stockforecaster-ynhyfpt5tgmm3rv4weriaf.streamlit.app/)

This project implements a **Demand Forecasting** application to forecast the demand of the top-selling products for the next 15 weeks using historical sales data. The model predicts future demand for selected products using **ARIMA** (AutoRegressive Integrated Moving Average) time series forecasting and displays both the historical and forecasted values in an intuitive plot.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Uploading Data](#uploading-data)
  - [Forecasting Demand](#forecasting-demand)
  - [Downloading Forecast](#downloading-forecast)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
  - [Data Preprocessing](#data-preprocessing)
  - [ARIMA Model](#arima-model)
  - [Visualization](#visualization)
- [Streamlit Application](#streamlit-application)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Top Products Display**: Displays the top 10 products based on the total quantity sold.
- **Interactive Selection**: Users can select a stock code (product) and choose the number of weeks (up to 15 weeks) to forecast.
- **ARIMA Forecasting**: The ARIMA model is used to generate a time series forecast for future demand.
- **Visualizations**: Historical and forecasted demand are plotted on an interactive graph.
- **Downloadable Forecast**: Users can download the forecasted demand data as a CSV file.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/demand-forecasting-app.git
    cd demand-forecasting-app
    ```

2. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

### Uploading Data
- Use the `Upload Transactional Data File 1` and `Upload Transactional Data File 2` buttons to upload two CSV files containing historical sales data. The data files should include fields such as:
  - `InvoiceDate`: The date when the product was sold.
  - `StockCode`: The unique code for each product.
  - `Quantity`: The number of units sold.

### Forecasting Demand
- After uploading the data, the app will display the top 10 products based on the total quantity sold.
- Select a product from the drop-down list and choose the number of weeks to forecast (1 to 15 weeks).
- The application will train an ARIMA model on the historical sales data for the selected product and display the forecasted demand for the chosen time horizon.

### Downloading Forecast
- Once the forecast is displayed, you can download the results as a CSV file using the **Download Forecast Data** button.

## Dependencies

The following Python libraries are used in this project:
- `streamlit`
- `pandas`
- `numpy`
- `matplotlib`
- `plotly`
- `statsmodels`
- `sklearn`

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

## Project Structure

```plaintext
demand-forecasting-app/
│
├── app.py                  # Main Streamlit app code
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation (this file)
```

## How It Works

### Data Preprocessing
The app concatenates the two uploaded CSV files and extracts the top 10 products based on the quantity sold. The user selects a product (StockCode), and the application resamples the sales data on a weekly basis.

### ARIMA Model
The ARIMA model is used for forecasting demand. The order of the model is currently set to `(5, 1, 0)`, but it can be adjusted for better performance. The model is trained on the weekly sales data for the selected product, and forecasts are generated for the specified number of weeks.

### Visualization
The app generates a time series plot that visualizes both the historical sales data and the forecasted demand. The forecasted values are plotted on the same graph as the historical data to allow easy comparison.

## Streamlit Application

You can also access the live version of the app deployed on Streamlit Cloud using the following link:

[Demand Forecasting App](https://stockforecaster-ynhyfpt5tgmm3rv4weriaf.streamlit.app/)



