# Day 8: Space Image Format
# Find the layer of a given elf image that contains the fewest 0 digits.

data = None

with open("input.txt") as file:
  data = file.readline().strip() # All the image data in one string.

width = 25
height = 6

layer_length = width * height

num_layers = len(data) // layer_length

layers = [data[i * layer_length : (i + 1) * layer_length] for i in range(num_layers)]

def how_many(c, cs):
  return len(list(filter(lambda x: x == c, cs)))

target_layer = min(layers, key=lambda x: how_many("0", x))

print(f'1s * 2s in layer with fewest 0s: {how_many("1", target_layer) * how_many("2", target_layer)}')
