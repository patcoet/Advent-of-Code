req_sum = 0

with open("input.txt") as file:
  for line in file:
    mass = int(line)
    req = (mass // 3) - 2
    req_sum += req

    while req > 0:
      req = (req // 3) - 2
      if req > 0:
        req_sum += req

print(f"Sum of fuel requirements: {req_sum}")