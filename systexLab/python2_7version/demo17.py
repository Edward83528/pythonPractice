list1 = list("ABCDEFG1234567abcdefg7654321")
list1[::2] = '*'*len(list1[::2])
print list1

l2 = ['A','B','C','D','E']
l3 = ['a','b','c','d','e']
l2.append(l3)
print l2
l4 = ['A','B','C','D','E']
l5 = ['a','b','c','d','e']
l4.extend(l5)
print l4
l6 = ['A','B','C','D','E']
l7 = ['a','b','c','d','e']
l6 += l7
print l6
l8 = list('qwertyuiopasdfghjklzxvbnm')
l8.sort()
print l8
l9 = list('qwertyuiopasdfgklzxcnmQWERTYUIOPASDFGHJKLZXCVBNM')
l9.sort()
print l9

