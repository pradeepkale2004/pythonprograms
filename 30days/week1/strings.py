# Day 3 – Strings
# Input a string and print it in reverse.
# Count vowels in a string.
# Take two strings and print them concatenated.
# Check if a string is a palindrome (e.g., madam).
# from itertools import count

# from test.string import last_name

# str1=input('Enter a string')
# reve=str1[::-1]
# print(reve)
# reversed_string=""
# for char in str1:
#     reversed_string=char+reversed_string
# print(reversed_string)

# string=input('Enter the String to count the vowels')
# counter=0
# for char in string:
#     if char=='a'or char=='e'or char=='i'or char=='o'or char=='u'or char=='A'or char=='E'or char=='I'or char=='O'or char=='U':
#         counter+=1
# print(counter)
#
# string = input('Enter the String to count the vowels')
# vowels = 'aeiouAEIOU'
# counter = 0
# for char in string:
#     if char in vowels:
#         counter += 1
# print(counter)

# first_name=input('Enter the first name')
# last_name=input('Enter the last name')
# full_name=first_name+" "+last_name
# print(full_name)

string_palindrome=input('Enter the string to check if String is palindrome or not')
reversed_string=string_palindrome[::-1]
if string_palindrome==reversed_string:
    print('String is palindrome')
else:
    print('String is not palindrome')