import random

print("このプログラムはユーザーが入力する最小数と最大数の間で、整数の乱数を作成します。\nユーザーはそれを当ててください。チャンスは5回です。")

# 最小数の入力
first_prompt = True
while True:
    if first_prompt:
        prompt_text = "まずは、最小数を整数で入力してください。"
        first_prompt = False
    else:
        prompt_text = "もう一度、最小数を整数で入力してください。"
    min_value = input(prompt_text)
    try:
        min_value = int(min_value)
        break
    except ValueError:
        print(f"{min_value} は整数ではありません。")

# 最大数の入力
second_prompt = True
while True:
    if second_prompt:
        second_text = "次に、最大数を整数で入力してください。"
        second_prompt = False
    else:
        second_text = "最大数を整数で入力してください。"
    max_value = input(second_text)
    try:
        max_value = int(max_value)
        if max_value < min_value:
            print(f"{min_value} よりも大きな数にしてください。")
            continue
        break
    except ValueError:
        print(f"{second_text} は整数ではありません。")

# 乱数を作成
answer = random.randint(min_value, max_value)

# ゲームのパート
guessed_correctly = False
for i in range(5):
    user_answer = input(f"{i + 1}回目の予測をしてください")
    try:
        user_answer = int(user_answer)
    except ValueError:
        print("整数を入力してください。")
        continue
    if user_answer == answer:
        print("おめでとうございます。正解です。これでプログラムを終了します。")
        guessed_correctly = True
        break
    else:
        print("残念。")
if not guessed_correctly:
    print(f"正解は {answer} でした。")


