import sys
args = sys.argv

a = args[1]
i = int(args[2])

a = a.split()

print(a[i-1], end="")
