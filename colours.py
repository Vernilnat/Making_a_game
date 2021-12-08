
WIDTH, HEIGHT = 512, 512
BG_COL = (128, 152, 183)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
LIGHTBLUE = (68, 85, 90)
BLACK = (0, 0, 0)
GAMEOVER = (101, 67, 33)


def block_colour(num):
    if num == 2:
        return 255, 250, 250
    elif num == 4:
        return 255, 225, 225
    elif num == 8:
        return 255, 200, 200
    elif num == 16:
        return 255, 175, 175
    elif num == 32:
        return 255, 150, 150
    elif num == 64:
        return 255, 125, 125
    elif num == 128:
        return 255, 100, 100
    elif num == 256:
        return 255, 75, 75
    elif num == 512:
        return 255, 50, 50
    elif num == 1024:
        return 255, 25, 25
    elif num == 2048:
        return 255, 0, 0
    else:
        return False


my_font = "Calibri"
FPS = 60
win_tile = 256

