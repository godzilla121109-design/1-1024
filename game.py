import os
import random
import sys


def clear_screen():
    """画面を綺麗にクリアする関数"""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear_screen()
    print("=" * 50)
    print(" 🎲 1/1024 の奇跡に挑む！10連続当てゲーム 🎲")
    print("=" * 50)
    print("毎回『1』か『2』を選んで入力してください。")
    print("10回連続で正解できればクリアです！（確率: 1/1024）\n")

    current_stage = 1
    max_stage = 10

    while current_stage <= max_stage:
        print(f"--- [ Stage {current_stage} / {max_stage} ] ---")

        # 毎回ランダムで正解（1 か 2）を決定
        correct_answer = random.choice([1, 2])

        # プレイヤーの入力処理
        try:
            user_input = input("1 または 2 を入力してください (qで終了): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nゲームを終了します。")
            sys.exit(0)

        # 終了コマンド
        if user_input.lower() == "q":
            print("ゲームを途中終了しました。")
            return

        # 入力チェック（1 か 2 以外が入力された場合）
        if user_input not in ["1", "2"]:
            print("⚠️ 入力が正しくありません。『1』か『2』を入力してください。\n")
            continue

        player_choice = int(user_input)

        # 判定
        if player_choice == correct_answer:
            print(f"⭕️ 正解！ (正解は {correct_answer} でした)\n")
            current_stage += 1
        else:
            print(f"❌ 残念... 不正解！ (正解は {correct_answer} でした)")
            print(
                f"\n💥 ゲームオーバー！ あなたは【Stage {current_stage}】まで到達しました。"
            )
            break

    # 10回連続正解した場合
    if current_stage > max_stage:
        print("\n" + "🎉" * 20)
        print(" Congratulations!!")
        print(" 1/1024 の超強運で見事 10回連続正解 しました！")
        print("🎉" * 20)


if __name__ == "__main__":
    main()
