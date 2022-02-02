mem = {}

with open("input.txt") as file:
  mask = ""
  for line in file:
    words = line.split()
    if words[0] == "mask":
      mask = words[2]
    else:
      i = str(bin(int(words[0].split("[")[1][:-1])))[2:].rjust(36, "0")
      value = int(words[2])

      for j in range(len(i)):
        if mask[j] != "0":
          i = i[:j] + mask[j] + i[j+1:]

      xs = i.count("X")

      for n in range(2 ** xs):
        nums = str(bin(n))[2:].rjust(xs, "0")
        k = 0
        str_ = i

        while k < xs:
          str_ = str_.replace("X", nums[k], 1)
          k += 1

        mem[int(str_, 2)] = value

print(sum(mem.values()))
