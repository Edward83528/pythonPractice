import requests
import bs4

url1 = 'https://www.uuu.com.tw/'
r1 = requests.get(url1)
soup = bs4.BeautifulSoup(r1.content, "html.parser")
print soup.title
courses = soup.find('div',{'id':'course_list'})
course_links = courses.find_all('a')
for c in course_links:
    print c
