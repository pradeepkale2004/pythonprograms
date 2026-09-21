vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster' : 'Triumph Street Triple'
}
vehicles['startfighter'] = "Lockheed f104"
vehicles['learjet'] = "Bombardier Lererjet 75"
vehicles['toy'] = "glider"

vehicles ['virago'] = "Yamaha XV535" # Upgrade the Virago

del vehicles["startfighter"] # delete the item

#pop method removes an item from the dictionary and return the value
#if the key doesn't exist, it return whatever you pass for the default instead.
print(vehicles.pop("toy",None))

# for key in vehicles:
#     print(key,vehicles[key], sep=': ')

for key, values in vehicles.items():
    print(key, values, sep=' : ')

# my_car = vehicles['fiesta'] # if key doesn't exist the program will be crash
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5") # if key doesn't exist the program will return none
# print(learner)
#
# honda = vehicles.get('dream')
# print(honda)

# honda1 = vehicles['dream']
# print(honda1)
