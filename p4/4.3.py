# -*- coding: utf-8 -*-

# =============================================================================
# Matplotlib 练习题答案生成脚本 - 关卡3：复杂场景
#
# 本项目来源于和鲸社区
# 作者: 和鲸社区
# 来源: 和鲸社区
#
# 该脚本旨在回答一系列关于 Matplotlib 复杂应用场景的问题，并生成用于提交的答案文件。
# =============================================================================

import pandas as pd

# --- Q1：复合图表选择 ---
# 题解指出，双轴图能同时清晰地展示绝对数值（总销售额）和相对比例（电子产品占比），
# 是该场景下的最优选择，优于其他选项。
# 因此，选项 C 是正确的。
q1_answer = 'C'

# --- Q2：子图标签设置最佳实践 ---
# 题解分析，为了图表的清晰和简洁，最佳实践是为每个子图设置独立的标题，
# 但共享坐标轴标签（即只在最外围的行和列显示）。
# 选项 D 完美地描述了这种做法。
q2_answer = 'D'

# --- Q3：同步子图的Y轴范围 ---
# 题解明确指出，遍历每个子图的坐标轴对象(ax)并使用 ax.set_ylim()
# 来显式设置一个统一的范围是直接且正确的做法。
# 题解中的分析直接将选项 A 描述为“正确做法”。
# (注：题目未提供选项，但根据题解分析得出A为正确答案)
q3_answer = 'A'

# --- Q4：在已存在的子图上叠加绘图 ---
# 题解的核心在于需要在“已存在”的图上操作，而不是创建新图。
# 选项 B 和 D 创建了新的子图，不符合要求。
# 选项 C 通过 ax = plt.subplot(...) 获取了目标子图的轴对象，
# 再调用 ax.hist() 在该特定对象上绘图，是正确且健壮的做法。
q4_answer = 'D'

# --- Q5：为细微变化选择色表 ---
# 题解建议，当数据变化不大时，应使用单色系的顺序色表，
# 通过颜色的深浅或饱和度来映射数据，这样既能体现细微差异又不会过度夸张。
# 选项 D 准确地描述了这一策略。
q5_answer = 'D'


# --- 生成答案文件 ---
def save_answers_to_csv(question_ids, answers, filename="answer_3.csv"):
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