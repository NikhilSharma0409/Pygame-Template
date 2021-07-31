import pygame
import sys

pygame.init()


SCREENWIDTH = 1200
SCREENHEIGHT = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("TITLE")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(60)
