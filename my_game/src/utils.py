# utils.py
import pygame
from src.items.glove_resource.glove_resource import Resource, CustomGroup
from src.maps.maps import MiniMap

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
        8: pygame.transform.scale(pygame.image.load('my_game/assets/images/ground.png'), (tile_size, tile_size)), # ground texture
        9: pygame.transform.scale(pygame.image.load('my_game/src/items/glove_resource/glove_resource.png'), (tile_size, tile_size))  # Glove texture
    }

def create_resources(map, textures, tile_size, is_underworld):
    glove_resources = CustomGroup()

    if is_underworld:
        for i, row in enumerate(map):
            for j, cell in enumerate(row):
                if cell == 9:
                    glove_resource = Resource(j * tile_size, i * tile_size, textures[9])
                    glove_resources.add(glove_resource)

    return glove_resources


def draw_map(map_name, current_maps, underworld_maps, textures, screen, tile_size, maps, player_position):
    for i in range(len(current_maps[map_name])):
        for j in range(len(current_maps[map_name][i])):
            tile_type = current_maps[map_name][i][j]
            if tile_type != 0 and tile_type != 9:  # Don't draw anything for empty space
                screen.blit(textures[tile_type], (j * tile_size, i * tile_size))
                if tile_type == 3 or tile_type == 6:  # Draw a red border for dangerous tiles
                    pygame.draw.rect(screen, (255, 0, 0), (j * tile_size, i * tile_size, tile_size, tile_size), 1)

    other_map = underworld_maps[map_name] if current_maps == maps else maps[map_name]
    mini_map = MiniMap(other_map, player_position)

    screen_width, _ = screen.get_size()
    mini_map_width, _ = mini_map.surface.get_size()
    mini_map.draw(screen, (screen_width - mini_map_width, 0))


def handle_player_movement(player, keys, tiles, PLAYER_VEL, tile_size, game,is_underworld):
    player.handle_move(player, keys, tiles, PLAYER_VEL, tile_size)

    dangerous_tiles = []
    for row in range(len(game.current_maps[game.current_map_key])):
        for col in range(len(game.current_maps[game.current_map_key][row])):
            tile_type = game.current_maps[game.current_map_key][row][col]
            if tile_type == 3 or tile_type == 6:
                tile_rect = pygame.Rect(col*tile_size, row*tile_size, tile_size, tile_size)
                dangerous_tiles.append(tile_rect)
    collisions = player.collision_test(dangerous_tiles)
    if collisions:
        game.end_game()

    if is_underworld:
        collided_sprites = pygame.sprite.spritecollide(player, game.current_resources, True)
        # The True argument makes spritecollide remove the sprites in the group when there is a collision
        for sprite in collided_sprites:
            game.resources_collected += 1