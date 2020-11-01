# encoding=UTF-8
import requests

base_url = 'https://ntudemo2019.firebaseio.com/%s.json'

r1 = requests.put(base_url % 'demo1', json='hello world using python')
print r1.content, r1.status_code

r2 = requests.put(base_url % 'demo2', json='中文內容')
print r2.content, r2.status_code

r3 = requests.put(base_url % 'demo3', json=u'中文內容')
print r3.content, r3.status_code

r4 = requests.put(base_url % 'demo4', json=['hi', 'welcome', '你好', None, '完成'])
print r4.content, r4.status_code

r5 = requests.put(base_url % 'demo5', json={'name': 'bdpy', 'duration': 35, 'level': 'intermediate'})
print r5.content, r5.status_code
