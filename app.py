import streamlit as st
from duckduckgo_search import DDGS # Anahtarsız arama için

st.title("⚽ Efsane Futbol Ansiklopedisi")

def futbol_bilgisi_getir(soru):
    # Botun futbol dışına çıkmasını engellemek için arama sorgusunu daraltıyoruz
    arama_sorgusu = f"{soru} futbolcu kariyeri istatistikleri"
    with DDGS() as ddgs:
        # Web'den en güncel futbol bilgilerini çekiyoruz
        search_results = [r['body'] for r in ddgs.text(arama_sorgusu, max_results=3)]
        context = "\n".join(search_results)
        
        # Yapay zekaya bu bilgileri verip Türkçe yorumlatıyoruz
        talimat = f"Sen bir futbol uzmanısın. Şu bilgilere dayanarak sadece Türkçe ve futbol odaklı cevap ver: {context}. Soru: {soru}"
        answer = ddgs.chat(talimat, model='gpt-4o-mini')
        return answer

if prompt := st.chat_input("Hangi futbolcuyu veya takımı merak ediyorsun?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        cevap = futbol_bilgisi_getir(prompt)
        st.markdown(cevap)
