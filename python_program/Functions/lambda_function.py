fun = lambda x : x*x
num = 10
square = fun(num)
print(f"Square of a given number {num} is",square)

fun2= lambda x,y: x if x>y else y
larger_number = fun2(20,30)
print('Larger number is', larger_number)

fun3 = lambda x,y: x+y
summ = fun3(10,20)
print('Addition of two number is ', summ)

power = int(input("Enter the range of number to calculate the power"))

result = list(map(lambda x: 2**x,range(power+1)))
print(result)

for i in range(len(result)):
    print(f'2^{i} =',result[i])