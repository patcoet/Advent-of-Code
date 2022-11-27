import math
from collections import deque
import re

class Node:
    def __init__(self):
        self.l = None
        self.r = None

    def __str__(self):
        return f'[{str(self.l)}, {str(self.r)}]'

    def __repr__(self):
        return str(self)

def parse(string):
    list_ = eval(string)
    node = Node()
    
    node.l = parse2(list_[0])
    node.r = parse2(list_[1])

    return node

def parse2(list_):
    if type(list_) == int:
        return list_
    else:
        node = Node()
        node.l = parse2(list_[0])
        node.r = parse2(list_[1])
        return node

numbers = []
with open('test') as file:
    for line in file:
        node = parse(line.strip())
        numbers.append(node)

def add_to_node(node, num, to_add, seen_node_number=0):
    # print(f'adding; {node=}, {to_add=}, {seen_node_number=}')
    if num < 0:
        return

    for i, child in enumerate([node.l, node.r]):
        # print(f'adding; {node=}, {num=}, {seen_node_number=}, {child=}')
        if type(child) == int:
            if seen_node_number == num:
                print(f'adding {to_add} to child number {num}')
                if i == 0:
                    node.l += to_add
                else:
                    node.r += to_add
            # print(f'{child=}, {seen_node_number=}')
            seen_node_number += 1
        else:
            seen_node_number = add_to_node(child, num, to_add, seen_node_number + 0)

    # print('returning', seen_node_number)
    return seen_node_number

m = 0
def reduce(node, root, depth=0): # Just the first pair
    global m
    # print(f'reduce; {node=}, {depth=}, {m=}')
    res = False

    for i, child in enumerate([node.l, node.r]):
        if depth > 2 and type(child) == Node and type(child.l) == type(child.r) == int:
            print(f'{root} exploding: {child=}, {m=}')
            add_to_node(root, m - 1, child.l)
            add_to_node(root, m + 2, child.r)
            if i == 0:
                node.l = 0
            else:
                node.r = 0
            return True
        elif type(child) == int and child >= 10:
            print(f'{root} splitting: {child=}')
            n1 = child // 2
            n2 = math.ceil(child / 2)
            if i == 0:
                node.l = Node()
                node.l.l = n1
                node.l.r = n2
            else:
                node.r = Node()
                node.r.l = n1
                node.r.r = n2
            return True
        else:
            if type(child) == int:
                m += 1
            elif not res:
                res = reduce(child, root, depth + 1)
                if res:
                    return res
    return res

def add(num1, num2):
    global m
    m = 0
    while reduce(num1, num1):
        m = 0
        continue
    m = 0
    while reduce(num2, num2):
        m = 0
        continue
    tmp = Node()
    tmp.l = num1
    tmp.r = num2
    m = 0
    while reduce(tmp, tmp):
        m = 0
        continue
    return tmp

root = numbers[0]
for num in numbers[1:]:
    print(f'  {str(root).replace(" ", "")}')
    print(f'+ {str(num).replace(" ", "")}')
    m = 0
    root = add(root, num)
    print(f'= {str(root).replace(" ", "")}')
    print()
    break

print(root)
