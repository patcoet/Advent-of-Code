total = 0

with open('input.txt') as file:
  for line in file:
    values = line.split('\t')
    for i in range(len(values)):
      values[i] = int(values[i])

    done = False
    for value in values:
      if not done:
        for other_value in values:
          if value != other_value:
            smaller_value = min(value, other_value)
            larger_value = max(value, other_value)
            if larger_value % smaller_value == 0:
              remainder = larger_value // smaller_value
              total = total + remainder
              done = True
              break

print(total)

