inputt = 'input.txt'

class Program:
  def __init__(self, program_id, connected_programs):
    self.program_id = program_id
    self.connected_programs = connected_programs

programs = []
with open(inputt) as file:
  for line in file:
    words = line.strip().split('<->')
    program_id = int(words[0])
    connected_programs = list(map(int, words[1].strip().split(',')))
    programs.append(Program(program_id, connected_programs))

for program in programs:
  for i in range(len(program.connected_programs)):
    program.connected_programs[i] = programs[program.connected_programs[i]]


def thing(node, connection_list):
  connection_list.add(node)
  for program in node.connected_programs:
    if program not in connection_list:
      connection_list = thing(program, connection_list)
  return connection_list

print("Number of programs in same group as 0:", len(thing(programs[0], set())))

