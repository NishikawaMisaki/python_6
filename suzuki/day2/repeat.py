import sys
args = sys.argv
number = int(args[1])
sum = 0
while 100 > sum:
  sum += number
if sum == 100:
  print("Just 100!", end="")
else:
  print("Over!", end="")

