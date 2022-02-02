lines = []

with open("input.txt") as file:
  for line in file:
    op, arg = line.strip().split()
    lines.append([op, int(arg)])

i = 0
acc = 0

seen_is = set()

while i not in seen_is:
  seen_is.add(i)
  op, arg = lines[i]
  if op == "acc":
    acc += arg
  elif op == "jmp":
    i += arg
    continue

  i += 1

print(acc)