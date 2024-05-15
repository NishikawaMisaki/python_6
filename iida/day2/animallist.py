import sys
args = sys.argv

i = int(args[1])
animal = args[2]
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animals.insert(i, animal)

animals.pop()

animals.sort()

print(animals, end="")