import streamlit as st
import google.generativeai as genai

# Sayfa Başlığı
st.title("⚽ Futbol Botu")

# API Anahtarını Secrets'tan al
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Anahtarı bulunamadı! Lütfen Secrets ayarlarına bakın.")

# --- EN ÖNEMLİ KISIM BURASI ---
# Eğer gemini-1.5-flash hata verirse otomatik olarak gemini-pro deneyecek
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    model = genai.GenerativeModel('gemini-pro')
# ------------------------------

prompt = st.text_input("Sorunuzu yazın:")

if prompt:
    try:
        # Bu satır artık hata vermemeli
        response = model.generate_content(prompt)
        st.write(response.text)
    except Exception as e:
        st.error(f"Hata oluştu: {e}")

