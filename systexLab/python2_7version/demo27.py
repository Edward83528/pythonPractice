l1 = ['Sunday', 'Monday', 'Tuesday']
t1 = ('Sunday', 'Monday', 'Tuesday')
print type(l1), type(t1), len(l1), len(t1)
print[len(e) for e in l1]
print[len(e) for e in t1]
# l1 += 'Wednesday'
print "before add list:", hex(id(l1))
l1.append('Wednesday')
print l1
print "after add list:", hex(id(l1))
print "\n"
print "before add tuple:", hex(id(t1))
t1 += ('Wednesday',)
print t1
print "after add tuple:", hex(id(t1))
s2 = ('Thursday')
t2 = ('Thursday',)
print type(s2), type(t2)
print s2 * 5
print t2 * 5

print len(t1), t1[0], t1[2], t1[3], t1[1]
print 'day' in s2
print 'day' in t2, 'Thursday' in t2

dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def split_head(x):
    return x[0], x[1:]

head, remaining = split_head(dayOfWeek)
print type(remaining), len(remaining), remaining
print type(head), len(head), head
