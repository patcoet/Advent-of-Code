recipes = [3, 7]
index1 = 0
index2 = 1

num_first = 765071
num_after = 10
while len(recipes) < num_first + num_after:
  score_sum = recipes[index1] + recipes[index2]
  digits = [int(d) for d in str(score_sum)]
  for digit in digits:
    recipes.append(digit)
  index1 = (index1 + recipes[index1] + 1) % len(recipes)
  index2 = (index2 + recipes[index2] + 1) % len(recipes)

print(recipes[-num_after:])