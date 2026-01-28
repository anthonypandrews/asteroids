import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0 # dt is delta time in seconds since last frame
    
    # Group setup
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Player setup
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Welcome message
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game loop
    while running:
        log_state()
        
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        
        # draw the player group
        for p in drawable:
            p.draw(screen)
        updatable.update(dt)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # Cap FPS at 60 and compute delta time (in seconds)
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
