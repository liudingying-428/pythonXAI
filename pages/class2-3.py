# for 迴圈
# for 會搭配 in 來使用，in 後面接個有範圍的東西
# range(5) 會產生一個從 0 到 4 的數字序列
# i 是迴圈的變數可以自己取名
# 迴圈變數每回合會從範圍中取出一個資料
# for i in range(5):
#     print(i, end=" ")

# range 可以設定起始值與結束值，但不包含結束值
# range(1, 6) 會產生一個從 1 到 5 的數字序列
# for i in range(1, 6):
#     print(i, end=" ")

# range 可以設定起始值、結束值與間隔值，但不包含結束值
# range(1, 10, 2) 會產生1 3 5 7 9 的數字序列
# for i in range(1, 10, 2):
#     print(i, end=" ")

# a = int(input("請輸入一個數字："))
# b = int(input("請輸入另一個數字："))
# for i in range(a, b + 1):
#     print(f"{i}號在教室")

# a = int(input("請輸入一個數字："))
# b = int(input("請輸入另一個數字："))
# c = 0
# for i in range(a, b + 1):
#     c = c + i
# print(f"{a}加到{b}的總和是{c}")

a = int(input("請輸入一個數字："))
b = int(input("請輸入另一個數字："))
print(f"(({a} + {b}) * {b - a + 1}) / 2) = {((a + b) * (b - a + 1)) / 2}")
