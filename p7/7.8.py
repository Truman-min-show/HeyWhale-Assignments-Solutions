# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: 抽取式摘要（Extractive Summarization）通过从原文中抽取关键句子或短语来组成摘要。
# TextRank是一种基于图的排序算法，用于评估句子在文本中的重要性，是实现抽取式摘要的经典算法。
# SVM和Random Forest是通用的分类/回归算法，不是专门的摘要算法。
A1 = 'A'

# Q2: 文本摘要，尤其是生成式摘要，本质上是一个将长序列（原文）映射到短序列（摘要）的任务。
# Seq2Seq（Sequence-to-Sequence）架构，包含一个编码器和一个解码器，是专门为处理这类任务而设计的。
# LSTM、CNN和GRU可以是构成Seq2Seq模型的组件，但Seq2Seq是描述整个任务的框架结构。
A2 = 'C'

# Q3: T5, BART, 和 PEGASUS 都是 Encoder-Decoder（编码器-解码器）架构，能够处理并生成文本，因此非常适合做文本摘要任务。
# Bert 是一个 Encoder-only（仅编码器）架构，它擅长理解文本并生成文本表示，但自身不具备生成新文本的能力（没有解码器），
# 因此不适合直接用于生成式摘要任务。
A3 = 'A'

# Q4: ROUGE 是文本摘要任务最常用、最标准的评估指标。BLEU 源于机器翻译，侧重于精确率，
# 虽然不如ROUGE常用，但它同样是衡量生成文本与参考文本相似度的n-gram指标，因此也可以被用来评估摘要质量。
# 所以这个说法是正确的。
A4 = 'A'

# Q5: 这段描述是完全正确的。对于Seq2Seq模型，解码器的输入（通常是目标文本）在处理时有特殊要求
# （例如，添加特定的起始符、进行偏移等）。使用 `with tokenizer.as_target_tokenizer():` 上下文管理器，
# 可以让同一个tokenizer实例在处理目标文本时，自动应用这些为解码器准备的特殊规则。
A5 = 'B'


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
        file_path = "task08.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3, A4, A5)