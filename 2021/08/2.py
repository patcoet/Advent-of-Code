import re

def decode_output(patterns, output):
    decoded_patterns = [set()] * 10
    for pattern in patterns:
        if len(pattern) == 2:
            decoded_patterns[1] = set(pattern)
        elif len(pattern) == 4:
            decoded_patterns[4] = set(pattern)
        elif len(pattern) == 3:
            decoded_patterns[7] = set(pattern)
        elif len(pattern) == 7:
            decoded_patterns[8] = set(pattern)

    for pattern in patterns:
        if len(pattern) == 6:
            if len(pattern.intersection(decoded_patterns[4])) == 4:
                decoded_patterns[9] = pattern
            elif len(pattern.intersection(decoded_patterns[1])) == 2:
                decoded_patterns[0] = pattern
            else:
                decoded_patterns[6] = pattern

        if len(pattern) == 5:
            if len(pattern.intersection(decoded_patterns[1])) == 2:
                decoded_patterns[3] = pattern
            elif len(pattern.intersection(decoded_patterns[4])) == 2:
                decoded_patterns[2] = pattern
            else:
                decoded_patterns[5] = pattern

    decoded_number = 0
    multiplier = 10 ** (len(output) - 1)
    for coded_number in output:
        for i, dcn in enumerate(decoded_patterns):
            if set(coded_number) == dcn:
                decoded_number += i * multiplier
                multiplier //= 10

    return decoded_number

total = 0

with open('input') as file:
    for line in file:
        p1, p2 = re.findall('(.*) \| (.*)', line)[0]
        patterns = [set(x) for x in re.findall('(\S+)\s?', p1)]
        output = re.findall('(\S+)\s?', p2)
        decoded = decode_output(patterns, output)
        total += decoded
    
print(total)
