foods = []
allergens = {}

with open("input.txt") as file:
  for line in file:
    split = line.strip().split("(")
    ingredients = split[0].strip().split(" ")
    allergens_ = split[1][len("contains "):-1].split(", ")
    foods.append((ingredients, allergens_))

# print(foods)
for food in foods:
  ingredients, allergens_ = food
  # print(allergens_)
  for allergen in allergens_:
    # print(1, allergen)
    if allergen not in allergens.keys():
      # allergens[allergen] = set()
      allergens[allergen] = []
    allergens[allergen].append(ingredients)
    # allergens[allergen].add(ingredients)
    # for ingredient in ingredients:
    #   allergens[allergen].add(ingredient)

# print(allergens)
possibly_allergenic_ingredients = []

for allergen in allergens.keys():
  # print(allergens[allergen])
  possible_ingredients = [x for x in allergens[allergen][0] if all([x in y for y in allergens[allergen]])]
  possibly_allergenic_ingredients += possible_ingredients
  # print(f"Ingredients that can contain {allergen}: {possible_ingredients}")
  # print()

# print(possibly_allergenic_ingredients)

safe_ingredients = []

for food in foods:
  ingredients, _ = food
  safe_ingredients += [ingredient for ingredient in ingredients if ingredient not in possibly_allergenic_ingredients]

print(len(safe_ingredients))