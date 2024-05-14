import sys
args = sys.argv

math_v = int(args[1])
jap_v = int(args[2])
eng_v = int(args[3])

if math_v >= 50 and jap_v >= 50 and eng_v >= 50:
    if math_v >= 70 and jap_v >= 70 and eng_v >=70:
        print("合格",end="")
    elif math_v + jap_v + eng_v >= 220:
        print("合格",end="")
    else:
        print("不合格",end="")
else:
    print("不合格",end="")

