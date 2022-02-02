num_players = 403
last_marble = 71920

circle = [0]
remaining_marbles = [i for i in range(1, last_marble+1)]
scores = [0 for i in range(num_players)]
current_player = 0
current_index = 0

while remaining_marbles != []:
  current_marble = remaining_marbles.pop(0)

  if current_marble % 23 == 0:
    current_index = (current_index-7) % len(circle)
    score = current_marble + circle.pop(current_index)
    scores[current_player] = scores[current_player] + score
  else:
    current_index = ((current_index + 1) % len(circle)) + 1
    circle.insert(current_index, current_marble)

  current_player = (current_player + 1) % num_players

print(max(scores))