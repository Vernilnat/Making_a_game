import pygame
from pygame.locals import (K_w, K_UP, K_a, K_LEFT, K_s, K_DOWN, K_d, K_m, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_RCTRL,
                           MOUSEBUTTONDOWN)
import random
import colours as c
import json

# TO DO LIST
# meny!
# slutmeny!


# Definiera en lista som har koll på spel-positionen
positions = []

# Variabler som används i spel-loopen senare...
gameisover = False
gameiswon = False
gameiswon_menu = False
moved = False
click = False
score = 0


def soundeffect():
    pygame.mixer.Sound("audio/Quack Sound Effect.mp3").play()


def drawtext(font, text, text_col, center, surface, bg_col=None):
    textobj = font.render(text, True, text_col, bg_col)
    textrect = textobj.get_rect()
    textrect.center = center
    surface.blit(textobj, textrect)
    return textrect


def drawblock(x, y, num):
    x = x * 128
    y = y * 128
    pygame.draw.rect(window, c.block_colour(num), pygame.Rect(x, y, 128, 128))
    drawtext(big_font, str(num), c.BLACK, (x + (c.WIDTH // 8), y + (c.HEIGHT // 8)), window)


def game_over():
    global gameisover
    drawtext(big_font, "Game Over!", c.GAMEOVER, (c.WIDTH // 2, c.HEIGHT // 4 + c.HEIGHT // 16), window)
    drawtext(small_font, "Press \"Right Control\" to play again", c.GAMEOVER, (c.WIDTH // 2, c.HEIGHT // 8 * 3 +
                                                                               c.HEIGHT // 16), window)
    drawtext(small_font, "Press \"m\" to exit to main menu", c.GAMEOVER, (c.WIDTH // 2, c.HEIGHT // 2 + c.HEIGHT // 16),
             window)
    drawtext(small_font, "Press \"Escape\" to quit the game", c.GAMEOVER, (c.WIDTH // 2, c.HEIGHT // 8 * 5 + c.HEIGHT
                                                                           // 16), window)

    gameisover = True


def winscreen():
    global gameiswon
    global gameiswon_menu
    drawtext(big_font, "You win!", c.BLACK, (c.WIDTH // 2, c.HEIGHT // 2), window)
    drawtext(small_font, "To continue the game press \"alt\"", c.BLACK, (c.WIDTH // 2, c.HEIGHT // 4 * 3), window)
    gameiswon = True
    gameiswon_menu = True


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
                for row in range(4):
                    rotate_positions.append([positions[j][row] for j in range(4)])
                if not mergecheck(rotate_positions):
                    game_over()


# en sätta ihop funktion, resten av funktionerna justerar listorna så att merge()-funktionen fungerar på rätt sätt för
# de olika situationerna
def merge(merge_list):
    global moved
    global score
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
                # poäng!
                score += new_num
            else:
                prev_num = tile
        # Sortera återigen listorna åt vänster efter att talen adderats
        merge_list[row] = [num for num in merge_list[row] if num != 0] + [0] * merge_list[row].count(0)
    if merge_list != original_list:
        moved = True
    else:
        moved = False
    # soundeffect()


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


def printscore():
    # Nuvarande poäng:
    global score
    score_text = small_font.render(f"Score: {score}", True, c.BLACK)
    window.blit(score_text, (0, 0))
    # Poängrekord:
    highscore_text = small_font.render("Highscore: " + str(values["highscore"]), True, c.BLACK)
    highscore_text_rect = highscore_text.get_rect()
    highscore_text_rect.topright = (c.WIDTH, 0)
    window.blit(highscore_text, highscore_text_rect)


def restart():
    global gameisover, gameiswon, positions, score
    if values["highscore"] < score:
        values["highscore"] = score
        thefile = open("constants.json", "w")
        json.dump(values, thefile)
    gameisover = False
    gameiswon = False
    score = 0
    positions = [[0] * 4 for i in range(4)]
    newblock(2)


def printbuttons():
    drawtext(big_font, "Choose difficulty: ", c.BLACK, (c.WIDTH // 2, c.HEIGHT // 8 * 3), window, c.RED)
    _2048 = drawtext(small_font, "2048", c.BLACK, (c.WIDTH // 4, c.HEIGHT // 2), window, c.WHITE)
    _1024 = drawtext(small_font, "1024", c.BLACK, (c.WIDTH // 2, c.HEIGHT // 2), window, c.WHITE)
    _512 = drawtext(small_font, "512", c.BLACK, (c.WIDTH // 4 * 3, c.HEIGHT // 2), window, c.WHITE)
    play = drawtext(big_font, "Play", c.BLACK, (c.WIDTH // 2, c.HEIGHT // 4 * 3), window, c.WHITE)
    mx, my = pygame.mouse.get_pos()
    if _2048.collidepoint((mx, my)) and click:
        c.win_tile = 2048
    elif _1024.collidepoint((mx, my)) and click:
        c.win_tile = 1048
    elif _512.collidepoint((mx, my)) and click:
        c.win_tile = 512
    elif play.collidepoint((mx, my)) and click:
        main()


def main_menu():
    global click

    while True:
        window.fill(c.BG_COL)
        printbuttons()
        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            elif event.type == QUIT:
                quit()
        pygame.display.update()


def main():
    global positions
    # Setup:
    positions = [[0] * 4 for i in range(4)]
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
        printscore()
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
                elif event.key == K_m:
                    main_menu()
            elif event.type == QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        pygame.time.Clock().tick(c.FPS)


if __name__ == "__main__":
    values = json.load(open("constants.json", "r"))
    pygame.init()
    big_font = pygame.font.SysFont(c.my_font, 42)
    small_font = pygame.font.SysFont(c.my_font, 20)
    window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("2048 av Verner Lindskog")
    icon = pygame.image.load("imgs/2048_logo.png")
    pygame.display.set_icon(icon)
    main_menu()
