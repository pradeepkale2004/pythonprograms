from operator import delitem

menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        [ "spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for index1 ,meal1 in enumerate(menu):
    print(index1,meal1)
for meal2 in menu:
    for index in range (len(meal2)-1,-1,-1):
        if meal2[index]=='spam':
            del(meal2[index])
    print(meal2)

# print('New Menu after deleting spam')
# for index, meal3 in enumerate(menu):
#     print(index, meal3)

for meal4 in menu:
    for item in meal4:
        if item != "spam":
            print(item)
    print()




