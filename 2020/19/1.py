import re

rules = {}
messages = []

with open("input.txt") as file:
  for line in file:
    if ":" in line:
      words = line.strip().split(":")
      rside = words[1].strip()
      if "|" in rside:
        rules[words[0]] = ("or", [("and", y) for y in [x.strip().split() for x in rside.split("|")]])
      elif "a" in rside or "b" in rside:
        rules[words[0]] = ("letter", rside[1:-1])
      else:
        rules[words[0]] = ("and", rside.split())
    elif line.strip() != "":
      messages.append(line)

def recurse(key):
  t, r = rules[key]

  if t == "letter":
    return r
  elif t == "and":
    return "".join([recurse(x) for x in r])
  elif t == "or":
    if len(r[0][1]) == 1:
      return "(" + "|".join(["".join([recurse(x[1][0])]) for x in r]) + ")"
    else:
      return "(" + "|".join(["".join([recurse(x[1][0]), recurse(x[1][1])]) for x in r]) + ")"

regex = recurse("0") + "\n"

print(sum(map(lambda x: (re.match(regex, x) != None) * 1, messages)))