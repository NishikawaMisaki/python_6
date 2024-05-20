from decimal import Decimal, ROUND_HALF_UP
import func_sarary
import sys
args = sys.argv

salary = int(args[1])


print("給与:"+str(salary)+"、"+"支給額:"+str(func_sarary.return_saraly(salary)[0])+"、"+"税額:"+str(func_sarary.return_saraly(salary)[1]))

