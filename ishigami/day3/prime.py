import sys
args = sys.argv

num = int(args[1])
l = []
i = 0
flag = True
list = [2,3,5,7,11,13,17,19]    #素数を格納　19以上の素数を使うとき正しく動きません！ importで完璧なモノデキル？

while flag:
    if num % list[i] == 0:      #listのi番目の素数で割り切れる場合
        num = num / list[i]     #入力値numを、listのi番目の素数で割って更新
        l.append(list[i])       #割った値（素因数）を保存しておく
        
        if num == 1:            #入力値numが1になるまで割り切ったら
            flag = False        #whileループ終了
    
    else:                       #listのi番目の素数で割り切れなくなった時
        i += 1


print(l)                        #出力

