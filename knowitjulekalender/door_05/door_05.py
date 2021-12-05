TOTAL_DEPTH = 0

# En tilpasset versjon av https://stackoverflow.com/questions/17140850/17141899#17141899
def make_list(long_list):
    stack = [[]]
    elf_name = ''
    for x in long_list:
        if x == '(':
            if elf_name != '':
                stack[-1].append(elf_name.strip())
                elf_name = ''
            stack[-1].append([])
            stack.append(stack[-1][-1])
        elif x == ')':
            if elf_name != '':
                stack[-1].append(elf_name.strip())
                elf_name = ''
            stack.pop()
            if not stack:
                return 'error: opening bracket is missing'
        else:
            if x == ' ' and elf_name != '':
                stack[-1].append(elf_name.strip())
                elf_name = ''
            else:
                elf_name += x
    if len(stack) > 1:
        return 'error: closing bracket is missing'
    return stack.pop()


def traverse_tree(graph, parent, curr_depth):
    global TOTAL_DEPTH

    if len(graph) == 0 or not isinstance(graph, list):
        TOTAL_DEPTH = max(TOTAL_DEPTH, curr_depth)
        return

    curr_depth -= 1 if parent == 'Grinch' else curr_depth

    for i in range(len(graph)):

        if isinstance(graph[i], list):
            traverse_tree(graph[i], graph[i-1], curr_depth + 1)
        else:
            curr_elf = graph[i]
            traverse_tree(curr_elf, parent, curr_depth)


def main():

    with open('tree.txt') as f:
        descendants = f.read()

    elf_list = make_list(descendants)
    traverse_tree(elf_list, '', 0)

    print(TOTAL_DEPTH)


if __name__ == '__main__':
    main()
