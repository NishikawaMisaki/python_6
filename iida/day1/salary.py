import sys

args = sys.argv

salary = int(args[1])

if salary > 1000000:
    tax = round((salary -1000000) * 0.2 + 100000)
else:
    tax = round(salary * 0.1)

pay = salary - tax

print("支給額:{}、税額:{}".format(pay, tax), end="")