# Day 3: Crossed Wires
# Task: Find nearest wire crossing point to origin.

# Idea: For each of the wires, compute the set of coordinates that they are on. Get the intersection of those two sets, and then get the closest of those.

wires = [] # This will contain two sets, each being the visited coords of each wire.

with open("input.txt") as file: # Input has two lines that look like "R8,U5,L5,D3".
  for line in file:
    visited_coords = set() # To be filled in and later appended to wires.
    curr_pos = (0, 0) # We need to keep track of the current position to know what to add to visited_coords.
    instructions = line.split(",") # Turn "R8,U5,L5,D3" into ["R8","U5","L5","D3"].

    for instruction in instructions:
      direction = instruction[0] # Will be "U", "D", "L", or "R".
      distance = int(instruction[1:])

      if direction == "U":                                   # If we're at (a, b) and we get the instruction "U5",
        for y in range(distance+1):
          visited_coords.add((curr_pos[0], curr_pos[1] + y)) # add (a, b+1) ... (a, b+5) to visited_coords,
        curr_pos = (curr_pos[0], curr_pos[1] + distance)     # and set curr_pos to (a, b+5).

      if direction == "D":
        for y in range(distance+1):
          visited_coords.add((curr_pos[0], curr_pos[1] - y))
        curr_pos = (curr_pos[0], curr_pos[1] - distance)

      if direction == "L":
        for x in range(distance+1):
          visited_coords.add((curr_pos[0] - x, curr_pos[1]))
        curr_pos = (curr_pos[0] - x, curr_pos[1])

      if direction == "R":
        for x in range(distance+1):
          visited_coords.add((curr_pos[0] + x, curr_pos[1]))
        curr_pos = (curr_pos[0] + x, curr_pos[1])

    wires.append(visited_coords)

overlap_points = wires[0].intersection(wires[1]) # The set of points visited by both wires.
overlap_points.remove((0,0)) # The origin point doesn't count, as per puzzle instructions.

closest_overlap = min(overlap_points, key=lambda x: abs(x[0]) + abs(x[1])) # If all coordinates were guaranteed to be positive we could've just used key=sum here, but they're not.
closest_distance = abs(closest_overlap[0]) + abs(closest_overlap[1])

print(f"Manhattan distance to the closest intersection: {closest_distance}")