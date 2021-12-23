from knowitjulekalender.door_20.door_20 import read_maze, turn_head, get_new_pos


def main():

    maze = read_maze('maze.txt')
    face, pos, total_steps = 2, (0, 0), 0  # South
    here = lambda _: maze[_[0]][_[1]]
    visited = list()

    while pos != (len(maze)-1, len(maze[0])-1):

        visited.append(pos)
        face = turn_head(face, True)
        while here(pos)[face] == 0:
            face = turn_head(face, False)

        pos = get_new_pos(pos, face)

        # difference from door_20:
        if pos in visited:
            visited = visited[:visited.index(pos)]

    print(len(visited))


if __name__ == '__main__':
    main()
