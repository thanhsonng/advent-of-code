import os
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/8/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Read line-by-line to save memory
    grid: str = res.read().decode('utf8')
    rows = grid.split('\n')[0:-1] # ignore the last empty line

    num_rows = len(rows)
    num_cols = len(rows[0])

    total_visible = num_cols * 2 + (num_rows - 2) * 2
    highest_scenic_score = 0

    for row in range(1, num_rows - 1):
        for col in range(1, num_cols - 1):
            tree = int(rows[row][col])

            is_visible_from_left = True
            viewing_distance_left = 0
            for c in reversed(range(0, col)):
                viewing_distance_left += 1
                if int(rows[row][c]) >= tree:
                    is_visible_from_left = False
                    break

            is_visible_from_right = True
            viewing_distance_right = 0
            for c in range(col + 1, num_cols):
                viewing_distance_right += 1
                if int(rows[row][c]) >= tree:
                    is_visible_from_right = False
                    break

            is_visible_from_top = True
            viewing_distance_top = 0
            for r in reversed(range(0, row)):
                viewing_distance_top += 1
                if int(rows[r][col]) >= tree:
                    is_visible_from_top = False
                    break

            is_visible_from_bottom = True
            viewing_distance_bottom = 0
            for r in range(row + 1, num_rows):
                viewing_distance_bottom += 1
                if int(rows[r][col]) >= tree:
                    is_visible_from_bottom = False
                    break

            is_visible = is_visible_from_left or is_visible_from_right or is_visible_from_top or is_visible_from_bottom
            if is_visible:
                total_visible += 1

            scenic_score = viewing_distance_left * viewing_distance_right * viewing_distance_top * viewing_distance_bottom
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    print(f'Total visible: {total_visible}')
    print(f'Highest scenic score: {highest_scenic_score}')
