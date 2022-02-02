starting_nums = []

with open("input.txt") as file:
  starting_nums = list(map(lambda x: int(x), file.readline().strip().split(",")))

# print(starting_nums)

spoken_nums = {} # index is number, value is turn numbers it's been spoken on

for n in range(len(starting_nums)):
  spoken_nums[starting_nums[n]] = [n]
  last_num_spoken = starting_nums[n]

# print(spoken_nums)
# print(last_num_spoken)
for i in range(len(spoken_nums), 2020):
  # print(f"turn number {i}")
  print(f"spoken_nums: {spoken_nums}")
  # print(f"turn, last: {i}, {last_num_spoken}")
  if last_num_spoken not in spoken_nums.keys():
    # print(f"Last num spoken was not spoken before")
    spoken_nums[last_num_spoken] = [i]
    last_num_spoken = 0
  elif len(spoken_nums[last_num_spoken]) == 1:
    # print(f"The last time {last_num_spoken} was spoken was the first")
    if 0 in spoken_nums.keys():
      spoken_nums[0].append(i)
    else:
      spoken_nums[0] = [i]
    last_num_spoken = 0
  else:
    # print(f"Last two times {last_num_spoken} was spoken: {spoken_nums[last_num_spoken][-1]} and {spoken_nums[last_num_spoken][-2]}")
    last_num_spoken = spoken_nums[last_num_spoken][-1] - spoken_nums[last_num_spoken][-2]
    if last_num_spoken in spoken_nums.keys():
      spoken_nums[last_num_spoken].append(i)
    else:
      spoken_nums[last_num_spoken] = [i]

# print(spoken_nums)
print(last_num_spoken)