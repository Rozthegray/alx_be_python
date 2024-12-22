monthly_income = int(input("Enter Your Monthly Income"))

monthly_expenses = int(input("Enter your monthly savings"))

monthly_savings = monthly_income - monthly_expenses

yearly_savings = monthly_savings * 12

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Projected savings after one year,{yearly_savings} with interest, is:{projected_savings}")
