import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Futbol AI", page_icon="⚽")
st.title("⚽ Efsane Futbol Ansiklopedisi")

def futbol_bilgisi_getir(soru):
    try:
        with DDGS() as ddgs:
            # Sadece chat özelliğini deneyelim, daha hızlıdır
            komut = f"Sen sadece Türkçe konuşan bir futbol uzmanısın. Şu futbol sorusunu cevapla: {soru}"
            cevap = ddgs.chat(komut, model='gpt-4o-mini')
            if cevap:
                return cevap
            else:
                return "Maalesef şu an cevap oluşturulamadı."
    except Exception as e:
        # Hata olursa web araması ile şansımızı deneyelim
        return f"Şu an bir teknik sorun var, ama genel olarak şunu söyleyebilirim: {soru} futbol dünyasında önemli bir konudur. Lütfen 10 saniye sonra tekrar sor."

if prompt := st.chat_input("Bir futbolcu veya takım sor..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        cevap = futbol_bilgisi_getir(prompt)
        st.markdown(cevap)
