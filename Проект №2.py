import os
import pygame
import sys
import random


pygame.init()
font = pygame.font.SysFont('Arial', 25)
fps = 50
gravity = 0.010
name_paint = "star1.png"
phon_color = "#7fc7ff"

size = width, height = 400, 600
screen = pygame.display.set_mode(size)

objects = []
screen_number = 0

texts = {
    0: [['КВЕСТ'], ['НАЧАТЬ!'], True],
    1: [['Вы плохо помните, что с вами случилось.', 'Сейчас Вы в темной комнате.', 'Личных вещи,кроме одежды, пропали,', 'вам необходимо отсюда выбраться'],
        ['Обыскать комнату', 'Звать на помощь', 'Ожидать спасения', 2, 100, 1000], True],
    100: [['Во время ваших поисков помощи,', 'вам удалось найти люк в полу.'],
           ['Открыть люк', 'Оставить люк', 101, 1], True],
    101: [['Крышка не была заперта,', 'под ней вы видите', 'черную бездну без дна'],
           ['Осторожно спрыгнуть', 'Спрыгнуть с разбегом', 'Закрыть люк', 102, 102, 1], True],
    102: [['Вы летите уже несколько минут,', 'всё набирая скорость.'],
           ['А-А-А-А!', 'А-А-А-А-А-А!', 'А-А-А-А-А-А-А-А!', 103, 103, 103], True],
    103: [['Спустя какое-то время,', 'вы влетаете в землю.', 'Летально.'],
           ['Вернуться в Главное Меню', 0], True],
    1000: [['Вы сели на пол и терпеливо ждёте,', 'пока кто-нибудь ваc здесь не найдёт  ', 'и поможет отсюда выбраться'],
           ['Обыскать комнату', 'Звать на помощь', 'Терпеливо ждать помощи', 2, 100, 1001], True],
    1001: [['Вы  уже несколько часов сидите,', 'ничего не делая.', 'Это черезвычайно скучно!'],
           ['Обыскать комнату', 'Звать на помощь', 'Превозмогая всё, ждать', 2, 100, 1002], True],
    1002: [['Прошёл день, может два:', 'вы не знаете, всё, как в тумане.', 'Нестерпимо хочется пить'],
           ['Ожидать спасения...', 1003], True],
    1003: [['Так и не дождавшись помощи,', 'вы погибли от обезвоживания,', 'совершенно один,', 'в этой мрачной комнате'],
           ['Вернуться в Главное Меню', 0], True],
    2: [['Обыскав комнату,', 'в одной из стен вы нашли углубление.', 'Ощупав его внимательнеее,', 'оказалось, что это - дверь!'],
        ['Войти в дверь', 'Вернуться обратно', 3, 1], True],
    3: [['Дверь вам не поддаётся'], ['Выломать дверь', 'Снять дверь', 'Вскрыть дверь', 4, 4, 4], True],
    4: [['Пройдя через дверь,', 'вы оказываетесь в новой комнате.', 'Позади вас закрывается решетка,', 'блокируя проход назад.'],
        ['Осмотреть новую комнату', 'Попытаться сломать решетку', 6, 5], True],
    5: [['Несмотря на все ваши попытки,', 'на решетке не осталось и следа.'],
        ['Осмотреть новую комнату', 6], True],
    6: [['Вы попали в очень просторную комнату.', 'Она хорошо освещена пламенем,', 'вырывающемся из прохода напротив вас.', 'Левее, проход,уходящий вниз,', 'заполненный водой', 'Правее, проход, заставленный трубами'],
        ['Левый коридор', 'Центральный коридор', 'Правый коридор', 8, 2000, 7], True],
    7: [['Весь проход плотно заставлен трубами,', 'по-видимому, медными.', 'Они сварены между собой, поэтому', "освободить проход не получится"],
        ['Левый коридор', 'Центральный коридор', 8, 2000], True],
    2000: [['Подгадывая нужный момент,', 'вы вбегаете в коридор.', 'Однако не пробежав и половины,', 'вас окутывают языки пламени...'],
           ['А-А-А-А-А-А-А....', 0], True],
    8: [['Коридор, хоть и шёл по водой,', 'был достаточно коротким.', 'Вы быстро проплываете', "и оказываетесь в новом помещении."],
        ['Ух....', 9], True],
    9: [['В комнату ведут все три коридора.', 'На противоположной стене', 'вы заметили табличку,', "а рядом с ней проход."],
        ['Прочесть табличку', 'Войти в проход', 'Высушить одежу у огня', 10, 12, 11], True],
    11: [['Вы посидели несколько минут', 'около центрального прохода с огнем.', 'Теперь вы не мокрые..'],
        ['Прочесть табличку', 'Войти в проход', 10, 12], True],
    10: [['На табличке написано:', '"ВХОД В ЛАБИРИНТ"'],
        ['Войти в лабиринт', 12], True],
    12: [['Темно.', 'Вы видите несколько проходов,'],
        ['Налево', 'Вперед', 'Направо', 14, 15, 13], True],
    13: [['Темно.', 'Идя некоторое время вы чуствуете:,', 'из под ног пропадает земля.'],
        ['А-А-А-А!',  102], True],
    14: [['Абсолютная тьма.', 'Вы хотите вернуться,', 'но не можете найти дорогу', 'Вы потерялись.', 'Это конец...'],
        ['Вернуться в Главное Меню',  0], True],
    15: [['Темно.', 'Похоже, вы вернулись в начало'],
        ['Налево', 'Вперед', 'Направо', 14, 16, 13], True],
    16: [['Пройда вперед ещё раз и вернувшись,', 'на месте входа в лабиринт - ПОРТАЛ.'],
        ['Войти в ПОРТАЛ', 17], True],
    17: [['ВЫ ВЫБРАЛИСЬ НА СВОБОДУ!'],
        ['ПОБЕДА!!', 0], True],


}


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
        image.set_alpha(10)
    return image


