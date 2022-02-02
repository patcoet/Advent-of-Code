inputt = 'input.txt'

class Layer:
  def __init__(self, depth, range):
    self.depth = depth
    self.range = range

  def position_at_tick(self, tick):
    mod = (self.range-1)*2
    if tick % mod == 0:
      return 1
    else:
      for i in range(0, mod):
        if tick % mod == i or tick % mod == mod-i:
          return i+1

layers = {}
last_firewall_layer = 0
with open(inputt) as file:
  for line in file:
    words = line.split(':')
    depth = int(words[0])
    rrange = int(words[1])
    layers[depth] = Layer(depth, rrange)
    last_firewall_layer = max(last_firewall_layer, depth)

def send_packet(delay):
  total_penalty = 0
  caught = False
  current_tick = delay
  current_layer = 0

  while current_layer <= last_firewall_layer:
    if current_layer in layers.keys():
      layer = layers[current_layer]
      if layer.position_at_tick(current_tick) == 1:
        caught = True
        total_penalty = total_penalty + current_layer * layer.range
    current_tick = current_tick + 1
    current_layer = current_layer + 1
  return caught, total_penalty

delay = 0
while True:
  caught, total_penalty = send_packet(delay)
  if not caught:
    print("Smallest delay without being caught:", delay)
    break
  else:
    delay = delay + 1
