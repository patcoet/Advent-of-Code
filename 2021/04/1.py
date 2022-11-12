import re

nums = []
boards = []

with open('input') as file:
  nums_line = file.readline()
  nums = [int(n) for n in re.findall('(\d+),?', nums_line)]
  file.readline()
  board = []

  for line in file:
    if line == '\n':
      boards.append(board)
      board = []
    else:
      for n in re.findall('\d+\s?', line.strip()):
        board.append(int(n))

def mark_boards(num):
  for board in boards:
    for i, n in enumerate(board):
      if n == num:
        board[i] = -n

def has_bingo(board):
  row_is = [range(x, x+5) for x in range(0, 25, 5)]
  col_is = [range(x, 25, 5) for x in range(0, 5)]

  row_bingo = any([all([board[i] < 0 for i in ri]) for ri in row_is])
  col_bingo = any([all([board[i] < 0 for i in ci]) for ci in col_is])

  return row_bingo or col_bingo

for num in nums:
  mark_boards(num)
  for n, board in enumerate(boards):
    if has_bingo(board):
      print(sum([n for n in board if n > 0]) * num)
      break
  else:
    continue
  break
