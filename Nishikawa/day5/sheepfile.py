import sys
args=sys.argv

a = int(args[1])

with open("sheep.txt", mode="w", encoding="utf-8")as s:
    for a in range(1,a):
        s.write("ひつじが"+str(a)+"匹\n")
    s.write("ひつじが"+str(a+1)+"匹")