# Program to calculate employee's gross and net pay
gross_pay = float(input("Enter gross pay: $"))
tax_rate = 0.20
tax_amount = gross_pay * tax_rate
net_pay = gross_pay - tax_amount

print(f"Gross Pay: ${gross_pay:.2f}")
print(f"Tax (20%): ${tax_amount:.2f}")
print(f"Net Pay: ${net_pay:.2f}")