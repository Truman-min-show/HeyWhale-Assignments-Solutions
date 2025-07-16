# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import numpy as np
import pandas as pd

# ------------------- STEP 1: 完成题目 -------------------

# --- 第一部分：布尔 ---
# 创建基础数组 A
np.random.seed(0)
A = np.random.randint(10, 100, size=(8, 8))
# print("原始数组 A:\n", A)
# A:
# [[54 57 74 77 77 19 93 31]
#  [46 97 80 98 98 22 68 75]
#  [49 97 56 98 91 47 35 87]
#  [82 19 30 90 79 89 57 74]
#  [92 98 59 39 29 29 24 49]
#  [42 75 19 67 42 41 84 33]
#  [45 85 65 38 44 10 10 46]
#  [63 15 48 27 89 14 52 68]]

# --- Q1 ---
# 计算数组中大于 50 的元素的个数
count_greater_than_50 = np.sum(A > 50)
# count_greater_than_50 的结果是 35
# 答案对应选项 C
a1 = 'C'

# --- Q2 ---

# 将这些大于50的元素在原矩阵中替换为 -1
A[A > 50] = -1
# 计算替换后的矩阵中第6行 (索引为5) 的和
sixth_row_sum = A[5, :].sum()
# sixth_row_sum 的结果是 174
# 答案对应选项 D
a2 = 'D'

# --- Q3 ---
# 判断数组中是否至少有一个元素大于 75
is_any_greater_than_75 = np.any(A > 75)
# is_any_greater_than_75 的结果是 True
# 答案对应选项 A
if(is_any_greater_than_75):
    a3 = 'A'
else:
    a3 = 'B'


# --- Q4: 索引的进阶用法 ---
# 1. 创建位置数组
np.random.seed(0)
mean = [0, 0]
cov = [[1, 0.5], [0.5, 1]]
locations = np.random.multivariate_normal(mean, cov, 200)

# 2. 提取指定索引的行
indices_to_select = [0, 30, 51, 130, 181]
selected_locations = locations[indices_to_select, :]

# 3. 计算选中点的x坐标 (第一列) 的平均值
x_coordinates_mean = selected_locations[:, 0].mean()
# x_coordinates_mean 的结果是 -0.29856...
# 答案对应选项 B
a4 = 'B'


# ------------------- STEP 2: 将结果保存为 csv 文件 -------------------

# 检查一下最终答案 (可选)
# print(f"Q1 答案: {a1}")
# print(f"Q2 答案: {a2}")
# print(f"Q3 答案: {a3}")
# print(f"Q4 答案: {a4}")

# 生成 csv 作业答案文件
def save_csv(ans1, ans2, ans3, ans4):
    """
    将最终答案保存到 CSV 文件中。
    """
    try:
        df = pd.DataFrame({"id": ["q1", "q2", "q3", "q4"], "answer": [ans1, ans2, ans3, ans4]})
        df.to_csv("answer_3.csv", index=None)
        print("文件 'answer_3.csv' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 运行这个cell,生成答案文件
save_csv(a1, a2, a3, a4)