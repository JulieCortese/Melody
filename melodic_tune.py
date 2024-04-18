import sys
from musicpy import *
import pygame.font

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
    title_surface = start_title_font.render("Melody", 0, LINE_COLOR)
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


def draw_note_options(screen, octave):
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
    octave_surf = note_font.render(str(octave), 0, (0, 0, 0))
    octave_rect = octave_surf.get_rect(center=(70, 380))
    screen.blit(octave_surf, octave_rect)

    # now to add the up and down octaves buttons
    octave_up_img = pygame.image.load('octave-up.png')
    screen.blit(octave_up_img, (20, 360))
    octave_up_rect = octave_up_img.get_rect(topleft=(20, 360))
    octave_down_img = pygame.image.load('octave-down.png')
    screen.blit(octave_down_img, (90, 360))
    octave_down_rect = octave_down_img.get_rect(topleft=(90, 360))

    # and for the sharp flat and natural options
    sharp_img = pygame.image.load('sharp.png')
    screen.blit(sharp_img, (240, 360))
    sharp_rect = sharp_img.get_rect(topleft=(240, 360))
    natural_img = pygame.image.load('natural.png')
    screen.blit(natural_img, (280, 360))
    natural_rect = natural_img.get_rect(topleft=(280, 360))
    flat_img = pygame.image.load('flat.png')
    screen.blit(flat_img, (320, 365))
    flat_rect = flat_img.get_rect(topleft=(320, 365))

    # make box for note options to be in
    pygame.draw.line(screen, (0, 0, 0), (20, 400), (580, 400))
    pygame.draw.line(screen, (0, 0, 0), (20, 400), (20, 460))
    pygame.draw.line(screen, (0, 0, 0), (20, 460), (580, 460))
    pygame.draw.line(screen, (0, 0, 0), (580, 460), (580, 400))
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
    screen.blit(rest_img, (400, 410))
    rest_rect = rest_img.get_rect(topleft=(400, 410))

    # the arrows should let the player navigate through screens
    left_ar_img = pygame.image.load('left_arrow.png')
    left_rect = left_ar_img.get_rect(center=(30, 500))
    screen.blit(left_ar_img, left_rect)
    right_ar_img = pygame.image.load('right_arrow.png')
    right_rect = right_ar_img.get_rect(center=(560, 500))
    screen.blit(right_ar_img, right_rect)

    # numbering the screens lets the player know the order the notes will go in
    screen_num_surf = note_font.render(f'screen {screen_num}', 0, (0, 0, 0))
    screen_num_rect = screen_num_surf.get_rect(center=(300, 500))
    screen.blit(screen_num_surf, screen_num_rect)
    high_c_surf = note_font.render('^C', 0, (0, 0, 0))
    high_c_rect = high_c_surf.get_rect(center=(350, 430))
    screen.blit(high_c_surf, high_c_rect)
    return (c_rect, d_rect, e_rect, f_rect, g_rect, a_rect, b_rect, rest_rect, left_rect,
            right_rect, high_c_rect, octave_up_rect, octave_down_rect, sharp_rect, natural_rect,
            flat_rect)
    # (actually I don't have audio files for flats and sharps, so it's all natural for now)


