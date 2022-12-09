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
    moves = all_input.split('\n')[0:-1] # ignore the last empty line

    # Part 1
    NUM_KNOTS = 2
    # Part 2
    # NUM_KNOTS = 10
    knots_positions = []
    for i in range(NUM_KNOTS):
        knots_positions.append((0, 0)) # x, y

    tail_positions = set()

    # Possible relative positions before and after head moves
    #
    #                                  H   H   H
    #      H   H   H               H   H   H   H   H
    #      H  T/H  H  --------->   H   H  T/H  H   H
    #      H   H   H               H   H   H   H   H
    #                                  H   H   H

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
                if knot_x - 1 <= prev_x <= knot_x + 1 and knot_y + 1 <= prev_y <= knot_y + 1:
                    pass # Don't need to move knot
                elif prev_y == knot_y:
                    if prev_x == knot_x + 2:
                        knot_x += 1 # Move knot to the right
                    elif prev_x == knot_x - 2:
                        knot_x -= 1 # Move knot to the left
                elif prev_x == knot_x:
                    if prev_y == knot_y + 2:
                        knot_y += 1 # Move knot up
                    elif prev_y == knot_y - 2:
                        knot_y -= 1 # Move knot down
                elif prev_x == knot_x + 1:
                    if prev_y == knot_y + 2:
                        knot_x += 1 # Move knot up-right
                        knot_y += 1
                    elif prev_y == knot_y - 2:
                        knot_x += 1 # Move knot down-right
                        knot_y -= 1
                elif prev_x == knot_x + 2:
                    if prev_y == knot_y + 1:
                        knot_x += 1 # Move knot up-right
                        knot_y += 1
                    elif prev_y == knot_y - 1:
                        knot_x += 1 # Move knot down-right
                        knot_y -= 1
                elif prev_x == knot_x - 1:
                    if prev_y == knot_y + 2:
                        knot_x -= 1 # Move knot up-left
                        knot_y += 1
                    elif prev_y == knot_y - 2:
                        knot_x -= 1 # Move knot down-left
                        knot_y -= 1
                elif prev_x == knot_x - 2:
                    if prev_y == knot_y + 1:
                        knot_x -= 1 # Move knot up-left
                        knot_y += 1
                    elif prev_y == knot_y - 1:
                        knot_x -= 1 # Move knot down-left
                        knot_y -= 1
                knots_positions[i] = (knot_x, knot_y)

                # Remember the positions tail has visited
                if i == NUM_KNOTS - 1:
                    tail_positions.add(knots_positions[i])

    print(f'Tail visited positions: {len(tail_positions)}')
