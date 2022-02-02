import re

regex = ""

with open('input.txt') as file:
  regex = file.readline().strip()[1:-1]

dead_ends = re.compile('\(\w+\|\)')                     # Matches all (abc|) groups
words = re.compile('[NSWE]+')                           # Matches all letter groups
last_split = re.compile('(\d+)\|(\d+)(?!.*(\d+\|\d+))') # Matches the last (x|y) group
a_plus_b = re.compile('(\d+)\((\d+)\)')                 # Matches all x(y) groups

subbed = dead_ends.sub('', regex)                         # Remove dead end parts
subbed = words.sub(lambda x: str(len(x.group())), subbed) # Replace all letter groups with their lengths
last = ""
while subbed != last:
  last = subbed
  subbed = last_split.sub(lambda x: str(max(int(x.group(1)), int(x.group(2)))), subbed) # Replace "(x|y)" with the largest of x and y
  subbed = a_plus_b.sub(lambda x: str(int(x.group(1)) + int(x.group(2))), subbed)       # Replace x(y) with x+y
print(subbed)
