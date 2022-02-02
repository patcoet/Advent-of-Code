decks = []

with open("input.txt") as file:
  player = 0
  for line in file:
    if line == "Player 1:\n":
      player = 0
      decks.append([])
    elif line == "Player 2:\n":
      player = 1
      decks.append([])
    elif line != "\n":
      decks[player].append(int(line.strip()))

def play():
  if decks[0][0] > decks[1][0]:
    decks[0].append(decks[0].pop(0))
    decks[0].append(decks[1].pop(0))
  else:
    decks[1].append(decks[1].pop(0))
    decks[1].append(decks[0].pop(0))

turn = 1
while len(decks[0]) > 0 and len(decks[1]) > 0:
  print(f"-- Round {turn} --")
  print(f"Player 1's deck: {decks[0]}")
  print(f"Player 2's deck: {decks[1]}")
  print()
  turn += 1
  play()

print(f"== Post-game results ==")
print(f"Player 1's deck: {decks[0]}")
print(f"Player 2's deck: {decks[1]}")

total = 0
for i in range(len(max(decks))):
  card = list(reversed(max(decks)))[i]
  total += card * (i+1)
print(f"Score: {total}")