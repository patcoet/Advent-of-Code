# groups = []

class Group:
  def __init__(self, num, team, size, hp, weaknesses, immunities, damage, damage_type, initiative, targeted_this_round=False, selected_target=None):
    self.num = num
    self.team = team
    self.size = size
    self.hp = hp
    self.weaknesses = weaknesses
    self.immunities = immunities
    self.damage = damage
    self.damage_type = damage_type
    self.initiative = initiative
    self.targeted_this_round = targeted_this_round
    self.selected_target = selected_target

  def effective_power(self):
    return self.damage * self.size

  def damage_potential(self, target_group):
    potential = self.effective_power()
    if self.damage_type in target_group.weaknesses:
      potential = potential * 2
    if self.damage_type in target_group.immunities:
      potential = 0
    return potential

  def attack(self, target_group):
    total_damage = self.damage_potential(target_group)
    killed_units = total_damage // target_group.hp
    target_group.size = target_group.size - killed_units

  # def boost(self, amount):
  #   if self.team == 'immune':
  #     self.damage = self.damage + amount
  #   return self

def read(filename):
  groups = []
  with open(filename) as file:
    lines = file.read()
    lines_immune = lines[:lines.find("Infection")].strip().split('\n')[1:]
    lines_infect = lines[lines.find("Infection"):].strip().split('\n')[1:]

    def thing(lines, team):
      i = 1
      for line in lines:
        units = int(line[:line.find("units")])
        hp = int(line[line.find("each with"):line.find("hit points")].split(' ')[2])
        weaknesses = []
        if "weak to" in line:
          weaknesses = line[line.find("weak to")+len("weak to")+1:line.find(")")].split(';')[0].replace(' ', '').split(',')
        immunities = []
        if "immune to" in line:
          immunities = line[line.find("immune to")+len("immune to")+1:line.find(")")].split(';')[0].replace(' ', '').split(',')
        damage = int(line[line.find("does"):line.find("damage")].split(' ')[1])
        damage_type = line[line.find("does"):line.find("damage")].split(' ')[2]
        initiative = int(line[line.find("initiative"):].split(' ')[1])
        groups.append(Group(i, team, units, hp, weaknesses, immunities, damage, damage_type, initiative))
        i = i + 1

    thing(lines_immune, 'immune')
    thing(lines_infect, 'infect')
  return groups

def fight(groups):
  i = 0
  immune = [g.team == 'immune' for g in groups]
  while any(immune) and not all(immune):
    # print(groups[0].team, groups[0].num, groups[0].hp, groups[0].size, groups[0].effective_power(), groups[0].damage_potential(groups[1]))
    # print(groups[1].team, groups[1].num, groups[1].hp, groups[1].size, groups[1].effective_power(), groups[0].damage_potential(groups[0]))
    groups.sort(key=lambda x: x.initiative, reverse=True)
    groups.sort(key=lambda x: x.effective_power(), reverse=True)
    for attacker in groups:
      targets = [group for group in groups if group.team != attacker.team]
      targets.sort(key=lambda x: x.initiative, reverse=True)
      targets.sort(key=lambda x: x.effective_power(), reverse=True)
      targets.sort(key=lambda x: attacker.damage_potential(x), reverse=True)
      for target in targets:
        if attacker.damage_potential(target) > 0 and not target.targeted_this_round:
          attacker.selected_target = target
          target.targeted_this_round = True
          break

    groups.sort(key=lambda x: x.initiative, reverse=True)
    for attacker in groups:
      if attacker.size > 0 and attacker.selected_target:
        attacker.attack(attacker.selected_target)

    for group in groups:
      group.targeted_this_round = False
      group.selected_target = None

    groups = [group for group in groups if group.size > 0]
    immune = [g.team == 'immune' for g in groups]
  return groups

boost = 31 # 30 = infinite loop because not enough damage potential
while True:
  groups = read('input.txt')
  for group in groups:
    if group.team == 'immune':
      group.damage = group.damage + boost
  groups = fight(groups)
  if groups[0].team == 'immune':
    print(sum([group.size for group in groups]))
    break
  boost = boost + 1
