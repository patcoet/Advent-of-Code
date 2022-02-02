factor_a = 16807
factor_b = 48271
dividend = 2147483647

# starting_value_a = 65
# starting_value_b = 8921
starting_value_a = 289
starting_value_b = 629

previous_value_a = starting_value_a
previous_value_b = starting_value_b

num_values = 5000000
num_matches = 0

accepted_values_a = []
accepted_values_b = []

while len(accepted_values_a) < num_values:
  product_a = previous_value_a * factor_a
  previous_value_a = product_a % dividend
  if previous_value_a % 4 == 0:
    accepted_values_a.append(previous_value_a)

while len(accepted_values_b) < num_values:
    product_b = previous_value_b * factor_b
    previous_value_b = product_b % dividend
    if previous_value_b % 8 == 0:
      accepted_values_b.append(previous_value_b)

for i in range(num_values):
  a = accepted_values_a[i]
  b = accepted_values_b[i]

  l16_a = a & ((1 << 16)-1)
  l16_b = b & ((1 << 16)-1)

  if l16_a == l16_b:
    num_matches = num_matches + 1

print(num_matches)