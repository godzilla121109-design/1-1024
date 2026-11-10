import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Legends of the Lost World")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

# Colors
GREEN = (65, 145, 65)
DARK_GREEN = (35, 100, 45)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 45, 45)
BLUE = (50, 100, 220)
YELLOW = (255, 220, 50)

# Player direction constants
UP, DOWN, LEFT, RIGHT = "up", "down", "left", "right"

# Player
player = pygame.Rect(380, 280, 32, 32)
player_speed = 4
player_hp = 100
player_max_hp = 100

# Player direction
direction = DOWN

# Attack settings
attack_active = False
attack_timer = 0
attack_cooldown = 0
hit_enemies = set()

# Enemies
enemies = []
for i in range(5):
    enemy = {
        "rect": pygame.Rect(
            random.randint(50, 700), random.randint(50, 500), 30, 30
        ),
        "hp": 60,
        "speed": 1.5,
        "attack_cooldown": 0,
    }
    enemies.append(enemy)

# Game loop
running = True
game_over = False

while running:
    dt = clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and attack_cooldown <= 0 and not game_over:
                attack_active = True
                attack_timer = 150
                attack_cooldown = 400
                hit_enemies.clear()
            if event.key == pygame.K_r and game_over:
                player_hp = player_max_hp
                player.x = 380
                player.y = 280
                for enemy in enemies:
                    enemy["hp"] = 60
                game_over = False

    keys = pygame.key.get_pressed()
    if not game_over:
        # Player movement
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.y -= player_speed
            direction = UP
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.y += player_speed
            direction = DOWN
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.x -= player_speed
            direction = LEFT
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.x += player_speed
            direction = RIGHT

        # Keep player inside screen
        player.clamp_ip(screen.get_rect())

        # Attack timer
        if attack_cooldown > 0:
            attack_cooldown -= dt
        if attack_active:
            attack_timer -= dt
            if attack_timer <= 0:
                attack_active = False

        # Create sword attack area
        sword = None
        if attack_active:
            if direction == UP:
                sword = pygame.Rect(player.x - 5, player.y - 28, 42, 28)
            elif direction == DOWN:
                sword = pygame.Rect(player.x - 5, player.y + 32, 42, 28)
            elif direction == LEFT:
                sword = pygame.Rect(player.x - 28, player.y - 5, 28, 42)
            elif direction == RIGHT:
                sword = pygame.Rect(player.x + 32, player.y - 5, 28, 42)

        # Enemy movement and combat
        for enemy in enemies:
            if enemy["hp"] <= 0:
                continue
            monster = enemy["rect"]
            dx = player.centerx - monster.centerx
            dy = player.centery - monster.centery
            distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)

            # Monster follows player
            if distance > 35:
                monster.x += int(dx / distance * enemy["speed"])
                monster.y += int(dy / distance * enemy["speed"])

            # Sword damage
            if sword and sword.colliderect(monster):
                enemy_id = id(enemy)
                if enemy_id not in hit_enemies:
                    enemy["hp"] -= 30
                    hit_enemies.add(enemy_id)

            # Monster attacks player
            if monster.colliderect(player):
                if enemy["attack_cooldown"] <= 0:
                    player_hp -= 10
                    enemy["attack_cooldown"] = 800
            if enemy["attack_cooldown"] > 0:
                enemy["attack_cooldown"] -= dt

        # Check player health
    if player_hp <= 0:
            player_hp = 0
            game_over = True

    # DRAW WORLD
    screen.fill(GREEN)

    # Grass decoration
    for x in range(0, WIDTH, 40):
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, DARK_GREEN, (x, y, 2, 2))

    # Trees
    for x, y in [(80, 80), (700, 100), (100, 480), (700, 480), (300, 80), (550, 500)]:
        pygame.draw.rect(screen, (100, 60, 25), (x + 10, y + 15, 12, 25))
        pygame.draw.rect(screen, (20, 100, 35), (x, y, 32, 25))

    # Draw enemies
    for enemy in enemies:
        if enemy["hp"] <= 0:
            continue
        monster = enemy["rect"]
        # Monster body
        pygame.draw.rect(screen, RED, monster)
        # Monster eyes
        pygame.draw.rect(screen, WHITE, (monster.x + 5, monster.y + 7, 6, 6))
        pygame.draw.rect(screen, WHITE, (monster.x + 19, monster.y + 7, 6, 6))
        # Monster health bar
        pygame.draw.rect(screen, BLACK, (monster.x - 5, monster.y - 12, 40, 6))
        pygame.draw.rect(
            screen, RED, (monster.x - 5, monster.y - 12, max(0, int(40 * enemy["hp"] / 60)), 6)
        )

    # Draw player
    pygame.draw.rect(screen, BLUE, player)
    # Player eyes
    pygame.draw.rect(screen, WHITE, (player.x + 7, player.y + 7, 5, 5))
    pygame.draw.rect(screen, WHITE, (player.x + 20, player.y + 7, 5, 5))

    # Draw sword
    if sword and attack_active:
        pygame.draw.rect(screen, YELLOW, sword)

    # Player health bar
    pygame.draw.rect(screen, BLACK, (20, 20, 204, 24))
    pygame.draw.rect(screen, RED, (22, 22, 200, 20))
    pygame.draw.rect(
        screen, (30, 220, 60), (22, 22, int(200 * player_hp / player_max_hp), 20)
    )

    hp_text = font.render(f"HP: {player_hp}/{player_max_hp}", True, WHITE)
    screen.blit(hp_text, (20, 50))

    # Game title
    title = font.render("LEGENDS OF THE LOST WORLD", True, WHITE)
    screen.blit(title, (250, 20))

    # Controls
    controls = font.render("WASD: Move | SPACE: Attack", True, WHITE)
    screen.blit(controls, (250, 560))

    # Game over screen
    if game_over:
        text = font.render("GAME OVER! Press R to restart", True, WHITE)
        screen.blit(text, (220, 280))

    pygame.display.flip()

pygame.quit()
sys.exit()
