factor_a = 16807
factor_b = 48271
dividend = 2147483647

starting_value_a = 289
starting_value_b = 629

previous_value_a = starting_value_a
previous_value_b = starting_value_b

num_values = 40000000
num_matches = 0

for i in range(num_values):
  product_a = previous_value_a * factor_a
  previous_value_a = product_a % dividend

  product_b = previous_value_b * factor_b
  previous_value_b = product_b % dividend

  # Magic spell from StackOverflow:
  n = 16
  bits = 1 << n
  last_16_a = previous_value_a & (bits-1)
  last_16_b = previous_value_b & (bits-1)

  if last_16_a == last_16_b:
    num_matches = num_matches + 1

print(num_matches)