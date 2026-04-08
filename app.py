import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Futbol AI", page_icon="⚽")
st.title("⚽ Efsane Futbol Ansiklopedisi")

# Botun karakterini ve dilini en başta belirliyoruz
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Sen sadece futbol uzmanısın. Sadece Türkçe konuşabilirsin. Dünyadaki tüm futbolcuları, kupaları ve futbol tarihini çok iyi biliyorsun."}
    ]

# Eski mesajları ekranda göster
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Kullanıcıdan soru al
if prompt := st.chat_input("Messi kaç kupa kazandı?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with DDGS() as ddgs:
                # 'text' yerine doğrudan 'chat' özelliğini kullanarak yapay zekaya soruyoruz
                # Bu yöntem daha kararlı çalışır
                cevap = ddgs.chat(f"Futbol uzmanı olarak Türkçe cevapla: {prompt}", model='gpt-4o-mini')
                if cevap:
                    st.markdown(cevap)
                    st.session_state.messages.append({"role": "assistant", "content": cevap})
                else:
                    st.warning("Şu an cevap hazırlanamadı, lütfen tekrar dene.")
        except Exception:
            st.error("Bağlantı hatası! Lütfen 1 dakika bekleyip tekrar sor.")
