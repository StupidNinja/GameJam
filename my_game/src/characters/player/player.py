import pygame
        
        
class Player(pygame.sprite.Sprite):
    COLOR=(255,0,0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("PinkMan", 32, 32, True)
    def __init__(self, x, y, width, height ):
        
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = 0
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        
    def move(self, dx, dy):
        self.rect.x +=dx
        self.rect.y += dy
        
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
            
        
        
    def move_right(self,vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
            
    def loop(self, fps):
        # self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        
        self.fall_count += 1
    
    def draw(self, win):
        self.sprite = self.SPRITES["idle"][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y))
    
        
        
