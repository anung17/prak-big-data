import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


st.write("""
# Aplikasi Yahoo Finance
## Data saham
""")

ticker = st.selectbox(
    "Ticker Perusahaan",
    options = ["ANTM.JK", "BMRI.JK", "BBNI.JK", "PNBN.JK", "ISAT.JK",
               "JSMR.JK", "LPGI.JK", "FREN.JK", "TLKM.JK", "EXCL.JK"
              ]
)

tickerData = yf.Ticker(ticker)

hari_mundur = st.selectbox(
    "Pilihan rentang hari",
    options = [7, 10, 20, 30, 60, 120, 365]
)

jumlah_hari = timedelta(days=-int(hari_mundur))

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

if ticker == 'ANTM.JK':
    nama_perusahaan = "PT Aneka Tambang Tbk"
elif ticker == 'BMRI.JK':
    nama_perusahaan = "PT Bank Mandiri (Persero) Tbk"
elif ticker == 'BBNI.JK':
    nama_perusahaan = "PT Bank Negara Indonesia (Persero) Tbk"
elif ticker == 'PNBN.JK':
    nama_perusahaan = "PT Bank Pan Indonesia Tbk"
elif ticker == 'ISAT.JK':
    nama_perusahaan = "PT Indosat Tbk"
elif ticker == 'JSMR.JK':
    nama_perusahaan = "PT Jasa Marga (Persero) Tbk"
elif ticker == 'LPGI.JK':
    nama_perusahaan = "PT Lippo General Insurance Tbk"
elif ticker == 'FREN.JK':
    nama_perusahaan = "PT Smartfren Telecom Tbk"
elif ticker == 'TLKM.JK':
    nama_perusahaan = "PT Telekomunikasi Indonesia Tbk"
elif ticker == 'EXCL.JK':
    nama_perusahaan = "PT XL Axiata Tbk"

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

