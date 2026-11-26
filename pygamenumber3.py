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

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("コイン獲得ゲーム")
clock = pygame.time.Clock()

# フォントはループの外で1回だけ作成する
font = pygame.font.Font(None, 36)

# プレイヤー（白い四角形）の設定
player_color = (255, 255, 255)
player_x = 200
player_y = 200
player_width = 30
player_height = 30
speed = 5

# ドラゴン（赤い四角形）の設定
dragon_color = (255, 0, 0)
dragon_x = 40
dragon_y = 200
dragon_width = 100
dragon_height = 75
dragon_speed = 3

# 炎（火の玉）の設定
fire_color = (255, 100, 0)
fire_width = 25
fire_height = 15
fire_speed = 7
fires = []
fire_timer = 0

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

    # プレイヤーのキー入力処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_height:
        player_y += speed

    # ドラゴンの移動処理（上下に往復）
    dragon_y += dragon_speed
    if dragon_y <= 0 or dragon_y >= SCREEN_HEIGHT - dragon_height:
        dragon_speed = -dragon_speed

    # 2秒おきに炎を発射する処理（60FPS × 2秒 = 120フレーム）
    fire_timer += 1
    if fire_timer >= 120:
        start_x = dragon_x + dragon_width
        start_y = dragon_y + (dragon_height // 2) - (fire_height // 2)
        fires.append(pygame.Rect(start_x, start_y, fire_width, fire_height))
        fire_timer = 0

    # 描画用のRectオブジェクトを作成
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    dragon_rect = pygame.Rect(dragon_x, dragon_y, dragon_width, dragon_height)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)

    # 炎の移動と当たり判定
    for fire in fires[:]:
        fire.x += fire_speed
        if player_rect.colliderect(fire):
            print("炎に当たった！ゲームオーバー")
            pygame.quit()
            sys.exit()
        if fire.x > SCREEN_WIDTH:
            fires.remove(fire)

    # 当たり判定（コイン獲得）
    if player_rect.colliderect(coin_rect):
        score += 1
        print(f"コイン獲得！ 現在のスコア: {score}")
        coin_x = random.randint(0, SCREEN_WIDTH - coin_size)
        coin_y = random.randint(0, SCREEN_HEIGHT - coin_size)

    # 当たり判定（ドラゴン本体にぶつかった場合）
    if player_rect.colliderect(dragon_rect):
        print("ドラゴンにぶつかった！ゲームオーバー")
        pygame.quit()
        sys.exit()

    # --- ここから描画処理 ---
    # 背景を黒で塗りつぶす
    screen.fill((0, 0, 0))

    # 各オブジェクトの描画
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, dragon_color, dragon_rect)
    pygame.draw.rect(screen, coin_color, coin_rect)

    for fire in fires:
        pygame.draw.rect(screen, fire_color, fire)

    # 背景を塗ったあとにスコアを描画する
    text_surface = font.render(f"Your score is: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    # 画面を更新
    pygame.display.flip()
    clock.tick(60)
