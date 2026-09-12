def count_sheep(n):
    i=1
    if n==0:
        print("")
    else:
        while i!=n+1:
            print(f'{i} sheep...',end ='')
            i+=1

count_sheep(3)
# 1 sheep...2 sheep...3 sheep...