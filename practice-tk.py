import pygame
import sys
from pygame import Rect
X = 1000
Y = 800
SURFACE = pygame.display.set_mode((X, Y))

player = (X/2, Y-100)
playercolor = (0, 0, 255) # blue

obstacle = Rect(X/2+50, 0, 60, 500)
obstaclecolor = (255, 0, 0) # red

plain = Rect(0, Y-30, X, 30)
plaincolor = (0, 255, 0) # green

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill((0, 0, 0))
    pygame.draw.circle(SURFACE, playercolor, player, 30)
    pygame.draw.rect(SURFACE, obstaclecolor, obstacle)
    pygame.draw.rect(SURFACE, plaincolor, plain)
    pygame.display.update()