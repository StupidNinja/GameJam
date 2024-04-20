# main.py
import pygame
from src.maps.maps import maps, underworld_maps
from src.characters.player.player import Player
from src.utils import load_textures, draw_map, handle_player_movement,create_resources
from src.items.glove_resource.glove_resource import Resource
from game import Game

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
    PLAYER_Y = (screen_height - tile_size *2) + 3
    clock = pygame.time.Clock()
    
    # Initialize the current map and map type
    current_map_key = "map_1"
    current_maps = maps

    # Load the texture
    textures = load_textures(tile_size)

    # Create the screen 
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Create the player
    player = Player(0, PLAYER_Y, tile_size-5, tile_size-5)  # Change the player size to match the tile size
    player_position = (player.rect.x, player.rect.y)

    

    # Create the game
    game = Game(screen, current_maps, underworld_maps, current_map_key, player, textures, tile_size, maps)

    # Game loop
    running = True
    previous_map_key = None
    sections_number = 4
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    game.switch_map()
                    print(game.resources)
                    if game.current_map_key != previous_map_key:
                        game.resources[game.current_map_key] = create_resources(game.current_maps[game.current_map_key], game.textures, game.tile_size, game.is_underworld)
                        game.current_resources = game.resources[game.current_map_key]
                        previous_map_key = game.current_map_key

        if game.resources_collected == 4 and game.current_map_key == "map_1":
            game.resources_collected = 0
            sections_number = 3
            game.switch_map_key("map_2")
            player.rect.x, player.rect.y = 0, PLAYER_Y
            

        elif game.resources_collected == 3 and game.current_map_key == "map_2":
            game.resources_collected = 0
            sections_number = 2
            game.switch_map_key("map_3")
            player.rect.x, player.rect.y = 0, PLAYER_Y
            
            

        # Fill screen with sky blue color
        screen.fill((135, 206, 235))

        game.collect_resources()

        # If the current map is not the underworld map, make the sprites inactive and invisible
        if game.current_maps == game.maps:
            for sprite in game.current_resources.sprites():
                sprite.active = False
                sprite.visible = False
        else:
            for sprite in game.current_resources.sprites():
                sprite.active = True
                sprite.visible = True

        # Handle player movement
        handle_player_movement(player, pygame.key.get_pressed(), game.tiles, PLAYER_VEL, tile_size, game)

        # Update the sprites
        for sprite in game.current_resources.sprites():
            if sprite.active:
                sprite.update()


        # Update the player's position
        player_position = (player.rect.x, player.rect.y)

        # Draw the map
        draw_map(game.current_map_key, game.current_maps, game.underworld_maps, game.textures, game.screen, game.tile_size,maps,player_position)

        # Draw the resource bar
        game.draw_bar(sections_number, game.resources_collected)

        # Draw the resources
        game.current_resources.draw(game.screen)

        # Draw the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()