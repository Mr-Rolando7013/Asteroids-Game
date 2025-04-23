import pygame
from constants import *
from player import Player
from asteroidfield import *
from asteroid import *
import sys
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    blackColor = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x,y)
    drawable_asteroids = pygame.sprite.Group()
    Asteroid.containers = (drawable_asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    drawable_shots = pygame.sprite.Group()
    field = AsteroidField()
    Shot.containers = (drawable, updatable, drawable_shots)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill(blackColor)
        for thing in drawable:
            thing.draw(screen)
            if thing is player or isinstance(thing, Shot):
                continue
            if player.collide(thing):
                print("Game over!")
                pygame.quit()
                sys.exit()
        for shot in drawable_shots:
            shot.draw(screen)
            for asteroid in drawable_asteroids:
                if shot.collide(asteroid):
                    print("Shot hit by asteroid")
                    shot.kill()
                    asteroid.split()
        #player.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
