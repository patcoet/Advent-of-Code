keys = []

with open("input.txt") as file:
  for line in file:
    keys.append(int(line.strip()))

divisor = 20201227
subject_number = 7

value = 1
n = 0

while value != keys[0]:
  value *= subject_number
  value = value % divisor
  n += 1

value = 1
for i in range(n):
  value *= keys[1]
  value = value % divisor

print(value)