from datetime import datetime

userName = input('Enter your name:   ')
age = int(input('Enter your age:    '))
years = datetime.today().year 
yearBorn = years - age
print('You were born in the year:  ',yearBorn)

print('You will be 100 years in the year:',yearBorn + 100)