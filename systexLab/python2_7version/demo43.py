url1 = 'https://bugzilla.mozilla.org/rest/bug/35'
import requests

r1 = requests.get(url1)
print r1.status_code, r1.headers['content-type']
print type(r1.content), type(r1.json())
bugs = r1.json()["bugs"]
print type(bugs)
firstBug = bugs[0]
print type(firstBug)
ccDetails = firstBug['cc_detail']
for detail in ccDetails:
    print type(detail), detail
    print detail["email"]
