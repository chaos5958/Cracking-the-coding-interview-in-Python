def print_parens(num_pairs):
    if num_pairs == 0:
        return

    pairs = []
    prefix = []
    find_parens(num_pairs, num_pairs, pairs, prefix)
    for pair in pairs:
        print("".join(pair))

import copy

def find_parens(num_left_parens, num_right_parens, pairs, prefix):
    if num_left_parens == 0 and num_right_parens == 0:
        pairs.append(copy.copy(prefix))
        return

    if num_left_parens > 0:
        prefix.append("(")
        find_parens(num_left_parens - 1, num_right_parens, pairs, prefix)
        prefix.pop()

    if num_left_parens < num_right_parens:
        prefix.append(")")
        find_parens(num_left_parens, num_right_parens - 1, pairs, prefix)
        prefix.pop()


print_parens(3)
