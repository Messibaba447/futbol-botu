import streamlit as st
import google.generativeai as genai

# En basit bağlantı yolu
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("⚽ Futbol Botu")
soru = st.text_input("Sorunuzu yazın:")

if soru:
    response = model.generate_content(soru)
    st.write(response.text)
