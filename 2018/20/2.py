import re

regex = ""

with open('input.txt') as file:
  regex = file.readline().strip()[1:-1]

p = re.compile('(\w+)\|\)')
regex = p.sub(lambda x: x.group(1)[:len(x.group(1))//2] + '|)', regex)

area_map = {}

min_x = 0
max_x = 0
min_y = 0
max_y = 0

area_map[(0, 0)] = 'X'

class Room:
  def __init__(self, pos, n=None, s=None, w=None, e=None):
    self.pos = pos
    self.n = n
    self.s = s
    self.w = w
    self.e = e

  def neighbors(self):
    result = []
    if self.n:
      result.append(self.n)
    if self.s:
      result.append(self.s)
    if self.w:
      result.append(self.w)
    if self.e:
      result.append(self.e)
    return result

rooms = {}
rooms[(0, 0)] = Room((0, 0))

def dig(starting_point, string):
  global min_x, max_x, min_y, max_y

  a = string.find('(')
  if a == -1:
    curr_point = starting_point
    for char in string:
      x, y = curr_point
      if char == 'N':
        area_map[x, y-1] = '-'
        area_map[x, y-2] = '.'
        min_y = min(min_y, y-2)
        prev_point = curr_point
        curr_point = (x, y-2)
        rooms[curr_point] = Room(curr_point, s=rooms[prev_point])
        rooms[prev_point].n = rooms[curr_point]
      elif char == 'S':
        area_map[x, y+1] = '-'
        area_map[x, y+2] = '.'
        max_y = max(max_y, y+2)
        prev_point = curr_point
        curr_point = (x, y+2)
        rooms[curr_point] = Room(curr_point, n=rooms[prev_point])
        rooms[prev_point].s = rooms[curr_point]
      elif char == 'W':
        area_map[x-1, y] = '|'
        area_map[x-2, y] = '.'
        min_x = min(min_x, x-2)
        prev_point = curr_point
        curr_point = (x-2, y)
        rooms[curr_point] = Room(curr_point, e=rooms[prev_point])
        rooms[prev_point].w = rooms[curr_point]
      elif char == 'E':
        area_map[x+1, y] = '|'
        area_map[x+2, y] = '.'
        max_x = max(max_x, x+2)
        prev_point = curr_point
        curr_point = (x+2, y)
        rooms[curr_point] = Room(curr_point, w=rooms[prev_point])
        rooms[prev_point].e = rooms[curr_point]
    return curr_point
  else:
    pre = string[:a]
    curr_point = dig(starting_point, pre)

    level = 0
    b = -1
    splits = [a+1]
    subs = []
    for i in range(len(string)):
      char = string[i]
      if char == '(':
        level = level + 1
      elif char == ')':
        level = level - 1
        if level == 0:
          b = i
          subs.append(string[splits[-1]:b])
          break
      elif char == '|' and level == 1:
        subs.append(string[splits[-1]:i])
        splits.append(i)

    for sub in subs:
      dig(curr_point, sub)

    post = string[b+1:]

    dig(curr_point, post)

dig((0, 0), regex)

# def print_map():
#   for y in range(min_y-1, max_y+2):
#     s = ""
#     for x in range(min_x-1, max_x+2):
#       s = s + (area_map[(x, y)] if (x, y) in area_map.keys() else '#')
#     print(s)

# print_map()

def dijk():
  unvisited_rooms = []
  dist = {}

  for room in rooms.values():
    unvisited_rooms.append(room)
    dist[room.pos] = 999999999

  curr_room = rooms[(0, 0)]
  dist[curr_room.pos] = 0

  while unvisited_rooms:
    curr_room = min(unvisited_rooms, key=lambda x: dist[x.pos])

    unvisited_rooms.remove(curr_room)

    for neighbor in curr_room.neighbors():
      alt = dist[curr_room.pos] + 1
      if alt < dist[neighbor.pos]:
        dist[neighbor.pos] = alt

  return dist

distances = dijk()

print(len([distance for distance in distances.values() if distance >= 1000]))

