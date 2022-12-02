import os
from urllib import request

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
    current_sum = 0
    for line in lines:
        if line == '':
            max_sum = max(current_sum, max_sum)
            current_sum = 0
        else:
            current_sum += int(line)

    print(max_sum)
