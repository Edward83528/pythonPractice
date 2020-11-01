list1 = ['A', 'B', 'C', 'D', 'E']
list2 = list1
list3 = list1[:]
list4 = list(list1)
print list1, list2, list3, list4
print hex(id(list1)), hex(id(list2)), hex(id(list3)), hex(id(list4))
list1[0] = 'a'
list2[1] = 'b'
print list1, list2, list3, list4
