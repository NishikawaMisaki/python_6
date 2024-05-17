import sys
import func_salary
args = sys.argv
pay_tax = []

for salary in args[1:]:
    pay_tax.append(func_salary.func_salary(int(salary)))


for i in pay_tax:
    print("給与:{}、支給額:{}、税額:{}".format(salary, i[0], i[1]))
