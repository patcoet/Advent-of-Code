inputt = 'input.txt'

class Layer:
  def __init__(self, depth, range, position=1, direction='down'):
    self.depth = depth
    self.range = range
    self.position = position
    self.direction = direction

  def tick(self):
    if self.direction == 'down' and self.position == self.range:
      self.direction = 'up'
    if self.direction == 'up' and self.position == 1:
      self.direction = 'down'

    if self.direction == 'down':
      self.position = self.position + 1
    else:
      self.position = self.position - 1

layers = []
last_firewall_layer = 0
with open(inputt) as file:
  for line in file:
    words = line.split(':')
    depth = int(words[0])
    range = int(words[1])
    layers.append(Layer(depth, range))
    last_firewall_layer = max(last_firewall_layer, depth)

def tick():
  for layer in layers:
    layer.tick()

packet_position = 0
total_penalty = 0
while packet_position <= last_firewall_layer:
  current_layer = packet_position
  for layer in layers:
    if layer.depth == current_layer and layer.position == 1:
      total_penalty = total_penalty + layer.depth*layer.range
  packet_position = packet_position + 1
  tick()

print("Severity:", total_penalty)