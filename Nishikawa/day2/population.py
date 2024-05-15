import sys
args=sys.argv

a = int(args[1])

population = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(population[a-1],end="")