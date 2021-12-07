def main():

    santa_pos, ant_pos = 40, 3

    while santa_pos > ant_pos:

        ant_pos = ant_pos * ((santa_pos + 20) / santa_pos)
        santa_pos += 20
        ant_pos += 1

    print(santa_pos / 100)


if __name__ == '__main__':
    main()
