inputt = 'input.txt'

lines = []
with open(inputt) as file:
  for line in file:
    line = line.strip('\n')
    lines.append(line)

still_looking = True

for line in lines:
  for other_line in lines:
    if line != other_line and still_looking:
      line_length = len(line)
      matching_chars = 0
      mismatching_char = ''
      for i in range(len(line)):
        if line[i] == other_line[i]:
          matching_chars = matching_chars + 1
        else:
          mismatching_char = line[i]

      if matching_chars == line_length-1:
        still_looking = False
        print("Common letters: ", line.replace(mismatching_char, ''))