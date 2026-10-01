import random
import os

SAVE_FILE = "save_data.txt"

# ==================== 敵クラス ====================
class Enemy:
    def __init__(self, name, base_hp, attack, base_reward, money_bonus_step):
        # 所持金10万円ごとに HP+10, 報酬+100（下限はベース値）
        bonus_hp = money_bonus_step * 10
        bonus_reward = money_bonus_step * 100

        self.name = name
        self.max_hp = max(10, base_hp + bonus_hp)
        self.hp = self.max_hp
        self.attack = attack
        self.reward = max(100, base_reward + bonus_reward)

# 通常の敵データ（名前, 基本HP, 通常攻撃力, 基本報酬）
NORMAL_ENEMY_DATA = [
    ("Goblin", 30, 18, 500),
    ("Skelton", 50, 22, 1200),
    ("Golem", 100, 30, 3000)
]

# ボスデータ（攻撃力を 200 に設定）
BOSS_ENEMY_DATA = [
    ("Dragon", 300, 200, 10000)  # ★攻撃力 200
]

# ==================== 武器データ ====================
WEAPON_SHOP = [
    {"name": "初期の剣", "price": 0, "atk": 30, "mult": 1},
    {"name": "倍加の剣", "price": 10000, "atk": 60, "mult": 2},
    {"name": "三倍の剣", "price": 200000, "atk": 90, "mult": 3},
    {"name": "五倍の剣", "price": 1000000, "atk": 150, "mult": 5},
    {"name": "七倍の剣", "price": 5000000, "atk": 230, "mult": 7},
]

