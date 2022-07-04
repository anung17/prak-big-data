import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


st.write("""
# Aplikasi Yahoo Finance
## Data saham

Berikut ini adalah data Closing Price, Volume, dan Highest Price
""")

ticker = st.selectbox(
    "Ticker Perusahaan",
    options = ["ANTM", "AAPL", "MSFT", "GOOG", "AMZN"]
)

tickerData = yf.Ticker(ticker)

hari_mundur = st.selectbox(
    "Pilihan rentang hari",
    options = [7, 20, 30, 120]
)

jumlah_hari = timedelta(days=-int(hari_mundur))

# '''
# tgl_mulai = st.date_input(
    # "Mulai dari tanggal",
    # value=date.today()+jumlah_hari
# )
# '''
tgl_mulai = date.today() + jumlah_hari

tgl_akhir = st.date_input(
    "Hingga",
    value=date.today()
)

tickerDF = tickerData.history(
    period='1d',
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

attributes = st.multiselect(
    "Informasi yang ditampilkan:",
    options=['Open', 'High', 'Low', 'Close', 'Volume'],
    default=['Volume']
)

st.markdown(f"### Attributes yang dipilih")
for attr in attributes:
    st.write(attr)

if ticker == 'ANTM':
    nama_perusahaan = "Aneka Tambang"
elif ticker == 'AAPL':
    nama_perusahaan = "Apple"
elif ticker == 'MSFT':
    nama_perusahaan = "Microsoft"
elif ticker == 'GOOG':
    nama_perusahaan = "Google"
elif ticker == 'AMZN':
    nama_perusahaan = "Amazon"

st.markdown(f"Lima data pertama:")
st.write(tickerDF.head())

# f-string
if 'Open' in attributes:
    st.markdown(f"## Harga pembukaan *{nama_perusahaan}*")
    st.plotly_chart( px.line(tickerDF.Open))

if 'Close' in attributes:
    st.markdown(f"## Harga penutupan *{nama_perusahaan}*")
    st.plotly_chart( px.line(tickerDF.Close))

if 'Volume' in attributes:
    st.markdown(f"## Volume transaksi saham *{nama_perusahaan}*")
    st.plotly_chart( px.line(tickerDF.Volume) )
    #st.line_chart(tickerDF.Volume)

if 'High' in attributes:
    st.markdown(f"## Harga tertinggi *{nama_perusahaan}*")
    st.plotly_chart( px.line(tickerDF.High) )
    #st.line_chart(tickerDF.High)

if 'Low' in attributes:
    st.markdown(f"## Harga terendah *{nama_perusahaan}*")
    st.plotly_chart( px.line(tickerDF.Low))

