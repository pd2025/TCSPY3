import math
import turtle
t = turtle.Turtle()

def odd_numbers(): # exercise 7.1
    count = 0
    for i in [1, 3, 5, 4, 6, 2, 10]:
        if i % 2 == 1:
            count += 1
        elif i % 2 == 0:
            count += 0
    print(count)

def even_numbers(): # exercise 7.2
    even_count = 0
    for i in [1, 2, 3, 4, 5, 6]:
        if i % 2 == 0:
            even_count += i
        elif i % 2 == 1:
            even_count += 0
    print(even_count)

def negative_numbers(): # exercise 7.3
    negative_count = 0
    for i in [-1, 2, -3, 4, 5, -6]:
        if i < 0:
            negative_count += i
        elif i > 0:
            negative_count += 0
    print(negative_count)

def list_length(): # exercise 7.4
    length_count = 0
    xs = 'dog', 'piano', 'eight', 'shark', 'five'
    for i in (xs):
        if len(i) == 5:
            length_count += 1
        else:
            length_count += 0
    print(length_count)

def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end=" ")
    print()

def print_mult_table():
    for i in range(1, 7):
        print_multiples(i)

def sum_list():
    count = 0
    for i in [11, 13, 15, 16]:
        if i % 2 != 0:
            count += 1
        else:
            return count

# def game(human_plays_first):
#     rng = random.Random()
#     array = ['you win', 'i win', 'game drawn']

# sam_list = ['dog', 'cat', 'car', 'fish', 'sam', 'eat', 'hi']

def count_sam():  # exercise 7.5
    count = 0
    for i in sam_list:
        if i == 'sam':
            break
        elif type(i) != str:
            print('i is not a word')
            continue
        elif i != 'sam':
            count += 1
        print(count) # # #

def triangular_numbers(x):
    a_number = 1
    for i in range (x):
        counter = a_number * (a_number + 1) / 2
        a_number += 1
        print(counter)


def is_prime(x):
    n = 1
    while True:
        n += 1
        if x % n == 0:
            return False
            break
        else:
            return True


house_points = ([100, 100], [0, 100], [100, 0], [0, 0], [50, 150])


def house():
    for (x, y) in house_points:
        t.pd()
        t.goto(x, y)


def print_multiples(n, i):
    for i in range(1, 7):
        print(n * i, end=" ")
    print()


def print_mult_tables(high):
    for i in range (high, high + 1):
        print_multiples(i, high)


def num_digits(n):
    count = 0
    if n == 0:
        count = 1
    while n != 0:
        if n > 0:
            count += 1
            n = n // 10
        elif n < 0:
            count += 1
            n = n // -10
    return count


def num_even_digits(n):
    count = 0
    if n == 0:
        count = 1
    while n != 0:
        if n > 0:
            if n % 2 == 0:
                n = n // 10
                count += 1
            elif n % 2 == 1:
                n = n // 10
        elif n < 0:
            if n % 2 == 0:
                count += 1
                n = n // -10
            elif n % 2 == 1:
                n = n // -10
    return count


def sum_of_squares(xs):
    count = 0
    for i in xs:
        i = i ** 2
        count += i
    return count


def play_once(human_plays_first):
    """
    Must play one round of the game. If the parameter
    Must play one round of the game. If the parameter
    computer gets to play first. When the round ends,
    the return value of the function is one of
    -1 (human wins), 0 (game drawn), 1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0}, winner={1} "
          .format(human_plays_first, result))
    return result


result = play_once(True)
print(result)

human_count = 0
robot_count = 0
draw_count = 0

while True:
    again = input('do you want to play again?')
    if again == 'yes':
        result = play_once(True)
        if result == 0:
            print('game drawn')
            draw_count += 1
        elif result == 1:
            print('i win')
            robot_count += 1
        elif result == -1:
            print('you win')
            human_count += 1
        if again == 'no':
            break
            print('goodbye')
        print('robot count = ', robot_count, 'human count = ', human_count, 'draw count = ', draw_count)

