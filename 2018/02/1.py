inputt = 'input.txt'

twos = 0
threes = 0

with open(inputt) as file:
  for line in file:
    line = line.strip('\n')
    # print("Line:", line)

    looking_for_twos = True
    looking_for_threes = True

    while len(line) > 0:
      char = line[0]
      if line.count(char) == 2 and looking_for_twos:
        # print("Found two of:", char)
        twos = twos + 1
        looking_for_twos = False
      elif line.count(char) == 3 and looking_for_threes:
        # print("Found three of:", char)
        threes = threes + 1
        looking_for_threes = False
      line = line.replace(char, '')



print("Twos:", twos)
print("Threes:", threes)
print("Checksum:", twos * threes)
