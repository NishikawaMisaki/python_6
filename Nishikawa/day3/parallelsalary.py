from func_salary import calcsalary
import sys
args=sys.argv

salary = int(args[1])

print("支給額:"+str(calcsalary(salary)[0])+"税額:"+str(calcsalary(salary)[1]),end="")
