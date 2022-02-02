inputt = 'input.txt'
claims = {}
with open(inputt) as file:
  for line in file:
    words = line.split(' ')
    claim_id = int(words[0].strip('#'))
    distance_x = int(words[2].split(',')[0])
    distance_y = int(words[2].split(',')[1].strip(':'))
    width = int(words[3].split('x')[0])
    height = int(words[3].split('x')[1])
    claims[claim_id] = {'distance_x': distance_x, 'distance_y': distance_y, 'width': width, 'height': height}

def squares_covered_by(claim_id):
  result = []
  claim = claims[claim_id]
  distance_x = claim['distance_x']
  distance_y = claim['distance_y']
  width = claim['width']
  height = claim['height']

  result = [(x, y) for x in range(distance_x, distance_x+width) for y in range(distance_y, distance_y+height)]
  return result

squares_covered = {}
for claim in claims:
  for square in squares_covered_by(claim):
    if square in squares_covered:
      squares_covered[square] = squares_covered[square] + 1
    else:
      squares_covered[square] = 1

print("Number of overlapped squares:", len(list(filter(lambda x: squares_covered.get(x) > 1, squares_covered))))