a1=4567

# In [40]:
# 初始错乱状态
zbj = '唐僧'
ss = '猪八戒'
ts = '沙僧'

# 利用Python的元组赋值特性，一行代码完成三个变量的循环交换
# 将 ss 的值('猪八戒')赋给 zbj
# 将 ts 的值('沙僧')赋给 ss
# 将 zbj 的值('唐僧')赋给 ts
zbj, ss, ts = ss, ts, zbj

# 现在，变量名（躯体）和变量值（灵魂）已经一一对应了
# zbj 的值是 '猪八戒'
# ss 的值是 '沙僧'
# ts 的值是 '唐僧'
# In [41]:
# 把最终合并后的字符串赋值给a2，并运行
a2 = zbj + ss + ts

# 运行后 a2 的值会是：'猪八戒沙僧唐僧'

# 生成 csv 作业答案文件
def save_csv(a1,a2):
    import pandas as pd
    df = pd.DataFrame({"id": ["q1","q2"], "answer": [a1,a2]})
    df.to_csv("answer_2.csv", index=None)

save_csv(a1,a2)  # 运行这个cell,生成答案文件；该文件在左侧文件树project工作区下，你可以自行右击下载或者读取查看
#cd /mnt/c/Users/lenovo/Desktop/internship/code
#./heywhale_submit -token 5f1ba9f600843e65 -file ./p1/answer_2.csv