import itertools

r1 = itertools.chain(list('ABC'), [1, 2, 3, 4], list('abc'))
print type(r1), r1
l1 = [r for r in r1]
for l in l1:
    print l,
print
for l in l1:
    print l,
print
list1 = ['A', 'B', 'C', 'D', 'E']
r2 = itertools.permutations(list1, 3)
l2 = [r for r in r2]
print len(l2), l2
r3 = itertools.combinations(list1, 3)
l3 = [r for r in r3]
print len(l3), l3
