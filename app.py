import streamlit as st
import google.generativeai as genai

# SAYFA AYARLARI
st.set_page_config(page_title="Futbol AI", page_icon="⚽")
st.title("⚽ Efsane Futbol Ansiklopedisi")

# BURAYA ALDIĞIN ANAHTARI YAZ
GOOGLE_API_KEY = "AIzaSyAu0jEIx1MWY52ft0M8scKaaEzh1HDLags"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


# BOTUN KURALI
talimat = "Sen sadece futbol uzmanısın. Sadece Türkçe konuş. Dünyadaki tüm futbolcuları ve tarihini biliyorsun."

if prompt := st.chat_input("Messi'yi sor..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        # Yapay zekaya soruyu gönderiyoruz
        response = model.generate_content(f"{talimat} Soru: {prompt}")
        st.markdown(response.text)
