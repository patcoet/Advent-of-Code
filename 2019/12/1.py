# Day 12: The N-Body Problem (part 1)
# Simulate moon orbits and calculate positions and velocities.

class Moon:
  def __init__(self, position):
    self.position = position
    self.velocity = [0, 0, 0]
    self.gravity = [0, 0, 0]

  def total_energy(self):
    potential = sum(map(abs, self.position))
    kinetic = sum(map(abs, self.velocity))
    return potential * kinetic

  def __repr__(self):
    return f"{(self.position, self.velocity)}"

def step(steps):
  for i in range(steps):
    for moon in moons:
      for other_moon in moons:
        if moon != other_moon:
          for i in range(len(moon.position)):
            if moon.position[i] < other_moon.position[i]:
              moon.gravity[i] += 1
            elif moon.position[i] > other_moon.position[i]:
              moon.gravity[i] -= 1

    for moon in moons:
      for i in range(len(moon.position)):
        moon.velocity[i] += moon.gravity[i]
        moon.gravity[i] = 0
        moon.position[i] += moon.velocity[i]

moons = []
with open("input.txt") as file: # Input is four lines that look like "<x=14, y=15, z=-2>\n".
  for line in file:
    position = list(map(int, "".join(list(filter(lambda x: x.isdigit() or x == "," or x == "-", line))).split(","))) # Turn "<x=14, y=15, z=-2>\n" into [14, 15, -2]. Listen: I don't think this is better than a regex would be, but I'm too lazy to look up how to regex right now.
    moons.append(Moon(position))

num_steps = 1000

step(num_steps)

print(f"Position, velocity, and total kinetic energy of each moon after {num_steps} steps:")
for m in moons: print(m.position, m.velocity, m.total_energy())
print()
print(f"Total energy of all moons: {sum([m.total_energy() for m in moons])}")

