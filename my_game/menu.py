# menu.py
import pygame
from main import main

class Button:
    def __init__(self, text, x, y, width, height, inactive_color, active_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.inactive_color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def handle_click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            if click[0] == 1:
                if self.text == "Start":
                    main()
                elif self.text == "Quit":
                    pygame.quit()

def menu():
    pygame.init()

    screen_width = 1280
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))

    button_width = 200
    button_height = 50
    button_y_start = 200
    button_y_gap = 100

    start_button = Button("Start", screen_width // 2 - button_width // 2, button_y_start, button_width, button_height, (50, 50, 50), (100, 100, 100))
    quit_button = Button("Quit", screen_width // 2 - button_width // 2, button_y_start + button_height + button_y_gap, button_width, button_height, (50, 50, 50), (100, 100, 100))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        start_button.draw(screen)
        quit_button.draw(screen)

        start_button.handle_click()
        quit_button.handle_click()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    menu()