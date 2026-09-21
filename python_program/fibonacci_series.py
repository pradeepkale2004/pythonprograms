#Python program to return the fibonacci series of number n
def print_fibonacci(n):
    if n<=0:
        print("Please enter a positive integer")
        return
    a=0
    b=1
    print(f'Fibonacci series up to {n} terms')

    for _ in range(n):
        print(a, end=' ')
        a ,b =b,a+b
    print()
try:
    terms =int(input('Enter the number of terms'))
    print_fibonacci(terms)
except ValueError:
    print('Invalid input, Please Enter the valid intput')