import random
import string


def encoding(name):
    chars = string.ascii_letters + string.digits
    result = ''.join(random.choices(chars, k=3))
    f=name[0]
    name= name.replace(name[0],'')
    name = name + f
    print(name)

encoding('Pradeep')