import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import tensorflow as tf
from datetime import datetime, timedelta

'''
https://python.plainenglish.io/building-a-stock-price-forecasting-app-with-python-and-streamlit-a-step-by-step-guide-50edfe1be374
how to use this program.
1. {.\myenv\Scripts\activate}
2. {streamlit run [파일명]}
 '''

# User input for stock ticker symbol
stock_symbol = st.sidebar.text_input('Enter Stock Ticker Symbol (e.g., MSFT):')

# Date range input
start_date = st.sidebar.date_input('Select Start Date:', datetime.now() - timedelta(days=365))
end_date = st.sidebar.date_input('Select End Date:', datetime.now())

# Load stock data
if stock_symbol:
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    print("stock_symbol")
    st.subheader('Stock Data')
    st.write(stock_data.head(50))  # Display first 50 rows
    stock_graph=go.Scatter(x=['Date'], y=['Close'], mode='lines', name='stock')


#주요 경제 지표 로드
Gold_Data=yf.download("GC=F", start=start_date, end=end_date)
print("Gold_Data")
st.subheader('Gold_Data')
st.write(Gold_Data.head(25))  # Display first 25 rows


Oil_Data=yf.download("CL", start=start_date, end=end_date)
print("Oil_Data")
st.subheader('Oil_price_Data')
st.write(Oil_Data.head(25))  # Display first 25 rows

NASDAQ_Data=yf.download("^IXIC", start=start_date, end=end_date)
print("NASDAQ_Data")
st.subheader('NASDAQ_Data')
st.write(NASDAQ_Data.head(25))  # Display first 25 rows

US_Interest_Rate10years=yf.download("THX", start=start_date, end=end_date)
print("US Interest Rate 10years")
st.subheader('US_Interest_Rate10years')
st.write(US_Interest_Rate10years.head(25)) 

