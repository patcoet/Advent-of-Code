total = 0

with open('input.txt') as file:
  dataz = file.read()

list_length = len(dataz)

dataz = dataz + dataz # Pretend we're wrapping around to look ahead

for i in range(list_length):
  current_digit = int(dataz[i])
  next_digit = int(dataz[i + list_length//2])
  # print("last, current:", last_digit, current_digit)
  if current_digit == next_digit:
    total = total + current_digit

print(total)