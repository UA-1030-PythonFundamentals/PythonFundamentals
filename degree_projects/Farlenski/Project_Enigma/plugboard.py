import pygame
import string

class Plugboard:
    def __init__(self, pairs):
        self.left = string.ascii_uppercase
        self.right = string.ascii_uppercase
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A + 1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B + 1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def draw(self, screen, x, y, w, h, font):
        # rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=1, border_radius=7)

        # left side
        for i in range(26):

            # left side
            letter = self.left[i]
            letter = font.render(letter, True, 'grey')
            text_box = letter.get_rect(center=(x + w / 4, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)

            # right side
            letter = self.right[i]
            letter = font.render(letter, True, 'grey')
            text_box = letter.get_rect(center=(x + w * 3 / 4, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)