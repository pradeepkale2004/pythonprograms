def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(5))
n = int(input('Enter the number to calculate the fibonacci series'))
if n <1:
    print("Enter the valid number")
else:
    for i in range(n):
        print(fibo(i))