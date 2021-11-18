import pygame
import random
import constants

positions = {
    (1, 1): 0, (2, 1): 0, (3, 4): 0, (4, 4): 0,
    (1, 2): 0, (2, 2): 0, (3, 3): 0, (4, 3): 0,
    (1, 3): 0, (2, 3): 0, (3, 2): 0, (4, 2): 0,
    (1, 4): 0, (2, 4): 0, (3, 1): 0, (4, 1): 0
}

pygame.font.init()
font = pygame.font.SysFont("Calibri", 42)


def drawblock(x, y, num):
    x = (x - 1) * 128
    y = (y - 1) * 128
    pygame.draw.rect(window, constants.BLUE, pygame.Rect(x, y, 128, 128))
    text = font.render(str(num), True, constants.BLACK)
    text_rect = text.get_rect()
    text_rect.center = (x + 64, y + 64)
    window.blit(text, text_rect)


def newblock():
    options = []
    for i in positions.items():
        if 0 in i:
            options.append(i[0])
    coords = random.choice(options)
    print(coords)
    num = random.choice((2, 4))


newblock()


def main():
    while True:
        window.fill(constants.BG_COL)
        drawblock(1, 1, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.Clock().tick(constants.FPS)


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("2048 av Verner Lindskog")
    icon = pygame.image.load("imgs/2048_logo.png")
    pygame.display.set_icon(icon)
    main()
