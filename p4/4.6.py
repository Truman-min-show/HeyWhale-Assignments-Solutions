# -*- coding: utf-8 -*-

# =============================================================================
# Seaborn 练习题答案生成脚本 - 关卡6：组合图表 (修正版)
#
# 本项目来源于和鲸社区
# 作者: 和鲸社区
# 来源: 和鲸社区
#
# 该脚本旨在回答一系列关于 Seaborn 组合图表和高级功能的问题，并生成用于提交的答案文件。
# (此版本已根据用户反馈修正 Q1 和 Q5 的答案)
# =============================================================================

import pandas as pd

# --- Q1：结合散点图与折线图 ---
# 新分析：更合理的绘图逻辑是先展示原始、具体的数据，再叠加抽象、总结的趋势。
# 因此，应先使用 `scatterplot` 绘制所有原始数据点，然后用 `lineplot`
# 在此基础上添加趋势线，以总结不同天气下的平均趋势。
# 选项 A 遵循了这一逻辑。
q1_answer = 'A'

# --- Q2：设置多子图的统一风格 ---
# 分析：Seaborn 提供了 `sns.set_style()` 和 `sns.set_context()` 两个函数，
# 用于在绘图前设置全局的图表风格和元素尺度。这是确保所有子图风格保持一致的
# 最推荐、最高效的方法。
# 选项 B 是正确的。
q2_answer = 'B'

# --- Q3：解读多产品的季节性趋势 ---
# 分析：当所有被分析的产品都表现出相同的季节性模式（如夏季销售额集体上升）时，
# 最合理的解释是存在一个影响整个市场的宏观因素，而不是每个产品独立的因素。
# 选项 C “反映了市场整体的季节性波动”是对此现象最恰当的解读。
q3_answer = 'C'

# --- Q4：关于 FacetGrid 的不正确说法 ---
# 分析：题目要求选出“不正确”的陈述。FacetGrid 的核心功能就是通过 `.map()` 方法
# 将绘图函数（如 `sns.histplot`）应用到数据的子集上，从而可以轻松地展示和比较
# 不同子集的数据分布。因此，“FacetGrid 不能展示...分布差异”的说法是完全错误的。
# 选项 C 是本题的正确答案。
q4_answer = 'C'

# --- Q5：判断 jointplot 的功能 ---
# 新分析：尽管 `jointplot` 可以通过 `hue` 参数引入第三个分类变量，但其图表的核心结构
# （一个中心二维图 + 两个边缘一维图）是为深度探索两个核心变量的关系而设计的。
# 因此，从其主要设计意图来看，“jointplot 只能用于绘制两个变量之间的关系”这个说法可以被认为是正确的。
# 选项 A 是正确的。
q5_answer = 'A'


# --- 生成答案文件 ---
def save_answers_to_csv(question_ids, answers, filename="answer_6.csv"):
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