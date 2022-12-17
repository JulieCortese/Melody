import pygame
from constants import *


class Note:
    def __init__(self, note, row, col, screen):
        self.note = note
        self.row = row
        self.col = col
        self.screen = screen

    def set_note_val(self, note):
        self.note = note

    def draw_note(self, screen):
        number_font = pygame.font.Font(None, 60)
        if self.note == '-':
            self.note = ''  # changes 0s to empty strings so nothing displays
        num_surf = number_font.render(str(self.note), 0, (0, 0, 0))
        chip_rect = num_surf.get_rect(
            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
        screen.blit(num_surf, chip_rect)
