import yfinance as yf
import streamlit as st
import plotly.express as px

st.write('''
# Simple Stock Price App

## Heading 2

Ini tulisan **tebal**.
Ini tulisan *miring*.

Ini juga tulisan _miring_.
''')

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(
    period='1d',
    start='2022-01-01',
    end='2022-11-18'
)

st.write(tickerDF.head(5))

st.plotly_chart(
    px.line( tickerDF.Close )
)

st.plotly_chart(  px.line(tickerDF['Open'])  )
