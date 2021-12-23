from functools import cache


def niklatz(n):

    sequence = [n]
    while n != 1:
        n = math_shenanigans(n)
        sequence.append(n)
    return sequence


def niklatz_xmas(n):

    sequence, count = [n], 0
    while n != 1:
        if n % 37 == 0:
            count = 3
        if count > 0:
            n = math_shenanigans_inverted(n)
            count -= 1
        else:
            n = math_shenanigans(n)
        sequence.append(n)
    return sequence


@cache
def math_shenanigans(i):
    i = i / 2 if i % 2 == 0 else i * 3 + 1
    return int(i)


@cache
def math_shenanigans_inverted(j):
    j = j / 2 if j % 2 != 0 else j * 3 + 1
    return int(j)


def main():

    total = 0
    for _ in range(1, 10**6):

        niklatz_seq = niklatz(_)
        niklatz_xmas_seq = niklatz_xmas(_)

        if len(niklatz_seq) != len(niklatz_xmas_seq):
            total += sum(niklatz_xmas_seq)

    print(math_shenanigans.cache_info(), math_shenanigans_inverted.cache_info())
    print(total)


if __name__ == '__main__':
    main()
