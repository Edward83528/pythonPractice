dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
length = []
for i in dayOfWeek:
    length.append(len(i))
    pass
print length

print [len(day) for day in dayOfWeek]
print [day for day in dayOfWeek if len(day) > 6]

sun, mon, tue, wed, thu, fri, sat = dayOfWeek
print sun, wed, fri
print tue, thu, sat

number_list = [3, 1, 4, 1, 5, 9, 26, 83, 47, 100, 29, 5, 7]
s1 = sorted(e for e in number_list if e > 10)
print s1
s2 = sorted(number_list)
print s2
s3 = sorted((e for e in number_list if e < 40), reverse=True)
print s3
