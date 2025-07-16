# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 完成题目 -------------------

# --- Q1 判断结果识别 ---
# 背景：
# score = 85
# passing_score = 60
# excellent_score = 90
#
# 表达式1: score > excellent_score -> 85 > 90 -> False
# 表达式2: score >= passing_score and score < excellent_score -> (85 >= 60) and (85 < 90) -> True and True -> True
# 表达式3: score != passing_score and score <= excellent_score -> (85 != 60) and (85 <= 90) -> True and True -> True
# 表达式4: score > passing_score or score < excellent_score -> (85 > 60) or (85 < 90) -> True or True -> True
#
# 结果序列: False, True, True, True
# 这对应于选项 A。

a1 = 'A'


# --- Q2 求和 ---
# 背景：计算从1到100之间所有偶数的和。

# 你的求解代码过程
sum_of_evens = 0
for num in range(1, 101):
    # 判断是否为偶数
    if num % 2 == 0:
        sum_of_evens += num

# 把求和结果赋值给a2
a2 = sum_of_evens


# --- Q3 条件判断 ---
# 背景：根据消费总金额计算折扣。
# 消费金额: [50, 100, 30, 10, 50, 49, 100]
# 折扣策略:
# > 500元 -> 30% 折扣
# > 200元 -> 20% 折扣
# > 100元 -> 10% 折扣

# 你的求解代码过程
expenses = [50, 100, 30, 10, 50, 49, 100]
total_amount = sum(expenses)
final_price = 0

# 注意：条件判断应该从大到小，以确保应用正确的最高折扣
if total_amount > 500:
    final_price = total_amount * (1 - 0.30)
elif total_amount > 200:
    final_price = total_amount * (1 - 0.20)
elif total_amount > 100:
    final_price = total_amount * (1 - 0.10)
else:
    final_price = total_amount

# 把计算结果赋值给a3，并保留整数部分
a3 = int(final_price)


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
        df.to_csv("answer_4.csv", index=None)
        print("文件 'answer_4.csv' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 运行这个cell,生成答案文件
save_csv(a1, a2, a3)