import self as self

WIDTH, HEIGHT = 512, 512
BG_COL = (128, 152, 183)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)
GAMEOVER_COL = (134, 21, 21)


def block_colour(num):
    if num == 2:
        return 255, 255, 255
    elif num == 4:
        return 255, 200, 200
    elif num == 8:
        return 255, 150, 150
    elif num == 16:
        return 255, 100, 100
    else:
        print("Number in block_colour(), incorrect")


my_font = "Calibri"
FPS = 60


