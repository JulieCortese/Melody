from note import *


class SoundArr:
    def __init__(self, screen):
        self.name = 'sound array'
        self.sound_arr = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
        self.screen = screen
        self.notes = [[Note(self.sound_arr[i][j], None, i, j, self.screen) for j in range(6)] for i in range(2)]

    def update_notes(self):
        outer_notes = []
        notes = []
        sound = ''
        for i in range(len(self.sound_arr)):
            for j in range(6):
                if self.sound_arr[i][j] == 'C':
                    sound = pygame.mixer.Sound('c4.mp3')
                elif self.sound_arr[i][j] == 'D':
                    sound = pygame.mixer.Sound('d4.mp3')
                elif self.sound_arr[i][j] == 'E':
                    sound = pygame.mixer.Sound('e4.mp3')
                elif self.sound_arr[i][j] == 'F':
                    sound = pygame.mixer.Sound('f4.mp3')
                elif self.sound_arr[i][j] == 'G':
                    sound = pygame.mixer.Sound('g4.mp3')
                elif self.sound_arr[i][j] == 'A':
                    sound = pygame.mixer.Sound('a5.mp3')
                elif self.sound_arr[i][j] == 'B':
                    sound = pygame.mixer.Sound('b5.mp3')
                elif self.sound_arr[i][j] == 'rest':
                    sound = None
                elif self.sound_arr[i][j] == '-':
                    sound = None
                notes.append(Note(self.sound_arr[i][j], sound, i, j, self.screen))
            outer_notes.append(notes)
            notes = []
        self.notes = outer_notes

    def add_note(self, note, sound, screens, screen_num):
        yes = 0
        not_full = 0
        for i in range(len(self.sound_arr)):
            if yes == 1:
                break
            for j in range(len(self.sound_arr[i])):
                if self.sound_arr[i][j] == '-':
                    not_full = 1
                    self.sound_arr[i][j] = note
                    self.notes[i][j].note = note
                    if sound is not None:
                        self.notes[i][j].sound = pygame.mixer.Sound(sound)
                    else:
                        self.notes[i][j].sound = None
                    SoundArr.draw_sound_arr(self, self.screen, screen_num)
                    pygame.display.update()
                    yes = 1
                    break
        if not_full == 0:
            screens += 1
            self.sound_arr.append([note, '-', '-', '-', '-', '-'])
            self.sound_arr.append(['-', '-', '-', '-', '-', '-'])
            self.update_notes()
            SoundArr.draw_sound_arr(self, self.screen, screen_num)
            pygame.display.update()
            print(screens)
            return screens

    def draw_sound_arr(self, screen, screen_num):
        x_start = WIDTH // 2 - 250
        y_start = HEIGHT // 2 - 120
        for i in range(2):
            for j in range(6):
                pygame.draw.line(screen, (0, 0, 0), (x_start + j * 100, y_start + i * 150),
                                 (x_start + j * 100, y_start + i * 150), 50)
        for i in range(screen_num - 1, screen_num + 1):
            for j in range(len(self.notes[i])):
                self.notes[i][j].draw_note(self.screen)
        """
        # draws the lines the notes go on
        for i in range(len(self.sound_arr)):
            for j in range(6):
                pygame.draw.line(screen, (0, 0, 0), (x_start + j * 100, y_start + i * 150),
                                 (x_start + j * 100, y_start + i * 150), 50)
                # need to figure out how to display the sound array itself
                # need to add code to display the options for each sound
        for i in range(len(self.notes)):
            for j in range(len(self.notes[i])):
                self.notes[i][j].draw_note(self.screen)
                """
