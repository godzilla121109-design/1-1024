import os
import random
import sys


def clear_screen():
    """画面を綺麗にクリアする関数"""
    os.system("cls" if os.name == "nt" else "clear")


def play_game():
    """1回分のゲーム処理"""
    clear_screen()
    print("=" * 50)
    print("1/1024 を当てろ！！")
    print("=" * 50)
    print("毎回『1』か『2』を選んで入力してください。")
    print("10回連続で正解してみてね！（確率: 1/1024）\n")

    current_stage = 1
    max_stage = 10

    while current_stage <= max_stage:
        print(f"--- [ Stage {current_stage} / {max_stage} ] ---")

        # 毎回ランダムで正解（1 か 2）を決定
        correct_answer = random.choice([1, 2])

        # プレイヤーの入力処理
        try:
            user_input = input(
                "1 または 2 を入力してください (qで終了): "
            ).strip()
        except (KeyboardInterrupt, EOFError):
            return False

        # 終了コマンド
        if user_input.lower() == "q":
            return False

        # 入力チェック（1 か 2 以外が入力された場合）
        if user_input not in ["1", "2"]:
            print(
                "!ERROR! 入力が正しくありません。『1』か『2』を入力してください。\n"
            )
            continue  # 間違えた入力のときはゲームオーバーにせず、もう一度入力を促す

        player_choice = int(user_input)

        # 判定
        if player_choice == correct_answer:
            print(f"正解！ (正解は {correct_answer} でした)\n")
            current_stage += 1
        else:
            print(f"残念... 不正解！ (正解は {correct_answer} でした)")
            print(
                f"\nゲームオーバー！ あなたは【Stage {current_stage}】まで到達しました。"
            )
            break

    # 10回連続正解した場合
    if current_stage > max_stage:
        print("\n" + "🎉" * 20)
        print(" Congratulations!!")
        print("おめでとうございます！ 1/1024 の超強運で見事 10回連続正解 しました！")
        print("🎉" * 20)

    # 再挑戦の確認
    print("\n" + "-" * 50)
    retry = input("もう一度挑戦しますか？ (y/n): ").strip().lower()
    return retry == "y"


def main():
    # プレイヤーが「n」を押すか「q」を入力するまで何度も繰り返す
    while True:
        again = play_game()
        if not again:
            print("\n遊んでくれてありがとうございました！")
            break

    # 勝手に画面が閉じないよう一時停止
    input("\nEnterキーを押すと終了します...")


if __name__ == "__main__":
    main()
