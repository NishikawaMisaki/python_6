from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv
sa = int(args[1])
if sa<=1000000:
    tax =sa * 0.1
else:
    tax =100000 + (sa-1000000)*0.2
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
pay = sa - tax
print("支給額:" + str(pay) + "、" + "税額:" + str(tax), end="")