# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import numpy as np
import numpy.lib.recfunctions as rfn
import pandas as pd

# ------------------- STEP 1: 完成题目 -------------------

# --- 会员信息数据初始化 ---
dtype = [
    ('member_id', int),
    ('age', int),
    ('gender', 'U1'),
    ('spend', float),
    ('points', int)
]

data = [
    (0, 33, 'M', 170.77, 100),
    (1, 23, 'F', 150.75, 100),
    (2, 34, 'M', 200.50, 200),
    (3, 45, 'F', 980.00, 800),
    (4, 28, 'M', 330.25, 300),
    (5, 65, 'F', 485.00, 400),
    (6, 53, 'M', 855.75, 755),
    (7, 41, 'F', 250.00, 200),
    (8, 30, 'M', 650.90, 600),
    (9, 37, 'F', 760.45, 730),
    (10, 29, 'M', 155.55, 145)
]

members = np.array(data, dtype=dtype)


# --- Q1: 聚合 ---
# 计算消费金额（spend）的平均数，保留整数部分
average_spend = members['spend'].mean()
a1 = int(average_spend)


# --- Q2: 挖掘潜在消费群体 ---
# Q2第一步：比较与索引
# 获取所有消费金额小于平均数的会员信息
low_spenders_mask = members['spend'] < average_spend
low_spenders = members[low_spenders_mask]

# Q2第二步: 聚合
# 计算消费金额小于平均数的会员的平均年龄，保留整数部分
average_age_low_spenders = low_spenders['age'].mean()
a2 = int(average_age_low_spenders)


# --- Q3： 发掘高效会员 ---
# Q3第一步：广播计算
# 定义一个新的变量为“获积分效率”，并将其作为新的一列添加
points_eff_values = members['points'] / members['spend']
# 使用 rfn.append_fields 添加新列
members_with_eff = rfn.append_fields(members, 'points_eff', points_eff_values, usemask=False)

# Q3第二步: 排序
# 获取获得积分最高效的会员id
# np.argmax找到效率最高行的索引
most_efficient_index = np.argmax(members_with_eff['points_eff'])
# 通过索引找到对应的会员记录，并提取其ID
most_efficient_member_id = members_with_eff[most_efficient_index]['member_id']
a3 = most_efficient_member_id


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
        df.to_csv("answer_5.csv", index=None)
        print("文件 'answer_5.csv' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 运行这个cell,生成答案文件
save_csv(a1, a2, a3)