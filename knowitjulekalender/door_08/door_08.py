def parse_input(textfile):

    cities, route = {}, []
    with open(textfile) as f:
        t = f.read().splitlines()

    for _ in enumerate(t):
        if _[1][:1] == '(':
            cities[_[0]] = (tuple(map(int, _[1][1:-1].split(','))))
        else:
            route.append(int(_[1]))

    return cities, route


def print_grid(grid_dict, grid_dim):

    t = ''
    for _ in grid_dict.values():
        t += str(_)
        if len(t) == grid_dim:
            print(t)
            t = ''


def main():

    city_list, route = parse_input('input.txt')
    grid, grid_dim = {}, 1000
    for x in range(grid_dim)[::-1]:
        for y in range(grid_dim):
            grid[(x, y)] = 0

    prev_city = 0
    for this_city in route:

        x_dir = 1 if city_list[prev_city][0] <= city_list[this_city][0] else -1
        y_dir = 1 if city_list[prev_city][1] <= city_list[this_city][1] else -1

        for y in range(city_list[prev_city][0], city_list[this_city][0], x_dir):
            for x in range(city_list[prev_city][1], city_list[this_city][1], y_dir):
                grid[x, y] += 1

        prev_city = this_city

    all_values = grid.values()
    max_value = max(all_values)
    max_list = {key: value for (key, value) in grid.items() if value == max_value}

    x_max, y_max = [], []
    for _ in max_list:
        x_max.append(_[1])
        y_max.append(_[0])

    print('%i,%i %i,%i' % (min(x_max), min(y_max), max(x_max), max(y_max)))


if __name__ == '__main__':
    main()
