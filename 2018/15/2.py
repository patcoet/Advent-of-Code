class Unit:
  def __init__(self, pos, team, hp=200, power=3):
    self.pos = pos
    self.team = team
    self.hp = hp
    self.power = power

  def __str__(self):
    return self.team + str(self.pos) + ":" + str(self.hp)

  def __repr__(self):
    return str(self)

  def neighbors(self):
    x, y = self.pos
    return [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]

  def reachable_coords(self):
    reachable = set()
    def recurse(coord, visited):
      if area_map[coord] == '.':
        visited.add(coord)
        reachable.add(coord)
        x, y = coord
        neighbors = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
        for neighbor in neighbors:
          if neighbor not in visited:
            recurse(neighbor, visited)

    for neighbor in self.neighbors():
      recurse(neighbor, {neighbor})

    return reachable

  def dijk_to(self, target):
    unvisited_squares = self.reachable_coords()
    unvisited_squares.add(self.pos)
    distances = {}
    prev = {}
    for square in unvisited_squares:
      distances[square] = 999
      prev[square] = None
    distances[self.pos] = 0

    curr_cell = self.pos

    while unvisited_squares:
      curr_cell = min(unvisited_squares, key=lambda x: distances[x])
      unvisited_squares.remove(curr_cell)

      if curr_cell == target:
        return distances[curr_cell]

      x, y = curr_cell
      neighbors = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
      for neighbor in neighbors:
        if neighbor in unvisited_squares:
          alt = distances[curr_cell] + 1
          if alt < distances[neighbor]:
            distances[neighbor] = alt
            prev[neighbor] = curr_cell

    return 999

  def next_step(self):
    enemy_neighbors = []
    for unit in units:
      if unit.team != self.team and unit.hp > 0:
        for neighbor in unit.neighbors():
          if neighbor in self.reachable_coords():
            enemy_neighbors.append((neighbor, self.dijk_to(neighbor)))

    closest_enemy_neighbors = [neighbor for neighbor in enemy_neighbors if neighbor[1] == min(enemy_neighbors, key=lambda x: x[1])[1]]
    closest_enemy_neighbors.sort(key=lambda x: x[0][0])
    closest_enemy_neighbors.sort(key=lambda x: x[0][1])

    if closest_enemy_neighbors:
      target = closest_enemy_neighbors[0][0]

      before = self.pos
      map_before = area_map[self.pos]
      step = self.pos
      distance_from_self_to_target = self.dijk_to(target)
      for neighbor in self.neighbors():
        if neighbor in self.reachable_coords():
          neighbor_map_before = area_map[neighbor]
          area_map[neighbor] = map_before
          area_map[before] = '.'
          self.pos = neighbor
          distance_from_neighbor_to_target = self.dijk_to(target)
          area_map[neighbor] = neighbor_map_before
          area_map[before] = map_before
          if distance_from_neighbor_to_target == distance_from_self_to_target - 1:
            step = neighbor
            break

      self.pos = before
      return step
    return self.pos

  def move(self):
    if not self.select_target():
      before = self.pos
      area_map[self.pos] = '.'
      self.pos = self.next_step()
      area_map[self.pos] = self.team

  def select_target(self):
    enemies_in_range = [unit for unit in units if unit.hp > 0 and unit.team != self.team and unit.pos in self.neighbors()]
    enemies_with_lowest_health = [enemy for enemy in enemies_in_range if enemy.hp == min(enemies_in_range, key=lambda x: x.hp).hp]
    target = None
    for neighbor in self.neighbors():
      if not target:
        for enemy in enemies_with_lowest_health:
          if enemy.pos == neighbor:
            target = enemy
            break
    return target

  def attack(self):
    target = self.select_target()
    if target:
      target.hp = target.hp - self.power
      if target.hp <= 0:
        area_map[target.pos] = '.'

def read(filename):
  area_map = {}
  units = []
  with open(filename) as file:
    y = 0
    for line in file:
      for x in range(len(line)):
        if line[x] == 'G' or line[x] == 'E':
          units.append(Unit((x, y), line[x]))
        area_map[x, y] = line[x]
      y = y + 1
  return area_map, units

def print_map(area_map):
  for y in range(max(area_map.keys(), key=lambda x: x[1])[1]+1):
    s = ""
    for x in range(max(area_map.keys(), key=lambda x: x[0])[0]):
      s = s + area_map[(x, y)]
    print(s)

def fight(units):
  turn = 0
  while True:
    units.sort(key=lambda x: x.pos[0])
    units.sort(key=lambda x: x.pos[1])
    for unit in units:
      if unit.hp <= 0:
        units.remove(unit)
    turn = turn + 1

    for i in range(len(units)):
      unit = units[i]
      if unit.hp > 0:
        possible_targets = len([enemy for enemy in units if unit.team != enemy.team and enemy.hp > 0])
        if possible_targets == 0:
          return turn-1, sum([unit.hp for unit in units if unit.hp > 0])

        unit.move()
        unit.attack()

    for unit in units:
      if unit.hp <= 0:
        units.remove(unit)

def buff_elves(units, amount):
  for unit in units:
    if unit.team == 'E':
      unit.power = unit.power + amount
  return units

for filename in ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt', 'test6.txt', 'input.txt']:
  n = 1
  print(filename)
  while True:
    # print(n)
    area_map, units = read(filename)
    starting_elves = len([unit for unit in units if unit.team == 'E'])
    units = buff_elves(units, n)
    rounds, hp = fight(units)
    remaining_elves = len([unit for unit in units if unit.team == 'E' and unit.hp > 0])
    if remaining_elves == starting_elves:
      print(units[0].power)
      print(rounds * hp)
      break
    else:
      n = n + 1
