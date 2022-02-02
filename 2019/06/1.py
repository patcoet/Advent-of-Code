# Day 6: Universal Orbit Map
# Task: Calculate number of orbits of objects in space.

class Node:
  def __init__(self, name="", orbitee=None, leaves=[]):
    self.name = name
    self.orbitee = orbitee
    self.leaves = leaves

  def __repr__(self):
    return f"{self.name}: {self.leaves}"

node_list = [Node("COM")]

with open("input.txt") as file:
  for line in file:
    parts = line.split(")") # `"COM)B"` into `["COM", "B\n"]`.
    orbitee = parts[0]
    orbiter = parts[1].strip() # Get rid of the newline character.

    # In the real input the objects aren't guaranteed to be listed in order (that is, if x orbits y, y isn't guaranteed to be listed before x).

    node_list.append(Node(orbiter, orbitee))

# So now we have a flat list of objects, and the next thing to do is to make a tree out of it.

# Go through the list of objects and populate each one's list of orbiting objects:
for node in node_list:
  for other_node in node_list:
    if node.name != other_node.name and other_node.orbitee == node.name and other_node not in node.leaves:
      node.leaves = node.leaves + [other_node]

# Find the node that isn't orbiting around any other and set it as our tree root:
root = None
for node in node_list:
  if node.orbitee == None:
    root = node
    break

import sys
sys.setrecursionlimit(1500) # The default recursion depth of 1000 is exceeded when using str(root) below. It's fine.

# Instead of doing this the right way, which would mean writing a recursive function, let's just take the string representation of the tree and count colons in it:
level = 0
total = 0
for char in str(root): # `str(root)` looks like `COM: [B: [C: [D: [E: [F: [], J: [K: [L: []]]], I: []]], G: [H: []]]]`.
  if char == "[":   # When reading this representation of the tree from left to right, each [ means we've gone down a level in the tree,
    level += 1
  elif char == "]": # ] means we've gone up a level,
    level -= 1
  elif char == ":": # and : means we're at a node,
    total += level  # and the number of direct + indirect orbits of a node is equal to its level in the tree.

print(total)