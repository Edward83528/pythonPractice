str1 = "ABCDEFG1234567abcdefg7654321"
print str1[0], str1[len(str1)-1]
print str1[-1], str1[-len(str1)]
print str1[0:5], str1[:5]
print str1[-5:-1], str1[-5:]
str2 = "www.uuu.com.tw"
result3 = str2.split('.')

print '!'.join(result3)