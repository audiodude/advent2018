import fileinput

data = []
for line in fileinput.input():
  data.append(line.strip())

for i, d in enumerate(data):
  for j, e in enumerate(data[i+1:]):
    mismatch = False
    for left, right in zip(d, e):
      if left != right:
        if mismatch:
          break
        else:
          mismatch = True
    else:
      print(d, e)
