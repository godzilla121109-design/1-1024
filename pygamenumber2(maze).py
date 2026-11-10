import pygame
import sys

# 1. 初期化
pygame.init()

# 画面サイズ (16マス × 16マス、1マス40px = 640x640)
CELL_SIZE = 40
GRID_SIZE = 16
SCREEN_WIDTH = CELL_SIZE * GRID_SIZE
SCREEN_HEIGHT = CELL_SIZE * GRID_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("シンプル迷路ゲーム")

clock = pygame.time.Clock()

# 2. マップデータ (1: 壁, 0: 通路, 2: ゴール)
maze_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,2,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# プレイヤーの初期座標（グリッドのマス目単位）
player_x = 1
player_y = 1

# 3. メインループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # キーが押された瞬間だけ判定
        if event.type == pygame.KEYDOWN:
            next_x, next_y = player_x, player_y
            
            if event.key == pygame.K_LEFT:
                next_x -= 1
            elif event.key == pygame.K_RIGHT:
                next_x += 1
            elif event.key == pygame.K_UP:
                next_y -= 1
            elif event.key == pygame.K_DOWN:
                next_y += 1

            # 移動先が「壁（1）」でなければ移動を許可
            if maze_map[next_y][next_x] != 1:
                player_x = next_x
                player_y = next_y

                # ゴール（2）にたどり着いたか判定
                if maze_map[player_y][player_x] == 2:
                    print("おめでとうございます！ゴールです！")

    # 画面を白で塗りつぶす
    screen.fill((255, 255, 255))

    # 4. マップ（壁とゴール）の描画
    for row_idx, row in enumerate(maze_map):
        for col_idx, cell in enumerate(row):
            rect = pygame.Rect(col_idx * CELL_SIZE, row_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell == 1:  # 壁
                pygame.draw.rect(screen, (40, 40, 40), rect)
            elif cell == 2:  # ゴール
                pygame.draw.rect(screen, (0, 200, 0), rect)

    # 5. プレイヤー（赤い四角形）の描画
    player_rect = pygame.Rect(
        player_x * CELL_SIZE + 5, 
        player_y * CELL_SIZE + 5, 
        CELL_SIZE - 10, 
        CELL_SIZE - 10
    )
    pygame.draw.rect(screen, (255, 0, 0), player_rect)

    # 画面更新
    pygame.display.flip()
    clock.tick(60)
