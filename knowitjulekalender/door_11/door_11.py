from collections import defaultdict


def read_files(name_file, code_file):

    with open(name_file, 'r') as f1, open(code_file, 'r') as f2:
        r1, r2 = f1.read().splitlines(), f2.read().splitlines()
    return r1, r2


def poss_combos(name):

    combos = {name}
    for a, b in zip(name[0:-1], name[1:]):
        combos.add(name.replace(a+b, b+a))
    return combos


def is_match(name, code):

    name_list = list(name)
    start, stop = -1, -1

    for c in enumerate(code):
        if c[1] == name_list[0]:
            start = c[0] if start == -1 else start
            if len(name_list) == 1:
                stop = c[0] + 1
                name_list.pop(0)
                break
            name_list.pop(0)

    match = False if name_list else True

    return stop - start - len(name), match


def main():

    name_combos, codes = read_files('names.txt', 'locked.txt')
    matches = defaultdict(list)
    for name in name_combos:
        name_set = set(name)
        for code in codes:
            if len(name_set - name_set.intersection(set(code))) == 0:
                matches[name].append(code)

    gift_list = defaultdict(list)

    for name in matches:
        name_combos = poss_combos(name)
        codes = matches.get(name)

        for code in codes:
            variation_diffs = []
            for name_var in name_combos:
                diff, match = is_match(name_var, code)
                if match:
                    variation_diffs.append(diff)
            if len(variation_diffs) != len(set(variation_diffs)):
                continue
            elif len(variation_diffs) > 0:
                min_variation_diff = min(variation_diffs)
                gift_list[code].append([name, min_variation_diff])

    final_list = defaultdict(int)
    for code_child, value in gift_list.items():
        if len(value) == 1:
            final_list[value[0][0]] += 1
        else:
            minimum = ('', float('inf'))
            for i in value:
                if i[1] < minimum[1]:
                    minimum = i

            count = 0
            for j in value:
                if j[1] == minimum[1]:
                    count += 1

            if count > 1:
                continue
            else:
                final_list[minimum[0]] += 1

    max_key = max(final_list, key=final_list.get)
    print('%s,%i' % (max_key, final_list.get(max_key)))


if __name__ == '__main__':
    main()
