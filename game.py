import pygame
import constants as c
from pygame.locals import (K_w, K_a, K_s, K_d, K_ESCAPE, KEYDOWN, QUIT)


def drawblock(x, y, num):
    x = x * 128
    y = y * 128
    pygame.draw.rect(window, c.block_colour(num), pygame.Rect(x, y, 128, 128))
    text = font.render(str(num), True, c.BLACK)
    text_rect = text.get_rect()
    text_rect.center = (x + 64, y + 64)
    window.blit(text, text_rect)


def main():
    while True:
        window.fill(c.BG_COL)
        drawblock(3, 1, 16)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    pygame.init()
    font = pygame.font.SysFont(c.my_font, 42)
    window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("2048 av Verner Lindskog")
    icon = pygame.image.load("imgs/2048_logo.png")
    pygame.display.set_icon(icon)
    main()
