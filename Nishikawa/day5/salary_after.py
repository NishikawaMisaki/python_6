import sys
args=sys.argv

#引数を変数salaryに代入
salary = int(args[1])

#給与100万円未満は税額10%、100万円超過分は税額20％で税額計算
if salary <= 1000000:
    tax=round(salary*0.1)
else:
    tax=round((salary-1000000)*0.2+100000)

#支給額=給与-税額
pay=salary-tax

#支給額と税額の出力
print("支給額:" + str(pay) + "、税額:" + str(tax), end="")