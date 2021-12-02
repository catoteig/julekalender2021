def main():
    with open("tall.txt") as f:
        num_all = f.read()
    num_map = {
        "en": 1, "to": 2, "tre": 3, "fire": 4, "fem": 5, "seks": 6, "sju": 7, "åtte": 8, "ni": 9,
        "ti": 10, "elleve": 11, "tolv": 12, "tretten": 13, "fjorten": 14,
        "femten": 15, "seksten": 16, "sytten": 17, "atten": 18, "nitten": 19,
        "femti": 50, "førti": 40, "tretti": 30, "tjue": 20
    }
    num_exceptions = ["to", "tre", "fem", "seks", "ni"]

    curr_word, total, skip_to, len_all = "", 0, -1, len(num_all)

    for letter in enumerate(num_all):
        if letter[0] <= skip_to:
            continue
        curr_word += letter[1]
        if curr_word in num_map:
            if curr_word in num_exceptions:
                temp_word = curr_word
                for e in range(1, 8):
                    if (letter[0] + e) >= len_all:
                        break
                    temp_word += num_all[letter[0] + e]
                    if temp_word in num_map:
                        total += num_map.get(temp_word)
                        skip_to = letter[0] + e
                        break
            if skip_to < letter[0]:
                total += num_map.get(curr_word)
            curr_word = ""
    print(total)


if __name__ == '__main__':
    main()
