def exercise_131():
    with open('../text_files/text.txt', 'w') as f:
        f.write('hiiiiii\n')
        f.write('hello therererererere\n')
        f.write('hi')

    with open('../text_files/exercise131.txt', 'w') as f:
        for line in reversed(list(open('../text_files/text.txt'))):
            f.write(line.rstrip())
            f.write('\n')


def exercise_132():
        # L = ["the snake bit me\n", "the dog bit me\n", "the snake is scary\n", "I like dogs\n", "I hate snakes\n"]
        # file1 = open('snake.txt', 'w')
        # file1.writelines(L)
        file1 = open('../text_files/snake.txt', 'r')
        for line in file1:
            if 'snake' in line:
                print(line)


def exercise_133():
    infile = open('mymodule1.py', 'r')
    outfile = open('../text_files/the_outfile.txt', 'w')
    line = infile.readlines()
    count = 0
    for x in range(len(line)):
        count += 1
        outfile.write("{0: >4} {1}".format(count, line[x]))


def exercise_134():
    infile = open('../text_files/the_outfile.txt', 'r')
    outfile = open('../text_files/outfile_134.txt', 'w')
    line = infile.readlines()
    for x in range(len(line)):
        current_line = line[x]
        current_line = current_line.replace(current_line[3], '')
        outfile.write(current_line)


exercise_134()