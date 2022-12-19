import sys

import pygame.font

# import vlc
from constants import *
from note import *
from sound_arr import *

# sounds = [pygame.mixer.Sound('')]

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


def draw_note_options(screen):
    note_font = pygame.font.Font(None, 60)
    c_surf = note_font.render('C', 0, (0, 0, 0))
    c_rect = c_surf.get_rect(center=(60, 430))
    screen.blit(c_surf, c_rect)
    d_surf = note_font.render('D', 0, (0, 0, 0))
    d_rect = d_surf.get_rect(center=(100, 430))
    screen.blit(d_surf, d_rect)
    e_surf = note_font.render('E', 0, (0, 0, 0))
    e_rect = e_surf.get_rect(center=(140, 430))
    screen.blit(e_surf, e_rect)
    f_surf = note_font.render('F', 0, (0, 0, 0))
    f_rect = f_surf.get_rect(center=(180, 430))
    screen.blit(f_surf, f_rect)
    g_surf = note_font.render('G', 0, (0, 0, 0))
    g_rect = g_surf.get_rect(center=(220, 430))
    screen.blit(g_surf, g_rect)
    a_surf = note_font.render('A', 0, (0, 0, 0))
    a_rect = a_surf.get_rect(center=(260, 430))
    screen.blit(a_surf, a_rect)
    b_surf = note_font.render('B', 0, (0, 0, 0))
    b_rect = b_surf.get_rect(center=(300, 430))
    screen.blit(b_surf, b_rect)
    """
    sharp_surf = note_font.render('#', 0, (0, 0, 0))
    sharp_rect = sharp_surf.get_rect(center=(500, 430))
    screen.blit(sharp_surf, sharp_rect)
    flat_surf = note_font.render('b', 0, (0, 0, 0))
    flat_rect = flat_surf.get_rect(center=(440, 430))
    screen.blit(flat_surf, flat_rect)
    nat_img = pygame.image.load('natural.png')
    screen.blit(nat_img, (535, 410))
    """
    rest_img = pygame.image.load('rest.png')
    screen.blit(rest_img, (320, 410))
    return c_rect, d_rect, e_rect, f_rect, g_rect, a_rect, b_rect  # flat_rect, sharp_rect nat_img
    # (actually I don't have audio files for flats and sharps so it's all natural for now)


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

    smaller_button_font = pygame.font.Font(None, 30)
    play_text = smaller_button_font.render('Play Tune', 0, (255, 255, 255))
    play_surface = pygame.Surface((play_text.get_size()[0] + 20, play_text.get_size()[1] + 20))
    play_surface.fill(LINE_COLOR)
    play_surface.blit(play_text, (10, 10))
    play_rectangle = play_surface.get_rect(center=(505, 370))
    screen.blit(play_surface, play_rectangle)

    note_font = pygame.font.Font(None, 30)
    backspace_surface = note_font.render('Backspace', 0, (0, 0, 0))
    backspace_rectangle = backspace_surface.get_rect(center=(500, 430))
    screen.blit(backspace_surface, backspace_rectangle)
    pygame.display.update()
    return main_menu_rectangle, quit_rectangle, backspace_rectangle, play_rectangle


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
        note_options = draw_note_options(screen)
        pygame.display.update()
        accidental = 0  # natural

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
                    elif buttons[2].collidepoint(event.pos):
                        print('clicked backspace')
                        back = 0
                        for i in range(1, -1, -1):
                            if back == 1:
                                break
                            for j in range(5, -1, -1):
                                if sound_arr.sound_arr[i][j] != '-':
                                    sound_arr.sound_arr[i][j] = '-'
                                    sound_arr.notes[i][j].note = '-'
                                    sound_arr.notes[i][j].sound = None
                                    screen.fill((255, 245, 218))
                                    buttons = draw_tune_screen(screen)
                                    note_options = draw_note_options(screen)
                                    SoundArr.draw_sound_arr(sound_arr, screen)
                                    pygame.display.update()
                                    back = 1
                                    break
                    elif note_options[0].collidepoint(event.pos):
                        print('clicked C')
                        sound = pygame.mixer.Sound('c4.mp3')
                        pygame.mixer.Sound.play(sound)
                        yes = 0
                        for i in range(2):
                            if yes == 1:
                                break
                            for j in range(6):
                                if sound_arr.sound_arr[i][j] == '-':
                                    sound_arr.sound_arr[i][j] = 'C'
                                    sound_arr.notes[i][j].note = 'C'
                                    sound_arr.notes[i][j].sound = pygame.mixer.Sound('c4.mp3')
                                    SoundArr.draw_sound_arr(sound_arr, screen)
                                    pygame.display.update()
                                    yes = 1
                                    break
                        """
                        for i in range(2):
                            for j in range(6):
                                if sound_arr.notes[i][j].note == '-':
                                    sound_arr.notes[i][j].note = 'C'
                                    pygame.display.update()
                                    break
                        """
                    elif note_options[1].collidepoint(event.pos):
                        print('clicked D')
                        sound = pygame.mixer.Sound('d4.mp3')
                        pygame.mixer.Sound.play(sound)
                        yes = 0
                        for i in range(2):
                            if yes == 1:
                                break
                            for j in range(6):
                                if sound_arr.sound_arr[i][j] == '-':
                                    sound_arr.sound_arr[i][j] = 'D'
                                    sound_arr.notes[i][j].note = 'D'
                                    sound_arr.notes[i][j].sound = pygame.mixer.Sound('d4.mp3')
                                    SoundArr.draw_sound_arr(sound_arr, screen)
                                    pygame.display.update()
                                    yes = 1
                                    break
                    elif note_options[2].collidepoint(event.pos):
                        print('clicked E')
                        sound = pygame.mixer.Sound('e4.mp3')
                        pygame.mixer.Sound.play(sound)
                        yes = 0
                        for i in range(2):
                            if yes == 1:
                                break
                            for j in range(6):
                                if sound_arr.sound_arr[i][j] == '-':
                                    sound_arr.sound_arr[i][j] = 'E'
                                    sound_arr.notes[i][j].note = 'E'
                                    sound_arr.notes[i][j].sound = pygame.mixer.Sound('e4.mp3')
                                    SoundArr.draw_sound_arr(sound_arr, screen)
                                    pygame.display.update()
                                    yes = 1
                                    break
                    elif note_options[3].collidepoint(event.pos):
                        print('clicked F')
                        sound = pygame.mixer.Sound('f4.mp3')
                        pygame.mixer.Sound.play(sound)
                        yes = 0
                        for i in range(2):
                            if yes == 1:
                                break
                            for j in range(6):
                                if sound_arr.sound_arr[i][j] == '-':
                                    sound_arr.sound_arr[i][j] = 'F'
                                    sound_arr.notes[i][j].note = 'F'
                                    sound_arr.notes[i][j].sound = pygame.mixer.Sound('f4.mp3')
                                    SoundArr.draw_sound_arr(sound_arr, screen)
                                    pygame.display.update()
                                    yes = 1
                                    break
                    elif note_options[4].collidepoint(event.pos):
                        print('clicked G')
                        sound = pygame.mixer.Sound('g4.mp3')
                        pygame.mixer.Sound.play(sound)
                        yes = 0
                        for i in range(2):
                            if yes == 1:
                                break
                            for j in range(6):
                                if sound_arr.sound_arr[i][j] == '-':
                                    sound_arr.sound_arr[i][j] = 'G'
                                    sound_arr.notes[i][j].note = 'G'
                                    sound_arr.notes[i][j].sound = pygame.mixer.Sound('g4.mp3')
                                    SoundArr.draw_sound_arr(sound_arr, screen)
                                    pygame.display.update()
                                    yes = 1
                                    break
                    elif note_options[5].collidepoint(event.pos):
                        print('clicked A')
                        sound = pygame.mixer.Sound('a5.mp3')
                        pygame.mixer.Sound.play(sound)
                        yes = 0
                        for i in range(2):
                            if yes == 1:
                                break
                            for j in range(6):
                                if sound_arr.sound_arr[i][j] == '-':
                                    sound_arr.sound_arr[i][j] = 'A'
                                    sound_arr.notes[i][j].note = 'A'
                                    sound_arr.notes[i][j].sound = pygame.mixer.Sound('a5.mp3')
                                    SoundArr.draw_sound_arr(sound_arr, screen)
                                    pygame.display.update()
                                    yes = 1
                                    break
                    elif note_options[6].collidepoint(event.pos):
                        print('clicked B')
                        sound = pygame.mixer.Sound('b5.mp3')
                        pygame.mixer.Sound.play(sound)
                        yes = 0
                        for i in range(2):
                            if yes == 1:
                                break
                            for j in range(6):
                                if sound_arr.sound_arr[i][j] == '-':
                                    sound_arr.sound_arr[i][j] = 'B'
                                    sound_arr.notes[i][j].note = 'B'
                                    sound_arr.notes[i][j].sound = pygame.mixer.Sound('b5.mp3')
                                    SoundArr.draw_sound_arr(sound_arr, screen)
                                    pygame.display.update()
                                    yes = 1
                                    break
                    """
                    elif note_options[7].collidepoint(event.pos):
                        print('clicked flat')
                    elif note_options[8].collidepoint(event.pos):
                        print('clicked sharp')
                    """
