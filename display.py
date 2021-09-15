import json
import sys

import pygame

with open('config.json') as config_file:
    data = json.load(config_file)

pygame.init()

WIN = pygame.display.set_mode((data['width'], data['height']))
pygame.display.set_caption(data['name'])
WIN.fill(data['colors']['BLACK'])

FONT = pygame.font.Font(None, 70)


class InputBox:

    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = data['colors']['INACTIVE']
        self.active = False
        self.text = text
        self.txt_surface = FONT.render(self.text, True, self.color)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 3:  # left or right click
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False

            self.color = data['colors']['ACTIVE'] if self.active else data['colors']['INACTIVE']

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    temp = self.text
                    self.text = ''
                    return temp
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.txt_surface = FONT.render(self.text, True, self.color)

        return None

    def update(self):
        width = max(data['width'] // 2, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        self.txt_surface = FONT.render(self.text, True, self.color)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


variables = {'paused': False}
input_box = InputBox(data['width'] // 4, data['height'] // 2, data['width'] // 2, data['height'] // 8)


def display_message(message):
    txt_surface = FONT.render(message, True, data['colors']['WHITE'])
    WIN.blit(txt_surface, (data['width'] // 3, data['height'] // 4))
    pygame.display.update()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            variables['paused'] = not variables['paused']


def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                return


def update(algorithm, swap1=None, swap2=None):
    WIN.fill(data['colors']['BLACK'])
    pygame.display.set_caption(f'Sorting Visualizer             Algortihm: {algorithm.name}')

    if not variables['paused']:
        bar_width = data['width'] // len(algorithm.data)
        clock = pygame.time.Clock()

        for i in range(len(algorithm.data)):
            color = data['colors']['WHITE']

            if swap1 == algorithm.data[i]:
                color = data['colors']['GREEN']
            elif swap2 == algorithm.data[i]:
                color = data['colors']['RED']

            pygame.draw.rect(WIN, color,
                             (i * bar_width, data['height'] - algorithm.data[i], bar_width, algorithm.data[i]))

        clock.tick(500)
        check_events()
        pygame.display.update()

    else:
        wait()
        variables['paused'] = False
