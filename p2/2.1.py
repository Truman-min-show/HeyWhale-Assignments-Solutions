# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import numpy as np
import pandas as pd

# ------------------- STEP 1: 完成题目 -------------------

# Q1：创建数列
# 利用arange函数，创建数组值从1开始到19结束（不包含19），步长为1，保存为a
# 再创建一个从19到49结束（不包含49），步长为1，保存为b
a = np.arange(1, 19, 1)
b = np.arange(19, 49, 1)

# Q2: 对数列形变
# 利用reshape函数，将a形变为3×6的数组，保存为A
# 将b形变为5×6的数组，保存为B
A = a.reshape(3, 6)
B = b.reshape(5, 6)

# Q3：数组拼接与分裂
# 利用vstack将A和B数组进行垂直方向拼接，保存为C数组
# 利用split对C数组在第2行分裂成两部分，将下半部分保存为D
C = np.vstack((A, B))
# np.split在索引2之前进行分割，返回一个列表，我们取第二部分[1]
D = np.split(C, [2], axis=0)[1]

# Q4：切片与索引
# 对D提取第1行所有元素，保存为E
E = D[0, :]

# Q5：数组计算
# 利用multiply.accumulate对E中所有元素依次求积，并保留最后一项作为E中的累计积保存为a1
cumulative_product = np.multiply.accumulate(E)
# 保留最后一项
a1 = cumulative_product[-1]


# ------------------- STEP 2: 将结果保存为 csv 文件 -------------------

# 检查一下最终答案 (可选)
# print(f"最终答案 a1 = {a1}")

# 生成 csv 作业答案文件
def save_csv(result_a1):
    """
    将最终答案保存到 CSV 文件中。
    """
    try:
        df = pd.DataFrame({"id": ["q1"], "answer": [result_a1]})
        df.to_csv("answer_1.csv", index=None)
        print("文件 'answer_1.csv' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 运行这个cell,生成答案文件
save_csv(a1)