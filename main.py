import pygame
from pygame.locals import (K_w, K_a, K_s, K_d, K_ESCAPE, KEYDOWN, QUIT)
import random
import constants

# Definiera en lista som har koll på spel-positionen
positions = {
    (1, 1): 0, (2, 1): 0, (3, 4): 0, (4, 4): 0,
    (1, 2): 0, (2, 2): 0, (3, 3): 0, (4, 3): 0,
    (1, 3): 0, (2, 3): 0, (3, 2): 0, (4, 2): 0,
    (1, 4): 0, (2, 4): 0, (3, 1): 0, (4, 1): 0
}
gameisover = False


def drawblock(x, y, num):
    x = (x - 1) * 128
    y = (y - 1) * 128
    pygame.draw.rect(window, constants.block_colour(num), pygame.Rect(x, y, 128, 128))
    text = font.render(str(num), True, constants.BLACK)
    text_rect = text.get_rect()
    text_rect.center = (x + 64, y + 64)
    window.blit(text, text_rect)


def game_over():
    global gameisover
    game_over_text = font.render("Game Over!", True, constants.GAMEOVER_COL)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (constants.WIDTH // 2, constants.HEIGHT // 2)
    window.blit(game_over_text, game_over_text_rect)
    gameisover = True


def newblock():
    # Kollar lediga rutor
    options = []
    for i in positions.items():
        if 0 in i:
            options.append(i[0])
    if not options:
        game_over()
        return False
    coords = random.choice(options)
    num = random.choice((2, 4))
    drawblock(*coords, num)
    # Lägg till värdet i positions-listan
    positions[coords] = num


# merge blocks
def up():
    pass


def left():
    pass


def down():
    pass


def right():
    pass


def main():
    while True:
        window.fill(constants.BG_COL)

        for block in positions:
            if positions[block] != 0:
                drawblock(*block, positions[block])
        if gameisover:
            game_over()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w:
                    up()
                    newblock()
                elif event.key == K_a:
                    left()
                    newblock()
                elif event.key == K_s:
                    down()
                    newblock()
                elif event.key == K_d:
                    right()
                    newblock()
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        pygame.time.Clock().tick(constants.FPS)


if __name__ == "__main__":
    pygame.init()
    font = pygame.font.SysFont(constants.my_font, 42)
    window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("2048 av Verner Lindskog")
    icon = pygame.image.load("imgs/2048_logo.png")
    pygame.display.set_icon(icon)
    main()
