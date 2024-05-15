import sys
args = sys.argv
number = int(args[1])
ani_name = args[2]
ani = ["giraffe", "tiger", "zebra", "elephant", "lion"]
ani.insert(number,args[2])
del ani[5]
ani.sort()
print(ani, end="")