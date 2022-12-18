import sys
from constants import *
from note import *
from sound_arr import *


def draw_start_menu(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 60)
    button_font = pygame.font.Font(None, 70)
    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Animal Crossing Town Tune", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    start_text = button_font.render("Start", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))

    # Initialize button background color and text
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    start_surface.fill(LINE_COLOR)
    start_surface.blit(start_text, (10, 10))

    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    # Initialize button rectangle
    start_rectangle = start_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 25))
    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))

    # Draw buttons
    screen.blit(start_surface, start_rectangle)
    screen.blit(quit_surface, quit_rectangle)
    # Loop so the buttons work
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rectangle.collidepoint(event.pos):
                    mode = 1  # start game
                    return mode
                elif quit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


def draw_tune_screen(screen):
    screen.fill(BG_COLOR)
    title_font = pygame.font.Font(None, 80)
    title_surface = title_font.render("Town Tune", 0, LINE_COLOR)
    pygame.draw.line(screen, LINE_COLOR, (10, 90), (590, 90), 5)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 250))
    screen.blit(title_surface, title_rectangle)
    button_font = pygame.font.Font(None, 50)

    main_menu_text = button_font.render('Main Menu', 0, (255, 255, 255))
    main_menu_surface = pygame.Surface((main_menu_text.get_size()[0] + 20, main_menu_text.get_size()[1] + 20))
    main_menu_surface.fill(LINE_COLOR)
    main_menu_surface.blit(main_menu_text, (10, 10))
    main_menu_rectangle = main_menu_surface.get_rect(center=(180, 560))
    screen.blit(main_menu_surface, main_menu_rectangle)

    quit_text = button_font.render('Quit', 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))
    quit_rectangle = quit_surface.get_rect(center=(450, 560))
    screen.blit(quit_surface, quit_rectangle)
    pygame.display.update()
    return main_menu_rectangle, quit_rectangle


if __name__ == '__main__':
    while True:
        pygame.init()
        pygame.display.set_caption('Animal Crossing Town Tune')
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BG_COLOR)
        start = draw_start_menu(screen)
        buttons = draw_tune_screen(screen)
        restart = False
        sound_arr = SoundArr(screen)
        SoundArr.draw_sound_arr(sound_arr, screen)
        pygame.display.update()

        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if buttons[0].collidepoint(event.pos):
                        restart = True
                    elif buttons[1].collidepoint(event.pos):
                        sys.exit()
