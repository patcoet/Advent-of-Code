class Point:
  def __init__(self, a, b, c, d):
    self.a = a
    self.b = b
    self.c = c
    self.d = d

  def __str__(self):
    return str(self.a) + "," + str(self.b) + "," + str(self.c) + "," + str(self.d)

  def __repr__(self):
    return str(self)

  def distance_to(self, other):
    a = abs(other.a - self.a)
    b = abs(other.b - self.b)
    c = abs(other.c - self.c)
    d = abs(other.d - self.d)
    return a+b+c+d

  def is_close_to(self, other):
    return self.distance_to(other) <= 3

def get_points(filename):
  points = []

  with open(filename) as file:
    for line in file:
      nums = line.strip().split(',')
      a = int(nums[0])
      b = int(nums[1])
      c = int(nums[2])
      d = int(nums[3])
      points.append(Point(a, b, c, d))

  return points

def get_constellations(points):
  constellations = []

  for point in points:
    constellations.append({point})

  for i in range(len(constellations)):
    last = 0
    while len(constellations[i]) != last:
      last = len(constellations[i])
      for j in range(i+1, len(constellations)):
        if any([point.is_close_to(point2) for point in constellations[i] for point2 in constellations[j]]):
          constellations[i] = constellations[i].union(constellations[j])
          constellations[j].clear()

  constellations = [constellation for constellation in constellations if constellation != set()]

  return constellations

test1 = get_constellations(get_points('test1.txt'))
test2 = get_constellations(get_points('test2.txt'))
test3 = get_constellations(get_points('test3.txt'))
test4 = get_constellations(get_points('test4.txt'))

for t in [test1, test2, test3, test4]:
  print(len(t), t)

print(len(get_constellations(get_points('input.txt'))))
