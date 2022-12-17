from note import *


class SoundArr:
    def __init__(self, screen):
        self.name = 'sound array'
        self.sound_arr = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
        self.screen = screen
        self.notes = [[Note(self.sound_arr[i][j], i, j, self.screen) for j in range(6)] for i in range(2)]

    def draw_sound_arr(self, screen):
        # draws the lines the notes go on
        x_start = WIDTH // 2 - 250
        y_start = HEIGHT // 2 - 120
        for i in range(len(self.sound_arr)):
            for j in range(len(self.sound_arr[0])):
                pygame.draw.line(screen, (0, 0, 0), (x_start + j * 100, y_start + i * 150),
                                 (x_start + j * 100, y_start + i * 150), 50)
                # need to figure out how to display the sound array itself
                # need to add code to display the options for each sound
        # make box for note options to be in
        pygame.draw.line(screen, (0, 0, 0), (20, 400), (580, 400))
        pygame.draw.line(screen, (0, 0, 0), (20, 400), (20, 460))
        pygame.draw.line(screen, (0, 0, 0), (20, 460), (580, 460))
        pygame.draw.line(screen, (0, 0, 0), (580, 460), (580, 400))
        # draws notes in array
        note_font = pygame.font.Font(None, 50)
        for i in range(2):
            for j in range(6):
                self.notes[i][j].draw_note(self.screen)