import os
from urllib import request
from dotenv import load_dotenv


load_dotenv()

input_url = 'https://adventofcode.com/2022/day/6/input'
headers = {
    'Authority': 'adventofcode.com',
    'cookie': f'session={os.getenv("COOKIE")}',
}
req = request.Request(input_url, headers=headers)


with request.urlopen(req) as res:
    # TODO: Read line-by-line to save memory
    signal: str = res.read().decode('utf8').strip()

    # Part 1
    last_4_chars = ''
    for i in range(len(signal)):
        if len(last_4_chars) == 4:
            last_4_chars = last_4_chars[1:] + signal[i]
        else:
            last_4_chars += signal[i]

        if len(set((last_4_chars))) == 4:
            print(f'First start-of-packet position: {i + 1}')
            break

    # Part 2
    last_14_chars = ''
    for i in range(len(signal)):
        if len(last_14_chars) == 14:
            last_14_chars = last_14_chars[1:] + signal[i]
        else:
            last_14_chars += signal[i]

        if len(set((last_14_chars))) == 14:
            print(f'First start-of-message position: {i + 1}')
            break
