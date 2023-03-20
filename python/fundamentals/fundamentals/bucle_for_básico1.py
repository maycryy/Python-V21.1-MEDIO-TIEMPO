for i in range(150):
    print(i)
    
for i in range(5, 1001):
    if i % 5 ==0:
        print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print (i)

suma= 0
for i in range(1, 500001, 2):
    suma += i 

print(suma)

num = 2018
while num > 0:
    print(num)
    num -= 4

lowhNum = 2
highNum= 9
mult= 3
for i in range(lowhNum, highNum + 1):
    if i % mult == 0:
        print(i)
