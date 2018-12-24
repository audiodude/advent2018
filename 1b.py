import fileinput
import sys

frequencies = []
for line in fileinput.input():
  l = line.strip()
  frequencies.append((l[0], int(l[1:])))

result = 0
seen_results = set()
while True:
  for sign, number in frequencies:
    if sign == '+':
      result += number
    elif sign == '-':
      result -= number
    else:
      raise ValueError('Line did not begin with + or -')

    if result in seen_results:
      print(result)
      sys.exit(0)
    seen_results.add(result)
