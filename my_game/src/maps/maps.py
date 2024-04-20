# maps.py
import pygame

class MiniMap:
    def __init__(self, game_map, player_position, tile_size=8, opacity=128):
        self.game_map = game_map
        self.player_position = player_position
        self.tile_size = tile_size
        self.opacity = opacity
        self.surface = self.create_surface()

    def create_surface(self):
        width = len(self.game_map[0]) * self.tile_size
        height = len(self.game_map) * self.tile_size
        surface = pygame.Surface((width, height)).convert_alpha()
        surface.fill((0, 0, 0, 0))  # Fill with transparent color
    
        for i, row in enumerate(self.game_map):
            for j, cell in enumerate(row):
                if cell != 0:
                    color = (0, 0, 255, self.opacity) if cell == 9 else (255, 255, 255, self.opacity)
                    pygame.draw.rect(surface, color, (j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size))
        
        # Draw the player as a red tile
        player_x, player_y = self.player_position
        player_x //= 64  # Convert the player's x-coordinate to the mini map's scale
        player_y //= 64  # Convert the player's y-coordinate to the mini map's scale
        pygame.draw.rect(surface, (255, 0, 0, self.opacity), (player_x * self.tile_size, player_y * self.tile_size, self.tile_size, self.tile_size))
    
        return surface

    def draw(self, screen, position):
        screen.blit(self.surface, position)

maps = {
    "map_1": [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 10 by 21 map = 640 by 1344
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0 ,0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0 ,0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    #Add more maps here...
}
underworld_maps = {
    "map_1": [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
}