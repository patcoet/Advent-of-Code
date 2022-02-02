preamble_length = 25
numbers = []

with open("input.txt") as file:
  for line in file:
    numbers.append(int(line.strip()))

invalid_number = 0

for i in range(preamble_length, len(numbers)):
  if not any([x + y == numbers[i] for x in numbers[i - preamble_length : i] for y in numbers[i - preamble_length : i] if x != y]):
    invalid_number = numbers[i]
    break

done = False

for i in range(len(numbers)):
  numbers2 = []
  if done:
    break

  for j in range(i, len(numbers)):
    numbers2.append(numbers[j])

    if sum(numbers2) == invalid_number:
      done = True
      print(min(numbers2) + max(numbers2))
      break
    elif sum(numbers2) > invalid_number:
      break
