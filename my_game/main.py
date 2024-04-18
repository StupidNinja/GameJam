import pygame
from src.maps.maps import maps
from src.characters.player.player import Player
# Initialize Pygame
pygame.init()

# Define the size of each tile and the screen
tile_size = 64
screen_width = tile_size * len(maps["map_1"][0])
screen_height = tile_size * len(maps["map_1"])
screen_size = (screen_width, screen_height)

FPS = 60
PLAYER_VEL = 5
clock = pygame.time.Clock()

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
    

player = Player(0, (screen_height - (tile_size * 3)), 64, 64)

# def handle_move(player):
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player.move_left(PLAYER_VEL)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with sky blue color
    screen.fill((135, 206, 235))
    
    def handle_move(player):
        keys = pygame.key.get_pressed()
    

        player.x_vel = 0
        if keys[pygame.K_LEFT]:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            player.move_right(PLAYER_VEL)   


    # Draw the map
    draw_map("map_1")
    player.draw(screen)
    player.loop(FPS)
    handle_move(player)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()