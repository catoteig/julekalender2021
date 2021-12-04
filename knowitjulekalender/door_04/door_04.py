from functools import cache

TOTAL_STEPS = 1000079
TOTAL_STEPS_TEST = 11


def main():

    curr_pos, north = [0, 0], True
    for _ in range(TOTAL_STEPS_TEST):

        if north:
            curr_pos[1] += 1
            if mod(curr_pos[1], 3) and not mod(curr_pos[1], 5):
                north = False
        else:
            curr_pos[0] += 1
            if mod(curr_pos[0], 5) and not mod(curr_pos[0], 3):
                north = True

    print(curr_pos)


@cache
def mod(num, check):
    res = 0
    num = str(num)
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % check
    return True if res == 0 else False


if __name__ == '__main__':
    main()
