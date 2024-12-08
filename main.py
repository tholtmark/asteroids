# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from circleshape import CircleShape
from pygame.locals import K_ESCAPE, KEYDOWN
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    # instantiate a Player object in middle of screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # creating groups and adding player instance
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # setting static containers for Asteroid, Shot and AsteroidField class
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # instatiate an AsteroidField
    asteroid_field = AsteroidField()

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

        # iterate through asteroids and check if there is a player collision
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()  # removes shot
                    asteroid.split()  # splits or kills asteroid

        # iterate though all sprites in updatable group and update them
        for sprite in updatable:
            sprite.update(dt)

            # Update display
            pygame.display.flip()  # Update the screen to show changes

        # Clear the screen
        screen.fill((0, 0, 0))

        # iterate through all sprites drawable group and draw them on screen
        for sprite in drawable:
            sprite.draw(screen)

        # Refresh the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
