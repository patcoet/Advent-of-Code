step_amount = 369

buffer = [0]
value = 1
current_index = 0

while value <= 2017:
  # print(buffer)
  current_index = (current_index + step_amount+1) % len(buffer)
  buffer.insert(current_index+1, value)
  value = value + 1

print(buffer[current_index-1:current_index+5])