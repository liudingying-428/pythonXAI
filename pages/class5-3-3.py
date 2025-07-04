import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "history" not in st.session_state:
    st.session_state.history = []

history = st.session_state.history

col1, col2, col3 = st.columns([10, 4, 1])

with col1:
    sys_msg = st.text_input("系統訊息", "請用繁體中文進行後續對話")

with col2:
    model = st.selectbox("AI模型", ["gpt-4o-mini", "gpt-4o"])

with col3:
    if st.button("🗑️"):
        st.session_state.history = []
        st.rerun()

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪄").write(message["content"])
    else:
        st.chat_message("assistant", avatar="✨").write(message["content"])

prompt = st.chat_input("請輸入想要的訊息")
if prompt:
    history.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model=model, messages=[{"role": "system", "content": sys_msg}] + history
    )
    assistant_message = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_message})
    st.rerun()
