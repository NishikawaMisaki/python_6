import sys
args = sys.argv
p1 = int(args[1])
p2 = int(args[2])
p3 = int(args[3])
from func_salary import calcsalary 
print("給与:{0}、支給額:{1}、税額:{2}".format(p1,calcsalary(p1)[0],calcsalary(p1)[1]))
print("給与:{0}、支給額:{1}、税額:{2}".format(p1,calcsalary(p2)[0],calcsalary(p2)[1]))
print("給与:{0}、支給額:{1}、税額:{2}".format(p1,calcsalary(p3)[0],calcsalary(p3)[1]))
 