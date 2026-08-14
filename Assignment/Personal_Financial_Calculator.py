# Personal Financial Calculator

# income details
print('income details')
print()
name = input('Enter your name: ')
salary = int(input('Enter your salary: '))
bonus = int(input('Enter your bonus: '))
side_income = int(input('Enter your side income: '))
print()
print('Name : ',name)
print('Salary : ',salary)
print('Annual Bonus : ',bonus)
print('Side Income : ',side_income)
print()

# expense details
print('expense details')
print()
rent = int(input('Enter your rent expense: '))
food = int(input('Enter your food expense: '))
transport = int(input('Enter your transport expense: '))
utilities = int(input('Enter your utilities expense: '))
entertainment = int(input('Enter your entertainment expense: '))
print()
print('Monthly rent : ',rent)
print('Monthly food : ',food)
print('Monthly transport : ',transport)
print('Monthly Utilities : ',utilities)
print('Monthly entertainment : ',entertainment)
print()


#  savings_goal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
print('savings_goal')
print()

current_savings = int(input('Enter your current savings: '))
target_savings = int(input('Enter your target savings: '))
goal_month = int(input('Enter your goal month: '))

print('Current Savings : ',current_savings)
print('Target Saving : ',target_savings)
print('Goal Month : ',goal_month)
print()

# monthly calculation
monthly_income = salary + side_income
monthly_expense = rent + food + transport + utilities + entertainment
monthly_bonus = side_income
monthly_saving = monthly_income - monthly_expense
print('Monthly Income : ',monthly_income)
print('Monthly expense : ',monthly_expense)
print('Monthly Bonus : ',monthly_bonus)
print('Monthly Savings : ',monthly_saving)
print()

# annual calculation
annual_income = monthly_income * 12 + bonus
annual_expense = monthly_expense * 12
annual_bonus = monthly_bonus * 12
print('Annual income : ',annual_income)
print('Annual Expense : ',annual_expense)
print('Annual Bonus : ',annual_bonus)
print()

# percentage
overall_expense_percentage = (monthly_expense/monthly_income) * 100
print('overall_expense_percentage : ',overall_expense_percentage ,'%')

rent_percentage = (rent/monthly_income) * 100
print('rent_percentage : ',rent_percentage ,'%')

food_percentage = (food/monthly_income) * 100
print('food_percentage : ',food_percentage ,'%')

transport_percentage = (transport/monthly_income) * 100
print('transport_percentage : ',transport_percentage , '%')

utilities_percentage = (utilities/monthly_income) * 100
print('utilities_percentage : ',utilities_percentage , '%')

entertainment_percentage = (entertainment/monthly_income) * 100
print('entertainment_percentage : ',entertainment_percentage , '%')
print()


savings_gap = target_savings - current_savings
print('savings_gap : ',savings_gap)
required_month = savings_gap / monthly_saving 
print('required_month : ',required_month)
estimated_month = round(required_month)
print('estimated_month : ' ,estimated_month , 'months') 