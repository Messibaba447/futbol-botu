import streamlit as st
import google.generativeai as genai

st.title("⚽ Futbol Botu Test")

# API Kontrolü
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)

    # Model seçimi - En güvenli yöntem
    model = genai.GenerativeModel('gemini-1.5-flash')

    soru = st.text_input("Bir soru yazın:")
    if soru:
        response = model.generate_content(soru)
        st.write(response.text)
except Exception as e:
    st.error(f"Sistemsel bir sorun oluştu: {e}")
    st.info("Lütfen sağ alttan 'Reboot App' yapın.")

