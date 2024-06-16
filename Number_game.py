import random

def get_user_input():
    while True:
        try:
            n = int(input("最小値を入力してください: "))
            m = int(input("最大値を入力してください: "))
            if n > m:
                print("最小値は最大値以下でなければなりません。")
            else:
                return n, m
        except ValueError:
            print("有効な整数を入力してください。")

def guess_the_number(n, m):
    target = random.randint(n, m)
    print(f"{n}から{m}の範囲内で数字を当ててください。")

    while True:
        try:
            guess = int(input("あなたの予想を入力してください: "))
            if guess < n or guess > m:
                print(f"予想は{n}から{m}の範囲内でなければなりません。")
            elif guess < target:
                print("もっと大きな数字です。")
            elif guess > target:
                print("もっと小さな数字です。")
            else:
                print("おめでとうございます！正解です！")
                break
        except ValueError:
            print("有効な整数を入力してください。")

def main():
    print("Main function started")
    n, m = get_user_input()
    guess_the_number(n, m)

main()