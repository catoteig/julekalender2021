def parse_list(task_list):

    with open(task_list) as f:
        t = f.read().splitlines()

    tasks = []
    for _ in t:
        i = _.split(' ', 1)
        tasks.append([len(i[0][:-1]), i[0][-1], i[1]])

    return tasks


def main():

    gift_list = parse_list('task.txt')
    total, temp, level = 0, 0, 0

    for curr in reversed(gift_list):
        level = curr[0]
        if curr[1] == 'K' and level < temp:
            total += 1
            temp = level
        elif curr[1] == 'G':
            temp = level

    print(total)


if __name__ == '__main__':
    main()
