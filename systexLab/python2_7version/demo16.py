x1 = 'abcde'
x2 = ['a', 'b', 'c', 'd', 'e']
print type(x1), len(x1)
print type(x2), len(x2)
print x1[0], x2[0]
x2[0] = 'A'
print type(x1), len(x1), x1
print type(x2), len(x2), x2
#x1[0] = 'K'
print "finished"
