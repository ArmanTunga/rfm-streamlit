import streamlit as st

TITLE = "RFM - RFM Metriklerinin Hesaplanması"
st.set_page_config(
    page_title=TITLE,
    page_icon="📈"
)

st.title(TITLE)

st.markdown("## Adım 1-2-3:")
st.markdown("1. Recency, Frequency ve Monetary tanımlarını yapınız.")
st.markdown("2. Müşteri özelinde Recency, Frequency ve Monetary metriklerini hesaplayınız.")
st.markdown("3. Hesapladığınız metrikleri rfm isimli bir değişkene atayınız")
st.markdown("- 📢 recency değerini hesaplamak için analiz tarihini maksimum tarihten 2 gün sonrası seçebilirsiniz.")
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
    st.code("""
# Bu 3 satır kod otomatik olarak en son verilen sipariş tarihine 2 gün ekler ve today_date'e eşitlerlast_order_date = df["last_order_date"].max()
last_order_date = df["last_order_date"].max()
last_order_date = dt.datetime.strptime(str(last_order_date), "%Y-%m-%d %H:%M:%S")
today_date = last_order_date + dt.timedelta(days=2)
# ---
rfm = df.groupby("...").agg({   "...": lambda date: (... - date.iloc[0]).days,
                                "...": lambda num: num,
                                "...": lambda value: value,
                            })
rfm = rfm.reset_index()
rfm.columns = ["customer_id", "...", "...", "..."]

        """
            , language="python")
if show_answer:
    st.code("""
last_order_date = df["last_order_date"].max()
last_order_date = dt.datetime.strptime(str(last_order_date), "%Y-%m-%d %H:%M:%S")
today_date = last_order_date + dt.timedelta(days=2)

rfm = df.groupby("master_id").agg({"last_order_date": lambda date: (today_date - date.iloc[0]).days,
                                   "order_num_total": lambda num: num,
                                   "customer_value_total": lambda value: value,
                                   })
rfm = rfm.reset_index()
rfm.columns = ["customer_id", "recency", "frequency", "monetary"]    
"""
            , language="python")

st.markdown("## Adım 4:")
st.markdown("- Oluşturduğunuz metriklerin isimlerini  recency, frequency ve monetary olarak değiştiriniz.")
show_tip = False  # Initially hide the tip code
show_answer = False  # Initially hide the answer code
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta2"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa2"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("""
# İlk olarak indexi resetlememiz gerekiyor
rfm = ...
# Sonrasında ise değişken adlarını değiştirmeliyiz
rfm.columns = ["customer_id", "...", "...", "..."]

        """
            , language="python")
if show_answer:
    st.code("""
rfm = rfm.reset_index()
rfm.columns = ["customer_id", "recency", "frequency", "monetary"]    
"""
            , language="python")
