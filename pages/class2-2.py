import streamlit as st

st.title("練習")
number = st.number_input("請輸入成績", min_value=0, max_value=100, value=0, step=1)
st.write(f"您輸入的成績是：{number}")
if number >= 90:
    st.write("A")
elif number >= 80:
    st.write("B")
elif number >= 70:
    st.write("C")
elif number >= 60:
    st.write("D")
else:
    st.write("F")

st.markdown("---")
st.markdown("### 按鈕練習")
# st.button()可以在網頁上顯示ㄧ個按鈕，使用者可以點擊按鈕
# key是按鈕的識別名稱，可以用來區分不同的按鈕
# 如果使用者點擊按鈕，st.button()會回傳True，否則回傳False
st.button("按我一下", key="button1")
if st.button("按我一下", key="ballons"):
    st.balloons()
if st.button("按我一下", key="snow"):
    st.snow()
st.markdown("---")

st.markdown("奇偶數判斷器")
number = st.number_input("請輸入一個整數", value=0, step=1)
if number % 2 == 0:
    st.write("您輸入的數字是偶數")
else:
    st.write("您輸入的數字是奇數")

# type for tests
print("Hello World")
