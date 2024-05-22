#Mission 眠れない夜は...2

import sys
args = sys.argv
sheep = int(args[1])
# ファイルを書き込みモードで開く
with open('sheep.txt', 'w') as f:
    for i in range(sheep):        
        f.write("ひつじが"+str(i+1)+"匹\n")       # ファイルに書き込む



