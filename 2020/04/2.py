passports = []

with open("input.txt") as file:
  curr_passport = ""

  for line in file:
    if line != "\n":
      curr_passport += " " + line.strip()
    else:
      passports.append(curr_passport.strip())
      curr_passport = ""

  passports.append(curr_passport.strip())

def valid(field, value):
  if field == "byr":
    return len(value) == 4 and value.isnumeric() and 1920 <= int(value) <= 2002
  if field == "iyr":
    return len(value) == 4 and value.isnumeric() and 2010 <= int(value) <= 2020
  if field == "eyr":
    return len(value) == 4 and value.isnumeric() and 2020 <= int(value) <= 2030
  if field == "hgt":
    unit = value[-2:]
    hgt = value[:-2]
    if unit == "cm":
      return hgt.isnumeric() and 150 <= int(hgt) <= 193
    else:
      return hgt.isnumeric() and 59 <= int(hgt) <= 76
  if field == "hcl":
    return value[0] == "#" and all(map(lambda x: x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"], value[1:]))
  if field == "ecl":
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  if field == "pid":
    return len(value) == 9 and value.isnumeric()

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_passports = 0

for passport in passports:
  fields = sorted([field.split(":")[0] for field in passport.split(" ")])
  if not all(map(lambda x: x in fields, required_fields)):
    continue

  valid_fields = 0

  for item in passport.split(" "):
    field = item.split(":")[0]
    value = item.split(":")[1]

    if valid(field, value):
      valid_fields += 1

  if valid_fields == 7:
    valid_passports += 1

print(valid_passports)