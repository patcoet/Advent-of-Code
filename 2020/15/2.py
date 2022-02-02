starting_nums = []

with open("input.txt") as file:
  starting_nums = list(map(lambda x: int(x), file.readline().strip().split(",")))

spoken_nums = {} # key is number, value is turn numbers it's been spoken on

for n in range(len(starting_nums)):
  spoken_nums[starting_nums[n]] = [n]
  last_num_spoken = starting_nums[n]

for i in range(len(spoken_nums), 30000000):
  if i % 100000 == 0:
    print(f"turn number {i}")
  if last_num_spoken not in spoken_nums.keys():
    spoken_nums[last_num_spoken] = [i]
    last_num_spoken = 0
  elif len(spoken_nums[last_num_spoken]) == 1:
    if 0 in spoken_nums.keys():
      spoken_nums[0].append(i)
      spoken_nums[0] = spoken_nums[0][-2:]
    else:
      spoken_nums[0] = [i]
    last_num_spoken = 0
  else:
    last_num_spoken = spoken_nums[last_num_spoken][-1] - spoken_nums[last_num_spoken][-2]
    if last_num_spoken in spoken_nums.keys():
      spoken_nums[last_num_spoken].append(i)
      spoken_nums[last_num_spoken] = spoken_nums[last_num_spoken][-2:]
    else:
      spoken_nums[last_num_spoken] = [i]

print(last_num_spoken)
