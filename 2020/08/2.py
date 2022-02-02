lines = []

with open("input.txt") as file:
  for line in file:
    op, arg = line.strip().split()
    lines.append([op, int(arg)])

terminated = False
switched_i = 0
switched_op = ""

while not terminated:
  acc = 0
  i = 0
  seen_is = set()
  for j in range(switched_i, len(lines)):
    if lines[j][0] == "jmp":
      switched_i = j
      switched_op = "jmp"
      lines[j][0] = "nop"
      break
    elif lines[j][0] == "nop":
      switched_i = j
      switched_op = "nop"
      lines[j][0] = "jmp"
      break

  while i not in seen_is:
    if i < 0 or i >= len(lines):
      terminated = True
      break

    seen_is.add(i)
    op, arg = lines[i]
    if op == "acc":
      acc += arg
    elif op == "jmp":
      i += arg
      continue

    i += 1

  lines[switched_i][0] = switched_op
  switched_i += 1

print(acc)