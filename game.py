import pygame
import colours as c
from pygame.locals import QUIT


def printtext(text, text_col, bg_col=None):
    textobj = font.render


def printbuttons():

    _2048 = small_font.render(" 2048 ", True, c.BLACK, c.BLUE)
    _2048_rect = _2048.get_rect()
    _2048_rect.center = (c.WIDTH // 2, c.HEIGHT // 2)
    window.blit(_2048, _2048_rect)


def main_menu():
    while True:
        window.fill(c.BG_COL)
        printbuttons()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
        pygame.display.update()
        pygame.time.Clock().tick(c.FPS)


if __name__ == "__main__":
    pygame.init()
    big_font = pygame.font.SysFont(c.my_font, 42)
    small_font = pygame.font.SysFont(c.my_font, 20)
    window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("2048 av Verner Lindskog")
    icon = pygame.image.load("imgs/2048_logo.png")
    pygame.display.set_icon(icon)
    main_menu()