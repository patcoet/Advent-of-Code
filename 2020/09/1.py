preamble_length = 25
numbers = []

with open("input.txt") as file:
  for line in file:
    numbers.append(int(line.strip()))

for i in range(preamble_length, len(numbers)):
  if not any([x + y == numbers[i] for x in numbers[i - preamble_length : i] for y in numbers[i - preamble_length : i] if x != y]):
    print(numbers[i])
    break