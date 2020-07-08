import sys
import matplotlib.pyplot as plt


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    test(not share_diagonal(5, 2, 2, 0))
    test(share_diagonal(5, 2, 3, 0))
    test(share_diagonal(5, 2, 4, 3))
    test(share_diagonal(5, 2, 4, 1))
    # Solutions cases that should not have any clashes
    test(not col_clashes([6, 4, 2, 0, 5], 4))
    test(not col_clashes([6, 4, 2, 0, 5, 7, 1, 3], 7))

    # More test cases that should mostly clash
    test(col_clashes([0, 1], 1))
    test(col_clashes([5, 6], 1))
    test(col_clashes([6, 5], 1))
    test(col_clashes([0, 6, 4, 3], 3))
    test(col_clashes([5, 0, 7], 2))
    test(not col_clashes([2, 0, 1, 3], 1))
    test(col_clashes([2, 0, 1, 3], 2))
    test(not has_clashes([6, 4, 2, 0, 5, 7, 1, 3]))  # Solution from above
    test(has_clashes([4, 6, 2, 0, 5, 7, 1, 3]))  # Swap rows of first two
    test(has_clashes([0, 1, 2, 3]))  # Try small 4x4 board
    test(not has_clashes([2, 0, 3, 1]))  # Solution to 4x4 case


bd1 = [[0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1],
       [0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0]]
bd2 = ["a6", "b4", "c2", "d0", "e5", "f7", "g1", "h3"]
bd3 = [(0, 6), (1, 4), (2, 2), (3, 0), (4, 5), (5, 7), (6, 1), (7, 3)]
bd4 = [6, 4, 2, 0, 5, 7, 1, 3]


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)  # Calc the absolute y distance
    dx = abs(x1 - x0)  # Calc the absolute x distance
    return dx == dy  # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def main(board_size):
    import random
    rng = random.Random()  # Instantiate a generator

    bd = list(range(board_size))  # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            for i in range(len(bd)):
                plt.plot(i, bd[i], 'r+')
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1


def main_mirror_y(board_size):
    import random
    rng = random.Random()  # Instantiate a generator

    bd = list(range(board_size))  # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            bd.reverse()
            for i in range(len(bd)):
                plt.plot(i, bd[i], 'r+')
            return bd
            tries = 0
            num_found += 1


def main_4c_90d(board_size):
    import random
    rng = random.Random()  # Instantiate a generator

    bd = list(range(board_size))  # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            # print("Found solution {0} in {1} tries.".format(bd, tries))
            # for i in range(len(bd)):
            #     plt.plot(bd[i], i, 'r+')
            # for i in range(len(bd)):
            #     bd[i] = i
            return bd
            tries = 0
            num_found += 1


def main_4d():
    import random
    rng = random.Random()
    result = []
    new_bd = main_4c_90d(8)
    print(new_bd)
    for i in range(2):
        rng.shuffle(new_bd)
        result.append(new_bd)
    return result


main_4d()

