#https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
def tower_builder(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

(tower_builder(3))
(tower_builder(5))