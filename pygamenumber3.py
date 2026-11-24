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

# 四角形の色・サイズ・位置・速度の定義
rect_color = (255, 255, 255)
x = 200
y = 200
width = 30
height = 30
speed = 5

rect_color = (255, 0, 0)
drangonx = 40
dragony = 200
dragonwidth = 100
dragonheight = 75

# メインループ
while True:
    # イベント処理（ウィンドウの×ボタンで終了できるようにする）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # 背景を黒で塗りつぶす
    screen.fill((0, 0, 0))

    # 更新された座標 (x, y) を使って四角形を描画する
    rect_dimensions = (x, y, width, height)
    pygame.draw.rect(screen, rect_color, rect_dimensions)

    # 画面を更新して描画を反映する
    pygame.display.flip()

    # フレームレートを60FPSに固定（これがないと移動が速すぎます）
    clock.tick(60)
