# Day 8: Space Image Format
# Compute what the final image looks like after stacking its layers.

data = None

with open("input.txt") as file:
  data = file.readline().strip() # All the image data in one list of strings (single characters).

width = 25
height = 6

layer_length = width * height

num_layers = len(data) // layer_length

layers = [data[i * layer_length : (i + 1) * layer_length] for i in range(num_layers)]

image = [""] * layer_length
for i, pixel in enumerate(layers[0]):
  for layer in layers:
    if layer[i] in ["0", "1"]:
      image[i] = layer[i]
      break

def pprint(img):
  for i in range(height):                                                          # For each line of the image:
    print("".join(img[i*width : (i+1)*width]).replace("0", " ").replace("1", "#")) # Take a list of one-character strings, turn it into one string, replace 0s with spaces, replace 1s with #s, and print.

pprint(image)
