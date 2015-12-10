#!/usr/bin/python3.4

def main():
    day7_1 = day_7_solver('7.txt')
    print('Part 1: {}'.format(day7_1))
    #day7_2 = day_7_solver('day7_2input.txt')
    #print('Part 2: {}'.format(day7_2))

def day_7_solver(file):
    with open(file) as input:
        instructions = [line.strip() for line in input]

    # Rearrange equation.
    for i, line in enumerate(instructions):
        exp, var = line.split(' -> ')
        instructions[i] = '{} = {}'.format(var, exp)

    # Sort by wire for major speed improvement.
    instructions.sort(key=lambda wire: (len(wire.split()[0]), wire.split()[0]))

    # Replace operators and 2 letter keyword variable names.
    dict = {'NOT':'~', 'AND':'&', 'OR':'|', 'LSHIFT':'<<', 'RSHIFT':'>>',
            'as':'_as', 'if':'_if', 'or':'_or', 'in':'_in', 'is':'_is'}
    for i,_ in enumerate(instructions):
        for key, val in dict.items():
            instructions[i] = instructions[i].replace(key, val)

    # Track completed lines and finished wires.
    completed = set()
    wires = {}

    # Attempt to exec each line over and over until something works.
    while len(completed) != len(instructions):
        for line in instructions:
            try:
                exec(line, {}, wires)
                completed.add(line)
            except NameError:
                pass

    return 'wire a = {}'.format(wires['a'])

if __name__ == "__main__":
    main()
