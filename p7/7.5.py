# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: BERT (Bidirectional Encoder Representations from Transformers) 的核心结构是Transformer的编码器部分。
A1 = 'C'

# Q2: BERT的输入由三部分嵌入（Embedding）相加而成：Token Embeddings（词元嵌入）、
# Segment Embeddings（分段嵌入，用于区分句子对）和 Position Embeddings（位置嵌入）。
# Graph Embedding（图嵌入）用于处理图结构数据，不属于BERT的输入部分。
A2 = 'D'

# Q3: 官方发布的bert-base-uncased/cased模型的标准配置中，隐藏层大小（hidden size）为768。
A3 = 'C'

# Q4: BERT在其架构中使用了Layer Normalization（层归一化）。根据题目要求，答案需为大写字符串。
A4 = 'LAYERNORM'

# Q5: BERT的两个著名的预训练任务是 Masked Language Model (MLM) 和 Next Sentence Prediction (NSP)。
# 因此选项“两个都是”是正确的。
A5 = 'C'


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
        file_path = "task05.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3, A4, A5)