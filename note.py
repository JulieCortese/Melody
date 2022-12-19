import pygame
from constants import *


class Note:
    def __init__(self, note, sound, row, col, screen):
        self.note = note
        self.sound = sound
        self.row = row
        self.col = col
        self.screen = screen

    def draw_note(self, screen):
        number_font = pygame.font.Font(None, 80)
        # changes 0s to empty strings so nothing displays
        if self.note == '-':
            self.note = ''
        elif self.note == 'rest':
            note_surf = pygame.image.load('rest.png')
            note_rect = note_surf.get_rect(center=(100 * self.col + SQUARE_SIZE // 4, 160 * self.row + 150))
            screen.blit(note_surf, note_rect)
        else:
            num_surf = number_font.render(str(self.note), 0, (0, 0, 0))
            chip_rect = num_surf.get_rect(
                center=(100 * self.col + SQUARE_SIZE // 4, 160 * self.row + 150))
            screen.blit(num_surf, chip_rect)
