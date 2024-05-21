import sys
args = sys.argv
la = args[1]
la_numb = int(args[2])
s = la
s = s.split()
print(s[la_numb - 1], end="")