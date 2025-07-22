# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: 匹配中文术语与英文拼写。
# 二分类 -> 3. Binary classification
# 多分类 -> 1. Multiclass classification
# 多标签 -> 2. Multilabel classification
# 正确的顺序是 312。
A1 = 'B'

# Q2: 为多标签分类选择损失函数。
# 多标签分类将每个标签视为独立的二分类问题，因此BCEWithLogitsLoss (结合了Sigmoid和二元交叉熵)是标准且最适合的选择。
# CrossEntropyLoss 用于互斥的多分类任务。L1loss 用于回归任务。
A2 = 'A'

# Q3: 多标签分类的标签表示。
# 多标签任务的标签使用“多热编码”（multi-hot），即一个样本可以对应多个“1”，例如[1, 0, 1, 0]。
# “独热编码”（one-hot）表示一个样本只能有一个“1”，用于多分类任务。因此，多标签任务需要转为“one-hot”。
A3 = 'A'

# Q4: 多标签分类的最优阈值。
# 0.5是一个默认的、直观的阈值，但它很少是“最优”的。最优阈值取决于数据集的平衡情况以及评估指标（如F1-score），
# 通常需要通过在验证集上测试不同的阈值来确定。因此，该说法是错误的。
A4 = 'A'

# Q5: 多标签分类的评估指标。
# 多标签任务可以看作是多个二分类任务的集合，因此标准的分类指标如精确率（precision）、
# 召回率（recall）和F1分数（f1-score）都适用。通常会对每个标签计算这些指标，然后再进行平均（如宏平均、微平均）。
# 因此，A、B、C都可以作为评估指标。
A5 = 'D'


# ------------------- STEP 2: 将结果保存为 csv 文件 -------------------

def save_answers_to_csv(ans1, ans2, ans3, ans4, ans5):
    """
    将所有题目的答案保存到一个CSV文件中。
    """
    try:
        # 创建一个DataFrame来存储ID和答案
        answer_df = pd.DataFrame({
            "id": ["Q1", "Q2", "Q3", "Q4", "Q5"],
            "answer": [ans1, ans2, ans3, ans4, ans5]
        })

        # 将DataFrame保存为CSV文件，不包含索引列
        file_path = "task03.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3, A4, A5)