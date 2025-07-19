import numpy as np
from sklearn.decomposition import PCA

# 1. 生成数据
# 设定随机种子以确保结果可重现
np.random.seed(999)
# 生成一个 1000x2 的矩阵，数值均匀分布在 0 到 10 之间
original_data = np.random.rand(1000, 2) * 10

# 2. 降维
# 初始化 PCA，目标是降到 1 维
pca = PCA(n_components=1)
# 执行 PCA 降维
reduced_data = pca.fit_transform(original_data)

# 3. 计算均值和方差
# 计算原始二维数据的整体均值和方差
original_mean = np.mean(original_data)
original_variance = np.var(original_data)

# 计算降维后一维数据的均值和方差
reduced_mean = np.mean(reduced_data)
reduced_variance = np.var(reduced_data)

# 4. 答案
# 将计算结果四舍五入到小数点后两位，并存入列表
a1 = [round(original_mean, 2), round(original_variance, 2), round(reduced_mean, 2), round(reduced_variance, 2)]

# 打印结果进行验证
#print(f"原始数据均值: {original_mean:.2f}")
#print(f"原始数据方差: {original_variance:.2f}")
#print(f"降维后数据均值: {reduced_mean:.2f}")
#print(f"降维后数据方差: {reduced_variance:.2f}")
#print(f"答案 a1 = {a1}")

import networkx as nx
import numpy as np

# 1. 创建图模型
# 创建一个无向图物件
G = nx.Graph()
# 定义边并加入图中
edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 1), (2, 4)]
G.add_edges_from(edges)

# 2. 计算节点度数
# 取得每个节点的度数，并转换为 NumPy 阵列以便进行向量运算
degrees = np.array([val for (node, val) in G.degree()])

# 3. 计算度数的熵
# 关键步骤：根据参考代码，将度数列表标准化为机率分布
# 计算方式是每个节点的度数 / 所有节点度数的总和
degree_probabilities = degrees / np.sum(degrees)

# 使用熵的公式 H(X) = -Σ(p(x) * log2(p(x))) 来计算
# 加上一个极小值 1e-10 是为了防止 log2(0) 的数学错误
degree_entropy = -np.sum(degree_probabilities * np.log2(degree_probabilities + 1e-10))

# 4. 答案
# 将计算出的熵四舍五入到小数点后两位，并存入列表
a2 = [round(degree_entropy, 2)]

# (选填) 打印中间结果以供验证
# print(f"各个节点的度数: {degrees}")
# print(f"度数总和: {np.sum(degrees)}")
# print(f"标准化后的机率: {degree_probabilities}")
# print(f"最终答案 a2: {a2}")


# 构造一个dict对象储存结果
answer = {
    "q1": a1,
    "q2": a2
}

# 定义一个保存文件的函数
# 保存时输入dict对象和文件名称，保存的文件会出现左侧文件树的`project`文件夹下
def to_json(answer: dict, file_name: str):
    '''
    :param answer: 答案的dict对象
    :param file_name: 注意文件名称要用json后缀
    '''
    from json import dump
    from re import search

    if not search('answer_\d\.json', file_name):
        raise Exception('文件名称格式不符')

    with open(file_name, 'w') as f:
        dump(answer, f)

# 调用函数
to_json(answer, 'answer_1.json')
