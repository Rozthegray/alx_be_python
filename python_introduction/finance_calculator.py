monthly_income = float(input("Enter Your Monthly Income"))

monthly_expenses = float(input("Enter your monthly expenses"))

monthly_savings = monthly_income - monthly_expenses

interest_rate = 0.05

yearly_savings = monthly_savings * 12

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

print(f"Projected savings after one year,{yearly_savings} with interest, is:{projected_savings}")
