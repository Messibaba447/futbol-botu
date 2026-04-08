import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Futbol AI", page_icon="⚽")
st.title("⚽ Efsane Futbol Ansiklopedisi")

def futbol_bilgisi_getir(soru):
    with DDGS() as ddgs:
        # Web araması yapıp bilgi topluyoruz
        arama_sonucu = ddgs.text(f"{soru} futbol bilgisi", max_results=3)
        bilgi_metni = " ".join([r['body'] for r in arama_sonucu])
        
        # Kesin talimat: Türkçe konuş!
        komut = f"SEN SADECE TÜRKÇE KONUŞAN BİR FUTBOL UZMANISIN. ASLA İNGİLİZCE CEVAP VERME. Soru: {soru}. Bilgi: {bilgi_metni}"
        
        try:
            cevap = ddgs.chat(komut)
            return cevap
        except:
            return "Üzgünüm, şu an futbol arşivine ulaşamadım. Lütfen tekrar sor."

if prompt := st.chat_input("Hangi futbolcuyu merak ediyorsun?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Futbol arşivini Türkçe olarak tarıyorum..."):
            cevap = futbol_bilgisi_getir(prompt)
            st.markdown(cevap)
