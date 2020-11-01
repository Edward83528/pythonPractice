# encoding=UTF-8
import requests

base_url = 'https://ntudemo2019.firebaseio.com/%s.json'

r1 = requests.get(base_url % 'demo1')
print r1.content
r2 = requests.get(base_url % 'demo2')
print r2.content
r3 = requests.get(base_url % 'demo3')
print r3.content
r4 = requests.get(base_url % 'demo4')
print r4.content, type(r4.content)
for item in r4.json():
    print item
r5 = requests.get(base_url % 'demo5')
for k, v in r5.json().items():
    print 'k/v=', k, v
print r5.content, type(r5.content)
r6 = requests.get(base_url % 'demo6')
print r6.content
for record in r6.json().values():
    for k, v in record.items():
        print 'k/v=', k, v
