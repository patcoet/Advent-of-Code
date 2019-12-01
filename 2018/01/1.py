current_frequency = 0

with open('input.txt') as file:
  for line in file:
    new_frequency = int(line)
    print("Current frequency before adding: " + str(current_frequency))
    print("Adding: " + str(new_frequency))
    current_frequency = current_frequency + new_frequency
    print("Current frequency after adding: " + str(current_frequency) + "\n---")

