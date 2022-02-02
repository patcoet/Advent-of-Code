import regex

lines = []

with open("input.txt") as file:
  for line in file:
    lines.append(regex.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line).groups()) # "8-10 r: rwrrtrvttrrrr" -> ("8", "10", "r", "rwrrtrvttrrrr")

valid_counter = 0

for line in lines:
  p1 = int(line[0])
  p2 = int(line[1])
  c = line[2]
  s = line[3]
  if (s[p1-1] == c or s[p2-1] == c) and s[p1-1] != s[p2-1]:
    valid_counter += 1

print(valid_counter)