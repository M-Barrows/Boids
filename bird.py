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
        self.steering_force = .5
        self.dx = velocity[0]
        self.dy = velocity[1]
        self.vision = vision
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

    def __avoid_walls__(self):
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

    def __regulaute_speed__(self):
        velocity_ratio = abs(self.dx * self.dy)/self.max_speed
        if velocity_ratio > 1: # Limit Spped
            self.dx = self.dx/velocity_ratio
            self.dy = self.dy/velocity_ratio

        # else:
        #     self.dx += 0.05
        #     self.dy += 0.05

    def __alignment__(self,flock,force,vision):
        """ Steer bird toward the average direction of the flock """
        flock_dy = 0
        flock_dx = 0
        flock_size = 0
        for bird in flock:
            if bird is not self and math.hypot(self.position[0] - bird.position[0],self.position[1]-bird.position[1])<vision:
                flock_dy += bird.dy
                flock_dx += bird.dx
                flock_size += 1
        if flock_size > 0:
            flock_dy = flock_dy/flock_size
            flock_dx = flock_dx/flock_size

            self.dx += (flock_dx - self.dx)*force if flock_dx>self.dx else -1*(flock_dx - self.dx)*force
            self.dy += (flock_dy - self.dy)*force if flock_dy>self.dx else -1*(flock_dy - self.dy)*force


    def __separateion__(self,flock,force,vision):
        """ Steer bird away from nearest fish when too close """
        for other in flock:
            if other is not self and math.hypot(self.position[0] - other.position[0],self.position[1]-other.position[1])<self.size*5:
                x=self.position[0] 
                x += (self.position[0]-other.position[0] ) 
                y=self.position[1]  
                y += (self.position[1]-other.position[1] ) 
                self.dx += x * force
                self.dy += y * force
        

    def __coherance__(self,flock,force,vision):
        """ Steer bird tward neerest bird"""

        # TODO: only do this for the NEAREST bird!
        fx = 0
        fy = 0
        min_distance = 99999
        for other in flock:
            if other is not self:
                if math.hypot(self.position[0] - other.position[0],self.position[1]-other.position[1])<min_distance:
                    min_distance = math.hypot(self.position[0] - other.position[0],self.position[1]-other.position[1])
                    fx = other.dx
                    fy = other.dy
        self.dx -= (self.dx - fx ) * force
        self.dy -= (self.dy - fy) * force


    def update(self,flock,forces):
        
        self.__avoid_walls__()
        self.__alignment__(flock,forces['alignment'],self.vision)
        self.__coherance__(flock,forces['coherance'],self.vision)
        self.__separateion__(flock,forces['separation'],self.vision)
        
        self.__regulaute_speed__()

        # Move the sprite
        x,y = self.position
        x -= self.dx 
        y -= self.dy
        self.position = [x,y]

        # Rotate Sprite
        self.image = pygame.transform.rotate(self.orig_image, math.degrees(math.atan2(-self.dy,self.dx))+90)
        self.rect = self.image.get_rect(center=self.position)


        



