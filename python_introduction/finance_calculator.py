monthly_income = float(input("Enter Your Monthly Income"))

monthly_expenses = float(input("Enter your monthly expenses"))

monthly_savings = monthly_income - monthly_expenses

interest_rate = 0.05

annual_savings = monthly_savings * 12

projected_savings = annual_savings + (annual_savings * interest_rate)

print(f"Projected savings after one year,{annual_savings} with interest, is:{projected_savings}")
