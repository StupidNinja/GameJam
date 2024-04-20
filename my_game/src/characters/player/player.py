import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        
        self.x_vel = 0
        self.y_vel = 0
        self.is_jumping = False
        self.prev_up_key = False
        self.is_moving = False
        self.direction = "right"
        self.sprites = {
            "calm": pygame.transform.scale(pygame.image.load('my_game/src/characters/player/animation/calm.png'), (width, height)),
            "walk": [
                pygame.transform.scale(pygame.image.load('my_game/src/characters/player/animation/walk1.png'), (width, height)),
                pygame.transform.scale(pygame.image.load('my_game/src/characters/player/animation/walk2.png'), (width, height)),
                pygame.transform.scale(pygame.image.load('my_game/src/characters/player/animation/walk3.png'), (width, height))
            ]
        }
        self.state = "calm"
        self.animation_count = 0
        # self.mask = pygame.mask.from_surface(self.sprites)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        if dx != 0:
            self.state = "walk"
            self.direction = "right" if dx > 0 else "left"
        else:
            self.state = "calm"

    def apply_gravity(self, gravity):
        self.y_vel += gravity
        self.rect.y += self.y_vel

    def draw(self, win):
        # if self.is_jumping:  # Player is jumping
        #     sprite = self.sprites["jump"]
        if self.is_moving:  # Player is walking
            sprite = self.sprites["walk"][self.animation_count // 8 % len(self.sprites["walk"])]
            self.animation_count += 1
        else:  # Player is standing still
            sprite = self.sprites["calm"]
            self.animation_count = 0

        if self.direction == "left":
            sprite = pygame.transform.flip(sprite, True, False)

        win.blit(sprite, (self.rect.x, self.rect.y))
    # Collision detection with tiles
    def collision_test(self, tiles):
        collisions = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                collisions.append(tile)
        return collisions
    def jump(self, tile_size):
        # Changable jump velocity respectively for scale 10 for 64px tile, 7.5 for 32px tile, 5 for 16px tile
        self.y_vel = (-3.75) - ((tile_size/16)*1.5)  #  5 for 16px tiles, 7.5 for 32px tiles, and 10 for 64px tiles
        print(self.y_vel)
        
    
    def handle_move(self, player, keys, tiles, PLAYER_VEL, tile_size):
        # Apply gravity to the player
        initial_y = player.rect.y  # Store the player's initial y position
        player.apply_gravity(0.5)
        y_collisions = player.collision_test(tiles)
        if y_collisions:  # If a collision occurred, reset the player's y position
            player.rect.y = initial_y
            player.y_vel = 0
            player.is_jumping = False  # Player has landed

        if keys[pygame.K_LEFT]:
            initial_x = player.rect.x  # Store the player's initial x position
            player.move(-PLAYER_VEL, 0)
            x_collisions = player.collision_test(tiles)
            if x_collisions:  # If a collision occurred, reset the player's x position
                player.rect.x = initial_x
            player.x_vel = 0
            self.is_moving = True

        if keys[pygame.K_RIGHT]:
            initial_x = player.rect.x  # Store the player's initial x position
            player.move(PLAYER_VEL, 0)
            x_collisions = player.collision_test(tiles)
            if x_collisions:  # If a collision occurred, reset the player's x position
                player.rect.x = initial_x
            player.x_vel = 0
            self.is_moving = True

        if keys[pygame.K_UP] and not player.prev_up_key and not player.is_jumping:  # Jump if UP key is just pressed and player is not already jumping
            # Check if there's a tile above the player
            player.rect.y -= 1  # Temporarily move the player up
            if not player.collision_test(tiles):
                player.jump(tile_size)
                player.is_jumping = True  # Player has jumped
            player.rect.y += 1  # Move the player back to the original position
        elif not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            player.is_moving = False

        player.prev_up_key = keys[pygame.K_UP]  # Store the current state of the UP key
