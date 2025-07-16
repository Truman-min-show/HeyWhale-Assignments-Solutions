# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd
import json

# ------------------- STEP 1: 完成题目 -------------------

# --- Q1 创建DataFrame ---
# 背景：
# 根据图片和Pandas的语法，创建一个DataFrame需要一个字典，其中键是列名，值是包含该列数据的列表。
# 选项A: pd.DataFrame({'姓名': ['李雷', '韩梅梅'], '工资': [5000, 6000]}) 是正确的语法。
# 选项B, C, D 均存在语法错误。
a1 = "A"


# --- Q2 查看DataFrame ---
# 背景：
# df.head() 查看前几行数据。
# df.info() 查看数据的基本信息（列、非空值、类型等）。
# df.describe() 查看数据的统计摘要。
# df.save() 不是一个标准的Pandas方法。要保存数据，应使用 df.to_csv(), df.to_excel() 等。
# 因此，不是常用查看基本信息方法的是 C。
a2 = "C"


# --- Q3 处理表格数据 ---
# 背景：清洗外星球实验数据。

# 1. 创建原始DataFrame
data = pd.DataFrame({
    '实验编号': [1, 2, 3, 4, 5],
    '实验日期': ['2024-01-15%', '2024-01-16%', '2024-01-17%', '2024-01-18%', '2024-01-19%'],
    '样本名称': ['样本A', '样本B', '样本C', '样本D', '样本E'],
    '样本重量': [2.5, 3.1, 2.8, 3.3, 2.9],
    '样本密度': [1.0, 1.0, 1.0, 1.0, 1.0],
    '表面温度': [-50, -45, -48, -47, -49],
    '磁场强度': [0.5, 0.6, 0.55, 0.52, 0.58],
    '放射性强度': [20, 25, 22, 21, 23]
})

# 2. 创建一个副本进行操作，以保持原始数据不变
cleaned_df = data.copy()

# 3. 清洗数据
# 3.1. 移除'实验日期'列中的 '%' 符号
cleaned_df['实验日期'] = cleaned_df['实验日期'].str.replace('%', '')

# 3.2. 将'表面温度'列的负数转为正数
cleaned_df['表面温度'] = cleaned_df['表面温度'].abs()

# 3.3. 删除'磁场强度'列
cleaned_df = cleaned_df.drop(columns=['磁场强度'])

# 4. 将清洗后的DataFrame转换为字典
# to_dict('list') 方法可以将DataFrame转换为以列名为键，列表为值的字典
a3 = cleaned_df.to_dict(orient='list')


# ------------------- STEP 2: 将结果保存为 json 文件 -------------------

# 检查一下最终答案 (可选)
# print(f"Q1 答案: {a1}")
# print(f"Q2 答案: {a2}")
# print("Q3 答案:")
# print(json.dumps(a3, indent=4, ensure_ascii=False))

# 生成 json 作业答案文件
json_data = {
    "q1": a1,
    "q2": a2,
    "q3": a3
}
# 使用 ensure_ascii=False 来确保中文字符正确显示
json_str = json.dumps(json_data, indent=4, ensure_ascii=False)

file_path = 'answer_1.json'

try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_str)
    print(f"文件 '{file_path}' 已成功生成。")
except Exception as e:
    print(f"写入文件时出错: {e}")