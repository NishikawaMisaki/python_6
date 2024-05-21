import datetime
import sys
args = sys.argv
date = args[1]
n_a = int(args[2])
n_c = int(args[3])

t1 = datetime.date(int(date[0:4]),int(date[4:6]),int(date[6:8]))

if t1.strftime("%w") == 0 or t1.strftime("%w") == 6:
 price = (2000 * n_a) + (1200 * n_c)
 print(price, end="")

else:
 price = (2400 * n_a) + (1500 * n_c)
 print(price, end="")

 
 
