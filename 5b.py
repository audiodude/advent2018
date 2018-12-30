import fileinput
import hashlib

for line in fileinput.input():
  orig_input = line.strip()

def collapse(ic):
  last_ic = None
  while last_ic != ic:
    i = 0
    last_ic = ic
    m = hashlib.md5()
    m.update(ic.encode('utf8'))
    print(m.hexdigest())
    while i+1 < len(ic):
      magic = abs(ord(ic[i]) - ord(ic[i+1]))
      if magic == 32:
        ic = ic[:i] + ic[i+2:]
        i -= 1
      i += 1
  return len(ic)

all_chars = set()
for c in orig_input:
  all_chars.add(c.lower())
print(all_chars)

min_length = len(orig_input)
for c in all_chars:
  ic = orig_input.replace(c.lower(), '').replace(c.upper(), '')
  length = collapse(ic)
  if length < min_length:
    min_length = length

print()
print(min_length)
