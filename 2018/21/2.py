from collections import Counter

def thing(r, instr):
  seen_r5s = Counter()
  prev_r5 = r[5]
  i = 0
  while True:
    r[instr] = i

    if i == 0:
      r[5] = 123
    elif i == 1:
      r[5] = r[5] & 456
    elif i == 2:
      r[5] = 1 if r[5] == 72 else 0
    elif i == 3:
      r[1] = r[5] + r[1]
    elif i == 4:
      r[1] = 0
    elif i == 5:
      r[5] = 0
    elif i == 6:
      r[4] = r[5] | 65536
    elif i == 7:
      r[5] = 13159625
    elif i == 8:
      r[3] = r[4] & 255
    elif i == 9:
      r[5] = r[5] + r[3]
    elif i == 10:
      r[5] = r[5] & 16777215
    elif i == 11:
      r[5] = r[5] * 65899
    elif i == 12:
      r[5] = r[5] & 16777215
    elif i == 13:
      r[3] = 1 if 256 > r[4] else 0
    elif i == 14:
      r[1] = r[3] + r[1]
    elif i == 15:
      r[1] = r[1] + 1
    elif i == 16:
      r[1] = 27
    elif i == 17:
      r[3] = 0
    elif i == 18:
      r[2] = r[3] + 1
    elif i == 19:
      r[2] = r[2] * 256
    elif i == 20:
      r[2] = 1 if r[2] > r[4] else 0
    elif i == 21:
      r[1] = r[2] + r[1]
    elif i == 22:
      r[1] = r[1] + 1
    elif i == 23:
      r[1] = 25
    elif i == 24:
      r[3] = r[3] + 1
    elif i == 25:
      r[1] = 17
    elif i == 26:
      r[4] = r[3]
    elif i == 27:
      r[1] = 7
    elif i == 28:
      r[3] = 1 if r[5] == r[0] else 0
      seen_r5s[r[5]] += 1
      if seen_r5s[r[5]] > 1:
        return prev_r5
      prev_r5 = r[5]
    elif i == 29:
      r[1] = r[3] + r[1]
    elif i == 30:
      r[1] = 5
    else:
      break

    i = r[instr] + 1
  return r

print(thing([0, 0, 0, 0, 0, 0], 1))