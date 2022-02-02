initial_cup_numbers = "219748365" # input
# initial_cup_numbers = "389125467" # example

initial_cup_numbers = [int(char) for char in initial_cup_numbers]

class Node:
  def __init__(self, label, next_):
    self.label = label
    self.next = next_

  def __str__(self):
    return f"{self.label} -> {self.next.label}"

num_cups = int(1e6)
# num_cups = 9

curr_cup = Node(initial_cup_numbers[0], None)
cups_by_label = {initial_cup_numbers[0]: curr_cup}
last_added = curr_cup
i = 1
for num in initial_cup_numbers[1:]:
  new_cup = Node(num, None)
  last_added.next = new_cup
  last_added = new_cup
  cups_by_label[num] = new_cup

for num in range(10, num_cups+1):
  new_cup = Node(num, None)
  last_added.next = new_cup
  last_added = new_cup
  cups_by_label[num] = new_cup

last_added.next = curr_cup

print(curr_cup)

for n in range(int(1e7)):
  if n % 100000 == 0:
    print(n, curr_cup)

  snip_start = curr_cup.next
  snipped_labels = [snip_start.label, snip_start.next.label, snip_start.next.next.label]
  # print(f"-- move {n+1} --")
  # print(f"current cup: {curr_cup}")
  # print(f"pick up: {snipped_labels}")
  curr_cup.next = curr_cup.next.next.next.next

  destination_label = ((curr_cup.label - 2) % num_cups) + 1
  while destination_label in snipped_labels:
    destination_label = ((destination_label - 2) % num_cups) + 1

  destination_cup = cups_by_label[destination_label]
  # print(f"destination label: {destination_label}")
  # print(f"destination: {destination_cup}")

  post_destination_cup = destination_cup.next
  destination_cup.next = snip_start
  destination_cup.next.next.next.next = post_destination_cup

  curr_cup = curr_cup.next
  # print()

while curr_cup.label != 1:
  curr_cup = curr_cup.next
l1 = curr_cup.next.label
l2 = curr_cup.next.next.label
print(f"{l1} * {l2} = {l1*l2}")