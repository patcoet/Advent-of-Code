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

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_passports = 0

for passport in passports:
  fields = [field.split(":")[0] for field in passport.split(" ")]
  if all(map(lambda x: x in fields, required_fields)):
    valid_passports += 1

print(valid_passports)