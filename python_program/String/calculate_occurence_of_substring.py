main_string = input('Enter the main string')
sub_string = input('Enter the sub string to be found')
flag = False
pos =-1
length_of_string = len(main_string)
while True:
    pos = main_string.find(sub_string, pos+1, length_of_string)
    if pos ==-1:
        break

    print(' Sub String found at position :', pos + 1)
    flag = True
if flag == False:
    print('String is not found ')