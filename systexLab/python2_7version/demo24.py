left = ['A', 'K']
right = ['Q', 'J']
p1 = [left, right]
p2 = p1
import copy

p3 = copy.copy(p1)
p4 = copy.deepcopy(p2)
print p1, p2, p3, p4
p1.append('7')
print 'after p1 get 7', p1, p2, p3, p4
p1[0][0] = 'JOKER'
print 'after get JOKER', p1, p2, p3, p4
