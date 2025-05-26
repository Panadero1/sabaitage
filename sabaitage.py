import sys
import fileinput

n = len(sys.argv)

inlines = {}

if n > 2:
  print("usage: sabaitage.py [file]")
  exit(1)
elif n == 2:
  inlines = fileinput.input(sys.argv[1])
else:
  inlines = fileinput.input()

for line in inlines:
  print(line.rstrip()[::-1])



exit(0)
