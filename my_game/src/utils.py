import pygame

def load_textures(tile_size):
    return {
        0: None,  # No texture for empty space
        1: pygame.transform.scale(pygame.image.load('my_game/assets/images/grass2.png'), (tile_size, tile_size)),  # Grass ground texture
        2: pygame.transform.scale(pygame.image.load('my_game/assets/images/box.png'), (tile_size, tile_size)),  # Box texture
        3: pygame.transform.scale(pygame.image.load('my_game/assets/images/lava.png'), (tile_size, tile_size)), # lava texture
        4: pygame.transform.scale(pygame.image.load('my_game/assets/images/metalbox.png'), (tile_size, tile_size)), # metalbox texture
        5: pygame.transform.scale(pygame.image.load('my_game/assets/images/metalbox2.png'), (tile_size, tile_size)), # metalbox2 texture
        6: pygame.transform.scale(pygame.image.load('my_game/assets/images/ships.png'), (tile_size, tile_size)), # ships texture
        7: pygame.transform.scale(pygame.image.load('my_game/assets/images/mushroom.png'), (tile_size, tile_size)), # mushroom texture
        8: pygame.transform.scale(pygame.image.load('my_game/assets/images/ground.png'), (tile_size, tile_size)) # ground texture
    }

def draw_map(map_name, current_maps, textures, screen, tile_size):
    for i in range(len(current_maps[map_name])):
        for j in range(len(current_maps[map_name][i])):
            tile_type = current_maps[map_name][i][j]
            if tile_type != 0:  # Don't draw anything for empty space
                screen.blit(textures[tile_type], (j * tile_size, i * tile_size))

def handle_player_movement(player, keys, tiles, PLAYER_VEL, tile_size):
    player.handle_move(player, keys, tiles, PLAYER_VEL, tile_size)