
min_price = 100
max_price = 10000

#############################      処理１　   ############################################

drink_list = { "お茶": 110, "コーヒー" : 100,"ソーダ" : 160, "コーンポタージュ": 130}

for drink, price in drink_list.items():
    print(drink + ":" + str(price)+"円")


#############################      処理2,3,4,5　   ############################################

your_money = input("投入金額を設定してください\n")

while True:

    last_digit = your_money % 10

    if your_money >= min_price :
        #print("何を購入しますか（商品名/cancel）")
        break

    if your_money > max_price:
        print("10,000円を超える金額は投入できません。")
        your_money = input("再度投入金額を設定してください\n")

    if your_money < min_price:
        print(str(your_money)+"円では購入できる商品がありません。")
        your_money = input("再度投入金額を設定してください\n")

    if last_digit == 1 and last_digit == 5:
        print("1円玉、5円玉は使用できません。")
        your_money = input("再度投入金額を設定してください\n")

print("何を購入しますか（商品名/cancel）\n")

#############################      処理6　   ############################################

while True:
    item = input()

    if item in drink_list:
        your_money -= drink_list[item]
        print("残金"+str(your_money)+"円\n")
        judge = input("続けて購入しますか（Y/N）")

        if judge == 'Y':
            print("何を購入しますか（商品名/cancel）\n")

        if judge == 'N':
            c_5000 = your_money % 5000
            your_money -= 5000  * c_5000

            c_2000 = your_money % 2000
            your_money -= 2000 * c_2000

            c_1000 = your_money % 1000
            your_money -= 1000 * c_1000

            c_500 = your_money % 500
            your_money -= 500 * c_500

            c_100 = your_money % 100
            your_money -= 100 * c_100

            c_50 = your_money % 50
            your_money -= 50 * c_50

            c_10 = your_money % 10
            your_money -= 10 * c_10

            c_5 = your_money % 5
            your_money -= 5 * c_5

            c_1 = your_money % 1
            your_money -= 1 * c_1

            print("おつり")
            break

        else:
            print("error! お釣りを払い出します")
            break
    else:
        print(str(item)+"は飲み物は商品に存在しません\n") 
        print("何を購入しますか（商品名/cancel）\n")
        continue





    


