number="9,223;372:036 854,777;887"
separator=""

for char in number:
    if not char.isnumeric():
        separator=separator+char

print(separator)