import sys
args = sys.argv

string = args[1]
number = int(args[2])

string_list = string.split()

print(string_list[number-1],end="")