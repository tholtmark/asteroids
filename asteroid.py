import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) # pass radius to parent class

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR, self.position, self.radius, width = 2)
           
    def split(self):
        self.kill()
    
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector_1 * 1.2
    
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector_2 * 1.2