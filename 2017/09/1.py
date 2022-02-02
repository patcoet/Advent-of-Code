inputt = 'input.txt'

stream = ''
with open(inputt) as file:
  stream = file.read().strip('\n')

# print("Input:", stream)

# Delete !s and following characters
length = len(stream)
i = 0
while i < length:
  if stream[i] == '!':
    stream = stream[0:i] + stream[i+2 : length]
  else:
    i = i + 1
  length = len(stream)

# print("!s removed:", stream)

# Delete garbage patches
i = 0
length = len(stream)
while i < length:
  if stream[i] == '<':
    for j in range(i+1, len(stream)):
      if stream[j] == '>':
        # print("Garbage patch:", stream[i:j+1])
        stream = stream[0:i] + stream[j+1 : len(stream)]
        i = i - 1
        break
  length = len(stream)
  i = i + 1

# print("Garbage removed:", stream)

# Count points
tmp = 0
total_score = 0
for i in range(0, len(stream)):
  curr_char = stream[i]
  if curr_char == '{':
    tmp = tmp + 1
  elif curr_char == '}':
    total_score = total_score + tmp
    tmp = tmp - 1

# print(stream)

print("Total score:", total_score)