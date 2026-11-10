import pygame
import sys
import random

# 初期化
pygame.init()

# 迷路のサイズ（※迷路のアルゴリズム上、幅・高さともに「奇数」にしてください）
GRID_WIDTH = 21
GRID_HEIGHT = 21
CELL_SIZE = 35

SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("自動生成迷路ゲーム ([R]キーで再生成)")

clock = pygame.time.Clock()

def generate_maze(w, h):
    """ 穴掘り法による迷路の自動生成 """
    # すべてを壁(1)で初期化
    maze = [[1] * w for _ in range(h)]
    
    # 開始地点（奇数座標）
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0
    stack = [(start_x, start_y)]
    
    # 上下左右に2マスずつ進むベクトル
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    
    while stack:
        cx, cy = stack[-1]
        # 方向をランダムにシャッフル
        random.shuffle(directions)
        
        carved = False
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # マップの内側かつ、まだ壁(1)の場合
            if 0 < nx < w - 1 and 0 < ny < h - 1:
                if maze[ny][nx] == 1:
                    # 間の壁と、進んだ先を通路(0)にする
                    maze[cy + dy // 2][cx + dx // 2] = 0
                    maze[ny][nx] = 0
                    stack.append((nx, ny))
                    carved = True
                    break
        
        if not carved:
            stack.pop() # 行き止まりになったら戻る
            
    # ゴール(2)を右下付近の通路に配置
    maze[h - 2][w - 2] = 2
    return maze

# 初回迷路の作成とプレイヤー初期化
maze_map = generate_maze(GRID_WIDTH, GRID_HEIGHT)
player_x, player_y = 1, 1
clear_flag = False

# メインループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # [R]キーで新しい迷路を再生成
            if event.key == pygame.K_r:
                maze_map = generate_maze(GRID_WIDTH, GRID_HEIGHT)
                player_x, player_y = 1, 1
                clear_flag = False
                print("新しい迷路を生成しました！")

            # クリアしていなければ移動受付
            if not clear_flag:
                next_x, next_y = player_x, player_y
                
                if event.key == pygame.K_LEFT:
                    next_x -= 1
                elif event.key == pygame.K_RIGHT:
                    next_x += 1
                elif event.key == pygame.K_UP:
                    next_y -= 1
                elif event.key == pygame.K_DOWN:
                    next_y += 1

                # 壁（1）でなければ移動
                if maze_map[next_y][next_x] != 1:
                    player_x = next_x
                    player_y = next_y

                    # ゴール（2）に到着したか判定
                    if maze_map[player_y][player_x] == 2:
                        clear_flag = True
                        print("CLEAR!! おめでとうございます！([R]キーで次の迷路へ)")

    # 画面を白でクリア
    screen.fill((255, 255, 255))

    # マップ（壁・通路・ゴール）の描画
    for row_idx, row in enumerate(maze_map):
        for col_idx, cell in enumerate(row):
            rect = pygame.Rect(col_idx * CELL_SIZE, row_idx * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell == 1:  # 壁
                pygame.draw.rect(screen, (50, 50, 50), rect)
            elif cell == 2:  # ゴール
                pygame.draw.rect(screen, (0, 200, 0), rect)

    # プレイヤーの描画（クリア時は色が変わる）
    player_rect = pygame.Rect(
        player_x * CELL_SIZE + 6, 
        player_y * CELL_SIZE + 6, 
        CELL_SIZE - 12, 
        CELL_SIZE - 12
    )
    if clear_flag:
        pygame.draw.rect(screen, (255, 215, 0), player_rect)  # クリア時は金色
    else:
        pygame.draw.rect(screen, (255, 0, 0), player_rect)  # 通常時は赤

    pygame.display.flip()
    clock.tick(60)
