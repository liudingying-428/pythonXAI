import streamlit as st

# a = st.number_input("請輸入一個整數", min_value=1, max_value=9, value=1, step=1)

# for i in range(1, a + 1):
#     st.write(str(i) * i)

b = st.number_input("請輸入一個整數", min_value=1, max_value=9, value=1, step=1)
line = ""

for i in range(1, b + 1):
    space = " " * (b - i)
    stars = "*" * (2 * i - 1)
    line = line + space + stars + "\n"

for i in range(1, b + 1):
    space = " " * (b - 1)
    stars = "*" * 1
    line = line + space + stars + "\n"
st.markdown(f"```\n{line}```")
