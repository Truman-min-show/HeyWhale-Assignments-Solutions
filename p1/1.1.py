a1 = 'B'  # 如 a1= 'A'
a2 = 'ABCD'  # 如 a2= 'AB'
a3 = 'B'  # 如 a3= 'A'
a4 = 'A'  # 如 a4= 'A'

def save_csv(a1,a2,a3,a4):
    import pandas as pd
    df = pd.DataFrame({"id": ["q1","q2","q3","q4"], "answer": [a1,a2,a3,a4]})
    df.to_csv("answer_1.csv", index=None)

save_csv(a1,a2,a3,a4)