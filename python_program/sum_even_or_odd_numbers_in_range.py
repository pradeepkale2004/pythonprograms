def sum_even_odd(n, t):
    if t=='e':
        start=2
    elif t=='o':
        start=1
    else:
        return -1
    return sum(range(start,n,2))


t=input('Enter e or o for even or odd sum')
n=int(input('Enter the range for calculating the sum'))

x=sum_even_odd(10,'e')
print(x)

y=sum_even_odd(n,t)
print(y)