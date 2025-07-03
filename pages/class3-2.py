import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面

st.title("點餐機")

if "order" not in st.session_state:
    st.session_state.order = []

col1, col2 = st.columns(2)
a = col1.text_input("請輸入餐點名稱")
if col2.button("加入", key="add"):
    st.session_state.order.append(a)

st.write("### 購物籃")

for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    col1.write(st.session_state.order[i])
    if col2.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()
