# -*- coding: utf-8 -*-

# =============================================================================
# Matplotlib 练习题答案生成脚本 - 关卡2：图表元素 (完整版)
#
# 本项目来源于和鲸社区
# 作者: 和鲸社区
# 来源: 和鲸社区
#
# 该脚本旨在回答一系列关于 Matplotlib 图表元素的问题，并生成用于提交的答案文件。
# (此版本已根据用户反馈补充了第3题的答案)
# =============================================================================

import pandas as pd

# --- Q1：代码错误检查 ---
# 题解指出，代码中的 plt.title.('My Data Visualization') 存在语法错误。
# 正确的函数调用方式是 plt.title('My Data Visualization')。
# 因此，选项 C 是正确的描述。
q1_answer = 'C'

# --- Q2：柱形图 Y 轴起点问题 ---
# 题解分析，当Y轴不从0开始时，条形高度的视觉比例被扭曲，
# 会在视觉上放大数据间的相对差异，从而夸大实际差异。
# 因此，选项 A 是正确的。
q2_answer = 'A'

# --- Q3：设置坐标轴范围 (补充) ---
# 题目问：当你想要设置图表的坐标轴范围时，应该使用以下哪些函数？
# 分析：在 Matplotlib 的 pyplot 接口中，plt.xlim() 和 plt.ylim()
# 是用来设置当前图表 x 轴和 y 轴范围的正确函数。
# 因此，选项 C 是正确的。
q3_answer = 'C'

# --- Q4：直方图代码错误检查 ---
# 题解指出，代码中的 alpha='0.5' 是一个字符串，而 alpha 参数需要一个浮点数（float）
# 来控制透明度。因此，这是一个类型错误。
# 选项 A 正确地指出了这个问题。
q4_answer = 'A'

# --- Q5：饼图标签美观性问题 ---
# 题解说明，在饼图的每个部分内部添加过长的描述文本会导致文本重叠或显示不全，
# 影响图表的可读性和美观性，是应该避免的做法。
# 因此，选项 D 是正确的。
q5_answer = 'D'


# --- 生成答案文件 ---
def save_answers_to_csv(question_ids, answers, filename="answer_2.csv"):
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


# 定义本次作答的完整问题ID和答案列表
ids = ["q1", "q2", "q3", "q4", "q5"]
final_answers = [q1_answer, q2_answer, q3_answer, q4_answer, q5_answer]

# 调用函数，生成CSV文件
save_answers_to_csv(ids, final_answers)