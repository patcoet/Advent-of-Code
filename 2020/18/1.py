sum_ = 0

with open("input.txt") as file:
  for line in file:
    line = line.strip().replace(" ", "")

    prev_fop = 0

    for i in range(line.count("+") + line.count("*")):
      fop = len(line)
      if (p := line.find("+", prev_fop)) != -1:
        fop = min(fop, p)
      if (t := line.find("*", prev_fop)) != -1:
        fop = min(fop, t)

      if line[fop-1].isdigit():
        line = line[:fop-1] + "(" + line[fop-1:]
      else:
        level = 0
        i = fop - 1
        while i >= 0:
          if line[i] == ")":
            level += 1
          elif line[i] == "(":
            level -= 1
          if level == 0:
            line = line[:i] + "(" + line[i:]
            break
          i -= 1

      fop += 1

      if line[fop+1].isdigit():
        line = line[:fop+2] + ")" + line[fop+2:]
      else:
        level = 0
        i = fop + 1
        while i < len(line):
          if line[i] == "(":
            level += 1
          elif line[i] == ")":
            level -= 1

          if level == 0:
            line = line[:i+1] + ")" + line[i+1:]
            break

          i += 1

      fop += 1

      prev_fop = fop

    sum_ += eval(line)

print(sum_)