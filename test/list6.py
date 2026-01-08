numbers = (input('Enter three numbers, separated by commas'))
token = numbers.split(',')
int_tokens=[]
for st in token:
    int_tokens.append(int(st))
print(int_tokens)
a,b,c = int_tokens
print(a+b-c)
result=int_tokens[0]+int_tokens[1]-int_tokens[2]
print(result)