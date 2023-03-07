import streamlit as st
from streamlit_ace import st_ace
import io
import sys
import pandas as pd

TITLE = "RFM - Veriyi Anlama ve Hazırlama"
st.set_page_config(
    page_title=TITLE,
    page_icon="📈"
)

st.title(TITLE)
st.markdown("## Adım 1:")
st.markdown("- flo_data_20K.csv verisini okuyunuz. Dataframe’in kopyasını oluşturunuz.")

show_tip = False  # Initially hide the tip code
show_answer = False  # Initially hide the answer code
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta1"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa1"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("df_ = ....\n"
            "df = df_.copy()"
            , language="python")
if show_answer:
    st.code("df_ = pd.read_csv('datasets/flo_data_20k.csv')\n"
            "df = df_.copy()"
            , language="python")

st.markdown("## Adım 2:")
st.markdown("####  _Veri Setinde_")
st.markdown("- İlk 10 gözlem")
st.markdown("- Veri Setinde değişken isimleri")
st.markdown("- Veri Setinde boyut bilgisi")
st.markdown("- Veri Setinde betimsel istatistik")
st.markdown("- Veri Setinde değişken tipleri, incelemesi")
show_tip = False  # Initially hide the tip code
show_answer = False  # Initially hide the answer code
col1, col2 = st.columns(2)

with col2:
    if st.button("Cevap 🔑", key="sa2"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_answer:
    st.code("""# a. The first 10 observations
df.head(10)\n
# b. Variable names
df.columns\n
# c. Variable names
df.shape\n
# d. Descriptive statistics
df.describe().T\n
# e. Null value
df.isnull().sum()\n
# f. Variable types, review.
df.info()  # df.dtypes gives only types
"""
            , language="python")
st.markdown("## Adım 3: ")
st.markdown(
    "- Omnichannel müşterilerin hem online'dan hem de offline platformlardan alışveriş yaptığını ifade etmektedir. Her bir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.")
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta3"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa3"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("""
# Değişken isimlerine tekrar göz atıp, uygun online ve offline içeren değişkenleri kullanınız
# df["order_num_total"] = df[...] + df[...]
# df["customer_value_total"] = df[...] + df[...]
    """
            , language="python")
if show_answer:
    st.code("""
#.astype(int) gerekli değil, sadece ondalıkları kaldırmak adına yazıldı
df["order_num_total"] = (df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]).astype(int)
df["customer_value_total"] = df["customer_value_total_ever_online"] + df["customer_value_total_ever_offline"]
    """
            , language="python")

st.markdown("## Adım 4: ")
st.markdown(
    "- Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz")
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta4"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa4"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("""
# date_cols = [col for col in df.columns if "..." in col]
# df[...] = df[...].astype("datetime64[ns]")
    """
            , language="python")
if show_answer:
    st.code("""
date_cols = [col for col in df.columns if "date" in col]
df[date_cols] = df[date_cols].astype("datetime64[ns]")
    """
            , language="python")

st.markdown("## Adım 5: ")
st.markdown(
    "- Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısının ve toplam harcamaların dağılımına bakınız.")
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta5"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa5"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("""
df.groupby("...").agg({ "...": "...",
                        "...": "sum",
                        "...": "..."
                    })
    """
            , language="python")
if show_answer:
    st.code("""
df.groupby("order_channel").agg({"master_id": "count",
                "order_num_total": "sum",
                "customer_value_total": "sum"})
    """
            , language="python")

st.markdown("## Adım 6: ")
st.markdown(
    "- En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.")
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta6"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa6"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("""
df.sort_values(by="...", ascending=...).head(...).reset_index()
    """
            , language="python")
if show_answer:
    st.code("""
df.sort_values(by="customer_value_total", ascending=False).head(10).reset_index()
    """
            , language="python")

st.markdown("## Adım 7: ")
st.markdown(
    "- En fazla siparişi veren ilk 10 müşteriyi sıralayınız.")
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta7"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa7"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("""
Adım 6'daki işlemin aynısı, sadece değişken adı değiştirilmeli
    """
            , language="python")
if show_answer:
    st.code("""
df.sort_values(by="order_num_total", ascending=False).head(10).reset_index()
    """
            , language="python")

st.markdown("## Adım 8: ")
st.markdown(
    "- Veri ön hazırlık sürecini fonksiyonlaştırınız")
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta8"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa8"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("""
# df'i etkliyen adımlarda yaptıklarımızı fonksiyon içerisinde yazıyoruz
def prepare_data(dataframe):
    ...
    ...
    ...
    return dataframe
    """
            , language="python")
if show_answer:
    st.code("""
def prepare_data(dataframe):    
    # Creating new variables for each customer's total purchases and spend.
    dataframe["order_num_total"] = (
            dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]).astype(int)
    dataframe["customer_value_total"] = dataframe["customer_value_total_ever_online"] + dataframe[
        "customer_value_total_ever_offline"]
    # Change the type of variables that express date to date.
    date_columns = [col for col in dataframe.columns if "date" in col]
    dataframe[date_columns] = dataframe[date_columns].astype("datetime64[ns]")
    return dataframe
"""
            , language="python")
