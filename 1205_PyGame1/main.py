# Документация: python -m pygame.docs
# Example file showing a basic pygame "game loop"
import pygame
from random import random


def draw1(screen):
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("0x000000")
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, PyGame!", True, (255, 204, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x, text_y, text_w, text_h), 1)


def draw_square(screen):
    color = pygame.Color(50, 150, 50)
    pygame.draw.rect(screen, color, (20, 20, 100, 100), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3] - 0.9)
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


def draw_pixels(screen):
    for i in range(10000):
        screen.fill(pygame.Color('0x99AA22'), (random() * width, random() * height, 20, 2))




if __name__ == '__main__':
    # pygame setup
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill("0xE00FFF")

        # RENDER YOUR GAME HERE
        draw1(screen)
        draw_square(screen)
        draw_pixels(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(30)  # limits FPS to 30

    pygame.quit()

