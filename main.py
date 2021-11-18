import pygame
import random
import constants


WIDTH, HEIGHT = 512, 512
BG_COL = (128, 152, 183)
BLUE = (0, 0, 128)
positions = [
    {(1, 4): None, (2, 4): None, (3, 4): None, (4, 4): None},
    {(1, 3): None, (2, 3): None, (3, 3): None, (4, 3): None},
    {(1, 2): None, (2, 2): None, (3, 2): None, (4, 2): None},
    {(1, 1): None, (2, 1): None, (3, 1): None, (4, 1): None}
]
pygame.font.init()
font = pygame.font.SysFont("Calibri", 42)


def drawblock(x, y):
    num = random.choice((2, 4))
    x = (x - 1) * 128
    y = (y - 1) * 128
    pygame.draw.rect(window, constants.BLUE, pygame.Rect(x, y, 128, 128))
    text = font.render(str(num), True, constants.BLACK)
    text_rect = text.get_rect()
    text_rect.center = (x + 64, y + 64)
    window.blit(text, text_rect)


def newblock():
    enumerate


newblock()
def main():
    while True:
        window.fill(constants.BG_COL)
        drawblock(4, 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.Clock().tick(constants.FPS)


'''
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("2048 av Verner Lindskog")
    icon = pygame.image.load("imgs/2048_logo.png")
    pygame.display.set_icon(icon)
    main()
'''