# Day 5 – Loops
# Print the multiplication table of a number.
# Print all even numbers from 1 to 50.
# Find the sum of first 10 natural numbers.
# Print the Fibonacci series up to n terms.
# Print this pattern:

# num1=int(input('Enter the number for multiplication table'))
# count=1
# while count<=10:
#     print(f'{num1} * {count} = ', num1*count)
#     count+=1

print('Printing all even numbers from 1 to 50')

i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1
for num in range(1,51):
    if num%2==0:
        print(num)
for j in range(2,51,2):
    print(j)

print('Finding sum of first 10 natural numbers')
m=1
total=0
while m<=10:
    total+=m
    m+=1
print(total)

total2=0
for i in range(1,11):
    total2+=i
print(total2)

print(sum(range(1,11)))