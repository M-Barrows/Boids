import pygame, sys
from pygame.locals import *
from bird import Bird
import random

pygame.init()
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 300
SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
BIRDS = 10

pygame.display.set_caption('Boid Simulation')
clock = pygame.time.Clock() 

entities = pygame.sprite.Group()

def pick_non_zero_int():
    choice = random.normalvariate(0,.5)
    if choice == 0:
        pick_non_zero_int()
    else:
        return choice

for i in range(1,BIRDS+1):
    b = Bird(
        position = (random.randint(100,DISPLAY_WIDTH),random.randint(100, DISPLAY_HEIGHT)),
        velocity = [pick_non_zero_int(),pick_non_zero_int()],
        size = 10,
        vision = 50
    )
    entities.add(b) 
forces = {
        'separation': 0.001,
        'alignment': 0.05,
        'coherance': 0.05
    }

while True: # main game loop
    SCREEN.fill((50,50,50))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            forces['separation'] += 0.001
            print(forces)

        if keys[pygame.K_DOWN]:
            forces['separation'] -= 0.001
            print(forces)

        if keys[pygame.K_RIGHT]:
            forces['alignment'] += 0.001
            print(forces)
        if keys[pygame.K_LEFT]:
            forces['alignment'] -= 0.001
            print(forces)
        if keys[pygame.K_PERIOD]:
            forces['coherance'] += 0.001
            print(forces)
        if keys[pygame.K_COMMA]:
            forces['coherance'] -= 0.001
            print(forces)

    entities.update(entities,forces)
    entities.draw(SCREEN)
    clock.tick(60)
    pygame.display.update()
    