TOTAL_STEPS = 1000079  # 666716,3333363
TOTAL_STEPS_TEST = 11

# Fikk tips om å først forsøke med færre nuller, fant da mønsteret med å legge til 6-ere og 3-ere
# og svaret: 66666666666666666716,33333333333333333363


def main():

    curr_pos, go_north = [0, 0], True
    for _ in range(TOTAL_STEPS):
        if go_north:
            curr_pos[1] += 1
            go_north = False if curr_pos[1] % 3 == 0 and curr_pos[1] % 5 != 0 else True
        else:
            curr_pos[0] += 1
            go_north = True if curr_pos[0] % 5 == 0 and curr_pos[0] % 3 != 0 else False

    print(curr_pos)


if __name__ == '__main__':
    main()
