import os
import re
from urllib import request
from dotenv import load_dotenv
from typing import List


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/5/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Read line-by-line to save memory
    strategy_guide: str = res.read().decode('utf8')
    input_text = strategy_guide.split('\n')
    stacks_input = input_text[0:8]
    moves_input = input_text[10:]

    # Construct stacks
    stacks: List[List] = []
    for i in range(9):
        stacks.append([])
    for line in stacks_input:
        for i in range(len(line)):
            if line[i].isalpha():
                stack_index = (i - 1) // 4
                stacks[stack_index].insert(0, line[i])

    # Operate
    for line in moves_input:
        if line == '':
            continue
        matches = re.match('move (\d+) from (\d+) to (\d+)', line)
        num, original_stack, destination_stack = (int(x) for x in matches.group(1, 2, 3))

        # Part 1
        # for i in range(num):
        #     stacks[destination_stack - 1].append(stacks[original_stack - 1].pop())

        # Part 2
        stacks[destination_stack - 1] += stacks[original_stack - 1][-num:]
        stacks[original_stack - 1] = stacks[original_stack - 1][0:-num]

    # Collect
    message = ''
    for stack in stacks:
        message += stack[-1]
    print(f'Message: {message}')
