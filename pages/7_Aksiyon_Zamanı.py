import streamlit as st

TITLE = "RFM - Aksiyon Zamanı"
st.set_page_config(
    page_title=TITLE,
    page_icon="📈"
)

st.title(TITLE)

st.markdown("## Adım 1:")
st.markdown("- Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.")

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
.groupby("...")[...].mean()
        """
            , language="python")
if show_answer:
    st.code("""
rfm.groupby("segment")["recency", "frequency", "monetary"].mean()
"""
            , language="python")

st.markdown("## Adım 2:")
st.markdown("- RFM analizi yardımıyla aşağıda verilen 2 case için ilgili profildeki müşterileri "
            "bulun ve müşteri id'lerini csv olarak kaydediniz")
st.markdown("-    - a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor."
            "Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde."
            "Bu nedenle markanın tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle "
            "özel olarak iletişime geçmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers)"
            " ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kurulacak müşteriler."
            "Bu müşterilerin id numaralarını csv dosyasına kaydediniz")
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
# .isin() methodu ile segmenti
# loyal_customers ve champions olan müşterileri bulalım
# Sonrasında ise bu müşterilerden interested_in_categories_12
# değişkeni KADIN olanları bulalım
# 🔑 .str.contains("KADIN")
"""
            , language="python")
if show_answer:
    st.code("""
loyal_customers_champions = rfm[rfm["segment"].isin(["loyal_customers", "champions"])]["customer_id"]
new_brand_target_customer_id = (
    df  # From our first df
    .loc[df["master_id"].isin(loyal_customers_champions) &  # Find loyal customers(loyal customers and champions) AND
        df["interested_in_categories_12"].str.contains("KADIN")]  # Find
    ["master_id"]
)
new_brand_target_customer_id.name = "customer_id"  # Change name attribute from master_id to customer_id
new_brand_target_customer_id.to_csv("datasets/new_brand_target_customer_id.csv")  # save to csv

"""
            , language="python")

st.markdown(
    "-    - b. Erkek ve Çocuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili "
    "kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir alışveriş yapmayan"
    " kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef"
    " alınmak isteniyor. Uygun profildeki müşterilerin id'lerini csv dosyasına kaydediniz.")
show_tip = False  # Initially hide the tip code
show_answer = False  # Initially hide the answer code
col1, col2 = st.columns(2)
with col1:
    if st.button("İpucu 💡", key="ta3"):
        show_tip = not show_tip  # Toggle the value of show_answer
with col2:
    if st.button("Cevap 🔑", key="sa3"):
        show_answer = not show_answer  # Toggle the value of show_answer

if show_tip:
    st.code("""
# a şıkkındaki gibi .isin() methodunu kullanabiliriz
# .str.contains("ERKEK|COCUK") | (pipe) = veya
"""
            , language="python")
if show_answer:
    st.code("""
target_customers = rfm[rfm["segment"].isin(["cant_loose", "hibernating", "new_customers"])]["customer_id"]
discount_target_customer_ids = (
    df
    .loc[df["master_id"].isin(target_customers) &
        df["interested_in_categories_12"].str.contains("ERKEK|COCUK")
        ]
)
discount_target_customer_ids.name = "customer_id"
discount_target_customer_ids.to_csv("datasets/discount_target_customer_ids.csv")
"""
            , language="python")
