import pygame
import sys

# 1. Pygameの初期化
pygame.init()

# 2. 画面サイズの設定 (幅, 高さ)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ウィンドウのタイトルを設定
pygame.display.set_caption("My Pygame App")

# 3. フレームレート（FPS）を管理するためのクロックオブジェクト
clock = pygame.time.Clock()

# キャラクターの初期座標
x = 400
y = 300

# 4. メインループ
while True:
    # イベント処理 (キー入力やウィンドウの×ボタンなど)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キーボード入力の検知と座標の移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    # 画面の背景色を塗りつぶす (RGB: 白)
    screen.fill((255, 255, 255))

    # 赤い四角形を描く
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))

    # 青い円を描く
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 30)

    # 画面中央に動かせる四角形を描く（移動確認用）
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 40, 40))

    # 画面を更新
    pygame.display.flip()

    # 60FPSに固定
    clock.tick(60)
