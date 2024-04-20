import pygame
from src.maps.maps import maps, underworld_maps

class Game:
    def __init__(self, screen, current_maps, underworld_maps, current_map_key, player, textures, tile_size, maps):
        self.screen = screen
        self.current_maps = current_maps
        self.maps = maps
        self.underworld_maps = underworld_maps
        self.current_map_key = current_map_key
        self.player = player
        self.textures = textures
        self.tile_size = tile_size
        self.tiles = self.create_tiles()
        self.entities = self.create_entities()

    def create_tiles(self):
        return [self._create_tile(i, j) for i, row in enumerate(self.current_maps[self.current_map_key]) for j, cell in enumerate(row) if cell != 0]

    def _create_tile(self, i, j):
        return pygame.Rect(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)

    def create_entities(self):
        entities = []
        for i, row in enumerate(self.current_maps[self.current_map_key]):
            for j, cell in enumerate(row):
                if cell == 9:
                    entities.append(self._create_entity(i, j))
        for i, row in enumerate(self.underworld_maps[self.current_map_key]):
            for j, cell in enumerate(row):
                if cell == 9:
                    entities.append(self._create_entity(i, j))
        return entities

    def _create_entity(self, i, j):
        return pygame.Rect(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)

    def switch_map(self):
        self.current_maps = underworld_maps if self.current_maps == maps else maps
        self.tiles = self.create_tiles()
        self._adjust_player_position()

    def _adjust_player_position(self):
        collision = True
        while collision:
            collision = False
            for tile in self.tiles:
                if self.player.rect.colliderect(tile):
                    self.player.rect.y = tile.y - self.player.rect.height
                    collision = True
                    break