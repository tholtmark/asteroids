import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        # correctly initializing the parent class and setting up rotation
        super().__init__(x, y, PLAYER_RADIUS) # pass x, y, and radius to CircleShape
        self.rotation = 0
        self.shot_cooldown = 0 # use self. to indicate it's an instance variable

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # override the draw method of CircleShape
    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(),2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        
        # since rotate is method of this class, we call it with self
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_cooldown <= 0: # checks for spacebar and cooldown
            self.shoot()
        if self.shot_cooldown > 0: # this checks if cooldown still active, if so decrease it by timer
            self.shot_cooldown -= dt

    def shoot(self):
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN # sets the cooldown timer after a shot is made
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


    def rotate(self, dt):
        # dt is used directly here, no need to store it with a self.dt
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    

    
