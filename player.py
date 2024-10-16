import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.shoot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, "WHITE", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
        else:
            if keys[pygame.K_SPACE]:
                self.shoot()


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        new_shot = Shot(position=self.position, velocity=shot_velocity)
        if self.shoot_cooldown > 0:
            return
        else:
            self.shots_group.add(new_shot)
            self.shoot_cooldown = PLAYER_SHOT_COOLDOWN