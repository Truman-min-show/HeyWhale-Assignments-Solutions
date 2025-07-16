# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import numpy as np
import pandas as pd

# ------------------- STEP 1: 完成题目 -------------------

# --- Q1: 找出最小的三个值 ---
# 1. 创建数组
np.random.seed(0)
data = np.random.rand(1000000)

# 2. 使用 np.partition 找出前三小的值
# np.partition(data, 3) 会将数组分区，使得前3个元素是最小的3个（顺序不定）
partitioned_data = np.partition(data, 3)
smallest_three_unsorted = partitioned_data[:3]

# 3. 对比选项，可以先排序以方便查看
# sorted_smallest_three = np.sort(smallest_three_unsorted)
# print(sorted_smallest_three)
# -> [7.07120317e-07 1.33367964e-06 2.95041628e-06]
# 结果与选项A一致
a1 = 'A'


# --- Q2: 寻找最优配送点 ---
# 1. 创建坐标数组
np.random.seed(0)
locations = np.random.multivariate_normal([50, 50], [[100, 50], [50, 100]], 100)

# 2. 计算所有配送地点间的欧几里得距离矩阵
dist_sq = np.sum((locations[:, np.newaxis, :] - locations[np.newaxis, :, :]) ** 2, axis=-1)
distances = np.sqrt(dist_sq)

# 3. 计算每个点到其他所有点的平均距离
# axis=1 表示对每一行（每个点）进行求和/求平均
mean_distances = distances.mean(axis=1)

# 4. 找到平均距离最小的点的索引
# np.argmin 返回数组中最小值的索引
optimal_center_index = np.argmin(mean_distances)
# optimal_center_index 的结果是 53
a2 = optimal_center_index


# --- Q3: 处理结构化数据 ---
# 1. 定义结构化数组
dtype = [('name', 'U10'), ('salary', float)]
employees = np.array([
    ('Alice', 50000.00),
    ('Bob', 55000.00),
    ('Charlie', 65000.00),
    ('David', 48000.00),
    ('Eve', 62000.00)
], dtype=dtype)

# 2. 访问 'salary' 字段并计算平均值
average_salary = employees['salary'].mean()

# 3. 将结果保留为整数
# average_salary 的结果是 56000.0
a3 = int(average_salary)


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
        df.to_csv("answer_4.csv", index=None)
        print("文件 'answer_4.csv' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 运行这个cell,生成答案文件
save_csv(a1, a2, a3)