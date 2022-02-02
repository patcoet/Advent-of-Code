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

def sum_tree(tree):
  sum1 = sum(tree.dataz)
  return sum1 + sum([sum_tree(child) for child in tree.children])

root = make_tree(numbers)
print(sum_tree(root))