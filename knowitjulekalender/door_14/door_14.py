import re


def count_creatures(text_file):

    nisser, trolls = 0, 0

    with open(text_file, 'r') as source_file:

        for line in source_file:
            nisse_regex = '^.*n.{0,2}i.{0,2}s.{0,2}s.{0,2}e.*$'
            nisse = line[:-1]
            if nisse[:1] != 'n' and nisse[-1] != 'e' and re.search(nisse_regex, nisse):
                nisser += 1

            troll_regex = '^.*t.{1,5}r.{1,5}o.{1,5}l.{1,5}l.*$'
            troll = line[:-1]
            if re.search(troll_regex, troll):
                trolls += 1

    return nisser, trolls


def main():

    print(sum(count_creatures('ordliste.txt')))


if __name__ == '__main__':
    main()
