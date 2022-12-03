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

    # Part 1
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

    # Part 2
    total_badges_priorities = 0
    group_counter = 0
    sets = [set(), set(), set()]

    for rucksack in rucksacks:
        group_counter += 1

        for item in rucksack:
            sets[group_counter - 1].add(item)

        if group_counter == 3:
            badges = sets[0] & sets[1] & sets[2]
            if len(badges) > 1:
                raise Exception(f'More than 1 badges found: {badges}')
            total_badges_priorities += get_priority(badges.pop())
            for s in sets:
                s.clear()
            group_counter = 0

    print(f'Total priorities of badges: {total_badges_priorities}')
