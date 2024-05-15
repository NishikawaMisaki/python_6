import sys
args=sys.argv

number = int(args[1])
animal_name = args[2]

animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animal.insert(number,animal_name)

animal.pop()

animal.sort()
print(animal,end="")
