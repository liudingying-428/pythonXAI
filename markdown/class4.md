太棒了！以下是把你今天學到的 Python 指令整理成**一份國中生也能懂的簡單筆記**，讓你複習更方便！

---

## 📂 開啟和讀取檔案

```python
f = open("檔案路徑", "r")
內容 = f.read()
print(內容)
f.close()
```

**說明**：開啟檔案、讀取後，記得用 `f.close()` 關掉。

更簡單的寫法（自動幫你關掉檔案）：

```python
with open("檔案路徑", "r") as f:
    內容 = f.read()
    print(內容)
```

---

## 📦 資料儲存：變數、list、字典

### ✅ call by value / reference

```python
a = 1
b = a  # b只是複製a的值
b = 2
print(a, b)  # 不會影響a
```

```python
a = [1, 2, 3]
b = a  # b和a指向同一個 list
b[0] = 2
print(a, b)  # a也會變
```

```python
a = [1, 2, 3]
b = a.copy()  # 複製一份新的，互不影響
b[0] = 2
print(a, b)
```

---

## ➕ List 常用操作

```python
L = [1, 2, 3]
L.append(4)  # 加到最後
L.remove("a")  # 移除第一個 "a"
L.pop(0)  # 移除第0個
L.pop()  # 移除最後一個
```

---

## 📚 算數指定運算子

| 寫法      | 意思         |
| --------- | ------------ |
| `a += 1`  | a = a + 1    |
| `a -= 1`  | a = a - 1    |
| `a *= 2`  | a = a \* 2   |
| `a /= 2`  | a = a / 2    |
| `a //= 2` | a = a // 2   |
| `a %= 2`  | a = a % 2    |
| `a **= 2` | a = a \*\* 2 |

---

## 🔢 運算子優先順序

1. `()` 括號
2. `**` 次方
3. `* / // %` 乘除
4. `+ -` 加減
5. 比較運算子 `== != > < >= <=`
6. `not`、`and`、`or`
7. 指定運算子 `= += -= ...`

---

## 🔁 while 迴圈 & break

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

```python
i = 0
while i < 5:
    print(i)
    if i == 3:
        break  # 跳出 while 迴圈
    i += 1
```

---

## 🎲 random 模組

```python
import random
print(random.randrange(7))  # 0~6
print(random.randrange(1, 6))  # 1~5
print(random.randint(1, 6))  # 1~6（包含6）
```

---

## 🎮 終端機猜數字遊戲

```python
import random
answer = random.randint(1, 100)
min_value = 1
max_value = 100

while True:
    number = int(input(f"請輸入{min_value}到{max_value}的數字："))
    if number < min_value or number > max_value:
        print("超出範圍")
    elif number == answer:
        print("猜中了！")
        break
    elif number < answer:
        min_value = number
        print("再大一點！")
    else:
        max_value = number
        print("再小一點！")
```

---

## 📖 字典（dict）

```python
d = {"a": 1, "b": 2, "c": 3}
```

### 成績查詢小系統

```python
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65]},
    "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63]},
}
print(grade["小明"]["數學"])  # 小明數學成績
print(grade["小美"]["國文"][0])  # 小美第一次國文
```

---

## 🖼️ Streamlit UI 元件

### 按鈕 + 分欄

```python
import streamlit as st
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

### with 語法 + 特效

```python
with col1:
    if st.button("按鈕"):
        st.balloons()
        st.write("這是col1")
```

### 文字輸入欄

```python
text = st.text_input("請輸入文字", value="預設文字")
st.write(f"你輸入了：{text}")
```

---

## 🛒 Streamlit 點餐機

```python
if "order" not in st.session_state:
    st.session_state.order = []

col1, col2 = st.columns(2)
item = col1.text_input("輸入餐點")
if col2.button("加入"):
    st.session_state.order.append(item)

for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    col1.write(st.session_state.order[i])
    if col2.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()
```

---

## 🔄 Streamlit 重新整理

```python
if st.button("重新整理"):
    st.success("準備重新整理")
    time.sleep(3)
    st.rerun()
```

---

這樣整理後，你可以很快地回顧今天的重點。如果你想要我幫你做成 PDF 筆記、簡報、或是加上圖片說明，也可以告訴我哦！💡
