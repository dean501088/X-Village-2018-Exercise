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