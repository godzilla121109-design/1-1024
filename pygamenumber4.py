import pygame
import sys
import random

# 初期化
pygame.init()

# 迷路サイズ（奇数推奨）
GRID_WIDTH = 21
GRID_HEIGHT = 21
CELL_SIZE = 32

SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("毎回迷路が変わるパックマン風ゲーム ([R]で新迷路)")
clock = pygame.time.Clock()

# セルの種類: 1=壁, 0=空き通路, 2=ドット
WALL = 1
EMPTY = 0
DOT = 2


def generate_pacman_maze(w, h, loop_chance=0.18):
    """穴掘り法 + ループ化でパックマン向けの迷路を生成"""
    maze = [[WALL] * w for _ in range(h)]

    # 穴掘り法で基本の通路を作成
    start_x, start_y = 1, 1
    maze[start_y][start_x] = EMPTY
    stack = [(start_x, start_y)]
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

    while stack:
        cx, cy = stack[-1]
        dirs = directions[:]
        random.shuffle(dirs)
        carved = False

        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 < nx < w - 1 and 0 < ny < h - 1:
                if maze[ny][nx] == WALL:
                    maze[cy + dy // 2][cx + dx // 2] = EMPTY
                    maze[ny][nx] = EMPTY
                    stack.append((nx, ny))
                    carved = True
                    break

        if not carved:
            stack.pop()

    # 外周以外の壁を一部壊してループ（逃げ道）を作る
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if maze[y][x] == WALL and random.random() < loop_chance:
                # 上下または左右が通路なら壊して通り抜けやすくする
                vert_open = (maze[y - 1][x] != WALL and maze[y + 1][x] != WALL)
                horiz_open = (maze[y][x - 1] != WALL and maze[y][x + 1] != WALL)
                if vert_open or horiz_open:
                    maze[y][x] = EMPTY

    # スタート付近とゴースト初期位置付近は確実に通路にする
    safe_cells = [(1, 1), (1, 2), (2, 1), (w - 2, h - 2), (w - 3, h - 2), (w - 2, h - 3)]
    for sx, sy in safe_cells:
        maze[sy][sx] = EMPTY

    # 通路にドットを配置（スタート地点は空のまま）
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if maze[y][x] == EMPTY and (x, y) != (1, 1):
                maze[y][x] = DOT

    return maze


def get_valid_neighbors(maze, gx, gy):
    """現在地から1マス進める隣接座標のリストを返す"""
    candidates = [(gx + 1, gy), (gx - 1, gy), (gx, gy + 1), (gx, gy - 1)]
    return [(nx, ny) for nx, ny in candidates if maze[ny][nx] != WALL]


def reset_stage():
    maze = generate_pacman_maze(GRID_WIDTH, GRID_HEIGHT)
    px, py = 1, 1
    # ゴースト初期位置（右下付近）と直前座標（Uターン抑制用）
    ghosts = [
        {"x": GRID_WIDTH - 2, "y": GRID_HEIGHT - 2, "prev": None, "color": (255, 80, 80)},
        {"x": GRID_WIDTH - 2, "y": 1, "prev": None, "color": (255, 140, 200)},
    ]
    return maze, px, py, ghosts, False, False


maze, player_x, player_y, ghosts, game_over, stage_clear = reset_stage()
move_timer = 0
ghost_timer = 0

while True:
    dt = clock.tick(60)
    move_timer += dt
    ghost_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                maze, player_x, player_y, ghosts, game_over, stage_clear = reset_stage()

            if event.key == pygame.K_RETURN and (game_over or stage_clear):
                maze, player_x, player_y, ghosts, game_over, stage_clear = reset_stage()

    # プレイヤー移動（約110msごとに1マス移動して操作しやすくする）
    if not game_over and not stage_clear and move_timer >= 110:
        keys = pygame.key.get_pressed()
        nx, ny = player_x, player_y
        if keys[pygame.K_LEFT]:
            nx -= 1
        elif keys[pygame.K_RIGHT]:
            nx += 1
        elif keys[pygame.K_UP]:
            ny -= 1
        elif keys[pygame.K_DOWN]:
            ny += 1

        if (nx, ny) != (player_x, player_y) and maze[ny][nx] != WALL:
            player_x, player_y = nx, ny
            move_timer = 0

            # ドット回収
            if maze[player_y][player_x] == DOT:
                maze[player_y][player_x] = EMPTY

            # 残りドット確認
            remaining_dots = sum(cell == DOT for row in maze for cell in row)
            if remaining_dots == 0:
                stage_clear = True

    # ゴースト移動（約220msごとに1マス移動）
    if not game_over and not stage_clear and ghost_timer >= 220:
        ghost_timer = 0
        for g in ghosts:
            neighbors = get_valid_neighbors(maze, g["x"], g["y"])
            # できるだけ直前のマスに戻らないようにする
            non_backtrack = [pos for pos in neighbors if pos != g["prev"]]
            choices = non_backtrack if non_backtrack else neighbors
            if choices:
                next_pos = random.choice(choices)
                g["prev"] = (g["x"], g["y"])
                g["x"], g["y"] = next_pos

    # プレイヤーとゴーストの接触判定
    if not game_over and not stage_clear:
        for g in ghosts:
            if (g["x"], g["y"]) == (player_x, player_y):
                game_over = True
                break

    # 描画
    screen.fill((15, 15, 30))

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell = maze[y][x]
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell == WALL:
                pygame.draw.rect(screen, (30, 50, 160), rect.inflate(-2, -2), border_radius=4)
            elif cell == DOT:
                center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2)
                pygame.draw.circle(screen, (255, 230, 150), center, 4)

    # パックマン（黄色い円）
    p_center = (player_x * CELL_SIZE + CELL_SIZE // 2, player_y * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(screen, (255, 220, 0), p_center, CELL_SIZE // 2 - 4)

    # ゴースト
    for g in ghosts:
        g_center = (g["x"] * CELL_SIZE + CELL_SIZE // 2, g["y"] * CELL_SIZE + CELL_SIZE // 2)
        pygame.draw.circle(screen, g["color"], g_center, CELL_SIZE // 2 - 4)

    # 状態メッセージ（コンソール＆タイトル表示）
    if game_over:
        pygame.display.set_caption("GAME OVER! [Enter]または[R]で新しい迷路に挑戦")
    elif stage_clear:
        pygame.display.set_caption("STAGE CLEAR! [Enter]または[R]で次の迷路へ")
    else:
        dots_left = sum(cell == DOT for row in maze for cell in row)
        pygame.display.set_caption(f"残りドット: {dots_left} | [R]で新迷路生成")

    pygame.display.flip()
