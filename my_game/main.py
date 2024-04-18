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

def flip(sprites):
    return[pygame.transform.flip(sprite, True, False) for sprite in sprites]

# def load_sprite_sheets(dir1, dir2, width, height, direction = False):
#     path = join("src", dir1, dir2)
#     images =[f for f in listdir(path) if isfile(join(path, f))]
    
#     all_sprites = {}
    
#     for image in images:
#         sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        
#         sprites = []
#         for i in range(sprite_sheet.get_width() // width):
#             surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
#             rect = pygame.Rect(i * width, 0, width, height)
#             surface.blit(sprite_sheet, (0, 0), rect)
#             sprites.append(pygame.transform.scale2x(surface))
        
#         if direction:
#             all_sprites[image.replace(".png", "") + "_right"] = sprites
#             all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
#         else:
#             all_sprites[image.replace(".png", "")] = sprites
            
#     return all_sprites

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