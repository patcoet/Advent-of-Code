bus_ids = []
earliest_departure = -1

with open("input.txt") as file:
  earliest_departure = int(file.readline().strip())
  for bus_id in file.readline().strip().split(","):
    if bus_id != "x":
      bus_ids.append(int(bus_id))

first_makeable_departures = []
for bus_id in bus_ids:
  time = 0

  while time < earliest_departure:
    time += bus_id

  first_makeable_departures.append([bus_id, time])

earliest_bus = min(first_makeable_departures, key=lambda x: x[1])

print(earliest_bus[0] * (earliest_bus[1] - earliest_departure))