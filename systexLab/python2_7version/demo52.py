file1 = open('data\\Python_Introduction')
data1 = file1.read()
file1.close()
print len(data1), type(data1), data1[:50]
with open('data\\Python_Introduction') as file2:
    data2 = file2.read().decode('UTF-8')

print len(data2), type(data2), data2[:50]

file3 = open('data\\clone1','w')
file3.write(data1)
file3.close()
with open('data\\clone2', 'w') as file4:
    file4.write(data2.encode('UTF-8'))
