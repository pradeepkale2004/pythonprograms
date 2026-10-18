import itertools
list_1 = [1,2,3,4,5]
list_2 = [10,20,30,40,50]

print(list(itertools.chain(list_1,list_2)))


for i in itertools.cycle(range(1,11)):
    print(i)




