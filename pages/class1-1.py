print("hello")
print("hello")
print("hello")
# """
# 這是多行註解
# """

# 這是單行註解
print("hello world!")  # print("hello world!")  # 這是單行註解

# 基本型態
print(1)  # int這是整數, -1 0 1 2 3 4
print(1.0)  # float這是浮點數, 1.0 2.0 3.0
print("apple")  # str這是字串, "apple" "banana" "cherry"
print(True)  # bool這是布林值, True False
print(False)  # bool這是布林值, True False

# 變數
a = 10  # 新增一個儲存空間並取名為a, 賦值為10
print(a)  # 終端機顯示a的值
a = "apple"  # 變數a的值改為"apple"
print(a)  # 終端機顯示a的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1**2)  # 指數運算
print(10 % 3)  # 取餘數
print(10 // 3)  # 取整數商

# 優先順序
# 1.()括號
# 2.**指數運算
# 3.* / // %乘除取餘數
# 4.+ -加減

# 字串運算，＋、＊
print("hello" + "world")  # 字串連接
print("hello" * 3)  # 字串重複

# 字串格式化
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # f-string格式化

print(len("hello"))  # 字串長度
print(len(","))  # 字串長度
# type() # 顯示變數的型態
print(type(1))  # 顯示1的型態
print(type(1.0))  # 顯示1.0的型態
print(type("apple"))  # 顯示"apple"的型態
print(type(True))  # 顯示True的型態

# 顯示變數的型態
print(int(1.0))  # 將1.0轉換為整數
print(float(1))  # 將1轉換為浮點數
print(str(1))  # 將1轉換為字串
print(bool(1))  # 將1轉換為布林值
print(int(1.234))  # 將1.234轉換為整數
print(float("1.234"))  # 將1.234轉換為浮點數
print(str(1.234))  # 將1.234轉換為字串
print(bool(1.234))  # 將1.234轉換為布林值
# print(int("hello"))  # 將"hello"轉換為整數會報錯
