import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Futbol Botu")
st.title("⚽ Futbol Bilgi Botu")

# 1. API Anahtarını Ayarlardan Çek
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Lütfen Secrets kısmına API anahtarınızı ekleyin.")
    st.stop()

# 2. En Garantili Modeli Tanımla
# Hata almamak için doğrudan ismi yazıyoruz
model = genai.GenerativeModel('gemini-1.5-flash')


# 3. Kullanıcı Girişi
soru = st.text_input("Sorunuzu buraya yazın:")

if soru:
    try:
        with st.spinner("Cevap hazırlanıyor..."):
            response = model.generate_content(soru)
            st.success("İşte cevabın:")
            st.write(response.text)
    except Exception as e:
        # Hata olursa ne olduğunu ekrana yazdırır
        st.warning("Bir sorun oluştu. Lütfen API anahtarınızın güncel olduğundan emin olun.")
        st.error(f"Hata detayı: {e}")

st.divider()
st.caption("Futbol Botu v1.0")
