import time
import calendar
import math
import copy
from exercises import mymodule1, mymodule2
import sys


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
    test(myreplace(",", ";", "this, that, and some other thing") == "this; that; and some other thing")
    test(myreplace(" ", "**", "Words will    now be separated by stars.") == "Words**will**now**be**separated**by**stars.")
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))
    test(extract_words("Now is the time! ’Now’, is the time? Yes, now.") ==
         ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") ==
         ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])
    test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
    test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
    test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)
    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
         ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
         ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
         ["a", "am", "are", "be", "but", "is", "or"])
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(longestword([ ]) == 0)


def time_practice_1():
    def do_my_sum(xs):
        sum = 0
        for v in xs:
            sum += v
        return sum

    sz = 10000000  # Lets have 10 million elements in the list
    testdata = range(sz)
    t0 = time.clock()
    my_result = do_my_sum(testdata)
    t1 = time.clock()
    print("my_result = {0} (time taken = {1:.4f} seconds)".format(my_result, t1-t0))
    t2 = time.clock()
    their_result = sum(testdata)
    t3 = time.clock()
    print("their_result = {0} (time taken = {1:.4f} seconds)".format(their_result, t3-t2))


def exercise_12_1a():
    cal = calendar.TextCalendar()
    cal.pryear(2012)


def exercise_12_1b():
    cal = calendar.TextCalendar()
    cal.setfirstweekday(calendar.THURSDAY)
    cal.pryear(2012)


def exercise_12_1ba():
    cal = calendar.TextCalendar(firstweekday=3)
    cal.pryear(2012)


def exercise_12_1c():
    return calendar.month(2020, 1, 2, 1)


def exercise_12_1d():
    d = calendar.LocaleTextCalendar(6, "FRENCH")
    d.pryear(2012)


def exercise_12_1e():
    cal = calendar.TextCalendar()
    cal.pryear(2012)
    return calendar.isleap(2020)  # 'isleap' takes a year as an argument and returns whether or not it's a leap year


# there are 56 functions in the math module


def exercise_12_2b():
    return math.ceil(44.8/7)  # ceiling division: performs division and rounds the quotient up (6.4 becomes 7)
    return math.floor(10/4)  # floor division: performs division and removes the decimal (2.5 becomes 2)


def exercise_12_2c(x):
    # print(math.sqrt(4))
    root = x ** 0.5
    return root


# 12 2d: tbd


def exercise_3():
    s = 3
    b = copy.deepcopy(s)
    return b, s
    """ deepcopy creates another variable with the same value as the original variable
    now, b is a new variable that has the same value as s"""


def exercise_4():
    print((mymodule2.myage - mymodule1.myage) ==
          (mymodule2.year - mymodule1.year))
    if __name__ == "__main__":
        print("This won’t run if I’m imported.")


def myreplace(old, new, s):  # work on this later
    s = s.split()
    s = ' '.join(s)
    s = new.join(s.split(old))
    return s


def cleanword(s):
    old = """!()-[]{};:'"\,<>./?@#$%^&*_~’+="""
    new = ''
    for i in s:
        if i in old:
            s = s.replace(i, new)
    return s


def has_dashdash(s):
    dashdash = '--'
    if dashdash in s:
        return True


def extract_words(s):
    old = """!()-[]{};:'"\,<>./?@#$%^&*_~’+="""
    new = ' '
    s = s.lower()
    for i in s:
        if i in old:
            s = s.replace(i, new)
    s = s.split()
    return s


def wordcount(word, s):
    count = 0
    for i in s:
        if i == word:
            count += 1
    return count


def wordset(s):
    s2 = []
    s.sort()
    for i in s:
        if i not in s2:
            s2.append(i)
    return s2


def longestword(s):
    length = 0
    for i in s:
        if length < len(i):
            length = len(i)
    return length





