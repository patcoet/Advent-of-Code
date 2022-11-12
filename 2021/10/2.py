from collections import deque

symbols = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 1, ']': 2, '}': 3, '>': 4}

scores = []
with open('input') as file:
    for line in file:
        stack = deque()
        for char in line.strip():
            if char in symbols:
                stack.append(char)
            elif char != symbols[stack.pop()]:
                break
        else:
            score = 0
            while stack:
                score *= 5
                score += points[symbols[stack.pop()]]

            scores.append(score)

scores.sort()
print(scores[int(len(scores) / 2)])
