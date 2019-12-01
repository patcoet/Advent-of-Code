step_amount = 369

buffer = [0]
current_index = 0

values = 50000000

buffer_length = 1
for value in range(1, values + 1):
  current_index = (current_index + step_amount+1) % buffer_length
  if current_index == 0:
    buffer.insert(1, value)
  buffer_length = buffer_length + 1

print(buffer[1])