import streamlit as st
import random

answer = random.randint(1, 100)
min_value = 1
max_value = 100
while True:
    number = int(input(f"請輸入{min_value}到{max_value}的數字"))
    if number < min_value or number > max_value:
        print(f"請輸入{min_value}到{max_value}的數字")
    else:
        if answer == number:
            print("猜中了！")
            break
        elif answer > number:
            min_value = number
            print("在大一點")
        elif answer < number:
            max_value = number
            print("在小一點")
