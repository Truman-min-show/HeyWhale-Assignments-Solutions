# -*- coding: utf-8 -*-

# =============================================================================
# Seaborn 练习题答案生成脚本 - 关卡5：基本图表
#
# 本项目来源于和鲸社区
# 作者: 和鲸社区
# 来源: 和鲸社区
#
# 该脚本旨在回答一系列关于 Seaborn 基本图表使用的问题，并生成用于提交的答案文件。
# =============================================================================

import pandas as pd

# --- Q1：在 kdeplot 中限制估计范围 ---
# 题解分析：为了防止核密度估计曲线延伸到不切实际的数值范围（如负年龄），
# 应当使用 `clip` 参数。`clip=(0, None)` 会将曲线的估计范围裁剪在0及以上。
# 选项 B 是正确的。
q1_answer = 'B'

# --- Q2：在同一图中按类别绘制不同回归线 ---
# 题解分析：`sns.lmplot` 是一个 figure-level 的函数，支持使用 `hue` 参数
# 在同一个坐标轴上为不同类别的数据绘制不同的回归线。`sns.regplot` 不支持 `hue`。
# 选项 C 完全符合题目要求。
q2_answer = 'C'

# --- Q3：使用 ecdfplot 确定四分位数范围 ---
# 题解分析：ECDF（累积概率密度图）的y轴代表累积概率。要找到中间50%的数据范围，
# 需要找到y轴上25%和75%对应的x轴上的值。
# 选项 D 描述了这一核心思想，是正确的。
q3_answer = 'D'

# --- Q4：使用不同标记（形状）区分散点 ---
# 题解分析：在 Seaborn 的 `scatterplot` 中，`style` 参数专门用于
# 根据一个分类变量来改变数据点的标记形状。
# 选项 A 正确使用了 `style` 参数来实现这一需求。
q4_answer = 'A'

# --- Q5：绘制 lineplot 时不显示置信区间 ---
# 题解分析：`sns.lineplot` 默认会计算并显示置信区间（一个半透明的带状区域）。
# 要禁用这一功能，需要将 `ci` 参数设置为 `None`。
# (注：在新版Seaborn中，`errorbar=None` 是推荐做法，但 `ci=None` 仍广泛有效)。
# 选项 D 是正确的。
q5_answer = 'D'


# --- 生成答案文件 ---
def save_answers_to_csv(question_ids, answers, filename="answer_5.csv"):
    """
    将问题ID和对应的答案保存为 CSV 文件。

    :param question_ids: 一个包含问题ID字符串的列表 (e.g., ['q1', 'q2'])
    :param answers: 一个包含答案字符串的列表 (e.g., ['A', 'B'])
    :param filename: 输出的CSV文件名
    """
    if len(question_ids) != len(answers):
        print("错误：问题ID数量与答案数量不匹配！")
        return

    try:
        df = pd.DataFrame({
            "id": question_ids,
            "answer": answers
        })
        df.to_csv(filename, index=None, encoding='utf_8_sig')
        print(f"答案文件 '{filename}' 已成功生成！")
    except Exception as e:
        print(f"生成文件时发生错误: {e}")


# 定义本次作答的问题ID和答案列表
ids = ["q1", "q2", "q3", "q4", "q5"]
final_answers = [q1_answer, q2_answer, q3_answer, q4_answer, q5_answer]

# 调用函数，生成CSV文件
save_answers_to_csv(ids, final_answers)