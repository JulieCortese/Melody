import pygame
from constants import *

class Note:
    def __init__(self):
        self.note = 'C'

    def draw_note(self, screen):
        number_font = pygame.font.Font(None, 60)
        if self.value == 0:
            self.value = ''  # changes 0s to empty strings so nothing displays
        num_surf = number_font.render(str(self.value), 0, (0, 0, 0))
        chip_rect = num_surf.get_rect(
            center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
        screen.blit(num_surf, chip_rect)
