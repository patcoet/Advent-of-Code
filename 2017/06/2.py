banks = []
inputt = 'test1.txt'
inputt = 'input.txt'

with open(inputt) as file:
  banks = [int(i) for i in file.read().strip('\n').split('\t')]

# print(banks)

previous_outputs = []

new_banks = []
for i in range(len(banks)):
  new_banks.append(banks[i])
previous_outputs.append(new_banks)

still_looking = True
counter = 0

while still_looking:
  chosen_bank_index = -1
  blocks_to_redistribute = 0
  for i in range(len(banks)):
    if banks[i] == max(banks):
      chosen_bank_index = i + 1
      blocks_to_redistribute = banks[i]
      banks[i] = 0
      break

  for i in range(chosen_bank_index, chosen_bank_index + blocks_to_redistribute):
    index = i % len(banks)
    banks[index] = banks[index] + 1

  # print(banks)
  counter = counter + 1

  for i in range(len(previous_outputs)):
    if previous_outputs[i] == banks:
      print(i, counter, counter - i)
  if banks in previous_outputs:
    print(counter)
    still_looking = False
    break
  else:
    new_banks = []
    for i in range(len(banks)):
      new_banks.append(banks[i])
    previous_outputs.append(new_banks)


# print(banks)

# i = 0
# while i < len(blocks)*2:
#   print(blocks[i % len(blocks)])
#   i = i + 1

# print(0 % 10)