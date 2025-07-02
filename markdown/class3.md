這份筆記已經很棒了！以下是我幫你**用簡單、國中生能看懂**的方式重新整理後的版本，也幫你排版、補充說明、修正錯字，讓你以後複習更清楚 👇

---

# 🔁 for 迴圈

### ✅ 基本用法

```python
for i in range(5):
    print(i, end=" ")
```

- `for` 是重複做事情的指令
- `range(5)` 會產生 0 到 4 的數字（不含 5）
- `i` 是一個變數，會把 `range` 裡的數字一個一個拿出來用

---

### ✅ range 的進階用法

```python
range(1, 6)  # 產生 1~5（不包含6）
range(1, 10, 2)  # 產生 1 3 5 7 9（每次+2）
```

---

### ✅ 用 for 跑出一段數字的總和

```python
a = int(input("請輸入一個數字："))
b = int(input("請輸入另一個數字："))
c = 0
for i in range(a, b + 1):
    c = c + i
print(f"{a}加到{b}的總和是{c}")
```

---

### ✅ 用公式算總和（不用 for 迴圈）

```python
a = int(input("請輸入一個數字："))
b = int(input("請輸入另一個數字："))
print(f"(({a} + {b}) * {b - a + 1}) / 2 = {((a + b) * (b - a + 1)) / 2}")
```

---

# 🌟 用 Streamlit 畫金字塔

````python
import streamlit as st

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
````

---

# 📋 list（清單）

### ✅ list 是什麼？

```python
print([])  # 空清單
print([1, 2, 3])  # 有3個元素
print([1, 2, 3, "a", "b", "c"])  # 可以放各種資料
print([1, 2, 3, ["a", "b", "c"]])  # 可以放另一個 list
```

---

### ✅ 讀取 list 的內容（從 index 0 開始）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[3])  # "a"
```

---

### ✅ list 的切片用法（跟 range 類似）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[::2])      # [1, 3, "b"]
print(L[1:4])      # [2, 3, "a"]
print(L[1:4:2])    # [2, "a"]
```

---

### ✅ list 的長度

```python
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6
```

---

# 🔁 用 for 跑 list 裡的東西

```python
L = ["Amy", "Mandy", "Peter"]

# 方法1：用 index
for i in range(len(L)):
    print(f"{i + 1}號是{L[i]}")

# 方法2：直接取值
number = 1
for name in L:
    print(f"{number}號是{name}")
    number += 1
```

---

### ✅ 多個 list 一起跑

```python
fruit = ["蘋果", "香蕉", "鳳梨"]
number = [3, 5, 6]

for i in range(len(fruit)):
    print(f"{fruit[i]}有{number[i]}個")
```

---

# 📦 call by value vs call by reference

### ✅ call by value（複製數值）

```python
a = 1
b = a
b = 2
print(a, b)  # a不會改變
```

### ✅ call by reference（同一個記憶體）

```python
a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)  # a也會被改到
```

### ✅ 用 `.copy()` 避免被改到

```python
a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)  # a 不會被改
```

---

# 🧱 list 的操作

### ✅ 加一個元素

```python
L = [1, 2, 3]
L.append(4)
print(L)  # [1, 2, 3, 4]
```

---

### ✅ 移除元素

#### 方法 1：用 remove（找值）

```python
L = ["a", "b", "c", "a"]
L.remove("a")  # 只移除第一個 "a"
```

#### 方法 2：用 pop（找位置）

```python
L = ["a", "b", "c", "d", "e"]
L.pop(0)  # 移除第0個
L.pop()   # 移除最後一個
print(L)
```

---

需要我幫你把這些筆記變成 PDF 或加插圖幫助記憶，也可以告訴我 😄
