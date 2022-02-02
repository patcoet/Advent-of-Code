import regex

lines = []

with open("input.txt") as file:
  for line in file:
    lines.append(regex.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line).groups()) # "8-10 r: rwrrtrvttrrrr" -> ("8", "10", "r", "rwrrtrvttrrrr")

valid_counter = 0

for line in lines:
  min_ = int(line[0])
  max_ = int(line[1])
  c = line[2]
  s = line[3]
  ds = s.replace(c, "") # The password with the special letters removed, so len(s) - len(ds) is the number of those letters
  if min_ <= len(s) - len(ds) <= max_:
    valid_counter += 1

print(valid_counter)