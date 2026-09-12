import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    square_root = math.sqrt(sq)
    print(square_root)
    if isinstance(square_root, int):
        sq+=1
        return sq*sq
    else:
        return -1

print(find_next_square(121))