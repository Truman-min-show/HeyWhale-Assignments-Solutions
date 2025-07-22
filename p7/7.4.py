# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd


# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: 句子相似性识别任务需要模型理解两个句子之间的关系，
# 这与BERT的“下一句预测”（Next Sentence Prediction, NSP）预训练任务的目标非常相似。
A1 = 'B'

# Q2: 当Tokenizer处理句子对（如sent1, sent2）时，
# 'token_type_ids'（或称segment IDs）被用来区分不同的句子。
# 按照惯例，第一个句子的所有token会被标记为0，第二个句子的所有token会被标记为1。
A2 = 'B'

# Q3: 梯度累加（gradient accumulation）是一种通过多次计算小批量（mini-batch）的梯度并将它们累加起来，
# 然后再用累加后的梯度更新模型参数的技术。这在数学效果上等同于使用一个更大的批量（batch size），
# 从而在GPU内存有限的情况下，实现大批量训练的效果。
A3 = 'B'

# Q4: 在PyTorch中，将一个参数（parameter）的 `requires_grad` 属性设置为 `False`，
# 意味着在反向传播过程中不会为该参数计算梯度。因此，优化器在更新权重时会跳过这个参数。
# 这个操作通常被称为“冻结”参数，使其在训练中保持不变。
A4 = 'A'

# Q5: 代码中的函数 `set_seed` 为所有相关的库（PyTorch, NumPy, Python random）都设置了固定的随机种子，
# 并配置了CUDA使用确定性算法。这样做的核心目的是消除由随机性（如权重初始化、数据洗牌、dropout等）
# 带来的训练结果波动，从而保证每次运行代码时都能得到完全相同的结果，即保证了实验的“可复现性”。
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
        file_path = "task04.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3, A4, A5)