total = 0

with open('input.txt') as file:
  for line in file:
    line_is_valid = True
    words = line.strip('\n').split(' ')
    print("Line is:", line.strip('\n'))

    for i in range(len(words)):
      if line_is_valid:
        for j in range(len(words)):
          if i != j:
            word = words[i]
            other_word = words[j]
            # print("Word:", word)
            # print("Other word:", other_word)
            sorted_word = ''.join(sorted(word))
            sorted_other_word = ''.join(sorted(other_word))
            # print(word, sorted_word, other_word, sorted_other_word)
            if sorted_word == sorted_other_word:
              # print("break")
              line_is_valid = False
              break

    if line_is_valid:
      total = total + 1

print(total)
