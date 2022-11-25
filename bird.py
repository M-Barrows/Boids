import pygame

class Bird(pygame.sprite.Sprite):

    def __init__(self,position:tuple, velocity:int, size:int, vision:int) -> None:
        pygame.sprite.Sprite.__init__(self)
        """
        Creates a bird object with starting position and velocity

        position: (x:int,y:int) tuple. Describes where a bird is on the canvas
        velocity: (velocity_x:int, velocity_y:int) tuple. Describes where a bird is going on the canvas.
        size: int - Size of the boid
        vision: int - Scalar - how many size units will the boid "see" or check for collision. (This basically sets the `.rect` size relative to the drawn sprite)
        """
        self.vx = velocity
        self.vy = velocity
        self.angle = 0
        self.position = position
        self.size = size
        self.color = (255,255,255)
        self.image = pygame.surface.Surface([size,size*2],flags=pygame.SRCALPHA)
        self.image.fill((0,0,0,50))
        pygame.draw.polygon(self.image, self.color, [[self.size/2, 0], [self.size, self.size*2],[0, self.size*2]])
        self.rect = self.image.get_rect(center = position)
        
        self.orig_image = self.image



    def update(self):
        _screen_w,_screen_h = pygame.display.get_window_size()

        # Edge detection
        if self.rect.left <= 0 or self.rect.right >= _screen_w:
            self.vx = self.vx*-1
        if self.rect.top <= 0 or self.rect.bottom >= _screen_h:
            self.vy = self.vy*-1


        # Move the sprite
        self.position = [self.position[0] + self.vx, self.position[1] +  self.vy]

        # Rotate Sprite
        self.angle += 1
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.position)



