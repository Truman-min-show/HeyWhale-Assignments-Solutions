# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 完成题目 -------------------

# --- Q1 DataFrame操作 ---
# 背景：
# 要根据条件（布尔索引）筛选行，并根据名称选择列，应该使用 .loc 访问器。
# A) .loc[row_indexer, column_indexer] 是正确的语法，其中 row_indexer 可以是布尔数组，column_indexer 可以是标签列表。
# B) .iloc 用于整数位置索引，不能接受列名列表。
# C) .at 和 D) .iat 用于访问单个标量值，不适用于选择多个行和列。
# 因此，选项 A 是正确的。
a1 = "A"


# --- Q2 筛选表格数据 ---
# 背景：筛选满足多个条件的同学，并计算其四科成绩的均值。

# 1. 初始化原始数据
scores_df = pd.DataFrame({
    '学生姓名': ['阿喵额', '伯婆佛', '的特了呢', '及气息'],
    '射击': [98, 83, 69, 99],
    '骑术': [77, 56, 97, 98],
    '哲学': [50, 32, 85, 34],
    '数理': [66, 99, 65, 88]
})

# 2. 定义筛选条件
# a. 射击和骑术得分大于各自科目的平均值
cond1 = scores_df['射击'] > scores_df['射击'].mean()
cond2 = scores_df['骑术'] > scores_df['骑术'].mean()

# b. 哲学课和数理课得分大于各自科目的最小值
cond3 = scores_df['哲学'] > scores_df['哲学'].min()
cond4 = scores_df['数理'] > scores_df['数理'].min()

# 3. 组合所有条件（使用 & 表示“与”）
combined_filter = cond1 & cond2 & cond3 & cond4

# 4. 应用组合筛选器，获取符合条件的行
selected_students = scores_df[combined_filter]

# 5. 提取四科成绩列，并计算每位符合条件的学生成绩的均值 (axis=1 表示按行计算)
score_columns = ['射击', '骑术', '哲学', '数理']
average_scores = selected_students[score_columns].mean(axis=1)

# 6. 将计算结果赋值给a2
# 因为只有一个学生符合条件，我们提取该学生的平均分
# 使用 .iloc[0] 获取第一个（也是唯一一个）符合条件的学生的均分
a2 = average_scores.iloc[0]


# ------------------- STEP 2: 将结果保存为 csv 文件 -------------------

# 检查一下最终答案 (可选)
# print(f"Q1 答案: {a1}")
# print(f"Q2 答案: {a2}")

# 生成 csv 作业答案文件
def save_csv(ans1, ans2):
    """
    将最终答案保存到 CSV 文件中。
    """
    try:
        df = pd.DataFrame({"id": ["q1", "q2"], "answer": [ans1, ans2]})
        df.to_csv("answer_2.csv", index=None)
        print("文件 'answer_2.csv' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 运行这个cell,生成答案文件
save_csv(a1, a2)