BOX_DIM = 10  # ^3
CHIMNEY_DIM = 90  # ^2
CHIMNEY_HEIGHT = 2500
START_POS = ((CHIMNEY_DIM // BOX_DIM // 2), ) * 2


def parse_moves(move_text):

    with open(move_text) as f:
        m = f.read().splitlines()

    return [_ for _ in m]


def do_move(pos, move):

    if move == 'N':
        new_pos = (pos[0], pos[1] - 1)
    elif move == 'S':
        new_pos = (pos[0], pos[1] + 1)
    elif move == 'E':
        new_pos = (pos[0] + 1, pos[1])
    elif move == 'W':
        new_pos = (pos[0] - 1, pos[1])
    else:
        new_pos = pos

    return new_pos


def main():

    chimney_floor = {(x, y): 0 for y in range(CHIMNEY_DIM // BOX_DIM) for x in range(CHIMNEY_DIM // BOX_DIM)}

    gifts = parse_moves('moves.txt')

    for gift in gifts:

        pos, curr_depth = START_POS, BOX_DIM
        for move in gift:
            new_pos = do_move(pos, move)
            if new_pos in chimney_floor and CHIMNEY_HEIGHT - chimney_floor[new_pos] >= curr_depth:
                pos = new_pos
            curr_depth += BOX_DIM

        chimney_floor[pos] += BOX_DIM

    print(chimney_floor[max(chimney_floor, key=chimney_floor.get)])


if __name__ == '__main__':
    main()
