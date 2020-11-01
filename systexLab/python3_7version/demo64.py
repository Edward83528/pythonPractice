class MyClass:
    pass

obj1 = MyClass()

print(type(obj1), type(MyClass), obj1.__class__, obj1.__class__.__bases__)
print(type(obj1)==MyClass)