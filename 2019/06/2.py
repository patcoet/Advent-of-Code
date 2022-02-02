# Day 6: Universal Orbit Map
# OK, let's be a little less silly for part 2.

class Node:
  def __init__(self, name="", orbitee=None, leaves=[]):
    self.name = name
    self.orbitee = orbitee
    self.leaves = leaves

nodes = [Node("COM")] # Flat list of nodes, for putting in a tree later.
root = nodes[0]

with open("test2.txt") as file:
  for line in file:
    parts = line.split(")") # `"COM)B"` into `["COM", "B\n"]`.
    orbitee = parts[0]
    orbiter = parts[1].strip() # Get rid of the newline character.

    nodes.append(Node(orbiter, orbitee))

# A Node's leaves is a list of all Nodes that have that Node as their orbitee.
for node in nodes:
  node.leaves = [node2 for node2 in nodes if node2 != node and node2.orbitee == node.name]
for node in nodes:
  if node.orbitee == "COM":
    root.leaves.append(node)

# Given the name of an object in space, return its corresponding Node:
def node(name):
  for n in nodes:
    if n.name == name:
      return n

# Given two Nodes, where node2 is located straight up the tree from node1, return the Nodes on the path between them:
def path_from_to_up(node1, node2):
  if node1 == node2:
    return [node2]
  else:
    return [node1] + path_from_to_up(node(node1.orbitee), node2)

# Given two Nodes anywhere in the tree, return the Nodes on the path between them:
def path_from_to(node1, node2):
  path1 = path_from_to_up(node1, root)
  path2 = path_from_to_up(node2, root)

  first_common_node = next(n for n in path1 for n2 in path2 if n == n2)

  return path_from_to_up(node1, first_common_node) + path_from_to_up(node2, first_common_node)[-2::-1]

def steps_between(node1, node2):
  return len(path_from_to(node1, node2)) - 3 # Our computed path is e.g. `[YOU, K, J, E, D, I, SAN]`, and what counts for the puzzle is `[J, E, D, I]`.

print(f'Transfers required from YOU to SAN: {steps_between(node("YOU"), node("SAN"))}')