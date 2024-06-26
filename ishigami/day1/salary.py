from decimal import Decimal, ROUND_HALF_UP

import sys
args = sys.argv

salary = int(args[1])


if salary >= 1000000:#給料が100万円を超える場合
    over_million = salary - 1000000 #100万を超える部分を計算
    over_tax = over_million * 0.2 + 100000
    over_tax = Decimal(str(over_tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    salary = salary - over_tax
    print("支給額:"+str(salary)+"、"+"税額:"+str(over_tax),end="")
    
else:               #給料が100万円以下の場合
    tax = salary * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    salary = salary - tax
    print("支給額:"+str(salary)+"、"+"税額:"+str(tax),end="")