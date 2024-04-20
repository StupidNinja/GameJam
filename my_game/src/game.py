import pygame
from src.maps.maps import maps, underworld_maps

class Game:
    def __init__(self, screen, current_maps, current_map_key, player, textures, tile_size):
        self.screen = screen
        self.current_maps = current_maps
        self.current_map_key = current_map_key
        self.player = player
        self.textures = textures
        self.tile_size = tile_size
        self.tiles = self.create_tiles()

    def create_tiles(self):
        return [pygame.Rect(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size) for i in range(len(self.current_maps[self.current_map_key])) for j in range(len(self.current_maps[self.current_map_key][i])) if self.current_maps[self.current_map_key][i][j] != 0]

    def switch_map(self):
        self.current_maps = underworld_maps if self.current_maps == maps else maps
        self.tiles = self.create_tiles()

        # Check if the player position is not where the tiles are placed
        collision = True
        while collision:
            collision = False
            for tile in self.tiles:
                if self.player.rect.colliderect(tile):
                    # print("Player is on a tile when the map changed. Adjusting player position.")
                    self.player.rect.y = tile.y - self.player.rect.height
                    collision = True
                    break