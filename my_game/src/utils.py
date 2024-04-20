import pygame
from src.items.glove_resource.glove_resource import Resource
from src.maps.maps import MiniMap

def load_textures(tile_size):
    glove_resource = Resource(0, 0)  # Create a Resource object for the glove

    return {
        0: None,  # No texture for empty space
        1: pygame.transform.scale(pygame.image.load('my_game/assets/images/grass2.png'), (tile_size, tile_size)),  # Grass ground texture
        2: pygame.transform.scale(pygame.image.load('my_game/assets/images/box.png'), (tile_size, tile_size)),  # Box texture
        3: pygame.transform.scale(pygame.image.load('my_game/assets/images/lava.png'), (tile_size, tile_size)), # lava texture
        4: pygame.transform.scale(pygame.image.load('my_game/assets/images/metalbox.png'), (tile_size, tile_size)), # metalbox texture
        5: pygame.transform.scale(pygame.image.load('my_game/assets/images/metalbox2.png'), (tile_size, tile_size)), # metalbox2 texture
        6: pygame.transform.scale(pygame.image.load('my_game/assets/images/ships.png'), (tile_size, tile_size)), # ships texture
        7: pygame.transform.scale(pygame.image.load('my_game/assets/images/mushroom.png'), (tile_size, tile_size)), # mushroom texture
        8: pygame.transform.scale(pygame.image.load('my_game/assets/images/ground.png'), (tile_size, tile_size)), # ground texture
        9: glove_resource  # Glove texture
    }

def draw_map(map_name, current_maps, underworld_maps, textures, screen, tile_size, maps,player_position):
    for i in range(len(current_maps[map_name])):
        for j in range(len(current_maps[map_name][i])):
            tile_type = current_maps[map_name][i][j]
            if tile_type != 0:  # Don't draw anything for empty space
                if tile_type == 9:  # If the tile type is 9, draw the glove
                    textures[tile_type].draw(screen)
                else:
                    screen.blit(textures[tile_type], (j * tile_size, i * tile_size))

    # Create a mini map for the other map
    other_map = underworld_maps[map_name] if current_maps == maps else maps[map_name]
    mini_map = MiniMap(other_map, player_position)

    # Draw the mini map at the top-right corner of the screen
    screen_width, _ = screen.get_size()
    mini_map_width, _ = mini_map.surface.get_size()
    mini_map.draw(screen, (screen_width - mini_map_width, 0))

def handle_player_movement(player, keys, tiles, PLAYER_VEL, tile_size):
    player.handle_move(player, keys, tiles, PLAYER_VEL, tile_size)