valid_ranges = {}
valid_tickets = []

with open("input.txt") as file:
  for line in file:
    if line.find("or") != -1:
      ranges = []
      for entry in line.split(":")[1].strip().split(" or "):
        start = int(entry.split("-")[0])
        end = int(entry.split("-")[1])
        ranges.append(range(start, end+1))
      valid_ranges[line.split(":")[0]] = ranges
    elif len(nums := line.strip().split(",")) > 1:
      valid = True

      for num in map(lambda x: int(x), nums):
        if not any(map(lambda x: num in x[0] or num in x[1], valid_ranges.values())):
          valid = False

      if valid:
        valid_tickets.append(list(map(lambda x: int(x), nums)))

ruled_out = {}
for i in range(len(valid_ranges.keys())):
  ruled_out[i] = []

known_fields = {}

while len(known_fields) < len(valid_ranges.keys()):
  for n in range(len(valid_ranges.keys())):
    if n in known_fields.keys():
      continue

    changed = True

    while changed:
      changed = False
      for ticket in valid_tickets:
        num = ticket[n]

        for curr_key in valid_ranges.keys():
          if curr_key not in ruled_out[n]:
            curr_ranges = valid_ranges[curr_key]
            if (num not in curr_ranges[0]) and (num not in curr_ranges[1]):
              # print(f"Field #{n} can't be {curr_key}")
              ruled_out[n].append(curr_key)
              changed = True

    if len(ruled_out[n]) == len(valid_ranges.keys()) - 1:
      known_fields[n] = filter(lambda x: x not in ruled_out[n], valid_ranges.keys()).__next__()
      # print(f"Field #{n} must be {known_fields[n]}")
      for i in range(1, len(ruled_out)):
        ruled_out[i].append(known_fields[n])

# print(known_fields)

product = 1

for field_number in known_fields.keys():
  if known_fields[field_number].find("departure") != -1:
    product *= valid_tickets[0][field_number]

print(product)