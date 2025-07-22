# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: 在处理像SWAG这样的多选任务时，输入通常是“上下文”和“选项”的组合。
# 为了保留完整的选项信息以供模型判断，通常会优先截断较长的上下文部分。
A1 = 'B'

# Q2: HuggingFace Tokenizer的`truncation`参数支持的策略包括 'longest_first'（默认）、
# 'only_first'、'only_second' 和 'do_not_truncate' (或False)。
# 'full' 并不是一个有效的截断策略选项。
A2 = 'D'

# Q3: 在使用滑窗（overflowing tokens）处理长文本时，`stride`参数用于定义
# 连续文本块（chunk）之间的重叠token数量，即滑窗的步长。
A3 = 'D'

# Q4: HuggingFace `transformers`库为不同的任务提供了专门的模型结构。
# 对于多项选择任务，应该使用 `AutoModelForMultipleChoice`，它在基础模型之上
# 添加了一个适用于多选任务的分类头。
A4 = 'D'

# Q5: 多项选择任务的目标是从多个选项中选出唯一正确的答案。
# 因此，最直接、最常用的评估指标是准确率（Accuracy），即模型选对的题目数占总题目数的比例。
# AUC主要用于二分类，RMSE用于回归。
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
        # 根据之前的任务模式，文件名通常为taskXX.csv
        file_path = "task06.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3, A4, A5)