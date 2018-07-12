def way(n):
    def km(x):
        return n*x
    return km
bus=way(0.03)
car=way(0.24)
scoo=way(0.06)
print("Bus",bus(100),"kg/km")
print("Car",car(100),"kg/km")
print("Scooter",scoo(100),"kg/km")