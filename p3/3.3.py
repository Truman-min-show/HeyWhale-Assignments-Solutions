# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# aihub.cloud.google.com Assignment
# ----------------------------------------------------------------

import pandas as pd
import json

# ------------------- STEP 1: 完成题目 -------------------

# --- Q1 表格纵向合并 ---
# 背景：
# pd.concat() 是用于沿特定轴（默认为纵向，axis=0）拼接对象的函数。
# 由于两个DataFrame的列结构相同，纵向合并是最佳选择。
# pd.merge() 用于数据库风格的连接操作，不适用于简单的行追加。
# axis=1 会导致横向合并，这不是题目要求。
# 因此，选项 C 是正确的。
a1 = "C"


# --- Q2 表格横向连接 ---
# 背景：合并玩家信息和成绩，并按得分排序。

# 1. 初始化原始数据
players_info = pd.DataFrame({
    '玩家ID': [101, 102, 103, 104],
    '姓名': ['Alice', 'Bob', 'Charlie', 'David'],
    '等级': [5, 7, 8, 6]
})
players_scores = pd.DataFrame({
    '玩家ID': [101, 102, 103, 105],
    '游戏得分': [1500, 1800, 1700, 1600],
    '游戏时间': [120, 150, 180, 200]
})

# 2. 使用 'left' join 合并，以 players_info 为主表
merged_df = pd.merge(players_info, players_scores, on='玩家ID', how='left')

# 3. 按 '游戏得分' 降序排列
sorted_df = merged_df.sort_values(by='游戏得分', ascending=False)

# 4. 提取前三名的姓名
top_three_names = sorted_df['姓名'].iloc[0:3].tolist()

# 5. 取每个姓名的首字母，并拼接成字符串
# 结果顺序: Bob, Charlie, Alice -> BCA
a2 = "".join([name[0] for name in top_three_names])


# --- Q3 数据清洗 ---
# 背景：处理任务数据中的空值和重复项。

# 1. 初始化原始数据
quests_info = pd.DataFrame({
    '士兵ID': [301, 302, 303, 304, 305, 306, 307, 302],
    '任务描述': ['击败敌人', None, '收集物品', '护送NPC', None, '探索区域', '完成任务链', None],
    '任务奖励': [100, 150, 200, 250, 300, 350, 400, 180],
    '任务难度': ['简单', '中等', '困难', '简单', '中等', '困难', '简单', '高级'],
    '任务时间': [30, 45, 60, 30, 45, 60, 30, 45]
})

# 2. 创建副本进行操作
cleaned_df = quests_info.copy()

# 3. (修复) 将 '任务描述' 中的空值替换为 '数据未返回'，使用推荐的赋值语法
cleaned_df['任务描述'] = cleaned_df['任务描述'].fillna('数据未返回')

# 4. (修复) 删除 '士兵ID' 的重复行，保留最后一次出现的记录，使用推荐的赋值语法
a3 = cleaned_df.drop_duplicates(subset=['士兵ID'], keep='last')


# --- Q4 表格排序 ---
# 背景：根据胜率对种族实力进行排序。

# 1. (修复) 初始化原始数据，修正'种族'列的长度
adventures = pd.DataFrame({
    '姓名': ['艾琳', '博尔', '卡尔', '戴安娜', '埃里克', '菲奥娜', '格雷戈', '赫尔加', '伊莎贝尔', '杰克'],
    '种族': ['精灵', '人类', '矮人', '精灵', '人类', '矮人', '精灵', '人类', '矮人', '精灵'],
    '角色类型': ['战士', '法师', '战士', '刺客', '法师', '战士', '法师', '刺客', '法师', '战士'],
    '战斗次数': [30, 45, 40, 35, 50, 25, 55, 20, 60, 33],
    '胜利次数': [15, 28, 37, 26, 19, 14, 20, 13, 32, 17]
})

# 2. 计算战斗次数的中位数
median_battles = adventures['战斗次数'].median()

# 3. 筛选战斗次数大于中位数的英雄
experienced_heroes = adventures[adventures['战斗次数'] > median_battles].copy()

# 4. 按种族分组，并计算每个种族总的胜利次数和战斗次数
race_stats = experienced_heroes.groupby('种族')[['胜利次数', '战斗次数']].sum()

# 5. 计算每个种族的胜率
race_stats['胜率'] = race_stats['胜利次数'] / race_stats['战斗次数']

# 6. 按胜率降序排序并提取胜率值
# 计算出的胜率约等于 [0.69, 0.49, 0.36]，与选项 A 匹配。
print(race_stats['胜率'])
a4 = "A"


# ------------------- STEP 2: 将结果保存为 json 文件 -------------------

# 生成 json 作业答案文件
def save_json(ans1, ans2, ans3_df, ans4):
    """
    将最终答案保存到 JSON 文件中。
    """
    try:
        # a3是DataFrame，需要先转换为字典
        a3_dict = ans3_df.to_dict(orient='list')

        json_data = {
            "q1": ans1,
            "q2": ans2,
            "q3": a3_dict,
            "q4": ans4
        }
        # ensure_ascii=False 确保中文字符能正确显示
        json_str = json.dumps(json_data, indent=4, ensure_ascii=False)
        file_path = 'answer_3.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)
        print(f"文件 '{file_path}' 已成功生成。")
    except Exception as e:
        print(f"写入文件时出错: {e}")

# 运行这个cell,生成答案文件
save_json(a1, a2, a3, a4)