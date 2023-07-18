# Генерація випадкових чисел
import random
from os import listdir
# Бібліотека
import pygame
# Виклик різних подій, таких як: закрити вікно та клавіш стрілок клавіатури
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

# Ініціалізація pygame
pygame.init()

# Створення FPS
FPS = pygame.time.Clock()

# Розмір полігону
screen = WIDTH, HEIGHT = 800, 600

# Визначення кольорів, які використовуються у грі за допомогою кодів RGB.
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

# Шлях до папки "goose"
IMGS_PATH = 'goose'

# Ви створюєте об'єкти шрифту для відображення тексту на екрані.
font = pygame.font.SysFont('Verdana', 20)
score_font = pygame.font.SysFont('Verdana', 20, True)

# Головна поверхня для відображення гри з встановленими розмірами.
main_surface = pygame.display.set_mode(screen)

# Завантаження зображення з папки "goose", конвертація його за допомогою модуля альфа-канал, швидкість "ball"
ball_imgs = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in listdir(IMGS_PATH)]
ball = ball_imgs[0]
ball_rect = ball.get_rect()
ball_speed = 5

# Початковий індекс для зміни зображеннь
ing_index = 0

# Порожні списки для ворогів та бонусів
enemies = []
bonuses = []

# Завантаження зображення фону, маштабування до розмірів полігону
# Встановлене початкове значення для зміщення фону та лічильника очок
bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bgx = 0
bgx2 = bg.get_width()
bg_speed = 3
scores = 0

# Функція яка створює ворога, завантаження зображення в форматі PNG
# Масштаб ворога, генерація випадкового значення для положення та швидкості ворога
def create_enemy():
    enemy = pygame.transform.scale(pygame.image.load('enemy.png').convert_alpha(),(80, 40))
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

# Функція яка створює бонус, завантаження зображення в форматі PNG
# Масштаб бонусу, генерація випадкового значення для положення та швидкості бонусу
def create_bonus():
    bonus = pygame.transform.scale(pygame.image.load('bonus.png').convert_alpha(),(120, 120))
    bonus_rect = pygame.Rect(random.randint(0, WIDTH - bonus.get_width()), - bonus.get_height(), *bonus.get_size())
    bonus_speed = random.randint(1, 2)
    return [bonus, bonus_rect, bonus_speed]

# Встановлені таймери для створення ворогів, бонусів та анімація головного персонажу
CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1000)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)

is_working = True

while is_working:

# Швидкісь кадрів (FPS)
    FPS.tick(60)
# Головний цикл
# Перевірка, чи відбувається подія QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
# Перевірка чи відбувається подія CREATE_ENEMY, створення нового ворога
        elif event.type == CREATE_ENEMY:
            enemies.append(create_enemy ())
# Перевірка чи відбувається подія CREATE_BONUS, створення нового бонусу
        elif event.type == CREATE_BONUS:
            bonuses.append(create_bonus ())
# Анімація
        if event.type == CHANGE_IMG:
            ing_index += 1
            if ing_index == len(ball_imgs):
                ing_index = 0
            ball = ball_imgs[ing_index]
# Обробка руху персонажу відповідно до натискання на клавіші
    pressed_keys = pygame.key.get_pressed()

# Рух background
    bgx -= bg_speed
    bgx2 -= bg_speed
# Перевірка чи вийшов background за межі, створює ефект руху background по колу
    if bgx < - bg.get_width():
        bgx = bg.get_width()

    if bgx2 < -bg.get_width():
        bgx2 = bg.get_width()
# Відображення двох екземплярів тла на головній поверхні. Це створює ефект неперервного руху тла зліва направо.
    main_surface.blit(bg, (bgx, 0))

    main_surface.blit(bg, (bgx2, 0))
# Відображення зображення персонажу на головній поверхні
    main_surface.blit(ball, ball_rect)
# Відображення тексту рахунку у верхньому правому куті на головної поверхні.
    main_surface.blit(font.render(str(scores), True, GREEN), (WIDTH - 30, 0))

# У цьому циклі проходить рух ворога
    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])
# Видалення воррога зі списку коли він досягає лівого краю екрану, щоб список не збільшувався та не зависла гра
        if enemy[1].left < 0:
            enemies.remove(enemy)
# Перевірка на зіткнення героя з ворогом, якщо так то гра завершина
        if ball_rect.colliderect(enemy[1]):
            is_working = False
# У цьому циклі проходить рух бонусу
    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])
# Видалення бонусу зі списку, щоб список не збільшувався та не зависла гра
        if bonus[1].bottom >= HEIGHT:
            bonuses.remove(bonus)
# Перевірка зіткнення з персонажем і збільшення лічильника очок на одиницю
        if ball_rect.colliderect(bonus[1]):
            bonuses.remove(bonus)
            scores += 1
# Перевірка, чи відповідають натискання клавіш руху персонажу, умова "not" превіряє чи не досягнуто меж полігону
    if pressed_keys[K_DOWN] and not ball_rect.bottom >= HEIGHT:
        ball_rect = ball_rect.move(0, ball_speed)

    if pressed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move(0, -ball_speed)

    if pressed_keys[K_RIGHT] and not ball_rect.right >= WIDTH:
        ball_rect = ball_rect.move(ball_speed, 0)

    if pressed_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move(-ball_speed, 0)

# Перевірки, чи дійсно працює remove (видалення ворогів та бонусів), після того як вони претинають межі полігону
    print(len(enemies))
    print(len(bonuses))
# Оновлення вікна гри, тобто відображення усіх змін
    pygame.display.flip()
