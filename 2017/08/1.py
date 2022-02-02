inputt = 'input.txt'

instructions = []
registers = {}
with open(inputt) as file:
  for line in file:
    line = line.strip('\n')
    words = line.split(' ')
    words[2] = int(words[2])
    words[6] = int(words[6])
    instructions.append(words)
    registers[words[0]] = 0

print("Registers before modifying", registers)

for instruction in instructions:
  register_to_modify = instruction[0]
  increment_or_decrement = instruction[1]
  modify_by_value = instruction[2]
  first_operand = instruction[4]
  equality_operation = instruction[5]
  second_operand = instruction[6]

  if increment_or_decrement == 'dec':
    modify_by_value = -modify_by_value

  result_is_true = False
  if equality_operation == '<':
    result_is_true = registers[first_operand] < second_operand
  elif equality_operation == '<=':
    result_is_true = registers[first_operand] <= second_operand
  elif equality_operation == '>':
    result_is_true = registers[first_operand] > second_operand
  elif equality_operation == '>=':
    result_is_true = registers[first_operand] >= second_operand
  elif equality_operation == '==':
    result_is_true = registers[first_operand] == second_operand
  elif equality_operation == '!=':
    result_is_true = registers[first_operand] != second_operand
  if result_is_true:
    registers[register_to_modify] = registers[register_to_modify] + modify_by_value

print("Registers after modifying:", registers)

values = []
for register in registers:
  values.append(registers[register])

print("Highest value:", max(values))