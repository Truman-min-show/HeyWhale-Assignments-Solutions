# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: 机器翻译是将一个语言序列转换为另一个语言序列的典型任务。
# 在HuggingFace中，这类任务由Sequence-to-Sequence（Seq2Seq）模型结构来处理。
# AutoModelForSeq2SeqLM 是专门用于此类任务（包括翻译、摘要等）的类。
A1 = 'D'

# Q2: `tokenizer.as_target_tokenizer()` 上下文管理器用于确保目标文本（即解码器的输入标签）
# 被正确地token化。对于许多Seq2Seq模型（如BART, T5, Marian），
# 这意味着在token序列的末尾添加一个表示序列结束的特殊符号，通常是 `</s>`。
A2 = 'C'

# Q3: SacreBLEU 工具包的主要贡献是解决了BLEU分数难以复现的问题。
# 在SacreBLEU出现之前，研究者们使用各自不同的预处理和分词（tokenize）脚本，
# 导致即使是相同的模型和数据，报告出的BLEU分数也无法直接比较。
# SacreBLEU通过内置标准化的分词流程，确保了计算的一致性和结果的可比性。
A3 = 'A'


# ------------------- STEP 2: 将结果保存为 csv 文件 -------------------

def save_answers_to_csv(ans1, ans2, ans3):
    """
    将所有题目的答案保存到一个CSV文件中。
    """
    try:
        # 创建一个DataFrame来存储ID和答案
        answer_df = pd.DataFrame({
            "id": ["Q1", "Q2", "Q3"],
            "answer": [ans1, ans2, ans3]
        })

        # 将DataFrame保存为CSV文件，不包含索引列
        file_path = "task09.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3)