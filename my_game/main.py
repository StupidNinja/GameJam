import pygame
from src.maps.maps import maps
from src.characters.player.player import Player
# Initialize Pygame
pygame.init()

# Define the size of each tile and the screen
tile_size =50  # Change this value to shrink or expand the tiles
screen_width = tile_size * len(maps["map_1"][0])
screen_height = tile_size * len(maps["map_1"])
screen_size = (screen_width, screen_height)

FPS = 60
PLAYER_VEL = 5
PLAYER_Y = (screen_height - tile_size *2)
clock = pygame.time.Clock()


# Load the texture
textures = {
    0: None,  # No texture for empty space
    1: pygame.transform.scale(pygame.image.load('my_game/assets/images/grass.png'), (tile_size, tile_size)),  # Grass ground texture
    2: pygame.transform.scale(pygame.image.load('my_game/assets/images/box.png'), (tile_size, tile_size)),  # Box texture
    3: pygame.transform.scale(pygame.image.load('my_game/assets/images/concrete.png'), (tile_size, tile_size))  # Concrete texture
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


# Create a list of tile rectangles for collision detection
tiles = [pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size) for i in range(len(maps["map_1"])) for j in range(len(maps["map_1"][i])) if maps["map_1"][i][j] != 0]

# Create the player
player = Player(0, PLAYER_Y, tile_size, tile_size)  # Change the player size to match the tile size

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with sky blue color
    screen.fill((135, 206, 235))

    # Handle player movement
    player.handle_move(player,pygame.key.get_pressed(),tiles,PLAYER_VEL,tile_size)
    
    # Draw the map
    draw_map("map_1")

    # Draw the player
    
    player.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()