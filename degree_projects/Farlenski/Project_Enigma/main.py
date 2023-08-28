import pygame
import string
from draw import draw
from enigma import Enigma
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector

# setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma machine")

# create fonts
BOLD = pygame.font.SysFont("FreeMono", 12, bold=True)
MONO = pygame.font.SysFont("FreeMono", 12)

# global variables
WIDTH = 800
HEIGHT = 450
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {'top': 100, "bottom": 50, "left": 50, "right": 50}
GAP = 50
INPUT = ""
OUTPUT = ""
PATH = []

# historical enigma rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboard and plugboard
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

# #define enigma machine
ENIGMA = Enigma(B, I, II, III, PB, KB)

# set message key
ENIGMA.set_key("CAT")

animating = True
while animating:
    # background
    SCREEN.fill(("#333333"))

    # text input
    text = BOLD.render(INPUT, True, 'white')
    text_box = text.get_rect(center=(WIDTH/2, MARGINS['top']/3))
    SCREEN.blit(text, text_box)

    # text output
    text = MONO.render(OUTPUT, True, 'white')
    text_box = text.get_rect(center=(WIDTH/2, MARGINS['top']/3+10))
    SCREEN.blit(text, text_box)

    # draw enigma machine
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

    # update screens
    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                INPUT += " "
                OUTPUT += " "
            else:
                key = event.unicode
                if key in string.ascii_uppercase.lower():
                    letter = key.upper()
                    INPUT += letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT += cipher
