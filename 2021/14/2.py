import re
from collections import defaultdict

template = ""
rules = {}

with open('input') as file:
    template = file.readline().strip()
    file.readline()
    for line in file:
        p1, p2 = re.findall('(\w\w) -> (\w)', line)[0]
        rules[p1] = p2

pairs = defaultdict(int)
for i in range(len(template) - 1):
    pairs[template[i:i+2]] += 1

added_elements = defaultdict(int)
for element in template:
    added_elements[element] += 1

for _ in range(40):
    pairs_to_decrement = defaultdict(int)
    pairs_to_increment = defaultdict(int)
    for pair in pairs:
        added_elements[rules[pair]] += pairs[pair]
        new_pair1 = pair[0] + rules[pair]
        new_pair2 = rules[pair] + pair[1]
        pairs_to_increment[new_pair1] += pairs[pair]
        pairs_to_increment[new_pair2] += pairs[pair]
        pairs_to_decrement[pair] += pairs[pair]

    for pair in pairs_to_increment:
        pairs[pair] += pairs_to_increment[pair]
    for pair in pairs_to_decrement:
        pairs[pair] -= pairs_to_decrement[pair]
        if pairs[pair] <= 0:
            del pairs[pair]

print(max(added_elements.values()) - min(added_elements.values()))
