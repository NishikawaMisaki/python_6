import sys
args=sys.argv

#日付を取得するモジュールをインポート
from datetime import date

#引数を変数に代入、日付はyyyymmdd(8桁数字)で入力してもらう
input_date=args[1]
adult=int(args[2])
child=int(args[3])

#引数から日付と曜日を取得、日付は年月日で分解
dt=date(int(input_date[0:4]),int(input_date[4:6]),int(input_date[6:8]))
week=int(input_date.strftime("%w"))

#土日は大人2400円、子供1500円
if week==0 or week==6:
    price= (2400*adult)+(1500*child)

#平日は大人2000円、子供1200円   
else:
    price= (2000*adult)+(1200*child)

#合計金額を出力
print(price,end="")