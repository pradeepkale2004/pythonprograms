from python_program.guessing_game import get_integer


def sum_even_odd(n, t):
    '''
    Get an integer and string as input and returns the sum of even and odd numbers depending on the parameter
    if t == e it will return the sum of even numbers upto n
    elif t== o it will return the sum of odd numbers upto n
    :param n:gets the value of integer of range for sum of even or odd numbers
    :param t:gets string as parameter as either e or o, e for even and o for odd numbers
    :return: returns the sum of even or odd numbers depending on the parameters
    '''
    if t=='e':
        start=2
    elif t=='o':
        start=1
    else:
        return -1
    return sum(range(start,n,2))

# print(input.__doc__)
# print('*' * 80)
# print(sum_even_odd.__doc__)
# print('*' * 80)
help(sum_even_odd)#prints the dockstring of function

t=input('Enter e or o for even or odd sum')
n=int(input('Enter the range for calculating the sum'))

x=sum_even_odd(10,'e')
print(x)

y=sum_even_odd(n,t)
print(y)