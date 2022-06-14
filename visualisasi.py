import yfinance as yf
import pandas as pd
import streamlit as st

st.write("""
# Aplikasi Yahoo Finance
## Data saham Google

Berikut ini adalah data Closing Price dan Volume dari Google.
""")

ticker = 'ANTM'
tickerData = yf.Ticker(ticker)
tickerDF = tickerData.history(period='1d', start='2022-01-01', end='2022-05-30')

st.write(type(tickerDF))

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
st.line_chart(tickerDF.High)
