#Print numbers from 1 to 100
# count =1
# while count <=100:
#     print(count)
#     count+=1
#
# #print numbers from 100 to 1
# count1=100
# while count1 >=1:
#     print(count1)
#     count1-=1

#print the multiplication table of number n
# num1=int(input('Enter the number for multiplication table'))
# n1=1
# while n1<=10:
#     m1=num1*n1
#     print(m1)
#     n1+=1

#printing the list of elements
# nums= [1,4,9,16,25,36,49,64,81,100]
# index=0
# while index < len (nums):
#     print(nums[index])
#     index+=1

#Search for number x in given tuple
tupl= (1,4,9,16,25,36,49,64,81,100)
ele=int (input('Enter the number to search'))
indx=0
i=1
while indx< len(tupl):
    if tupl[indx]==ele:
        print(f'Element {ele} found at {indx} position')
    else:
        i=0
    indx+=1
if i==0:
    print('Element not Found')

