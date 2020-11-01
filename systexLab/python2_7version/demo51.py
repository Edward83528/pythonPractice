import requests

base_url = 'https://ntudemo2019.firebaseio.com/%s.json'

r1 = requests.delete(base_url % 'demo1')
r2 = requests.delete(base_url % 'demo2')
r3 = requests.delete(base_url % 'demo3')
r4 = requests.delete(base_url % 'demo4')
r5 = requests.delete(base_url % 'demo5')
r6 = requests.delete(base_url % 'demo6')