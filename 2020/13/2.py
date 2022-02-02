bus_ids = []
earliest_departure = -1

with open("input.txt") as file:
  earliest_departure = int(file.readline().strip())
  tmp = file.readline().strip().split(",")
  for i in range(len(tmp)):
    if tmp[i] != "x":
      bus_ids.append([i, int(tmp[i])])

biggest_id = max(bus_ids, key=lambda x: x[1])
i = 0
k = 0
while True:
  if i % 1000000 == 0:
    print(k)
  if all([((k + (bus_id[0] - biggest_id[0])) / bus_id[1]).is_integer() for bus_id in bus_ids]):
    print(k - biggest_id[0])
    break
  i += 1
  k += biggest_id[1]