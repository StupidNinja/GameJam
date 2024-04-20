import pygame
import os

class Resource:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50  # Replace with the actual width
        self.height = 50  # Replace with the actual height
        self.images = [pygame.image.load(os.path.join('my_game\\src\\items\\glove_resource\\animation', f'glove_resource{i+1}.png')) for i in range(8)]
        self.frame = 0

    def draw(self, screen):
        screen.blit(self.images[self.frame % len(self.images)], (self.x, self.y))
        self.frame += 1

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)