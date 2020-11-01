l1 = list('APPLE')
t1 = tuple('APPLE')
s1 = set(list('APPLE'))
s2 = {'A', 'P', 'P', 'L', 'E'}
print l1, type(l1)
print t1, type(t1)
print s1, type(s1)
print s2, type(s2)
s3 = set(list('BANANA'))
print s3, type(s3)
print s2 | s3, len(s2 | s3)
print s2 & s3, len(s2 & s3)
print s2 ^ s3, len(s2 ^ s3)
for e in s3:
    s2.add(e)
print s2
# s2.add(s3)
