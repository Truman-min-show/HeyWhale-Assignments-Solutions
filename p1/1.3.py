# Q1 计算代码
total_products = 50000
price = 5000
sell_discount = 0.8
return_rate = 0.2

actual_price = price * sell_discount
final_revenue = total_products * (1 - return_rate) * actual_price
a1 = round(final_revenue)
print(f"a1 = {a1}")

# Q1 最终答案
a1 = 160000000

# Q2 最终答案
a2 = 4312
print(f"a2 = {a2}")

# Q3 计算代码
# 选手A
a = [5, 7, 3, 9]
a.append(5)
a.sort()
a.pop(0)
a.pop(-1)
avg_a = sum(a) / len(a)

# 选手B
b = [1, 5, 3, 8]
b.append(6)
b.sort()
b.pop(0)
b.pop(-1)
avg_b = sum(b) / len(b)

# 选手C
c = [6, 8, 10, 5]
c.append(9)
c.sort()
c.pop(0)
c.pop(-1)
avg_c = sum(c) / len(c)

# 求和
total_score = avg_a + avg_b + avg_c
a3 = round(total_score)
print(f"a3 = {a3}")

# Q3 最终答案
a3 = 18

# 生成 csv 作业答案文件
import pandas as pd

# 从前面的步骤获取变量值
a1 = 160000000
a2 = 4312
a3 = 18

def save_csv(a1, a2, a3):
    df = pd.DataFrame({"id": ["q1", "q2", "q3"], "answer": [a1, a2, a3]})
    df.to_csv("answer_3.csv", index=None)

save_csv(a1, a2, a3) # 运行这个cell,生成答案文件；该文件在左侧文件树project工作区下，你可以自行右击下载或者读取查看

print("已成功生成 answer_3.csv 文件。")
print("文件内容如下：")
print(pd.read_csv("answer_3.csv"))