import pygame

from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
        self.rect = pygame.Rect(position.x - SHOT_RADIUS, position.y - SHOT_RADIUS, SHOT_RADIUS * 2, SHOT_RADIUS * 2)

    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius, width = 2)
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))