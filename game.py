prev_num = None
can_merge = False


def mergecheck(grid):
    global prev_num
    global can_merge
    for i in grid:
        if can_merge:
            break
        for j in i:
            if j == prev_num:
                print(prev_num)
                print(j)
                can_merge = True
                break
            prev_num = j
        prev_num = None
    return can_merge


for lol in range(1):
    positions = [
        [8, 4, 8, 2],
        [64, 1, 512, 9],
        [32, 2, 9, 4],
        [8, 4, 2, 4]
    ]
    
    options = []
    if not options:
        if not mergecheck(positions):
            print("HELLO")
            rotate_positions = []
            for i in range(4):
                rotate_positions.append([positions[j][i] for j in range(4)])
            print(rotate_positions)
            if not mergecheck(rotate_positions):
                print("game over")
            else:
                print("." + str(mergecheck(rotate_positions)))

    