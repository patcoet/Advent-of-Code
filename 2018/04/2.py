inputt = 'input.txt'

lines = []
guard_ids = []

with open(inputt) as file:
  for line in file:
    lines.append(line.strip())
    if "Guard" in line:
      guard_id = int(line.split(' ')[3].strip('#'))
      if guard_id not in guard_ids:
        guard_ids.append(guard_id)

sorted_lines = sorted(lines)

sleep_log = {}
for i in range(60):
  sleep_log[i] = []

last_guard_id = 0
last_sleep_start = 0
last_sleep_end = 0
for line in sorted_lines:
  words = line.split(' ')
  if "Guard" in words:
    last_guard_id = int(words[3].strip('#'))
  else:
    minute = int(words[1].split(':')[1].strip(']'))
    if "falls" in words:
      last_sleep_start = minute
    if "wakes" in words:
      last_sleep_end = minute
      for i in range(last_sleep_start, last_sleep_end):
        sleep_log[i].append(last_guard_id)

sleeps = list(map(lambda guard_id: list(map(lambda minute: sleep_log[minute].count(guard_id), sleep_log)), guard_ids))
max_sleeps = max(map(max, sleeps))
for i in range(len(sleeps)):
  for j in range(len(sleeps[i])):
    if sleeps[i][j] == max_sleeps:
      print("Guard ID: #" + str(guard_ids[i]))
      print("Minute: ", j)
      print("id * minute =", guard_ids[i]*j)