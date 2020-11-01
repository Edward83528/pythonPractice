# encoding=UTF-8
import requests

base_url = 'https://ntudemo2019.firebaseio.com/%s.json'

r4 = requests.patch(base_url % 'demo4', json={'0':'害','3':'新加入','8':'更多資訊'})
print r4.content, r4.status_code

r5 = requests.patch(base_url % 'demo5', json={'name': 'python for data science', 'duration': 42,
                                              'instructor':'Mark'})
print r5.content, r5.status_code
