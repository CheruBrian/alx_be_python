#pront user about finance 
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

#calulate monthly savings
monthly_savings = income - expenses

#Project annual savings with 5% intrest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

#display
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
