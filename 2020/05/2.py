seat_ids = []

with open("input.txt") as file:
  for line in file:
    rows = range(0, 128)
    cols = range(0, 8)

    for letter in line:
      if letter == "F":
        rows = rows[:len(rows)//2] # range(0, 128) -> range(0, 64)
      elif letter == "B":
        rows = rows[len(rows)//2:] # range(0, 128) -> range(64, 128)
      elif letter == "L":
        cols = cols[:len(cols)//2]
      elif letter == "R":
        cols = cols[len(cols)//2:]

    seat_id = rows[0]*8 + cols[0]
    seat_ids.append(seat_id)

seat_ids.sort()
i = min(seat_ids)

while True:
  if seat_ids[i - min(seat_ids)] != i:
    print(i)
    break

  i += 1