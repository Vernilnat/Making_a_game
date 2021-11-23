import pygame
from pygame.locals import (K_w, K_UP, K_a, K_LEFT, K_s, K_DOWN, K_d, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_RCTRL)
import random
import constants as c
# ev. import json (for scores!)

# Definiera en lista som har koll på spel-positionen
positions = [[0] * 4 for i in range(4)]

# Variabler som används i spel-loopen senare...
gameisover = False
gameiswon = False
moved = False


def drawblock(x, y, num):
    x = x * 128
    y = y * 128
    pygame.draw.rect(window, c.block_colour(num), pygame.Rect(x, y, 128, 128))
    text = font.render(str(num), True, c.BLACK)
    text_rect = text.get_rect()
    text_rect.center = (x + 64, y + 64)
    window.blit(text, text_rect)


def game_over():
    global gameisover
    game_over_text = font.render("Game Over!", True, c.GAMEOVER_COL)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (c.WIDTH // 2, c.HEIGHT // 2)
    window.blit(game_over_text, game_over_text_rect)
    gameisover = True


def winscreen():
    global gameiswon
    win_text = font.render("You win!", True, c.BLACK)
    win_text_rect = win_text.get_rect()
    win_text_rect.center = (c.WIDTH // 2, c.HEIGHT // 2)
    window.blit(win_text, win_text_rect)
    gameiswon = True


def wincheck(win_tile):
    for row in positions:
        for i in row:
            if i == win_tile:
                winscreen()


def newblock(rep=1):
    # rep = antal repetitioner (till setup när man ska börja med 2 rutor)
    # Kollar om du redan vunnit
    wincheck(c.win_tile)

    for i in range(rep):
        # Kollar lediga rutor
        options = []
        for row in range(4):
            for column, value in enumerate(positions[row]):
                if value == 0:
                    options.append((column, row))
        coords = random.choice(options)
        num = random.choice((2, 4))
        # drawblock(*coords, num)
        # Lägg till värdet i positions-listan
        positions[coords[1]][coords[0]] = num
        # Kolla om användaren har förlorat, kolla ifall det finns några möjliga drag
        if len(options) < 2:
            if not mergecheck(positions):
                rotate_positions = []
                for i in range(4):
                    rotate_positions.append([positions[j][i] for j in range(4)])
                if not mergecheck(rotate_positions):
                    game_over()


# en sätta ihop funktion, resten av funktionerna justerar listorna så att merge()-funktionen fungerar på rätt sätt för
# de olika situationerna
def merge(merge_list):
    global moved
    # Spara listan för att kolla ifall något rör sig. Om inget rör sig ska inget nytt block skapas.
    original_list = merge_list[:]
    # Samla alla tal till vänster i listorna
    for row in range(4):
        merge_list[row] = [num for num in merge_list[row] if num != 0] + [0] * merge_list[row].count(0)
        # Addera ihop tal ifall det behövs
        prev_num = None
        for column, tile in enumerate(merge_list[row]):
            if tile == 0:
                break
            elif tile == prev_num:
                new_num = tile * 2
                merge_list[row][column - 1] = new_num
                merge_list[row][column] = 0
                prev_num = None
            else:
                prev_num = tile
        # Sortera återigen listorna åt vänster efter att talen adderats
        merge_list[row] = [num for num in merge_list[row] if num != 0] + [0] * merge_list[row].count(0)
    if merge_list != original_list:
        moved = True
    else:
        moved = False


def mergecheck(grid):
    prev_num = None
    can_merge = False
    for i in grid:
        if can_merge:
            break
        for j in i:
            if j == prev_num:
                can_merge = True
                break
            prev_num = j
        prev_num = None
    return can_merge


def up():
    up_positions = []
    for i in range(4):
        up_positions.append([positions[j][i] for j in range(4)])
    merge(up_positions)
    positions.clear()
    for i in range(4):
        positions.append([up_positions[j][i] for j in range(4)])


def left():
    merge(positions)


def down():
    down_positions = []
    for i in range(4):
        down_positions.append([positions[j][i] for j in range(-1, -5, -1)])
    merge(down_positions)
    positions.clear()
    for i in range(-1, -5, -1):
        positions.append([down_positions[j][i] for j in range(4)])


def right():
    right_positions = []
    for i in range(4):
        right_positions.append(positions[i][::-1])
    merge(right_positions)
    positions.clear()
    for i in range(4):
        positions.append(right_positions[i][::-1])


def restart():
    global gameisover, gameiswon, positions
    gameisover = False
    gameiswon = False
    positions = [[0] * 4 for i in range(4)]
    newblock(2)


def main():
    # Setup:
    newblock()
    newblock()
    # Spel-loop
    while True:
        window.fill(c.BG_COL)
        for row in range(4):
            for column, value in enumerate(positions[row]):
                if value != 0:
                    drawblock(column, row, value)
        if gameisover:
            game_over()
        elif gameiswon:
            winscreen()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:
                    up()
                    if moved:
                        newblock()
                elif event.key == K_a or event.key == K_LEFT:
                    left()
                    if moved:
                        newblock()
                elif event.key == K_s or event.key == K_DOWN:
                    down()
                    if moved:
                        newblock()
                elif event.key == K_d or event.key == K_RIGHT:
                    right()
                    if moved:
                        newblock()
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_RCTRL:
                    restart()
            elif event.type == QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        pygame.time.Clock().tick(c.FPS)


if __name__ == "__main__":
    pygame.init()
    font = pygame.font.SysFont(c.my_font, 42)
    window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("2048 av Verner Lindskog")
    icon = pygame.image.load("imgs/2048_logo.png")
    pygame.display.set_icon(icon)
    main()
