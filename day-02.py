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
    # TODO: Read line-by-line to save memory
    strategy_guide: str = res.read().decode('utf8')
    rounds = strategy_guide.split('\n')

    # TODO: Use enum
    def get_shape_from_encryption(encryption):
        if encryption in ['A', 'X']:
            return 'Rock'
        if encryption in ['B', 'Y']:
            return 'Paper'
        if encryption in ['C', 'Z']:
            return 'Scissors'
        return None

    def get_outcome(elf_shape, my_shape):
        shapes = ['Rock', 'Paper', 'Scissors']
        elf_index = shapes.index(elf_shape)
        my_index = shapes.index(my_shape)
        if elf_index == my_index:
            return 'Draw'
        if elf_index == (my_index + 1) % 3:
            return 'Lose'
        return 'Win'

    def get_score_from_enc_shape(enc_shape):
        scores = {
            'Rock': 1,
            'Paper': 2,
            'Scissors': 3,
        }
        shape = get_shape_from_encryption(enc_shape)
        return scores[shape]

    def get_score_from_outcome(enc_elf_shape, enc_my_shape):
        scores = {
            'Lose': 0,
            'Draw': 3,
            'Win': 6,
        }
        elf_shape = get_shape_from_encryption(enc_elf_shape)
        my_shape = get_shape_from_encryption(enc_my_shape)
        outcome = get_outcome(elf_shape, my_shape)
        return scores[outcome]

    total_score = 0

    for a_round in rounds:
        if a_round == '':
            continue
        elf_shape, my_shape = a_round.split(' ')
        total_score += get_score_from_enc_shape(my_shape) + get_score_from_outcome(elf_shape, my_shape)

    print(f'Total score: {total_score}')
