numbers = []
with open('input.txt') as file:
  numbers = list(map(int, file.readline().strip().split(' ')))

class Node:
  def __init__(self, children, dataz):
    self.children = children
    self.dataz = dataz

def make_tree(numbers):
  num_children = numbers.pop(0)
  num_dataz = numbers.pop(0)
  children = [make_tree(numbers) for n in range(num_children)]
  dataz = [numbers.pop(0) for n in range(num_dataz)]
  return Node(children, dataz)

def node_value(node):
  children = node.children
  dataz = node.dataz
  if len(children) == 0:
    return sum(dataz)
  else:
    return sum([node_value(children[index-1]) for index in dataz if 0 < index and index <= len(children)])

root = make_tree(numbers)
print(node_value(root))