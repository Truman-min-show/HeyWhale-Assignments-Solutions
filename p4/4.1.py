# -*- coding: utf-8 -*-

# =============================================================================
# Matplotlib 练习题答案生成脚本
#
# 本项目来源于和鲸社区
# 作者: Rue
# 来源: https://www.heywhale.com/mw/project/667a7464a1473f7c88d83631
#
# 该脚本旨在回答一系列关于 Matplotlib 使用的问题，并生成用于提交的答案文件。
# =============================================================================

import pandas as pd

# --- 问题1 ---
# 在绘制饼图时，如果我们想要突出显示某一块，应该使用哪个参数？
# 答案：A. explode 参数用于设置饼图中各个扇形离圆心的距离，从而实现突出显示的效果。
a1 = 'A'


# --- 问题2 ---
# 在散点图中，假设要根据每个点的某项指标大小来决定点的大小，应该使用 scatter() 函数的哪个参数？
# 答案：B. s 参数用于控制散点图中点的大小（size）。它可以是一个数值，也可以是一个数组。
a2 = 'B'


# --- 问题3 ---
# 你在绘制多个分类的数据，并希望将不同类别的数据柱形图并列排列。在这种情况下，你需要对每个条形的____进行调整，
# 以使它们在同一刻度上不会重叠，且沿着x轴正确排列。
# 答案：C. x 轴位置。为了将多组柱形图并列显示，需要计算每组柱形图在 x 轴上的精确位置，
# 通常通过原始 x 坐标加上或减去柱形宽度的倍数来实现。
a3 = 'C'


# --- 问题4 ---
# 在绘制面积图时，要设置图表中填充区域的透明度，应该调整哪个参数？
# 答案：B. alpha 参数在 Matplotlib 中通用地用于设置图形元素的透明度，取值范围为 0 (完全透明) 到 1 (完全不透明)。
a4 = 'B'


# --- 问题5 ---
# 如果你想比较不同产品在同一年中的销售额，以下哪种图表最合适？
# 答案：C. 柱形图。柱形图非常适合用于比较不同类别（如不同产品）下的数值大小（如销售额），清晰直观。
a5 = 'C'


# --- 生成答案文件 ---
def save_csv(q1_ans, q2_ans, q3_ans, q4_ans, q5_ans):
    """
    将答案保存为 CSV 文件。
    """
    try:
        df = pd.DataFrame({
            "id": ["q1", "q2", "q3", "q4", "q5"],
            "answer": [q1_ans, q2_ans, q3_ans, q4_ans, q5_ans]
        })
        file_path = "answer_1.csv"
        df.to_csv(file_path, index=None, encoding='utf_8_sig')
        print(f"答案文件 '{file_path}' 已成功生成！")
    except Exception as e:
        print(f"生成文件时发生错误: {e}")

# 调用函数，传入已填写的答案
save_csv(a1, a2, a3, a4, a5)
