from functools import reduce

list1 =[1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda x:x*x,list1))
cube = list(map(lambda x:x**3,list1))
print(square)
print(cube)

even = list(filter(lambda x:x%2==0,list1))
odd = list(filter(lambda x:x%2!=0,list1))
print(even)
print(odd)



product = reduce(lambda x, y: x * y, list1)
summation = reduce(lambda x,y:x+y,list1)
print(product)