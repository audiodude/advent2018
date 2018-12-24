import fileinput
import re

INPUT_RE = re.compile(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)')

data = []
for line in fileinput.input():
  md = INPUT_RE.match(line.strip())
  if not md:
    raise ValueError('Line (%s) did not match regex' % line)
  data.append(
    (int(md.group(1)), int(md.group(2)), int(md.group(3)), int(md.group(4))))

m = [[[0] for _ in range(1000)] for x in range(1000)]
disqualified = set()

for i, d in enumerate(data):
  i += 1
  left, top, width, height = d
  for x in range(left, left+width):
    for y in range(top, top+height):        
      m[x][y][0] += 1
      m[x][y].append(i)
      if m[x][y][0] > 1:
        for elf in m[x][y][1:]:
          disqualified.add(elf)

print(disqualified)

for i in range(1, len(data)):
  if i not in disqualified:
    print(i)
    break
