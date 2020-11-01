x = 5
print x, hex(id(x))
x = 6
print x, hex(id(x))
l1 = [5]
print l1[0], hex(id(l1)), hex(id(l1[0]))
l1[0] = 6
print l1[0], hex(id(l1)), hex(id(l1[0]))


class Person:
    def __init__(self, age):
        self.age = age
        pass

    pass
p1 = Person(5)

print p1.age, hex(id(p1)), hex(id(p1.age))
p1.age = 6
print p1.age, hex(id(p1)), hex(id(p1.age))