def calcsalary(salary):
    if salary <= 1000000:
        tax=round(salary*0.1)
    else:
        tax=round((salary-1000000)*0.2+100000)
    pay=salary-tax
    return pay,tax