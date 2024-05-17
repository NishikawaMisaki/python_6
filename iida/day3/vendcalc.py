
menu = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}







for i in menu:
    print("{}：{} 円".format(i,menu[i]))

while True:
    money = int(input("投入金額を入力してください"))
    if money >= 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        continue;
    if money < 100:
        print("{}園では購入できる商品がありません。再度投入金額を入力してください".format(money))
        continue;
    if money % 10!= 0:
        print("１円玉、５円玉は使用できません。再度投入金額を入力してください")
        continue;
    break;



while True:
    try:
        what = input("何を購入しますか（商品名/cancel）")
        money -= menu[what]
        
        print("残金：{}円".format(money))
        if money == 0:
            break;
        elif money < 100:
            break;
        
        which = input("続けて購入しますか（Y/N）")
        if which == "Y":
            for i in menu:
                print("{}：{} 円".format(i,menu[i]))
            continue;
        elif which == "N":
            break;
    except:
        print("その商品は存在しません。再度商品名を入力してください")

def oturi(money):
    value = [5000, 1000, 500, 100, 50, 10]
    print("おつり")