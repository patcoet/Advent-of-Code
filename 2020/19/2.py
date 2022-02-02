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
        # rules[words[0]] = "|".join(["(" + ",".join(y) + ")" for y in [x.strip().split() for x in rside.split("|")]])
      elif "a" in rside or "b" in rside:
        rules[words[0]] = ("letter", rside[1:-1])
        # rules[words[0]] = rside[1:-1]
      else:
        rules[words[0]] = ("and", rside.split())
        # rules[words[0]] = "(" + ",".join(rside.split()) + ")"
    elif line.strip() != "":
      messages.append(line)

rules["8"] = ("or", [("and", ["42"]), ("and", ["42", "8"])])
rules["11"] = ("or", [("and", ["42", "31"]), ("and", ["42", "11", "31"])])
# rules["8"] = "(42)|(42,8)"
# rules["8"] = "(42+)"
# rules["11"] = "(42,31)|(42,11,31)"
# rules["11"] = "(42+,31+)"

def recurse(key):
  t, r = rules[key]

  if t == "letter":
    return r
  elif t == "and":
    return "".join([recurse(x) for x in r])
  elif t == "or":
    if len(r[0][1]) == 1:
      return "(?:" + "|".join(["".join([recurse(x[1][0])]) for x in r]) + ")"
    else:
      return "(?:" + "|".join(["".join([recurse(x[1][0]), recurse(x[1][1])]) for x in r]) + ")"

re42 = re.compile("" + recurse("42") + "")
re31 = re.compile("" + recurse("31") + "")
passes = []
for message in messages:
  num_42s = 0
  num_31s = 0
  offset = 0

  while match := re42.match(message, offset):
    num_42s += 1
    offset = match.end()

  while match := re31.match(message, offset):
    num_31s += 1
    offset = match.end()

  if not message[offset:].strip() and num_31s > 0 and num_42s > num_31s:
    passes.append(message.strip())

# for p in passes:
#   print(p)

print(len(passes))