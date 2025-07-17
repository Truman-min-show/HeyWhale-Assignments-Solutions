
import pandas as pd


from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split


"""
cancer = datasets.load_breast_cancer()
x = pd.DataFrame(cancer.data)
y = pd.DataFrame(cancer.target)
x.head(), y.head()

x[x.index == 411]

# 数据基础分析

x.info(), y.info()


x.describe().T, y.describe().T


# 模型训练

# 1. 拆分数据训练集和测试集，比例 7:3
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
x_train.head(), x_test.head(), y_train.head(), y_test.head()

# 2. 构建模型

model = LinearRegression()

# 3. 训练模型

model.fit(x_train, y_train)

# 4. 使用测试集测试模型获取测试结果

data_tmp = pd.DataFrame({0:11.04, 1:16.83, 2:70.92, 3:373.2, 4:0.1077, 5:0.07804, 6:0.03046, 7:0.0248, 8:0.1714, 9:0.0634, 10:0.1967, 11:1.387, 12:1.342, 13:13.54, 14:0.005158,
                        15:0.009355, 16:0.01056, 17:0.007483, 18:0.01718, 19:0.002198, 20:12.41, 21:26.44, 22:79.93, 23:471.4, 24:0.1369, 25:0.1482, 26:0.1067,
                        27:0.07431, 28:0.2998, 29:0.07881}, index=[0])
y_pred = model.predict(data_tmp)
print(y_pred)
# 此输出的是预测为1 的概率
"""


a1 = 'A'  # 如 a1= 'B'
a2 = 'B'  # 如 a2= 'B'
a3 = 'A'  # 如 a3= 'B'


# 生成 csv 作业答案文件
def save_csv(a1, a2, a3):
    df = pd.DataFrame({"id": ["q1", "q2", "q3"], "answer": [a1, a2, a3]})
    df.to_csv("answer_1.csv", index=None)
    print(df)

save_csv(a1,a2,a3)