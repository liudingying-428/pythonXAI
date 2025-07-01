import streamlit as st

with st.expander("Class1 課堂筆記"):
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

with st.expander("Class2 課堂筆記"):
    st.write(
        """
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

* 用 `if`、`elif`、`else` 來判斷密碼是誰的。
* `elif` 是「如果不是上面那個，再來判斷這個」的意思。
* 如果每次都用 `if`，電腦會每個都跑，比較慢。

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

        """
    )
