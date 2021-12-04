import numpy as np


def main():

    with open('input.txt') as f:
        children = f.read()

    value_list = [0]
    for _ in children:
        if _ == 'J':
            value_list.append(1)
        else:
            value_list.append(-1)
    # [0, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1]

    cum_list = np.cumsum(value_list)
    # [0  1  2  3  4  5  4  3  4  5  4  3  4  5  6  7  8]

    prev_index, size, index = {}, 0, 0
    for _, cum_sum in enumerate(cum_list):
        if cum_sum in prev_index:
            j = _ - prev_index[cum_sum]
            if j > size:
                index = prev_index[cum_sum]
                size = j
        else:
            prev_index[cum_sum] = _

    print("%i, %i" % (size, index))


if __name__ == '__main__':
    main()
