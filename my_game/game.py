import pygame
from src.maps.maps import maps, underworld_maps
from src.utils import create_resources
from src.items.glove_resource.glove_resource import CustomGroup

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
        self.resources_collected = 0
        self.is_underworld = False 
        self.resources = {current_map_key: create_resources(self.current_maps[self.current_map_key], self.textures, self.tile_size, self.is_underworld)}
        self.current_resources = self.resources[current_map_key]

    def create_tiles(self):
        return [self._create_tile(i, j) for i, row in enumerate(self.current_maps[self.current_map_key]) for j, cell in enumerate(row) if cell != 0 and cell != 9]

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

    def collect_resources(self):
        if self.current_maps == self.underworld_maps:  # Check if the current map is an underworld map
            for sprite in self.current_resources.sprites():
                if sprite.active and pygame.sprite.collide_rect(self.player, sprite):
                    self.resources_collected += 1
                    sprite.active = False
                    sprite.visible = False

    def draw_bar(self, total_sections, filled_sections, bar_color=(0, 255, 0), empty_color=(255, 0, 0), bar_width=100, bar_height=20, space=2):
        section_width = (bar_width - (total_sections - 1) * space) // total_sections

        for i in range(total_sections):
            x = self.player.rect.centerx - bar_width // 2 + i * (section_width + space)
            y = self.player.rect.y - bar_height - 10  # 10 is the space between the player and the bar
            if y < 0:  # If the bar would be drawn off the screen, adjust its y-coordinate
                y = self.player.rect.y + self.player.rect.height + 10
            if i < filled_sections:
                pygame.draw.rect(self.screen, bar_color, pygame.Rect(x, y, section_width, bar_height))
            else:
                pygame.draw.rect(self.screen, empty_color, pygame.Rect(x, y, section_width, bar_height))

    def switch_map(self):
        if self.current_maps == self.maps:
            self.current_maps = self.underworld_maps
            self.is_underworld = True
            # Reactivate and show the sprites
            for sprite in self.current_resources.sprites():
                sprite.active = True
                sprite.visible = True
        else:
            self.current_maps = self.maps
            self.is_underworld = False
            # Deactivate the sprites
            for sprite in self.current_resources.sprites():
                sprite.active = False
        self.tiles = self.create_tiles()
        self._adjust_player_position()
    def switch_map_key(self, new_map_key):
        if new_map_key in self.maps:
            self.current_map_key = new_map_key
            self.current_maps = self.maps if not self.is_underworld else self.underworld_maps
            self.tiles = self.create_tiles()
            self.entities = self.create_entities()
            self.resources = {new_map_key: create_resources(self.current_maps[self.current_map_key], self.textures, self.tile_size, self.is_underworld)}
            self.current_resources = self.resources[new_map_key]
            self._adjust_player_position()
        else:
            print(f"Invalid map key: {new_map_key}")
            
    def _adjust_player_position(self):
        collision = True
        while collision:
            collision = False
            for tile in self.tiles:
                if self.player.rect.colliderect(tile):
                    self.player.rect.y = tile.y - self.player.rect.height
                    collision = True
                    break