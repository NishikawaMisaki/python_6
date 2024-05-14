import sys
args = sys.argv
M = int(args[1])
J = int(args[2])
E = int(args[3])
if ((M>=70)and(J>=70)and(E>=70)) or ((M+J+E)>=220) and ((M>=50)and(J>=50)and(E>=50)):
    print("合格", end="")
else:
    print("不合格", end="")

