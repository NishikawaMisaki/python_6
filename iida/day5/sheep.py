import sys
args = sys.argv

num = int(args[1])

with open("sheep.txt", mode="w", encoding="utf-8") as f:
    for i in range(1,num):
        f.write("ひつじが{}匹\n".format(i))
    f.write("ひつじが{}匹".format(num))