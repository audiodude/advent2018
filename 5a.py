import fileinput
import hashlib

for line in fileinput.input():
  ic = line.strip()

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
print()
print(len(ic))
