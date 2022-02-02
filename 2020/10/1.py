ratings = []

with open("input.txt") as file:
  for line in file:
    ratings.append(int(line.strip()))

ratings.sort()
ratings.append(max(ratings) + 3)
diffs = []

for i in range(len(ratings)):
  prev = 0
  if i > 0:
    prev = ratings[i - 1]

  diffs.append(ratings[i] - prev)

print(len([x for x in diffs if x == 1]) * len([x for x in diffs if x == 3]))