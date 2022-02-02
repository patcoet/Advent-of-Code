cups = "219748365" # input
# cups = "389125467" # example

cups = [int(char) for char in cups]

i = 0

for n in range(0, 100):
  print(f"-- move {n+1} --")
  print(f"cups: {i} {cups}")
  curr_label = cups[i]
  to_pick_up = range(i+1, i+4)
  picked_up = []
  for n in to_pick_up:
    picked_up.append(cups[n % len(cups)])
  for n in picked_up:
    cups.pop(cups.index(n))
  print(f"pick up: {picked_up}")
  i = cups.index(curr_label)

  for j in [(x % 9) + 1 for x in range(cups[i]-2, cups[i]-9, -1)]:
    if j in cups:
      destination = j
      break

  print(f"Destination: {destination}")

  d = cups.index(destination)

  cups = cups[:d+1] + picked_up + cups[d+1:]
  i = (cups.index(curr_label) + 1) % len(cups)
  print()


print(f"-- final --")
print(f"cups: {cups}")

i = cups.index(1)
cs = cups[i+1:] + cups[:i]
print(f"cups after 1: {''.join(map(lambda x: str(x), cs))}")