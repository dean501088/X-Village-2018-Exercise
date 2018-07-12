def sala(x,y):
    
    if x>90:
        print(8000+200*y)
    elif 70<x<90:
        print(6000+200*y)
    elif x<70:
        print(4000+200*y)
    
    return""
    
print(sala(55,14))
print(sala(96,13))
print(sala(85,22))