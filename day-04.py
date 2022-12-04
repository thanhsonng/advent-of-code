import os
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/4/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Read line-by-line to save memory
    strategy_guide: str = res.read().decode('utf8')
    pairs = strategy_guide.split('\n')

    # Part 1

    fully_contain_pairs = 0

    for pair in pairs:
        if pair == '':
            continue
        range_1, range_2 = pair.split(',')
        lower_1, upper_1 = [int(x) for x in range_1.split('-')]
        lower_2, upper_2 = [int(x) for x in range_2.split('-')]
        if (lower_1 <= lower_2 and upper_1 >= upper_2) or (lower_1 >= lower_2 and upper_1 <= upper_2):
            fully_contain_pairs += 1

    print(f'Fully contain pairs: {fully_contain_pairs}')
