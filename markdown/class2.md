這是一份很棒的 Python 上課筆記！我幫你**重新整理成簡單、國中生也能看懂的版本**，加上一些註解與說明，讓你以後複習更方便 👇

---

## 🧠 比較運算子（比大小、判斷相等）

這些是用來**比較兩個東西**的指令，結果會是 `True`（對）或 `False`（錯）。

```python
print(1 == 1)   # 等於，結果是 True（因為 1 等於 1）
print(1 != 1)   # 不等於，結果是 False（因為 1 不等於 1 是錯的）
print(1 > 1)    # 大於，結果是 False（因為 1 沒有大於 1）
print(1 < 1)    # 小於，結果是 False
print(1 >= 1)   # 大於等於，結果是 True
print(1 <= 1)   # 小於等於，結果是 True
```

---

## 🔁 邏輯運算子（判斷對錯的組合）

### `and`（而且） → 兩個都要對，才會是 `True`

```python
print(True and True)   # True
print(True and False)  # False
```

### `or`（或者） → 有一個對，就會是 `True`

```python
print(True or False)   # True
print(False or False)  # False
```

### `not`（不是） → 把對變成錯，把錯變成對

```python
print(not True)   # False
print(not False)  # True
```

---

## 🥇 運算順序（誰先做？）

以下是 Python 計算時的**優先順序**（從最先做的開始）：

1. `()` 括號
2. `**` 次方
3. `* / // %` 乘法、除法、整除、餘數
4. `+ -` 加減法
5. 比較運算（像是 `==`、`>`）
6. `not`
7. `and`
8. `or`

---

## 🔐 密碼門檢查程式

```python
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎Jeremy")
elif password == "123456":
    print("歡迎Jeffery")
elif password == "12345678":
    print("歡迎Tim")
else:
    print("密碼錯誤")
```

✅ 說明：

- 用 `if`、`elif`、`else` 來判斷密碼是誰的。
- `elif` 是「如果不是上面那個，再來判斷這個」的意思。
- 如果每次都用 `if`，電腦會每個都跑，比較慢。

---

## 🧪 成績等級判斷（用 Streamlit）

```python
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
```

💡 `st.number_input()` 是讓使用者輸入數字
💡 成績會根據範圍顯示 A 到 F

---

## 🖱️ 按鈕互動（Streamlit 小遊戲）

```python
st.markdown("---")
st.markdown("### 按鈕練習")

st.button("按我一下", key="button1")

if st.button("按我一下", key="ballons"):
    st.balloons()  # 畫面放氣球動畫

if st.button("按我一下", key="snow"):
    st.snow()  # 畫面下雪動畫
```

🔘 `st.button()`：在網頁上顯示一個按鈕
🎈 `st.balloons()`：點擊後會有氣球動畫
❄️ `st.snow()`：點擊後會有雪花動畫

---

如果你之後還有上到其他 Python 語法，也可以用這種簡單好記的方式整理出來唷！需要我幫你排版成 PDF、PPT 或更進階的筆記，也可以說 😄
