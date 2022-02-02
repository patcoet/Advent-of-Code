highest_seat_id = 0

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
    highest_seat_id = max(seat_id, highest_seat_id)

print(highest_seat_id)