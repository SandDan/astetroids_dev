import pygame
import sys

from constants import *
from player import Player
from asteroidfield import *
from asteroid import *
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Initialize groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    #Create player and add to groups
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, shots_group)
    updatable.add(player)
    drawable.add(player)
    
    #Set the static containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (shots_group, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot
            
        screen.fill(pygame.Color("BLACK"))
        for asteroid in asteroids:
            for shot in shots_group:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
 
if __name__ == "__main__":
    main()