import string

MESSAGE = '452051451920510572814191151813572091210211251812015161619112520914' \
          '75141221011351923522729182181222718192919149121210211251491919514'
MESSAGE_TEST = '7154102112'


def convert_wordlist(wordlist):

    word_dict = {}
    alphabet = list(string.ascii_lowercase)
    alphabet.extend(['æ', 'ø', 'å'])

    with open(wordlist, 'r') as f:
        for line in f:
            word = ''
            for letter in line[:-1]:
                word += str(alphabet.index(letter) + 1)
            word_dict[word] = line[:-1]

    return word_dict


def main():

    message = MESSAGE
    word_dict = convert_wordlist('wordlist.txt')
    match = []

    for code in word_dict:
        if code in message:
            code_value = word_dict.get(code)
            pos = message.find(code)
            letter_code = list(code)
            letter_list = ''
            for i in range(len(message)):
                if i >= pos and letter_code:
                    letter_list += letter_code[0]
                    letter_code.pop(0)
                else:
                    letter_list += '_'
            match.append((letter_list, code_value, pos))

    match = sorted(match, key=lambda _: _[2])
    for _ in match:
        print(_[0], _[1])

    # Went through the output manually.
    # Answer: detenestejegønskermegtiljuleratoppskytingenavjameswebbgårbraværsåsnilljulenissen


if __name__ == '__main__':
    main()
