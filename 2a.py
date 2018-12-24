from collections import defaultdict
import fileinput

def has_n(data, n):
  counts = defaultdict(int)
  for l in data:
    counts[l] += 1
  for l, count in counts.items():
    if count == n:
      return True
  return False

twos = 0
threes = 0
for line in fileinput.input():
  l = line.strip()
  if has_n(l, 2):
    twos += 1
  if has_n(l, 3):
    threes += 1

print(twos*threes)
