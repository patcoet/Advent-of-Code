recipes = [3, 7]
index1 = 0
index2 = 1

sequence = [7, 6, 5, 0, 7, 1]

while recipes[-len(sequence):] != sequence and recipes[-len(sequence)-1:-1] != sequence:
  score_sum = recipes[index1] + recipes[index2]
  digits = [int(d) for d in str(score_sum)]
  for digit in digits:
    recipes.append(digit)
  index1 = (index1 + recipes[index1] + 1) % len(recipes)
  index2 = (index2 + recipes[index2] + 1) % len(recipes)

print(''.join([str(r) for r in recipes]).find(''.join([str(s) for s in sequence])))