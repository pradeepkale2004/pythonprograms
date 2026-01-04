# name='Pradeep'
# age=22
# # print(name+ 'is having age '+ age)
# print(name+ ' is having age ', age)

#string=('we win')
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[3])
# print(string[4])
# print(string[5])
# print(string[0:4])
# print(string[:4])
# print(string[4:])

# for i in range(1, 13):
#     print("no.{:2} is squared {:3} is cubed {:4}".format(i,i**2,i**3))
#   #  print(f"no.{i} is squared {i**2} is cubed {i**3}")
# name=input('Enter the Name')
# age=int(input(f'How old are you {name}'))
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char ,end=' ')