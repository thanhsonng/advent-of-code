import os
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/1/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Read line-by-line to save memory
    calories_list: str = res.read().decode('utf8')
    lines = calories_list.split('\n')

    max_sum = 0
    max_sums = [0, 0, 0]

    current_sum = 0
    for line in lines:
        if line == '':
            max_sum = max(current_sum, max_sum)

            max_sums.append(current_sum)
            max_sums.sort(reverse=True)
            max_sums.pop()

            current_sum = 0
        else:
            current_sum += int(line)

    print(f'Max calories of one elf: {max_sum}')
    print(f'Total calories of top three elves: {sum(max_sums)}')
