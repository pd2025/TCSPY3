import sys
import numpy as np


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# list(range(10, 0, -2))
# that = ["I", "am", "not", "a", "crook"]
# print("Test 1: {0}".format(this is that))
# that = this  # does not work, because this is not yet defined. The correct code would be this = that, and it would
# # be on line 3
# print("Test 2: {0}".format(this is that))


def test_suite():
    # exercise 5 tests
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    # exercise 6 tests
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    # exercise 7 tests
    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    # exercise 10 tests
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")


def add_vectors(u, v):
    y = []
    for i in range(len(u)):
        x = u[i] + v[i]
        y.append(x)
    return y


def scalar_mult(s, v):
    y = []
    for i in range(len(v)):
        x = v[i] * s
        y.append(x)
    return y


def dot_product(u, v):
    y = []
    b = 0
    for i in range(len(u)):
        x = u[i] * v[i]
        y.append(x)
    for i in y:
        b += i
    return b


def cross_product(u, v):
    cross_product_ = np.cross(u, v)
    return cross_product_


def replace(s, old, new):
    s = s.replace(old, new)
    return s


def swap(x, y): # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)


a = ["This", "is", "fun"]
b = [2, 3, 4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)



