import math
import random
import pygame

pygame.init()

# WINDOW
WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MY RPG ADVENTURE")
clock = pygame.time.Clock()

font = pygame.font.SysFont("consolas", 24)
big_font = pygame.font.SysFont("consolas", 45)

# COLORS
BLACK = (15, 15, 20)
WHITE = (255, 255, 255)
GREEN = (50, 220, 90)
RED = (230, 50, 50)
BLUE = (60, 130, 255)
YELLOW = (255, 220, 50)
PURPLE = (170, 80, 255)
GRAY = (70, 70, 80)

# PLAYER
player = pygame.Rect(430, 280, 35, 35)
player_speed = 5
hp = 100
max_hp = 100
level = 1
xp = 0
xp_needed = 50
damage = 25
weapon = "Sword"

# GAME OBJECTS
enemies = []
bullets = []
enemy_spawn_timer = 0
sword_cooldown = 0
gun_cooldown = 0
invincible_timer = 0
game_over = False


# CREATE ENEMY
def spawn_enemy():
  side = random.choice(["top", "bottom", "left", "right"])
  if side == "top":
    x, y = random.randint(0, WIDTH), -30
  elif side == "bottom":
    x, y = random.randint(0, WIDTH), HEIGHT + 30
  elif side == "left":
    x, y = -30, random.randint(0, HEIGHT)
  else:
    x, y = WIDTH + 30, random.randint(0, HEIGHT)
  enemies.append({
      "rect": pygame.Rect(x, y, 32, 32),
      "hp": 50 + level * 10,
      "speed": min(1.5 + level * 0.15, 4),
  })


# DRAW TEXT
def draw_text(text, x, y, color=WHITE):
  image = font.render(str(text), True, color)
  screen.blit(image, (x, y))


# MAIN GAME
running = True
while running:
  dt = clock.tick(60)
  screen.fill(BLACK)

  # EVENTS
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if not game_over and event.type == pygame.KEYDOWN:
      # SWORD ATTACK
      if event.key == pygame.K_SPACE and sword_cooldown <= 0:
        for enemy in enemies[:]:
          distance = math.hypot(
              enemy["rect"].centerx - player.centerx,
              enemy["rect"].centery - player.centery,
          )
          if distance < 75:
            enemy["hp"] -= damage
        sword_cooldown = 350

      # GUN ATTACK
      if event.key == pygame.K_f and gun_cooldown <= 0:
        if level >= 2:
          closest = None
          closest_distance = 1000
          for enemy in enemies:
            distance = math.hypot(
                enemy["rect"].centerx - player.centerx,
                enemy["rect"].centery - player.centery,
            )
            if distance < closest_distance:
              closest_distance = distance
              closest = enemy
          if closest:
            dx = closest["rect"].centerx - player.centerx
            dy = closest["rect"].centery - player.centery
            length = math.hypot(dx, dy)
            if length > 0:
              bullets.append({
                  "x": float(player.centerx),
                  "y": float(player.centery),
                  "dx": dx / length * 9,
                  "dy": dy / length * 9,
              })
          gun_cooldown = 400

  if not game_over:
    keys = pygame.key.get_pressed()
    # MOVEMENT
    if keys[pygame.K_w]:
      player.y -= player_speed
    if keys[pygame.K_s]:
      player.y += player_speed
    if keys[pygame.K_a]:
      player.x -= player_speed
    if keys[pygame.K_d]:
      player.x += player_speed
    player.clamp_ip(screen.get_rect())

    # TIMERS
    enemy_spawn_timer += dt
    sword_cooldown -= dt
    gun_cooldown -= dt
    invincible_timer -= dt

    # SPAWN ENEMIES
    if enemy_spawn_timer >= max(500, 1800 - level * 100):
      spawn_enemy()
      enemy_spawn_timer = 0

    # MOVE ENEMIES
    for enemy in enemies[:]:
      rect = enemy["rect"]
      dx = player.centerx - rect.centerx
      dy = player.centery - rect.centery
      distance = math.hypot(dx, dy)
      if distance > 0:
        rect.x += dx / distance * enemy["speed"]
        rect.y += dy / distance * enemy["speed"]

      # ENEMY ATTACK
      if rect.colliderect(player) and invincible_timer <= 0:
        hp -= 10
        invincible_timer = 700

      # ENEMY DEFEATED
      if enemy["hp"] <= 0:
        enemies.remove(enemy)
        xp += 20

    # BULLETS
    for bullet in bullets[:]:
      bullet["x"] += bullet["dx"]
      bullet["y"] += bullet["dy"]
      bullet_rect = pygame.Rect(
          int(bullet["x"]) - 5, int(bullet["y"]) - 5, 10, 10
      )
      pygame.draw.circle(
          screen, YELLOW, (int(bullet["x"]), int(bullet["y"])), 5
      )

      if not screen.get_rect().colliderect(bullet_rect):
        bullets.remove(bullet)
        continue

      hit = False
      for enemy in enemies[:]:
        if bullet_rect.colliderect(enemy["rect"]):
          enemy["hp"] -= 35
          hit = True
          if enemy["hp"] <= 0:
            enemies.remove(enemy)
            xp += 20
          break

      if hit and bullet in bullets:
        bullets.remove(bullet)

    # LEVEL UP
    while xp >= xp_needed:
      xp -= xp_needed
      level += 1
      max_hp += 20
      hp = max_hp
      damage += 10
      xp_needed += 30
      if level >= 2:
        weapon = "Sword + Gun"

    if hp <= 0:
      hp = 0
      game_over = True

    # DRAW PLAYER
    if invincible_timer <= 0 or invincible_timer // 100 % 2 == 0:
      pygame.draw.rect(screen, BLUE, player)

    # DRAW ENEMIES
    for enemy in enemies:
      rect = enemy["rect"]
      pygame.draw.rect(screen, RED, rect)

      # ENEMY HEALTH BAR
      max_enemy_hp = 50 + level * 10
      pygame.draw.rect(screen, GRAY, (rect.x, rect.y - 10, 32, 5))
      pygame.draw.rect(
          screen,
          GREEN,
          (rect.x, rect.y - 10, max(0, 32 * enemy["hp"] / max_enemy_hp), 5),
      )

    # HUD
    pygame.draw.rect(screen, GRAY, (20, 20, 200, 20))
    pygame.draw.rect(screen, GREEN, (20, 20, 200 * hp / max_hp, 20))
    draw_text(f"HP: {hp}/{max_hp}", 20, 45)
    draw_text(f"LEVEL: {level}", 20, 85, YELLOW)
    draw_text(f"XP: {xp}/{xp_needed}", 20, 120, PURPLE)
    draw_text(f"DAMAGE: {damage}", 20, 155)
    draw_text(f"WEAPON: {weapon}", 20, 190, YELLOW)

    draw_text("WASD: MOVE", 650, 20)
    draw_text("SPACE: SWORD", 650, 50)
    draw_text("F: GUN (LEVEL 2)", 650, 80)

  else:
    # GAME OVER
    title = big_font.render("GAME OVER", True, RED)
    screen.blit(title, (320, 220))
    draw_text(f"FINAL LEVEL: {level}", 350, 290, YELLOW)
    draw_text(f"TOTAL XP: {xp}", 350, 330)
    draw_text("Close the window to exit", 290, 400)

  pygame.display.flip()

pygame.quit()
