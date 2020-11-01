def func2():
    x = 1
    y = 2
    z = 3
    t = yield x
    yield y + z + t

f2 = func2()
print f2.next()
print f2.send(4)
