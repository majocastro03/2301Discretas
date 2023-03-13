P = [True, False] 

print('x\ty\t x -> y')
print('-'*30)
for x in P:
    for y in P:
        print(x, y, ( ( x and not y) or (y or not x)) and ((not y and x) or ( not x or  y)),'\t')  

result = []

for x in P:
    for y in P:
        result.append(( ( x and not y) or (y or not x)) and ((not y and x) or ( not x or  y)))
        
print (result)   

if True in result:
     print("La preposicion es una tautologia")
else:
     print("No es una tautologia")