def draw_tune_screen(screen):
    screen.fill(BG_COLOR)
    title_font = pygame.font.Font(None, 80)
    title_surface = title_font.render("Melodic Tune", 0, LINE_COLOR)
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
        pygame.display.set_caption('Melody')
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BG_COLOR)
        start = draw_start_menu(screen)
        buttons = draw_tune_screen(screen)
        restart = False
        sound_arr = SoundArr(screen)
        screen_num = 1
        screens = 1
        octave = 4
        accidental = 0
        SoundArr.draw_sound_arr(sound_arr, screen, screen_num)
        note_options = draw_note_options(screen, octave)
        pygame.display.update()
        screen_num = 1

        while not restart:
            """
            if screens > 1 and screen_num < screens:
                # load right arrow image and blit it onscreen (how to make clickable if may or may not exist?)
                # screen_num changes when arrow clicked, screen changes when arrow clicked
                right_arrow_surf = pygame.image.load('right_arrow.png')
                right_arrow_rect = right_arrow_surf.get_rect(center=(30, 70))
                screen.blit(right_arrow_surf, right_arrow_rect)
            elif screens > 1 and screen_num > 1:
                # load left arrow and blit (same problem above) and same results above
                left_arrow_surf = pygame.image.load('left_arrow.png')
                """
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
                        # clicked backspace
                        back = 0
                        for i in range(len(sound_arr.sound_arr) - 1, -1, -1):
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
                                    SoundArr.draw_sound_arr(sound_arr, screen, screen_num)
                                    pygame.display.update()
                                    back = 1
                                    break
                    elif buttons[3].collidepoint(event.pos):
                        # clicked play tune
                        for i in range(len(sound_arr.sound_arr)):
                            for j in range(6):
                                if sound_arr.notes[i][j].sound is not None and sound_arr.sound_arr[i][j] != 'rest':
                                    pygame.mixer.Sound.play(sound_arr.notes[i][j].sound)
                                    pygame.time.wait(300)
                                elif sound_arr.sound_arr[i][j] == 'rest':
                                    pygame.time.wait(600)
                    elif note_options[0].collidepoint(event.pos):
                        # clicked C
                        sound = pygame.mixer.Sound('c4.mp3')
                        pygame.mixer.Sound.play(sound)
                        sound = 'c4.mp3'
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, 'C', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[1].collidepoint(event.pos):
                        # clicked D
                        sound = pygame.mixer.Sound('d4.mp3')
                        pygame.mixer.Sound.play(sound)
                        sound = 'd4.mp3'
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, 'D', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[2].collidepoint(event.pos):
                        # clicked E
                        sound = pygame.mixer.Sound('e4.mp3')
                        pygame.mixer.Sound.play(sound)
                        sound = 'e4.mp3'
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, 'E', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[3].collidepoint(event.pos):
                        # clicked F
                        sound = pygame.mixer.Sound('f4.mp3')
                        pygame.mixer.Sound.play(sound)
                        sound = 'f4.mp3'
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, 'F', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[4].collidepoint(event.pos):
                        # clicked G
                        sound = pygame.mixer.Sound('g4.mp3')
                        pygame.mixer.Sound.play(sound)
                        sound = 'g4.mp3'
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, 'G', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[5].collidepoint(event.pos):
                        # clicked A
                        sound = pygame.mixer.Sound('a4.mp3')
                        pygame.mixer.Sound.play(sound)
                        sound = 'a4.mp3'
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, 'A', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[6].collidepoint(event.pos):
                        # clicked B
                        sound = pygame.mixer.Sound('b4.mp3')
                        pygame.mixer.Sound.play(sound)
                        sound = 'b4.mp3'
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, 'B', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[7].collidepoint(event.pos):
                        # clicked rest
                        sound = None
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, 'rest', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[8].collidepoint(event.pos):
                        # left arrow clicked
                        if screens > 1 and screen_num > 1:
                            screen_num -= 1
                            screen.fill((255, 245, 218))
                            buttons = draw_tune_screen(screen)
                            note_options = draw_note_options(screen)
                            SoundArr.draw_sound_arr(sound_arr, screen, screen_num)
                            pygame.display.update()
                    elif note_options[9].collidepoint(event.pos):
                        # right arrow clicked
                        if screens > 1 and screen_num < screens:
                            screen_num += 1
                            screen.fill((255, 245, 218))
                            buttons = draw_tune_screen(screen)
                            note_options = draw_note_options(screen)
                            SoundArr.draw_sound_arr(sound_arr, screen, screen_num)
                            pygame.display.update()
                    elif note_options[10].collidepoint(event.pos):
                        # clicked high C
                        sound = pygame.mixer.Sound('c5.mp3')
                        pygame.mixer.Sound.play(sound)
                        sound = 'c5.mp3'
                        screens_temp = screens
                        screens = SoundArr.add_note(sound_arr, '^C', sound, screens, screen_num)
                        if screens is None:
                            screens = screens_temp
                    elif note_options[11].collidepoint(event.pos):
                        print('octave up')
                        if octave < 8:
                            octave += 1
                        else:
                            print('highest possible octave')
                    elif note_options[12].collidepoint(event.pos):
                        print('octave down')
                        if octave > 0:
                            octave -= 1
                        else:
                            print('lowest possible octave')
                    elif note_options[13].collidepoint(event.pos):
                        print('sharp')
                    elif note_options[14].collidepoint(event.pos):
                        print('natural')
                    elif note_options[15].collidepoint(event.pos):
                        print('flat')
