#尋找質數
def prnum(a,b):
    lista=[]
    for n in range(a,b):
        for x in range(2,n):
            if n % x == 0:
                break
        else:
            lista.append(n)
    del lista[0]
    return lista

print(prnum(1,50))