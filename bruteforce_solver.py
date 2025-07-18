# 文件名: bruteforce_solver.py

import os
import sys
import subprocess
import random
import csv


# --- 辅助函数 (无变动) ---

def get_validated_input(prompt, type_converter=int):
    """持续提示用户，直到输入了指定类型的有效值。"""
    while True:
        try:
            return type_converter(input(prompt))
        except ValueError:
            print("输入无效。请输入一个有效的数字。", file=sys.stderr)


def confirm_action(prompt):
    """向用户请求 Y/N 确认。"""
    response = input(f"{prompt} [Y/n]: ").strip().lower()
    return response in ['', 'y', 'yes']


# --- 核心逻辑函数 ---

def get_problem_details():
    """从用户处收集并确认关于测验的所有必要信息。(无变动)"""
    while True:
        print("\n--- 请提供测验详情 ---")
        project_num = get_validated_input("请输入项目编号 (例如, p5 请输入 5): ")
        level_num = get_validated_input("请输入关卡编号 (例如, answer_2.csv 请输入 2): ")
        total_questions = get_validated_input("请输入总题数: ")

        options_per_question = []
        print("\n现在，请输入每道题的选项数量 (例如, A/B/C 三个选项请输入 3)。")
        for i in range(total_questions):
            while True:
                num_choices = get_validated_input(f"  - 第 {i + 1} 题的选项数量: ")
                if 1 <= num_choices <= 4:
                    options_per_question.append(num_choices)
                    break
                else:
                    print("错误: 请输入 1 到 4 之间的数字。", file=sys.stderr)

        print("\n--- 请确认信息 ---")
        print(f"项目: p{project_num}")
        print(f"关卡: {level_num}")
        print(f"总题数: {total_questions}")
        for i, count in enumerate(options_per_question):
            print(f"  - 第 {i + 1} 题有 {count} 个选项。")

        if confirm_action("以上信息是否正确？"):
            return project_num, level_num, total_questions, options_per_question
        else:
            print("\n信息有误，将重新开始输入流程...")


# --- 新增函数 ---
def save_answers_to_csv(answer_sheet, project_num, level_num):
    """仅负责将当前的答案字典保存到CSV文件中。"""
    # 强制使用正斜杠'/'来构建路径，确保提交脚本的-f参数格式正确
    relative_path = f'p{project_num}/answer_{level_num}.csv'

    # 确保目录存在
    os.makedirs(os.path.dirname(relative_path), exist_ok=True)

    # 写入 CSV 文件
    with open(relative_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'answer'])
        for q_num, answer in sorted(answer_sheet.items()):  # 按题号排序后写入
            writer.writerow([f'q{q_num}', answer])

    print(f"✅ 当前答案已保存至: {relative_path}")
    return relative_path


