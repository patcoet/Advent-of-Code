lines = 0
totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('input') as file:
  for line in file:
    for n, char in enumerate(line.strip()):
      totals[n] += int(char)
    lines += 1

most_common = [x > (lines / 2) for x in totals]

# Should be done with int(s, 2) instead:
gamma = 0
epsilon = 0
multiplier = 1
for n in reversed(most_common):
  gamma += n * multiplier
  epsilon += (not n) * multiplier
  multiplier *= 2

print(gamma * epsilon)
