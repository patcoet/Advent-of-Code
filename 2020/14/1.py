mem = {}

with open("input.txt") as file:
  mask = ""
  for line in file:
    words = line.split()
    if words[0] == "mask":
      mask = words[2]
    else:
      i = int(words[0].split("[")[1][:-1])
      value = str(bin(int(words[2])))[2:].rjust(36, "0")
      # print(f"index {i}")
      # print(f"value before mask: {value}")
      # print(f"mask:              {mask}")
      for j in range(len(value)):
        if mask[j] != "X":
          value = value[:j] + mask[j] + value[j+1:]
      mem[i] = value
      # print(f"value after mask:  {value}")


# print(mem)

sum_ = 0

for value in mem.values():
  total = 0

  for i in range(len(value)):
    if value[len(value) - (i+1)] == "1":
      total += 2 ** i

  sum_ += total

print(sum_)