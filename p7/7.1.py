# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: HuggingFace的中文名称是“抱抱脸”。
A1 = 'A'

# Q2: HuggingFace transformers 库的官方 GitHub 地址是 huggingface 组织下的 transformers仓库。
A2 = 'B'

# Q3: HuggingFace 的模型仓库（Model Hub）地址是 https://huggingface.co/models。
A3 = 'C'

# Q4: tokenizer.encode_plus 在 return_token_type_ids=True 和 return_attention_mask=True 的情况下，
# 会返回三个主键：'input_ids' (默认), 'token_type_ids', 和 'attention_mask'。
A4 = 'A'

# Q5: 当在模型配置中设置 output_hidden_states=True 时，
# 模型输出会包含三个主_键：'last_hidden_state', 'pooler_output', 和 'hidden_states'。
A5 = 'C'


# ------------------- STEP 2: 将结果保存为 csv 文件 -------------------

# 修正并定义一个功能完整的保存函数
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
        file_path = "task01.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3, A4, A5)