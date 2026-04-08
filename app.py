import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Futbol AI", page_icon="⚽")
st.title("⚽ Efsane Futbol Ansiklopedisi")

def futbol_bilgisi_getir(soru):
    with DDGS() as ddgs:
        # Önce web araması yapıp bilgi topluyoruz
        arama_sonucu = ddgs.text(f"{soru} futbol kariyeri", max_results=3)
        bilgi_metni = " ".join([r['body'] for r in arama_sonucu])
        
        # Yapay zekaya bu bilgiyi verip Türkçe yorumlatıyoruz
        # Yeni sürümde model ismini belirtmeden sadece chat(mesaj) kullanıyoruz
        komut = f"Sen sadece Türkçe konuşan bir futbol uzmanısın. Şu bilgilere dayanarak cevap ver: {bilgi_metni}. Soru: {soru}"
        
        # En güncel chat komutu budur:
        try:
            cevap = ddgs.chat(komut)
            return cevap
        except:
            # Eğer chat özelliği o an çalışmazsa direkt arama özetini veriyoruz
            return "Aradığın bilgiyi buldum: " + bilgi_metni[:500] + "..."

if prompt := st.chat_input("Hangi futbolcuyu merak ediyorsun?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Futbol arşivine bakıyorum..."):
            cevap = futbol_bilgisi_getir(prompt)
            st.markdown(cevap)
