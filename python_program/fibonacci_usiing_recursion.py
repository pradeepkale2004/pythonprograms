def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_numbers(n):
    ans = []
    for i in range(1,n+1):
        ans.append(fibonacci(i))
    return ans
print(fibonacci_numbers(5))