# ==================== プレイヤークラス ====================
class Player:
    def __init__(self):
        self.money = 0
        self.target_money = 99999999
        self.current_hp = 100
        self.weapon_index = 0

    @property
    def current_weapon(self):
        return WEAPON_SHOP[self.weapon_index]

    # 所持金に応じて最大HPを計算（上限2,000）
    def get_max_hp(self):
        bonus_hp = (self.money // 500) * 10
        calculated_hp = 100 + bonus_hp
        return min(2000, calculated_hp)

    def get_money_bonus_step(self):
        return self.money // 100000

    def save_game(self):
        try:
            with open(SAVE_FILE, "w", encoding="utf-8") as f:
                f.write(f"{self.money},{self.weapon_index}")
            print(f"\n💾 セーブしました！（所持金: {self.money:,}円 / 装備: {self.current_weapon['name']}）")
        except Exception as e:
            print(f"⚠️ セーブ失敗: {e}")

    def load_game(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r", encoding="utf-8") as f:
                    data = f.read().strip().split(",")
                    self.money = int(data[0])
                    if len(data) > 1:
                        self.weapon_index = int(data[1])
                    print(f"📂 ロードしました！（所持金: {self.money:,}円 / 装備: {self.current_weapon['name']}）")
            except Exception as e:
                print(f"⚠️️ ロード失敗のため初期化します: {e}")
        else:
            print("🆕 はじめからスタートします！")

# ==================== 商店（ショップ） ====================
def shop(player):
    while True:
        print("\n" + "=" * 50)
        print(f" 🛒 武器屋 【所持金: {player.money:,} 円】")
        print(f" 現在の装備: {player.current_weapon['name']} (攻撃力:{player.current_weapon['atk']} / 報酬:{player.current_weapon['mult']}倍)")
        print("=" * 50)
        
        for i, w in enumerate(WEAPON_SHOP):
            status = ""
            if i <= player.weapon_index:
                status = "【購入済み】"
            print(f"{i + 1}: {w['name']} - {w['price']:,}円 (攻撃力:{w['atk']} / 報酬:{w['mult']}倍) {status}")
        
        print("0: 商店を出る")
        cmd = input("購入する剣を選択してください: ").strip()

        if cmd == "0":
            break
        
        if cmd.isdigit():
            idx = int(cmd) - 1
            if 0 <= idx < len(WEAPON_SHOP):
                target_weapon = WEAPON_SHOP[idx]
                if idx <= player.weapon_index:
                    print("＞ すでに持っているか、それ以上の剣を所持しています！")
                elif player.money < target_weapon["price"]:
                    print("＞ 所持金が足りません！")
                else:
                    player.money -= target_weapon["price"]
                    player.weapon_index = idx
                    print(f"✨ {target_weapon['name']} を購入して装備しました！")
                    player.save_game()
            else:
                print("＞ 無効な番号です。")
        else:
            print("＞ 数字を入力してください。")

# ==================== バトル処理 ====================
def start_battle(player):
    max_hp = player.get_max_hp()
    player.current_hp = max_hp

    step = player.get_money_bonus_step()
    
    # ★ 所持金が10万円（100,000円）以上の場合はドラゴンが出現対象に加わる
    if player.money >= 100000:
        available_enemies = NORMAL_ENEMY_DATA + BOSS_ENEMY_DATA
    else:
        available_enemies = NORMAL_ENEMY_DATA

    base_name, base_hp, atk, base_reward = random.choice(available_enemies)
    enemy = Enemy(base_name, base_hp, atk, base_reward, step)
    
    weapon = player.current_weapon

    print("\n" + "=" * 50)
    if enemy.name == "Dragon":
        print(f" 🐉 警告！ 超強力ボス 【Dragon】 が姿を現した！（通常攻撃力: 200）")
    else:
        print(f" あらわれる！ {enemy.name}")
    print(f" HP: {enemy.hp} / 通常攻撃力: {enemy.attack}")
    print(f" 基本報酬: {enemy.reward:,} 円  [所持金補正: HP+{step*10} / 報酬+{step*100}]")
    print(f" 装備中: {weapon['name']}（攻撃力: {weapon['atk']} / 報酬倍率: {weapon['mult']}倍）")
    print("=" * 50)

    turn = 1
    while True:
        print(f"\n--- ターン {turn} ---")
        print(f"【プレイヤー】HP: {player.current_hp}/{max_hp}")
        print(f"【 {enemy.name} 】HP: {enemy.hp}/{enemy.max_hp}")
        print("-" * 30)
        print(f"1: {weapon['name']}で攻撃（{weapon['atk']}ダメージ）")
        print("2: たてでふせぐ")
        
        choice = input("行動を選択してください (1 or 2): ").strip()
        enemy_action = random.choice(["attack", "roar"])
        
        print("\n【戦闘結果】")
        
        if choice == "1":
            if enemy_action == "attack":
                print(f"＞ 剣を振るったが、{enemy.name} の通常攻撃に押し込まれた！")
                print(f"＞ プレイヤーは {enemy.attack} のダメージを受けた！")
                player.current_hp -= enemy.attack
            else:
                print(f"＞ {enemy.name} は吠えたてている！ その隙を突いて攻撃！")
                print(f"＞ {enemy.name} に {weapon['atk']} のダメージを与えた！")
                enemy.hp -= weapon["atk"]

        elif choice == "2":
            if enemy_action == "attack":
                print(f"＞ {enemy.name} の通常攻撃！ 盾で完全に防ぎきった！")
            else:
                print(f"＞ {enemy.name} が激しく吠えたてた！ 10 のダメージを受けた！")
                player.current_hp -= 10
        else:
            print("＞ まごまごしているうちに攻撃を受けた！")
            if enemy_action == "attack":
                player.current_hp -= enemy.attack
            else:
                player.current_hp -= 10

        # --- 判定処理 ---
        if enemy.hp <= 0:
            final_reward = enemy.reward * weapon["mult"]
            print(f"\n✨ {enemy.name} をたおした！")
            print(f"💰 報酬: {enemy.reward:,}円 × 武器倍率({weapon['mult']}倍) = {final_reward:,} 円 を手に入れた！")
            player.money += final_reward
            player.save_game()
            break

        if player.current_hp <= 0:
            print(f"\n☠️️ プレイヤーの体力が 0 になった…（敗北）")
            loss_amount = min(player.money, enemy.reward * weapon["mult"])
            player.money -= loss_amount
            print(f" 罰金として {loss_amount:,} 円を失った…")
            player.save_game()
            break

        turn += 1

# ==================== メイン処理 ====================
def main():
    player = Player()
    print("★ ゲームスタート！ ★")
    player.load_game()

    while True:
        max_hp = player.get_max_hp()
        step = player.get_money_bonus_step()
        print(f"\n【現在のステータス】")
        print(f"・所持金: {player.money:,} 円")
        print(f"・最大HP: {max_hp} / 2,000(上限)")
        print(f"・装備中の剣: {player.current_weapon['name']} (攻撃力:{player.current_weapon['atk']} / 報酬:{player.current_weapon['mult']}倍)")
        print(f"・敵の補正段階: {step}段階 (所持金10万円ごとに敵HP+10 / 報酬+100)")
        if player.money >= 100000:
            print("・ドラゴン出現フラグ: 🐉【解放済み】")
        else:
            print("・ドラゴン出現フラグ: 🔒 (所持金10万円以上で開放)")
        print("-" * 30)
        print("1: 冒険に出かける（バトル）")
        print("2: 商店（武器屋）に行く")
        print("3: セーブしてゲームをやめる")
        
        cmd = input("選択してください (1~3): ").strip()
        if cmd == "1":
            start_battle(player)
        elif cmd == "2":
            shop(player)
        elif cmd == "3":
            player.save_game()
            print("ゲームを終了します。また遊んでね！")
            break
        else:
            print("1〜3の数字を入力してください。")

if __name__ == "__main__":
    main()
