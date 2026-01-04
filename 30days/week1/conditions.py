# Day 4 – Conditions
# Take marks and print grade:
# ≥90 → A
# ≥80 → B
# ≥70 → C
# else → Fail
# Check if a person is eligible to vote (age ≥ 18).
# Find the largest of three numbers.
# Check if a year is a leap year.
from numpy.random import permutation

# marks=int(input('Enter the marks to check grade'))
# if marks>=90:
#     print('A')
# elif marks>=80:
#     print('B')
# elif marks>=70:
#     print('C')
# else:print('fail')
#
# # Check if a person is eligible to vote (age ≥ 18).
# age=int(input('Enter the age to check if eligible for voting or not'))
# if age>=18:
#     print('Eligible for voting')
# else:
#     print('age below 18 not eligible for voting')

# Find the largest of three numbers.
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))

if first_number >= second_number and first_number >= third_number:
    print(f'Largest number is {first_number}')
elif second_number >= first_number and second_number >= third_number:
    print(f'Largest number is {second_number}')
else:
    print(f'Largest number is {third_number}')
print('Largest number is',max(first_number,second_number,third_number))

year =int(input('Enter the year to check if leap year or not'))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f'{year} is leap year')
else:
    print(f'{year} is non leap year')