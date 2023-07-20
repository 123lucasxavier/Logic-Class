# Variables

# Numbers
speed_internet = 10
print(speed_internet)

# Boolean Values

# Strings

# How would variables be used in an actual program?
# Problem 1 - Hourly Rate
# Write a program that calculates an employee's hourly rate based on their monthly salary and hours worked per month. 

'''
pseudocode
input monthly_salary
input hours_worked_per_month
hourly_rate = monthly_salary / hours_worked_per_month
print hourly_rate
'''

monthly_salary = input('What is your monthly salary?')
hours_worked_per_month = input('How many hours do you work per month?')
hourly_rate = int(monthly_salary) / int(hours_worked_per_month)
print(hourly_rate)