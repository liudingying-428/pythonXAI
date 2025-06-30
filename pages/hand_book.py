import streamlit as st

st.write(
    """
# class1 課堂筆記

以下是把你今天上課學到的 Python 指令，用**簡單、國中生能看懂**的方式整理成的筆記，幫助你複習！

---

# 🐍 Python 基礎筆記 (國中版)

---

## 🖨️ 1. 顯示文字：`print()`

我們用 `print()` 來把東西「印」在螢幕上，也就是顯示出來。

```python
print("hello")
print("hello world!")
```

---

## 📝 2. 註解：寫給人看的說明（不會被執行）

* 單行註解：用 `#` 開頭
* 多行註解：用 `\"\"\"` 包起來

```spython
# 這是單行註解
\"\"\"
這是多行註解
可以寫很多行～
\"\"\"
```

---

## 🔢 3. 基本資料型態（程式看資料的「種類」）

| 類型          | 範例                | 說明        |
| ----------- | ----------------- | --------- |
| 整數 `int`    | `1`, `-5`         | 沒有小數的數字   |
| 浮點數 `float` | `1.0`, `3.14`     | 有小數的數字    |
| 字串 `str`    | `"apple"`, `"你好"` | 文字或句子     |
| 布林值 `bool`  | `True`, `False`   | 表示「對」或「錯」 |

```python
print(1)
print(1.0)
print("apple")
print(True)
print(False)
```

---

## 🧠 4. 變數：幫資料取名字

```python
a = 10
print(a)  # 顯示變數a的值
a = "apple"
print(a)
```

---

## ➕ 5. 運算子（加減乘除）

| 符號   | 意義         |
| ---- | ---------- |
| `+`  | 加法         |
| `-`  | 減法         |
| `*`  | 乘法         |
| `/`  | 除法         |
| `**` | 次方（乘自己）    |
| `%`  | 餘數         |
| `//` | 整數除法（不要小數） |

```python
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)
print(2 ** 3)  # 2的三次方 = 8
print(10 % 3)  # 餘數是1
print(10 // 3)  # 商是3
```

---

## 📚 6. 運算順序（就像數學裡的先後順序）

1. `()` 括號最優先
2. `**` 次方
3. `* / // %`
4. `+ -`

---

## 🔤 7. 字串運算（用在文字）

```python
print("hello" + "world")  # 接起來變成 helloworld
print("hi!" * 3)  # 重複顯示三次
```

---

## 🧩 8. 字串格式化（變數插進文字裡）

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

---

## 📏 9. `len()` 看字串長度（有幾個字）

```python
print(len("hello"))  # 5個字
```

---

## 🔍 10. `type()` 看資料型態

```python
print(type(1))  # int
print(type("hi"))  # str
print(type(True))  # bool
```

---

## 🔄 11. 資料型態轉換

```python
print(int(1.2))       # 轉成整數：1
print(float(1))       # 轉成小數：1.0
print(str(123))       # 轉成字串："123"
print(bool(0))        # 轉成布林：False（0是False，其他是True）
```

---

## 🎤 12. 輸入 `input()`（讓使用者輸入資料）

🔺輸入進來的都是「字串」，如果要算數學記得轉換型態！

```python
a = input("請輸入底：")
b = input("請輸入高：")
area = (int(a) * int(b)) / 2
print(f"三角形面積是：{area}")
```

```python
r = input("圓的半徑：")
pi = 3.14
area = pi * float(r) ** 2
print(f"圓的面積是 {area}")
```

---

## 🌐 13. Streamlit 入門（用來做網頁介面）

````python
import streamlit as st

st.title("這是標題")

st.write("這是用 st.write 寫的文字，可以顯示很多種格式")

st.text("這是 st.text，只能顯示純文字")

st.markdown(\"\"\"
# 用 Markdown 寫的標題
**粗體文字**
*斜體文字*
[連結](https://www.example.com)

```python
print("hello world!")
````

"""
)
