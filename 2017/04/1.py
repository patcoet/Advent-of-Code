total = 0

with open('input.txt') as file:
  for line in file:
    line_is_valid = True
    words = line.strip('\n').split(' ')

    for i in range(len(words)):
      if line_is_valid:
        for j in range(len(words)):
          if i != j and words[i] == words[j]:
            line_is_valid = False
            break

    if line_is_valid:
      total = total + 1

print(total)