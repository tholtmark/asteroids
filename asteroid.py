import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) # pass radius to parent class

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self,screen):
        pygame.draw.circle(screen, COLOR, self.position, self.radius, width = 2)
           

    