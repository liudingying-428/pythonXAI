import streamlit as st

st.title("這是標題")
st.write(
    "這是一個用·st,write·寫的文字,可以處理多種格式,例如Markdown、HTML、數字、文字等。"
)
st.text("這是一個用·st.text·寫的文字,只能處理純文字。")
st.markdown(
    """
# 這是一個用·st.markdown·寫的文字,可以處理Markdown語法。
例如
**粗體文字**
*斜體文字*
[連結](https://www.example.com)
＊代碼塊
```python
print("hello world!")
```
"""
)
