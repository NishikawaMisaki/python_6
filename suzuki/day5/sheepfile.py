with open("sheep.txt", mode="w",encoding="utf-8") as f:
    import sys
    args = sys.argv
    sh = int(args[1])
    for sh in range(1,sh+1):
        f.write("ひつじが" + str(sh) + "匹\n")
