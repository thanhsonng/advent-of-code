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

    head_position = (0, 0) # x, y
    tail_position = (0, 0)
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
            head_x, head_y = head_position
            if direction == 'R':
                head_x += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1
            head_position = (head_x, head_y)

            # Move tail
            tail_x, tail_y = tail_position
            if tail_x - 1 <= head_x <= tail_x + 1 and tail_y + 1 <= head_y <= tail_y + 1:
                pass # Don't need to move tail
            elif head_y == tail_y:
                if head_x == tail_x + 2:
                    tail_x += 1 # Move tail to the right
                elif head_x == tail_x - 2:
                    tail_x -= 1 # Move tail to the left
            elif head_x == tail_x:
                if head_y == tail_y + 2:
                    tail_y += 1 # Move tail up
                elif head_y == tail_y - 2:
                    tail_y -= 1 # Move tail down
            elif head_x == tail_x + 1:
                if head_y == tail_y + 2:
                    tail_x += 1 # Move tail up-right
                    tail_y += 1
                elif head_y == tail_y - 2:
                    tail_x += 1 # Move tail down-right
                    tail_y -= 1
            elif head_x == tail_x + 2:
                if head_y == tail_y + 1:
                    tail_x += 1 # Move tail up-right
                    tail_y += 1
                elif head_y == tail_y - 1:
                    tail_x += 1 # Move tail down-right
                    tail_y -= 1
            elif head_x == tail_x - 1:
                if head_y == tail_y + 2:
                    tail_x -= 1 # Move tail up-left
                    tail_y += 1
                elif head_y == tail_y - 2:
                    tail_x -= 1 # Move tail down-left
                    tail_y -= 1
            elif head_x == tail_x - 2:
                if head_y == tail_y + 1:
                    tail_x -= 1 # Move tail up-left
                    tail_y += 1
                elif head_y == tail_y - 1:
                    tail_x -= 1 # Move tail down-left
                    tail_y -= 1
            tail_position = (tail_x, tail_y)

            # Remember the position tail has visited
            tail_positions.add(tail_position)

    print(f'Tail visited positions: {len(tail_positions)}')
