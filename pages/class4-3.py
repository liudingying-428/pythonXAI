import streamlit as st
import os
import time

st.title("購物平台")


# 初始化商品資料（只做一次）
if "products" not in st.session_state:
    st.session_state.products = [
        {"name": "apple", "price": 10, "stock": 10, "image": "apple.png"},
        {"name": "banana", "price": 10, "stock": 10, "image": "banana.png"},
        {"name": "bg", "price": 10, "stock": 10, "image": "bg.png"},
        {"name": "orange", "price": 10, "stock": 10, "image": "orange.png"},
    ]

products = st.session_state.products  # 使用 session 裡的商品資料
image_folder = "image"

cols_per_row = st.number_input("請輸入欄位數", min_value=1, max_value=5, value=2)

# ----------- 商品顯示區（自動排版）-----------

for i in range(0, len(products), cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(products):
            product = products[i + j]
            with cols[j]:
                st.image(f"{image_folder}/{product['image']}", use_container_width=True)
                st.write(f"**{product['name']}**")
                st.write(f"💰 價格: {product['price']} 元")
                st.write(f"📦 庫存: {product['stock']} 個")

                if product["stock"] > 0:
                    if st.button(f"🛒 購買 {product['name']}", key=f"buy_{i+j}"):
                        product["stock"] -= 1
                        st.success(
                            f"已購買 {product['name']}，剩餘庫存：{product['stock']}"
                        )
                        time.sleep(1)
                        st.rerun()
                else:
                    st.error("❌ 庫存不足")

# ----------- 補貨功能 -----------
st.header("📦 新增商品庫存")

# product_names = [product["name"] for product in products]
product_names = []
for product in products:
    product_names.append(product["name"])


col1, col2 = st.columns(2)
with col1:
    selected_product_name = st.selectbox("選擇商品", product_names)
with col2:
    added_stock = st.number_input("新增數量", min_value=1, step=1)

if st.button("✅ 新增庫存"):
    for product in products:
        if product["name"] == selected_product_name:
            product["stock"] += added_stock
            st.rerun()
            break


# ----------- 顯示目前商品庫存 -----------
st.write("目前商品庫存")
for product in products:
    st.write(f"🔸 {product['name']}：{product['stock']} 個")
