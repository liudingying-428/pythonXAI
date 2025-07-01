# 比較運算子
print(1 == 1)  # 等於 true
print(1 != 1)  # 不等於 false
print(1 > 1)  # 大於 false
print(1 < 1)  # 小於 false
print(1 >= 1)  # 大於等於 true
print(1 <= 1)  # 小於等於 true

# # 邏輯運算子
# # and 運算子
print(True and True)  # true
print(True and False)  # false
print(False and True)  # false
print(False and False)  # false

# # or 運算子
print(True or True)  # true
print(True or False)  # true
print(False or True)  # true
print(False or False)  # false

# # not 運算子
print(not True)  # false
print(not False)  # true

# 優先順序
# 1. () 括號
# 2. ** 指數運算
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != < > <= >= 比較運算子
# 6. not 邏輯運算子
# 7. and 邏輯運算子
# 8. or 邏輯運算子

# 密碼門檢查
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎Jeremy")
elif password == "123456":
    print("歡迎Jeffery")
elif password == "12345678":
    print("歡迎Tim")
else:
    print("密碼錯誤")
# 連續使用if跟使用if elif else的差異
# elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省了時間
# 但是如果是使用多個if來獨立判斷，則每個if都會被執行，所以效率降低
