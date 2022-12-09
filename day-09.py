import os
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/9/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Read line-by-line to save memory
    all_input: str = res.read().decode('utf8')
    moves = all_input.strip().split('\n')

    # Part 1
    # NUM_KNOTS = 2
    # Part 2
    NUM_KNOTS = 10
    knots_positions = []
    for i in range(NUM_KNOTS):
        knots_positions.append((0, 0)) # x, y

    tail_positions = set()

    # Part 1: Possible relative positions before and after head moves
    #
    #                                  H   H   H
    #      H   H   H               H   H   H   H   H
    #      H  T/H  H  --------->   H   H  T/H  H   H
    #      H   H   H               H   H   H   H   H
    #                                  H   H   H

    # Part 2: Possible relative positions before and after knot moves
    #
    #                              K   K   K   K   K
    #      K   K   K               K   K   K   K   K
    #      K  T/K  K  --------->   K   K  T/K  K   K
    #      K   K   K               K   K   K   K   K
    #                              K   K   K   K   K

    for move in moves:
        direction, steps = move.split(' ')
        steps = int(steps)
        for step in range(steps):
            # Move head
            head_x, head_y = knots_positions[0]
            if direction == 'R':
                head_x += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1
            knots_positions[0] = (head_x, head_y)

            # Move other knots
            for i in range(1, NUM_KNOTS):
                prev_x, prev_y = knots_positions[i - 1]
                knot_x, knot_y = knots_positions[i]

                diff_x = prev_x - knot_x
                diff_y = prev_y - knot_y
                if abs(diff_x) <= 1 and abs(diff_y) <= 1:
                    pass
                else:
                    coef = {
                        2: 1,
                        1: 1,
                        0: 0,
                        -1: -1,
                        -2: -1,
                    }
                    knot_x += coef[diff_x] * 1
                    knot_y += coef[diff_y] * 1
                knots_positions[i] = (knot_x, knot_y)

                # Remember the positions tail has visited
                if i == NUM_KNOTS - 1:
                    tail_positions.add(knots_positions[i])

    print(f'Tail visited positions: {len(tail_positions)}')
