"""
0: 6 segments
1: 2
2: 5
3: 5
4: 4
5: 5
6: 6
7: 3
8: 7
9: 6

Uniques:
1: 2
4: 4
7: 3
8: 7

9 is the only one that has 4 in common with 4 plus 2 more
0 has 2 in common with 1 plus 4 more
6 is the other 6

Out of the 5-segments,
3 is the only one that has 2 in common with 1
2 and 4 have 2 segments in common
5 and 4 have 3 segments in common
"""
import re


def decode_output(patterns, output):
    decoded_numbers = [set()] * 10
    for pattern in patterns:
        if len(pattern) == 2:
            decoded_numbers[1] = set(pattern)
        elif len(pattern) == 4:
            decoded_numbers[4] = set(pattern)
        elif len(pattern) == 3:
            decoded_numbers[7] = set(pattern)
        elif len(pattern) == 7:
            decoded_numbers[8] = set(pattern)

    for pattern in patterns:
        if len(pattern) == 6:
            if len(pattern.intersection(decoded_numbers[4])) == 4:
                decoded_numbers[9] = pattern
            elif len(pattern.intersection(decoded_numbers[1])) == 2:
                decoded_numbers[0] = pattern
            else:
                decoded_numbers[6] = pattern

    for pattern in patterns:
        if len(pattern) == 5:
            if len(pattern.intersection(decoded_numbers[1])) == 2:
                decoded_numbers[3] = pattern
            elif len(pattern.intersection(decoded_numbers[4])) == 2:
                decoded_numbers[2] = pattern
            else:
                decoded_numbers[5] = pattern

    res = []
    for coded_number in output:
        for i, dcn in enumerate(decoded_numbers):
            if set(coded_number) == dcn:
                res.append(i)

    return res

# (Oops, I didn't need to decode all of them for part 1!)

with open('input') as file:
    total = 0
    for line in file:
        p1, p2 = re.findall('(.*) \| (.*)', line)[0]
        patterns = [set(x) for x in re.findall('(\S+)\s?', p1)]
        output = re.findall('(\S+)\s?', p2)
        decoded = decode_output(patterns, output)

        total += sum([1 for x in decoded if x in [1, 4, 7, 8]])
    
    print(total)
