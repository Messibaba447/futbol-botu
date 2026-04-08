# Kullanılabilir modelleri listele ve uygun olanı seç
try:
    # Önce en yeniyi dene
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Test et
    model.generate_content("test")
except:
    try:
        # Olmazsa bir öncekini dene
        model = genai.GenerativeModel('gemini-pro')
    except:
        st.error("Maalesef API anahtarınız şu anki modellere erişemiyor.")
