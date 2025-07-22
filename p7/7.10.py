# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd

# ------------------- STEP 1: 按照要求计算下方题目结果 -------------------

# Q1: 自动问答（QA）系统根据其寻找答案的数据来源，通常被划分为三大类：
# 1. 检索式问答（从大量非结构化文档中检索并抽取答案）。
# 2. 社区问答（从已有的问答对中寻找答案）。
# 3. 知识库问答（从结构化的知识图谱中查询答案）。
# 因此，三者都是正确的分类。
A1 = 'C'

# Q2: 自动问答系统按照其能够回答问题的领域范围，可以划分为：
# 1. 开放域问答（Open-domain QA），能回答关于任何主题的问题。
# 2. 垂直域/限定域问答（Vertical-domain/Closed-domain QA），专注于特定领域。
# 两者都是标准的划分方式。
A2 = 'C'

# Q3: 在基于Transformer的抽取式问答任务中（如SQuAD），模型的输出层通常是两个线性分类器。
# 对于输入文本中的每一个token，模型会预测两个概率：该token是答案开始位置的概率，以及该token是答案结束位置的概率。
# 最终通过寻找最优的起止点组合来确定答案。
A3 = 'A'

# Q4: 当在HuggingFace Tokenizer中设置 `return_offsets_mapping=True` 时，
# tokenizer会额外返回一个 `offset_mapping` 字段。这个字段记录了每个token
# 在原始输入字符串中对应的字符级起始和结束位置，即偏移量。
A4 = 'B'

# Q5: HuggingFace `transformers` 库为不同的NLP任务提供了专门的模型“头”。
# 对于抽取式问答任务，应该使用 `AutoModelForQuestionAnswering` 类。
# 这个类在基础模型之上添加了一个专门用于预测答案起始和结束位置的头部。
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
        file_path = "task10.csv"
        answer_df.to_csv(file_path, index=False)

        print(f"文件 '{file_path}' 已成功生成。")
        print("答案内容:")
        print(answer_df)

    except Exception as e:
        print(f"写入文件时出错: {e}")


# 执行函数，传入所有答案
save_answers_to_csv(A1, A2, A3, A4, A5)