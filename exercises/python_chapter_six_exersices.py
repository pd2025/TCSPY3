import sys
import math

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def day_num(day):
    if day == 'Sunday':
        return 0
    elif day == 'Monday':
        return 1
    elif day == 'Tuesday':
        return 2
    elif day == 'Wednesday':
        return 3
    elif day == 'Thursday':
        return 4
    elif day == 'Friday':
        return 5
    elif day == 'Saturday':
        return 6

def day_name(day):
    if day == 0:
        return 'Sunday'
    if day == 1:
        return 'Monday'
    if day == 2:
        return 'Tuesday'
    if day == 3:
        return 'Wednesday'
    if day == 4:
        return 'Thursday'
    if day == 5:
        return 'Friday'
    if day == 6:
        return 'Saturday'

def day_add(day, days_added):
    print(day_name(day_num(day) + days_added))


def test_suite():
    # test(day_num('Friday') == 5)
    # test(day_num('Sunday') == 0)
    # test(day_num(day_name(3)) == 3)
    # test(day_name(day_num("Thursday")) == "Thursday")
    # test(day_name(3) == "Wednesday")
    # test(day_name(6) == "Saturday")
    # test(day_name(42) == None)
    # test(day_add("Monday", 4) == "Friday")
    # test(day_add("Tuesday", 0) == "Tuesday")
    # test(day_add("Tuesday", 14) == "Tuesday")
    # test(day_add("Sunday", 100) == "Tuesday")
    # test(3 % 4 == 0)
    # test(3 % 4 == 3)
    # test(3 / 4 == 0)
    # test(3 // 4 == 0)
    # test(3 + 4 * 2 == 14)
    # test(4 - 2 + 2 == 0)
    # test(len("hello, world!") == 13)
    # test(to_secs(2, 30, 10) == 9010)
    # test(to_secs(2, 0, 0) == 7200)
    # test(to_secs(0, 2, 0) == 120)
    # test(to_secs(0, 0, 42) == 42)
    # test(to_secs(0, -10, 10) == -590)
    # test(mysum([1, 2, 3, 4]) == 10)
    # # test(mysum([1.25, 2.5, 1.75]) == 5.5)
    # test(count_sam(['dog', 'pam', 'cat', 'same']) == 3)
    # test(num_digits(0) == 1)
    # test(num_digits(-12345) == 5)
    # test(num_even_digits(123456) == 3)
    # test(num_even_digits(2468) == 4)
    # test(num_even_digits(1357) == 0)
    # test(num_even_digits(0) == 1)
    # test(backwards_words("happy") == "yppah")
    # test(backwards_words("Python") == "nohtyP")
    # # test(backwards_words("") == "")
    # # test(backwards_words("a") == "a")
    # test(mirror("good") == "gooddoog")
    # test(is_palindrome("abba"))
    # test(remove_letter("a", "apple") == "pple")
    test(count_substring("is", "Mississippi") == 2)


def to_secs(hours, minutes, seconds):
    return ((hours * 60 * 60) + (minutes * 60) + (seconds))//1


def hypot(a, b):
    return math.sqrt(a**2 + b**2)


def mysum(xs):
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total


def slope(y1, y2, x1, x2):
    return (y2 - y1) / (x2 - x1)


def backwards_words(fruit):
    sz = len(fruit)
    count = 0
    for i in fruit:
        count += 1
        last = fruit[sz-count] + i
        return last


def mirror(fruit):
    sz = len(fruit)
    count = 0
    for i in fruit:
        count += 1
        fruit = fruit + fruit[sz-count]
    return fruit


def is_palindrome(fruit):
    str1 = ""
    for i in fruit:
        str1 = i + str1
    if str1 == fruit:
        return True
    else:
        return False


def remove_letter(occurence, string):
    for x in string:
        if x in occurence:
            string = string.replace(x, "")
    return string


def count_substring(substring, string):
    return string.count(substring)


print(test_suite())


