# Day 3: Crossed Wires
# Task: Find wire crossing point with lowest signal delay.

# Idea: Write down visited coords like before, but add the step number to each one, like [(0, (0,0)), (1, (1,0)), ...]. Find the overlapping points like before, but get the minimum with respect to steps instead of distance.

wires = [] # This will contain two sets, each being the visited coords of each wire.

with open("input.txt") as file: # Input has two lines that look like "R8,U5,L5,D3".
  for line in file:
    visited_coords = set() # To be filled in and later appended to wires.
    curr_pos = (0, 0) # We need to keep track of the current position to know what to add to visited_coords.
    curr_step = 0
    instructions = line.split(",") # Turn "R8,U5,L5,D3" into ["R8","U5","L5","D3"].

    for instruction in instructions:
      direction = instruction[0] # Will be "U", "D", "L", or "R".
      distance = int(instruction[1:])

      if direction == "U":                                   # If we're at (a, b) and we get the instruction "U5",
        for y in range(distance+1):
          visited_coords.add((curr_step + y, (curr_pos[0], curr_pos[1] + y))) # add (curr_step+1, (a, b+1)) ... (curr_step+5, (a, b+5)) to visited_coords,
        curr_pos = (curr_pos[0], curr_pos[1] + distance)     # and set curr_pos to (a, b+5).

      if direction == "D":
        for y in range(distance+1):
          visited_coords.add((curr_step + y, (curr_pos[0], curr_pos[1] - y)))
        curr_pos = (curr_pos[0], curr_pos[1] - distance)

      if direction == "L":
        for x in range(distance+1):
          visited_coords.add((curr_step + x, (curr_pos[0] - x, curr_pos[1])))
        curr_pos = (curr_pos[0] - x, curr_pos[1])

      if direction == "R":
        for x in range(distance+1):
          visited_coords.add((curr_step + x, (curr_pos[0] + x, curr_pos[1])))
        curr_pos = (curr_pos[0] + x, curr_pos[1])

      curr_step += distance

    wires.append(visited_coords)

overlap_points = {coord for (step, coord) in wires[0]}.intersection({coord for (step, coord) in wires[1]}) # The set of points visited by both wires.
overlap_points.remove((0,0)) # The origin point doesn't count, as per puzzle instructions.

combined_delays = []

for op in overlap_points:
  delay1 = [point for point in wires[0] if point[1] == op][0][0]
  delay2 = [point for point in wires[1] if point[1] == op][0][0]
  combined_delays.append(delay1 + delay2)
# Well, here's something I should go back and redo later! The above is much slower than it seems like it should be. I think maybe possibly that's because I'm mixing sets and lists, but I don't know. Maybe maps and filters would be better. Either way, I need to take a break before I think about this again.

print(f"Fewest combined steps: {min(combined_delays)}")
