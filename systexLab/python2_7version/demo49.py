# encoding=UTF-8
import requests

base_url = 'https://ntudemo2019.firebaseio.com/%s.json'

for i in range(0, 10):
    r6 = requests.post(base_url % 'demo6', json={'name': 'MarkHo', 'quantity': 10 + 10 * i})
    print r6.status_code, r6.content
