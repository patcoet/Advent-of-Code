class Particle:
  def __init__(self, id, position, velocity, acceleration):
    self.id = id
    self.position = position
    self.velocity = velocity
    self.acceleration = acceleration

  def __str__(self):
    return "p=<" + str(self.position[0]) + "," + str(self.position[1]) + "," + str(self.position[2]) + ">, v=<" + str(self.velocity[0]) + "," + str(self.velocity[1]) + "," + str(self.velocity[2]) + ">, a=<" + str(self.acceleration[0]) + "," + str(self.acceleration[1]) + "," + str(self.acceleration[2]) + ">"

  def tick(self):
    p = self.position
    v = self.velocity
    a = self.acceleration
    self.velocity = [v[0] + a[0], v[1] + a[1], v[2] + a[2]]
    v = self.velocity
    self.position = [p[0] + v[0], p[1] + v[1], p[2] + v[2]]

  def distance_to_origin(self):
    return sum(map(abs, self.position))

def read(filename):
  particles = []
  i = 0
  with open(filename) as file:
    for line in file:
      parts = line.strip().split(' ')
      p = list(map(lambda x: int(x), parts[0][3:-2].split(',')))
      v = list(map(lambda x: int(x), parts[1][3:-2].split(',')))
      a = list(map(lambda x: int(x), parts[2][3:-1].split(',')))
      particles.append(Particle(i, p, v, a))
      i = i + 1
  return particles

particles = read('input.txt')

for i in range(10000):
  for particle in particles:
    particle.tick()

# This doesn't at all make sure that the closest particle will never change again, but it does happen to be correct, so...
print("Closest particle:", min(particles, key=lambda x: x.distance_to_origin()).id)
