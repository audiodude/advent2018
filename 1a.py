import fileinput

result = 0
for line in fileinput.input():
  l = line.strip()
  sign, number = l[0], l[1:]

  if sign == '+':
    result += int(number)
  elif sign == '-':
    result -= int(number)
  else:
    raise ValueError('Line did not begin with + or -')

print(result)

