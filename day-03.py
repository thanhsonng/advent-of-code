import os
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/3/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    def get_priority(char: str):
        if char.islower():
            return ord(char) - 96
        else:
            return ord(char) - 38

    # TODO: Read line-by-line to save memory
    strategy_guide: str = res.read().decode('utf8')
    rucksacks = strategy_guide.split('\n')

    total_priorities = 0

    for rucksack in rucksacks:
        rucksack_size = len(rucksack)
        compartment_size = rucksack_size // 2
        compartment_1 = set()
        for i in range(0, rucksack_size):
            item = rucksack[i]
            if i < compartment_size:
                compartment_1.add(item)
            elif item in compartment_1:
                total_priorities += get_priority(item)
                break

    print(f'Total priorities: {total_priorities}')
