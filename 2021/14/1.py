import re

template = ""
rules = {}

with open('test') as file:
    template = file.readline().strip()
    file.readline()
    for line in file:
        p1, p2 = re.findall('(\w\w) -> (\w)', line)[0]
        rules[p1] = p2

for _ in range(10):
    i = 0
    while i < len(template) - 1:
        pair = template[i:i+2]
        template = template[:i+1] + rules[pair] + template[i+1:]
        i += 2

freqs = {}
for char in template:
    if char not in freqs:
        freqs[char] = template.count(char)

print(max(freqs.values()) - min(freqs.values()))
