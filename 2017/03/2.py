def layer_of(x):
  for i in range(x):
    # Layer i contains numbers ((2*(i-1) + 1)^2 + 1) to ((2*i + 1)^2)
    if (i*2 + 1)**2 >= x:
      return i

inputt = 265149
input_layer = layer_of(inputt) + 1

matrix = {}

for i in range(-input_layer, input_layer):
  matrix[i] = {}
  for j in range(-input_layer, input_layer):
    matrix[i][j] = {'number': -1, 'value': 0}

matrix[0][0] = {'number': 1, 'value': 1}
curr_x = 1
curr_y = 0
c = 2

for layer in range(1, input_layer - 1):
  while curr_x < layer:
    value = 0
    for i in range (-1, 2):
      for j in range(-1, 2):
        if not (i == 0 and j == 0):
          value = value + matrix[curr_x + i][curr_y + j]['value']
    matrix[curr_x][curr_y] = {'number': c, 'value': value}
    curr_x = curr_x + 1
    c = c + 1
  while curr_y < layer:
    value = 0
    for i in range (-1, 2):
      for j in range(-1, 2):
        if not (i == 0 and j == 0):
          value = value + matrix[curr_x + i][curr_y + j]['value']
    matrix[curr_x][curr_y] = {'number': c, 'value': value}
    curr_y = curr_y + 1
    c = c + 1
  while curr_x > -layer:
    value = 0
    for i in range (-1, 2):
      for j in range(-1, 2):
        if not (i == 0 and j == 0):
          value = value + matrix[curr_x + i][curr_y + j]['value']
    matrix[curr_x][curr_y] = {'number': c, 'value': value}
    curr_x = curr_x - 1
    c = c + 1
  while curr_y > -layer:
    value = 0
    for i in range (-1, 2):
      for j in range(-1, 2):
        if not (i == 0 and j == 0):
          value = value + matrix[curr_x + i][curr_y + j]['value']
    matrix[curr_x][curr_y] = {'number': c, 'value': value}
    curr_y = curr_y - 1
    c = c + 1

largers = []

for i in range(-input_layer, input_layer):
  for j in range(-input_layer, input_layer):
    value = matrix[i][j]['value']
    if value > inputt:
      largers.append(value)

print(min(largers))