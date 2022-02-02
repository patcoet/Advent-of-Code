inputt = 'input.txt'

tree = {}

with open(inputt) as file:
  for line in file:
    line = line.strip('\n')
    words = line.split(' ')
    name = words[0]
    weight = words[1]
    weight = int(weight[1 : len(weight)-1])
    branches = []
    for i in range(3, len(words)):
      branches.append(words[i].strip(','))
    tree[name] = {'weight': weight, 'branches': branches}

possible_roots = []
for node in tree:
  possible_roots.append(node)

for node in tree:
  name = node
  weight = tree[node]['weight']
  branches = tree[node]['branches']

  for branch in branches:
    # The root is the only node that isn't a branch of another node
    possible_roots.remove(branch)

print(possible_roots)