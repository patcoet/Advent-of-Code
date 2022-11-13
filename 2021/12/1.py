import re

nodes = {}

class Node:
    def __init__(self, name):
        if name not in nodes:
            self.name = name
            self.connections = []
            nodes[name] = self

    def add_connection(self, connection):
        self.connections.append(connection)
        if connection not in nodes:
            Node(connection)
        if self.name not in nodes[connection].connections:
            nodes[connection].add_connection(self.name)

def explore(path_so_far):
    last = path_so_far[-1]
    if last == 'end':
        paths.append(path_so_far)
        return

    for connection in nodes[last].connections:
        if connection.isupper() or connection not in path_so_far:
            explore(path_so_far + [connection])

with open('input') as file:
    for line in file:
        node1, node2 = re.findall('(\w+)-(\w+)', line.strip())[0]
        Node(node1)
        nodes[node1].add_connection(node2)

paths = []
explore(['start'])

print(len(paths))
