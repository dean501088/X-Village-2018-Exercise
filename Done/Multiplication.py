def f99(n):

    i = n  
    j = 1  
    while i <= 9:
        while j <= 9:
            print(i, '*', j, '=', i*j, sep='', end=' ')
            j += 1
        print("")
        j = 1
        i += 1
    return ""

print(f99(2)) 