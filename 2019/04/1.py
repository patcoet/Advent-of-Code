# Day 4: Secure Container
# Task: Find how many numbers within a given range meet criteria.

# Our puzzle input is that we're looking for numbers in the range 246515-739105 (inclusive, I assume).
input_low  = 246515
input_high = 739105

# Criteria for the password:
# * It is a six-digit number
# * The value is within the range given in your puzzle input
# * Two adjacent digits are the same (like 22 in 122345)
# * Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)

# Since we only have 500k numbers to check, it seems reasonable to just do a loop from the low end to the high and increment a counter.

password_hits = 0

for num in range(input_low, input_high + 1):
  num_str = str(num) # Turn the number into a string for easy access to digits.

  six_digits = len(num_str) == 6

  # If we cared about speed we could put if not six_digits: continue here (and same below), but this is already fast enough.
  # I assume turning each number into a string to do these checks is also slower than using math on the original numbers, but this was easier to write.

  has_pair = False
  for i, digit in enumerate(num_str):
    if i > 0:
      if num_str[i-1] == digit:
        has_pair = True

  digits_never_decrease = True
  for i, digit in enumerate(num_str):
    if i > 0:
      if num_str[i-1] > digit:
        digits_never_decrease = False

  if six_digits and has_pair and digits_never_decrease:
    password_hits += 1

print(f"{password_hits} passwords within the range {input_low}-{input_high} fit the criteria.")