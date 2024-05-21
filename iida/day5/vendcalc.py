
menu = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}


def oturi(money):
    '''金額を入力したらお釣りを表示する関数'''
    value = [5000, 2000, 1000, 500, 100, 50, 10]
    count = []
    aa = ["円札", "円札", "円札", "円玉", "円玉", "円玉", "円玉"]
    i = 0
    print("おつり")
    for v  in value:
        while True:
            if money/v >= 1:
                i += 1
                money -= v
            else:
                count.append(i)
                i = 0
                break
    for (v,c, a) in zip(value, count, aa):
        if c == 0:
            continue
        print("{}{}：{}枚".format(v, a, c))



def menu_print():
    '''メニューを表示する関数'''
    for i in menu:
        print("{}：{} 円".format(i,menu[i]))


menu_print()

while True:
    money = int(input("投入金額を入力してください"))
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        continue;
    if money < 100:
        print("{}円では購入できる商品がありません。再度投入金額を入力してください".format(money))
        continue;
    if money % 10!= 0:
        print("１円玉、５円玉は使用できません。再度投入金額を入力してください")
        continue;
    break;



while True:
    try:
        what = input("何を購入しますか（商品名/cancel）")
        
        # キャンセルの場合はお釣りを表示し処理を終了
        if what == "cancel":
            oturi()
            break;
        
        # 商品を買うお金が足りなかった場合
        if money < menu[what]:
            print("その商品は金額が足りません")
            while True:
                which = input("続けて購入しますか（Y/N）")
                if not(which == "Y" or which == "N"):
                    print("Y/Nを入力してください")
                else:
                    break;
        # 商品を買うお金がない場合、続けて買うか辞めるかを選択
        if which == "Y":
            menu_print()
            continue;
        elif which == "N":
            oturi(money)
            break;
        
        # 商品を買い、所持金額を更新
        money -= menu[what]
        
        # 0円の場合、買う商品がない場合は処理を終了する
        if money == 0:
            break;
        elif money < 100:
            oturi(money)
            break;
        
        # 残金がある場合は残金を表示し、続けて商品を購入するか確認する
        print("残金：{}円".format(money))
        while True:
            which = input("続けて購入しますか（Y/N）")
            if not(which == "Y" or which == "N"):
                print("Y/Nを入力してください")
            else:
                break;
        
        # 商品を買う場合はもう一度ループし、買わない場合はお釣りを表示し処理を終了する
        if which == "Y":
            menu_print()
            continue;
        elif which == "N":
            oturi(money)
            break;
     
    except:
        print("その商品は存在しません。再度商品名を入力してください")