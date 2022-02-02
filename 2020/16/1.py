valids = []
sum_ = 0

with open("input.txt") as file:
  for line in file:
    if line.find("or") != -1:
      for entry in line.split(":")[1].strip().split(" or "):
        start = int(entry.split("-")[0])
        end = int(entry.split("-")[1])
        valids.append(range(start, end+1))
    elif len(nums := line.split(",")) > 1:
      for num in map(lambda x: int(x), nums):
        if all(map(lambda x: num not in x, valids)):
          sum_ += num

print(sum_)