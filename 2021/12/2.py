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

def explore(explored):
    last = explored[-1]
    if last == 'end':
        paths.append(explored)
        return

    no_doubles = all(explored.count(x) < 2 for x in explored if x.islower())
    for connection in nodes[last].connections:
        if connection == 'start':
            continue
        if connection.isupper() or connection not in explored or no_doubles:
            explore(explored + [connection])

with open('input') as file:
    for line in file:
        node1, node2 = re.findall('(\w+)-(\w+)', line.strip())[0]
        Node(node1)
        nodes[node1].add_connection(node2)

paths = []
explore(['start'])

print(len(paths))
