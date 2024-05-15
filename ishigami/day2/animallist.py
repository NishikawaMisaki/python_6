import sys
args = sys.argv

insert_location = int(args[1])
animal_name = args[2]

animal_list = [ "giraffe", "tiger", "zebra", "elephant", "lion"]

animal_list.insert(insert_location,animal_name) #挿入

del animal_list[len(animal_list) - 1] #削除

animal_list.sort() #ソート

print(animal_list,end="")