all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

pygame.mixer.music.load('data/phon.mp3')
pygame.mixer.music.play(-1)
click_s = pygame.mixer.Sound('data/click.mp3')
fire_s = pygame.mixer.Sound('data/fire.mp3')
scream = pygame.mixer.Sound('data/scream.mp3')
fanfari = pygame.mixer.Sound('data/fafari.mp3')

screen_rect = (0, 0, width, height)


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star1.png", -1)]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos

        self.gravity = gravity

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, n=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.n = n

        self.fillColors = {
            'normal': '#228B22',
            'hover': '#006400',
            'pressed': '#556B2F',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                click_s.play()
                if self.onePress:
                    self.onclickFunction(self.n)
                elif not self.alreadyPressed:
                    self.onclickFunction(self.n)
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def myFunction(n):
    print(n)
    global screen_number
    global objects
    objects = []
    clock.tick(2)
    if screen_number == 102:
        scream.play()
    elif screen_number == 16:
        fanfari.play()
    screen_number = n
    texts[screen_number][2] = True
    autosave(screen_number)


def starting(n):
    global screen_number
    global objects
    objects = []
    clock.tick(2)
    screen_number = 1
    texts[screen_number][2] = True
    autosave(screen_number)


def autosave(n):
    os.system(r'nul>data/autosave.txt')
    f = open('data/autosave.txt', 'w')
    n = str(n)
    f.write(n)
    f.close()


def load(n):
    global screen_number
    global objects
    objects = []
    f = open('data/autosave.txt', 'r')
    clock.tick(2)
    screen_number = int(f.read())
    f.close()


def start_screen(screen_number):
    intro_text = texts[screen_number][0]
    if screen_number == 0:
        text_f = pygame.font.SysFont('Times', 70)
        text_coord = 50
        for line in intro_text:
            string_rendered = text_f.render(line, 1, pygame.Color('black'), )
            screen.blit(string_rendered, (90, 100))
        if texts[screen_number][2]:
            Button(50, 350, 300, 50, texts[screen_number][1][0], starting, True)
            texts[screen_number][2] = False
    else:
        text_f = pygame.font.SysFont('Arial', 20)
        text_coord = 50
        for line in intro_text:
            if screen_number == 14:
                string_rendered = text_f.render(line, 1, pygame.Color('white'))
            else:
                string_rendered = text_f.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        if texts[screen_number][2]:
            n = 0
            num = 0
            leng = len(texts[screen_number][1]) // 2
            for btns in texts[screen_number][1][:leng]:
                Button(10, 325 + n, 380, 50, btns, myFunction, True, texts[screen_number][1][num + leng])
                num += 1
                n += 75

            texts[screen_number][2] = False


f = open('data/autosave.txt','r')
if f.read() != '0':
    Button(105, 300, 185, 40, 'Продолжить...', load, True)
f.close()

all_sprites = pygame.sprite.Group()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        if random.randint(1, 10) == 3:
            create_particles((random.randint(1, width), random.randint(1, height)))

        if screen_number == 1000:
            pygame.mixer.music.set_volume(0.50)
            phon_color = "#1faee9"
        elif screen_number == 1001:
            pygame.mixer.music.set_volume(0.25)
            phon_color = "#0099cc"
        elif screen_number == 1002:
            pygame.mixer.music.set_volume(0.1)
            phon_color = "#007399"
        elif screen_number == 1003:
            pygame.mixer.music.set_volume(0)
            phon_color = "#002633"
        elif screen_number == 0:
            pygame.mixer.music.set_volume(1)
            phon_color = "#7fc7ff"
            fire_s.stop()
        elif screen_number == 2:
            pygame.mixer.music.set_volume(1)
            phon_color = "#7fc7ff"
        elif screen_number == 2000:
            phon_color = "#f05d22"
            pygame.mixer.music.set_volume(0.20)
            fire_s.play()
        elif screen_number == 102:
            pygame.mixer.music.set_volume(0)
            phon_color = "#022027"
        elif screen_number == 103:
            pygame.mixer.music.set_volume(0)
            phon_color = "#022027"
        elif screen_number == 12 or screen_number == 13 or screen_number == 14 or screen_number == 15 or screen_number == 16:
            pygame.mixer.music.set_volume(0)
            phon_color = "#121910"
        elif screen_number == 17:
            pygame.mixer.music.set_volume(0)
            phon_color = "#ffffff"

    all_sprites.update()
    screen.fill(pygame.Color(phon_color))
    all_sprites.draw(screen)
    start_screen(screen_number)
    for object in objects:
        object.process()
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()