# Day 12: The N-Body Problem (part 2)
# Determine how many steps it will take for the moons to come back to the starting state.

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

  def copy(self):
    new_moon = Moon(self.position.copy())
    new_moon.velocity = self.velocity.copy()
    return new_moon

  def __eq__(self, other):
    return self.position == other.position and self.velocity == other.velocity


def step(moons):
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

# The step function above works for verifying that the system repeats after 2772 steps with test1.txt, but it's way too slow for the second example that takes 4686774924 steps, and presumably the real input.
# 4686774924 is a big enough number that we can probably be pretty sure that there's a way to do this that doesn't involve simulating every step, since even just counting from 0 to 4686774924 takes a long time.
# The position and velocity of each moon change each step depending on the positions of the other moons, but the axes are independent.
# What comes to my mind is that maybe we could run the simulation until moon 0 has repeated and note how many steps that took, and same with the others, and then the answer would be the lowest common multiple of those numbers. I tried this, but it also seems too slow.
# But maybe if we repeat that trick, and check when the (x-position, x-velocity) of moon 0 repeats, when y-, and when z-, and take the LCM of those, that will help.
# Before we try it, can we prove that it will work? We would want to know that moon 1 repeats every x steps and only every x steps, and same with the others. I guess we can compromise by checking on test1...

moons2 = [moon.copy() for moon in moons]

# for i in range(2772):
#   step(moons2)

# print(moons2)

done = False
i = 0
axis = 2
moon_num = 2
comparison_moon = moons[moon_num].copy()
repeats = []
while not done:
  i += 1
  step(moons2)
  moon = moons2[moon_num]
  if i > 1000 and comparison_moon.position[axis] == moon.position[axis] and comparison_moon.velocity[axis] == moon.velocity[axis]:
    repeats.append(i)
    if len(repeats) > 25:
      break

# print()
print(repeats)
done = False
for i in range(len(repeats)):
  for j in range(i+1, len(repeats)):
    if (repeats[j] / repeats[i]).is_integer():
      print(repeats[i])
      done = True
      break
  if done: break

# 0, x: 84032
# 0, y: 231614
# 0, z: 193052

# 1, x: 84032
# 1, y: 231614
# 1, z: 193052

# 2, x: 84032
# 2, y: 231614
# 2, z: 193052

# LCM: 469671086427712
# Correct! Wow. OK, great. I will clean all this up and make it automatic... tomorrow. I'm going to commit this mess to have a record of the before and after.














# print(list(map(lambda x: x/21, repeats)))
# moon 0 x repeats: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, ...]
# moon 0 y repeats: [28, 56, 84, 112, 140, 168, 196, 224, 252, 280, 308, ...]
# moon 0 z repeats: [44, 88, 132, 176, 220, 264, 308, 352, 396, 440, 484, ...]
# moon 0 total: 924
# moon 1 x: 9
# moon 1 y: 28
# moon 1 z: 44
# moon 1 total: 2772
# moon 2 x: 18
# moon 2 y: 28
# moon 2 z: 44
# moon 2 total: 2772

# 2772 = 924 * 3, so we expect the whole state to repeat every 2772 steps, since that's the lowest common multiple of 924, 2772, and 2772. 2772 is (of course) also the lowest common multiple of 6, 9, 18, 28, and 44, so it seems we can skip those intermediate steps.

# For test2:
# 0, x: 2028
# 0, y: weird and complicated, but contains 5898
# 0, z: weird, but contains 4702 = 2351*2
# 1, x: weird, but contains 2028, and 4056, and 6084, 8112, 10140, ...
# 1, y: 5898
# 1, z: weird, but contains 4702
# 2, x: 2028
# 2, y: 5898
# 2, z: weird, but contains 4702

# LCM of those four simple numbers is 1993524, which is a divisor of 4686774924 (2351 (prime...)), so it seems right thus far... but why the weird and complicated results?

# LCM(2028, 5898, 4702) = 4686774924!
# So apparently we have the numbers we want and also some garbage numbers. Maybe we can look at the first 10 or whatever hits, and filter for numbers that have multiples in that list.