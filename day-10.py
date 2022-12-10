import os
import math
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/10/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Read line-by-line to save memory
    all_input: str = res.read().decode('utf8')
    instructions = all_input.strip().split('\n')

    # Part 1
    current_cycle = 1
    x = 1
    total_signal_strength = 0
    IMPORTANT_CYCLES = [20, 60, 100, 140, 180, 220]

    for instruction in instructions:
        splitted = instruction.split(' ')
        if len(splitted) == 1:
            operation = splitted[0]
        else:
            operation, value = splitted

        if operation == 'noop':
            num_cycles = 1
        elif operation == 'addx':
            num_cycles = 2

        for i in range(num_cycles):
            if current_cycle in IMPORTANT_CYCLES:
                total_signal_strength += current_cycle * x
            current_cycle += 1

        if operation == 'addx':
            x += int(value)

    print(f'Total signal strength: {total_signal_strength}')

    # Part 2
    current_cycle = 1
    x = 1
    lines = ['' for _ in range(6)]

    for instruction in instructions:
        splitted = instruction.split(' ')
        if len(splitted) == 1:
            operation = splitted[0]
        else:
            operation, value = splitted

        if operation == 'noop':
            num_cycles = 1
        elif operation == 'addx':
            num_cycles = 2

        for i in range(num_cycles):
            row = math.ceil(current_cycle / 40) - 1
            line_index = current_cycle - 40 * row
            lines[row] += '#' if x <= line_index <= x + 2 else '.'
            current_cycle += 1

        if operation == 'addx':
            x += int(value)

    print('CRT')
    for line in lines:
        print(line)
