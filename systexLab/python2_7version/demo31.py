def foo(a, b):
    return "[demo31]:a+b=%d" % (a + b)


def bar(c, d):
    return "[demo31]:c*d=%d" % (c * d)


if __name__ == '__main__':
    print "inside demo31:"
    print "foo:", foo(1, 2)
    print "bar:", bar(3, 4)
