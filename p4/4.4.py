# -*- coding: utf-8 -*-

# =============================================================================
# Seaborn 练习题答案生成脚本 - 关卡4
#
# 本项目来源于和鲸社区
# 作者: 和鲸社区
# 来源: 和鲸社区
#
# 该脚本旨在回答一系列关于 Seaborn 使用的问题，并生成用于提交的答案文件。
# =============================================================================

import pandas as pd

# --- Q1：使用 relplot 和 hue ---
# 题解分析：为了用颜色区分数据点，应使用 `hue` 参数。`relplot` 的默认 `kind`
# 是 `scatter`，但显式指定 `kind="scatter"` 是更清晰的做法。
# 选项 B 是最明确和正确的。
q1_answer = 'D'

# --- Q2：使用 catplot 创建子图列 ---
# 题解分析：`catplot` 中，`col` 参数用于按指定变量的值创建子图列。
# `kind="box"` 指定了图表类型为箱型图。
# 选项 A 准确地满足了所有要求。
q2_answer = 'A'

# --- Q3：relplot 中 hue 和 palette 的关系 ---
# 题解分析：`hue` 参数根据一个分类变量来自动分配颜色，而 `palette` 参数可以
# 与 `hue` 配合使用，来具体控制或自定义所使用的颜色集。
# 选项 D 对这两个参数的关系描述得最准确、最全面。
q3_answer = 'D'

# --- Q4：scatterplot 中 size 和 style 的作用 ---
# 题解分析：`size` 参数根据一个（通常是数值）变量来改变散点的大小。
# `style` 参数根据一个（通常是分类）变量来改变散点的形状（标记样式）。
# 选项 C 的描述完全正确。
q4_answer = 'C'

# --- Q5：对比不同类别的数值分布 ---
# 题解分析：题目的关键是对比“分布情况”。直方图 (`histplot`) 是专门用于
# 可视化数据分布的图表。结合 `hue` 参数，可以完美地在同一张图上对比多个类别的分布。
# 选项 A 是最佳选择。
q5_answer = 'A'


# --- 生成答案文件 ---
def save_answers_to_csv(question_ids, answers, filename="answer_4.csv"):
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