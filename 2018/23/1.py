import re

class Nanobot:
  def __init__(self, pos, r):
    self.pos = pos
    self.r = r

bots = []
longest_range = 0

with open('input.txt') as file:
  for line in file:
    p = re.compile('pos=<(-*\d*),(-*\d*),(-*\d*)>, r=(\d*)')
    nums = p.search(line)
    r = int(nums[4])
    longest_range = max(longest_range, r)
    bots.append(Nanobot((int(nums[1]), int(nums[2]), int(nums[3])), r))

strongest_bot = [bot for bot in bots if bot.r == longest_range][0]
bots_in_range = [bot for bot in bots if abs(bot.pos[0] - strongest_bot.pos[0]) + abs(bot.pos[1] - strongest_bot.pos[1]) + abs(bot.pos[2] - strongest_bot.pos[2]) <= strongest_bot.r]
print(len(bots_in_range))
