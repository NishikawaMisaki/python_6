#Mission 無限ループって怖くね？
import sys
args = sys.argv

num = int(args[1])
flag = False
sum = 0

while flag == False :
    sum += num
    if sum == 100 :
        print('Just 100!',end="")
        flag = True
    if sum > 100 :
        print("Over!",end="")
        flag = True