def run_submission(token, csv_path):
    """执行 submit.py 脚本来上传答案。(无变动)"""
    if not confirm_action(f"🚀 已准备好提交 '{csv_path}'。是否继续上传？"):
        print("用户已取消提交。")
        return False

    command = [sys.executable, 'submit.py', '-t', token, '-f', csv_path]

    print(f"\n正在执行命令: {' '.join(command)}")
    print("--- 提交脚本输出 ---")
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True, encoding='utf-8')
        print(result.stdout)
        if result.stderr:
            print("--- 提交脚本错误 ---", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
    except FileNotFoundError:
        print("致命错误: 在当前目录下未找到 'submit.py'。", file=sys.stderr)
        return False
    except subprocess.CalledProcessError as e:
        print("\n--- 提交失败 ---", file=sys.stderr)
        print("提交脚本运行出错并退出。", file=sys.stderr)
        print("脚本输出:", file=sys.stderr)
        print(e.stdout, file=sys.stderr)
        print("脚本错误输出:", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        return False
    except Exception as e:
        print(f"提交过程中发生意外错误: {e}", file=sys.stderr)
        return False

    print("-------------------------")
    print("✅ 提交命令执行完毕。")
    return True


def get_incorrect_questions(total_questions):
    """询问用户哪些题号是错误的。(无变动)"""
    while True:
        print("\n❓ 请根据上次提交结果提供反馈。")
        user_input = input("请输入回答错误的题号，以空格分隔 (例如: '3 8 15')。\n如果全部正确，请输入 '0': ")

        if not user_input.strip():
            print("输入不能为空，请重试。", file=sys.stderr)
            continue

        try:
            incorrect_nums = [int(n) for n in user_input.split()]
            if any(n < 0 or n > total_questions for n in incorrect_nums):
                print(f"错误: 所有题号必须在 1 到 {total_questions} 之间，或者为 0。", file=sys.stderr)
                continue
            if confirm_action(f"您输入了以下错误题号: {incorrect_nums}。是否正确？"):
                return incorrect_nums
        except ValueError:
            print("输入无效。请输入仅由数字和空格组成的内容。", file=sys.stderr)


# --- 主程序 (逻辑已完全重构) ---

def main():
    """主函数，用于协调整个穷举流程。"""
    print("--- 和鲸(HeyWhale)选择题答案穷举助手 ---")

    # 1. 初始化设置
    project_num, level_num, total_questions, options_per_question = get_problem_details()

    all_options = ['A', 'B', 'C', 'D']
    possible_answers = {
        i + 1: all_options[:options_per_question[i]] for i in range(total_questions)
    }

    submission_token = input("\n请输入您的和鲸(HeyWhale)提交令牌(token): ").strip()

    # --- 已修复：逻辑重构 ---
    # 2. 仅在最开始时，生成一份完整的初始随机答案
    print("\n🔄 正在生成初始随机答案...")
    master_answer_sheet = {}
    for q_num in range(1, total_questions + 1):
        master_answer_sheet[q_num] = random.choice(possible_answers[q_num])
    print("✅ 初始答案生成完毕。")

    # 3. 迭代循环，最多尝试4次
    for attempt in range(1, 5):
        print(f"\n=============== 第 {attempt} 次尝试 ===============")

        # 3.1. 将当前的主答案表保存到文件
        csv_path = save_answers_to_csv(master_answer_sheet, project_num, level_num)

        # 3.2. 运行提交脚本
        if not run_submission(submission_token, csv_path):
            print("因提交被取消或发生错误，程序停止。")
            break

        # 3.3. 获取反馈
        incorrect_q_nums = get_incorrect_questions(total_questions)

        # 3.4. 处理反馈
        if incorrect_q_nums == [0]:
            print("\n🎉 恭喜！所有答案均正确，问题解决！")
            break

        # --- 已修复：核心更新逻辑 ---
        # 仅更新被标记为错误的题目的答案
        print("\n正在根据反馈更新错误题目的答案...")
        for q_num in incorrect_q_nums:
            if q_num not in master_answer_sheet: continue

            # a. 从可用选项中移除已知的错误答案
            wrong_answer = master_answer_sheet[q_num]
            if wrong_answer in possible_answers[q_num]:
                possible_answers[q_num].remove(wrong_answer)
                print(f"  - 对于第 {q_num} 题, 排除错误选项 '{wrong_answer}'。剩余可用: {possible_answers[q_num]}")

            # b. 仅为这道错题选择一个新的答案并更新到主答案表
            if possible_answers[q_num]:
                new_answer = random.choice(possible_answers[q_num])
                master_answer_sheet[q_num] = new_answer
                print(f"  - 第 {q_num} 题的新答案已更新为: '{new_answer}'")
            else:
                print(f"⚠️ 警告: 第 {q_num} 题已无剩余可用选项！将其标记为 '?'")
                master_answer_sheet[q_num] = '?'

        print("\n✅ 答案更新完毕，正确的题目答案保持不变。")

        if attempt == 4:
            print("\n🏁 已达到最大尝试次数，正确答案理应已被找到。")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序被用户中断。正在退出。")
        sys.exit(0)