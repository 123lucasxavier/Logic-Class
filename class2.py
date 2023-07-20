#Conditional
#if, elif, else

'''
input first_value
inputr second_value
if first_value > second_value
  print the first value is greater
else
  print the second value is greater 
'''
first_value = input('type the first value: ')
second_value = input('type the second value: ')

if int(first_value) > int(second_value):
  print('The first value is the greater!')
else:
  print('The seconrd value is greater!')