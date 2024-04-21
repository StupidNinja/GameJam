import pygame


class Resource(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.active = True
        self.visible = True


    def draw(self, surface):
        if self.visible:
            surface.blit(self.image, self.rect)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class CustomGroup(pygame.sprite.Group): # Custom group class that allows for drawing only visible sprites
    def draw(self, surface):
        for sprite in self.sprites():
            if sprite.visible:
                surface.blit(sprite.image, sprite.rect)