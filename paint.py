import pygame
from pygame.draw import *

white = (255, 255, 255)
yellow = (232, 243, 42)
black = (0, 0, 0, 50)
red = (255, 0, 0)
blue = (0, 225, 255)
grey1 = (93, 86, 86, 50)
grey2 = (121, 116, 116, 50)
grey3 = (147, 133, 133, 50)
grey4 = (155, 150, 150, 50)
grey5 = (55, 54, 54, 50)
grey6 = (105, 105, 105, 50)
grey7 = (119, 123, 119, 50)


def draw_car(x0, y0, width, height, zerkal = False):
    if zerkal:
        exhaust_pipe = (x0 + width * 0.85, y0 + height * 0.7, width * 0.15, height * 0.07)
        body = (x0, y0 + height * 0.4, width * 0.9, height * 0.4)
        roof = (x0 + width * 0.15, y0, width * 0.6, height * 0.4)
        wheel1 = (x0 + width * 0.1, y0 + height * 0.6, width * 0.2, height * 0.4)
        wheel2 = (x0 + width * 0.6, y0 + height * 0.6, width * 0.2, height * 0.4)
        window1 = (x0 + 0.2 * width, y0 + 0.1 * height, width * 0.2, height * 0.3)
        window2 = (x0 + 0.5 * width, y0 + 0.1 * height, width * 0.2, height * 0.3)
    else:
        exhaust_pipe = (x0, y0 + height * 0.7, width * 0.15, height * 0.07)
        body = (x0 + 0.1 * width, y0 + height * 0.4, width * 0.9, height * 0.4)
        roof = (x0 + width * 0.25, y0, width * 0.6, height * 0.4)
        wheel1 = (x0 + width * 0.2, y0 + height * 0.6, width * 0.2, height * 0.4)
        wheel2 = (x0 + width * 0.7, y0 + height * 0.6, width * 0.2, height * 0.4)
        window1 = (x0 + 0.3 * width, y0 + 0.1 * height, width * 0.2, height * 0.3)
        window2 = (x0 + 0.6 * width, y0 + 0.1 * height, width * 0.2, height * 0.3)

    ellipse(screen, black, exhaust_pipe)
    rect(screen, blue, body)
    rect(screen, blue, roof)
    ellipse(screen, black, wheel1)
    ellipse(screen, black, wheel2)
    rect(screen, white, window1)
    rect(screen, white, window2)


def draw_background():
    rect1 = pygame.Surface((50, 750), pygame.SRCALPHA)
    rect1.fill(black)
    screen.blit(rect1, (0, 0))
    rect2 = pygame.Surface((100, 750), pygame.SRCALPHA)
    rect2.fill(grey2)
    screen.blit(rect2, (0, 50))
    rect3 = pygame.Surface((150, 750), pygame.SRCALPHA)
    rect3.fill(black)
    screen.blit(rect3, (200, 10))
    rect4 = pygame.Surface((10, 750), pygame.SRCALPHA)
    rect4.fill(grey4)
    screen.blit(rect4, (230, 0))
    rect5 = pygame.Surface((50, 750), pygame.SRCALPHA)
    rect5.fill(grey5)
    screen.blit(rect5, (150, 300))
    rect6 = pygame.Surface((100, 750), pygame.SRCALPHA)
    rect6.fill(grey6)
    screen.blit(rect6, (350, 100))
    rect7 = pygame.Surface((200, 750), pygame.SRCALPHA)
    rect7.fill(grey7)
    screen.blit(rect7, (300, 100))
    rect8 = pygame.Surface((300, 750), pygame.SRCALPHA)
    rect8.fill(black)
    screen.blit(rect8, (450, 200))
    rect9 = pygame.Surface((100, 750), pygame.SRCALPHA)
    rect9.fill(grey4)
    screen.blit(rect9, (480, 50))
    rect10 = pygame.Surface((300, 750), pygame.SRCALPHA)
    rect10.fill(black)
    screen.blit(rect10, (100, 150))
    rect(screen, (110, 134, 132), (0, 400, 700, 700))


def draw_foreground():
    grey_fore_1 = (184, 197, 201)
    green1 = (148, 174, 169)
    green2 = (184, 201, 197)
    green3 = (111, 146, 139)
    whitef = (218, 227, 220)
    green4 = (167, 185, 185)
    greyf = (148, 169, 174)

    rect(screen, grey_fore_1, (250, 300, 400, 250))
    rect(screen, white, (250, 300, 400, 250), 5)
    ellipse(screen, green4, (400, 340, 300, 70))
    rect(screen, greyf, (550, 310, 90, 238))
    rect(screen, green1, (450, 330, 90, 230))
    rect(screen, green2, (480, 350, 90, 230))
    rect(screen, green3, (300, 360, 90, 230))

    rect(screen, grey_fore_1, (0, 320, 350, 250))
    rect(screen, white, (0, 320, 350, 250), 5)
    rect(screen, green1, (40, 340, 90, 232))
    rect(screen, green2, (0, 360, 90, 240))
    rect(screen, whitef, (230, 335, 90, 237))
    rect(screen, green3, (210, 370, 90, 230))


def draw_cars():
    draw_car(50, 560, 100, 50, zerkal=True)
    draw_car(250, 570, 100, 50, zerkal=True)
    draw_car(360, 560, 100, 50, zerkal=True)
    draw_car(480, 580, 100, 50, zerkal=True)
    draw_car(80, 610, 200, 100)
    draw_car(400, 640, 150, 75, zerkal=True)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 720))
screen.fill((108, 108, 108))

draw_background()
draw_foreground()
draw_cars()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
