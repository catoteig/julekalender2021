def main():

    x, y, z = set(), set(), set()

    for _ in range(2000):
        x.add(2424154637 * _ + 1854803357)
        y.add(2807727397 * _ + 2787141611)
        z.add(2537380333 * _ + 1159251923)

    print(x.intersection(y).intersection(z))


if __name__ == '__main__':
    main()
