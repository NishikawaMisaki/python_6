#Clear!! Mission No6 丁？半？
import sys
args = sys.argv

def judge_odd_or_even(x):
    if x % 2 == 0:
        print("偶数",end="")
    else:
        print("奇数",end="")

num = int(args[1])
#num2 = int(args[2])

judge_odd_or_even(num)
#judge_odd_or_even(num2)