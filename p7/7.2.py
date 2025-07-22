# STEP1: 按照要求计算下方题目结果
# ⚠️注意以下均为选择题，完成题目后，将每个Q选项赋值的答案给A题号， 注意值须全部为大写字符串、无任何分隔符（如：A1 ='A')

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
