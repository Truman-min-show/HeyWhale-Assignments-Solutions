# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 完成题目 -------------------

# --- Q1 函数调用 ---
# 背景：分析函数 sum_xxx([1,2,3,4,5]) 的结果
#
# def sum_xxx(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:       # 判断是否为奇数
#             total += num ** 2  # 如果是，则将其平方加入total
#     return total
#
# 调用过程：
# 1. num = 1 (奇数), total = 0 + 1^2 = 1
# 2. num = 2 (偶数), total不变
# 3. num = 3 (奇数), total = 1 + 3^2 = 1 + 9 = 10
# 4. num = 4 (偶数), total不变
# 5. num = 5 (奇数), total = 10 + 5^2 = 10 + 25 = 35
# 函数返回 35。这对应于选项 B。

a1 = 'B'


# --- Q2 定义中位数函数 ---
# 背景：为列表 lst 计算中位数

# 请输入你的计算代码
def calculate_median(data_list):
    """
    计算一个数字列表的中位数，不使用外部库。
    """
    # 1. 对列表进行排序
    sorted_list = sorted(data_list)
    n = len(sorted_list)

    # 2. 判断列表长度是奇数还是偶数
    if n % 2 == 1:
        # 如果是奇数，中位数是中间的那个数
        median = sorted_list[n // 2]
    else:
        # 如果是偶数，中位数是中间两个数的平均值
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        median = (mid1 + mid2) / 2

    return median


# 给定的数据列表
lst = [3, 4, 1, 12, 4, 1, 43, 6, 12, 9, 6, 5, 24, 33, 2, 7, 9, 10]

# 把计算出来的结果赋值给a2
a2 = calculate_median(lst)


# --- Q3 定义身材健康度函数 ---
# 背景：定义一个函数计算BMI并返回健康状况。

# 输入你的计算代码过程
def calculate_bmi(weight, height):
    """
    根据体重(kg)和身高(m)计算BMI指数并返回健康状况。
    """
    # 防止身高为0导致除零错误
    if height == 0:
        return "身高不能为0"

    # 计算BMI指数
    bmi = weight / (height ** 2)

    # 根据BMI范围返回结果
    if bmi < 18.5:
        return "体重过轻"
    elif 18.5 <= bmi < 25:
        return "正常"
    elif 25 <= bmi < 30:
        return "体重超重"
    else:  # bmi >= 30
        return "肥胖"


# 把小白的健康程度赋值给a3
# 小白体重120公斤，身高2米
a3 = calculate_bmi(120, 2)


# ------------------- STEP 2: 将结果保存为 csv 文件 -------------------

# 检查一下计算结果 (可选)
# print(f"a1 = {a1}")
# print(f"a2 = {a2}")
# print(f"a3 = {a3}")

# 生成 csv 作业答案文件
def save_csv(a1, a2, a3):
    """
    将答案保存到 CSV 文件中。
    """
    try:
        df = pd.DataFrame({"id": ["q1", "q2", "q3"], "answer": [a1, a2, a3]})
        df.to_csv("answer_5.csv", index=None)
        print("文件 'answer_5.csv' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")


# 运行这个cell,生成答案文件
save_csv(a1, a2, a3)