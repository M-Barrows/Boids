import pygame, sys
from pygame.locals import *
from bird import Bird
import random

pygame.init()
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 800
SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
BIRDS = 10

pygame.display.set_caption('Boid Simulation')
clock = pygame.time.Clock()

entities = pygame.sprite.Group()

for i in range(1,BIRDS+1):
    b = Bird(
        position = (random.randint(0,DISPLAY_WIDTH),random.randint(0, DISPLAY_HEIGHT)),
        velocity = (random.choice([-1,1])*random.randrange(1,5)),
        size = 40,
        vision = 10
    )
    entities.add(b)

while True: # main game loop
    SCREEN.fill((50,50,50))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    entities.update()
    entities.draw(SCREEN)
    clock.tick(60)
    pygame.display.update()
    