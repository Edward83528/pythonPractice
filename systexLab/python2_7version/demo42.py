# encoding=UTF-8
import json

list1 = ['apple', 100, 3.14, True, False, None, 'end']
result1 = json.dumps(list1)
print result1
dict1 = {'name': "BDPY", "duration": 35, "location": '台中'}
result2 = json.dumps(dict1)
print result2

print type(result1), type(result2)
return1 = json.loads(result1)
print type(return1)
for x in return1:
    print x

return2 = json.loads(result2)
print type(return2)
for k, v in return2.items():
    print "k=", k, ", v=", v
