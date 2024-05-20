# functions.py

def function1():
    print("Function 1 is called")

def function2():
    print("Function 2 is called")

def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")