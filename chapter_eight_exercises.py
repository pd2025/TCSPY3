def practice_with_strings():  # 8.19.1
    print("Python"[1])  # prints 'y'
    print("Strings are sequences of characters."[5])  # prints 'g'
    print(len("wonderful"))  # prints 9
    print("Mystery"[:4])  # prints 'Myst'
    print("p" in "Pineapple")  # True
    print("apple" in "Pineapple")  # True
    print("pear" not in "Pineapple")  # True
    print("apple" > "pineapple")  # False
    print("pineapple" < "Peach")  # False


def ack_practice():  # 8.19.2
    prefixes = "JKLMNOPQ"
    u = 'u'
    suffix = "ack"
    for letter in prefixes:
        if letter == prefixes[5] or letter == prefixes[7]:
            print(letter + u + suffix)
        else:
            print(letter + suffix)


def count_letters(string, letter):
    fruit = string
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    return count


def count_letters_2():
    count = 0
    word = 'banana'
    found = -1
    while word.find('a', found + 1) != -1:
        found = word.find("a", found + 1)
        count += 1
    return count


def paragraph_breakdown():
    count = 0
    count2 = 0
    paragraph = """When he was nearly thirteen, my brother Jem got his arm badly broken at the
elbow. When it healed, and Jem’s fears of never being able to play football were
assuaged, he was seldom self-conscious about his injury. His left arm was
somewhat shorter than his right; when he stood or walked, the back of his hand
was at right angles to his body, his thumb parallel to his thigh. He couldn’t have
cared less, so long as he could pass and punt."""
    punctuation = """!()-[]{};:'"\,<>./?@#$%^&*_~’"""
    for x in paragraph.lower():
        if x in punctuation:
            paragraph = paragraph.replace(x, "")
    xs = paragraph.split()
    for i in xs:
        length = len(xs)
        for a in i:
            if a == 'e':
                count2 += 1
                if count2 > 1:
                    count2 = 1
                    count = count + count2
    percent = length / count * 100
    print('Your text contains', length, 'words, of which', count, '(', percent, '%) contain an "e"')


def twelve_by_twelve():
    print("1\t  2\t\t  3\t      4\t      5\t      6\t      7\t      8\t      9\t      10\t  11\t  12")
    for i in range(2, 13):
        print(i, "\t ", i * 2, "\t ", i * 3, "\t ", i * 4, "\t ", i * 5, "\t ", i * 6, "\t ", i * 7, "\t ", i * 8, "\t ", i * 9, "\t ", i * 10, "\t ", i * 11, "\t ", i * 12)


def backwards_words(fruit):
    sz = len(fruit)
    count = 0
    for i in fruit:
        count += 1
        return fruit[sz-count]


def reverse(fruit):
    str1 = ""
    for i in fruit:
        str1 = i + str1
    return str1


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


def remove_from_string(string, occurence):
    for x in string:
        if x in occurence:
            string = string.replace(x, "")
    return string


def count_substring(substring, string):
    return string.count(substring)


def remove_substring(substring, string):
    result = string.find(substring)
    if result != 1:
        return string[0:result] + string[result + len(substring)]
    return string


def remove_string_from_string(substring, string):
    string = string.replace(substring, "")
    return string


print(remove_substring('na', 'banana'))







