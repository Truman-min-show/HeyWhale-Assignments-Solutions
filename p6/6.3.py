import numpy as np
import pandas as pd

# STEP1：请根据要求完成题目
# Q1: 给定一个大小为 32x32x1 的灰度图像（MNIST 手写数字图像），以及一个大小为 3x3x1x8 的卷积核，使用 conv2D_gemm 函数（我们上文中实现的）对图像进行卷积运算，步幅为 1，并填充方式为 same。 请问卷积结果的形状是多少？
# 提示：参考教案中GEMM转换的实现代码

# 假设输入为单个图像，通常会增加一个 batch 维度，即 (1, 32, 32, 1)
# 输入图像的高宽
H, W = 32, 32
# 步幅
S = 1
# 填充方式
padding = 'same'
# 卷积核中的滤波器数量
K = 8

# 对于 'same' 填充，输出的高度和宽度计算如下：
# output_height = ceil(float(H) / float(S))
# output_width = ceil(float(W) / float(S))
# 在这里，H=32, S=1，所以 output_height = 32
# W=32, S=1，所以 output_width = 32
output_h = int(np.ceil(float(H) / float(S)))
output_w = int(np.ceil(float(W) / float(S)))

# 输出通道数等于卷积核的个数
output_c = K

# 假设 batch size 为 1，则输出形状为 (batch_size, output_h, output_w, output_c)
output_shape = (1, output_h, output_w, output_c)

# 将卷积结果的形状作为答案赋值给 a1
a1 = str(output_shape).replace(" ", "") # 格式化为 "(1,32,32,8)"
# 根据题目要求格式化为 "(1, 32, 32, 8)"
a1 = f"({output_shape[0]}, {output_shape[1]}, {output_shape[2]}, {output_shape[3]})"

# Q2: 你正在实现一个简单的卷积神经网络（CNN）。请从以下选项中选择正确的代码片段，用于在卷积层中计算卷积操作的前向传播。假设输入图像为 28x28x1，卷积核大小为 3x3x1x8，步幅为 1，填充为 same。
# 哪段代码正确地实现了卷积操作的前向传播？(不使用高级api)
#
# 分析：
# [cite_start]A. 使用 scipy.signal.convolve2d，这是一个库函数，属于高级API。此外，它不直接支持多通道卷积。 [cite: 1]
# [cite_start]B. 使用 im2col 和 GEMM (矩阵乘法) 的方法是实现卷积的手动、底层方式，不依赖于深度学习框架的内置卷积层。这是正确的。 [cite: 2]
# [cite_start]C. 使用 tf.nn.conv2d，这是 TensorFlow 的高级 API。 [cite: 3]
# [cite_start]D. 使用 torch.nn.Conv2d，这是 PyTorch 的高级 API。 [cite: 4]
a2 = "B"

# Q3:你正在实现一个简单的循环神经网络（RNN）模型，并希望使用长短期记忆网络（LSTM）来解决梯度消失和梯度爆炸的问题。请从以下选项中选择正确的代码片段，使用LSTM来处理一个简单的序列数据。
# 哪段代码正确地实现了LSTM单元的前向传播？(不使用高级api)
# 提示：参考教案中循环神经网络（RNN）模型的实现代码
#
# 分析：
# [cite_start]A. 该代码段使用 numpy 手动实现了 LSTM 的核心计算，包括输入门、遗忘门、输出门和细胞状态的更新。这符合“不使用高级api”的要求。 [cite: 5, 6]
# [cite_start]B. 使用 tf.keras.layers.LSTMCell，这是 TensorFlow 的高级 API。 [cite: 7]
# [cite_start]C. 使用 torch.nn.LSTM，这是 PyTorch 的高级 API。 [cite: 8]
# [cite_start]D. 使用 sklearn.neural_network.MLPRegressor，这根本不是一个 LSTM 实现。 [cite: 9]
a3 = "A"

# Q4: 你正在实现一个简单的自动编码器（Autoencoder）模型来进行数据压缩和重构。请从以下选项中选择正确的代码片段，用于实现一个基本的全连接自动编码器的前向传播部分。假设输入数据为 784 维（例如MNIST图像的展平版本），编码器将其压缩到 64 维，解码器将其重构回 784 维。
# 哪段代码正确地实现了自动编码器的前向传播？(不使用高级api)
# 提示：参考教案中自动编码器（Autoencoder）模型的实现原理
#
# 分析：
# [cite_start]A. 该代码段使用 numpy 手动实现了自动编码器的编码和解码过程（矩阵乘法、加偏置、激活函数），符合“不使用高级api”的要求。 [cite: 10]
# [cite_start]B. 使用 tf.matmul 和 tf.nn.tanh，这是 TensorFlow 的高级 API。 [cite: 11]
# [cite_start]C. 使用 torch.nn.Linear，这是 PyTorch 的高级 API。 [cite: 12]
# [cite_start]D. 使用 sklearn.neural_network.MLPRegressor，这不是一个自动编码器实现。 [cite: 13]
a4 = "A"


# STEP2：将结果保存为 csv 文件
# 将结果保存为 csv 文件
# csv 需要有两列，列名：id、answer。其中，id 列为题号，如 q1、q2、q3；answer 列为 STEP1 中各题你计算出来的结果。💡 这一步的代码你不用做任何修改，直接运行即可。
def save_csv(a1, a2, a3, a4):
    df = pd.DataFrame({"id": ["q1", "q2", "q3", "q4"], "answer": [a1, a2, a3, a4]})
    # According to the problem description, save to "answer_3.csv"
    df.to_csv("answer_3.csv", index=None)
    print("CSV file 'answer_3.csv' created successfully.")
    print(df)

save_csv(a1, a2, a3, a4)