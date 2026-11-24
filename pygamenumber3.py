import pygame
import sys
import random
pygame.init
GRID_WIDTH = 35
GRID_HEIGHT = 65
CELL_SIZE = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
rect_color = (150, 30, 60,)
rect_demnsions = (35, 65, 30, 30,)
pygame.draw.rect(screen, rect_color, rect_dimensions)
