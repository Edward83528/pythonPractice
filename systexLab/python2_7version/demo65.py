class Car:
    vender = 'Lexus'
    valid = True

c1 = Car()
c2 = Car()
print Car.vender, Car.valid, c1.vender, c1.valid
Car.valid = False
Car.function = True
print Car.valid, c1.valid, c2.valid, Car.function, c1.function, c2.function
c1.color='RED'
c2.speed = 60
print c1.vender, c1.valid, c1.color
print c2.vender, c2.valid, c2.speed
#print c1.speed
