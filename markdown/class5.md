太棒了！這是一份非常完整的上課筆記，已經涵蓋了許多 Python 與 Streamlit 的實用指令。以下是我幫你整理的重點筆記，用 **簡單、國中生能看懂的方式**，方便你日後複習！

---

## 🧠 Python 字典 dict 教學

### ✅ 什麼是 dict？

是一種用來存「一組資料」的方式，格式是：`{"key": value}`，像是：

```python
d = {"a": 1, "b": 2, "c": 3}
```

---

### 🔑 取得所有 key（名字）

```python
print(d.keys())  # dict_keys(['a', 'b', 'c'])
for key in d.keys():
    print(key)
```

---

### 📦 取得所有 value（值）

```python
print(d.values())  # dict_values([1, 2, 3])
for value in d.values():
    print(value)
```

---

### 🔄 同時拿到 key 和 value

```python
print(d.items())
# dict_items([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():
    print(key, value)
```

---

### ➕ 新增或修改資料

```python
d["d"] = 4  # 新增
d["a"] = 5  # 修改
print(d)
```

---

### ❌ 刪除資料

```python
print(d.pop("a"))  # 刪除並回傳 5
print(d.pop("e", "Not Found"))  # 沒有的話給預設值
```

---

### ❓ 檢查有沒有某個 key

```python
print("a" in d)  # True
print("e" in d)  # False
```

---

### 🧩 複雜一點的 dict

```python
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1, 2, 3]
print(d["a"][0])  # 1
print(d["b"]["c"])  # 4
```

---

## 🖼️ Streamlit 顯示圖片元件

```python
st.image("image/apple.png", width=300)  # 顯示圖片，設定寬度
```

### 🔁 顯示資料夾所有圖片

```python
image_files = os.listdir("image")
for image_file in image_files:
    st.image(f"image/{image_file}", use_container_width=True)
```

---

## 🛒 Streamlit 購物平台練習

- 商品用 list of dict 表示
- 可以**購買（扣庫存）**和**新增庫存**

```python
# 範例商品
products = [
    {"name": "apple", "price": 10, "stock": 10, "image": "apple.png"},
]
```

- 顯示商品（自動排版）
- 按鈕購買，會更新庫存
- 下方用 selectbox 和 number_input 新增庫存

---

## 💬 Streamlit 聊天功能

### 🗨️ 顯示對話泡泡

```python
st.chat_message("user").write("你好")
st.chat_message("assistant").write("哈囉")
```

### 🕘 聊天記錄儲存在 session_state

```python
if "history" not in st.session_state:
    st.session_state.history = []
```

### ✏️ 輸入框輸入訊息 + 自動重整頁面顯示

```python
prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()
```

---

## 🤖 用 OpenAI API 和 AI 對話（終端機版）

### 基本結構

```python
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "請用繁體中文進行後續對話"},
        {"role": "user", "content": user_input},
    ],
)
```

### 💬 多輪對話版本

使用 `messages` 把每次對話都記下來：

```python
messages = [{"role": "system", "content": "請用繁體中文進行後續對話"}]
# 每次輸入後 append，AI 回應後也 append
```

---

## 🗑️ Streamlit 對話清除按鈕 + 模型選擇

```python
col1, col2, col3 = st.columns([10, 4, 1])
# col1: 系統訊息輸入
# col2: 模型下拉選單
# col3: 🗑️ 清除紀錄按鈕
```

---

如果你想要，我也可以幫你這些筆記**整理成 PDF、簡報或 Markdown 檔案**喔，適合分享或列印複習用！要嗎？
