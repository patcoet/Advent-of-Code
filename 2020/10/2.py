ratings = [0]

with open("input.txt") as file:
  for line in file:
    ratings.append(int(line.strip()))

ratings.sort()
ratings.append(max(ratings) + 3)

multipliers = []
i = 0

while i < len(ratings):
  num_ = 0
  for j in range(i+1, len(ratings)):
    if ratings[j] - ratings[j-1] == 1:
      num_ += 1
    else:
      i += num_
      multipliers.append(num_ + 1)
      break

  i += 1

total = 1
for multiplier in multipliers:
  if multiplier == 3:
    total *= 2
  elif multiplier == 4:
    total *= 4
  elif multiplier == 5:
    total *= 7

print(total)
