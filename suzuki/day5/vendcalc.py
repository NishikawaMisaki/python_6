kinds = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}
for name in kinds.keys():
    print(name + ":" + str(kinds[name]) + "円")

flag = True
while flag == True:
    money = int(input("投入金額を入力してください"))

if money >= 100:
    buy = input("何を購入しますか（商品名/cancel）")
elif money > 10000:
    print(str(money) + "円では購入できる商品がありません。再度投入金額を入力してください")


