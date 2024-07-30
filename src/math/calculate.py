import random


def generate_problem(number, force_carry_borrow=False):
    problems = []

    while len(problems) < number:
        a = random.randint(10, 99)
        b = random.randint(10, 99)

        if (a + b) >= 100:
            continue
        elif force_carry_borrow:
            if a % 10 + b % 10 > 10:
                problems.append(f"{a} + {b} =")
        else:
            problems.append(f"{a} + {b} =")

        if (len(problems)) == number:
            break

        a = random.randint(10, 99)
        b = random.randint(10, 99)

        if a == b:
            continue
        elif force_carry_borrow:
            if a > b and a % 10 < b % 10:
                problems.append(f"{a} - {b} =")
            elif b > a and b % 10 < a % 10:
                problems.append(f"{b} - {a} =")
        else:
            problems.append(f"{a} - {b} =" if a > b else f"{b} - {a} =")

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
    problems = generate_problem(30)
    lines = generate_lines(problems, 3, ' '*25)

    for line in lines:
        print(line)


def print_vertical_calculation():
    problems = generate_problem(6, True)
    lines = generate_lines(problems, 3, ' '*25)

    for line in lines:
        print(line)
        print("\n")


def printing():
    print_mental_calculation()
    print("-" * 68)
    print_vertical_calculation()


def print_all():
    for _ in range(33):
        printing()
        print()


print_all()