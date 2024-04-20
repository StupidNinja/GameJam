# main.py
import pygame
from src.maps.maps import maps, underworld_maps
from src.characters.player.player import Player
from src.utils import load_textures, draw_map, handle_player_movement
from src.game import Game

def main():
    # Initialize Pygame
    pygame.init()

    # Define the size of each tile and the screen
    tile_size =64 # Change this value to shrink or expand the tiles
    screen_width = tile_size * len(maps["map_1"][0])
    screen_height = tile_size * len(maps["map_1"])
    screen_size = (screen_width, screen_height)

    FPS = 60
    PLAYER_VEL = 5
    PLAYER_Y = (screen_height - tile_size *2)
    clock = pygame.time.Clock()

    # Load the texture
    textures = load_textures(tile_size)

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Create the player
    player = Player(0, PLAYER_Y, tile_size, tile_size)  # Change the player size to match the tile size
    player_position = (player.rect.x, player.rect.y)

    # Initialize the current map and map type
    current_map_key = "map_1"
    current_maps = maps

    # Create the game
    game = Game(screen, current_maps, underworld_maps, current_map_key, player, textures, tile_size, maps)

    # Game loop
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    game.switch_map()

        # Fill screen with sky blue color
        screen.fill((135, 206, 235))

        # Handle player movement
        handle_player_movement(player, pygame.key.get_pressed(), game.tiles, PLAYER_VEL, tile_size)

        # Update the player's position
        player_position = (player.rect.x, player.rect.y)

        # Draw the map
        draw_map(game.current_map_key, game.current_maps, game.underworld_maps, game.textures, game.screen, game.tile_size,maps,player_position)

        # Draw the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()