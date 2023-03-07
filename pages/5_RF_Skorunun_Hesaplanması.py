import streamlit as st

TITLE = "RFM - RF Skorunun Hesaplanması"
st.set_page_config(
    page_title=TITLE,
    page_icon="📈"
)

st.title("RF Skorunun Hesaplanması")

st.markdown("## Adım 1-2:")
st.markdown("1. Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çeviriniz. ")
st.markdown("2. Bu skorları recency_score, frequency_score ve monetary_score olarak kaydediniz.")

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
# pd.qcut() methodu verilen değişkeni çeyrekliklere ayırıp,
# o çeyrekliklerde kalan değerlere etiket atamaya yarıyor.
# Bir tane değişkenimiz için, bazı değerler çok fazla tekrar ettiği için
# bu değerler birden fazla çeyreklikte gözlemleniyor. (10,10,10,10,20,30)
# değerlerine bakıldığında; 10 hem 0%-25% hem de 50%-75% içerisinde bulunacak.👎
# Bundan dolayı; rfm["..."].rank(method="first") methodunu kullanmamız gerekiyor.

rfm["..."] = pd.qcut(rfm["..."], 5, labels=["5", "4", "3", "2", "1"])
rfm["..."] = pd.qcut(rfm["..."], 5, labels=["1", "2", "3", "4", "5"])
rfm["..."] = pd.qcut(rfm["..."], 5, labels=["1", "2", "3", "4", "5"])

        """
            , language="python")
if show_answer:
    st.code("""
rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=["5", "4", "3", "2", "1"])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=["1", "2", "3", "4", "5"])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=["1", "2", "3", "4", "5"])    
"""
            , language="python")

st.markdown("## Adım 3:")
st.markdown("- recency_score ve frequency_score’u tek bir değişken olarak ifade ediniz ve RF_SCORE olarak kaydediniz.")

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
# 💡 Stringlerde metin birleştirme: Matematiksel işlemler için kullandığımız
# “+” operatörü ile python üzerinde string toplama yapmamız mümkündür.
# Fakat bizim değişkenlerimiz int tipinde? 🔑 .astype()
rfm["RF_SCORE"] = ...
"""
            , language="python")
if show_answer:
    st.code("""
rfm["RF_SCORE"] = rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str)
"""
            , language="python")
