sum_ = 0

with open("input.txt") as file:
  for line in file:
    line = line.strip().replace(" ", "")

    for op in ("+", "*"):
      last_i = 0

      for n in range(line.count(op)):
        i = line.find(op, last_i+1)
        if line[i-1].isdigit():
          line = line[:i-1] + "(" + line[i-1:]
        else:
          level = 0
          j = i - 1
          while True:
            if line[j] == ")":
              level += 1
            elif line[j] == "(":
              level -= 1
            if level == 0:
              line = line[:j] + "(" + line[j:]
              break
            j -= 1

        i += 1

        if line[i+1].isdigit():
          line = line[:i+2] + ")" + line[i+2:]
        else:
          level = 0
          j = i + 1
          while True:
            if line[j] == "(":
              level += 1
            elif line[j] == ")":
              level -= 1
            if level == 0:
              line = line[:j+1] + ")" + line[j+1:]
              break
            j += 1

        last_i = i

    sum_ += eval(line)

print(sum_)