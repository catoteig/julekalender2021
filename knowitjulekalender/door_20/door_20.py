def read_maze(text_file):

    with open(text_file) as f:
        t = f.read().splitlines()

    result = []
    for line in t:
        split_ = line[1:-1].split(')(')
        tpl = lambda _: tuple(map(int, _.split(',')))
        result.append([tpl(i) for i in split_])
    return result


def turn_head(current_face, go_left):

    cell = [0, 3, 2, 1] if go_left else [0, 1, 2, 3]
    coord = cell.index(current_face)

    return cell[coord+1] if coord + 1 < len(cell) else cell[0]


def get_new_pos(curr_pos, face):

    new_pos = tuple()
    if face == 0: new_pos = (curr_pos[0] - 1, curr_pos[1])
    elif face == 1: new_pos = (curr_pos[0], curr_pos[1] + 1)
    elif face == 2: new_pos = (curr_pos[0] + 1, curr_pos[1])
    elif face == 3: new_pos = (curr_pos[0], curr_pos[1] - 1)

    return new_pos


def main():

    maze = read_maze('maze.txt')
    face, pos, total_steps = 2, (0, 0), 0  # South
    here = lambda _: maze[_[0]][_[1]]

    while pos != (len(maze)-1, len(maze[0])-1):

        face = turn_head(face, True)
        while here(pos)[face] == 0:
            face = turn_head(face, False)

        pos = get_new_pos(pos, face)

        total_steps += 1

    print(total_steps)


if __name__ == '__main__':
    main()
