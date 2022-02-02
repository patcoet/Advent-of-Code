# Given a number, returns the layer it's on (starting at 0)
def layer(x):
  for i in range(x):
    # Layer i contains numbers ((2*(i-1) + 1)^2 + 1) to ((2*i + 1)^2)
    if (i*2 + 1)**2 >= x:
      return i

# Given a layer, returns the smallest number in it
def smallest(layer):
  if layer == 0:
    return 1
  else:
    return (2*(layer - 1) + 1)**2 + 1

def largest(layer):
  return (2*layer + 1)**2

# If we know the input number is on layer k, we know that the distance is
# between k (if it's straight up/down/left/right) and 2*k (if it's in a
# corner), so if we start at smallest(k) and oscillate between those values...
def distance_to_origin(inputt):
  input_layer = layer(inputt)
  smallest_value_in_layer = smallest(input_layer)
  largest_value_in_layer = largest(input_layer)
  minimum_possible_steps = input_layer
  maximum_possible_steps = input_layer * 2

  incrementing_result = False
  result = input_layer * 2

  for i in range(largest_value_in_layer, smallest_value_in_layer, -1):
    if i == inputt:
      return result
    else:
      if result == minimum_possible_steps:
        incrementing_result = True
      elif result == maximum_possible_steps:
        incrementing_result = False

      if incrementing_result:
        result = result + 1
      else:
        result = result - 1

print(distance_to_origin(265149))