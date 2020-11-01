def func1():
    a = 1
    b = 2
    yield a
    a += b
    yield a
    a += b
    yield a


f1 = func1()
print type(f1), f1
print f1.next()
print f1.next()

print func1().next()
print func1().next()
print func1().next()

f2 = func1()
for p in f2:
    print p,
