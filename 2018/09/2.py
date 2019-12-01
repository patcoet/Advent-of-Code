import datetime

num_players = 403
last_marble = 71920 * 100

circle = [0]
scores = [0 for i in range(num_players)]
current_player = 0
current_index = 0
current_marble = 1

for current_marble in range(1, last_marble+1):
  if current_marble % (last_marble//100) == 0:
    print(datetime.datetime.now())
    print("Current marble:", current_marble, "(" + str(int(current_marble / last_marble * 100)) + "%)")
    print("Current highest score:", max(scores))
    print()

  if current_marble % 23 == 0:
    current_index = (current_index-7) % len(circle)
    score = current_marble + circle.pop(current_index)
    scores[current_player] = scores[current_player] + score
  else:
    current_index = ((current_index + 1) % len(circle)) + 1
    circle.insert(current_index, current_marble)

  current_player = (current_player + 1) % num_players

print(max(scores))
