import sys
import time

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# lists
# friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
# xs = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]


def test_suite():
    # test(search_linear(friends, "Zoe") == 1)
    # test(search_linear(friends, "Joe") == 0)
    # test(search_linear(friends, "Paris") == 6)
    # test(search_linear(friends, "Bill") == -1)
    # book_words = "the apple fell from the tree to the grass".split()
    # test(find_unknown_words(vocab, book_words) == ["from", "to"])
    # test(find_unknown_words([], book_words) == book_words)
    # test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])
    # test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
    # test(text_to_words('"Well, I never!", said Alice.') ==
    #      ["well", "i", "never", "said", "alice"])
    # test(search_binary(xs, 20) == -1)
    # test(search_binary(xs, 99) == -1)
    # test(search_binary(xs, 1) == -1)
    # for (i, v) in enumerate(xs):
    #     test(search_binary(xs, v) == i)
    # test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
    # test(remove_adjacent_dups([]) == [])
    # test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) == ["a", "big", "bite", "dog"])
    # xs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # ys = [4, 8, 12, 16, 20, 24]
    # zs = xs + ys
    # zs.sort()
    # test(merge(xs, []) == xs)
    # test(merge([], ys) == ys)
    # test(merge([], []) == [])
    # test(merge(xs, ys) == zs)
    # test(merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5])
    # test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
    #      ["a", "big", "big", "bite", "cat", "dog"])
    # test(merge_a_correct([1, 2, 5, 5, 8], [2, 8, 11]) == [2, 8])
    test(merge_c_correct([xs], []) == [])
    test(merge_c_correct([], [ys]) == [])
    test(merge_c_correct(xs, ys) == [11])


def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'".format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time


def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if search_binary(vocab, w) < 0:
            result.append(w)
    return result


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds


bigger_vocab = load_words_from_file("vocab.txt")
# print("There are {0} words in the vocab, starting with\n {1} ".format(len(bigger_vocab), bigger_vocab[:6]))


def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

#
# book_words = get_words_in_book("AliceInWonderland.txt")
# print("There are {0} words in the book, the first 100 are\n{1}".
#            format(len(book_words), book_words[:100]))


# missing_words = find_unknown_words(bigger_vocab, book_words)
# t0 = time.clock()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.clock()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))


# t0 = time.clock()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.clock()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

# search_binary(bigger_vocab, "magic")

def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result


all_words = get_words_in_book("AliceInWonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print("There are {0} words in the book. Only {1} are unique.".
                      format(len(all_words), len(book_words)))
print("The first 100 words are\n{0}".
           format(book_words[:100]))


def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def merge_a_correct(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # if end of list xs
            return result  # fin
        if yi >= len(ys):  # if end of list ys
            return result  # fin
        if xs[xi] == ys[yi]:  # if element in xs == element in ys
            result.append(xs[xi])  # append element to list
            xi += 1  # increment xi
            yi += 1  # increment yi
        elif xs[xi] < ys[yi]:  # if element in xs < element in ys
            xi += 1  # increment xi but not yi
        else:  # if element in xs < element in ys
            yi += 1  # increment yi but not xi


def merge_a(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    while True:
        for i in xs:
            if i in ys:
                if i not in result:
                    result.append(i)
        return result


def merge_b_correct(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # if end of list xs
            return result  # fin
        if yi >= len(ys):  # if end of list ys
            return result  # fin
        if xs[xi] == ys[yi]:  # if element in xs == element in ys
            xi += 1  # increment xi
            yi += 1  # increment yi
        elif xs[xi] < ys[yi]:  # if element in xs < element in ys
            result.append(xs[xi])  # append element to list
            xi += 1  # increment xi but not yi
        else:  # if element in xs < element in ys
            yi += 1  # increment yi but not xi


def merge_b(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    while True:
        for i in xs:
            if i in xs and i not in ys:
                if i not in result:
                    result.append(i)
        return result


def merge_c_correct(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # if end of list xs
            return result  # fin
        if yi >= len(ys):  # if end of list ys
            return result  # fin
        if xs[xi] == ys[yi]:  # if element in xs == element in ys
            xi += 1  # increment xi
            yi += 1  # increment yi
        elif xs[xi] < ys[yi]:  # if element in xs < element in ys
            result.append(ys[yi])  # append element to list
            yi += 1  # increment xi but not yi
        else:  # if element in xs < element in ys
            xi += 1  # increment yi but not xi


def merge_c(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    while True:
        for i in ys:
            if i in ys and i not in xs:
                if i not in result:
                    result.append(i)
        return result


def merge_d_correct(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # if end of list xs
            return result  # fin
        if yi >= len(ys):  # if end of list ys
            return result  # fin
        if xs[xi] == ys[yi]:  # if element in xs == element in ys
            xi += 1  # increment xi
            yi += 1  # increment yi
        else:  # if element in xs < element in ys
            result.append(ys[yi])  # append element to list
            result.append(xs[xi])  # append element to list
            xi += 1  # increment yi but not xi
            yi += 1  # increment xi but not yi


def merge_d(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    while True:
        for i in xs:
            if i in xs or i in ys:
                if i not in result:
                    result.append(i)
        for i in ys:
            if i in xs or i in ys:
                if i not in result:
                    result.append(i)
        return result


def merge_e_correct(xs, ys):
    result = xs[:]
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # if end of list xs
            return result  # fin
        if yi >= len(ys):  # if end of list ys
            return result  # fin
        if xs[xi] == ys[yi]:  # if element in xs == element in ys
            xs.remove(xs[xi])
            yi += 1  # increment yi
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1


def merge_e(xs, ys):
    while True:
        for i in xs:
            if i in ys:
                xs.remove(i)
                ys.remove(i)
        return xs


print(merge_e_correct([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))
