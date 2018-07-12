from random import randint
x = randint(1,100)
print(x)   
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