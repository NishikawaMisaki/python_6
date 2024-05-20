import sys
args=sys.argv

import datetime

a=args[1]
b=int(args[2])
c=int(args[3])

t=datetime.date(int(a[0:4]),int(a[4:6]),int(a[6:8]))
week=int(t.strftime("%w"))

if week==0 or week==6:
    price= (2400*b)+(1500*c)
    print(price,end="")
else:
    price= (2000*b)+(1200*c)
    print(price,end="")
