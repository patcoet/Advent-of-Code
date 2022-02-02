class Point:
  def __init__(self, x, y, dx, dy):
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy

  def tick(self, num_ticks):
    return self.x + self.dx*num_ticks, self.y + self.dy*num_ticks

initial_points = []

with open('input.txt') as file:
  for line in file:
    p1 = line.find('<')+1
    p2 = line.find('>')
    p3 = line.find('<', p2)+1
    p4 = line.find('>', p3)
    pos = line[p1:p2].split(',')
    vel = line[p3:p4].split(',')
    x = int(pos[0])
    y = int(pos[1])
    dx = int(vel[0])
    dy = int(vel[1])
    initial_points.append(Point(x, y, dx, dy))

def box_size(points):
  xs = [point.x for point in points]
  ys = [point.y for point in points]
  x0 = min(xs)
  x1 = max(xs)
  y0 = min(ys)
  y1 = max(ys)
  size = (x1 - x0) * (y1 - y0)
  return size

def tick(num_ticks):
  return [Point(point.tick(num_ticks)[0], point.tick(num_ticks)[1], point.dx, point.dy) for point in initial_points]

curr_tick = 1
while True:
  old_size = box_size(tick(curr_tick))
  new_size = box_size(tick(curr_tick+1))
  if new_size > old_size:
    break
  else:
    curr_tick = curr_tick + 1

message_points = tick(curr_tick)

def print_message(points):
  xys = [(point.x, point.y) for point in points]
  xs = [point.x for point in points]
  ys = [point.y for point in points]

  for y in range(min(ys)-1, max(ys)+2):
    s = ""
    for x in range(min(xs)-1, max(xs)+2):
      if (x, y) in xys:
        s = s + "#"
      else:
        s = s + "."
    print(s)

print_message(message_points)
print(curr_tick)