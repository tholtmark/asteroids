# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from pygame.locals import K_ESCAPE, KEYDOWN

# initialize pygame
pygame.init()

# create an object to help track time
clock = pygame.time.Clock()
dt = 0

# set up display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # instantiate a Player object
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    while True:
        # calculating dt first!
        dt = clock.tick(60) / 1000.0

       # Handle termination events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                 pygame.quit()
                 exit()

        # re-rendering player each frame
        player.update(dt)
        
        # Fill the screen with black
        screen.fill((0, 0, 0))
        player.draw(screen)
        

        # Refresh the display
        pygame.display.flip()


if __name__ == "__main__":
    main()