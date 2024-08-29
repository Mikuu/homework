import random


def generate_problem(number):
    problems = []

    while len(problems) < number:
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        problems.append(f"{a} x {b} =")

    return problems


def generate_lines(problems=[], column=3, spliter=' '*10):
    lines = []

    while len(problems):
        problems_in_line = []

        for _ in range(column):
            if len(problems):
                problems_in_line.append(problems.pop())

        lines.append(spliter.join(problems_in_line))

    return lines


def print_mental_calculation():
    problems = generate_problem(100)
    lines = generate_lines(problems, 5, ' '*25)

    for line in lines:
        print(line)


# def print_vertical_calculation():
#     problems = generate_problem(6, True)
#     lines = generate_lines(problems, 3, ' '*25)
#
#     for line in lines:
#         print(line)
#         print("\n")


def printing():
    print_mental_calculation()
    print("-" * 68)
    # print_vertical_calculation()


def print_all():
    for _ in range(5):
        printing()
        print()


print_all()