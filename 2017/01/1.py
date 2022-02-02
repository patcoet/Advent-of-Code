total = 0

with open('input.txt') as file:
  dataz = file.read()

dataz = dataz + dataz[0] # Pretend we're reading the file circularly

for i in range(len(dataz)):
  if i > 0:
    last_digit = int(dataz[i-1])
    current_digit = int(dataz[i])
    # print("last, current:", last_digit, current_digit)
    if last_digit == current_digit:
      total = total + current_digit

print(total)