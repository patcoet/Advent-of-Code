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

def play_game(decks):
  seen_decks = []
  game_winner = -1

  while game_winner == -1:
    if decks in seen_decks:
      return 0

    seen_decks.append([decks[0][:], decks[1][:]])
    drawn_cards = [decks[0].pop(0), decks[1].pop(0)]

    if drawn_cards[0] <= len(decks[0]) and drawn_cards[1] <= len(decks[1]):
      round_winner = play_game([decks[0][:drawn_cards[0]], decks[1][:drawn_cards[1]]])
    else:
      if drawn_cards[0] > drawn_cards[1]:
        round_winner = 0
      else:
        round_winner = 1

    if round_winner == 0:
      decks[0].append(drawn_cards[0])
      decks[0].append(drawn_cards[1])
    else:
      decks[1].append(drawn_cards[1])
      decks[1].append(drawn_cards[0])

    if len(decks[0]) == 0:
      game_winner = 1
    elif len(decks[1]) == 0:
      game_winner = 0

  return game_winner

winning_deck = decks[play_game(decks)]
total = 0
for i in range(len(winning_deck)):
  card = list(reversed(winning_deck))[i]
  total += card * (i+1)

print(f"Score: {total}")