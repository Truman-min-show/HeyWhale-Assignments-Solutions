# STEP1: 按照要求计算下方题目结果
# ⚠️注意以下均为选择题，完成题目后，将每个Q选项赋值的答案给A题号， 注意值须全部为大写字符串、无任何分隔符（如：A1 ='A')

"""
Q1: torch.cuda.is_available() 是PyTorch中用于检查CUDA（即NVIDIA GPU）是否可用并已正确配置的标准函数。所以答案是 A。
Q2: 在Pandas中，train.shape[0] 返回DataFrame的总行数。train.count() 返回每列的非空值数量。因此，总行数 - 非空值数 得到的就是每列的空值（NaN）数量。所以答案是 B。
Q3: [SEP], [UNK], [PAD], [CLS], [MASK] 都是BERT模型中预定义的特殊标记（special tokens），用于不同的目的（如分隔句子、表示未知词、填充、分类任务、掩码语言模型等）。所以答案是 D。
Q4: bert-base-chinese 模型是Google发布的中文BERT基础模型，其词汇表大小为 21128。所以答案是 A。
Q5: 对于bert-base-chinese模型：hidden_size（隐藏层维度）是768。last_hidden_state 的维度是 [batch_size, sequence_length, hidden_size]。
题目中序列长度（ids个数）为32，批次大小默认为1，所以形状为 [1, 32, 768]。
pooled_output 是 [CLS] 标记对应的隐藏状态经过一个全连接层和激活函数后的输出，维度为 [batch_size, hidden_size]，即 [1, 768]。
因此，选项A是正确的。所以答案是 A。
"""

# In [35]:
A1='A'
# In [36]:
A2='B'
# In [37]:
A3='D'
# In [38]:
A4='A'
# In [39]:
A5='A'

# STEP2: 将结果保存为 csv 文件
# csv 需要有两列，列名：id、answer。其中，id 列为题号，如 Q1、Q2、Q3、Q4、Q5。
# answer 列为各题你的答案。

# In [40]:
import pandas as pd
# In [41]:
# answer=pd.DataFrame() # 此行可以省略，因为变量未被使用

# In [42]:
def save_csv():
    """
    创建一个包含问题ID和答案的DataFrame，并将其保存为CSV文件。
    该函数直接使用全局变量 A1, A2, A3, A4, A5。
    """
    df = pd.DataFrame({
        "id": ["Q1", "Q2", "Q3", "Q4", "Q5"],
        "answer": [A1, A2, A3, A4, A5]
    })
    print("将要保存的DataFrame内容：")
    print(df)
    # 将DataFrame保存到名为 "task02.csv" 的文件中，不包含pandas的默认索引列
    df.to_csv("task02.csv", index=None)
    print("\n文件 'task02.csv' 已成功保存。")

# 执行这个cell,就可以获得文件了；文件在左侧文件树 project 工作区下
save_csv()
