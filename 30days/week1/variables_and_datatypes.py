# ⭐ Day 2 – Variables & Data Types
# Write a program to swap two numbers.
# Take radius from the user and print the area of a circle.
# Convert temperature from Celsius to Fahrenheit.
# Take an integer and print if it’s positive, negative, or zero.
import math

a=10
b=20
print(f'before swapping a={a} and b={b}')
c=a
a=b
b=c
print(f'After 1st swapping a={a} and b={b}')
a=a+b
b=a-b
a=a-b
print(f'After 2nd swapping a={a} and b={b}')
a,b=b,a
print(f'After 3rd swapping a={a} and b={b}')

radius=int(input('Enter the radius of circle'))
area=math.pi*(radius**2)
print(area)

temp=float(input('Enter temperature in celcius'))
fah=(temp * 9/5) + 32
print(f'Temperature in {temp} celsius is {fah} in fahrenheit')
celsius = (fah - 32) * 5/9
print(f'Temperature in {fah} fahrenheit is {celsius} in celsius')

number=int(input('Enter a number to check if positive negative or zero'))
if number>0:
    print('Number is positive')
elif number<0:
    print('Number is Negative')
else:
    print('Number is Zero')