lines = []

with open('input') as file:
  for line in file:
    lines.append(line.strip())

ogr_lines = lines
csr_lines = lines
for n, digit in enumerate(lines[0]):
  if len(ogr_lines) > 1:
    mc = int(len([line for line in ogr_lines if line[n] == '1']) >= len(ogr_lines) / 2)
    ogr_lines = [line for line in ogr_lines if int(line[n]) == mc]

  if len(csr_lines) > 1:
    lc = int(not len([line for line in csr_lines if line[n] == '1']) >= len(csr_lines) / 2)
    csr_lines = [line for line in csr_lines if int(line[n]) == lc]

print(int(ogr_lines[0], 2) * int(csr_lines[0], 2))
