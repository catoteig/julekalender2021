from functools import cache

TOTAL_STEPS = 1000079  # 666716,3333363
TOTAL_STEPS_TEST = 11

# Fikk tips om å først forsøke med færre nuller, fant da mønsteret og svar: 66666666666666666716,33333333333333333363


def main():

    curr_pos, north = [0, 0], True
    for _ in range(TOTAL_STEPS_TEST):
        if north:
            curr_pos[1] += 1
            north = False if mod(curr_pos[1], 3) and not mod(curr_pos[1], 5) else True
        else:
            curr_pos[0] += 1
            north = True if mod(curr_pos[0], 5) and not mod(curr_pos[0], 3) else False

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
