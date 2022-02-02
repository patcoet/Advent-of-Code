foods = []
allergens = {}
ingredient_list = []

with open("input.txt") as file:
  for line in file:
    split = line.strip().split("(")
    ingredients = split[0].strip().split(" ")
    ingredient_list += [x for x in ingredients if x not in ingredient_list]
    allergens_ = split[1][len("contains "):-1].split(", ")
    foods.append((ingredients, allergens_))

for food in foods:
  ingredients, allergens_ = food
  for allergen in allergens_:
    if allergen not in allergens.keys():
      allergens[allergen] = []
    allergens[allergen].append(ingredients)

known_ingredients = {}

for allergen in allergens.keys():
  allergens[allergen] = [x for x in allergens[allergen][0] if all([x in y for y in allergens[allergen]])]
  if len(allergens[allergen]) == 1:
    known_ingredients[allergens[allergen][0]] = allergen

changed = True
while changed:
  changed = False
  for allergen in allergens.keys():
    if len(allergens[allergen]) > 1:
      allergens[allergen] = [x for x in allergens[allergen] if x not in known_ingredients.keys()]

    if len(allergens[allergen]) == 1 and allergens[allergen][0] not in known_ingredients.keys():
      known_ingredients[allergens[allergen][0]] = allergen
      changed = True

print(",".join(sorted(known_ingredients, key=lambda x: known_ingredients[x])))