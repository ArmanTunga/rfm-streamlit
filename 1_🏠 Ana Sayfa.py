import streamlit as st

TITLE = "RFM - Ana Sayfa"
st.set_page_config(
    page_title=TITLE,
    page_icon="📈"
)
st.sidebar.success("Select a page above")
st.title("RFM Analizi ile Müşteri Segmentasyonu")
st.image("src/rfm-segments.png", caption="RFM Segments")
st.markdown(
    """
    Recency, Frequency, Monetary kelimelerinin baş harflerinden oluşup, bu üç metriğin hesaplanmasından sonra birleştirilmesiyle meydana gelen bir skordur. Müşterilerin mevcut durumunun analiz edilip, bu skorlara göre segmentlere ayrılmasına yardımcı olur.

**Recency:** Müşterinin en son alışverişi üzerinden geçen zamanı belirtir.

**Frequency:** Müşterinin ne sıklıkla alışveriş yaptığını gösteren metriktir.

**Monetary:** Müşterinin harcamalarının toplamıdır.
    """
)

st.markdown("---\n## Ödev")
st.markdown(
    "FLO'nun veriseti kullanılarak RFM Analizi ile Müşteri Segmentasyonu yapılması")
