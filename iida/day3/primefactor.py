import sys
args = sys.argv

num = int(args[1])
a = []
i = 2

while True:
    if num % i == 0:
        a.append(i)
        num = num / i
    elif num == 1:
        break
    else:
        i += 1

print(a, end="")