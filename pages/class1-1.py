# print("hello")
# print("hello")
# print("hello")
# # """
# # 這是多行註解
# # """

# # 這是單行註解
# print("hello world!")  # print("hello world!")  # 這是單行註解

# # 基本型態
# print(1)  # int這是整數, -1 0 1 2 3 4
# print(1.0)  # float這是浮點數, 1.0 2.0 3.0
# print("apple")  # str這是字串, "apple" "banana" "cherry"
# print(True)  # bool這是布林值, True False
# print(False)  # bool這是布林值, True False

# # 變數
# a = 10  # 新增一個儲存空間並取名為a, 賦值為10
# print(a)  # 終端機顯示a的值
# a = "apple"  # 變數a的值改為"apple"
# print(a)  # 終端機顯示a的值

# # 運算子
# print(1 + 1)  # 加法
# print(1 - 1)  # 減法
# print(1 * 1)  # 乘法
# print(1 / 1)  # 除法
# print(1**2)  # 指數運算
# print(10 % 3)  # 取餘數
# print(10 // 3)  # 取整數商

# #優先順
# 1.() 括號
# 2.**指數運算
# 3.* / // %乘除取餘數
# 4.+ -加減

# # 字串運算，＋、＊
# print("hello" + "world")  # 字串連接
# print("hello" * 3)  # 字串重複

# # 字串格式化
# name = "Alice"
# age = 30
# print(f"My name is {name} and I am {age} years old.")  # f-string格式化

# print(len("hello"))  # 字串長度
# print(len(","))  # 字串長度

# # type() # 顯示變數的型態
# print(type(1))  # 顯示1的型態
# print(type(1.0))  # 顯示1.0的型態
# print(type("apple"))  # 顯示"apple"的型態
# print(type(True))  # 顯示True的型態

# # 顯示變數的型態
# print(int(1.0))  # 將1.0轉換為整數
# print(float(1))  # 將1轉換為浮點數
# print(str(1))  # 將1轉換為字串
# print(bool(1))  # 將1轉換為布林值
# print(int(1.234))  # 將1.234轉換為整數
# print(float("1.234"))  # 將1.234轉換為浮點數
# print(str(1.234))  # 將1.234轉換為字串
# print(bool(1.234))  # 將1.234轉換為布林值
# # print(int("hello"))  # 將"hello"轉換為整數會報錯

# 輸入輸出
# a = input("三角形的底")
# b = input("三角形的高")
# # 計算三角形的面積
# area = (int(a) * int(b)) / 2  # 將輸入的底和高轉換為整數並計算面積
# print(area)  # 顯示三角形的面積

# a = input("姓名")
# b = input("年齡")
# print(f"你好，{a}!你今年{b}歲。")  # 使用f-string格式化輸出

# pi = 3.14
# r = input("圓的半徑")
# area = pi * float(r) ** 2  # 計算圓的面積
# print(f"圓的面積是{area}")  # 使用f-string格式化輸出圓的面積

# a = int(input("請輸入一個數字"))
# print(str(a))  # 將輸入的數字轉換為字串並顯示
# print("你輸入的數字是" + str(a) * 3)  # 將輸入的數字轉換為字串並重複三次顯示

# print("輸入開始")
# # input()是一個函式，可以讓使用者輸入文字
# # ()裡面的文字是提示訊息會先顯示在終端機才會等待使用者輸入
# a = input("請輸入一些文字：")
# print("輸入結束")
# print(int(a) + 10)
# print(type(a))  # 證明透過input()輸入的都是字串

# a = input("請輸入一個字串：")
# b = len(a)  # 計算字串的長度
# print(f"你輸入的字串長度是：{b}")

# 商品名稱 = input("請輸入商品名稱：")
# 商品單價 = input("請輸入商品單價：")
# 商品數量 = input("請輸入商品數量：")
# print(f"你買了{商品名稱}，單價是{商品單價}，總價是{float(商品單價) * int(商品數量)}。")
