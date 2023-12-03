import os
import re
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/11/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Read line-by-line to save memory
    all_input: str = res.read().decode('utf8')
    monkey_specs = all_input.strip().split('\n\n')


class Monkey:
    def __init__(self, spec) -> None:
        lines = [line.strip() for line in spec.split('\n')]
        for line in lines:
            if match := re.match('Monkey (\d+)', line):
                self.index = int(match.group(1))
            elif match := re.match('Starting items: (.+)', line):
                self.items = [int(item) for item in match.group(1).split(', ')]
            elif match := re.match('Operation: new = (.+)', line):
                self.operation = match.group(1)
            elif match := re.match('Test: divisible by (\d+)', line):
                self.divisor = int(match.group(1))
            elif match := re.match('If true: throw to monkey (\d+)', line):
                self.true_dest = int(match.group(1))
            elif match := re.match('If false: throw to monkey (\d+)', line):
                self.false_dest = int(match.group(1))

    def get_num_items(self):
        return len(self.items)

    def act(self, monkeys):
        while len(self.items) > 0:
            item = self.items.pop(0)
            worry = self.operate(item)
            # Enabled in Part 1
            # Disabled in Part 2
            worry //= 3
            if self.test(worry):
                self.pass_to(monkeys[self.true_dest], worry)
            else:
                self.pass_to(monkeys[self.false_dest], worry)


    def operate(self, worry):
        old = worry
        return eval(self.operation)

    def test(self, worry):
        return worry % self.divisor == 0

    def pass_to(self, monkey, item):
        monkey.items.append(item)


monkeys = [Monkey(spec) for spec in monkey_specs]
num_inspected = [0 for _ in monkeys]
# Part 1
NUM_ROUNDS = 20
# Part 2
# NUM_ROUNDS = 10_000

for i in range(NUM_ROUNDS):
    for j in range(len(monkeys)):
        monkey = monkeys[j]
        num_inspected[j] += monkey.get_num_items()
        monkey.act(monkeys)

max_1 = max(num_inspected)
num_inspected.remove(max_1)
max_2 = max(num_inspected)
print(f'Monkey business: {max_1 * max_2}')
