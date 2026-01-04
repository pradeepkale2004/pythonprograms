for i in range(1,11):
    for j in range(1,11):
        # print(f"{i} * {j}  = ",i*j)
        print(f"{i:>2} * {j:>2}  = {i*j:>3}")#here :>2 and :>3 is used for proper alignment
        #{i:<2} → keeps numbers  right-aligned in 2 spaces
    print("------------")#TODO Remove this 