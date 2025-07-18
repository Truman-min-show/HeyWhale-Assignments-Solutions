# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import numpy as np
import pandas as pd

# ------------------- STEP 1: 完成题目 -------------------

# --- Q1: 利用数组广播计算 ---
# 1. 定义数组
A = np.arange(1, 10).reshape(3, 3)
B = np.array([10, 20, 30])

# 2. 利用广播计算 C = A + B
#    A: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#    B: [10, 20, 30]
#    C: [[11, 22, 33], [14, 25, 36], [17, 28, 39]]
C = A + B

# 3. 计算C第三列的平均值
#    第三列: [33, 36, 39]
#    平均值: (33 + 36 + 39) / 3 = 108 / 3 = 36
#    答案对应选项 C
a1 = 'C'


# --- Q2: 利用广播机制进行数据归一化 ---
# 1. 题目给定的数组D
np.random.seed(0)
# D = np.random.rand(6, 4) # 这行生成随机数，但为了结果一致，我们使用题目中给出的具体数值
D = np.array([
    [0.5488135 , 0.71518937, 0.60276338, 0.54488318],
    [0.4236548 , 0.64589411, 0.43758721, 0.891773  ],
    [0.96366276, 0.38344152, 0.79172504, 0.52889492],
    [0.56804456, 0.92559664, 0.07103606, 0.0871293 ],
    [0.0202184 , 0.83261985, 0.77815675, 0.87001215],
    [0.97861834, 0.79915856, 0.46147936, 0.78052918]
])

# 2. 获取每列的min和max
D_min = D.min(axis=0)
D_max = D.max(axis=0)

# 3. 利用广播进行归一化
D_normalized = (D - D_min) / (D_max - D_min)

# 4. 提取第三行 (索引为2)，并计算其平均值
third_row_mean = D_normalized[2, :].mean()
#    计算结果约为 0.63335...
#    答案对应选项 A
a2 = 'A'


# --- Q3: 求二维数组最大值 ---
# 第一步：利用linspace生成两个范围为 [0, 2] 的 60 个等间距数组
u = np.linspace(0, 2, 60)
v = np.linspace(0, 2, 60)

# 第二步：将v转化为列向量
v = v[:, np.newaxis]

# 第三步：计算二维数组 w
w = np.sin(u**2) * np.cos(v) + np.cos(5 + u*v) * np.sin(v)

# 第四步：获取w的最大值
w_max = w.max()
#    计算结果约为 1.655225...
#    答案对应选项 C
a3 = 'C'


# ------------------- STEP 2: 将结果保存为 csv 文件 -------------------

# 检查一下最终答案 (可选)
# print(f"Q1 答案: {a1}")
# print(f"Q2 答案: {a2}")
# print(f"Q3 答案: {a3}")

# 生成 csv 作业答案文件
def save_csv(ans1, ans2, ans3):
    """
    将最终答案保存到 CSV 文件中。
    """
    try:
        df = pd.DataFrame({"id": ["q1", "q2", "q3"], "answer": [ans1, ans2, ans3]})
        df.to_csv("answer_2.csv", index=None)
        print("文件 'answer_2.csv' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 运行这个cell,生成答案文件
save_csv(a1, a2, a3)