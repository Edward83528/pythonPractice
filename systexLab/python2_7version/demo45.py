import requests
import bs4

url1 = 'https://www.mobile01.com/'
headers = {
    'User-Agent': 'iPhoneXXSS',
    'From': 'google'
}
result1 = requests.get(url1, headers=headers)
# print result1.status_code, result1.content
soup1 = bs4.BeautifulSoup(result1.content, "html.parser")
print soup1.title
posts = soup1.find('div', {"id": 'hot-posts'})
post_links = posts.find_all("a")
for p in post_links:
    print p

# url2 = 'https://www.mobile01.com/category.php?id=4'
# url3 = 'https://www.mobile01.com/category.php?id=5'
# url4 = 'https://www.mobile01.com/category.php?id=6'
ids = [4, 5, 6]
base_url = 'https://www.mobile01.com/category.php?id=%d'
for id in ids:
    url = base_url % id
    result1 = requests.get(url, headers=headers)
    # print result1.status_code, result1.content
    soup1 = bs4.BeautifulSoup(result1.content, "html.parser")
    print soup1.title
    posts = soup1.find('div', {"id": 'hot-posts'})
    post_links = posts.find_all("a")
    for p in post_links:
        print p

