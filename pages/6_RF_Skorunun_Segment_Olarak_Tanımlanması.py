import streamlit as st

TITLE = "RFM - RF Skorunun Segment Olarak Tanımlanması"
st.set_page_config(
    page_title=TITLE,
    page_icon="📈"
)

st.title("RF Skorunun Segment Olarak Tanımlanması")

st.markdown("## Adım 1-2:")
st.markdown("1. Oluşturulan RF skorları için segment tanımlamaları yapınız.")
st.markdown("2. Aşağıdaki seg_map yardımı ile skorları segmentlere çeviriniz.")
st.code("""
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}
""", language="python")
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
#🤔 .replace(..., regex=True)
rfm["segment"] = 
        """
            , language="python")
if show_answer:
    st.code("""
    seg_map = {
    ...
    }
rfm["segment"] = rfm["RF_SCORE"].replace(seg_map, regex=True)
"""
            , language="python")
