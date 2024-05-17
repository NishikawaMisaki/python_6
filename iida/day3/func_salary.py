def func_salary(salary):
    if salary > 1000000:
        tax = round((salary -1000000) * 0.2 + 100000)
    else:
        tax = round(salary * 0.1)
    pay = salary - tax
        
    return pay, tax