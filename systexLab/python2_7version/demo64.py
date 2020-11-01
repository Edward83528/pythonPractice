class MyClass:
    pass

obj1 = MyClass()

print type(obj1), type(MyClass), obj1.__class__, obj1.__class__.__bases__
print type(obj1)==MyClass


class MyClass2(object):
    pass

obj2 = MyClass2()

print type(obj2), type(MyClass2), obj2.__class__, obj2.__class__.__bases__
print type(obj2)==MyClass2