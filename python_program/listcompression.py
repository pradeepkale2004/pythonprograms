# Great idea—practice is the fastest way to master list comprehensions. Here are progressive questions (easy → advanced). Try solving them using list comprehensions only.
#
# 🟢 Level 1: Basic
# 1. Square numbers
# Given a list of numbers, return a list of their squares.
# 👉 Example: [1, 2, 3] → [1, 4, 9]
from pandas.core.computation.ops import isnumeric


def squarelist(lst1):
    return [x*x for  x in  lst1]
print(squarelist([1, 2, 3]))

# 2. Convert to uppercase
# Convert all strings in a list to uppercase.
# 👉 ["a", "b", "c"] → ["A", "B", "C"]
def upperlist(lst2):
    return[a.upper() for a in lst2 ]
print(upperlist(["a", "b", "c"]))

# 3. Add 10 to each number
# 👉 [1, 2, 3] → [11, 12, 13]
def add10(lst3):
    return[x+10 for x in lst3]
print(add10([1, 2, 3]))
#
# 4. Get string lengths
# 👉 ["hi", "hello"] → [2, 5]
def getlen(lst4):
    return [len(x) for x in lst4]
print(getlen( ["hi", "hello"]))

# 🟡 Level 2: With Conditions
# 5. Even numbers only
# 👉 [1,2,3,4,5] → [2,4]
def evennum(lst5):
    return [x for x in lst5 if x%2==0]
print(evennum([1,2,3,4,5]))

# 6. Odd squares
# 👉 [1,2,3,4] → [1,9]
def oddsquare(lst6):
    return [x*x for x in lst6 if x%2!=0]
print(oddsquare( [1,2,3,4]))
#
# 7. Words longer than 3 letters
# 👉 ["hi","hello","cat"] → ["hello"]
def longerthan3letter(lst7):
    return [str for str in lst7 if len(str)>3]
print(longerthan3letter( ["hi","hello","cat"]))
#
# 8. Remove vowels from string
# 👉 "hello world" → ['h','l','l',' ','w','r','l','d']
def removevowels(lst8):
    lst=list(lst8)
    return [char for char in lst if char not in 'aeiouAEIOU']
print(removevowels("hello world"))
#
# 🟠 Level 3: If-Else
# 9. Replace negatives with 0
# 👉 [1,-2,3,-4] → [1,0,3,0]
def repwi0(lst9):
    return [ 0 if num <0 else num for num in lst9 ]
print(repwi0( [1,-2,3,-4]))
#
# 10. Label numbers as even/odd
# 👉 [1,2,3] → ["odd","even","odd"]
def evenodd(lst):
    return["odd" if num%2==0 else "even" for num in lst]
print(evenodd([1,2,3]))

# 11. Positive → keep, Negative → absolute
# 👉 [1,-2,3,-4] → [1,2,3,4]
def positivekeepnegativeabsolute(lst):
    return [num if num >0 else -num for num in lst]
print(positivekeepnegativeabsolute([1,-2,3,-4]))

#
# 🔵 Level 4: Nested
# 12. Flatten a list
# 👉 [[1,2],[3,4]] → [1,2,3,4]
def flatten_list(lst):
    lst2=[]
    return [num for num in lst]
print(flatten_list([[1,2],[3,4]]))

def flatten_list1(lst):
    lst2=[]
    for x in lst:
        lst2+=x
    return lst2
print(flatten_list1([[1,2],[3,4]]))

def flatten_list2(lst):
    nested_list = [[1, 2], [3, 4]]
    flat_list = [item for sublist in nested_list for item in sublist]
print(flatten_list1([[1,2],[3,4]]))
#
# 13. Multiplication table (1–3)
# 👉 Output: [1,2,3,2,4,6,3,6,9]
def multiplicationtable(f,l):
    print('Multiplication Table')
    lst1=[f*x for x in range(f,l+1)]
    lst1 += [(f+1) * x for x in range(f, l + 1)]
    lst1 += [(f+2) * x for x in range(f, l + 1)]
    return lst1

print(multiplicationtable(1,5))
#
# 14. All pairs
# 👉 [1,2] and ['a','b'] → [(1,'a'),(1,'b'),(2,'a'),(2,'b')]
def allpairs(x,y):
    n=[]
    for i in x:
        for j in y:
            n.append((i,j))
    return n
print(allpairs([1,2] ,['a','b']))

#
# 🔴 Level 5: Advanced
# 15. Remove duplicates
# 👉 [1,2,2,3] → [1,2,3] (without using set)
def removedepli(x):
    for i in x:
        if x.count(i)>1:
            x.remove(i)
    return x
print(removedepli([1,2,2,3,3,3,3]))

#
# 16. Extract digits from string
# 👉 "a1b2c3" → [1,2,3]
def extract_digit(str1):
    lst1=[]
    for i in str1:
        if i.isdigit():
            lst1.append(int(i))
    return lst1
print(extract_digit('a1b2c3d4e5'))
# 17. Matrix transpose
# 👉 [[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]
def matrix_transpose(x):
    for i in range
print(matrix_transpose([[1,2,3],[4,5,6]]))

#
# 18. Filter palindromes
# 👉 ["madam","hello","level"] → ["madam","level"]
#
# ⚡ Challenge (Real Interview Level)
# 19. Flatten + filter even numbers
# 👉 [[1,2,3],[4,5,6]] → [2,4,6]
#
# 20. Create dictionary from list
# 👉 ["a","b","c"] → {'a':1,'b':1,'c':1}
