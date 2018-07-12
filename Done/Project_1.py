#解方程式
import math
def quadratic(a, b, c):
    if (b * b - 4 * a * c) < 0:
        return 'None'
    Delte = math.sqrt(b * b - 4 * a * c)
    if Delte > 0:
        x = (- b + Delte) / (2 * a)
        y = (- b - Delte) / (2 * a)
        return x, y
    else:
        x = (- b) / (2 * a)
        return x
print(quadratic(1,2,-63))

#尋找質數
print("1 is not a prime number")
for n in range(2,100):
    for x in range(2,n):
        if n % x == 0:
            print(n ,'is not a prime number')
            break
    else:
        print(n ,'is a prime number')
#猜數字
print ('Hello')

from random import randint
x = randint(1,100)
    
while True:

    y = input("Plz type in an integer:")
    if y == "stop":
        break
    y = int(y)
    if x<y:
        print("Too big")
    if x>y:
        print("Too small")
    if x == y:
        print("Correct!")
        break

#座標象限
def elephant(a,b):
    if a>0 and b>0:
        return "第一象限"
    elif a<0 and b>0:
        return "第二象限"
    elif a<0 and b<0:
        return "第三象限"
    else:
        return "第四象限"
    
print(elephant(-1,-10))
print(elephant(5,-5))
print(elephant(1,1))
print(elephant(-2,3))


#直角三角形
size = int(input("Type in the size of the Right triangle:" ))

i = 1
while i <= size:        
    j = 1
    while j <=size+1-i:     
        print("*",end="")
        j +=1
    print("")                  
    i +=1

