total = 0

with open('input.txt') as file:
  for line in file:
    values = line.split('\t')
    for i in range(len(values)):
      values[i] = int(values[i]) # Can you tell I don't know Python?
    smallest_value = min(values)
    largest_value = max(values)
    value_difference = largest_value - smallest_value
    total = total + value_difference

print(total)
