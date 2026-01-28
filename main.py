import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Clock object
    clock = pygame.time.Clock()
    dt = 0

    # Game loop
    while True:
        log_state()
        
        # Add 'x out' functionality to game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()

        # Cap FPS at 60 and compute delta time (in seconds)
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
