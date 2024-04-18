import pygame
from src.maps.maps import maps

# Initialize Pygame
pygame.init()

# Define the size of each tile and the screen
tile_size = 64
screen_width = tile_size * len(maps["map_1"][0])
screen_height = tile_size * len(maps["map_1"])

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Draw the map
def draw_map(map_name):
    for i in range(len(maps[map_name])):
        for j in range(len(maps[map_name][i])):
            if maps[map_name][i][j] == 1:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the map
    draw_map("map_1")

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()