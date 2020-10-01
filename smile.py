import pygame
from pygame.draw import *

yellow = (232, 243, 42)
black = (0, 0, 0)
red = (255, 0, 0)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((137, 143, 137))

circle(screen, yellow, (200, 200), 100)
circle(screen, black, (200, 200), 100, 1)

circle(screen, red, (150, 170), 20)
circle(screen, black, (150, 170), 20, 1)
circle(screen, black, (150, 170), 8)

circle(screen, red, (250, 170), 15)
circle(screen, black, (250, 170), 15, 1)
circle(screen, black, (250, 170), 7)

rect(screen, black, (150, 250, 100, 20))

polygon(screen, black, [(100, 120), (106, 110), (175, 150), (170, 160)])
polygon(screen, black, [(230, 160), (227, 150), (298, 135), (300,145)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()