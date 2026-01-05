even=[2,4,6,8]
odd=[1,3,5,7,9]
print('List of even numbers',even)
print('List odd numbers',odd)
print('Minimum number in even list is',min(even))
print('Maximum number in odd lists is',max(odd))
even.extend(odd)
print('Combining even and odd list',even)
even.sort()
print('Sorted list',even)
even.sort(reverse=True)
print('Reverse sorted list',even)
sorted_list=sorted(even)
print(sorted_list)
pangram='The quick brown fox jumps over the lazy dog'
sorted_pangram=sorted(pangram)
print(sorted_pangram)

names=["John Snow",
       "denereyas Targerian",
       "Gregor clegane",
       "Rob Stark",
       "Joffrey Barrathina",
       "Viserian"]
sorted_names= sorted(names, key=str.casefold)# key=casefold() convert the string into lowercase for caseless comparison
print(sorted_names)

digits = sorted("43238765678")
print(digits)