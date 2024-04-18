import pygame
from src.maps.maps import maps

# Initialize Pygame
pygame.init()

# Define the size of each tile and the screen
tile_size = 64
screen_width = tile_size * len(maps["map_1"][0])
screen_height = tile_size * len(maps["map_1"])


# Load the texture
textures = {
    0: None,  # No texture for empty space
    1: pygame.image.load('my_game/assets/images/grass.png'), # Grass ground texture
    2: pygame.image.load('my_game/assets/images/box.png'), # Box texture
    3: pygame.image.load('my_game/assets/images/concrete.png') # Concrete texture
}

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Draw the map
def draw_map(map_name):
    for i in range(len(maps[map_name])):
        for j in range(len(maps[map_name][i])):
            tile_type = maps[map_name][i][j]
            if tile_type != 0:  # Don't draw anything for empty space
                screen.blit(textures[tile_type], (j * tile_size, i * tile_size))

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