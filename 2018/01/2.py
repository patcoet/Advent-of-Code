current_frequency = 0
previous_frequencies = { current_frequency }
still_looking = True

while still_looking:
  with open('input.txt') as file:
    for line in file:
      new_frequency = int(line)
      # print("Current frequency before adding: " + str(current_frequency))
      # print("Adding: " + str(new_frequency))
      current_frequency = current_frequency + new_frequency
      # print("Current frequency after adding: " + str(current_frequency))
      # print("Previous frequencies: " + str(previous_frequencies) + "\n---")

      if {current_frequency}.issubset(previous_frequencies):
        print("Frequency first reached twice: " + str(current_frequency))
        still_looking = False
        break
      else:
        previous_frequencies.add(current_frequency)

