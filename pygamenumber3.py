import pygame
import sys
import random

# Pygameの初期化（括弧が必要）
pygame.init()

# 画面とグリッドの設定
GRID_WIDTH = 35
GRID_HEIGHT = 35
CELL_SIZE = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# ウィンドウ（screen）の作成
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Rect Example")

# 四角形の色とサイズ・位置の定義（スペルを統一）
rect_color = (255, 255, 255)
rect_dimensions = (35, 65, 30, 30)  # (X座標, Y座標, 幅, 高さ)

# メインループ
while True:
    # イベント処理（ウィンドウの×ボタンで終了できるようにする）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 背景を黒で塗りつぶす
    screen.fill((0, 0, 0))

    # 四角形を描画する
    pygame.draw.rect(screen, rect_color, rect_dimensions)

    # 画面を更新して描画を反映する
    pygame.display.flip()

