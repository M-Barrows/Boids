import pygame
import math
import random
class Bird(pygame.sprite.Sprite):

    def __init__(self,position:tuple, velocity:int, size:int, vision:int) -> None:
        pygame.sprite.Sprite.__init__(self)
        """
        Creates a bird object with starting position and velocity

        position: (x:int,y:int) tuple. Describes where a bird is on the canvas
        speed: int. Describes how fast a bird will move (px).
        size: int - Size of the boid
        vision: int - Scalar - how many size units will the boid "see" or check for collision. (This basically sets the `.rect` size relative to the drawn sprite)
        """
        self.max_speed = 3
        self.steering_force = 0.2
        self.angle = 180#random.randrange(-180,180)
        self.dx = velocity
        self.dy = velocity
        self.position = position
        self.size = size
        self.color = (255,255,255)
        self.image = pygame.surface.Surface([size,size*2],flags=pygame.SRCALPHA)
        self.image.fill((0,0,0,0))
        pygame.draw.polygon(self.image, self.color, [
            [self.size/2, 0],
            [self.size, self.size*2],
            [self.size/2,self.size*1.6],
            [0, self.size*2]])
        self.rect = self.image.get_rect(center = position)

        self.orig_image = self.image


    def update(self):
        _screen_w,_screen_h = pygame.display.get_window_size()
        # Edge detection
        if self.position[0] <= self.size*4:
            self.dx -= self.steering_force
        if self.position[1] <= self.size*4:
            self.dy -= self.steering_force
        if self.position[0] >= _screen_w-(self.size*4):
            self.dx += self.steering_force
        if self.position[1] >= _screen_h-(self.size*4):
            self.dy += self.steering_force


        # Move the sprite
        x,y = self.position
        x -= self.dx 
        y -= self.dy
        self.position = [x,y]

        # Rotate Sprite
        self.image = pygame.transform.rotate(self.orig_image, math.degrees(math.atan2(-self.dy,self.dx))+90)
        self.rect = self.image.get_rect(center=self.position)



