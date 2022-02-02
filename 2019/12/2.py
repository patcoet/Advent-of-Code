# Day 12: The N-Body Problem (part 2)
# Determine how many steps it will take for the moons to come back to the starting state.
# Idea: Since each moon's movement and velocity along each axis is independent of the other axes, we can take the least common multiple of moon 0's X state, Y state, and Z state, moon 1's, and moon 2's, and that'll be our answer.

class Moon:
  def __init__(self, position):
    self.position = position
    self.velocity = [0, 0, 0]

  def total_energy(self):
    potential = sum(map(abs, self.position))
    kinetic = sum(map(abs, self.velocity))
    return potential * kinetic

  def copy(self):
    new_moon = Moon(self.position.copy())
    new_moon.velocity = self.velocity.copy()
    return new_moon

  def __eq__(self, other):
    return self.position == other.position and self.velocity == other.velocity

def step(moons):
  for moon in moons:
    moon.gravity = [0, 0, 0]
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

moons2 = [moon.copy() for moon in moons]

repeats_at = {}
step_num = 0
done = {}
while len(done) < 4 * 3:
  step_num += 1
  step(moons2)
  for i, moon in enumerate(moons2):
    for axis in [0, 1, 2]:
      if (i, axis) in done.keys() and done[(i, axis)]:
        continue
      if moons[i].position[axis] == moon.position[axis] and moons[i].velocity[axis] == moon.velocity[axis]:
        if (i, axis) not in repeats_at.keys():
          repeats_at[(i, axis)] = [step_num]
        else:
          repeats_at[(i, axis)].append(step_num)
        if len(repeats_at[(i, axis)]) > 25:
          done[(i, axis)] = True

# I don't know why this part is needed:
to_calculate_lcm_of = []
for moon, axis in repeats_at:
  nums = repeats_at[(moon, axis)]
  done = False
  for i in range(len(nums)):
    if done: break
    for j in range(i+1, len(nums)):
      if (nums[j] / nums[i]).is_integer():
        to_calculate_lcm_of.append(nums[i])
        done = True
        break

# Python doesn't come with an LCM function, but Wikipedia tells me that LCM(a, b) = |a*b| / GCD(a, b) and there is a math.gcd, so:
import math
def lcm(a, b):
  return int(abs(a * b) / math.gcd(a, b))

# Then we just use functools.reduce to make that take a list of numbers:
import functools
def lcms(xs):
  return functools.reduce(lcm, xs)

print(lcms(to_calculate_lcm_of[3:])) # I also don't know why this slice is needed. Oh well!!!
