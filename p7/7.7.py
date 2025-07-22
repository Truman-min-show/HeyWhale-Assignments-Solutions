# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: 文本生成任务根据输入数据的模态可以分为多种。
# (1)文本到文本（如翻译、摘要）、(2)数据到文本（如从表格生成报告）、
# 和(3)图像到文本（如图说）都是文本生成领域公认的重要分类。
A1 = 'C'

# Q2: BLEU, NIST, 和 ROUGE 都是自然语言生成领域广泛使用的、基于n-gram重叠度的评估指标。
# AUC（Area Under the Curve）是用于评估二分类模型性能的指标，衡量模型区分正负样本的能力，
# 不适用于评估生成文本的质量。
A2 = 'C'

# Q3: GPT-2和BERT的核心区别在于它们使用的Transformer结构不同。
# BERT使用Transformer的Encoder（编码器）部分，是双向的。
# GPT-2使用Transformer的Decoder（解码器）部分，是单向的（自回归）。
# 它们的预训练任务也不同。但它们共同的基础都是源于Transformer架构。
A3 = 'C'

# Q4: HuggingFace的 `generate` 方法为`AutoModelForCausalLM`这类自回归模型提供了多种解码策略。
# 贪心搜索（Greedy Search）、集束搜索（Beam Search）以及各种采样方法（包括温度采样、Top-K、Top-p）
# 都是支持的。
A4 = 'D'

# Q5: 这句话是正确的。不同的解码策略有不同的优缺点。
# 例如，贪心搜索速度快但可能生成重复乏味的内容；集束搜索更流畅但可能缺乏创造性；
# 采样方法更多样化但可能牺牲事实准确性。
# 因此，需要根据具体的应用场景（如要求事实准确的摘要 vs. 要求创造性的故事生成）来选择最合适的解码方法。
A5 = 'A'


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
        file_path = "task07.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3, A4, A5)