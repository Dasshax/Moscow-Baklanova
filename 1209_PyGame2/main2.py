# Example file showing a circle moving on screen
import pygame


if __name__ == '__main__':
    # pygame setup
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    v = 500
    dt = 0
    # limits FPS to 60
    fps = 60

    while running:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, "red", event.pos, 90)
                pygame.draw.circle(screen, "red", (width - event.pos[0], event.pos[1]), 40)
                pygame.draw.circle(screen, "red", (event.pos[1], event.pos[0]), 40)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(fps) / 1000

    pygame.quit()

