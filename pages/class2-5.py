print([])  # 這是一個空list
print([1, 2, 3])  # 這是一個有三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個有六個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有四個元素的list，其中一個元素是另一個list
print(
    [1, True, "a", 3.14]
)  # 這是一個有四個元素的list，其中包含整數、布林值、字串和浮點數

# list 讀取元素，元素ㄉ˙index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 讀取第一個元素 1
print(L[1])  # 讀取第二個元素 2
print(L[2])  # 讀取第三個元素 3
print(L[3])  # 讀取第四個元素 "a"

midterm = [80, 95, 78, 60, 55]
final = [64, 73, 52, 34, 95]
print(f"(midterm[1]和final[1]的平均分數是{(midterm[1] + final[1]) / 2})")

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取２個元素所以是[1, 3, "b"]
print(L[::2])
# 就是取index 1到3的元素，不包含index 4，所以是[2, 3, "a"]
# print(L[1:4])
# 就是取index 1到3的元素，不包含index 4，並且每次取2個元素，所以是[2, "a"]
print(L[1:4:2])
# 跟range一樣的用法，只是符號不同

# list 取長度，也就是list中有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 讀取list的長度，結果是6

# list 走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 這兩種方式都可以，但是看使用的情境是否會需要index來決定要用哪一種方式
# L = [1, 2, 3, "a", "b", "c"]
# for i in range(len(L)):
#     print(L[i])

# for i in L:
#     print(i)

# name = ["Amy", "Mandy", "Peter"]
# for i in range(len(name)):
#     print(f"{i+1}號是{name[i]}")
# number = 1
# for i in name:
#     print(f"{number}號是{i}")
#     number = number + 1

fruit = ["頻果", "香蕉", "鳳梨"]
number = [3, 5, 6]
for i in range(len(fruit)):
    print(f"{fruit[i]}有{number[i]}個")
