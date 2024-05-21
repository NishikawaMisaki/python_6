from datetime import date
import sys
from tables import Holiday
from database import session

args = sys.argv
date = args[1]
n_a = int(args[2])
n_c = int(args[3])

t1 = date(int(date[0:4]),int(date[4:6]),int(date[6:8]))
holidaylist = session.query(Holiday).all()

flag = False
for i in holidaylist:
    if t1 == holidaylist(i):
      flag = True


if t1.strftime("%w") == 0 or t1.strftime("%w") == 6 or flag == True :
 price = (2000 * n_a) + (1200 * n_c)
 print(price, end="")


else:
 price = (2400 * n_a) + (1500 * n_c)
 print(price, end="")