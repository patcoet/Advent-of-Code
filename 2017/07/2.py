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
    possible_roots.remove(branch)

root_node = possible_roots[0]




def tree_weight(node_id):
  name = node_id
  weight = tree[node_id]['weight']
  branches = tree[node_id]['branches']

  for branch in branches:
    weight = weight + tree_weight(branch)

  return weight

def is_leaf(node_id):
  if tree[node_id]['branches'] == []:
    return True
  else:
    return False

def has_same_weight_branches(node_id):
  if is_leaf(node_id):
    return True
  else:
    branch_ids = tree[node_id]['branches']
    branch_weights = [tree_weight(branch_id) for branch_id in branch_ids]
    all_same_weight = all(map(lambda x: x == branch_weights[0], branch_weights))
    return all_same_weight

# Return the correct weight minus the incorrect
def weight_difference_to_correct(root_id):
  branch_ids = tree[root_id]['branches']
  branch_weights = sorted([tree_weight(branch_id) for branch_id in branch_ids])
  right_weight = 0
  wrong_weight = 0
  if branch_weights.count(branch_weights[0]) > 1:
    right_weight = branch_weights[0]
    wrong_weight = branch_weights[-1]
  else:
    right_weight = branch_weights[-1]
    wrong_weight = branch_weights[0]
  return right_weight - wrong_weight

def thing(node_id):
  if has_same_weight_branches(node_id):
    return node_id
  else:
    branch_ids = tree[node_id]['branches']
    branch_weights = [tree_weight(branch_id) for branch_id in branch_ids]
    for branch_id in branch_ids:
      branch_weight = tree_weight(branch_id)
      if branch_weights.count(branch_weight) == 1:
        return thing(branch_id)

node_id_to_rebalance = thing(root_node)
for node in tree:
  branch_ids = tree[node]['branches']
  if node_id_to_rebalance in branch_ids:
    d = weight_difference_to_correct(node)
    print(tree[node_id_to_rebalance]['weight'] + d)
