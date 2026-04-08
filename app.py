import streamlit as st
import google.generativeai as genai

st.title("⚽ Futbol Botu")

# Ayarlardaki kutudan anahtarı alır
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# MODEL İSMİ BURADA: En sorunsuz ismi yazdım
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("Sorunuzu yazın:")

if prompt:
    try:
        response = model.generate_content(prompt)
        st.write(response.text)
    except Exception as e:
        st.error(f"Hata çıktı: {e}")
