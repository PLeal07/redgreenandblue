import pygame
import sys

pygame.init()

screenw = 800
screenh = 500
screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Red, Green and Blue")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()