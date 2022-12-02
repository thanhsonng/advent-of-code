import os
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/2/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Use enum
    def get_shape_from_encryption(encryption):
        if encryption in ['A', 'X']:
            return 'Rock'
        if encryption in ['B', 'Y']:
            return 'Paper'
        if encryption in ['C', 'Z']:
            return 'Scissors'
        return None

    def get_outcome_from_shapes(elf_shape, my_shape):
        shapes = ['Rock', 'Paper', 'Scissors']
        elf_index = shapes.index(elf_shape)
        my_index = shapes.index(my_shape)
        if elf_index == my_index:
            return 'Draw'
        if elf_index == (my_index + 1) % 3:
            return 'Lose'
        return 'Win'

    def get_outcome_from_encryption(enc_outcome):
        outcomes = {
            'X': 'Lose',
            'Y': 'Draw',
            'Z': 'Win',
        }
        return outcomes[enc_outcome]

    def get_score_from_outcome(outcome):
        scores = {
            'Lose': 0,
            'Draw': 3,
            'Win': 6,
        }
        return scores[outcome]

    def get_shape_from_outcome(outcome, elf_shape):
        shapes = ['Rock', 'Paper', 'Scissors']
        elf_index = shapes.index(elf_shape)
        if outcome == 'Draw':
            index = elf_index
        elif outcome == 'Lose':
            index = (elf_index - 1) % len(shapes)
        else:
            index = (elf_index + 1) % len(shapes)
        return shapes[index]

    def get_score_from_shape(shape):
        scores = {
            'Rock': 1,
            'Paper': 2,
            'Scissors': 3,
        }
        return scores[shape]


    # TODO: Read line-by-line to save memory
    strategy_guide: str = res.read().decode('utf8')
    rounds = strategy_guide.split('\n')

    total_score_1 = 0
    total_score_2 = 0

    for a_round in rounds:
        if a_round == '':
            continue
        enc_elf_shape, enc_value = a_round.split(' ')
        elf_shape = get_shape_from_encryption(enc_elf_shape)

        # Part 1
        my_shape_1 = get_shape_from_encryption(enc_value)
        outcome_1 = get_outcome_from_shapes(elf_shape, my_shape_1)
        score_from_shape_1 = get_score_from_shape(my_shape_1)
        score_from_outcome_1 = get_score_from_outcome(outcome_1)
        total_score_1 += score_from_shape_1 + score_from_outcome_1

        # Part 2
        outcome_2 = get_outcome_from_encryption(enc_value)
        my_shape_2 = get_shape_from_outcome(outcome_2, elf_shape)
        score_from_shape_2 = get_score_from_shape(my_shape_2)
        score_from_outcome_2 = get_score_from_outcome(outcome_2)
        total_score_2 += score_from_shape_2 + score_from_outcome_2

    print(f'Total score 1: {total_score_1}')
    print(f'Total score 2: {total_score_2}')
