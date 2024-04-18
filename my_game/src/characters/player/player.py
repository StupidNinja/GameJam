import pygame
import os

def load_sprite_sheets(dir1, dir2, width, height, direction = False):
    path = os.path.join("src", dir1, dir2)
    images =[f for f in os.listdir(path) if os.path.isfile(join(path, f))]
    
    all_sprites = {}
    
    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        
        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))
        
        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites
            
    return all_sprites  
        
class Player(pygame.sprite.Sprite):
    COLOR=(255,0,0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("player", "animation", 32, 32, True)
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
        self.sprite = self.SPRITES["calm"][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y))
    
        
        
