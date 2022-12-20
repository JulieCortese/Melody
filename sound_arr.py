from note import *


class SoundArr:
    def __init__(self, screen):
        self.name = 'sound array'
        self.sound_arr = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
        self.screen = screen
        self.notes = [[Note(self.sound_arr[i][j], None, i, j, self.screen) for j in range(6)] for i in range(2)]

    def update_notes(self):
        self.notes = [[Note(self.sound_arr[i][j], None, i, j, self.screen) for j in range(6)] for i in range(2)]

    def add_note(self, note, sound):
        yes = 0
        not_full = 0
        for i in range(len(self.sound_arr)):
            if yes == 1:
                break
            for j in range(6):
                if self.sound_arr[i][j] == '-':
                    not_full = 1
                    self.sound_arr[i][j] = note
                    self.notes[i][j].note = note
                    if sound is not None:
                        self.notes[i][j].sound = pygame.mixer.Sound(sound)
                    else:
                        self.notes[i][j].sound = None
                    SoundArr.draw_sound_arr(self, self.screen)
                    pygame.display.update()
                    yes = 1
                    break
        if not_full == 0:
            self.sound_arr.append([note, '-', '-', '-', '-', '-'])
            self.sound_arr.append(['-', '-', '-', '-', '-', '-'])
            self.update_notes()

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