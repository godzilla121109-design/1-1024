import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# 画面とグリッドの設定
GRID_WIDTH = 35
GRID_HEIGHT = 35
CELL_SIZE = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# ウィンドウ（screen）の作成
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("コイン獲得ゲーム")
clock = pygame.time.Clock()

# プレイヤー（白い四角形）の設定
player_color = (255, 255, 255)
player_x = 200
player_y = 200
player_width = 30
player_height = 30
speed = 5

# ドラゴン（赤い四角形）の設定 ※変数名を整理
dragon_color = (255, 0, 0)
dragon_x = 40
dragon_y = 200
dragon_width = 100
dragon_height = 75

# コイン（黄色の四角形）の設定
coin_color = (255, 215, 0)
coin_size = 20
coin_x = random.randint(0, SCREEN_WIDTH - coin_size)
coin_y = random.randint(0, SCREEN_HEIGHT - coin_size)

score = 0

# メインループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力の処理（画面外に出ないよう制限を追加）
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_height:
        player_y += speed

    # 描画用のRect（矩形）オブジェクトを作成
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    dragon_rect = pygame.Rect(dragon_x, dragon_y, dragon_width, dragon_height)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)

    # 当たり判定（コイン獲得）
    if player_rect.colliderect(coin_rect):
        score += 1
        print(f"コイン獲得！ 現在のスコア: {score}")
        # コインを新しいランダムな位置に移動
        coin_x = random.randint(0, SCREEN_WIDTH - coin_size)
        coin_y = random.randint(0, SCREEN_HEIGHT - coin_size)

    # 当たり判定（ドラゴンにぶつかった場合）
    if player_rect.colliderect(dragon_rect):
        print("ドラゴンにぶつかった！ゲームオーバー")
        pygame.quit()
        sys.exit()

    # 背景を黒で塗りつぶす
    screen.fill((0, 0, 0))

    # 各オブジェクトの描画
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, dragon_color, dragon_rect)
    pygame.draw.rect(screen, coin_color, coin_rect)

    # 画面を更新
    pygame.display.flip()
    clock.tick(60)
