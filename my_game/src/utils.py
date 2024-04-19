import pygame

def load_textures(tile_size):
    return {
        0: None,  # No texture for empty space
        1: pygame.transform.scale(pygame.image.load('my_game/assets/images/grass.png'), (tile_size, tile_size)),  # Grass ground texture
        2: pygame.transform.scale(pygame.image.load('my_game/assets/images/box.png'), (tile_size, tile_size)),  # Box texture
        3: pygame.transform.scale(pygame.image.load('my_game/assets/images/concrete.png'), (tile_size, tile_size))  # Concrete texture
    }

def draw_map(map_name, current_maps, textures, screen, tile_size):
    for i in range(len(current_maps[map_name])):
        for j in range(len(current_maps[map_name][i])):
            tile_type = current_maps[map_name][i][j]
            if tile_type != 0:  # Don't draw anything for empty space
                screen.blit(textures[tile_type], (j * tile_size, i * tile_size))

def handle_player_movement(player, keys, tiles, PLAYER_VEL, tile_size):
    player.handle_move(player, keys, tiles, PLAYER_VEL, tile_size)