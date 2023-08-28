import pygame
import string


class Rotor:

    def __init__(self, wiring, notch):
        self.left = string.ascii_uppercase
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def rotate(self, n=1, forward=True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def rotate_to_letter(self, letter):
        n = string.ascii_uppercase.find(letter)
        self.rotate(n)

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

            # highlight top letter
            if i == 0:
                pygame.draw.rect(screen, 'teal', text_box, border_radius=2)

            # highlight turnover notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, "#333333")
                pygame.draw.rect(screen, 'white', text_box, border_radius=2)

            screen.blit(letter, text_box)

            # right side
            letter = self.right[i]
            letter = font.render(letter, True, 'grey')
            text_box = letter.get_rect(center=(x + w * 3 / 4, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)