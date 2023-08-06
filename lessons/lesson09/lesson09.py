import pygame

pygame.init()

Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
Navy_Blue = (0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)

gameDisplay = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()
COLOR = [0, 0, 0]
done = False
e = 0
points = []
X = 0
def get_color():
    global e
    e += 10
    COLOR[0] = int(int(e / 255) / 255) % 255
    COLOR[1] = int(e / 255) % 255
    COLOR[2] = int(e % 255)
    # print(COLOR)


while not done:
    gameDisplay.fill(COLOR)
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True # Flag that we are done so we exit this loop
            # pygame.quit()
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        if event.type == pygame.KEYDOWN:
            if event.dict.get("key") == pygame.K_RIGHT:
                X += 5
            if event.dict.get("key") == pygame.K_LEFT:
                X -= 5
        if event.type == pygame.KEYUP:
            print("User let go of a key.")
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.dict.get("pos")
            points.append((x, y))
            print("User pressed a mouse button")
        if event.type == pygame.MOUSEMOTION:
            _x, _y = event.dict.get("pos")
            print(pygame.mouse.get_pos())
            pygame.draw.rect(gameDisplay, Maroon, [10+_x, 10+_y, 100, 100])


    pygame.draw.rect(gameDisplay, Red, [55+X, 50, 20, 25])
    pygame.draw.line(gameDisplay, Gray, [0, 0], [100, 100], 5)
    if len(points)> 3:
        pygame.draw.polygon(gameDisplay, Yellow, points)
    get_color()
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(120)
