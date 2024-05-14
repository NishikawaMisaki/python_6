import sys
args = sys.argv

a = int(args[1])
b = int(args[2])
c = int(args[3])

sum = a + b + c

if (sum >= 220 or (a >= 70 and b >= 70 and c >= 70)) and (a >= 50 and b >= 50 and c >= 50):
    print("合格", end="")
else:
    print("不合格", end="")