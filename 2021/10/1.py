from collections import deque

stack = deque()
score = 0
symbols = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

with open('input') as file:
    for line in file:
        for char in line.strip():
            if char in symbols:
                stack.append(char)
            elif char != symbols[stack.pop()]:
                score += points[char]
                break

print(score)
